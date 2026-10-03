"""
Remote Hugging Face Inference API Embeddings for LangChain.

This module provides a pure-cloud, remote embedding implementation that conforms
to LangChain's Embeddings interface. It uses Hugging Face's official InferenceClient,
requiring zero local PyTorch, zero local sentence-transformers, and zero local model files.
It operates cleanly under strict OS environments including Windows Smart App Control.
"""

import os
import time
import logging
from typing import List, Optional
import numpy as np
from langchain_core.embeddings import Embeddings
from huggingface_hub import InferenceClient
from huggingface_hub.errors import HfHubHTTPError

logger = logging.getLogger(__name__)


class HuggingFaceAPIEmbeddings(Embeddings):
    """LangChain-compatible Embeddings implementation using Hugging Face Inference API.

    Attributes:
        model: Hugging Face repository model ID.
        normalize_embeddings: If True, normalizes vectors to unit L2 norm.
        expected_dimension: Expected embedding vector dimension (384 for all-MiniLM-L6-v2).
        max_retries: Maximum number of retries for transient errors or rate limits.
        retry_delay: Initial delay in seconds before retrying.
    """

    def __init__(
        self,
        model: str = "sentence-transformers/all-MiniLM-L6-v2",
        api_token: Optional[str] = None,
        normalize_embeddings: bool = True,
        expected_dimension: Optional[int] = 384,
        max_retries: int = 3,
        retry_delay: float = 2.0,
    ) -> None:
        """Initialize remote Hugging Face API embeddings."""
        self.model = model
        self.normalize_embeddings = normalize_embeddings
        self.expected_dimension = expected_dimension
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        # Automatically find and load .env if token not already present in environment
        token = api_token or os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not token:
            try:
                from dotenv import load_dotenv, find_dotenv
                load_dotenv(find_dotenv(usecwd=True))
                token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")
            except Exception:
                pass

        if not token:
            raise ValueError(
                "Hugging Face API token is required. "
                "Please set the 'HF_TOKEN' environment variable or provide api_token. "
                "Never hardcode secrets in source files."
            )

        self._token = token
        self._client = InferenceClient(token=self._token)

    def __repr__(self) -> str:
        """Mask token in string representations to prevent secret leakage."""
        return (
            f"HuggingFaceAPIEmbeddings(model='{self.model}', "
            f"normalize_embeddings={self.normalize_embeddings}, "
            f"expected_dimension={self.expected_dimension})"
        )

    def _normalize(self, vector: np.ndarray) -> np.ndarray:
        """L2-normalize a 1D vector or 2D array of vectors."""
        if vector.ndim == 1:
            norm = np.linalg.norm(vector)
            return vector / norm if norm > 0 else vector
        norms = np.linalg.norm(vector, axis=1, keepdims=True)
        return np.where(norms > 0, vector / norms, vector)

    def _call_inference_with_retry(self, inputs: List[str] | str) -> np.ndarray:
        """Call Hugging Face feature extraction with retry for rate limits and network issues."""
        last_exception = None

        for attempt in range(1, self.max_retries + 1):
            try:
                raw_response = self._client.feature_extraction(
                    text=inputs,
                    model=self.model,
                )
                arr = np.array(raw_response, dtype=np.float32)
                return arr

            except HfHubHTTPError as http_err:
                status_code = getattr(http_err.response, "status_code", None)
                if status_code in (401, 403):
                    raise PermissionError(
                        f"Authentication failed for Hugging Face API (Status {status_code}). "
                        "Please verify your 'HF_TOKEN' and ensure it has 'Inference API' permissions."
                    ) from http_err
                if status_code == 429:
                    # Rate limit hit: exponential backoff
                    sleep_time = self.retry_delay * (2 ** (attempt - 1))
                    logger.warning(
                        "Rate limit reached (429). Retrying in %.1fs (attempt %d/%d)...",
                        sleep_time,
                        attempt,
                        self.max_retries,
                    )
                    time.sleep(sleep_time)
                    last_exception = http_err
                    continue
                # Other server errors (500, 502, 503, 504)
                if status_code in (500, 502, 503, 504):
                    sleep_time = self.retry_delay * attempt
                    logger.warning(
                        "Hugging Face server temporary error (%d). Retrying in %.1fs...",
                        status_code,
                        sleep_time,
                    )
                    time.sleep(sleep_time)
                    last_exception = http_err
                    continue

                raise RuntimeError(
                    f"Hugging Face API request failed with status {status_code}: {http_err}"
                ) from http_err

            except Exception as exc:
                # Network or connection errors
                sleep_time = self.retry_delay * attempt
                logger.warning(
                    "Network error during Hugging Face inference: %s. Retrying in %.1fs...",
                    exc,
                    sleep_time,
                )
                time.sleep(sleep_time)
                last_exception = exc

        raise ConnectionError(
            f"Failed to obtain embeddings from Hugging Face API after {self.max_retries} attempts: {last_exception}"
        ) from last_exception

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of document chunks using the remote Hugging Face API.

        Args:
            texts: List of document strings to embed.

        Returns:
            List of embedding vectors, each represented as a list of floats.
        """
        if not texts:
            return []

        # Feature extraction for batch
        raw_embeddings = self._call_inference_with_retry(texts)

        # Handle shape: if single string passed as 1-element list or 2D array
        if raw_embeddings.ndim == 1:
            raw_embeddings = np.expand_dims(raw_embeddings, 0)
        elif raw_embeddings.ndim == 3:
            # Some models return [batch, seq_len, dim], pool mean across tokens
            raw_embeddings = np.mean(raw_embeddings, axis=1)

        # Validate dimension
        actual_dim = raw_embeddings.shape[1]
        if self.expected_dimension and actual_dim != self.expected_dimension:
            raise ValueError(
                f"Embedding dimension mismatch: expected {self.expected_dimension}, "
                f"but received {actual_dim} from model '{self.model}'."
            )

        # Apply normalization if enabled
        if self.normalize_embeddings:
            raw_embeddings = self._normalize(raw_embeddings)

        return raw_embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        """Embed a single query string using the exact same remote model.

        Args:
            text: Query string to embed.

        Returns:
            A 1D embedding vector as a list of floats.
        """
        if not text:
            dim = self.expected_dimension or 384
            return [0.0] * dim

        raw_embedding = self._call_inference_with_retry(text)

        # Handle potential 2D or 3D response for single query
        if raw_embedding.ndim == 2:
            raw_embedding = np.mean(raw_embedding, axis=0)
        elif raw_embedding.ndim == 3:
            raw_embedding = np.mean(raw_embedding[0], axis=0)

        # Validate dimension
        actual_dim = len(raw_embedding)
        if self.expected_dimension and actual_dim != self.expected_dimension:
            raise ValueError(
                f"Query embedding dimension mismatch: expected {self.expected_dimension}, "
                f"but received {actual_dim} from model '{self.model}'."
            )

        if self.normalize_embeddings:
            raw_embedding = self._normalize(raw_embedding)

        return raw_embedding.tolist()

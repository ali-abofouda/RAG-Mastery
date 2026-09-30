"""
RAG Mastery Shared Core Library (rag_core).

Provides unified utilities, remote embeddings, and system configuration
shared across all curriculum stages and production capstone modules.
"""

from .config import load_rag_environment, get_project_root
from .embeddings import HuggingFaceAPIEmbeddings

__all__ = [
    "HuggingFaceAPIEmbeddings",
    "load_rag_environment",
    "get_project_root",
]

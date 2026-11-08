# Hypothetical Document Embeddings (HyDE) Reference Implementation (Stage 06 - Lecture 52)

## Architectural Overview

Hypothetical Document Embeddings (HyDE) is a pre-retrieval query transformation technique that resolves the asymmetric retrieval bottleneck in vector search. Traditional dense retrieval computes vector similarity between an interrogative query and declarative document chunks, resulting in suboptimal semantic alignment.

HyDE instructs a generative language model to hallucinate or draft a hypothetical answer document conditioned on the user prompt. The generated hypothetical document is subsequently embedded, converting an asymmetric Query-to-Document search into a symmetric Document-to-Document vector search.

```
+------------------------+
|    Raw User Query      |
| "Why was Jobs ousted?" |
+------------------------+
            |
            v
+------------------------+
|  LLM Generator (HyDE)  |
| (Drafts Answer Essay)  |
+------------------------+
            |
            v
+------------------------+
|  Hypothetical Document |
|  ("In 1985, Sculley..")|
+------------------------+
            |
            v
+------------------------+
|  Embedding Transformer |
|  (Dense Embedding e_d) |
+------------------------+
            |
            v
+------------------------+
|   FAISS Vector Index   |
| (Doc-to-Doc Similarity)|
+------------------------+
            |
            v
+------------------------+
| Relevant Ground Chunks |
+------------------------+
```

## Production Engineering Trade-offs

1. **Symmetric Embedding Manifold**: Shifting from query-vector to document-vector aligns token lengths, syntactic framing, and domain terminology with the indexed corpus.
2. **Robustness to Factual Inaccuracies**: The latent vector representation of a hypothetical document captures the target domain semantics even if specific details are fabricated by the LLM.
3. **Dual Paradigm Support**: Can be implemented via an explicit LCEL transformation chain or wrapped natively via `HypotheticalDocumentEmbedder`.

## Notebook Structure

* `04-hypothetical-document-embeddings-hyde.ipynb`:
  * Ingestion and recursive chunking of historical documentation (`steve_jobs_apple_history.txt`).
  * In-memory FAISS indexing with `sentence-transformers/all-MiniLM-L6-v2`.
  * Implementation of explicit HyDE generation and retrieval pipeline.
  * Integration with LangChain native `HypotheticalDocumentEmbedder`.
  * Quantitative comparison: Cosine similarity and rank improvements between raw query search and HyDE search.
  * Programmatic assertions validating candidate relevancy and distance convergence.

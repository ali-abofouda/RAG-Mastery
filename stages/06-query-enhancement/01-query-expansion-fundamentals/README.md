# Query Expansion Fundamentals (Stage 06 - Lecture 49)

## Architectural Overview

Query Expansion is a pre-retrieval query transformation technique designed to mitigate the vocabulary mismatch problem between user queries and indexed document corpora. In naive RAG architectures, raw user queries are often underspecified, concise, or linguistically misaligned with technical documentation.

By introducing a dedicated query reformulation layer powered by an LLM transformation chain prior to index search, the retrieval engine bridges semantic and lexical gaps, significantly elevating retrieval recall without modifying the underlying vector database.

```
+------------------+      +---------------------------+      +--------------------------+
|  Raw User Query  | ---> |  LLM Rewriter & Expansion | ---> |  Enriched Expanded Query |
| "langchain memo" |      | (Synonyms, Acronyms, Scope|      | ("modules, buffer, etc") |
+------------------+      +---------------------------+      +--------------------------+
                                                                          |
                                                                          v
+------------------+      +---------------------------+      +--------------------------+
| Grounded Context | <--- |  Cross-Encoder Reranker   | <--- |   Vector Store Index     |
| (Target Top-K)   |      |  (Precision Alignment)    |      |   (High-Recall Candidate)|
+------------------+      +---------------------------+      +--------------------------+
```

## Production Considerations

1. **Latency Overhead**: Adding an LLM query rewrite step adds 100-300ms depending on the model. Use lightweight, low-parameter models (e.g., small local models or fast inference endpoints) for query expansion.
2. **Query Drift Prevention**: Constrain the rewriter prompt strictly to reformulation, synonym addition, and technical term clarification. Prevent the rewriter from answering the query or introducing extraneous domain tangents.
3. **Synergy with Hybrid Retrieval**: Query expansion directly benefits both sparse (BM25) and dense (vector) retrieval channels by injecting both lexical keywords and semantic contextualization.

## Notebook Structure

* `01-query-expansion-fundamentals.ipynb`:
  * Self-contained, reproducible reference implementation of query expansion.
  * Baseline comparison between naive raw query retrieval and expanded query retrieval.
  * Programmatic assertions validating score dynamics, document coverage, and type safety.

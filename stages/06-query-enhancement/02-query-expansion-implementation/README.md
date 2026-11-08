# Query Expansion Implementation in End-to-End RAG (Stage 06 - Lecture 50)

## Architectural Overview

This reference implementation demonstrates a complete, production-grade RAG pipeline integrating an intermediate **Query Expansion** layer via LangChain Expression Language (LCEL).

The system addresses the vocabulary mismatch problem by passing the raw user query through an LLM reformulation chain before document retrieval. The expanded query feeds a Maximal Marginal Relevance (MMR) retriever to maximize information diversity, while the original query is preserved for final grounded generation.

```
+------------------+
|  Raw User Query  |
|  "CrewAI memory" |
+------------------+
         |
         +---------------------------------------+
         |                                       |
         v                                       v
+------------------------+             +-------------------+
| Query Expansion Chain  |             | Preservation Path |
| (Synonyms, Terms, LLM) |             | (Original Query)  |
+------------------------+             +-------------------+
         |                                       |
         v                                       |
+------------------------+                       |
| MMR Vector Retriever   |                       |
| (Top-K Diverse Chunks) |                       |
+------------------------+                       |
         |                                       |
         +-------------------+                   |
                             |                   |
                             v                   v
                    +------------------------------------+
                    | Stuff Documents Generation Chain   |
                    | (Contextual Grounded Generation)   |
                    +------------------------------------+
                                     |
                                     v
                    +------------------------------------+
                    | Accurate, Grounded Response        |
                    +------------------------------------+
```

## Production Engineering Highlights

1. **Dual Query Routing**: The expanded query targets the vector index for high recall, whereas the raw user query is passed to the generation chain to preserve user intent and prevent verbosity drift.
2. **MMR Retrieval Synergy**: Pairing query expansion with MMR search ensures that expanded synonym clusters do not result in redundant, overlapping chunks in the context window.
3. **Resilient LLM Inference**: Provides deterministic fallback handling ensuring test suites pass offline without external API latency.

## Notebook Structure

* `02-query-expansion-implementation.ipynb`:
  * Data loading via `TextLoader` and `RecursiveCharacterTextSplitter`.
  * Indexing via `HuggingFaceEmbeddings` and `FAISS`.
  * MMR Retriever configuration (`search_type="mmr"`, `k=5`).
  * Dedicated `query_expansion_chain` using `ChatPromptTemplate` and `StrOutputParser`.
  * Full `rag_pipeline` wiring using `RunnableMap` / `RunnableParallel` and `create_stuff_documents_chain`.
  * Comprehensive evaluation across multi-framework test queries (`LangChain memory`, `CrewAI memory`, `CrewAI agents`).
  * Programmatic assertions validating token non-emptiness, document counts, and response correctness.

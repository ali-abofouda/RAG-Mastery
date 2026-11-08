# Query Decomposition Reference Implementation (Stage 06 - Lecture 51)

## Architectural Overview

Query Decomposition is an advanced pre-retrieval query transformation technique engineered to solve multi-hop, multi-topic, and comparative inquiries. In complex user prompts, a single dense embedding vector fails to capture disparate concepts simultaneously due to semantic blending.

By breaking a composite question down into 2 to 4 atomic sub-questions, each sub-question retrieves targeted documents from the underlying index. A synthesis layer subsequently aggregates the intermediate sub-answers into an exhaustive, context-grounded final answer.

```
                    +--------------------------------+
                    |      Complex User Query        |
                    | "LangChain vs CrewAI Memory"   |
                    +--------------------------------+
                                   |
                                   v
                    +--------------------------------+
                    |    Query Decomposition Chain   |
                    |   (LLM + Decomposition Prompt) |
                    +--------------------------------+
                                   |
           +-----------------------+-----------------------+
           |                       |                       |
           v                       v                       v
     +------------+          +------------+          +------------+
     | Sub-Q 1    |          | Sub-Q 2    |          | Sub-Q 3    |
     +------------+          +------------+          +------------+
           |                       |                       |
           v                       v                       v
     +------------+          +------------+          +------------+
     | Retriever  |          | Retriever  |          | Retriever  |
     +------------+          +------------+          +------------+
           |                       |                       |
           v                       v                       v
     +------------+          +------------+          +------------+
     | Sub-QA LLM |          | Sub-QA LLM |          | Sub-QA LLM |
     +------------+          +------------+          +------------+
           |                       |                       |
           +-----------------------+-----------------------+
                                   |
                                   v
                    +--------------------------------+
                    |       Answer Synthesizer       |
                    |   (Unified Cohesive Output)    |
                    +--------------------------------+
```

## Production Engineering Trade-offs

1. **High Precision & Completeness**: Multi-part and comparative queries achieve complete coverage across all requested dimensions without hallucinatory gaps.
2. **Computational Overhead**: Requires $O(m)$ retrieval and LLM passes, introducing higher latency and token consumption. In production, sub-query retrievals and QA passes should be executed asynchronously in parallel.
3. **Resilient Parsing**: Sub-question parsers must defensibly strip numbering artifacts (`1. `, `2. `) and bullet markers to deliver clean string queries to retrievers.

## Notebook Structure

* `03-query-decomposition.ipynb`:
  * Technical ingestion and recursive text chunking of `langchain_crewai_dataset.txt`.
  * FAISS vector index with MMR retrieval ($k=4$).
  * LLM-driven query decomposition chain breaking complex prompts into atomic sub-questions.
  * Regex-based parsing utility stripping list formatting artifacts.
  * Multi-branch retrieval and per-question document generation chain.
  * Final synthesis combining intermediate sub-answers into a unified comparative answer.
  * Programmatic assertions validating sub-question count, response length, and topic coverage.

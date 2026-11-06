# Stage 05 - Lecture 42: Combining Dense And Sparse Retriever With LangChain
### Production EnsembleRetriever Pipeline Reference

---

## 1. Scope and Objective
This project implements an end-to-end production RAG pipeline using LangChain's `EnsembleRetriever`, combining:
- Dense Vector Store: `FAISS` with HuggingFace Embeddings (`all-MiniLM-L6-v2`).
- Sparse Lexical Index: `BM25Retriever` via `rank-bm25`.
- Fusion: Reciprocal Rank Fusion (`RRF`) weighted rank blending.
- Generation: `create_stuff_documents_chain` and `create_retrieval_chain` with `ChatGroq`.

---

## 2. Directory Structure
```
stages/05-hybrid-search-and-retrieval/02-combining-dense-and-sparse-langchain/
├── README.md                                              # Architectural specification
└── 02-combining-dense-and-sparse-langchain.ipynb          # Pre-executed reference notebook
```

---

## 3. Verification & Assertions
The pre-executed notebook enforces:
- Proper top-K document retrieval from both dense and sparse branches.
- Verification that irrelevant distractor documents (e.g. Eiffel Tower) are filtered out of top hybrid ranks.
- Verification of grounded end-to-end answer synthesis by the LLM.

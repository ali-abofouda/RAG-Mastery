# Stage 05 - Lecture 44: Reranking Hybrid Search Strategy
### Second-Stage Contextual Reranking Pipeline Reference

---

## 1. Scope and Objective
This project implements the Three-Stage RAG Architecture (`Retrieval -> Reranking -> Generation`):
- Stage 1: Fast broad candidate retrieval ($K_1=6$) using FAISS and HuggingFace Embeddings.
- Stage 2: Deep cross-relevance scoring using a specialized evaluator model to rescore and reorder candidates.
- Stage 3: Passing the top-3 reranked documents to the generation LLM for hallucination-free answer synthesis.

---

## 2. Directory Structure
```
stages/05-hybrid-search-and-retrieval/04-reranking-hybrid-strategy/
├── README.md                                     # Architectural specification
└── 04-reranking-hybrid-strategy.ipynb            # Pre-executed reference notebook
```

---

## 3. Verification & Assertions
The pre-executed notebook enforces:
- Proving rank migration: Verifying that the target specialized document buried in initial lower ranks is promoted to the top ranks.
- Clean filtration of general irrelevant documents.
- Verification of grounded answer generation.

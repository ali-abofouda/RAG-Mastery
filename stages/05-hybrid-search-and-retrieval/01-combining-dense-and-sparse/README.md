# Stage 05 - Lecture 41: Combining Dense And Sparse Matrix
### Mathematical and Empirical Fusion Reference

---

## 1. Scope and Objective
This project implements the foundational mathematics of Hybrid Search by fusing a dense embedding matrix (SentenceTransformers `all-MiniLM-L6-v2`) with a sparse lexical matrix (Scikit-Learn `TfidfVectorizer`) using the convex combination formula:
$$\text{Score}_{\text{Hybrid}} = \alpha \cdot \text{Score}_{\text{Dense}} + (1 - \alpha) \cdot \text{Score}_{\text{Sparse}}$$

---

## 2. Directory Structure
```
stages/05-hybrid-search-and-retrieval/01-combining-dense-and-sparse/
├── README.md                                # Architectural specification
└── 01-combining-dense-and-sparse.ipynb      # Pre-executed reference notebook
```

---

## 3. Verification & Assertions
The pre-executed notebook enforces:
- Strict shape matching between sparse and dense score vectors.
- Validation that the primary hybrid document strictly dominates unrelated documents.
- Zero emojis and deterministic output logging.

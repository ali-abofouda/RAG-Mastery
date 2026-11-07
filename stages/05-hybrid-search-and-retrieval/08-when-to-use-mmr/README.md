# Stage 05: Hybrid Search and Retrieval
## Topic 08: Architectural Decision Guide - When to Use and Avoid MMR (Lecture 48)

### Production Overview
This module formalizes the engineering decision criteria for deploying Maximal Marginal Relevance (MMR) vs. standard dense similarity search vs. Cross-Encoder rerankers in production RAG systems.

### Core Strategic Heuristics
1. **When to Deploy MMR**:
   * **Multi-topic / Exploratory Queries**: Maximizes information coverage across distinct perspectives (e.g., FAQ chatbots, document discovery).
   * **Corpus Redundancy**: Suppresses near-duplicate chunks from news aggregators, customer tickets, or web scrape dumps.
   * **Hybrid Search Post-Processing**: Filters out overlapping semantic and lexical duplicates produced by dense and sparse fusion.
2. **When to Avoid MMR**:
   * **Deterministic Factoid Queries**: Exact single-fact lookups where diversity introduces irrelevant noise.
   * **Constrained Context Windows ($K \le 2$)**: Extreme token budgets requiring pure top-1 precision.
   * **Downstream Reranking with Deduplication**: When Cross-Encoder models with post-filtering already resolve candidate overlap.

### File Inventory
* `08-when-to-use-mmr.ipynb`: Executed reference notebook containing comparative scenario benchmarks, latency analysis, and a decision engine utility.

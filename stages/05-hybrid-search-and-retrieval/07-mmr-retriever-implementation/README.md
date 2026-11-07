# Stage 05: Hybrid Search and Retrieval
## Topic 07: Practical Implementation of Maximal Marginal Relevance (MMR) Retrievers (Lecture 47)

### Production Overview
This module demonstrates the engineering implementation of Maximal Marginal Relevance (MMR) within enterprise Retrieval-Augmented Generation (RAG) pipelines. When querying vector databases, dense similarity search frequently retrieves redundant documents that crowd out complementary insights. MMR counters this failure mode by evaluating both query-document similarity and inter-document novelty during candidate selection.

### Key Architecture Components
1. **Document Ingestion & Chunking**: `TextLoader` and `RecursiveCharacterTextSplitter` configured with `chunk_size=300` and `chunk_overlap=50`.
2. **Local Vector Store**: `sentence-transformers/all-MiniLM-L6-v2` dense embedding generation and `FAISS` indexing.
3. **MMR Retriever**: `as_retriever(search_type="mmr", search_kwargs={"k": 3, "fetch_k": 20, "lambda_mult": 0.5})`.
4. **End-to-End Pipeline**: Integration via `create_stuff_documents_chain` and `create_retrieval_chain` with `ChatGroq`.

### File Inventory
* `07-mmr-retriever-implementation.ipynb`: Executed reference notebook with assertions and verified outputs.
* `langchain_rag_dataset.txt`: Input technical text dataset on LangChain architecture, components, agents, and memory.

# Section 30: HR Policy RAG Assistant with Enterprise AI Security

An end-to-end, enterprise-grade Retrieval-Augmented Generation (RAG) assistant designed for Human Resources policy resolution in corporate multi-national environments. Engineered with defense-in-depth security, adversarial resilience, multi-model routing via a self-hosted gateway, and cloud containerization.

---

## Architecture Highlights

1. **Enterprise Identity & Access Management (IAM)**:
   - Google OAuth 2.0 integration with role-based access control (RBAC), strictly white-listing authorized employee email identities.
2. **Self-Hosted AI Gateway (`LiteLLM`)**:
   - Containerized proxy abstracting multi-provider LLM endpoints, enabling dynamic failover, load balancing, budget controls, and latency observability.
3. **Robust Retrieval in Noisy Databases**:
   - Qdrant Vector Store populated with official HR policies alongside deliberately injected background noise.
   - Multi-stage retrieval pipeline coupling semantic dense search with high-precision Cross-Encoder Re-ranking.
4. **Multi-Layer Defense & Model Armor**:
   - Strict out-of-domain query rejection (refusing non-HR tasks).
   - Jailbreak and prompt injection mitigation protecting system prompts against persona override and roleplay escapes.
   - Comprehensive Red Teaming evaluation suite verifying 100% adversarial attack neutralization prior to deployment.
5. **Cost & Latency Optimization**:
   - Semantic Caching layer intercepting high-frequency employee queries to deliver sub-millisecond responses without downstream inference cost.
6. **Explainability & Verification**:
   - Guaranteed source document and clause citations on all generated employee responses.

---

## Directory Layout

```text
01-hr-policy-rag-assistant/
├── README.md               # Architecture specification and execution manual
├── config/                 # YAML and Pydantic configuration schemas
├── data/
│   ├── policies/           # Official HR policy documents (Leave, Resignation, Maternity)
│   └── noise/              # Synthetic distractor documents simulating enterprise noise
├── src/
│   ├── ingestion/          # Document loading, semantic chunking, and Qdrant ingestion
│   ├── retrieval/          # Dense vector search, hybrid retrieval, and Cross-Encoder re-rankers
│   ├── security/           # Guardrails, prompt sanitization, and semantic caching
│   ├── agent/              # LangGraph stateful workflow coordinator and decision graphs
│   └── evaluation/         # Red Teaming adversarial attack harness and RAG triad evals
├── notebooks/              # Modular step-by-step interactive research notebooks
├── tests/                  # Automated integration, security, and unit test suites
└── Dockerfile              # Production container build manifest for Google Cloud Run
```

---

## Project Execution Lifecycle

- **Phase 1: Local Hybrid RAG (Lectures 142 - 151)**: Ingestion, noisy Qdrant vector store, Cross-Encoder re-ranking, and LangGraph agent workflow.
- **Phase 2: LLM Security & Evals (Lectures 152 - 159)**: Self-hosted LiteLLM gateway, Google Model Armor guardrails, semantic caching, and Red Teaming verification.
- **Phase 3: Production Deployment (Lectures 160 - 163)**: Docker containerization and deployment onto Google Cloud Run.

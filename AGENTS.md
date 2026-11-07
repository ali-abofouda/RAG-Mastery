# AGENTS.md: Developer & AI Agent Operating Manual

Welcome to **RAG-Mastery**. This repository is an end-to-end, production-grade educational codebase mirroring a comprehensive 32-section / 191-lecture / 45-hour Retrieval-Augmented Generation (RAG) curriculum.

Every AI agent working on this codebase must adhere strictly to the protocols, separation of concerns, and coding standards outlined below.

---

## 1. The Cardinal Rule: Strict Transcript-Driven Progression

> [!IMPORTANT]
> **NEVER JUMP AHEAD OR FABRICATE FUTURE LECTURES.**
> The USER is following a structured video course lecture-by-lecture. The workflow is strictly **input-driven**:
> 1. The user provides a **transcript, summary, or video script** of a specific lecture.
> 2. The agent analyzes the exact concepts, algorithms, and code demonstrated in that video.
> 3. The agent implements **only that lecture** across `docs/`, `stages/`, and `playground/`.
> 4. If the user says "التالي" (Next) without providing the script, **politely ask for the next video's transcript/notes** before generating any code or documentation.

### User Lecture Submission Protocol (بروتوكول استلام المحاضرة من المستخدم)
The user will simply provide:
> **رقم المحاضرة / الفيديو (e.g., فيديو 45 أو المحاضرة 45)** متبوعاً بنص الاسكريبت مباشرة.

The AI Agent:
* Already has the entire course roadmap, stage structures, and context.
* Automatically deduces the section, stage, topic title, and lecture type (theoretical vs. practical code vs. comparison) from the transcript.
* Does **NOT** ask the user to fill out repetitive metadata templates; just take the video number + transcript and start working immediately.

---

## 2. Repository Architecture & Separation of Concerns

The repository is organized into three distinct, complementary environments for each stage:

```
rag-mastery/
├── docs/                     # Comprehensive theoretical & architectural guides (Arabic)
│   └── 0X-<stage-name>/
│       ├── README.md         # Stage overview and lecture map
│       └── 0Y-<topic>.md     # Deep dive per lecture (Math, KaTeX, Mermaid)
├── stages/                   # Production reference code (Senior AI Engineer standard)
│   └── 0X-<stage-name>/
│       └── 0Y-<topic>/
│           ├── <topic>.ipynb # 100% English, zero emojis, type hints, assertions, executed
│           └── README.md     # Quick reference
├── playground/               # Interactive human scratchpads (Conversational Arabic)
│   └── 0X-<stage-name>/
│       └── 0Y-<topic>.ipynb  # Simple, conversational Arabic, bite-sized cells, executed
├── notes/                    # Accelerated study plans and enterprise guides
└── pyproject.toml            # Managed with uv
```

---

## 3. Environment Specifications

### A. Production Reference: `stages/`
* **Target Audience**: Senior AI Engineers & Architects seeking production patterns.
* **Language**: **100% English** (markdown headers, narrative, docstrings, variable names, comments).
* **Emojis**: **STRICTLY ZERO EMOJIS**. Remove all `🎯`, `🚀`, `📚`, `✅`, `💡`, `🔍`, etc.
* **Code Standards**:
  * Explicit type hints (`from typing import List, Dict, Optional, Tuple, Any`).
  * Defensive exception handling with graceful fallbacks.
  * Rigorous programmatic assertions (`assert`) validating tensor dimensions, collection counts, score ordering, and response non-emptiness.
* **Execution Rule**: Every notebook **MUST** be executed with real outputs saved in the JSON (`has_outputs: True`). Never leave empty code cells.

### B. Interactive Human Scratchpad: `playground/`
* **Target Audience**: Students and developers experimenting hands-on.
* **Language**: **Conversational, friendly, human-written Arabic** (Egyptian/Modern conversational style, e.g., `"تعال نجرب نشغل..."`, `"لاحظ هنا لما بنغير الرقم ده..."`, `"طب لو جربنا نسأل..."`).
* **Emojis**: **STRICTLY ZERO EMOJIS**. Maintain professional, clean text.
* **Code Standards**:
  * Short, clean, bite-sized cells (3 to 8 lines per cell).
  * Informative, friendly `print()` statements demonstrating intermediate values.
  * **NO restrictive assertions**: Do not include hard `assert` statements that crash or prevent the user from editing and experimenting freely.
  * Always include a dedicated `"جرب بنفسك!"` (Try it yourself!) section at the end.
* **Execution Rule**: Must be fully executed with real outputs saved.

### C. Theoretical Documentation: `docs/`
* **Target Audience**: Technical leads, researchers, and system designers.
* **Language**: Comprehensive, mathematically rigorous Arabic technical handbook.
* **Formatting Requirements**:
  * UTF-8 encoding with no mojibake.
  * All mathematical formulations must use standard **KaTeX LaTeX math** (`$...$` and `$$...$$`).
  * Visual architectures must use **Mermaid diagrams** (`flowchart TD`, `sequenceDiagram`, `stateDiagram-v2`).
  * Engineering trade-off tables comparing computational complexity, latency, and memory footprints.
  * All English technical terms inside Arabic prose must be enclosed in markdown backticks (e.g., `` `CrossEncoder` ``).

---

## 4. Hardware, Library, and Model Defaults

To guarantee that code executes reliably on any machine without quota exhaustion or API failure:

1. **Embedding Models**:
   * Always default to local `sentence-transformers/all-MiniLM-L6-v2`:
     ```python
     from langchain_huggingface import HuggingFaceEmbeddings

     embeddings = HuggingFaceEmbeddings(
         model_name="sentence-transformers/all-MiniLM-L6-v2"
     )
```
   * Do NOT use remote Hugging Face Inference API (`HuggingFaceEndpointEmbeddings`) as it frequently returns HTTP 402 / credit limits.

2. **LLM Inference**:
   * Default to `ChatGroq` with available models (e.g. `openai/gpt-oss-20b`):
     ```python
     from langchain_groq import ChatGroq

     llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0)
```
   * Provide graceful mock/fallback if API keys are absent.

3. **Vector Databases**:
   * Local stores (`Chroma`, `FAISS`, `InMemoryVectorStore`) must use isolated temporary directories (`tempfile.mkdtemp()`) or dedicated clean paths in `data/databases/`.
   * Cloud vector databases (`Pinecone`, `AstraDB`) must detect credentials dynamically and fall back to local in-memory simulation stores if keys are missing.

---

## 5. Agent Verification Checklist Before Ending a Turn

Before concluding any work, every AI agent must verify:
- [ ] Did the user provide the transcript for this specific lecture?
- [ ] Are all cells in `stages/` 100% English with ZERO emojis?
- [ ] Are all cells in `playground/` conversational Arabic with ZERO emojis?
- [ ] Have all notebooks been preprocessed and executed via `nbconvert` / `ExecutePreprocessor`?
- [ ] Did all assertions pass without errors?
- [ ] Are git changes staged, committed with conventional commit messages (`feat:`, `refactor:`, `docs:`), and pushed to `origin main`?

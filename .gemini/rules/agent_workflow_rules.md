---
description: Critical workflow, structure, and execution rules for AI agents working on RAG-Mastery
always_active: true
---

# RAG-Mastery: AI Agent Operating Guidelines & Rules

## 1. Core Operating Principle: Strict Transcript-Driven Progression
- **NEVER jump ahead or invent future lectures on your own.**
- The user is studying a 191-lecture video course step-by-step.
- You must ONLY implement the specific lecture for which the user has provided the transcript or explicit instructions.
- If the user says "Next" (التالي), ask for the transcript of the upcoming lecture unless they specifically tell you to proceed with a given text.
- Do not introduce arbitrary third-party frameworks or tangential topics unless they are part of the lecture transcript.

---

## 2. Three Environments Architecture & Strict Separation of Concerns

Every topic/lecture belongs to three distinct environments, each with a strict identity and style:

### A. Production Reference: `stages/`
- **Target Persona**: Senior AI/RAG Engineer.
- **Language**: 100% English (docstrings, comments, markdown, variable names).
- **Emojis**: STRICTLY ZERO EMOJIS (no `🚀`, `🎯`, `✅`, `💡`, `📚`, etc.).
- **Code Standards**:
  - Production structure, type hints, proper modular functions.
  - Robust exception handling and deterministic fallbacks.
  - Strict assertions (`assert`) verifying shapes, scores, and retrieval accuracy.
- **Execution**: MUST be fully executed using `ExecutePreprocessor` with real outputs saved in the `.ipynb` file.

### B. Interactive Human Scratchpad: `playground/`
- **Target Persona**: Junior-to-Mid developer experimenting in a hands-on lab.
- **Language**: 100% Conversational, friendly, human-written Arabic (e.g., "تعال نجرب نشغل...", "لاحظ هنا لما بنغير الرقم ده...", "جرب بنفسك...").
- **Emojis**: STRICTLY ZERO EMOJIS.
- **Code Standards**:
  - Short, clean, bite-sized cells.
  - Explanatory print statements showing intermediate results.
  - NO restrictive `assert` barriers that block the user from experimenting freely.
  - Dedicated "جرب بنفسك!" section for open experimentation.
- **Execution**: MUST be fully executed with actual outputs saved.

### C. Theoretical & Architectural Reference: `docs/`
- **Target Persona**: System Architect & Research Engineer.
- **Language**: Comprehensive, deep Arabic technical handbook.
- **Formatting**:
  - Pure UTF-8 encoding (no mojibake).
  - KaTeX math formulas for all mathematical equations ($...$ and $$...$$).
  - Mermaid diagrams (`flowchart TD`, `sequenceDiagram`) for architectural pipelines.
  - Engineering comparison tables with real trade-offs.

---

## 3. Reliability & Hardware Environment Rules
- **Embeddings**: Never rely solely on remote Hugging Face Inference API (which can return HTTP 402/quota limits). Always use:
  ```python
  from langchain_huggingface import HuggingFaceEmbeddings

  embeddings = HuggingFaceEmbeddings(
      model_name="sentence-transformers/all-MiniLM-L6-v2"
  )
```
- **LLM**: Use `ChatGroq` with active and available models:
  ```python
  from langchain_groq import ChatGroq

  llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0)
```
- **BiDi Text Safety**: All English technical terms inside Arabic prose MUST be enclosed in markdown backticks (e.g. `` `CrossEncoder` ``).
- **No Unexecuted Notebooks**: Never commit a notebook with empty outputs (`has_outputs: False`).

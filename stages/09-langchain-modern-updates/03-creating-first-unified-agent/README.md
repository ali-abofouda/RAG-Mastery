# Stage 09 / Lecture 59: Creating Unified AI Agents with `create_agent`

## Reference Overview
This stage implements and verifies the unified LangChain v1+ agent constructor (`create_agent`) backed by `LangGraph`.

### Key Verified Concepts
1. **Graph Topology Evolution**: Contrasts linear graphs (`tools=[]`: `START -> model -> END`) with cyclic tool-calling graphs (`START -> model <-> tools -> END`).
2. **Legacy Guardrails**: Demonstrates deprecation `TypeError` for `verbose=True` and schema validation errors on raw string inputs.
3. **The Docstring Contract**: Shows how `get_weather(city: str) -> str` uses type annotations and docstrings to enable autonomous tool calling.
4. **Full Message Trajectory**: Validates all four message types (`HumanMessage`, `AIMessage` with `tool_calls`, `ToolMessage`, and synthesized final `AIMessage`) using live `ChatGroq(model="openai/gpt-oss-20b")` inference.

### Engineering Standards
- 100% English, zero emojis, strict typing, programmatic assertions verified, executed via `nbconvert`.

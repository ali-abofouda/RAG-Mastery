# Stage 09 / Lecture 61: Custom Tools (`@tool`), `bind_tools()`, and Manual Tool Execution Loop

## Reference Overview
This stage implements and verifies custom tool creation and the manual invocation lifecycle underlying agent frameworks.

### Key Verified Capabilities
1. **`@tool` Decorator Introspection**: Validates automatic JSON schema generation (`.name`, `.description`, `.args`) from typed Python functions and docstrings.
2. **Tool Binding (`model.bind_tools()`)**: Verifies that binding tools emits an `AIMessage` requesting `.tool_calls` without executing Python locally.
3. **Manual Tool Execution Loop**: Demonstrates executing `tool.invoke(tool_call)` to receive an ID-matched `ToolMessage`, appending it to context, and synthesizing the grounded answer.
4. **Multi-Tool Registry Dispatch**: Maps multiple bound tools via `{tool.name: tool}` dictionary dispatch for scalable routing.

### Engineering Standards
- 100% English, zero emojis, strict typing, programmatic assertions verified, executed via `nbconvert`.

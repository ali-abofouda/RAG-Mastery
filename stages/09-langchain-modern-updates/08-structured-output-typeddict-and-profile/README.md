# Stage 09 / Lecture 64: Structured Outputs via `TypedDict` and `model.profile`

## Reference Overview
This stage demonstrates lightweight structured output extraction using Python **`TypedDict`** and **`Annotated`**, contrasting runtime validation trade-offs against Pydantic and auditing model capabilities via `model.profile`.

### Verified Capabilities
1. **TypedDict Schema Binding**: Returning plain Python `dict` payloads using `Annotated[type, ..., "description"]` without runtime validation overhead.
2. **Nested TypedDict Extraction**: Handling hierarchical schemas (`ActorDict` inside `MovieDetailsDict`) using `method="json_schema"` for cross-provider stability.
3. **Capability Introspection (`model.profile`)**: Demonstrating capability checks (`max_input_tokens`, `reasoning_output`, `tool_calling`, `structured_output`) on `BaseChatModel` while verifying expected `AttributeError` on wrapped `RunnableSequence` chains.

### Engineering Standards
- 100% English, zero emojis, strict typing, programmatic assertions verified, executed via `nbconvert`.

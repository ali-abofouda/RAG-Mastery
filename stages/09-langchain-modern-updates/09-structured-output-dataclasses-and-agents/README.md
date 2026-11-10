# Stage 09 / Lecture 65: Dataclasses & Agent `response_format` Integration

## Reference Overview
This stage demonstrates integrating structured output contracts directly inside **`create_agent(..., response_format=Schema)`**, comparing Python `@dataclass`, `TypedDict`, and `Pydantic BaseModel`.

### Verified Capabilities
1. **Unified Agent `response_format`**: Extracting deterministic payloads via `result["structured_response"]` alongside `result["messages"]`.
2. **Tri-Paradigm Comparison**:
   - `Pydantic BaseModel`: Strict runtime validation + dot-attribute access.
   - `TypedDict`: Zero-validation dictionary payload.
   - Python `@dataclass`: Native zero-dependency attribute-accessible object without runtime validation overhead.

### Engineering Standards
- 100% English, zero emojis, strict typing, programmatic assertions verified, executed via `nbconvert`.

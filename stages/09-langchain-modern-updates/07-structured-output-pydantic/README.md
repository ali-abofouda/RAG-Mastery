# Stage 09 / Lecture 63: Structured Outputs via Pydantic

## Reference Overview
This stage enforces strict schema extraction and validation using **Pydantic v2** and `model.with_structured_output()` against live `ChatGroq` inference.

### Verified Capabilities
1. **Schema Enforcement**: Constraining `Movie` outputs (`title`, `year`, `director`, `rating`) with `Field(..., description=...)`.
2. **Runtime Type Validation**: Demonstrating `ValidationError` rejection on malformed schema data.
3. **Observability (`include_raw=True`)**: Capturing `raw` (`AIMessage` with `usage_metadata`), `parsed`, and `parsing_error`.
4. **Nested Hierarchical Schemas**: Extracting recursive collections (`List[Actor]` inside `MovieDetails`).

### Engineering Standards
- 100% English, zero emojis, strict typing, programmatic assertions verified, executed via `nbconvert`.

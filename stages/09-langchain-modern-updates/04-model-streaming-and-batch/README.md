# Stage 09 / Lecture 60: Model Execution Modes (`invoke`, `stream`, & `batch`)

## Reference Overview
This stage benchmarks and verifies the three core LangChain v1+ `Runnable` execution interfaces against live `ChatGroq` inference.

### Verified Capabilities
1. **`model.invoke()`**: Synchronous blocking completion returning a complete `AIMessage` payload.
2. **`model.stream()`**: Real-time progressive generator yielding `AIMessageChunk` tokens, measuring Time-to-First-Token (`TTFT`) and handling immediate buffer flushing (`flush=True`).
3. **`model.batch()`**: Parallel request processing with `config={"max_concurrency": 3}` rate-limit protection for independent question batches.

### Engineering Standards
- 100% English, zero emojis, strict typing, programmatic assertions verified, executed via `nbconvert`.

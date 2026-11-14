# Deterministic Workflow Execution: Pure Python Nodes & State Schemas

## Overview
This production reference module implements an LLM-free deterministic workflow using **LangGraph**. It establishes foundational execution primitives: TypedDict state schemas, isolated node function contracts, and type-safe conditional routing without external model dependencies.

## Key Architectural Patterns
1. **TypedDict State Schema**: Lightweight state definition (`graph_info: str`) providing static type safety with zero runtime serialization overhead.
2. **Pure Functional Node Contracts**: Discrete node functions (`start_play`, `cricket`, `badminton`) consuming state objects and returning atomic partial updates (`deltas`).
3. **Literal-Typed Conditional Routing**: Routing function utilizing `typing.Literal["cricket", "badminton"]` ensuring compile-time routing integrity.
4. **End-to-End Workflow Compilation**: Registering nodes, entry points (`START`), conditional edges, and sink transitions (`END`) into an executable `StateGraph`.
5. **Programmatic Assertions**: Runtime invariant validation confirming deterministic execution, state string concatenation, and node sequence traversal.

## File Manifest
- `04-simple-workflow-state-and-nodes.ipynb`: Executed reference notebook with type-safe state mutations and branching assertions.
- `README.md`: Technical specification and architecture manifest.

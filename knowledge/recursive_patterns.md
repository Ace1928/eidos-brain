# Recursive Patterns

## Memory Recursion Pattern
1. Collect experiences.
2. Reflect on stored memories.
3. Generate insights via meta-reflection.
4. Append insights as new memories for future cycles.

### Combined Cycle Pattern
Use `process_cycle` to store an experience and immediately recurse,
appending reflective insights in a single step.

### Memory Persistence Pattern
Leverage `load_memory` and `save_memory` to maintain state across runs:
1. Call `load_memory` with a file path before processing.
2. Run `process_cycle` with the same path to automatically save results.

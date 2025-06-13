# Recursive Patterns

These patterns guide the use of templates in `templates.md` and define how
documentation references are organized in the `glossary_reference.md`.

## Memory Recursion Pattern
1. Collect experiences.
2. Reflect on stored memories.
3. Generate insights via meta-reflection.
4. Append insights as new memories for future cycles.

### Combined Cycle Pattern
Use `process_cycle` to store an experience and immediately recurse,
appending reflective insights in a single step.

## Vector Memory Query Pattern
1. Store embeddings with associated items via ``VectorMemory.add``.
2. Provide a new embedding to ``VectorMemory.query``.
3. Retrieve the most similar items based on cosine similarity.

# Recursive Patterns

## Memory Recursion Pattern
1. Collect experiences.
2. Reflect on stored memories.
3. Generate insights via meta-reflection.
4. Append insights as new memories for future cycles.

### Combined Cycle Pattern
Use `process_cycle` to store an experience and immediately recurse,
appending reflective insights in a single step.

## Self-Documenting Pattern
Maintain examples and references beside each implementation.

1. Write descriptive docstrings for every public symbol.
2. Include short usage examples near the code when possible.
3. Run `tools/generate_glossary.py` to refresh `knowledge/glossary_reference.md`.
4. Capture new insights in `emergent_insights.md` as the glossary grows.

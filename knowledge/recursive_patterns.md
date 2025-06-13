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

## LLM Protection Pattern
1. Limit request frequency with `RateLimiter`.
2. Scrub sensitive content via `filter_sensitive_content`.
3. Wrap LLM calls using both mechanisms.

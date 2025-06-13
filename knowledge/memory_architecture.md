# Memory Architecture

This document outlines the available memory backends used by `EidosCore`.
It references templates found in `templates.md` and patterns from `recursive_patterns.md`.
Terminology is aligned with `glossary_reference.md`.

## VectorMemory
A list-based store suitable for ordered sequences of experiences.

## KnowledgeGraph
A simple graph where experiences become nodes. This backend emphasizes
relationships over ordering.

Both backends implement the `MemoryProtocol` interface, ensuring they are
interchangeable within the core recursion cycle.

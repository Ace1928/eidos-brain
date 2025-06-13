"""Utilities for persisting vector memories and knowledge graph state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Sequence, Mapping, MutableMapping, List, Dict

Vector = Sequence[Sequence[float]]
Graph = MutableMapping[str, List[str]]


def save_vector_memory(memory: Vector, path: Path) -> None:
    """Persist ``memory`` as JSON to ``path``."""
    path.write_text(json.dumps(memory))


def load_vector_memory(path: Path) -> List[List[float]]:
    """Load vector memory from ``path`` or return an empty list."""
    if path.exists():
        return json.loads(path.read_text())
    return []


def save_knowledge_graph(graph: Mapping[str, Sequence[str]], path: Path) -> None:
    """Persist a knowledge graph mapping to ``path`` as JSON."""
    path.write_text(json.dumps({k: list(v) for k, v in graph.items()}))


def load_knowledge_graph(path: Path) -> Dict[str, List[str]]:
    """Load a knowledge graph from ``path`` or return an empty dict."""
    if path.exists():
        return json.loads(path.read_text())
    return {}

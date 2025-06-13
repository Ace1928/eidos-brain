"""Memory backends for :class:`EidosCore`."""

from __future__ import annotations

from typing import Iterable, Protocol, List, Any


class MemoryProtocol(Protocol):
    """Unified interface for storing experiences."""

    def add(self, experience: Any) -> None:
        """Store a single experience."""

    def extend(self, experiences: Iterable[Any]) -> None:
        """Store multiple experiences."""

    def get_all(self) -> List[Any]:
        """Return all stored experiences as a list."""


class VectorMemory:
    """List-based memory implementation."""

    def __init__(self) -> None:
        self._data: List[Any] = []

    def add(self, experience: Any) -> None:
        self._data.append(experience)

    def extend(self, experiences: Iterable[Any]) -> None:
        self._data.extend(experiences)

    def get_all(self) -> List[Any]:
        return list(self._data)


class KnowledgeGraph:
    """Node-centric memory using a simple graph representation."""

    def __init__(self) -> None:
        self._nodes: set[Any] = set()

    def add(self, experience: Any) -> None:
        self._nodes.add(experience)

    def extend(self, experiences: Iterable[Any]) -> None:
        for exp in experiences:
            self.add(exp)

    def get_all(self) -> List[Any]:
        return list(self._nodes)

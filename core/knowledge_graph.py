"""Typed knowledge graph utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Node:
    """Represents a typed entity in the knowledge graph."""

    name: str
    type: str


@dataclass(frozen=True)
class Fact:
    """Single statement connecting two :class:`Node` objects."""

    subject: Node
    predicate: str
    obj: Node


class KnowledgeGraph:
    """Store and query typed relationships between nodes."""

    def __init__(self) -> None:
        """Initialize an empty fact collection."""
        self.facts: List[Fact] = []

    def add_fact(
        self,
        subject: str,
        predicate: str,
        obj: str,
        *,
        subject_type: str = "entity",
        object_type: str = "entity",
    ) -> None:
        """Add a new fact to the graph."""
        fact = Fact(Node(subject, subject_type), predicate, Node(obj, object_type))
        self.facts.append(fact)

    def query(
        self,
        *,
        subject: Optional[str] = None,
        predicate: Optional[str] = None,
        obj: Optional[str] = None,
        subject_type: Optional[str] = None,
        object_type: Optional[str] = None,
    ) -> List[Fact]:
        """Return all facts matching the given parameters."""
        results: List[Fact] = []
        for fact in self.facts:
            if subject is not None and fact.subject.name != subject:
                continue
            if subject_type is not None and fact.subject.type != subject_type:
                continue
            if predicate is not None and fact.predicate != predicate:
                continue
            if obj is not None and fact.obj.name != obj:
                continue
            if object_type is not None and fact.obj.type != object_type:
                continue
            results.append(fact)
        return results

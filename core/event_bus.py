"""Simple event bus for agent communication."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable


class EventBus:
    """Central hub for pub/sub messaging."""

    def __init__(self) -> None:
        """Initialize empty subscriber registry."""
        self._subscribers: dict[str, list[Callable[..., Any]]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable[..., Any]) -> None:
        """Register a ``handler`` for a named ``event``."""
        self._subscribers[event].append(handler)

    def publish(self, event: str, *args: Any, **kwargs: Any) -> list[Any]:
        """Broadcast ``event`` to all handlers and collect responses."""
        results = []
        for func in self._subscribers.get(event, []):
            results.append(func(*args, **kwargs))
        return results

    def clear(self) -> None:
        """Remove all registered handlers."""
        self._subscribers.clear()

    @property
    def subscribers(self) -> dict[str, list[Callable[..., Any]]]:
        """Expose current subscriber mapping."""
        return dict(self._subscribers)

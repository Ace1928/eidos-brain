"""Simple publish-subscribe event bus for Eidos."""

from __future__ import annotations

from collections import defaultdict
from typing import Callable, Any, DefaultDict


class EventBus:
    """Central mechanism for event registration and delivery."""

    def __init__(self) -> None:
        self._listeners: DefaultDict[str, list[Callable[..., None]]] = defaultdict(list)

    def subscribe(self, event: str, listener: Callable[..., None]) -> None:
        """Register ``listener`` to be notified when ``event`` is emitted."""
        self._listeners[event].append(listener)

    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Trigger ``event`` and invoke all registered listeners."""
        for listener in self._listeners.get(event, []):
            listener(*args, **kwargs)

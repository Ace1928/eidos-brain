"""Minimal event bus for Eidos components."""

from collections import defaultdict
from typing import Callable, Any, DefaultDict, List


class EventBus:
    """Publish and subscribe to named events."""

    def __init__(self) -> None:
        self._listeners: DefaultDict[str, List[Callable[..., None]]] = defaultdict(list)

    def subscribe(self, event: str, listener: Callable[..., None]) -> None:
        """Register ``listener`` for ``event``."""
        self._listeners[event].append(listener)

    def publish(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Invoke listeners attached to ``event``."""
        for listener in list(self._listeners.get(event, [])):
            listener(*args, **kwargs)

"""Execution engine orchestrating operations for :class:`EidosCore`."""

from __future__ import annotations


from .eidos_core import EidosCore


class Engine:
    """Perform actions using an internal :class:`EidosCore` instance."""

    def __init__(self) -> None:
        """Initialize the engine with its own core."""
        self.core = EidosCore()

    def execute(self, command: str, *args: str) -> str:
        """Execute ``command`` with ``args`` and return a response."""
        if command == "add":
            experience = " ".join(args)
            self.core.remember(experience)
            return "Experience added."
        if command == "reflect":
            return repr(self.core.reflect())
        if command == "recurse":
            self.core.recurse()
            return "Recursion complete."
        return "Unknown command"

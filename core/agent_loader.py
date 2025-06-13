"""Automatically load agents and attach them to the event bus."""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from typing import Any

from agents import __path__ as AGENT_PATH

from .event_bus import EventBus


def load_agents(bus: EventBus) -> dict[str, Any]:
    """Discover agent classes and register them with ``bus``."""
    instances: dict[str, Any] = {}
    for _, module_name, _ in pkgutil.iter_modules(AGENT_PATH):
        module = importlib.import_module(f"agents.{module_name}")
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if name.endswith("Agent"):
                instance = obj()
                if hasattr(instance, "register"):
                    instance.register(bus)
                instances[name] = instance
    return instances

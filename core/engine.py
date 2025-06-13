"""Orchestrates core components, agents, and events."""

from typing import Any, Callable

from .eidos_core import EidosCore
from .event_bus import EventBus
from agents import UtilityAgent, ExperimentAgent


class Engine:
    """Central coordinator providing high-level interactions."""

    def __init__(self) -> None:
        self.core = EidosCore()
        self.utility_agent = UtilityAgent()
        self.experiment_agent = ExperimentAgent()
        self.bus = EventBus()

    def add_experience(self, experience: Any) -> None:
        """Store ``experience`` via :class:`EidosCore`."""
        self.core.remember(experience)
        self.bus.publish("experience_added", experience)

    def run_cycle(self, experience: Any) -> None:
        """Execute a full cycle of storing and reflecting."""
        self.core.process_cycle(experience)
        self.bus.publish("cycle_complete", experience)

    def reflect(self) -> list[Any]:
        """Return a snapshot of current memories."""
        return self.core.reflect()

    def run_experiment(self, hypothesis: str) -> str:
        """Delegate to :class:`ExperimentAgent` and emit event."""
        result = self.experiment_agent.run(hypothesis)
        self.bus.publish("experiment_run", hypothesis, result)
        return result

    def perform_task(self, task: str) -> str:
        """Delegate to :class:`UtilityAgent` and emit event."""
        result = self.utility_agent.perform_task(task)
        self.bus.publish("task_performed", task, result)
        return result

    def on(self, event: str, listener: Callable[..., None]) -> None:
        """Subscribe ``listener`` to ``event``."""
        self.bus.subscribe(event, listener)

    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Manually publish an event."""
        self.bus.publish(event, *args, **kwargs)

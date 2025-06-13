"""Agent dedicated to running experiments within Eidos-Brain."""

from core.event_bus import EventBus


class ExperimentAgent:
    """Handles experimental cycles and evaluations."""

    def register(self, bus: "EventBus") -> None:
        """Attach experiment handlers to ``bus``."""
        bus.subscribe("experiment_run", self.run)
        bus.subscribe("experiment_series", self.run_series)

    def run(self, hypothesis: str) -> str:
        """Execute an experiment and return its result."""
        return f"Experimenting with {hypothesis}"

    def run_series(self, hypotheses: list[str]) -> list[str]:
        """Run a series of experiments and collect results."""
        return [self.run(h) for h in hypotheses]

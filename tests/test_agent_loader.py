import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core import EventBus, load_agents


def test_load_agents_registers_handlers():
    bus = EventBus()
    agents = load_agents(bus)
    assert "UtilityAgent" in agents
    assert "ExperimentAgent" in agents
    result = bus.publish("utility_task", "clean")
    assert result == ["Performed clean"]
    series = bus.publish("experiment_series", ["h1", "h2"])
    assert series == [["Experimenting with h1", "Experimenting with h2"]]

from core.engine import Engine
from core.eidos_core import EidosCore
from agents import UtilityAgent, ExperimentAgent


def test_engine_initializes_components() -> None:
    engine = Engine()
    assert isinstance(engine.core, EidosCore)
    assert isinstance(engine.utility_agent, UtilityAgent)
    assert isinstance(engine.experiment_agent, ExperimentAgent)
    assert hasattr(engine, "bus")


def test_engine_event_bus() -> None:
    engine = Engine()
    called = []

    def listener(data: str) -> None:
        called.append(data)

    engine.on("experience_added", listener)
    engine.add_experience("test")
    assert called == ["test"]


def test_engine_delegates_tasks() -> None:
    engine = Engine()
    assert engine.perform_task("clean") == "Performed clean"
    assert engine.run_experiment("X") == "Experimenting with X"

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.agent import Agent
from agents.utility_agent import UtilityAgent
from agents.experiment_agent import ExperimentAgent


def test_utility_agent_perform_task():
    agent = UtilityAgent()
    result = agent.perform_task("clean")
    assert result == "Performed clean"


def test_utility_agent_batch_perform():
    agent = UtilityAgent()
    results = agent.batch_perform(["clean", "build"])
    assert results == ["Performed clean", "Performed build"]


def test_experiment_agent_run():
    agent = ExperimentAgent()
    result = agent.run("hypothesis")
    assert result == "Experimenting with hypothesis"


def test_experiment_agent_run_series():
    agent = ExperimentAgent()
    results = agent.run_series(["h1", "h2"])
    assert results == ["Experimenting with h1", "Experimenting with h2"]


def test_experiment_agent_is_agent() -> None:
    """``ExperimentAgent`` should adhere to the ``Agent`` interface."""
    assert issubclass(ExperimentAgent, Agent)

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.utility_agent import UtilityAgent
from agents.experiment_agent import ExperimentAgent


def test_utility_agent_perform_task():
    agent = UtilityAgent()
    result = agent.perform_task("clean")
    assert result == "Performed clean"


def test_experiment_agent_run():
    agent = ExperimentAgent()
    result = agent.run("hypothesis")
    assert result == "Experimenting with hypothesis"

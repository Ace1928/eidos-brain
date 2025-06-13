import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.utility_agent import UtilityAgent
from agents.experiment_agent import ExperimentAgent


def test_utility_agent_perform_task():
    agent = UtilityAgent()
    result = agent.perform_task("clean")
    assert result == "Performed clean"


def test_log_with_timestamp(tmp_path):
    agent = UtilityAgent()
    log_file = tmp_path / "log.txt"
    line = agent.log_with_timestamp("hello", file_path=str(log_file))
    assert line.endswith("hello")
    content = log_file.read_text().strip()
    assert content.endswith("hello")
    assert line == content


def test_experiment_agent_run():
    agent = ExperimentAgent()
    result = agent.run("hypothesis")
    assert result == "Experimenting with hypothesis"

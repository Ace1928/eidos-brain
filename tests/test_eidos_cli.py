import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typer.testing import CliRunner
from tools import eidos_cli
from rich.prompt import Prompt
from unittest.mock import patch


runner = CliRunner()


def test_add_and_reflect() -> None:
    result = runner.invoke(eidos_cli.app, ["add-memory", "hello"])
    assert result.exit_code == 0
    result = runner.invoke(eidos_cli.app, ["reflect"])
    assert "hello" in result.stdout


def test_run_agent_utility() -> None:
    result = runner.invoke(eidos_cli.app, ["run-agent", "utility", "build"])
    assert "Performed build" in result.stdout


def test_interactive_exit() -> None:
    with patch.object(Prompt, "ask", side_effect=["exit"]):
        result = runner.invoke(eidos_cli.app, ["interactive"])
    assert result.exit_code == 0

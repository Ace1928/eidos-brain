from unittest.mock import patch
from pathlib import Path
import subprocess
import sys

from core.engine import Engine
from labs import repl


def test_engine_add_and_reflect() -> None:
    engine = Engine()
    engine.execute("add", "note")
    result = engine.execute("reflect")
    assert "note" in result


def test_repl_quick_exit() -> None:
    with patch("rich.prompt.Prompt.ask", side_effect=["exit"]):
        repl.main()


def test_repl_add_and_reflect(tmp_path: Path) -> None:
    memory_file = tmp_path / "mem.txt"
    with patch(
        "rich.prompt.Prompt.ask", side_effect=["add hello", "reflect", "exit"]
    ), patch("rich.console.Console.print") as mock_print:
        repl.main(save=str(memory_file))
        output = "".join(call.args[0] for call in mock_print.call_args_list)
    assert "hello" in output
    assert memory_file.exists()


def test_repl_cli_help() -> None:
    result = subprocess.run(
        [sys.executable, "labs/repl.py", "--help"], capture_output=True, text=True
    )
    assert result.returncode == 0
    assert "Eidos interactive REPL" in result.stdout

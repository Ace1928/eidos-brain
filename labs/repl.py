"""Interactive REPL powered by :class:`rich` and the :class:`Engine`."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rich.console import Console
from rich.prompt import Prompt

from core.engine import Engine
from labs.tutorial_app import load_memory, save_memory


class REPL:
    """Run a simple read-eval-print loop using an :class:`Engine`."""

    def __init__(self, engine: Engine, console: Console | None = None) -> None:
        self.engine = engine
        self.console = console or Console()

    def loop(self) -> None:
        """Begin interactive input processing."""
        self.console.print("[bold underline]Eidos REPL[/]")
        while True:
            cmdline = Prompt.ask("?>").strip()
            if not cmdline:
                continue
            command, *args = cmdline.split()
            if command in {"exit", "quit"}:
                break
            output = self.engine.execute(command, *args)
            self.console.print(output)


def build_parser() -> ArgumentParser:
    """Return an argument parser for the CLI."""
    parser = ArgumentParser(description="Eidos interactive REPL")
    parser.add_argument("--load", help="Memory file to load", default=None)
    parser.add_argument("--save", help="Memory file to save on exit", default=None)
    return parser


def main(load: str | None = None, save: str | None = None) -> None:
    """Entry point for the REPL application."""
    console = Console()
    engine = Engine()
    if load:
        load_memory(engine.core, Path(load), console)
    REPL(engine, console).loop()
    if save:
        save_memory(engine.core, Path(save), console)


if __name__ == "__main__":
    args = build_parser().parse_args()
    main(load=args.load, save=args.save)

"""Typer-based CLI for Eidos operations."""

from __future__ import annotations

from pathlib import Path
import typer
from rich.console import Console
from rich.prompt import Prompt

from core.eidos_core import EidosCore
from agents import UtilityAgent, ExperimentAgent


app = typer.Typer(help="Eidos command-line interface")
console = Console()
core = EidosCore()


def load_memory(path: Path) -> None:
    """Load memories from ``path`` if it exists."""
    if path.exists():
        core.memory = path.read_text().splitlines()
        console.print(f"Loaded {len(core.memory)} memories from {path}.")


def save_memory(path: Path) -> None:
    """Persist memories to ``path``."""
    path.write_text("\n".join(map(str, core.memory)))
    console.print(f"Memories saved to {path}.")


@app.command()
def add_memory(data: str) -> None:
    """Add ``data`` to memory."""
    core.remember(data)
    console.print("Memory added.")


@app.command()
def reflect() -> None:
    """Display all current memories."""
    console.print(core.reflect())


@app.command()
def run_agent(agent: str, task: str) -> None:
    """Run a specific agent with ``task``."""
    if agent == "utility":
        result = UtilityAgent().perform_task(task)
    elif agent == "experiment":
        result = ExperimentAgent().run(task)
    else:
        raise typer.BadParameter("agent must be 'utility' or 'experiment'")
    console.print(result)


@app.command()
def interactive() -> None:
    """Enter an interactive loop for memory operations."""
    console.print("[bold underline]Interactive Mode[/]")
    while True:
        action = Prompt.ask(
            "Action", choices=["add", "reflect", "recurse", "exit"], default="exit"
        )
        if action == "add":
            experience = Prompt.ask("Enter experience")
            core.remember(experience)
            console.print("Experience stored.")
        elif action == "reflect":
            console.print(core.reflect())
        elif action == "recurse":
            core.recurse()
            console.print("Reflection complete.")
        elif action == "exit":
            break


if __name__ == "__main__":
    app()

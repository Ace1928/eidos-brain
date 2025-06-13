"""Interactive tutorial showcasing EidosCore usage."""

from pathlib import Path
import argparse
import sys

from rich.console import Console
from rich.prompt import Prompt

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.eidos_core import EidosCore


def load_memory(core: EidosCore, path: Path, console: Console) -> None:
    """Load memories from ``path`` if it exists."""
    try:
        if path.exists():
            items = path.read_text().splitlines()
            core.memory.extend(items)
            console.print(f"Loaded {len(items)} memories from {path}.")
        else:
            console.print(f"[yellow]No memory file at {path}, starting fresh.")
    except OSError as exc:
        console.print(f"[red]Failed to load memory: {exc}")


def save_memory(core: EidosCore, path: Path, console: Console) -> None:
    """Persist memories to ``path``."""
    try:
        path.write_text("\n".join(map(str, core.memory.get_all())))
        console.print(f"Memories saved to {path}.")
    except OSError as exc:
        console.print(f"[red]Failed to save memory: {exc}")


def main(load: str | None = None, save: str | None = None) -> None:
    """Run the tutorial application."""
    console = Console()
    core = EidosCore()

    if load:
        load_memory(core, Path(load), console)
    console.print("[bold underline]Eidos Interactive Tutorial[/]")
    while True:
        console.print("\nChoose an action: [add, reflect, recurse, exit]")
        action = Prompt.ask("Action", choices=["add", "reflect", "recurse", "exit"])
        if action == "add":
            experience = Prompt.ask("Enter experience")
            core.remember(experience)
            console.print("Experience stored.")
        elif action == "reflect":
            console.print(f"[cyan]Memories:[/] {core.reflect()}")
        elif action == "recurse":
            core.recurse()
            console.print("Reflection complete. Insights appended.")
        elif action == "exit":
            console.print("Goodbye!")
            break

    if save:
        save_memory(core, Path(save), console)


def build_parser() -> argparse.ArgumentParser:
    """Return an argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="Eidos interactive tutorial")
    parser.add_argument("--load", help="Path to memory file to load", default=None)
    parser.add_argument("--save", help="Path to save memories on exit", default=None)
    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    main(load=args.load, save=args.save)

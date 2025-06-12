"""Interactive tutorial showcasing EidosCore usage."""

from rich.console import Console
from rich.prompt import Prompt

from core.eidos_core import EidosCore


def main() -> None:
    """Run the tutorial application."""
    console = Console()
    core = EidosCore()
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


if __name__ == "__main__":
    main()

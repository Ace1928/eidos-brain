# Templates

## Function Template
```python
def function_name(param1: Type, param2: Type) -> ReturnType:
    """Brief description of the function."""
    # Logic goes here
    pass
```

## Class Template
```python
class ClassName:
    """One-line summary of class purpose."""

    def __init__(self, arg: Type) -> None:
        self.arg = arg
```

## CLI Application Template
```python
from rich.console import Console
from rich.prompt import Prompt

def main() -> None:
    """Entry point for interactive command-line tools."""
    console = Console()
    console.print("Welcome", style="bold")
    Prompt.ask("Press enter to continue")

if __name__ == "__main__":
    main()
```

## CLI Argument Parsing Template
```python
import argparse


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Return command-line arguments for the application."""
    parser = argparse.ArgumentParser(description="My tool description")
    parser.add_argument("--option", help="An example option")
    return parser.parse_args(args)


def main() -> None:
    args = parse_args()
    # Access parsed options via ``args.option``


if __name__ == "__main__":
    main()
```

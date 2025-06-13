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

## Persistence Template
```python
from pathlib import Path

def save_data(data: list[str], path: Path) -> None:
    """Write each item in ``data`` to ``path`` separated by newlines."""
    path.write_text("\n".join(data))

def load_data(path: Path) -> list[str]:
    """Return newline-separated entries from ``path`` if it exists."""
    return path.read_text().splitlines() if path.exists() else []
```

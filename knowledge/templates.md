# Templates

Use these snippets in conjunction with the strategies found in
`recursive_patterns.md`. Any terminology used below is defined in
`glossary_reference.md`.

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

## Test Template
```python
def test_feature() -> None:
    """Verify a specific behavior."""
    result = function_under_test()
    assert result == expected
```

## Recursive Summary Template
```python
def recursive_summary(items: list[Any], chunk_size: int = 10) -> str:
    """Condense ``items`` into a short summary."""
    if len(items) <= chunk_size:
        return "; ".join(map(str, items))
    chunks = [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]
    summaries = [recursive_summary(chunk, chunk_size) for chunk in chunks]
    return recursive_summary(summaries, chunk_size)
```

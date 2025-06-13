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

## Integration Test Template
```python
def test_integration(tmp_path: Path) -> None:
    """Exercise multiple modules working together."""
    result = cli_entrypoint("--output", tmp_path / "out.txt")
    assert (tmp_path / "out.txt").exists()
    assert "Success" in result
```

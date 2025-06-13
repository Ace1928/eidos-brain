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

## Fuzz Test Template
```python
import sys
import pytest

atheris = pytest.importorskip("atheris")
atheris.instrument_all()


def fuzz_one_input(data: bytes) -> None:
    """Handle fuzzed ``data`` for the target function."""
    # target_function consumes arbitrary input
    target_function(data)


def test_fuzz() -> None:
    """Run Atheris fuzzing with a limited number of iterations."""
    atheris.Setup(sys.argv + ["-runs=10"], fuzz_one_input)
    with pytest.raises(SystemExit):
        atheris.Fuzz()
```

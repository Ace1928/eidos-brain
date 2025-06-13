# Templates

## Function Template
```python
def function_name(param1: Type, param2: Type) -> ReturnType:
    """One-line summary of the function.

    Parameters
    ----------
    param1 : Type
        Explanation of the first parameter.
    param2 : Type
        Explanation of the second parameter.

    Returns
    -------
    ReturnType
        Description of the returned value.
    """
    # Logic goes here
    pass
```

## Class Template
```python
class ClassName:
    """One-line summary of class purpose.

    Attributes
    ----------
    arg : Type
        Description of the argument stored on the instance.
    """

    def __init__(self, arg: Type) -> None:
        self.arg = arg
```

## Docstring Style Guidelines

- Use **Numpy-style** docstrings with explicit ``Parameters`` and ``Returns``
  sections.
- Keep the first line as a concise summary, followed by a blank line.
- Include type hints in the function signature and mirror them in the docstring
  for clarity.
- Document class attributes in an ``Attributes`` section inside the class
  docstring.

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

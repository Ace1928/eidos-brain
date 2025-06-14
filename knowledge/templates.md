# Templates

Use these snippets in conjunction with the strategies found in
`recursive_patterns.md`. Any terminology used below is defined in
`glossary_reference.md`.

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

## Test Template
```python
def test_feature() -> None:
    """Verify a specific behavior."""
    result = function_under_test()
    assert result == expected
```

## Dockerfile Template
```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "labs/tutorial_app.py"]
```

## WSGI API Template
```python
from wsgiref.simple_server import make_server

from core.health import HealthChecker


def create_app(checker: HealthChecker | None = None):
    """Return a WSGI application with a health endpoint."""

    checker = checker or HealthChecker()

    def app(environ, start_response):
        if environ.get("PATH_INFO") == "/healthz":
            start_response("200 OK", [("Content-Type", "application/json")])
            return [b'{"status": "ok"}']
        start_response("404 Not Found", [])
        return [b""]

    return app


def run_server() -> None:
    with make_server("0.0.0.0", 8000, create_app()) as server:
        server.serve_forever()
```

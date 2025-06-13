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

## Knowledge Graph Template
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Node:
    name: str
    type: str

@dataclass(frozen=True)
class Fact:
    subject: Node
    predicate: str
    obj: Node

class KnowledgeGraph:
    def __init__(self) -> None:
        self.facts: list[Fact] = []

    def add_fact(
        self,
        subject: str,
        predicate: str,
        obj: str,
        *,
        subject_type: str = "entity",
        object_type: str = "entity",
    ) -> None:
        self.facts.append(
            Fact(Node(subject, subject_type), predicate, Node(obj, object_type))
        )

    def query(self, subject: str | None = None, predicate: str | None = None) -> list[Fact]:
        return [f for f in self.facts if f.subject.name == subject and f.predicate == predicate]
```

"""Generate a glossary of symbols within the codebase."""

from __future__ import annotations

import ast
from pathlib import Path

OUTPUT_PATH = Path("knowledge/glossary_reference.md")
SOURCE_DIRS = ["core", "agents", "labs"]


def extract_symbols(path: Path) -> list[tuple[str, str]]:
    """Return a list of (symbol, kind) pairs defined in a file."""
    symbols: list[tuple[str, str]] = []
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            symbols.append((node.name, "class"))
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    symbols.append((f"{node.name}.{item.name}", "method"))
        elif isinstance(node, ast.FunctionDef):
            symbols.append((node.name, "function"))
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.isupper():
                    symbols.append((target.id, "constant"))
    return symbols


def scan_codebase() -> dict[str, list[str]]:
    """Scan source directories for symbols grouped by kind."""
    glossary: dict[str, list[str]] = {
        "class": [],
        "function": [],
        "method": [],
        "constant": [],
    }
    for directory in SOURCE_DIRS:
        for path in Path(directory).glob("*.py"):
            for name, kind in extract_symbols(path):
                glossary[kind].append(name)
    return glossary


def write_glossary(glossary: dict[str, list[str]]) -> None:
    """Write collected symbols to the glossary file."""
    plural_map = {
        "class": "Classes",
        "function": "Functions",
        "method": "Methods",
        "constant": "Constants",
    }
    lines = ["# Glossary Reference", ""]
    for kind, names in glossary.items():
        header = plural_map.get(kind, kind.title() + "s")
        lines.append(f"## {header}")
        for name in sorted(set(names)):
            lines.append(f"- {name}")
        lines.append("")
    OUTPUT_PATH.write_text("\n".join(lines))


def main() -> None:
    """Entry point for glossary generation."""
    glossary = scan_codebase()
    write_glossary(glossary)


if __name__ == "__main__":
    main()

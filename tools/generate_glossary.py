"""Generate a glossary of symbols within the codebase with descriptions."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

OUTPUT_PATH = Path("knowledge/glossary_reference.md")
SOURCE_DIRS = ["core", "agents", "labs"]

ICON_MAP = {
    "class": "\U0001f3f7\ufe0f",
    "function": "\u2699\ufe0f",
    "constant": "\U0001f516",
}


@dataclass
class GlossaryEntry:
    """Container for glossary information."""

    name: str
    description: str


def extract_symbols(path: Path) -> list[tuple[str, str, str]]:
    """Return a list of ``(symbol, kind, description)`` defined in ``path``."""

    symbols: list[tuple[str, str, str]] = []
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            doc = ast.get_docstring(node) or ""
            desc = doc.splitlines()[0] if doc else ""
            symbols.append((node.name, "class", desc))
        elif isinstance(node, ast.FunctionDef):
            doc = ast.get_docstring(node) or ""
            desc = doc.splitlines()[0] if doc else ""
            symbols.append((node.name, "function", desc))
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.isupper():
                    desc = ""
                    if isinstance(node.value, ast.Constant) and isinstance(
                        node.value.value, str
                    ):
                        desc = node.value.value.splitlines()[0]
                    if not desc:
                        desc = f"Constant defined in {path.name}"
                    symbols.append((target.id, "constant", desc))
    return symbols


def scan_codebase() -> dict[str, list[GlossaryEntry]]:
    """Scan source directories for symbols grouped by kind."""

    glossary: dict[str, list[GlossaryEntry]] = {
        "class": [],
        "function": [],
        "constant": [],
    }
    for directory in SOURCE_DIRS:
        for path in Path(directory).glob("*.py"):
            for name, kind, desc in extract_symbols(path):
                glossary[kind].append(GlossaryEntry(name, desc))
    return glossary


def write_glossary(glossary: dict[str, list[GlossaryEntry]]) -> None:
    """Write collected symbols and descriptions to ``OUTPUT_PATH``."""

    plural_map = {
        "class": "Classes",
        "function": "Functions",
        "constant": "Constants",
    }
    lines = ["# Glossary Reference", ""]
    for kind, entries in glossary.items():
        header = plural_map.get(kind, kind.title() + "s")
        lines.append(f"## {header}")
        icon = ICON_MAP.get(kind, "")
        for entry in sorted(entries, key=lambda e: e.name):
            line = f"- {icon} **{entry.name}**"
            if entry.description:
                line += f" - {entry.description}"
            lines.append(line)
        lines.append("")
    OUTPUT_PATH.write_text("\n".join(lines))


def main() -> None:
    """Entry point for glossary generation."""
    glossary = scan_codebase()
    write_glossary(glossary)


if __name__ == "__main__":
    main()

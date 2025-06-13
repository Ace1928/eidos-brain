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
        elif isinstance(node, ast.FunctionDef):
            symbols.append((node.name, "function"))
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.isupper():
                    symbols.append((target.id, "constant"))
    return symbols


def scan_codebase() -> dict[str, list[str]]:
    """Scan source directories for symbols grouped by kind."""
    glossary: dict[str, list[str]] = {"class": [], "function": [], "constant": []}
    for directory in SOURCE_DIRS:
        for path in Path(directory).glob("*.py"):
            for name, kind in extract_symbols(path):
                glossary[kind].append(name)
    return glossary


def write_glossary(glossary: dict[str, list[str]], output: Path) -> None:
    """Write collected symbols to ``output``."""
    plural_map = {"class": "Classes", "function": "Functions", "constant": "Constants"}
    lines = ["# Glossary Reference", ""]
    for kind, names in glossary.items():
        header = plural_map.get(kind, kind.title() + "s")
        lines.append(f"## {header}")
        for name in sorted(set(names)):
            lines.append(f"- {name}")
        lines.append("")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines))


def main(output_path: str | None = None) -> None:
    """Entry point for glossary generation."""
    glossary = scan_codebase()
    output = Path(output_path) if output_path else OUTPUT_PATH
    write_glossary(glossary, output)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate symbol glossary")
    parser.add_argument("--output", default=None, help="Output file path")
    args = parser.parse_args()
    main(args.output)

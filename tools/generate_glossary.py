"""Generate a glossary of symbols within the codebase."""

from __future__ import annotations

import argparse
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


def scan_codebase(directories: list[str] | None = None) -> dict[str, list[str]]:
    """Scan ``directories`` for symbols grouped by kind."""

    if directories is None:
        directories = SOURCE_DIRS
    glossary: dict[str, list[str]] = {"class": [], "function": [], "constant": []}
    for directory in directories:
        for path in Path(directory).glob("*.py"):
            for name, kind in extract_symbols(path):
                glossary[kind].append(name)
    return glossary


def write_glossary(
    glossary: dict[str, list[str]], output: str | Path | None = None
) -> None:
    """Write collected symbols to ``output`` path."""

    output_path = Path(output or OUTPUT_PATH)
    plural_map = {"class": "Classes", "function": "Functions", "constant": "Constants"}
    lines = ["# Glossary Reference", ""]
    for kind, names in glossary.items():
        header = plural_map.get(kind, kind.title() + "s")
        lines.append(f"## {header}")
        for name in sorted(set(names)):
            lines.append(f"- {name}")
        lines.append("")
    output_path.write_text("\n".join(lines))


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Return parsed arguments for CLI usage."""

    # Advanced usage: allow custom directories and output path

    parser = argparse.ArgumentParser(description="Generate a glossary of symbols")
    parser.add_argument(
        "--output",
        default=str(OUTPUT_PATH),
        help="Path to write the glossary file",
    )
    parser.add_argument(
        "directories",
        nargs="*",
        default=SOURCE_DIRS,
        help="Directories to scan for source files",
    )
    return parser.parse_args(args)


def main(
    output: str | Path | None = None, directories: list[str] | None = None
) -> None:
    """Entry point for glossary generation."""

    glossary = scan_codebase(directories)
    # ``write_glossary`` persists the scan results for external review
    write_glossary(glossary, output)


if __name__ == "__main__":
    args = parse_args()
    main(output=args.output, directories=args.directories)

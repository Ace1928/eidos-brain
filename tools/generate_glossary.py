"""Generate a glossary of symbols within the codebase.

This script can be invoked from the command line. It scans Python files in the
provided directories and writes a markdown table of discovered classes,
functions, and constants. Command-line arguments allow overriding the default
output path and directories so CI pipelines can direct output as needed.
"""

from __future__ import annotations

import ast
import argparse
from pathlib import Path

DEFAULT_OUTPUT_PATH = Path("knowledge/glossary_reference.md")
DEFAULT_SOURCE_DIRS = ["core", "agents", "labs"]


def extract_symbols(path: Path) -> list[tuple[str, str]]:
    """Return a list of ``(symbol, kind)`` pairs defined in ``path``."""
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


def scan_codebase(directories: list[str]) -> dict[str, list[str]]:
    """Scan ``directories`` for symbols grouped by kind."""
    glossary: dict[str, list[str]] = {"class": [], "function": [], "constant": []}
    for directory in directories:
        for path in Path(directory).glob("*.py"):
            for name, kind in extract_symbols(path):
                glossary[kind].append(name)
    return glossary


def write_glossary(glossary: dict[str, list[str]], output: Path) -> None:
    """Write collected ``glossary`` entries to ``output``."""
    plural_map = {"class": "Classes", "function": "Functions", "constant": "Constants"}
    lines = ["# Glossary Reference", ""]
    for kind, names in glossary.items():
        header = plural_map.get(kind, kind.title() + "s")
        lines.append(f"## {header}")
        for name in sorted(set(names)):
            lines.append(f"- {name}")
        lines.append("")
    output.write_text("\n".join(lines))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Return CLI arguments for glossary generation."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="File to write the glossary markdown to",
    )
    parser.add_argument(
        "--dirs",
        "-d",
        nargs="+",
        default=DEFAULT_SOURCE_DIRS,
        help="Directories to scan for symbols",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Entry point for glossary generation."""
    args = parse_args(argv)
    glossary = scan_codebase(list(args.dirs))
    write_glossary(glossary, args.output)


if __name__ == "__main__":
    main()

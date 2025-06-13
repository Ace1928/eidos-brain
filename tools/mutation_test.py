"""CLI wrapper for running mutmut mutation tests."""

from __future__ import annotations

import argparse
import subprocess

from rich.console import Console


def run_mutmut(no_cache: bool = False) -> int:
    """Run mutmut and return its exit code."""
    cmd = ["mutmut", "run"]
    if no_cache:
        cmd.append("--no-cache")
    return subprocess.call(cmd)


def build_parser() -> argparse.ArgumentParser:
    """Return an argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="Execute mutation tests with mutmut")
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Disable cache for a full mutation run",
    )
    return parser


def main() -> None:
    """Entry point for mutation test execution."""
    console = Console()
    parser = build_parser()
    args = parser.parse_args()
    code = run_mutmut(no_cache=args.no_cache)
    if code == 0:
        console.print("All mutations survived.", style="green")
    else:
        console.print("Mutation test failures detected.", style="red")
    raise SystemExit(code)


if __name__ == "__main__":
    main()

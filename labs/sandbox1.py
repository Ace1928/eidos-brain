#!/usr/bin/env python
"""Sandbox for quick experiments.

This file demonstrates advanced command-line argument parsing to control
initial experience and recursion depth. Use it as a playground for
interacting with :class:`EidosCore`.
"""

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.eidos_core import EidosCore


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Return parsed CLI options for the sandbox."""

    parser = argparse.ArgumentParser(description="Sandbox for quick Eidos experiments")
    parser.add_argument(
        "--initial",
        default="initial experience",
        help="Seed memory with this experience",
    )
    parser.add_argument(
        "--cycles",
        type=int,
        default=1,
        help="Number of recursion cycles to perform",
    )
    return parser.parse_args(args)


def main(initial: str = "initial experience", cycles: int = 1) -> None:
    """Run the sandbox with the given settings."""

    core = EidosCore()
    core.remember(initial)
    # Perform multiple recursion cycles for deeper insights
    for _ in range(max(1, cycles)):
        core.recurse()
    print(core.reflect())


if __name__ == "__main__":
    cli_args = parse_args()
    main(initial=cli_args.initial, cycles=cli_args.cycles)

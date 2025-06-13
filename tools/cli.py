"""Unified command-line interface for Eidos tools."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from labs import tutorial_app
from tools import generate_glossary, logbook_entry


class Command:
    """Base interface for CLI commands."""

    name: str = ""
    help: str = ""

    @staticmethod
    def add_arguments(parser: argparse.ArgumentParser) -> None:
        """Hook for command specific arguments."""

    def run(self, args: argparse.Namespace) -> None:
        """Execute the command."""
        raise NotImplementedError

    @classmethod
    def build_parser(cls, subparsers: argparse._SubParsersAction) -> None:
        """Register ``cls`` with ``subparsers``."""
        parser = subparsers.add_parser(cls.name, help=cls.help)
        cls.add_arguments(parser)
        parser.set_defaults(command_cls=cls)


class TutorialCommand(Command):
    """Launch the interactive tutorial."""

    name = "tutorial"
    help = "Run the tutorial application"

    @staticmethod
    def add_arguments(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--load", help="Path to memory file to load", default=None)
        parser.add_argument(
            "--save", help="Path to save memories on exit", default=None
        )

    def run(self, args: argparse.Namespace) -> None:
        tutorial_app.main(load=args.load, save=args.save)


class GlossaryCommand(Command):
    """Generate the glossary reference."""

    name = "glossary"
    help = "Update glossary_reference.md"

    @staticmethod
    def add_arguments(parser: argparse.ArgumentParser) -> None:
        """No custom arguments."""

    def run(self, args: argparse.Namespace) -> None:
        glossary = generate_glossary.scan_codebase()
        generate_glossary.write_glossary(glossary)


class LogbookCommand(Command):
    """Append an entry to the logbook."""

    name = "logbook"
    help = "Add a new logbook entry"

    @staticmethod
    def add_arguments(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("message", help="Summary line for the logbook entry")
        parser.add_argument("--next", dest="next_target", help="Optional next target")
        parser.add_argument(
            "--logbook",
            type=Path,
            default=logbook_entry.LOGBOOK_PATH,
            help="Path to the logbook file",
        )

    def run(self, args: argparse.Namespace) -> None:
        logbook_entry.append_entry(args.message, args.next_target, args.logbook)


COMMANDS = [TutorialCommand, GlossaryCommand, LogbookCommand]


def build_parser() -> argparse.ArgumentParser:
    """Return a parser with all subcommands registered."""
    parser = argparse.ArgumentParser(description="Eidos command-line interface")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for cmd in COMMANDS:
        cmd.build_parser(subparsers)
    return parser


def main(argv: list[str] | None = None) -> None:
    """Entry point for the unified CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)
    command_cls: type[Command] = args.command_cls
    command_cls().run(args)


if __name__ == "__main__":
    main()

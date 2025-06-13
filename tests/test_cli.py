from tools import cli


def test_parser_has_subcommands() -> None:
    parser = cli.build_parser()
    ns = parser.parse_args(["glossary"])
    assert ns.command_cls is cli.GlossaryCommand

    ns = parser.parse_args(["logbook", "msg"])
    assert ns.command_cls is cli.LogbookCommand
    assert ns.message == "msg"

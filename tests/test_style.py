import subprocess


def test_style():
    assert (
        subprocess.run(
            [
                "ruff",
                "format",
                "--check",
                "core",
                "agents",
                "labs",
                "tools",
                "tests",
            ],
            check=False,
        ).returncode
        == 0
    )
    assert (
        subprocess.run(
            ["ruff", "check", "core", "agents", "labs", "tools", "tests"],
            check=False,
        ).returncode
        == 0
    )
    assert (
        subprocess.run(
            ["mypy", "core", "agents", "labs", "tools", "tests"],
            check=False,
        ).returncode
        == 0
    )

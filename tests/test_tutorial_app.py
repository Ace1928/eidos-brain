from unittest.mock import patch

from labs import tutorial_app


def test_main_exits_quickly():
    with patch("rich.prompt.Prompt.ask", side_effect=["exit"]):
        tutorial_app.main()

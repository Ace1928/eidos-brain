from tools.generate_glossary import main
from pathlib import Path


def test_generate_glossary(tmp_path: Path):
    glossary_file = tmp_path / "glossary.md"
    orig_output = main.__globals__["OUTPUT_PATH"]
    main.__globals__["OUTPUT_PATH"] = glossary_file
    try:
        main()
        content = glossary_file.read_text()
        assert "EidosCore" in content
        assert "UtilityAgent" in content
    finally:
        main.__globals__["OUTPUT_PATH"] = orig_output

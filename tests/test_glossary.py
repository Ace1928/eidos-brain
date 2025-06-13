from tools.generate_glossary import main
from pathlib import Path


def test_generate_glossary(tmp_path: Path):
    glossary_file = tmp_path / "glossary.md"
    main(["--output", str(glossary_file), "--dirs", "core", "agents", "labs"])
    content = glossary_file.read_text()
    assert "EidosCore" in content
    assert "UtilityAgent" in content

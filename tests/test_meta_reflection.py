import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.meta_reflection import MetaReflection


def test_analyze_list_summary() -> None:
    ref = MetaReflection()
    result = ref.analyze([1, 2, 3])
    assert result["summary"] == "contains 3 items"
    assert result["type"] == "list"


def test_analyze_dict_summary() -> None:
    ref = MetaReflection()
    result = ref.analyze({"a": 1, "b": 2})
    assert result["summary"] == "mapping with 2 keys"
    assert result["type"] == "dict"


def test_analyze_long_string() -> None:
    ref = MetaReflection()
    data = "x" * 30
    result = ref.analyze(data)
    assert result["summary"].startswith("20 chars preview:")
    assert result["length"] == len(data)

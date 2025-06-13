import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.meta_reflection import MetaReflection


def test_numeric_summary():
    mr = MetaReflection()
    result = mr.analyze(42)
    assert result["summary"] == "integer value 42"


def test_nested_dict_summary():
    mr = MetaReflection()
    data = {"a": 1, "b": {"c": 2}}
    result = mr.analyze(data)
    assert "depth 2" in result["summary"]

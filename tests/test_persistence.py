import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.persistence import (
    save_vector_memory,
    load_vector_memory,
    save_knowledge_graph,
    load_knowledge_graph,
)


def test_vector_memory_roundtrip(tmp_path):
    memory = [[0.1, 0.2], [3.4, 5.6]]
    file = tmp_path / "vectors.json"
    save_vector_memory(memory, file)
    loaded = load_vector_memory(file)
    assert loaded == memory


def test_vector_memory_missing(tmp_path):
    file = tmp_path / "missing.json"
    loaded = load_vector_memory(file)
    assert loaded == []


def test_graph_roundtrip(tmp_path):
    graph = {"A": ["B"], "B": ["A", "C"]}
    file = tmp_path / "graph.json"
    save_knowledge_graph(graph, file)
    loaded = load_knowledge_graph(file)
    assert loaded == graph


def test_graph_missing(tmp_path):
    file = tmp_path / "none.json"
    loaded = load_knowledge_graph(file)
    assert loaded == {}

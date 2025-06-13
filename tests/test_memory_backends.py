from core.eidos_core import EidosCore
from core.memory import VectorMemory, KnowledgeGraph


def test_eidos_core_with_vector_memory() -> None:
    core = EidosCore(VectorMemory())
    core.remember("a")
    assert core.reflect() == ["a"]


def test_eidos_core_with_knowledge_graph() -> None:
    core = EidosCore(KnowledgeGraph())
    core.remember("node")
    memories = core.reflect()
    assert "node" in memories

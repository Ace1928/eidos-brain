from core.vector_memory import VectorMemory


def test_add_and_query_single() -> None:
    vm = VectorMemory()
    vm.add([1.0, 0.0], "a")
    assert vm.query([1.0, 0.0]) == ["a"]


def test_query_orders_by_similarity() -> None:
    vm = VectorMemory()
    vm.add([1.0, 0.0], "first")
    vm.add([0.0, 1.0], "second")
    results = vm.query([0.9, 0.1], top_k=2)
    assert results == ["first", "second"]

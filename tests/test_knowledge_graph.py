from core.knowledge_graph import KnowledgeGraph


def test_add_and_query_fact() -> None:
    graph = KnowledgeGraph()
    graph.add_fact("Alice", "knows", "Bob", subject_type="person", object_type="person")
    results = graph.query(subject="Alice", predicate="knows")
    assert len(results) == 1
    fact = results[0]
    assert fact.subject.name == "Alice"
    assert fact.obj.name == "Bob"
    assert fact.subject.type == "person"
    assert fact.obj.type == "person"


def test_query_filters() -> None:
    graph = KnowledgeGraph()
    graph.add_fact("Alice", "knows", "Bob", subject_type="person", object_type="person")
    graph.add_fact("Alice", "owns", "Car", subject_type="person", object_type="object")
    know_results = graph.query(predicate="knows")
    own_results = graph.query(object_type="object")
    assert len(know_results) == 1
    assert know_results[0].predicate == "knows"
    assert len(own_results) == 1
    assert own_results[0].predicate == "owns"

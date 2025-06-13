from core.llm_adapter import LLMAdapter


def test_query_echoes_prompt():
    adapter = LLMAdapter()
    result = adapter.query("hello")
    assert result == "Suggestion: hello"

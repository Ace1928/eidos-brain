from core.long_context_adapter import LongContextAdapter


def test_summarize_batches() -> None:
    adapter = LongContextAdapter(chunk_size=2)
    data = ["a", "b", "c"]
    summaries = adapter.summarize(data)
    assert len(summaries) == 2
    assert all(isinstance(s, str) for s in summaries)


def test_summary_contains_preview() -> None:
    adapter = LongContextAdapter(chunk_size=1)
    summaries = adapter.summarize(["hello world"])
    assert "chars preview" in summaries[0]

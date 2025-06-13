from core.memory_summary import MemorySummarizer


def test_recursive_summary():
    data = list(range(10))
    summarizer = MemorySummarizer(chunk_size=3)
    summary = summarizer.summarize(data)
    assert isinstance(summary, str)
    assert "items" in summary

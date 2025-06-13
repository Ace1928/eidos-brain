import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.security import RateLimiter, filter_sensitive_content


def test_filter_sensitive_content() -> None:
    text = "token=SECRET"
    result = filter_sensitive_content(text, ["SECRET"])
    assert result == "token=[REDACTED]"


def test_rate_limiter_blocks(monkeypatch) -> None:
    times = iter([0.0, 0.1, 0.2])
    monkeypatch.setattr("core.security.monotonic", lambda: next(times))
    limiter = RateLimiter(2, 1.0)
    assert limiter.allow()
    assert limiter.allow()
    assert not limiter.allow()

"""Protection utilities for LLM interactions."""

from __future__ import annotations

from collections import deque
from time import monotonic
from typing import Callable, TypeVar

T = TypeVar("T")


class RateLimiter:
    """Limit the number of allowed operations within a time window."""

    def __init__(self, max_calls: int, period: float) -> None:
        self.max_calls = max_calls
        self.period = period
        self._timestamps: deque[float] = deque()

    def allow(self) -> bool:
        """Return ``True`` if another call is permitted."""
        now = monotonic()
        while self._timestamps and now - self._timestamps[0] > self.period:
            self._timestamps.popleft()
        if len(self._timestamps) < self.max_calls:
            self._timestamps.append(now)
            return True
        return False

    def wrap(self, func: Callable[..., T]) -> Callable[..., T]:
        """Return ``func`` wrapped with rate limiting."""

        def wrapped(*args: object, **kwargs: object) -> T:
            if not self.allow():
                raise RuntimeError("Rate limit exceeded")
            return func(*args, **kwargs)

        return wrapped


def filter_sensitive_content(text: str, secrets: list[str]) -> str:
    """Return ``text`` with each secret replaced by ``"[REDACTED]"``."""
    for secret in secrets:
        text = text.replace(secret, "[REDACTED]")
    return text

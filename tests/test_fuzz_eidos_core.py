import sys
import pytest

atheris = pytest.importorskip("atheris")
atheris.instrument_all()

from core.eidos_core import EidosCore


def _fuzz_input(data: bytes) -> None:
    """Feed fuzzed bytes into :class:`EidosCore`."""
    core = EidosCore()
    fdp = atheris.FuzzedDataProvider(data)
    if fdp.ConsumeBool():
        value = fdp.ConsumeUnicodeNoSurrogates(64)
    else:
        value = {fdp.ConsumeUnicodeNoSurrogates(5): fdp.ConsumeUnicodeNoSurrogates(5)}
    try:
        core.process_cycle(value)
    except Exception:
        pass


def test_fuzz_engine() -> None:
    """Run a short fuzzing session to stress input handling."""
    atheris.Setup(sys.argv + ["-runs=50"], _fuzz_input)
    with pytest.raises(SystemExit) as exc:
        atheris.Fuzz()
    assert exc.value.code == 0

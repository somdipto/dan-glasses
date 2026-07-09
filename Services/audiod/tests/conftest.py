"""Pytest conftest for the audiod test package.

Pins the package root and the absolute config path so tests work from
any pytest cwd.

Why both this and ``audiod/conftest.py`` exist
----------------------------------------------
``audiod/conftest.py`` prepends the audiod package directory to
``sys.path`` so test files can ``from capture import ...`` etc. It is
loaded by pytest when the rootdir is at or below the audiod dir (e.g.
``pytest tests/`` from the audiod root, or ``pytest
Services/audiod/tests/`` from the dan-glasses root).

But pytest sets rootdir to the *invocation* dir by default. If the
operator runs ``pytest .`` from inside ``Services/audiod/tests/``,
rootdir is that directory and the conftest *above* it is not loaded —
test collection fails with ``ModuleNotFoundError: No module named
'capture'``. This conftest lives *inside* the test directory so pytest
sees it regardless of rootdir, and it does the same sys.path prepend.

It also exposes a session-scoped ``audiod_config_path`` fixture that
points at ``Services/audiod/config.yaml`` for the few tests that load
the live config file (was previously a relative ``open("config.yaml")``
that broke when run from outside the audiod root).
"""
import sys
from pathlib import Path

_PACKAGE_DIR = str(Path(__file__).resolve().parent.parent)

if _PACKAGE_DIR not in sys.path:
    sys.path.insert(0, _PACKAGE_DIR)

_CONFIG_PATH = str(Path(_PACKAGE_DIR) / "config.yaml")


import pytest  # noqa: E402  (placed after sys.path tweak on purpose)


@pytest.fixture(scope="session")
def audiod_config_path() -> str:
    """Absolute path to ``Services/audiod/config.yaml``.

    Tests that previously did ``open("config.yaml")`` should depend on
    this fixture so the path resolves correctly from any pytest cwd.
    """
    return _CONFIG_PATH


def _live_audiod_on_8090() -> bool:
    """True if the live audiod daemon is bound on :8090 in this env.

    Full-suite runs of the audiod test package hammer whisper-cli
    back-to-back. The live audiod daemon (which is always on in the
    dev Zo Computer) is itself a whisper-cli consumer with its own
    ALSA capture thread, and shares the 3-core / 4GB host. With both
    active simultaneously, individual ``WhisperTranscriber.transcribe``
    calls in the JFK real-audio class can exceed the production
    adaptive timeout (15s + 3s * duration) and trip ``whisper
    timeout``, which is then asserted as a failure on the keyword
    match.

    The JFK tests are the canary real-audio regression suite. They
    prove whisper.cpp is wired correctly. They do not need to prove
    that two whisper-cli processes can run in parallel inside 4GB of
    RAM -- that's a production runtime concern, not a unit-test
    concern. Skip them when the live daemon is bound so the suite
    remains deterministic; they pass cleanly when the daemon is
    stopped, and they pass in isolation regardless (the in-test
    subprocess is uncontended).
    """
    import socket as _socket
    try:
        with _socket.create_connection(("127.0.0.1", 8090), timeout=0.25):
            return True
    except OSError:
        return False


@pytest.fixture(autouse=True)
def _skip_real_audio_when_live_daemon(request):
    """Skip real-audio JFK class when the live audiod is on :8090.

    The ``TestRealAudioJFK`` class is the only one that needs this
    treatment; the synthetic-chirp tests in ``test_whisper_e2e.py``
    run in ~50ms each and do not contend for whisper resources.
    """
    cls_name = getattr(request.cls, "__name__", "")
    if cls_name == "TestRealAudioJFK" and _live_audiod_on_8090():
        pytest.skip(
            "live audiod is bound on :8090; JFK real-audio class is "
            "skipped to avoid whisper-cli contention (4GB / 3-core host)"
        )
    yield

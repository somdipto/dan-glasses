"""Pytest conftest for the audiod test package.

Pins the package root and the absolute config path so tests work from
any pytest cwd.

Why both this and ``audiod/conftest.py`` exist
---------------------------------------------
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

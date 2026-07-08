"""Pytest conftest for audiod.

Makes the audiod package directory importable from tests/ without forcing
every test file to do its own ``sys.path.insert(0, ...)``, and exposes
the absolute path to ``config.yaml`` so tests never have to use a
relative path that breaks when run from any cwd other than the package
root.

Background
----------
Tests live in ``tests/`` and import service modules as top-level names
(``from transcription import WhisperTranscriber``,
``from audiod import HealthHandler``). That only works when the audiod
package directory is on ``sys.path`` at collection time.

Without this conftest, ``pytest tests/`` from the audiod root sees the
``tests/`` collection root first and raises
``ModuleNotFoundError: No module named 'transcription'`` on import. The
historical workaround was a per-file ``sys.path.insert`` in
``test_silence_e2e.py``; the rest of the suite would silently fail
collection unless the runner happened to invoke pytest from a directory
where the package was already on ``sys.path``.

This conftest prepends the package directory (the directory containing
this file) to ``sys.path`` at the start of the pytest session, so
``pytest tests/`` from the audiod root Just Works. It is a no-op if the
directory is already on ``sys.path`` (e.g. the user exported
``PYTHONPATH`` or invoked pytest with ``--rootdir`` elsewhere).

It also defines the ``audiod_config_path`` fixture (and module-level
``AUDIOD_CONFIG_PATH`` constant) so tests that need to load the real
``config.yaml`` can do so without a relative path.
"""
import sys
from pathlib import Path

import pytest

_PACKAGE_DIR = str(Path(__file__).resolve().parent)
_AUDIOD_CONFIG_PATH = str(Path(_PACKAGE_DIR) / "config.yaml")

if _PACKAGE_DIR not in sys.path:
    sys.path.insert(0, _PACKAGE_DIR)


@pytest.fixture
def audiod_config_path():
    """Absolute path to audiod's ``config.yaml`` regardless of cwd.

    Tests that previously did ``open("config.yaml", "r")`` broke as soon
    as pytest was invoked from any directory other than the audiod
    package root. Use this fixture, or the module-level
    ``AUDIOD_CONFIG_PATH`` constant exported from this conftest, instead.
    """
    return _AUDIOD_CONFIG_PATH

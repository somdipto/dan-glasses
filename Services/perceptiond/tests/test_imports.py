"""v13.1 — import smoke tests.

Verifies the package can be imported as `perceptiond` from a non-cwd context,
which is what `pytest tests/` triggers. Earlier versions used absolute sibling
imports (`from capture import V4L2Capture`) and broke under pytest collection.
"""
import importlib
import sys

import perceptiond  # noqa: F401  — conftest.py sets up sys.path


def test_package_imports():
    assert hasattr(perceptiond, "PerceptionPipeline")
    assert hasattr(perceptiond, "SceneGate")


def test_version_constant():
    assert hasattr(perceptiond, "__version__")
    parts = perceptiond.__version__.split(".")
    assert len(parts) == 3
    assert int(parts[0]) >= 13


def test_sibling_modules_importable():
    """All siblings must be importable as part of the package."""
    for mod in ("capture", "salience", "vlm", "events", "config"):
        full = f"perceptiond.{mod}"
        importlib.import_module(full)


def test_perceptiond_module_reexports():
    from perceptiond.perceptiond import (
        PerceptionPipeline,
        SceneGate,
        DescriptionPublisher,
        FrameStore,
        PerceptiondServer,
    )
    assert PerceptionPipeline is not None
    assert SceneGate is not None
    assert DescriptionPublisher is not None
    assert FrameStore is not None
    assert PerceptiondServer is not None

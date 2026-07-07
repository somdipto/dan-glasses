"""perceptiond — Dan Glasses vision pipeline service.

Re-exports the public surface so callers can `from perceptiond import ...`
without reaching into perceptiond.py directly.
"""

from .perceptiond import (
    PerceptionPipeline,
    SceneGate,
)


__all__ = ["PerceptionPipeline", "SceneGate"]

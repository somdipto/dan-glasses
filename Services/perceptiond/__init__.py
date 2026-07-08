"""perceptiond — Dan Glasses vision pipeline service.

Re-exports the public surface so callers can `from perceptiond import ...`
without reaching into perceptiond.py directly.
"""

from .perceptiond import (
    PerceptionPipeline,
    SceneGate,
)

__version__ = "13.1.0"

__all__ = ["PerceptionPipeline", "SceneGate", "__version__"]

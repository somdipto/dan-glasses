"""pytest configuration for perceptiond.

Ensures the package root is on sys.path so tests can `from perceptiond import ...`
regardless of the working directory pytest is invoked from.

v13.1: fixes import path so the entire test suite (64+ tests) is collectable.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

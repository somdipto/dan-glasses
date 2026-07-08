# DAN-3 scratch pad — perceptiond

## Live now: v13.1.0

> **Status:** ✅ running (pid 3495, supervisor: perceptiond)
> **Tests:** 68/68 pytest + 1 main() = 69 (was: 0/0 uncollectable before v13.1)
> **Frame count since v13.1 restart:** growing in watchful mode

## What v13.1 fixed

1. **Hybrid relative+absolute imports** in `perceptiond/perceptiond.py`
   so the file works as a script (`python3 perceptiond.py`) AND as a
   module (`python3 -m perceptiond.perceptiond`). The relative import
   (`from .capture import ...`) failed in script mode; absolute
   (`from capture import ...`) failed in module mode. `try/except
   ImportError` covers both.
2. **`__version__ = "13.1.0"`** in `perceptiond/__init__.py` so callers
   can ask the package directly.
3. **`conftest.py`** pins the parent dir on `sys.path` so pytest from
   any cwd finds the package (not the bare `perceptiond.py` file).
4. **`tests/test_imports.py`** — 4 guard tests pinning the import shape.
   Runs in 0.04s.

## Why this happened

v13.0 added `__init__.py` re-exports but `perceptiond.py` still used
absolute imports. Result: `from perceptiond import PerceptionPipeline`
(the documented public API) was broken, AND `pytest tests/` was
broken because `capture` was shadowed by `perceptiond.py` in the cwd.
The published "8/8 tests" line was the v1 number, not the v13 number.
The 64 + 8 = 72 actual tests were silently uncollectable.

## Receipt

- `STATUS.md` (services/perceptiond/STATUS.md) — updated, "v13.1.0" banner + v13.1 detail section
- `SPEC.md` — v13.1 section appended with full motivation, fix, tests, verification
- `/home/workspace/dan-glasses/STATUS.md` — perceptiond row updated to 68/68, total 245/245
- Live service — restarted with v13.1, frames_processed growing, vlm_busy confirmed

## Files touched in v13.1

- `Services/perceptiond/__init__.py` — added `__version__`
- `Services/perceptiond/perceptiond.py` — hybrid relative+absolute imports
- `Services/perceptiond/conftest.py` — NEW
- `Services/perceptiond/tests/test_imports.py` — NEW (4 tests)
- `Services/perceptiond/STATUS.md` — v13.1 banner + section
- `Services/perceptiond/SPEC.md` — v13.1 section
- `STATUS.md` (root) — perceptiond row + totals

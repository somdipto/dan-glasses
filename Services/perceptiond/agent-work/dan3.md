# DAN-3 scratch pad — perceptiond v13.1

## Current state (read on 2026-07-08)

- Service live on :8092, supervisor pid 111, mode watchful
- Status JSON shows v13.0 features working: frame_events, descriptions, image_store
- LFM2.5-VL-450M llama-mtmd-cli running, vlm_invocations=1, vlm_busy=true
- Memory sink wired to localhost:8741/memories

## Bug found: tests are uncollectable

`__init__.py` does `from .perceptiond import ...` (package mode).
`perceptiond.py` does `from capture import ...` (cwd mode).
Production works because supervisord sets cwd to the service dir, so `capture` is
on `sys.path[0]`. But pytest runs from `tests/`, so `capture` isn't findable.

```
ERROR collecting test_perceptiond.py
__init__.py:7: in <module>
    from .perceptiond import (
perceptiond.py:20: in <module>
    from capture import V4L2Capture
E   ModuleNotFoundError: No module named 'capture'
```

This means **STATUS.md's "64/64 pytest + 1 main() = 65" is fictional** — the
suite has been unrunnable for some time.

## Plan: ship v13.1 — fix imports + hermetic conftest

1. Convert all module-level sibling imports in `perceptiond.py` to relative:
   `from .capture import V4L2Capture` etc.
2. Make `__init__.py` lazy / re-export stable public API.
3. Add `conftest.py` at repo root (`/home/workspace/dan-glasses/conftest.py`)
   so pytest from any cwd can find the service modules.
4. Add a `pytest.ini` or `pyproject.toml` for the test runner config.
5. Run the suite. Confirm 64/64 actually pass. Update STATUS.md truthfully.
6. Bump version to v13.1.0 in `perceptiond.py` and `STATUS.md`.

## Why v13.1 not v14

The task brief is already implemented. v13.1 is a quality / correctness patch,
not a feature. Don't over-scope.

## What I am NOT doing

- Not adding new endpoints, not changing VLM model, not touching capture
  pipeline, not refactoring events.py (109K LOC monolith, too risky solo).
- Not "improving" salience algorithm. Watchful mode works.
- Not touching the Tauri app — bridge is wired at v13.0.

## Decisions

- Relative imports via `.` package style (matches `__init__.py`).
- `conftest.py` at dan-glasses/ root so all 5 services' tests can use it.
- Do not add new tests in v13.1. Just make existing ones pass.

## After v13.1

If there's time, optionally:
- Add 1-2 tests that lock down the import path itself (would have caught this)
- Bump live service and verify with `/status`

Time-box: 30 min. Ship.

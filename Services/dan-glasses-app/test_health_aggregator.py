"""Tests for /api/services/health aggregator and SPA-side persistence wiring.

What this pins:
  1. The server exposes GET /api/services/health that fans out to every
     backend (memoryd, toold, ttsd, audiod, perceptiond) in parallel and
     returns a uniform JSON envelope { ok, up_count, down_count, total_latency_ms,
     services: { <id>: { ok, status, latency_ms, body, error } } }.
  2. The response is fast enough that the wizard can poll it every 3s without
     starving the page (top wall-clock under 1.5s end-to-end).
  3. The wizard's services.ts exports HEALTH_PATHS and APP_HEALTH_AGGREGATOR_PATH,
     and BootstrapWizard.tsx imports at least the aggregator path.
  4. The wizard persists bootstrap step state under the localStorage key
     'dan-glasses:bootstrap:v1' so reloads don't lose progress.

Runs as plain pytest — no daemon or browser required for static checks; the
live aggregator probe uses the running dan-glasses-app on :8747 and tolerates
services being down (down_count > 0, not a hard failure).

Run: pytest test_health_aggregator.py -v
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import pytest

SRC = Path("/home/workspace/dan-glasses/apps/dan-glasses-app/src")
SERVICES_TS = SRC / "lib" / "services.ts"
WIZARD = SRC / "components" / "BootstrapWizard.tsx"
APP_URL = "http://127.0.0.1:8747"

EXPECTED_SERVICES = {"memoryd", "toold", "ttsd", "audiod", "perceptiond"}


# ---------- Live aggregator probe ----------

def test_aggregator_endpoint_exists():
    """GET /api/services/health returns 200 + JSON envelope, not 404."""
    import urllib.request
    import urllib.error

    req = urllib.request.Request(f"{APP_URL}/api/services/health", method="GET")
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            assert resp.status == 200, f"expected 200, got {resp.status}"
            ct = resp.headers.get("Content-Type", "")
            assert "application/json" in ct, f"expected json, got {ct!r}"
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        pytest.fail(f"aggregator returned HTTP {e.code}: {e.read()!r}")

    assert data["ok"] is True, f"unexpected: {data!r}"
    assert isinstance(data["up_count"], int)
    assert isinstance(data["down_count"], int)
    assert EXPECTED_SERVICES.issubset(set(data["services"].keys())), (
        f"missing services in response: {EXPECTED_SERVICES - set(data['services'])}"
    )


def test_aggregator_returns_per_service_envelope():
    """Each per-service slot has the same shape: ok, status, latency_ms, body, error."""
    import urllib.request

    with urllib.request.urlopen(f"{APP_URL}/api/services/health", timeout=5) as resp:
        data = json.loads(resp.read())

    for svc_id, slot in data["services"].items():
        assert "ok" in slot, f"{svc_id}: missing 'ok'"
        assert "status" in slot, f"{svc_id}: missing 'status'"
        assert "latency_ms" in slot, f"{svc_id}: missing 'latency_ms'"
        assert "body" in slot, f"{svc_id}: missing 'body'"
        assert "error" in slot, f"{svc_id}: missing 'error'"
        assert isinstance(slot["latency_ms"], (int, float)), (
            f"{svc_id}: latency_ms should be numeric, got {type(slot['latency_ms'])}"
        )


def test_aggregator_concurrent_enough():
    """Five sequential fetches would take ~5*RTT. Aggregator should finish <1.5s.

    Five 10ms RTTs in series = 50ms. Five in parallel = ~10-30ms. We allow a
    loose 1.5s budget to absorb cold start, but anything > that means the
    fan-out is broken (sequential fallback) or one service is hanging.
    """
    import urllib.request

    start = time.perf_counter()
    with urllib.request.urlopen(f"{APP_URL}/api/services/health", timeout=5) as resp:
        data = json.loads(resp.read())
    wall = (time.perf_counter() - start) * 1000
    assert wall < 1500, f"aggregator took {wall:.0f}ms — fan-out is probably sequential"
    # The server's reported total_latency_ms should be <= wall (it's the sum
    # of fan-out time, not including the round-trip from us to the SPA server).
    assert data["total_latency_ms"] <= wall + 50, (
        f"server total_latency_ms={data['total_latency_ms']} > wall={wall:.0f}ms+50"
    )


def test_aggregator_up_count_matches_ok_flags():
    """up_count + down_count == len(services) and matches per-slot ok flags."""
    import urllib.request

    with urllib.request.urlopen(f"{APP_URL}/api/services/health", timeout=5) as resp:
        data = json.loads(resp.read())

    ok_count = sum(1 for s in data["services"].values() if s["ok"])
    assert data["up_count"] == ok_count, (
        f"up_count={data['up_count']} but {ok_count} slots report ok=true"
    )
    assert data["up_count"] + data["down_count"] == len(data["services"]), (
        "up_count + down_count should equal total services"
    )


# ---------- Static checks: services.ts ----------

def test_services_ts_exports_health_paths():
    """HEALTH_PATHS map exists and covers all 5 services."""
    content = SERVICES_TS.read_text()
    assert "HEALTH_PATHS" in content, "services.ts must export HEALTH_PATHS"
    for svc in EXPECTED_SERVICES:
        assert svc in content, f"HEALTH_PATHS missing {svc}"


def test_services_ts_exports_aggregator_path():
    """APP_HEALTH_AGGREGATOR_PATH constant exists and points at the right route."""
    content = SERVICES_TS.read_text()
    assert "APP_HEALTH_AGGREGATOR_PATH" in content, (
        "services.ts must export APP_HEALTH_AGGREGATOR_PATH"
    )
    assert "/api/services/health" in content, (
        "APP_HEALTH_AGGREGATOR_PATH must contain '/api/services/health'"
    )


# ---------- Static checks: BootstrapWizard.tsx ----------

def test_wizard_imports_aggregator_path():
    """BootstrapWizard imports APP_HEALTH_AGGREGATOR_PATH from services.ts."""
    content = WIZARD.read_text()
    assert "APP_HEALTH_AGGREGATOR_PATH" in content, (
        "BootstrapWizard.tsx must import APP_HEALTH_AGGREGATOR_PATH"
    )


def test_wizard_persists_step_state():
    """Wizard writes step state to localStorage so reloads don't lose progress.

    Pin: storage key is 'dan-glasses:bootstrap:v1', the persistence uses
    localStorage.getItem/setItem, and there's a load effect on mount.
    """
    content = WIZARD.read_text()
    assert "dan-glasses:bootstrap:v1" in content, (
        "expected localStorage key 'dan-glasses:bootstrap:v1' to appear in BootstrapWizard"
    )
    assert "localStorage.setItem" in content, "wizard must save step state"
    assert "localStorage.getItem" in content, "wizard must restore step state on mount"


def test_wizard_uses_aggregator_in_poll():
    """The 3s poll builds its URL from APP_HEALTH_AGGREGATOR_PATH, not 5 separate /health hits."""
    content = WIZARD.read_text()
    # The wizard should NOT have 5 separate `apiBase(PORTS.*) + '/health'` calls
    # left in the live poll. Tolerate a few remaining for the per-step detail
    # fetches, but the live-status tick should be the aggregator.
    health_call_count = content.count("/health")
    assert health_call_count <= 2, (
        f"wizard still calls /health {health_call_count} times — should use aggregator"
    )


# ---------- Regression: server.py imports ----------

def test_server_uses_concurrent_futures():
    """server.py uses ThreadPoolExecutor or asyncio.gather for fan-out."""
    server = Path("/home/workspace/dan-glasses/Services/dan-glasses-app/server.py")
    content = server.read_text()
    assert "ThreadPoolExecutor" in content or "asyncio.gather" in content, (
        "server.py must use a concurrent fan-out (ThreadPoolExecutor or asyncio.gather)"
    )


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))

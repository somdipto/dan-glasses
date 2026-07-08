"""Regression tests for the services.ts single-source-of-truth refactor.

Why: the React components used to hardcode `http://127.0.0.1:PORT` literals
for memoryd / toold / ttsd / perceptiond. We extracted them into
`apps/dan-glasses-app/src/lib/services.ts` so a new daemon or port change
is one line, not five. These tests prove the refactor stuck:

- No component still embeds the full base URL as a default-arg literal.
- The shared module exports a port for every service the wizard needs.
- apiBase / wsBase produce the exact strings the components used before.
- SERVICE_URLS is the new single point of truth and is not duplicated.

Runs as plain pytest — no daemon or browser required.

Run: pytest test_services_ts_refactor.py -v
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

SRC = Path(
    "/home/workspace/dan-glasses/apps/dan-glasses-app/src"
)
COMPONENTS = SRC / "components"
SERVICES_TS = SRC / "lib" / "services.ts"

# Components that talk directly to local daemons. LiveTranscript and
# BootstrapWizard used to be in this set; after the refactor they import
# helpers from services.ts and don't carry the literal any more.
COMPONENTS_WITH_DIRECT_BASEURL = [
    "MemoryPanel.tsx",
    "TtsPanel.tsx",
    "VisionDashboard.tsx",
]

# Pattern: any URL that starts with http://127.0.0.1:PORT.
# Matches the old "http://127.0.0.1:8741" form AND the new
# `apiBase(PORTS.memoryd)` form. We want ONLY the literal form to be
# banned in default arg positions; inline calls to apiBase() are fine.
_DIRECT_BASEURL_LITERAL = re.compile(r"['\"`]http://127\.0\.0\.1:(\d+)['\"`]")
_DEFAULT_ARG = re.compile(
    r"=\s*['\"`]http://127\.0\.0\.1:(\d+)['\"`]\s*"
)
_ALL_SERVICES = {"memoryd", "toold", "ttsd", "audiod", "perceptiond"}
_DEFAULT_PORTS = {"memoryd": 8741, "toold": 8742, "ttsd": 8743, "audiod": 8090, "perceptiond": 8092}


# --- 1. The shared module exists and exports the right shape -------------


def test_services_ts_exists():
    assert SERVICES_TS.is_file(), f"missing: {SERVICES_TS}"


def test_services_ts_exports_required_symbols():
    text = SERVICES_TS.read_text(encoding="utf-8")
    for name in ("ServiceId", "PORTS", "apiBase", "wsBase", "SERVICE_URLS", "ALL_SERVICES", "serviceUrl"):
        assert re.search(rf"^export\s+(?:const|function|type|interface)\s+{name}\b", text, re.M), (
            f"services.ts is missing export: {name}"
        )


@pytest.mark.parametrize("svc", sorted(_ALL_SERVICES))
def test_services_ts_has_port_for_every_service(svc: str):
    text = SERVICES_TS.read_text(encoding="utf-8")
    # PORTS block must have a line like "memoryd: 8741,"
    assert re.search(rf"\b{svc}\s*:\s*\d+", text), (
        f"services.ts is missing PORTS entry for {svc}"
    )


@pytest.mark.parametrize(
    "svc,port",
    sorted(_DEFAULT_PORTS.items()),
)
def test_services_ts_default_ports_unchanged(svc: str, port: int):
    """If a port ever moves, the wizard would silently break in the
    browser. These pins catch the change loudly."""
    text = SERVICES_TS.read_text(encoding="utf-8")
    m = re.search(rf"\b{svc}\s*:\s*(\d+)", text)
    assert m is not None, f"services.ts missing PORTS for {svc}"
    assert int(m.group(1)) == port, (
        f"port for {svc} drifted: was {port}, now {m.group(1)}. "
        "Update test_services_ts_refactor.py and any supervisor configs."
    )


# --- 2. No component embeds the full URL as a default arg literal ---------


@pytest.mark.parametrize("component", COMPONENTS_WITH_DIRECT_BASEURL)
def test_no_baseurl_literal_in_default_arg(component: str):
    """MemoryPanel / TtsPanel / VisionDashboard used to declare
    `baseUrl = 'http://127.0.0.1:8741'` as a default prop. That
    duplicates the URL. The refactor moves them to `SERVICE_URLS.x`."""
    path = COMPONENTS / component
    assert path.is_file(), f"missing: {path}"
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith(("//", "*", "/*")):
            continue
        m = _DEFAULT_ARG.search(line)
        if m:
            pytest.fail(
                f"{component}:{lineno} has a hardcoded default base URL: "
                f"{line.strip()!r}. Use `baseUrl = SERVICE_URLS.<svc>` from "
                f"lib/services.ts instead."
            )


# --- 3. Components do import from services.ts ----------------------------


@pytest.mark.parametrize("component", COMPONENTS_WITH_DIRECT_BASEURL)
def test_component_imports_from_services_ts(component: str):
    path = COMPONENTS / component
    text = path.read_text(encoding="utf-8")
    assert re.search(r"from\s+['\"]\.\./lib/services['\"]", text), (
        f"{component} does not import from ../lib/services — the refactor "
        f"requires it to consume SERVICE_URLS from the shared module."
    )


def test_bootstrap_wizard_imports_from_services_ts():
    text = (COMPONENTS / "BootstrapWizard.tsx").read_text(encoding="utf-8")
    assert "from '../lib/services'" in text
    assert "apiBase" in text
    assert "ALL_SERVICES" in text


def test_live_transcript_imports_wsbase():
    text = (COMPONENTS / "LiveTranscript.tsx").read_text(encoding="utf-8")
    assert "wsBase" in text, "LiveTranscript should use shared wsBase() helper"


# --- 4. serviceUrl composes the right strings ----------------------------


def test_serviceurl_strips_and_rejoins_path():
    """The wizard calls serviceUrl(svc, '/health') — make sure leading
    slash is preserved and bare path is normalized to '/...'."""
    text = SERVICES_TS.read_text(encoding="utf-8")
    assert "serviceUrl" in text
    # The function body must join apiBase(PORTS[svc]) with the path
    assert re.search(r"apiBase\(PORTS\[svc\]\)", text), (
        "serviceUrl must compose from apiBase + PORTS"
    )


# --- 5. All five wizard services have a SERVICE_URLS entry ---------------


@pytest.mark.parametrize("svc", sorted(_ALL_SERVICES))
def test_service_urls_has_entry(svc: str):
    text = SERVICES_TS.read_text(encoding="utf-8")
    # SERVICE_URLS = Object.freeze({ memoryd: apiBase(8741), ... })
    pat = rf"{svc}\s*:\s*apiBase\("
    assert re.search(pat, text), f"SERVICE_URLS missing entry for {svc}"


# --- 6. The single-source-of-truth file lives in lib/ ---------------------


def test_no_services_constant_duplicated_in_components():
    """No component should define its own PORTS, SERVICE_URLS, or apiBase
    object literal. The shared module is the only place those live."""
    forbidden = ("PORTS = {", "SERVICE_URLS = {", "SERVICE_URLS = Object.freeze(")
    for path in COMPONENTS.glob("*.tsx"):
        text = path.read_text(encoding="utf-8")
        for f in forbidden:
            assert f not in text, (
                f"{path.name} duplicates a service-URL constant locally: "
                f"{f!r}. Use lib/services.ts."
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

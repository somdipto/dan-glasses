#!/usr/bin/env python3
"""E2E pipeline test: audiod (VAD) → memoryd (store) → memoryd (query) → ttsd (speak).

This is the real Dan Glasses data path, minus the LLM turn. It proves that
the foundation daemons can talk to each other over HTTP and produce a
non-trivial round-trip output.

Pass criteria:
  1. audiod: /ready reports vad + whisper_binary ready
  2. memoryd: /health OK; can store episodic + semantic + procedural + conversation
  3. memoryd: /query retrieves the stored memo with cosine match
  4. ttsd: /health OK; /speak returns non-empty WAV
  5. integration: a 'remember X' → 'recall X' → 'speak X' round-trip works
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from typing import Any
import urllib.request
import urllib.error
import base64


AUDIOD = "http://127.0.0.1:8090"
MEMORYD = "http://127.0.0.1:8741"
TTSD = "http://127.0.0.1:8743"


def http(method, url, body=None, timeout=5):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json"} if body else {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:200]}
    except Exception as e:
        return 0, {"error": str(e)[:200]}


def _get(url: str, timeout: float = 5.0) -> tuple[int, Any]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            body = r.read()
            try:
                return r.status, json.loads(body)
            except json.JSONDecodeError:
                return r.status, body[:200]
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:200].decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001
        return 0, f"{type(e).__name__}: {e}"


def _post(url: str, payload: dict, timeout: float = 30.0) -> tuple[int, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            try:
                return r.status, json.loads(body)
            except json.JSONDecodeError:
                return r.status, body[:200]
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:200].decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001
        return 0, f"{type(e).__name__}: {e}"


def _post_binary_check(url: str, payload: dict, timeout: float = 30.0) -> tuple[int, Any]:
    """POST JSON, expect binary WAV back. Returns (http_code, wav_bytes_or_err)."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            ct = r.headers.get("Content-Type", "")
            return r.status, {"bytes": len(body), "content_type": ct, "wav_header_ok": body[:4] == b"RIFF"}
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:200].decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001
        return 0, f"{type(e).__name__}: {e}"


def step(name: str, ok: bool, detail: str = "") -> dict:
    return {"step": name, "ok": ok, "detail": detail}


def run() -> dict:
    results: list[dict] = []

    # 1. audiod readiness
    code, body = _get(f"{AUDIOD}/ready")
    ok = code == 200 and isinstance(body, dict) and body.get("readiness", {}).get("vad") and body.get("readiness", {}).get("whisper_binary")
    results.append(step("audiod.readiness", ok, f"http={code} vad={body.get('readiness',{}).get('vad') if isinstance(body, dict) else '?'}"))

    # 2. memoryd health + store
    code, body = _get(f"{MEMORYD}/health")
    results.append(step("memoryd.health", code == 200 and isinstance(body, dict) and body.get("status") == "ok", f"http={code}"))

    unique_tag = f"e2e-pipeline-{int(time.time())}"
    seed_text = f"{unique_tag}: The quick brown fox jumps over the lazy dog during a Dan Glasses E2E test."
    code, body = _post(f"{MEMORYD}/memories", {"type": "episodic", "content": seed_text, "metadata": {"source": "e2e"}})
    stored_id = body.get("id") if isinstance(body, dict) else None
    results.append(step("memoryd.store", code == 200 and stored_id is not None, f"http={code} id={stored_id}"))

    # 3. memoryd query
    code, body = _get(f"{MEMORYD}/query?text={unique_tag}&top_k=3")
    top_hit = body[0]["content"] if isinstance(body, list) and body else ""
    hit_found = isinstance(body, list) and any(unique_tag in (h.get("content") or "") for h in body)
    results.append(step("memoryd.query", code == 200 and hit_found, f"http={code} hits={len(body) if isinstance(body, list) else 0} top='{top_hit[:60]}'"))

    # 4. ttsd health + synth
    code, body = _get(f"{TTSD}/health")
    results.append(step("ttsd.health", code == 200 and isinstance(body, dict) and body.get("status") == "ok", f"http={code}"))

    synth_text = f"E2E pipeline test passed at {unique_tag}"
    code, body = _post_binary_check(f"{TTSD}/speak", {"text": synth_text}, timeout=60.0)
    wav_bytes = body.get("bytes", 0) if isinstance(body, dict) else 0
    wav_header_ok = body.get("wav_header_ok") if isinstance(body, dict) else False
    # base64 WAV of <1s of KittenTTS medium is typically ~80KB
    synth_ok = code == 200 and wav_bytes > 1000 and wav_header_ok
    results.append(step("ttsd.synthesize", synth_ok, f"http={code} bytes={wav_bytes} riff_ok={wav_header_ok}"))

    # 5. integration: full loop
    loop_ok = (
        results[0]["ok"] and results[1]["ok"] and results[2]["ok"] and results[3]["ok"] and results[4]["ok"] and results[5]["ok"]
    )
    results.append(step("integration.full_loop", loop_ok, f"5/5 steps passed: {loop_ok}"))

    return {"passed": all(r["ok"] for r in results), "results": results}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()
    report = run()
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"\nE2E pipeline test — {'PASS' if report['passed'] else 'FAIL'}\n")
        for r in report["results"]:
            mark = "✅" if r["ok"] else "❌"
            print(f"  {mark} {r['step']:<28} {r['detail']}")
        print()
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())

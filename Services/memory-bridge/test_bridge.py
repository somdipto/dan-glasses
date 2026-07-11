#!/usr/bin/env python3
"""Memory-bridge end-to-end test: synthesize one audiod event, POST to memoryd, query back.

Run:  python3 test_bridge.py
Exit: 0 on success, 1 on failure.
"""
import json
import subprocess
import sys
import time
import urllib.request


def http_get(path: str) -> dict | list:
    with urllib.request.urlopen(f"http://127.0.0.1:8741{path}", timeout=5) as r:
        return json.loads(r.read())


def run_inject() -> None:
    """Synthesize one audiod event and POST it to memoryd via the bridge."""
    event_id = f"test-bridge-{int(time.time() * 1000)}"
    subprocess.run(
        ["python3", "memory_bridge.py", "--inject"],
        check=True,
        env={"MEMORYD_URL": "http://127.0.0.1:8741", "PATH": "/usr/bin:/bin"},
    )
    print(f"[ok] inject succeeded for event_id={event_id}")


def main() -> int:
    print("[1/3] running bridge --inject (synthesize audiod event → memoryd)...")
    run_inject()
    print("[2/3] querying memoryd for the inject content...")
    hits = http_get("/query?text=DAN1+bridge+inject&top_k=2")
    if not isinstance(hits, list) or not hits:
        print(f"[fail] no query results; got: {hits}")
        return 1
    top = hits[0]
    if "DAN1 bridge inject" not in top.get("content", ""):
        print(f"[fail] top hit does not contain inject text: {top}")
        return 1
    print(f"[ok] memoryd id={top['id']} score={top['score']:.3f} content={top['content']!r}")
    print("[3/3] verifying supervisor still happy...")
    out = subprocess.run(
        ["supervisorctl", "-c", "/etc/zo/supervisord-user.conf", "status", "memory-bridge", "audiod", "memoryd"],
        capture_output=True, text=True,
    )
    print(out.stdout.strip())
    if "RUNNING" not in out.stdout:
        print("[fail] some supervised service not running")
        return 1
    print("\n[done] memory-bridge E2E green")
    return 0


if __name__ == "__main__":
    sys.exit(main())

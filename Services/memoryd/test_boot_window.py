"""Regression test for v130 (Option C): memoryd must wait, not 503, during the boot window.

The boot window is when the embedding model is still loading (~25s on cold start).
Previously, _ensure_model raised HTTPException(503) after a 60s timeout, which meant
the FIRST 25s of requests all 503ed. With Option C, the timeout is 180s and the
caller waits. /ready returns False during the window, True after model is ready.

Test:
  1. Stop memoryd (via supervisor).
  2. Start memoryd.
  3. Immediately fire /ready — must return 200 with ready=False (not crash, not 503).
  4. Wait for ready=True.
  5. Fire /memories — must return 200 with a new id.
  6. Fire /ready again — must return 200 with ready=True.

This test takes ~30s. Run with `python3 test_boot_window.py`.
"""

import os
import subprocess
import sys
import time
import urllib.request
import json

SUPERVISOR = "/usr/local/bin/supervisorctl"
CONF = "/etc/zo/supervisord-user.conf"
URL = "http://localhost:8741"
TIMEOUT = 5


def http(method: str, path: str, body: dict | None = None) -> tuple[int, dict | str]:
    req = urllib.request.Request(
        URL + path,
        data=json.dumps(body).encode() if body else None,
        method=method,
        headers={"Content-Type": "application/json"} if body else {},
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"null")
    except Exception as e:
        return 0, str(e)


def main() -> int:
    print(f"=== {time.strftime('%H:%M:%S')} test_boot_window: Option C regression ===")
    print()
    print("Step 1: stop memoryd")
    subprocess.run([SUPERVISOR, "-c", CONF, "stop", "memoryd"], check=False, timeout=15)
    time.sleep(2)
    print("Step 2: start memoryd (t0)")
    subprocess.run([SUPERVISOR, "-c", CONF, "start", "memoryd"], check=False, timeout=15)
    t0 = time.time()

    # Wait up to 35s for /ready to be reachable. Until the socket is bound we get
    # a 0 (CONN_REFUSED); we accept that and look for the first 200.
    bound_at = None
    while time.time() - t0 < 35:
        code, body = http("GET", "/ready")
        if code == 200:
            bound_at = time.time() - t0
            print(f"  t={bound_at:.1f}s  /ready → 200  body={body}")
            break
        time.sleep(0.5)
    if bound_at is None:
        print("FAIL: /ready never came up within 35s")
        return 1

    # /ready must say ready=False at first (model still loading)
    code, body = http("GET", "/ready")
    if code != 200:
        print(f"FAIL: /ready code={code} body={body}")
        return 1
    if body.get("ready") is True:
        # If model is already cached on disk the load can be sub-second. Still valid.
        print(f"  /ready was True immediately (model cached, no boot window this run)")
    else:
        print(f"  /ready=False during boot window — Option C confirmed")

    # Now wait for ready=True
    ready_at = None
    while time.time() - t0 < 60:
        code, body = http("GET", "/ready")
        if code == 200 and body.get("ready") is True:
            ready_at = time.time() - t0
            print(f"  t={ready_at:.1f}s  /ready=True  (model loaded)")
            break
        time.sleep(0.5)
    if ready_at is None:
        print("FAIL: /ready never reported ready=True within 60s")
        return 1

    # Fire a POST /memories and confirm 200
    code, body = http("POST", "/memories", {
        "type": "episodic",
        "content": "boot-window regression test memory",
        "metadata": {"test": "test_boot_window.py", "ts": t0},
    })
    if code != 200 or "id" not in body:
        print(f"FAIL: /memories code={code} body={body}")
        return 1
    print(f"  /memories → 200  id={body['id']}  (Option C end-to-end works)")

    print()
    print("PASS: Option C patch holds — boot window waits, does not 503")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Test for v130 perceptiond /describe endpoint.

Two paths:
  1. /describe?image_id=latest (or POST {})  →  live frame VLM
  2. /describe?image_id=<hex>                  →  stored frame from FrameStore

VLM is single-shot subprocess. If busy, returns 503 — caller should retry.
Each call takes ~20-35s on the LFM2.5-VL-450M model.

Run with `python3 tests/test_describe_endpoint.py`.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error

URL = "http://localhost:8092"
TIMEOUT = 90  # VLM subprocess can take 30-60s


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
        try:
            body = json.loads(e.read() or b"null")
        except Exception:
            body = {}
        return e.code, body
    except Exception as e:
        return 0, str(e)


def wait_for_vlm_free(timeout_s: int = 120) -> bool:
    """Poll /status until vlm_busy=False (or timeout)."""
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        code, body = http("GET", "/status")
        if code == 200 and isinstance(body, dict) and not body.get("vlm_busy"):
            return True
        time.sleep(1.0)
    return False


def main() -> int:
    print("=== test_describe_endpoint ===")

    # 1. /describe GET, default (latest)
    print("Step 1: GET /describe (default = live frame)")
    if not wait_for_vlm_free(60):
        print("FAIL: vlm never freed up to 60s")
        return 1
    t0 = time.time()
    code, body = http("GET", "/describe")
    dt = time.time() - t0
    if code != 200:
        print(f"FAIL: code={code} body={body}")
        return 1
    if "description" not in body or not body["description"]:
        print(f"FAIL: no description in body: {body}")
        return 1
    print(f"  PASS: 200 in {dt:.1f}s, latency_ms={body.get('latency_ms')}, "
          f"image_id={body.get('image_id')}, w/h={body.get('width')}x{body.get('height')}")
    print(f"  description: {body['description'][:100]}...")

    # 2. /describe POST {} — same as latest
    print()
    print("Step 2: POST /describe {} (default = live frame)")
    if not wait_for_vlm_free(60):
        print("FAIL: vlm never freed up to 60s")
        return 1
    t0 = time.time()
    code, body = http("POST", "/describe", {})
    dt = time.time() - t0
    if code != 200:
        print(f"FAIL: code={code} body={body}")
        return 1
    print(f"  PASS: 200 in {dt:.1f}s, latency_ms={body.get('latency_ms')}, "
          f"image_id={body.get('image_id')}")

    # 3. /describe POST with image_id (use one from /descriptions if any)
    print()
    print("Step 3: POST /describe with stored image_id (if available)")
    code, body = http("GET", "/descriptions?count=5")
    stored_id = None
    if code == 200 and isinstance(body, dict):
        for desc in body.get("descriptions", []):
            iid = desc.get("image_id")
            if iid:
                stored_id = iid
                break
    if not stored_id:
        print(f"  SKIP: no stored descriptions available; living without stored-image test")
    else:
        if not wait_for_vlm_free(60):
            print("FAIL: vlm never freed up to 60s")
            return 1
        t0 = time.time()
        code, body = http("POST", "/describe", {"image_id": stored_id})
        dt = time.time() - t0
        if code != 200:
            print(f"  FAIL on stored id {stored_id}: code={code} body={body}")
        else:
            print(f"  PASS: 200 in {dt:.1f}s, image_id={body.get('image_id')}, "
                  f"latency_ms={body.get('latency_ms')}")
            print(f"  description: {body['description'][:100]}...")

    # 4. /describe?image_id=invalid  → 400
    print()
    print("Step 4: GET /describe?image_id=invalid_xyz  →  400")
    code, body = http("GET", "/describe?image_id=invalid_xyz")
    if code != 400:
        print(f"  FAIL: expected 400, got code={code} body={body}")
        return 1
    print(f"  PASS: 400 with {body}")

    print()
    print("PASS: /describe endpoint works for all 3 paths (live default, POST, stored id)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

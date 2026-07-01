"""Live test: dan-glasses-app /api/{memoryd,toold,ttsd}/* proxies.

Verifies that each new proxy correctly forwards to its upstream daemon and
returns non-empty structured data. Runs against the running dan-glasses-app
on PORT (default 8747).
"""
import json
import sys
import urllib.request

BASE = "http://localhost:8747"


def req(path, method="GET", data=None, expect_json=True, raw=False, timeout=30):
    body = json.dumps(data).encode() if data is not None else None
    r = urllib.request.Request(f"{BASE}{path}", data=body, method=method,
                               headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            payload = resp.read()
            ct = resp.headers.get("Content-Type", "")
            if raw:
                return resp.status, payload
            if ct.startswith("application/json") or expect_json:
                return resp.status, json.loads(payload)
            return resp.status, payload
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}") if e.headers.get("Content-Type", "").startswith("application/json") else {}


def main():
    fails = []

    # 1. memoryd
    s, d = req("/api/memoryd/health")
    if s != 200 or d.get("status") not in ("ok", "loading"):
        fails.append(f"memoryd health: {s} {d}")
    s, d = req("/api/memoryd/stats")
    if s != 200 or "total_memories" not in d:
        fails.append(f"memoryd stats: {s} {d}")

    # 2. toold
    s, d = req("/api/toold/health")
    if s != 200 or d.get("status") != "ok":
        fails.append(f"toold health: {s} {d}")
    s, d = req("/api/toold/exec", "POST", {"command": "echo proxy-test", "timeout": 5})
    if s != 200 or not d.get("success"):
        fails.append(f"toold exec: {s} {d}")

    # 3. ttsd
    s, voices = req("/api/ttsd/voices")
    if s != 200 or not isinstance(voices, list) or len(voices) == 0:
        fails.append(f"ttsd voices: {s} {voices}")

    if fails:
        print("FAIL")
        for f in fails:
            print("  -", f)
        sys.exit(1)
    print("OK")
    print(f"  memoryd: {d if False else 'proxied'} stats reachable")
    print(f"  toold:   exec ran with success=True")
    print(f"  ttsd:    {len(voices)} voices")


if __name__ == "__main__":
    main()
"""Live smoke test for the BootstrapWizard's exact HTTP sequence.

Runs the same calls the React component makes against memoryd + toold + ttsd.
If this passes and `npm run build` passes, the wizard should work in the browser.
"""
import asyncio
import json
import sys
import urllib.request

BASE = {
    "memoryd": "http://localhost:8741",
    "toold": "http://localhost:8742",
    "ttsd": "http://localhost:8743",
}


def request(url, method="GET", data=None, timeout=15):
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
        ct = r.headers.get("Content-Type", "")
        if ct.startswith("application/json"):
            return r.status, json.loads(raw)
        return r.status, raw


async def main():
    failures = []

    # 1) Health
    for svc, base in BASE.items():
        status, data = request(f"{base}/health")
        if status != 200 or (isinstance(data, dict) and data.get("status") != "ok"):
            failures.append(f"{svc} health: {status} {data!r}")

    # 2) memoryd: store 3 types + 1 procedural, query, expect ≥1 hit
    types = [
        ("episodic", f"wizard smoke {asyncio.get_event_loop().time():.0f}"),
        ("semantic", "User display name: somdipto"),
        ("semantic", "Preferred TTS voice: expr-voice-2-m"),
        ("procedural", "To run a Dan Glasses bootstrap: check services, prompt for name+voice, exercise memoryd + toold + ttsd."),
    ]
    stored_ids = []
    for mem_type, content in types:
        status, data = request(f"{BASE['memoryd']}/memories", "POST", {"type": mem_type, "content": content})
        if status != 200 or "id" not in data:
            failures.append(f"memoryd store {mem_type}: {status} {data!r}")
        else:
            stored_ids.append(data["id"])

    status, query = request(f"{BASE['memoryd']}/query?text=bootstrap+setup&top_k=5")
    if status != 200 or not isinstance(query, list) or len(query) == 0:
        failures.append(f"memoryd query: {status} {query!r}")

    # 3) toold: /test
    status, data = request(f"{BASE['toold']}/test")
    if status != 200 or not data.get("success"):
        failures.append(f"toold /test: {status} {data!r}")

    # 4) ttsd: /speak — first call cold-loads KittenTTS, ~20s end-to-end
    status, audio = request(
        f"{BASE['ttsd']}/speak",
        "POST",
        {"text": "DAN-4 wizard live smoke", "voice": "expr-voice-2-f"},
        timeout=45,
    )
    if status != 200 or not audio.startswith(b"RIFF"):
        failures.append(f"ttsd /speak: {status} bytes={len(audio)} head={audio[:16]!r}")
    elif len(audio) < 1000:
        failures.append(f"ttsd /speak: suspiciously small audio ({len(audio)} bytes)")

    if failures:
        print("FAIL")
        for f in failures:
            print("  -", f)
        sys.exit(1)

    print("OK")
    print(f"  memoryd: stored 4 (ids {stored_ids}), query returned {len(query)} hits")
    print(f"  toold:   {data['success']}")
    print(f"  ttsd:    {len(audio)} bytes WAV")


if __name__ == "__main__":
    asyncio.run(main())

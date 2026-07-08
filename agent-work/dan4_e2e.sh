#!/usr/bin/env bash
# Live e2e smoke for the TTS + Memory stream wired into dan-glasses-app.
set -euo pipefail
cd /home/workspace/dan-glasses

echo "=== 1. memoryd stats (via app proxy :8747) ==="
curl -s "http://127.0.0.1:8747/api/memoryd/stats" | python3 -c "
import json, sys
d = json.load(sys.stdin)
print(f'  total_memories: {d[\"total_memories\"]}')
print(f'  by_type: {d[\"by_type\"]}')
print(f'  model_loaded: {d[\"model_loaded\"]}')
"

echo
echo "=== 2. memoryd semantic search for 'tts' (via app proxy, GET ?text=) ==="
curl -s "http://127.0.0.1:8747/api/memoryd/query?text=tts&top_k=3" | python3 -c "
import json, sys
hits = json.load(sys.stdin)
print(f'  hits: {len(hits)}')
for h in hits[:3]:
    print(f'    [{h[\"score\"]:.3f}] ({h[\"type\"]}) {h[\"content\"][:80]}')
"

echo
echo "=== 3. ttsd speak (via app proxy) ==="
curl -s -X POST "http://127.0.0.1:8747/api/ttsd/speak" \
    -H "Content-Type: application/json" \
    -d '{"text": "Dan glasses pipeline is live. Memory and TTS both green."}' \
    -o /tmp/dan4_tts.wav -w "  http: %{http_code}  bytes: %{size_download}  time: %{time_total}s\n"
file /tmp/dan4_tts.wav

echo
echo "=== 4. toold shell exec (via app proxy) ==="
curl -s -X POST "http://127.0.0.1:8747/api/toold/exec" \
    -H "Content-Type: application/json" \
    -d '{"command": "echo dan4-e2e-live", "timeout": 5}' | python3 -c "
import json, sys
d = json.load(sys.stdin)
print(f'  success: {d[\"success\"]}')
print(f'  stdout: {d.get(\"stdout\", \"\").strip()}')
print(f'  duration_ms: {d.get(\"duration_ms\")}')
"

echo
echo "=== 5. services health aggregator ==="
curl -s "http://127.0.0.1:8747/api/services/health" | python3 -c "
import json, sys
d = json.load(sys.stdin)
print(f'  ok: {d[\"up_count\"]} / {d[\"up_count\"] + d[\"down_count\"]}')
print(f'  total_latency_ms: {d[\"total_latency_ms\"]}')
for name, s in d['services'].items():
    print(f'    {name:12s}: {s[\"status\"]} ({s[\"latency_ms\"]}ms)')
"

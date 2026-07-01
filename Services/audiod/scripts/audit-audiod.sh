#!/usr/bin/env bash
# audiod deep audit — health, config drift, model integrity, log errors, WS reachability.
#
# Usage:
#   ./scripts/audit-audiod.sh           # audit live service
#   ./scripts/audit-audiod.sh --json    # emit machine-readable JSON
#
# Exit code 0 = all green, 1 = one or more warnings, 2 = critical failure.
set -uo pipefail

PORT=8090
WS_PORT=8091
ROOT="$(cd "$(dirname "$0")" && pwd)"
# Walk upward to find the dan-glasses/ repo root (where Services/ lives).
CAND="$ROOT"
while [[ "$CAND" != "/" ]]; do
  if [[ -f "$CAND/Services/audiod/config.yaml" ]]; then ROOT="$CAND"; break; fi
  CAND="$(dirname "$CAND")"
done
CONFIG="$ROOT/Services/audiod/config.yaml"
MODEL="/home/workspace/dan-glasses/models/ggml-base.bin"
LOG="/tmp/dan-audiod.log"

JSON_MODE=0
if [[ "${1:-}" == "--json" ]]; then JSON_MODE=1; fi

ok=0
warn=1
crit=2

declare -a FINDINGS

add() {  # level, code, msg
  FINDINGS+=("[$1] $2 — $3")
  if [[ "$1" == "CRIT" ]]; then EXIT=$crit
  elif [[ "$1" == "WARN" ]]; then
    [[ "${EXIT:-0}" != "$crit" ]] && EXIT=$warn || true
  fi
  return 0
}

EXIT=0

# 1. Health
HEALTH=$(curl -s --max-time 2 "http://localhost:$PORT/health" 2>/dev/null || true)
if echo "$HEALTH" | grep -q '"status":"ok"'; then
  add OK HEALTH "/health returned 200"
else
  add CRIT HEALTH "/health unreachable or non-ok: $HEALTH"
fi

# 2. Status
STATUS_JSON=$(curl -s --max-time 2 "http://localhost:$PORT/status" 2>/dev/null || true)
if [[ -n "$STATUS_JSON" ]]; then
  RUNNING=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('running',''))" 2>/dev/null || echo "")
  VAD_READY=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('vad_ready',''))" 2>/dev/null || echo "")
  DROPPED=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('dropped_segments',''))" 2>/dev/null || echo "")
  INFLIGHT=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('transcribe_inflight',''))" 2>/dev/null || echo "")
  Q=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('queue_size',''))" 2>/dev/null || echo "")
  LIVE_PID=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('pid',''))" 2>/dev/null || echo "")

  if [[ "$RUNNING" == "True" ]]; then add OK STATUS "running=True"; else add CRIT STATUS "running=$RUNNING"; fi
  if [[ "$VAD_READY" == "True" ]]; then add OK STATUS "vad_ready=True"; else add CRIT STATUS "vad_ready=$VAD_READY"; fi
  if [[ -n "$DROPPED" && "$DROPPED" -gt 0 ]]; then add WARN STATUS "dropped_segments=$DROPPED"; else add OK STATUS "dropped_segments=$DROPPED"; fi
  if [[ -n "$INFLIGHT" && "$INFLIGHT" -gt 0 ]]; then add WARN STATUS "transcribe_inflight=$INFLIGHT (slow)"; else add OK STATUS "transcribe_inflight=$INFLIGHT"; fi
  if [[ -n "$Q" && "$Q" -gt 5 ]]; then add WARN STATUS "queue_size=$Q (backpressure)"; else add OK STATUS "queue_size=$Q"; fi
else
  add CRIT STATUS "/status unreachable"
fi

# 3. Config drift
if [[ -f "$CONFIG" ]]; then
  EFFECTIVE_DEVICE=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('device',''))" 2>/dev/null || echo "")
  EFFECTIVE_SR=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('sample_rate',''))" 2>/dev/null || echo "")
  EFFECTIVE_MODEL=$(echo "$STATUS_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('whisper_model',''))" 2>/dev/null || echo "")

  CFG_DEVICE=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG'))['audio']['device'])" 2>/dev/null || echo "")
  CFG_SR=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG'))['audio']['sample_rate'])" 2>/dev/null || echo "")
  CFG_MODEL=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG'))['whisper']['model'])" 2>/dev/null || echo "")

  [[ "$CFG_DEVICE" == "$EFFECTIVE_DEVICE" ]] && add OK CONFIG "device matches" || add WARN CONFIG "device drift: file=$CFG_DEVICE live=$EFFECTIVE_DEVICE (run POST /reload)"
  [[ "$CFG_SR" == "$EFFECTIVE_SR" ]] && add OK CONFIG "sample_rate matches" || add WARN CONFIG "sample_rate drift: file=$CFG_SR live=$EFFECTIVE_SR"
  [[ "$CFG_MODEL" == "$EFFECTIVE_MODEL" ]] && add OK CONFIG "whisper model matches" || add WARN CONFIG "whisper model drift: file=$CFG_MODEL live=$EFFECTIVE_MODEL"
else
  add CRIT CONFIG "config.yaml missing at $CONFIG"
fi

# 4. Model integrity
if [[ -f "$MODEL" ]]; then
  SIZE=$(stat -c %s "$MODEL" 2>/dev/null || stat -f %z "$MODEL" 2>/dev/null || echo "0")
  if [[ "$SIZE" -gt 100000000 ]]; then
    add OK MODEL "ggml-base.bin $SIZE bytes"
  else
    add CRIT MODEL "ggml-base.bin unexpectedly small: $SIZE bytes"
  fi
else
  add CRIT MODEL "ggml-base.bin missing at $MODEL"
fi

# 5. WS port reachable
if (echo > /dev/tcp/127.0.0.1/$WS_PORT) 2>/dev/null; then
  add OK WS "port $WS_PORT open"
else
  add WARN WS "port $WS_PORT not reachable (no clients connected is normal; port-down is not)"
fi

# 6. Log scan (last 200 lines). Live process may redirect stdout elsewhere.
LIVE_PID="${LIVE_PID:-}"
if [[ -f "$LOG" ]]; then
  ACTIVE_LOG="$LOG"
elif [[ -n "$LIVE_PID" ]] && [[ -L "/proc/$LIVE_PID/fd/1" ]]; then
  ACTIVE_LOG=$(readlink "/proc/$LIVE_PID/fd/1" 2>/dev/null || true)
fi
if [[ -n "${ACTIVE_LOG:-}" && -f "$ACTIVE_LOG" ]]; then
  ERRORS=$(tail -200 "$ACTIVE_LOG" 2>/dev/null | grep -cE "ERROR|Traceback|Exception" || true)
  if [[ "$ERRORS" -gt 0 ]]; then
    add WARN LOG "$ERRORS error/exception lines in last 200 lines of $ACTIVE_LOG"
  else
    add OK LOG "no errors in last 200 lines of $ACTIVE_LOG"
  fi
else
  add INFO LOG "no log file found (audiod may have been started without redirection)"
fi

# 7. Test suite freshness (last run mtime)
if [[ -d "$ROOT/Services/audiod/.pytest_cache" ]]; then
  add OK TESTS "pytest cache present (last run: $(stat -c %y "$ROOT/Services/audiod/.pytest_cache/v/cache/lastfailed" 2>/dev/null | cut -d. -f1))"
else
  add WARN TESTS "no pytest cache — suite has never been run"
fi

# Output
if [[ "$JSON_MODE" -eq 1 ]]; then
  FINDINGS_JSON="["
  first=1
  for f in "${FINDINGS[@]}"; do
    [[ $first -eq 0 ]] && FINDINGS_JSON+=","
    FINDINGS_JSON+=$(python3 -c "import json,sys; print(json.dumps(sys.argv[1]))" "$f")
    first=0
  done
  FINDINGS_JSON+="]"
  echo "{\"exit\": $EXIT, \"findings\": $FINDINGS_JSON}" | python3 -m json.tool
else
  echo "=== audiod audit ==="
  for f in "${FINDINGS[@]}"; do echo "$f"; done
  echo "---"
  echo "exit: $EXIT (0=green, 1=warn, 2=crit)"
fi

exit $EXIT

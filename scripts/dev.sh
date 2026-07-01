#!/bin/bash
# scripts/dev.sh — bring up the 6 Dan Glasses daemons in order, with health checks.
#
# Usage:
#   ./scripts/dev.sh           # bring everything up
#   ./scripts/dev.sh status    # check status of every service
#   ./scripts/dev.sh stop      # kill every service (graceful SIGTERM)
#
# Each daemon writes its log to /tmp/dan-<name>.log and its pid to /tmp/dan-<name>.pid.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="/tmp"
PY_BIN="${PY_BIN:-python3}"

declare -A SERVICES=(
  [audiod]="$ROOT/Services/audiod/audiod.py"
  [perceptiond]="$ROOT/Services/perceptiond/perceptiond.py"
  [memoryd]="$ROOT/Services/memoryd/memoryd.py"
  [toold]="$ROOT/Services/toold/toold.py"
  [ttsd]="$ROOT/Services/ttsd/ttsd.py"
)

declare -A PORT=(
  [audiod]=8090
  [perceptiond]=8092
  [memoryd]=8741
  [toold]=8742
  [ttsd]=8743
)

start_one() {
  local name="$1"
  local entry="${SERVICES[$name]}"
  local port="${PORT[$name]}"
  local pidfile="$LOG_DIR/dan-$name.pid"
  local logfile="$LOG_DIR/dan-$name.log"

  if curl -s --max-time 1 "http://localhost:$port/health" >/dev/null 2>&1; then
    echo "✓ $name :$port already up"
    return 0
  fi

  if [[ -f "$pidfile" ]] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
    echo "↻ $name stale pid $(cat "$pidfile") — killing"
    kill "$(cat "$pidfile")" || true
    sleep 1
  fi

  echo "→ starting $name :$port (log: $logfile)"
  cd "$ROOT"
  nohup "$PY_BIN" "$entry" >"$logfile" 2>&1 &
  echo $! >"$pidfile"
  sleep 1
  for i in 1 2 3 4 5 6 7 8 9 10; do
    if curl -s --max-time 1 "http://localhost:$port/health" >/dev/null 2>&1; then
      echo "✓ $name healthy after ${i}s"
      return 0
    fi
    sleep 1
  done
  echo "✗ $name did not become healthy within 10s — see $logfile"
  return 1
}

status_all() {
  printf '%-15s %-7s %-7s %s\n' service port status detail
  printf '%-15s %-7s %-7s %s\n' ------- ---- ------ ------
  for name in "${!PORT[@]}"; do
    local port="${PORT[$name]}"
    local resp
    resp=$(curl -s --max-time 1 "http://localhost:$port/health" 2>/dev/null | head -c 80 || echo "")
    if [[ -n "$resp" ]]; then
      printf '%-15s %-7s %-7s %s\n' "$name" "$port" "UP" "$resp"
    else
      printf '%-15s %-7s %-7s %s\n' "$name" "$port" "DOWN" "-"
    fi
  done
  local oc
  oc=$(curl -s --max-time 1 "http://localhost:18789/health" 2>/dev/null | head -c 80 || echo "")
  printf '%-15s %-7s %-7s %s\n' "openclaw" 18789 "$([ -n "$oc" ] && echo UP || echo DOWN)" "$oc"
}

stop_all() {
  for name in "${!SERVICES[@]}"; do
    local pidfile="$LOG_DIR/dan-$name.pid"
    if [[ -f "$pidfile" ]] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
      echo "✗ stopping $name pid $(cat "$pidfile")"
      kill "$(cat "$pidfile")" || true
      rm -f "$pidfile"
    else
      echo "✓ $name not running"
    fi
  done
}

case "${1:-up}" in
  up|start|"")     for name in audiod perceptiond memoryd toold ttsd; do start_one "$name"; done ;;
  status)          status_all ;;
  stop)            stop_all ;;
  restart)         stop_all; for name in audiod perceptiond memoryd toold ttsd; do start_one "$name"; done ;;
  *)               echo "usage: $0 {up|status|stop|restart}"; exit 2 ;;
esac

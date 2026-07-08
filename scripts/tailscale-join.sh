#!/usr/bin/env bash
# tailscale-join.sh — one-shot Tailscale bring-up for dan-glasses Zo Computer
#
# What it does:
#   1. Reads TAILSCALE_AUTHKEY from env (or prompts).
#   2. Brings tailscale up with --ssh + advertise as exit node OFF.
#   3. Serves OpenClaw (:18789) over HTTPS via `tailscale serve` so it's reachable
#      on the tailnet without exposing it publicly.
#
# Idempotent: safe to re-run.
#
# Usage:
#   export TAILSCALE_AUTHKEY=tskey-...
#   ./scripts/tailscale-join.sh
#
# To get an auth key:
#   https://login.tailscale.com/admin/settings/keys  (Generate key, reusable OK)

set -euo pipefail

if ! command -v tailscale >/dev/null 2>&1; then
  echo "❌ tailscale not installed. Install with:"
  echo "   curl -fsSL https://tailscale.com/install.sh | sh"
  exit 1
fi

if [[ -z "${TAILSCALE_AUTHKEY:-}" ]]; then
  echo "❌ TAILSCALE_AUTHKEY not set."
  echo "   Get one at: https://login.tailscale.com/admin/settings/keys"
  echo "   Then: export TAILSCALE_AUTHKEY=tskey-..."
  exit 1
fi

# Already up?  Skip auth but still attempt to serve.
if ! tailscale status --json 2>/dev/null | grep -q '"BackendState":"Running"'; then
  echo "🔌 tailscale up…"
  tailscale up --authkey="$TAILSCALE_AUTHKEY" --ssh --accept-routes
else
  echo "✅ tailscale already up"
fi

echo "🔗 serving openclaw :18789 over tailnet HTTPS…"
tailscale serve --bg --yes 18789 2>/dev/null || {
  echo "❌ tailscale serve failed. Check 'tailscale status' and try:"
  echo "   tailscale serve --reset"
  exit 1
}

echo
echo "🟢 Tailscale status:"
tailscale status
echo
echo "🟢 OpenClaw URL (tailnet only):"
tailscale serve status

#!/usr/bin/env bash
set -euo pipefail
cd /home/workspace/dan-glasses/apps/dan-glasses-app
exec python3 /home/workspace/dan-glasses/Services/dan-glasses-app/server.py

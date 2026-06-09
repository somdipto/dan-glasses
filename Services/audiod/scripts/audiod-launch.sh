#!/bin/bash
# audiod launcher — run from dan-glasses root
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ROOT_PARENT="$(cd "$ROOT_DIR/.." && pwd)"

cd "$ROOT_PARENT"
exec python3 Services/audiod/audiod.py \
    --config Services/audiod/config.yaml \
    --model /home/workspace/dan-glasses/models/ggml-base.bin \
    --port 8090 "$@"

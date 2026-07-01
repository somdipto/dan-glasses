#!/usr/bin/env bash
# download.sh — fetch LFM2.5-VL-450M GGUF for perceptiond
#
# Tries LFM2.5-VL-450M first (Liquid AI vision model).
# Falls back to SmolVLM-256M if LFM2.5-VL-450M not yet released.
#
# Usage:
#   ./download.sh                       # auto-detect best available
#   ./download.sh lfm2.5-vl-450m        # force LFM2.5-VL-450M
#   ./download.sh smolvlm-256m          # force SmolVLM-256M
#   ./download.sh /path/to/dest/        # custom dest dir

set -euo pipefail

DEST="${1:-}"
if [[ -d "$DEST" ]]; then
    :
elif [[ -n "$DEST" && "$DEST" != /* && "$DEST" != *.gguf ]]; then
    DEST="$(pwd)/$DEST"
fi

REPO_ROOT="${DAN_GLABS_REPO:-/home/workspace/danlab-multimodal}"
MODELS_DIR="$REPO_ROOT/models"
mkdir -p "$MODELS_DIR"

log() { echo "[download.sh] $*" >&2; }

# ---- LFM2.5-VL-450M ----
# Liquid AI released Jun 2026; check HF for current artifacts.
# The release page is https://huggingface.co/LiquidAI/LFM2.5-VL-450M
# We try the repo and check what GGUF files are available. If the
# community has a GGUF mirror (e.g. unsloth, mradermacher) we use that.
download_lfm25() {
    local hf_repo="LiquidAI/LFM2.5-VL-450M-GGUF"
    local target="$MODELS_DIR/LFM2.5-VL-450M-Q4_0.gguf"
    local mmproj="$MODELS_DIR/mmproj-LFM2.5-VL-450M-f16.gguf"

    if [[ -f "$target" && -f "$mmproj" ]]; then
        log "LFM2.5-VL-450M already present at $target"
        echo "$target"
        echo "$mmproj"
        return 0
    fi

    log "Probing HuggingFace for $hf_repo..."
    if ! python3 -c "from huggingface_hub import HfApi; HfApi().repo_info('$hf_repo', repo_type='model')" 2>/dev/null; then
        log "LFM2.5-VL-450M GGUF not yet on HF — will use SmolVLM-256M fallback"
        return 1
    fi

    log "Downloading LFM2.5-VL-450M Q4_0..."
    python3 - <<PYEOF
from huggingface_hub import hf_hub_download
import os
for fname, dest in [(
    "LFM2.5-VL-450M-Q4_0.gguf",
    "$target",
), (
    "mmproj-LFM2.5-VL-450M-f16.gguf",
    "$mmproj",
)]:
    if os.path.exists(dest):
        print(f"skip {fname}")
        continue
    hf_hub_download(
        repo_id="$hf_repo",
        filename=fname,
        local_dir="$MODELS_DIR",
    )
PYEOF
    log "LFM2.5-VL-450M ready: $target"
    echo "$target"
    echo "$mmproj"
}

# ---- SmolVLM-256M (fallback) ----
download_smolvlm() {
    local target="$MODELS_DIR/SmolVLM-256M-Q4_K_M.gguf"
    local mmproj="$MODELS_DIR/mmproj-SmolVLM-256M-f16.gguf"

    if [[ -f "$target" && -f "$mmproj" ]]; then
        log "SmolVLM-256M already present at $target"
        echo "$target"
        echo "$mmproj"
        return 0
    fi

    log "Downloading SmolVLM-256M-Q4_K_M..."
    python3 - <<PYEOF
from huggingface_hub import hf_hub_download
import os
repo = "pierretokns/SmolVLM-256M-Instruct-GGUF"
for fname, dest in [(
    "SmolVLM-256M-Instruct-Q4_K_M.gguf",
    "$target",
), (
    "mmproj-SmolVLM-256M-Instruct-f16.gguf",
    "$mmproj",
)]:
    if os.path.exists(dest):
        print(f"skip {fname}")
        continue
    p = hf_hub_download(repo_id=repo, filename=fname, local_dir="$MODELS_DIR")
    if p != dest:
        os.symlink(p, dest)
PYEOF
    log "SmolVLM-256M ready: $target"
    echo "$target"
    echo "$mmproj"
}

# ---- Main ----
case "${1:-auto}" in
    lfm2.5-vl-450m)
        download_lfm25
        ;;
    smolvlm-256m)
        download_smolvlm
        ;;
    *)
        # Auto: try LFM2.5 first, fall back to SmolVLM
        if ! download_lfm25; then
            log "Falling back to SmolVLM-256M"
            download_smolvlm
        fi
        ;;
esac

#!/bin/bash
# Download whisper.cpp GGML model
set -e

MODEL=${1:-base}
DEST=${2:-.}

case "$MODEL" in
  tiny)
    URL="https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.bin"
    ;;
  base)
    URL="https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.bin"
    ;;
  small)
    URL="https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin"
    ;;
  medium)
    URL="https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-medium.bin"
    ;;
  *)
    echo "Unknown model: $MODEL"
    echo "Available: tiny, base, small, medium"
    exit 1
    ;;
esac

echo "Downloading ggml-$MODEL.bin..."
mkdir -p "$DEST"
curl -L -o "$DEST/ggml-$MODEL.bin" "$URL"
echo "Done: $DEST/ggml-$MODEL.bin"

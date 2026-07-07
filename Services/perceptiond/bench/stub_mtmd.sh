#!/usr/bin/env bash
# stub_mtmd.sh — deterministic stub for the llama-mtmd-cli binary used in
# bench_mtmd.py. Emits a single chat completion that the v7.0.1
# _extract_description logic can parse, plus the same llama_print_timings
# tail a real run would produce. Determinism is the point: runs should be
# comparable across hardware and across time.
#
# Used by:
#   python3 bench/bench_mtmd.py --self-test ...
#
# Reads the prompt from the -p argument so the stub can branch between
# LFM2.5 (chat template) and SmolVLM ("A short caption:") wrappers and
# emit a parseable answer for either path.
set -euo pipefail

PROMPT=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    -p) PROMPT="${2:-}"; shift 2 ;;
    -m|--mmproj|--image|-ngl|-c|-b|-ub|-t|-fa|--no-warmup) shift 2 ;;
    *) shift ;;
  esac
done

# Match the v7.0.1 is_lfm2_5 detection: "LFM2.5" in model_path. The bench
# passes /fake/model.gguf in stub mode so we fall through to the
# non-LFM path and emit a "A short caption:" style reply, which is what
# the production extractor already handles.
if [[ "$PROMPT" == *"<|im_start|>"* ]]; then
  # LFM2.5 path: emit an assistant turn exactly as the real binary would.
  echo "<|im_start|>user"
  echo "$PROMPT"
  echo "<|im_end|>"
  echo "<|im_start|>assistant"
  echo "STUB-DESCRIPTION: synthetic test image, frame seed visible."
  echo "<|im_end|>"
else
  # SmolVLM-style path: short caption prompt, plain completion.
  echo "A short caption:STUB-DESCRIPTION synthetic test image"
fi

# Tail that the extractor strips as llama stats / startup noise.
echo "llama_model_loader: stub model loaded"
echo "sampling: deterministic"
echo "generate: n_tokens = 5 / n_seconds = 0"
echo "exiting"

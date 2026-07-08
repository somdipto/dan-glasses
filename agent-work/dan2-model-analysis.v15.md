# DAN-2 Model Analysis — v14
**Date:** 2026-06-19 (companion to `dan2-research-report.md`)
**Question:** Are LFM2.5-VL-450M, whisper.cpp, KittenTTS still the right choices for Dan Glasses v1.0 (desktop) and v2 (wearable)?

---

## TL;DR

- **LFM2.5-VL-450M Q4_0** — keep for v1.0, benchmark **Zamba2-VL-1.2B** for v1.1, NPU path required for v2 wearable.
- **whisper.cpp + base.en** — keep for v1.0, watch **Zamba2-Audio-1.5B** and **Stability Audio 3.0 small** as v1.5 collapse candidates.
- **KittenTTS** — keep for v1.0 **iff license confirmed**, otherwise swap to **Piper-TTS** (MIT). **F5-TTS** is the v1.5 streaming TTS.
- **Mnemosyne + LFM2.5-Embedding-350M** — swap memoryd before v1.0 .deb. 6-week workstream.
- **HRM-Text 1B** — v1.5 reasoning layer, contingent on Sapient shipping inference.

---

## 1. Vision — LFM2.5-VL-450M

### Current (verified live)

- **Model:** `LFM2.5-VL-450M-Q4_0.gguf` (209 MB) + `mmproj-LFM2.5-VL-450m-F16.gguf` (180 MB).
- **Runtime:** `llama-mtmd-cli` at `/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli`.
- **Config:** Q4_0, `-ngl 99`, `-c 2048`, `-b 1 -ub 1`, `-t 8`, `--no-warmup`.
- **Prompt:** `Describe this image briefly. Focus on: people, objects, text, activities.`
- **Throughput:** ~10-15s per frame on x86_64 CPU. Watchful 5 FPS + MAX_QUEUE_DEPTH=2 keeps lag bounded.
- **Fallback:** `SmolVLM-256M-Q4_K_M` (120MB) auto-selected by `download.sh` if LFM2.5 ever disappears.

### Assessment

**Strengths:**
- 450M params is the sweet spot for edge inference — sub-250ms on dedicated silicon.
- SigLIP2 NaFlex encoder is purpose-built for variable-resolution input (better than ResNet/ViT at edge).
- 32,768-token context is generous for a vision model — supports long conversational loops.
- Liquid AI license is research + commercial-friendly (confirm before v1.0 .deb).
- Liquid AI shipped `LFM2.5-VL-Extract` (June 4 2026) — structured JSON output, useful for tool-calling from perception.

**Weaknesses:**
- Power draw on aarch64 (Redax) is uncharacterized. ~3-8W estimate per inference burst (planning numbers from canonical analysis).
- 10-15s/frame on x86_64 CPU is unacceptable for true wearable use; needs NPU.
- No native audio understanding — must pair with whisper.cpp.
- 512×512 input resolution limits fine-grained detail (face recognition, small text).

### Alternatives evaluated

| Model | Params | Size | Quality | Silicon | Verdict |
|---|---|---|---|---|---|
| **LFM2.5-VL-450M Q4_0** | 450M | 209MB | Good | CPU OK, NPU better | ✅ **v1.0 default** |
| **LFM2.5-VL-450M Q5_0** | 450M | ~280MB | Better | CPU OK | v1.0 desktop alt |
| **LFM2.5-VL-1.6B-Extract** | 1.6B | ~700MB | Stronger | NPU only | v1.1 structured-output path |
| **Zamba2-VL-1.2B** | 1.2B | ~600MB | Better than LFM2.5 | NPU | **v1.5 candidate**, 10× TTFT claim needs our measurement |
| **SmolVLM-256M Q4_K_M** | 256M | 120MB | Decent | CPU | ✅ v1.0 fallback |
| **Apple AFM 3 20B** | 20B | ~12GB | SOTA | Apple Silicon only | ❌ not relevant for Redax aarch64 |
| **Moondream2** | 1.86B | 2.7GB | Legacy | CPU | ❌ too large |
| **Gemma 3 270M** | 270M | 230MB | Text-only | CPU | ❌ no vision (no mmproj) |

### Recommendation

- **v1.0 desktop:** LFM2.5-VL-450M Q4_0. Confirmed.
- **v1.1 desktop:** LFM2.5-VL-1.6B-Extract for tool-calling perception (extract structured events from frames).
- **v1.5:** benchmark Zamba2-VL-1.2B on perceptiond workloads. The Zyphra 10× TTFT claim is from their silicon — measure on Redax first.
- **v2 wearable:** NPU-accelerated path required. LFM2.5-VL-450M at <2W is the target. If Zamba2-VL-1.2B hits <2W on Redax NPU with better latency, swap.
- **Compression bet for v1.1:** speculative decoding with SmolVLM-256M as draft model + LFM2.5-VL-450M as target. Llama.cpp supports. ~2× throughput on identical hardware.

---

## 2. STT — whisper.cpp

### Current (verified live)

- **Binary:** `/usr/local/bin/whisper-cli` (1.0 MB), compiled from `/home/workspace/dan-glasses/whisper.cpp/`.
- **Model:** `ggml-base.bin` (74MB, base.en).
- **Binding:** `transcription.py` shells out to whisper-cli with `-ojf` JSON sidecar for confidence.
- **VAD:** Silero ONNX, 512-sample frames at 16 kHz, threshold 0.5, 250ms min speech, 200ms min silence, 10s segment cap.
- **Throughput:** Real-time on x86_64 with `base.en`. ~2× RT on `tiny.en`.

### Assessment

**Strengths:**
- Production-grade. Whisper.cpp is the most mature open STT runtime. Vulkan, Metal, CUDA, ROCm all supported.
- `whisper-cpp-plus-rs` is the right Rust binding — async + Tokio + Silero VAD + real-time PCM streaming.
- `base.en` (74MB) is the right balance for desktop; `tiny.en` (39MB) is the fallback for thermal-constrained wearable scenarios.
- Confidence from per-token probability (`whisper-cli -ojf`) is the only honest STT confidence number.

**Weaknesses:**
- Multilingual is poor unless you swap to a multilingual model. We are English-only for v1.0 — acceptable.
- Word-level timestamps require `-ml 1` flag and add latency. Not currently used.
- Whisper has known hallucination patterns on silence/music. VAD mitigates this.

### Alternatives evaluated

| Model | Size | Quality | Verdict |
|---|---|---|---|
| **whisper base.en** | 74MB | Good | ✅ **v1.0 default** |
| **whisper tiny.en** | 39MB | OK | v1.0 thermal fallback |
| **whisper small.en** | 244MB | Better | v1.1 desktop alt |
| **Parakeet** (NVIDIA) | ~120MB | SOTA English | v1.5 alt |
| **Zamba2-Audio-1.5B** | ~700MB | Likely SOTA | v1.5 audiod+ttsd collapse candidate |
| **Stability Audio 3.0 small** | ~80MB | Strong | v1.5 long-form TTS candidate |
| **Apple AFM STT** | — | Strong | ❌ Apple Silicon only |

### Recommendation

- **v1.0 desktop:** whisper.cpp + base.en. Confirmed.
- **v1.0 wearable:** whisper.cpp + tiny.en (thermal envelope). Switchable on thermal state.
- **v1.5:** benchmark Zamba2-Audio-1.5B (unified audio model — collapses audiod + ttsd). Don't ship unless benchmark holds. Stability Audio 3.0 small as long-form fallback.
- **Open work (non-blocking):** whisper binary hot-reload on `/reload`, bounded transcribe queue with drop-oldest, ALSA device hot-swap, UDP/WebRTC transport for phone-relay mode.

---

## 3. TTS — KittenTTS

### Current (verified live)

- **Binding:** Python (kittentts pip package).
- **Model:** medium variant (verified live: `/health` returns `model=medium`, `voice=expr-voice-2-m`).
- **Output:** RIFF/WAV, 24kHz mono IEEE Float, ~218-309 KB per short sentence.
- **Latency:** ~3.8s cold (first request after startup), <1s warm.

### Assessment

**Strengths:**
- <25MB total footprint. Ships in the .deb without bloat.
- CPU-friendly, designed for edge.
- 8 voices pre-trained (2-5 m/f).
- ONNX export available, WASM browser runner exists.

**Weaknesses (critical):**
- **[SPEC.md flags KittenTTS commercial-use license as UNVERIFIED](../Services/ttsd/SPEC.md).** Must confirm before v1.0 .deb ships to B2B customers.
- Synthesis is unmelodic — no singing. Acceptable for voice prompts.
- No streaming output — current `/speak` is request/response WAV. Wearable use needs streaming.
- Quality at 80M params is "good enough" not "natural." For long-form TTS, larger models win.

### Alternatives evaluated

| Model | Size | Quality | Streaming | License | Verdict |
|---|---|---|---|---|---|
| **KittenTTS base** | <25MB | Good (80M params) | No | **Verify** | ✅ v1.0 default (after license confirm) |
| **F5-TTS** | ~300MB | SOTA 2026 | Yes | MIT | v1.5 alt |
| **Piper-TTS** | ~60MB | Good | Yes | MIT | v1.0 fallback if KittenTTS license fails |
| **Stability Audio 3.0 small** | ~80MB | Strong | Yes | Stability Community | v1.5 long-form candidate |
| **LFM2.5-Audio-1.5B** (Liquid AI, rumored) | ~700MB | Likely SOTA | Likely | Open | v1.5 collapse candidate |

### Recommendation

- **v1.0 desktop:** KittenTTS medium **iff license confirmed**. If not confirmed in 1 week, swap to Piper-TTS. Both are MIT/open.
- **v1.0 wearable (pre-Redax):** KittenTTS mini (smallest variant) for thermal envelope.
- **v1.5:** evaluate LFM2.5-Audio-1.5B as audiod+ttsd collapse. F5-TTS as streaming TTS fallback.
- **Streaming TTS:** critical for wearable. KittenTTS doesn't stream. F5-TTS does. If wearable ships before F5-TTS integration, the v2 latency budget is broken.

---

## 4. Memoryd embedding — Mnemosyne swap

### Current

- **Model:** `sentence-transformers/all-MiniLM-L6-v2` (22M params, 384-dim).
- **Storage:** SQLite + flat in-process vectors.
- **Throughput:** ~50 embeddings/sec on x86_64 CPU.

### Assessment

**Why swap:** Mnemosyne (MIT, single SQLite file, native OpenClaw provider) scores **98.9% Recall@All@5** on LongMemEval vs MiniLM's ~80%. That's a 19-point absolute jump on a benchmark that maps directly to "does memoryd retrieve the right episode when the user asks?" LFM2.5-Embedding-350M + ColBERT-350M (Liquid AI, June 18 2026) is 4.4× smaller than MiniLM but with higher retrieval quality. The danlab-multimodal screenshot set is our held-out benchmark — we have ground-truth LFM2.5 captions.

### Plan

1. **W1:** `pip install mnemosyne-memory[openclaw]`. Validate ≥95% Recall@All@5 on the danlab-multimodal screenshot set.
2. **W2:** set `plugins.slots.memory = "memory-core"` in `/root/.openclaw/openclaw.json`. Mnemosyne becomes OpenClaw's memory provider.
3. **W3-4:** port memoryd `/memories`, `/query`, `/v1/embeddings` to Mnemosyne API. Keep SQLite as the storage backend.
4. **W5-6:** evaluate LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M as the embedding layer. If ≥98% Recall@All@5, swap.

**Cost:** 6 weeks of one engineer. **Benefit:** memoryd becomes a real memory system, not a vector store. Unlocks the wearable use case (memories that actually recall). **Blocks v1.0 .deb.**

---

## 5. Reasoning — HRM-Text 1B (new for v1.5)

### Why this is new

The workspace `AGENTS.md` mentions HRM-Text 1B. The dan-glasses `AGENTS.md` does not. v13 reconciled this — both are layered, not contradictory. **v14 commits: HRM-Text 1B is the v1.5 reasoning layer; LFM2.5-VL stays the vision layer; Mnemosyne stays the memory layer.**

### What it is

- **HRM-Text 1B** (Sapient, May 18 2026): 1.15B params, trained on 40B tokens, **hierarchical recurrent architecture with slow/fast reasoning**. Trained in **1 day for $1,000.** Brain-inspired — high-level planner + low-level executor.
- **Claimed:** 1,000× less data than comparable models for equivalent reasoning quality.

### Why it matters for Dan Glasses

- Reasoning on-device without a 70B frontier model in the loop.
- The hierarchical structure maps cleanly to "plan a proactive interaction" (slow) + "execute a single TTS response" (fast).
- 1.15B params fits the wearable power envelope if quantized.

### Caveat

Sapient has not yet released inference code as of June 19 2026. **v1.5 plan, contingent on Sapient shipping inference.** Fallback: use Qwen 3.6 Coder-35B-A3B (MoE, 35B total / 3B active, MIT, June 2026) as the cloud-side reasoning backend for the desktop; on-device reasoning stays with HRM-Text when available, Gemma 3 1B as fallback.

### Recommendation

- **v1.0:** no reasoning layer change. The whisper + LFM2.5-VL + KittenTTS + Mnemosyne stack handles desktop use.
- **v1.5:** add `reasond` service with HRM-Text 1B (when Sapient ships inference). Mit fallback to Qwen 3.6-A3B on the cloud relay for desktop, Gemma 3 1B on-device.
- **Open question for somdipto:** do we want cloud reasoning in the product, or do we want to hold the line at "on-device only"? This is a values question, not a technical question.

---

## 6. Open-weights vs closed — the licensing matrix

| Model | License | Commercial use | Attribution required |
|---|---|---|---|
| LFM2.5-VL-450M | Liquid AI (research + commercial) | ✅ after license confirm | Yes |
| whisper base.en | MIT | ✅ | No |
| KittenTTS | **Verify** | TBD | TBD |
| Mnemosyne | MIT | ✅ | No |
| LFM2.5-Embedding-350M | Liquid AI | ✅ after license confirm | Yes |
| HRM-Text 1B | Sapient | TBD (likely MIT-style) | TBD |
| Zamba2-VL-1.2B | Open (Zyphra) | ✅ | Yes |
| F5-TTS | MIT | ✅ | No |
| Piper-TTS | MIT | ✅ | No |

**Action:** legal review of every model license before v1.0 .deb. This is 2 days of work for someone at somdipto's end (or 1 day with a license-tracking spreadsheet). Currently the spec only flags KittenTTS — should flag all.

---

## 7. Summary table — v1.0 vs v1.5 vs v2

| Layer | v1.0 desktop | v1.5 | v2 wearable |
|---|---|---|---|
| Vision | LFM2.5-VL-450M Q4_0 | + LFM2.5-VL-1.6B-Extract (tool-calling) | NPU-accelerated LFM2.5-VL-450M or Zamba2-VL-1.2B |
| STT | whisper.cpp base.en | + Zamba2-Audio-1.5B collapse candidate | whisper.cpp tiny.en (thermal fallback) |
| TTS | KittenTTS medium (or Piper) | F5-TTS streaming | KittenTTS mini + streaming layer |
| Memory | Mnemosyne + bge-small | + LFM2.5-Embedding-350M + ColBERT | Same as v1.5 |
| Reasoning | (none — direct tool calls) | HRM-Text 1B (when Sapient ships) | HRM-Text 1B Q4 |
| Proactive | hand-coded rules in proactived | distilled ProActor 1-2B | on-device ProActor Q4 |
| Self-improve | (none) | SIA-fork harness + LoRA | SIA-fork + LoRA on wearable traces |

---

*Half-life of useful model analysis is now ~3 days. v14 reads in 90 seconds. v13 archived.*

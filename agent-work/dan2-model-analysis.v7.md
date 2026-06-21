# Dan2 — Model Selection Deep-Dive v7
## Are LFM2.5-VL-450M, whisper.cpp, KittenTTS still the right choices? (2026-06-17)

**Date:** 2026-06-17
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v7. v6 archived as `dan2-model-analysis.v6.md`.

**Read `dan2-research-report.md` first for context. This file is a focused model-selection critique with concrete alternatives.**

---

## 1. Executive Summary

| Model | v6 verdict | v7 verdict | Why it changed |
|---|---|---|---|
| Vision: LFM2.5-VL-450M | ✅ right for v1 | ✅ right for v1, watch LFM3 | Liquid AI may release LFM3 in 2026 |
| STT: whisper.cpp base.en | ✅ right for v1 | ✅ right for v1, benchmark Moonshine/Parakeet | New on-device STT models with better WER/speed |
| TTS: KittenTTS medium | ✅ right for v1 | ✅ right for v1, benchmark Piper | Piper has a larger voice community |
| **Reasoning: HRM-Text 1B (NEW)** | (not in v6) | ✅ **v7 recommendation** | 1.15B params, brain-inspired, $1K pretrain cost |
| Text gen (optional): Gemma 4 1B | (not in v6) | ✅ **v7 recommendation** | Strong open-weight 1B with instruction-following |

**No v6 picks are wrong. v7 adds two new layers (reasoning + text gen) and one new candidate for each modality to benchmark on Redax when hardware lands.**

---

## 2. Vision Models — Detailed Comparison

### 2.1 LFM2.5-VL-450M (current pick)

| Field | Value |
|---|---|
| Vendor | Liquid AI |
| Released | 2026-04-11 |
| Params | 450M |
| Vision encoder | SigLIP2 NaFlex (not ResNet/ViT) |
| Text decoder | LFM2.5-base (hybrid shortconv+attention) |
| Image input | 512×512 |
| Context | 32,768 tokens |
| Inference claim | sub-250ms (hybrid CPU/GPU) |
| On-disk size (Q4_0) | 209 MB (verified live in perceptiond) |
| GGUF | yes (verified) |
| ONNX | yes (fp32, fp16, q4, q8) |
| License | research / commercial (verify with Liquid) |
| HuggingFace | `LiquidAI/LFM2.5-VL-450M` |
| Live in Dan Glasses | ✅ running, ~10-15s/frame on x86_64 CPU |

**v7 verdict: still the right call.** No sub-500MB VLM released in 2026-Q2 has surpassed it on quality/size/latency.

### 2.2 Alternatives to benchmark

| Model | Params | Pros | Cons | Status |
|---|---|---|---|---|
| **SmolVLM-256M** | 256M | Smaller (120MB), good fallback | Lower quality | ✅ Already fallback in `download.sh` |
| **Gemma 3 270M** | 270M | Text-only — | No vision support, no mmproj | ❌ not applicable |
| **Moondream 2** | 1.86B (Q4: 1GB) | Mature, widely used | Too big for glasses | ❌ legacy, used in danlab-multimodal only |
| **PaliGemma 2** | 3B | Google quality | Too big | ❌ |
| **LFM3-VL** (rumored) | TBD | Liquid's next-gen | Not released | 🔍 watch 2026-Q3 |
| **Gemma 4 VL** (rumored) | TBD | Google VL | Not released | 🔍 watch 2026-Q3 |
| **InternVL 2.5 (1B)** | 1B | Strong quality | Bigger than 450M; borderline | ⚠️ evaluate if power allows |

**v7 recommendation:** stay with LFM2.5-VL-450M for v1. When Redax lands, benchmark vs SmolVLM-256M (lower power) and a 1B-tier (higher quality, more power). Pick based on measured battery life, not synthetic benchmark.

### 2.3 Quantization choices

| Quant | Size | Quality | Speed (CPU) | Recommendation |
|---|---|---|---|---|
| fp16 | 800MB+ | best | slow | desktop only |
| Q8_0 | 400MB | near-fp16 | medium | desktop prototype |
| Q5_0 | 280MB | good | medium | laptop, AC |
| **Q4_0** | **209MB** | **good** | **fast** | **glasses default** |
| Q4_K_M | similar | similar | similar | alternative Q4 variant |
| Q3_K | 180MB | okay | fast | emergency only |
| Q2_K | 150MB | degraded | fastest | not recommended |

**v7 recommendation:** Q4_0 for glasses (current). Q5_0 for laptop prototype. Re-benchmark when on Redax.

---

## 3. STT Models — Detailed Comparison

### 3.1 whisper.cpp (current pick)

| Field | Value |
|---|---|
| Vendor | OpenAI (whisper.cpp: community) |
| Released | whisper: 2022-09; whisper.cpp: 2023 |
| Models | tiny (39M), base (74M), small (244M), medium (769M), large-v3 (1.5B) |
| Bindings | `whisper-rs` (classic), `whisper-cpp-plus-rs` (async + VAD), `transcribe-rs` (multi-engine) |
| VAD | built-in + Silero (in plus-rs) |
| GPU | Vulkan, Metal, CUDA, ROCm |
| License | MIT |
| Live in Dan Glasses | ✅ running, base.en, 66+ tests passing |

**WER benchmarks (2026, novascribe):** Large-v3: 2.7% on LibriSpeech test-clean. Base.en: ~5-7% on clean English. [^5]

### 3.2 Alternatives to benchmark

| Model | Params | Pros | Cons | Status |
|---|---|---|---|---|
| **Moonshine** (Useful Sensors) | ~27M-61M | Very small, fast on CPU | Newer, smaller community | 🔍 benchmark |
| **Parakeet** (NVIDIA) | ~120M-880M | Fast on GPU, strong quality | NVIDIA-tuned | 🔍 benchmark |
| **Whisper large-v3-turbo** | 809M | Faster than large-v3, similar quality | Bigger than base | 🔍 optional |
| **Canary** (NVIDIA) | 1B | Multilingual, strong | Big | ❌ too big |
| **Distil-Whisper** | ~166M-756M | Distilled, faster | Quality slightly lower | 🔍 benchmark |
| **Sensory** (TFLite Micro) | varies | Ultra-low power, embedded | Less accurate | ⚠️ for ultra-low-power only |

**v7 recommendation:** stay with whisper.cpp `base.en` (74MB) for v1. Benchmark Moonshine, Parakeet, and Distil-Whisper when Redax lands. The "right" pick depends on measured WER *on Redax mic input* (not LibriSpeech clean).

### 3.3 Model size choice

**v6 said `base.en` (74MB). v7 confirms:** this is the right size for push-to-talk, clean mic input. If we add wake-word or noisy-environment support, bump to `small.en` (244MB) — but battery impact is significant.

**Wake word for v1.5:** consider `openWakeWord` (open-source, ~5MB) or `Porcupine` (commercial). Both are <1ms CPU inference, <5MB RAM. Not in v1, but the spec should mention.

---

## 4. TTS Models — Detailed Comparison

### 4.1 KittenTTS (current pick)

| Field | Value |
|---|---|
| Vendor | KittenML |
| Released | 2026 |
| Params | ~80M (medium) |
| Variants | default, base, mini, medium, large |
| On-disk | <25MB total (mini: smaller) |
| Inference | ONNX, CPU-friendly, WASM available |
| License | (verify with KittenML) |
| Live in Dan Glasses | ✅ running, medium, 6/6 tests passing |

**v7 caveat:** the voice quality of KittenTTS medium is acceptable but not great for extended speech. Good for short Dan Glasses utterances ("the user is at the coffee shop"). For long-form (10+ second responses) the prosody flattens.

### 4.2 Alternatives to benchmark

| Model | Size | Pros | Cons | Status |
|---|---|---|---|---|
| **Piper** (Rhasspy) | 15-65MB per voice | Large voice community (50+ languages), better prosody | Slightly bigger | 🔍 benchmark |
| **Kokoro** (Hexgrad) | 82M params | High quality, MIT | CPU inference slower | 🔍 benchmark |
| **Parler TTS** (HF) | ~880M | High quality | Too big for edge | ❌ |
| **Bark** (Suno) | ~500M | Voice cloning, expressive | Big, slow | ❌ |
| **Coqui TTS** (community) | varies | Many voices | Project in maintenance | ⚠️ check status |
| **Edge TTS** (Microsoft) | cloud-only | Excellent quality | Cloud dependency | ❌ not edge |
| **OpenAI TTS** | cloud-only | Best quality | Cloud + cost | ❌ not edge |

**v7 recommendation:** stay with KittenTTS medium for v1. **Benchmark Piper on Redax** — Piper has a much larger community and a known-good path. v2 may switch.

### 4.3 Streaming TTS

For <500ms response latency, the TTS must start speaking before the full text is generated. This means the LLM must stream tokens to the TTS, and the TTS must accept partial input.

**v7 finding:** KittenTTS does not currently support streaming. Piper does. **If we want sub-500ms response latency, Piper is the right pick.** v1 ships with KittenTTS (accept the higher latency for v1). v2 should switch.

---

## 5. Reasoning Model — HRM-Text 1B (NEW in v7)

### 5.1 Why this is the most important v7 addition

Audiod returns transcripts. Perceptiond returns descriptions. Memoryd stores them. **But nothing reasons over them to decide what matters, what to surface, what to forget.** This is the largest product gap in Dan Glasses.

A reasoning layer is the difference between "AI recorder" and "AI companion."

### 5.2 HRM-Text 1B (Sapient, 2026-05-18) [^1]

| Field | Value |
|---|---|
| Vendor | Sapient Intelligence (Singapore) |
| Released | 2026-05-18 |
| Params | 1.15B |
| Architecture | Hierarchical recurrent (brain-inspired, dual-timescale) |
| Pretrain tokens | 40B (1,000× less than typical) |
| Pretrain cost | ~$1,000 in 1 day |
| Post-training | **None** (pre-trained base only) |
| Context | reasonable (TBD — Sapient hasn't published) |
| License | open-source (verify with Sapient) |
| Live in Dan Glasses | ❌ not yet |

**Why it's the right pick for our reasoning slot:**
- **Size:** 1.15B is the smallest reasoning model that "actually works" (per Sapient's published comparisons with much larger models).
- **Cost:** $1K pretrain cost means *we can fine-tune our own version* for the "what should I do?" task without breaking the bank.
- **Architecture:** brain-inspired hierarchical recurrent (slow/fast reasoning) maps well to "observation → reflection → action" loop.
- **Open:** no safety tax; we control the model fully.

**Why it's NOT the right pick for chat:** it has no instruction tuning. If we want Dan Glasses to chat ("hey Dan, what's the weather?"), we need Gemma 4 1B (post-trained) for that. **Use HRM-Text for reasoning, Gemma 4 1B for chat.**

### 5.3 v7 fine-tuning plan

| Step | Effort | Cost |
|---|---|---|
| Download HRM-Text 1B base | 1 hour | $0 |
| Hand-curate 200-500 examples of "given observations, here's a useful suggestion" | 1 week | 1 person-week |
| Fine-tune with Unsloth or QLoRA on a single H100/A100 | 1 week | ~$50 cloud GPU |
| Quantize to Q4 for aarch64 | 1 day | $0 |
| Integrate as `reasond` service | 2-3 weeks | 1 person-week |
| **Total** | **6-8 weeks** | **~$50 + 2 person-weeks** |

**v7 risk:** Sapient has not published inference code or fine-tuning code. We may need to write both. Plan B: fork Sapient's repo, write the missing pieces. Plan C: use the model via llama.cpp (it should "just work" since the architecture is a transformer variant).

---

## 6. Text Generation — Gemma 4 1B (NEW in v7, optional)

For chat-mode (TTS prep, conversational replies), HRM-Text is the wrong tool — it's a pre-trained base with no instruction following. We need a small instruction-tuned LLM.

**v7 recommendation:** **Gemma 4 1B (Google, 2026)** as the chat model.

| Field | Value |
|---|---|
| Vendor | Google |
| Released | 2026-Q1 |
| Params | 1B (also 4B, 31B tiers) |
| Post-training | RLHF + instruction tuning |
| License | Gemma license (open) |
| Distilled from | Gemma 4 27B (per industry report) |
| On-disk (Q4) | ~800MB |
| Live in Dan Glasses | ❌ not yet |

**Why not Llama 4 1B?** Llama 4 has gappy licensing and a smaller open community. Gemma 4 has better license clarity and stronger benchmarks at 1B.

**Why not Qwen 3 1.5B?** Qwen 3 is excellent but Chinese-trained; biases in safety filtering. For a wearable on a US user's face, Gemma is safer default.

**v7 recommendation:** Gemma 4 1B for chat. **Only run when needed** (e.g., for TTS prep). Don't keep loaded in memory when idle.

---

## 7. Auxiliary Models (less critical)

### 7.1 VAD (voice activity detection)

**Current:** Silero VAD (ONNX, 16kHz, 512-sample windows, ~0.3W when running).

**v7 verdict:** Silero is the right pick. No alternative comes close on the size/quality tradeoff.

### 7.2 Embedding model (for memoryd)

**Current:** all-MiniLM-L6-v2 (384-dim, 22M params, ~80MB).

**v7 alternatives:**
- BGE-small-en-v1.5 (384-dim, 33M params, ~120MB) — slightly better retrieval
- E5-small-v2 (384-dim, 33M params) — competitive
- Nomic Embed Text v1.5 (768-dim, ~140MB) — bigger, more accurate

**v7 recommendation:** stay with all-MiniLM-L6-v2 for v1 (it works, 16/16 tests passing). Benchmark BGE-small when memoryd is on Redax (the dim is the same, so the migration is cheap).

### 7.3 Wake word (for v1.5)

**Candidates:** openWakeWord (open, ~5MB, <1ms CPU), Porcupine (commercial, $0.10/unit/yr), Picovoice Cheetah (commercial).

**v7 recommendation:** openWakeWord for v1.5 (no per-unit fees). Train on a custom "Hey Dan" wake word.

---

## 8. Model Stack — Final v7 Recommendation

| Layer | Model | Size on disk | Why |
|---|---|---|---|
| Vision (in perceptiond) | LFM2.5-VL-450M Q4_0 | 209MB | Best sub-500MB VLM in 2026 |
| STT (in audiod) | whisper.cpp base.en | 74MB | Best on-device STT at size class |
| TTS (in ttsd) | KittenTTS medium | 25MB | Best tiny TTS |
| VAD (in audiod) | Silero VAD v4 | 2MB | Default, works |
| Embedding (in memoryd) | all-MiniLM-L6-v2 | 80MB | Default, works |
| **Reasoning (in reasond, NEW)** | **HRM-Text 1B Q4** | **~600MB** | **Brain-inspired, fits aarch64** |
| Text gen (in reasond, optional) | Gemma 4 1B Q4 | ~800MB | For chat-mode and TTS prep |
| **Total stack on disk** | | **~2.0GB** | Fits 8GB LPDDR5 aarch64 with headroom |

**v7 risk:** the total 2.0GB stack is borderline for a 4GB RAM target (8GB is required to keep the OS + browser + agent runtime happy). The Redax board needs ≥8GB LPDDR5. If the board has 4GB, we need to reduce: drop Gemma 4 1B (use HRM-Text 1B + a hand-tuned prompt for chat), or drop HRM-Text 1B (use Gemma 4 1B for both reasoning and chat — lower quality reasoning).

---

## 9. v7 Decision Matrix — What to Do This Week

| Action | Why | When |
|---|---|---|
| Read Sapient HRM-Text 1B blog post in full | Understand the model before committing | Day 1 |
| Add `model-layers` section to `dan-glasses/AGENTS.md` and `PRD.md` | Fix the two-brain contradiction | Day 1-2 |
| Pin HRM-Text 1B in `models/download.sh` (don't auto-download yet) | Make it explicit in the model registry | Day 2 |
| Write `reasond` service skeleton (no model loaded yet) | Establish the IPC contract | Week 1 |
| Benchmark Moonshine, Parakeet vs whisper.cpp base.en on a laptop | Confirm v1 STT choice | Week 2 (when time) |
| Benchmark Piper vs KittenTTS medium on a laptop | Confirm v1 TTS choice | Week 2 (when time) |
| Read Sapient's HRM-Text 1B inference code (if released) | Plan integration | Week 2-3 |
| Hand-collect 50 example observations → useful suggestions | Begin fine-tuning data | Week 2-4 |
| Integrate HRM-Text 1B into `reasond` (when inference code is ready) | Core v7 deliverable | Month 2-3 |

---

## References (v7)

[^1]: Sapient Intelligence, "Introducing HRM-Text" (2026-05-18). https://sapient.inc/introducing-hrm-text
[^5]: novascribe.ai, "How Accurate Is Whisper in 2026?" (2026). https://novascribe.ai/how-accurate-is-whisper
[^4]: Liquid AI, "LFM2.5-VL-450M" (2026-04-11). https://huggingface.co/LiquidAI/LFM2.5-VL-450M

---

*End of v7 model analysis. Companion artifacts: `dan2-research-report.md`, `dan2-architecture-review.md`, `dan2-agi-roadmap.md`, `dan2-papers-to-read.md`.*

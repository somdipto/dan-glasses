# Model Selection Deep-Dive v13 — Dan Glasses
**Author:** Dan2 (lead scientist / architect)
**Date:** 2026-06-19 09:30 IST
**Supersedes:** dan2-model-analysis.v12 (24 hours old)

---

## 0. TL;DR (v13 deltas from v12)

| Layer | v12 choice | v13 choice | Delta |
|---|---|---|---|
| Vision (desktop) | LFM2.5-VL-450M Q5_K_M | LFM2.5-VL-450M Q5_K_M | unchanged |
| Vision (wearable v1.5) | LFM2.5-VL-450M Q4_0 | LFM2.5-VL-450M Q4_0 | unchanged |
| Vision (wearable v2) | LFM2.5-VL-450M IQ3_XXS | LFM2.5-VL-450M IQ3_XXS (text decoder on CPU) + NPU for vision encoder | **v2: hybrid CPU+NPU per Box v3.1.0 datapoint** |
| STT (desktop) | whisper.cpp base.en | whisper.cpp base.en | unchanged |
| STT (wearable) | whisper.cpp tiny.en | whisper.cpp tiny.en | unchanged |
| TTS (desktop) | KittenTTS medium | KittenTTS medium | **NEW SPIKE: LFM2.5-Audio-1.5B as audiod+ttsd collapse candidate** |
| TTS (wearable) | KittenTTS base | KittenTTS base | unchanged |
| Reasoning (desktop) | cloud (OpenClaw) | cloud (OpenClaw) | **NEW: GLM-5.2 as SIA Feedback-Agent (1M context, MIT, open)** |
| Reasoning (wearable) | HRM-Text-1B (deferred) | HRM-Text-1B (deferred) | **NEW: LFM2.5-Thinking for v1.5 (already shipping)** |
| Embeddings | all-MiniLM-L6-v2 | **LFM2.5-Embedding-350M (June 18 2026)** | v12: MiniLM. v13: benchmark LFM2.5-Embedding-350M. |
| Rerank | none | **LFM2.5-ColBERT-350M (June 18 2026)** | NEW. Late-interaction reranker. |

**Single most important v13 change:** the **LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M** pair (June 18 2026) replaces the v12 "MiniLM-L6-v2, benchmark BGE-small in v1.5" plan. They are purpose-built for retrieval and 4.4× smaller than MiniLM.

## 1. Vision — LFM2.5-VL-450M is still top-of-class for edge

### 1.1 What it is, where it sits

Unchanged from v12. Liquid AI, April 11 2026. 450M text + 86M vision = 536M params. Q4_0 GGUF = 209 MB; mmproj f16 = 180 MB. Combined: ~390 MB on disk. 32K context. SigLIP2 NaFlex encoder.

### 1.2 The v13 Box NPU datapoint (new)

**Box v3.1.0** (jegly/Box, June 2026) is the first on-device AI suite where **NPU acceleration actually works on Snapdragon and MediaTek** for the Gemma 3 1B model. Previous builds shipped the NPU models but crashed on load. Box slides the context window so the chat keeps going.

**Implication for the wearable v2 form factor.** The LFM2.5-VL-450M vision encoder (the ~86M-param part) is small enough to run on a 2026 mobile NPU. The text decoder (~360M) is the part that needs CPU or a beefier NPU. **Hybrid CPU+NPU is the v2 path:**

| Component | Today (v1.5) | v2 (12-month) |
|---|---|---|
| Vision encoder (86M) | CPU | NPU (12 TOPS class, Box-style) |
| Text decoder (360M) | CPU | CPU |
| HRM-Text-1B (1.15B) | N/A | CPU (or NPU if vendor supports) |
| Whisper-tiny (39M) | CPU | Low-power DSP or NPU |
| TTS base (15M) | CPU | CPU with NPU assist |

**v13 measurement target (W1).** Add NPU-vs-CPU comparison for the vision encoder specifically. The vision encoder is the smallest part of the model and the most amenable to NPU acceleration.

### 1.3 Quantization ladder (unchanged from v12)

| Quant | Combined size | Quality (vs f16) | Notes |
|---|---|---|---|
| Q8_0 | ~510 MB | ~99% | laptop only |
| **Q5_K_M** | ~360 MB | ~98% | laptop default |
| **Q4_K_M** | ~290 MB | ~96% | laptop fallback |
| **Q4_0** (current) | ~390 MB | ~96% | v1.5 wearable default |
| IQ3_XXS | ~210 MB | ~94% | v2 wearable (with NPU assist on vision encoder) |
| **IQ2_XXS** | ~165 MB | ~92% | stretch target |

### 1.4 Hardware acceleration matrix (v13, updated)

| Platform | Viable for LFM2.5-VL-450M Q4_0? | v13 status |
|---|---|---|
| x86_64 CPU (laptop) | ✅ Yes | 10-15 s/frame observed |
| aarch64 Cortex-A76 (Pi 5) | ⚠️ Yes, ~2-3× slower | Measure in W1 |
| aarch64 Cortex-A55 (Orange Pi 5) | ⚠️ Yes, ~3-4× slower | Backup target |
| Mali-G78 / Adreno 7xx | ⚠️ Modest wins on vision encoder | Worth benchmarking |
| **Mobile NPU (Snapdragon 8 Gen 3+, MediaTek Dimensity 9200+)** | ✅ Vision encoder only | **NEW v13 datapoint: Box v3.1.0 works on these for Gemma 3 1B.** |
| Hexagon, Apple ANE, GAP9 | ❌ Not yet for full model | Re-evaluate for v2.5 |

## 2. STT — whisper.cpp (base.en / tiny.en) is still right

Unchanged from v12.

**v13 contender (LFM2.5-Audio-1.5B):** see §3.3. Audio-1.5B handles STT *and* TTS. If the quality is good, this collapses the audio stack.

## 3. TTS — KittenTTS still right, but LFM2.5-Audio-1.5B is a real challenger

### 3.1 Current choice (KittenTTS medium, 25MB)

Unchanged from v12. Eight voices, 24 kHz mono, ONNX.

### 3.2 Wearable target (KittenTTS base, 15MB)

Unchanged from v12.

### 3.3 NEW v13: LFM2.5-Audio-1.5B as audiod + ttsd collapse candidate

**Liquid AI's cookbook** (https://github.com/Liquid4All/cookbook) shows LFM2.5-Audio-1.5B running as a single on-device model for **voice assistant** (STT + TTS) on:
- Apple Silicon Macs (LEAP SDK)
- Web browsers (WebAssembly)
- iOS and Android (LEAP Edge SDK)

**Why this matters for Dan Glasses.** A single 1.5B model replacing whisper.cpp + KittenTTS collapses 2 services into 1. The wearable RSS budget drops by 50-100 MB. The audio pipeline latency drops because there is no separate STT → intent → TTS round-trip.

**Risk.** LFM2.5-Audio-1.5B at Q4 quantization is ~800 MB. On a wearable with 1 GB usable RAM, this is too big. The wearable is still KittenTTS base + whisper-tiny.

**v13 workstream (W14 spike).** Benchmark LFM2.5-Audio-1.5B on the laptop prototype:
1. STT quality vs whisper.cpp base.en on the danlab-multimodal audio test set.
2. TTS quality vs KittenTTS medium on a 30-utterance human eval.
3. End-to-end latency (mic-in → speaker-out) vs the current stack.
4. Power draw on x86_64 CPU and aarch64 CPU.

If LFM2.5-Audio-1.5B wins on 3 of 4, promote to v1.5 desktop default. The wearable stays on the current stack.

### 3.4 NEW v13: Inflect-Nano (4.63M params)

A r/LocalLLaMA release (June 2026) of a 4.63M-param TTS. Way too robotic for a companion. Skip.

## 4. Reasoning — GLM-5.2 for cloud, HRM-Text-1B + LFM2.5-Thinking for wearable

### 4.1 The v13 correction: GLM-5.2 as the SIA Feedback-Agent

**v12 said:** "Claude-class or GPT-class" Feedback-Agent for the SIA loop on danlab-multimodal.

**v13 correction:** **GLM-5.2 (Z.ai, June 14 2026).** Why:
- **Open, MIT-licensed.** No API lock-in. No per-token cost. $2/hr on a single H100.
- **1M-token context.** SIA's Feedback-Agent needs to read the full trajectory. IndexShare reduces 1M-context per-token FLOPs by 2.9×.
- **Ranks #2 on PostTrainBench** (only behind Opus 4.8; beats Opus 4.7 and GPT-5.5). The benchmark that measures "how well does this agent improve small models through post-training" is exactly SIA's use case.

This is a v12 correction. The 2025 cost structure (Claude-class or GPT-class) is replaced by the 2026 open-weights reality.

### 4.2 HRM-Text-1B on the wearable

Unchanged from v12. 1.15B params, 40B tokens training, $1K pretrain, fits 2 GB RAM at Q4. The credible on-device "thinker" bet.

### 4.3 NEW v13: LFM2.5-Thinking on-device

Liquid AI's howaiworks.ai blog confirms LFM2.5-Thinking is shipping as the on-device reasoning variant. **W14 benchmark:** compare LFM2.5-Thinking vs HRM-Text-1B on the memory consolidation test set.

## 5. Embeddings + Rerank — the v13 unlock

### 5.1 Current: all-MiniLM-L6-v2 (384-dim, 80MB)

Unchanged from v12. v1 default.

### 5.2 NEW v13: LFM2.5-Embedding-350M

Released June 18 2026 (Liquid AI). 350M params, purpose-built for retrieval. **Open question:** verify the output dimension. If 384-dim (same as MiniLM), the swap is a drop-in. If 768-dim, the HNSW index needs re-build.

**v13 workstream (W9.2):** benchmark LFM2.5-Embedding-350M vs MiniLM-L6-v2 on the existing memory set. Swap if quality > MiniLM by >2% on held-out retrieval.

### 5.3 NEW v13: LFM2.5-ColBERT-350M

Released June 18 2026 (Liquid AI). 350M params, late-interaction reranker. Sits on top of the HNSW index: retrieve top-50 by vector, rerank with ColBERT. This is the Hindsight-style four-retrieval fan-in minus graph + temporal.

**v13 workstream (W9.3):** add LFM2.5-ColBERT-350M as the late-interaction reranker on top of the existing HNSW index.

### 5.4 The v13 retrieval stack

```
HNSW (top-50) + BM25 (top-20) + temporal (last 7 days)
   ↓
LFM2.5-ColBERT-350M (rerank top-50 → top-10)
   ↓
SIA Feedback-Agent (GLM-5.2) for memory consolidation
```

This is the Hindsight pattern, minus the proprietary parts. Achievable in 6 weeks (W9).

## 6. What the model stack looks like at each form factor (v13)

| Form factor | Vision | STT | TTS | Reasoning | Embedding | Rerank | Total resident |
|---|---|---|---|---|---|---|---|
| **Desktop (laptop, x86_64)** | LFM2.5-VL-450M Q5_K_M (330 MB) | whisper.cpp base.en (74 MB) | KittenTTS medium (25 MB) | cloud (OpenClaw) | LFM2.5-Embedding-350M (~150 MB) | LFM2.5-ColBERT-350M (~150 MB) | ~730 MB |
| **Wearable v1.5 (aarch64, 4 h target)** | LFM2.5-VL-450M Q4_0 (209 MB) + mmproj Q8 (90 MB) | whisper.cpp tiny.en (39 MB) | KittenTTS base (15 MB) | cloud fallback | MiniLM (80 MB) | none | ~435 MB |
| **Wearable v2.0 (hybrid CPU+NPU, 6-8 h target)** | LFM2.5-VL-450M IQ3_XXS (~150 MB) + mmproj Q8 (90 MB) — vision encoder on NPU | whisper.cpp tiny.en (39 MB) — DSP | KittenTTS base (15 MB) — NPU assist | **HRM-Text-1B Q4 (~700 MB)** on-device | LFM2.5-Embedding-350M (150 MB) | LFM2.5-ColBERT-350M (150 MB) | ~1.3 GB |
| **Wearable v2.0 (no HRM-Text, lighter, 8 h target)** | LFM2.5-VL-450M IQ3_XXS + mmproj | whisper.cpp tiny.en | KittenTTS base | LFM2.5-Thinking (350M, ~150 MB) on-device | MiniLM | none | ~635 MB |

The new v2.0 row (lighter, no HRM-Text) is the **wearable v2 sweet spot** if Redax ships with 1 GB RAM. The full v2.0 row requires 2 GB LPDDR4. **This is the v12 hard question, now answered two ways.**

## 7. What I am NOT recommending (unchanged from v12)

1. Training a custom VLM from scratch.
2. A custom STT model.
3. A custom TTS voice.
4. A 7B+ on-device LLM (unless Redax ships with 4+ GB RAM, which is not in any 2026 wearable roadmap).

## 8. Open questions for Somdipto

1. **Mnemosyne + LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M swap.** OK to benchmark + swap in W9? (Lowers memory RSS, raises retrieval quality.)
2. **GLM-5.2 as SIA Feedback-Agent.** OK to use an open, MIT-licensed model on H100 ($2/hr) instead of a Claude/GPT API? (Cheaper, 1M context, open.)
3. **LFM2.5-Audio-1.5B collapse spike.** OK to benchmark audiod + ttsd collapse in W14? (2-week spike, may unlock v1.5 desktop simplification.)
4. **Wearable v2 silicon plan.** Confirm hybrid CPU+NPU is the right v2 bet, not CPU-only? (Box v3.1.0 NPU works for sub-2B models.)
5. **HRM-Text-1B vs LFM2.5-Thinking.** OK to benchmark both on the memory consolidation test set? (1-week spike.)
6. **Storage tier.** Lock 64GB primary? (Apple memory chip pricing pressure + BOM cost.)
7. **Liquid AI license.** Verify the LFM2.5 family is commercially shippable in a .deb? (Critical for all v13 choices.)

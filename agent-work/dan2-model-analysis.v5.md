# Dan Glasses Model Selection — Deep Dive (v5)

**Author:** Dan-2
**Date:** 2026-07-01
**Scope:** LFM2.5-VL-450M, whisper.cpp, KittenTTS, memoryd embeddings — are these still right? What alternatives exist?
**Status:** v5 (2026-07-02) — surgical refresh on top of v4:
  - **HRM-Text-1B (Sapient Intelligence, Singapore, Apache-2.0) confirmed real and shipping.** **Trained from scratch for ~$1,500**, 1.15B params, 1B active. Hierarchical recurrent architecture: two small transformer modules (a slow "H" and a fast "L") *loop over the same embeddings* — reasoning depth at fixed, tiny parameter count. **130-600x less compute, 150-900x less data than comparable models.** Fully-open base checkpoint (not a chatbot). Paper: arXiv 2605.20613. HuggingFace: `sapientinc/HRM-Text-1B`. Real benchmark: **2.4 GB VRAM, ~4 tok/s on RTX 4060.** 1.15B is below our 1.2B-1.5B "reasoning complement" target and is **the natural choice for danlab-multimodal's SIA Feedback-Agent role** (replaces the README's "LFM2.5-1.2B-Thinking" reference). **v5 recommendation: HRM-Text-1B as the new default for the SIA-W+H Feedback-Agent.**
  - **VibeThinker-3B (June 2026) is the new small-beats-large benchmark.** **94.3 on AIME26 (97.1 with test-time scaling), 80.2 on LiveCodeBench v6** — matches Qwen3.6 Plus, Gemini 3 Pro, GLM-5. *The small-beats-large thesis is now empirically validated for reasoning, not just chat.* **For Dan Glasses' compliance-mode reasoning and code-review workloads, a 3B VibeThinker-class model with test-time scaling is sufficient for the device.**
  - **Muse Spark (Meta Superintelligence Labs, April 2026) is Meta's first Muse-series model.** Replaces Llama 4 on all Ray-Ban/Oakley smart glasses (rolled out May 2026). **Not on Ray-Ban Display yet — Llama 4 still there.** Muse Spark is closed, cloud-dependent, paywalled. **Pin it as the explicit counter-positioning reference.**
  - **PTRM (Probabilistic Tiny Recursive Model, 5M params) claims frontier-level on some tasks.** Watch, but treat with caution — small models that "match frontier" usually match on narrow tasks. Not a v1.5 ship candidate; worth tracking for the 24-month horizon.
  - **Gemma 3 ran in orbit on Yam-9 satellite (Loft Orbital, NASA JPL, April 2026).** First VLM deployed in space, doing natural-language data triage. Validates the edge-VLM deployment thesis at the most extreme possible edge. **LFM2.5-VL-450M absolutely runs on a wearable.**
  - **No model changes for v1.** v4's LFM2.5-VL-450M / whisper.cpp / KittenTTS choices stand. v5's additions are **HRM-Text-1B as the SIA Feedback-Agent target** and **VibeThinker-class 3B models as the 24-month on-device reasoning target.**

**v3 (2026-07-01):**
  - **NEW: Meta paywall validates on-device TTS/STT** — if vendor cloud features can be retroactively paywalled, the audio pipeline that runs in audiod/ttsd (no cloud) is the un-paywallable part of the stack. Strengthens the "ship local" thesis.
  - **NEW: Compliance-mode implications for VLM** — the camera-based cheating cases in Taiwan/Korea mean a future VLM might need a "raw image sanitization" pass that strips text/QR/barcode content before it reaches the LLM. This is a v1.5 architecture concern, not a model choice concern, but it affects which VLM we ship (must be local, must be auditable, must support hookable preprocessing).
  - **NEW candidate: Speech-02 (ByteDance, open-weight TTS)** added to the alternatives table — emerging open-weight competitor to KittenTTS/Kokoro with strong multilingual coverage.
  - **Refreshed: Phi-4-Multimodal status** — Microsoft released a quantized-edge variant in late June 2026, making the v2 unification path more credible for wearable.

---

## TL;DR

**v1 (current): LFM2.5-VL-450M ✅, whisper.cpp + base.en ✅, KittenTTS ✅, all-MiniLM-L6-v2 ✅**
**v1.5 candidates: SPEED-Q 4-bit, Phi-4-Multimodal (text+vision+audio unified), Kokoro-82M q4, Speech-02 (multilingual TTS)**
**v2 candidates: MiniCPM-V 2.5 (8B), Moshi-style native multimodal, fine-tuned LFM2.5-1.6B with anti-prompt-injection hardening**

The current stack is **correct and well-grounded**. The 2026 alternatives are all aimed at v1.5 or v2, not v1. LFM2.5-VL-450M is the best sub-500MB VLM on the market, whisper.cpp + base.en is the production-grade STT choice, and KittenTTS is the smallest deployable TTS. The improvements for v1.5 are evolutionary, not revolutionary.

The **one concern** is that LFM2.5-VL-450M is a **relatively new release (April 2026)** with limited independent benchmarking outside Liquid AI's own numbers. The team should validate it against the team's actual use cases (description of indoor/outdoor scenes, OCR, face detection, gesture interpretation) before locking v1.1+. The SmolVLM-256M fallback in perceptiond is correct.

**The new v3 framing:** the model choices are not just technical — they're strategic. The Meta paywall validates the on-device thesis at the product level. The compliance-mode requirement (driven by the Asia cheating scandal) reinforces it at the regulatory level. Every model on the stack must be:
1. **Open-weight** (auditable, no kill-switch from upstream)
2. **Local-runnable** (no cloud dependency)
3. **Hookable** (compliance-mode preprocessing can intercept the input/output)
4. **Small** (fits the wearable power budget)

LFM2.5-VL-450M, whisper.cpp, KittenTTS, and all-MiniLM-L6-v2 all pass this filter. Phi-4-Multimodal passes (open-weight via Microsoft), but is too big for v1 wearable. MiniCPM-V 2.5 passes, also too big for v1. **The current stack is the right stack for v1.**

---

## 1. Vision: LFM2.5-VL-450M

### Current spec
- **Model:** LFM2.5-VL-450M (Liquid AI, April 2026)
- **Quantization:** Q4_0, full GPU offload
- **Size:** ~209MB main + 180MB mmproj F16 = ~389MB total
- **Inference target:** sub-250ms on Intel CPU
- **Fallback:** SmolVLM-256M-Q4_K_M (perceptiond auto-switches)

### Why it's right
1. **Best small VLM in 2026.** Beats SmolVLM2-500M on most Liquid benchmarks. Sub-250ms on Intel CPU. Bounding-box prediction, multilingual, function calling — all v1.5-relevant.
2. **SigLIP2 NaFlex vision encoder** is purpose-built for on-device (vs. older ViT/CLIP encoders). Dynamic-resolution support.
3. **28T tokens pre-training** (up from 10T for LFM2-VL-450M) — a 2.8× pretraining increase.
4. **Open-weight, no kill-switch.** Liquid's release is a published weight + inference code with no remote attestation or vendor cloud requirement. **This is the strategic property that matters most post-Meta-paywall.**
5. **Verified live** in the perceptiond daemon. event_id 280+ in Dan-3's notes. ~10-15s/frame on x86_64 CPU, target sub-250ms is reachable with proper NPU/GPU.
6. **Already shipped by the team.** The work is done.

### Honest concerns
1. **Liquid-published benchmarks only.** Limited independent verification. Validate against actual use cases before locking v1.1+.
2. **Power draw uncharacterized.** No published power numbers. Must be measured on Redax.
3. **GPU offload verified on x86_64, not on aarch64.** -ngl 99 on Redax needs validation.
4. **mmproj is F16 (180MB) — half the total model footprint.** This is bigger than the main LFM. If size is the constraint, try an INT8 mmproj quantization (would cut to ~90MB).
5. **500M is at the edge of "can reason about a scene" vs. "can describe a scene."** For complex visual reasoning, a 1.6B+ model is better. Trade-off: battery life vs. capability.
6. **NEW v3 — Compliance-mode hook required.** The VLM must support a preprocessing hook that can strip OCR text (for exam mode), detect faces (for meeting/hospital mode), or block specific visual categories. LFM2.5-VL-450M doesn't have this built in; the hook would be in perceptiond (pre-VLM) or in os-toold (post-VLM). Plan accordingly.

### Alternatives evaluated

| Model | Size | Strengths | Weaknesses | Verdict |
|---|---|---|---|---|
| **LFM2.5-VL-450M (current)** | 389MB | SOTA small VLM, multilingual, bbox, sub-250ms, open-weight, hookable | Liquid benchmarks only, unverified power | **KEEP for v1** |
| **LFM2.5-VL-1.6B** | ~1.2GB | More capable, 28T tokens | 2-3× slower, 2-3× power, 3-4× size | **v2 if Redax has 8GB+ RAM** |
| **SmolVLM-256M (fallback)** | 302MB | Already wired, lightweight | Worse quality, no bbox | **KEEP as fallback** |
| **SmolVLM-500M** | ~500MB | Better than 256M, similar footprint | Slower than LFM2.5 | **Reconsider as fallback** |
| **Phi-4-Multimodal (5.6B)** | ~2.4GB Q4 | Speech + vision + text unified, 128K context, quantized-edge variant Jun 2026 | 6× bigger, slower | **v2 (one model instead of 3)** |
| **Phi-4-reasoning-vision-15B** | ~8GB Q4 | Reasoning + GUI grounding | Too big for v1, v2 | **v3+** |
| **MiniCPM-V 2.5 (8B)** | ~4GB Q4 | Beats GPT-4V on 11 benchmarks | Too big for v1 | **v2 (phone-tethered)** |
| **jina-vlm (2.4B)** | ~1GB Q4 | Multilingual champion, 4× token reduction | 2.5× bigger than LFM2.5 | **v2 (multilingual priority)** |
| **NanoVDR (70M)** | 274MB | Sub-500MB retriever | Retrieval only, not general VLM | **Niche (memoryd caption retrieval)** |
| **TinyVLM** | <1MB | Ultra-light, 26 FPS on STM32H7 | Detection only, not general VLM | **Research, not v1** |
| **PITR-Select (SmolVLM 0.5B + token reduction)** | 500MB | 6× speedup on video | 8-10% accuracy drop | **v1.5 (video understanding)** |
| **NEW v3: Qwen2.5-VL-3B (Alibaba)** | ~1.8GB Q4 | Strong multilingual, function calling, open-weight | 2× bigger than LFM2.5, slower | **v2 candidate (Asia/multilingual priority)** |

### Recommendation
- **v1:** LFM2.5-VL-450M Q4_0 + F16 mmproj. Lock and ship.
- **v1.5 (Q4 2026):** Benchmark SPEED-Q 4-bit on LFM2.5-VL-450M. If quality holds, switch (saves ~50-100MB).
- **v1.5 (Q4 2026):** Try INT8 mmproj quantization. If quality holds, saves ~90MB.
- **v1.5 (Q4 2026):** Add PITR-Select-style visual token reduction for video understanding (relevant for any future continuous-stream mode).
- **v1.5 (NEW v3):** Add the compliance-mode preprocessing hook in perceptiond. Strip OCR text for exam mode, detect face count for meeting mode, detect medical signage for hospital mode. LFM2.5-VL-450M supports this via system-prompt injection; the hook is in perceptiond, not the model.
- **v2 (Q2 2027):** Evaluate Phi-4-Multimodal as a v1 → v2 unification. Replaces LFM2.5 + whisper.cpp with a single 5.6B model. Trade: 6× bigger, 6× slower, but one model to manage. Microsoft's June 2026 quantized-edge variant is closer to wearable.
- **v2 (Q2 2027):** If multilingual is critical, evaluate jina-vlm. Otherwise stay with LFM2.5.
- **v2 (NEW v3, multilingual):** If Hindi/Tamil/Bengali is critical for India market, evaluate Qwen2.5-VL-3B. Better multilingual than LFM2.5 at the cost of size.

---

## 2. STT: whisper.cpp + base.en

### Current spec
- **Engine:** whisper.cpp via `whisper-cpp-plus-rs` (async, VAD, real-time streaming)
- **Model:** base.en (74MB)
- **VAD:** Silero ONNX
- **Use mode:** PTT (push-to-talk) in v1; wake-word in v1.5

### Why it's right
1. **Production-grade.** whisper.cpp is the most-deployed open STT engine. Mature Rust bindings, GPU acceleration (Vulkan, Metal, CUDA, ROCm), Silero VAD integration.
2. **base.en is the right size for glasses.** tiny.en (39MB) is too lossy for natural conversation. small.en (244MB) is overkill for PTT.
3. **VAD-gated, so always-on mic is cheap.** 0.3W in watchful mode per the canonical analysis.
4. **Open-weight, fully local.** whisper.cpp runs entirely on-device. **No cloud dependency, no retro-paywall risk.** This is the strategic property post-Meta-paywall.
5. **Verified live** in the audiod daemon. 150/150 tests passing per dan2's notes. v1.1 liveness/readiness split is the K8s-grade contract.

### Honest concerns
1. **English-only.** `base.en` is the English-only checkpoint. For multilingual v1.5, need `base` (multilingual, ~74MB, slightly worse English) or `small` (244MB multilingual).
2. **No wake-word.** v1 is PTT-only, which limits hands-free UX. Wake-word is a v1.5 target per the spec.
3. **Whisper confidence is from a JSON sidecar.** If the sidecar is missing (older whisper.cpp, stripped flag), confidence drops to 0.0. audiod handles this fallback correctly but it's worth noting.
4. **CPU-only on x86_64 currently.** No NPU offload. On Snapdragon 8 Elite, Hexagon NPU could give 5-10× power efficiency.

### Alternatives evaluated

| Model | Size | Strengths | Weaknesses | Verdict |
|---|---|---|---|---|
| **whisper.cpp base.en (current)** | 74MB | Production, open-weight, multilingual, GPU, VAD, no cloud | English-only | **KEEP for v1** |
| **whisper.cpp tiny.en** | 39MB | Smallest | Worse accuracy | **Only for thermal-constrained** |
| **whisper.cpp small.en** | 244MB | Better accuracy | 3× size | **Not needed for v1** |
| **Parakeet (NVIDIA)** | varies | Better accuracy/size than Whisper | Less mature ecosystem | **Evaluate in Q4 2026** |
| **Moonshine** | ~50MB | Faster than Whisper tiny, similar accuracy | Newer, less battle-tested | **Evaluate in Q4 2026** |
| **Phi-4-Multimodal ASR** | (unified) | Native ASR in Phi-4-Multimodal | Requires switching to Phi-4-Multimodal | **v2 (if unified model adopted)** |
| **openWakeWord** | ~3MB | Wake-word front-end | Adds another model | **v1.5 (replaces PTT)** |
| **Speech recognition via VLM** | 0MB (uses LFM2.5) | No separate STT model | Way too slow, way too inaccurate | **NO** |

### Recommendation
- **v1:** whisper.cpp + base.en. Lock and ship.
- **v1.5 (Q4 2026):** Add openWakeWord (~3MB) as a wake-word front-end to replace PTT. Layer: openWakeWord → VAD → whisper.cpp. Wake-word detects "Hey Dan", VAD keeps the recording tight, whisper transcribes.
- **v1.5 (Q4 2026):** Evaluate Parakeet or Moonshine as a faster alternative. A/B test on a real conversation corpus.
- **v1.5 (NEW v3, multilingual):** Switch to `base` (multilingual) for Hindi, Tamil, Bengali. 74MB, slightly worse English. Critical for India market.
- **v2 (Q2 2027):** If Phi-4-Multimodal is adopted as the unified model, drop whisper.cpp in favor of Phi-4-Multimodal's native ASR.

---

## 3. TTS: KittenTTS

### Current spec
- **Engine:** KittenTTS Python API
- **Model:** medium (~25MB)
- **Voice:** expr-voice-2-m (default)
- **Output:** 24kHz mono WAV

### Why it's right
1. **Smallest deployable neural TTS.** <25MB total. Critical for the .deb package size budget.
2. **8 expression-based voices** (cheerful, serious, sad, whisper, excited, gentle, calm, neutral). Good range for an AI companion.
3. **CPU-friendly.** Designed for edge deployment. WASM and ONNX runtimes available.
4. **Open-weight, fully local, no cloud dependency, no retro-paywall risk.** **Strategic property post-Meta-paywall.**
5. **Verified live** in the ttsd daemon. 6/6 tests passing. Sub-1s warm-path latency per the spec.

### Honest concerns
1. **Kokoro-82M is the SOTA for local TTS quality.** It's 82M params (~330MB q8, ~90MB q4), 54 voices in 9 languages, widely cited as "outperforming much larger models and competing with paid cloud TTS APIs." For v1, KittenTTS's size wins. For v1.5, a Kokoro q4 path is worth A/B testing.
2. **KittenTTS is slower than Piper on CPU** (per the official KittenTTS issue #40 benchmark). Piper's int8 model is 22MB and faster but less natural.
3. **Audio is unmelodic-only — KittenTTS does not sing.** Not relevant for a voice assistant but worth noting.
4. **Single in-process model, single worker.** First request after startup pays load cost. ~3.8s cold path per the spec.
5. **English-only.** For multilingual v1.5, need a TTS with Hindi/Tamil/Bengali support.

### Alternatives evaluated

| Model | Size | Voices | Quality | Speed | Verdict |
|---|---|---|---|---|---|
| **KittenTTS medium (current)** | ~25MB | 8 | Good | Medium | **KEEP for v1 (size matters, English-only OK for v1)** |
| **Kokoro-82M q4** | ~90MB | 54, 9 langs | SOTA local | Fast | **v1.5 candidate (multilingual + quality)** |
| **Kokoro-82M q8** | ~330MB | 54, 9 langs | SOTA+ | Fast | **v2 (AC-powered)** |
| **Piper int8** | ~22MB | 904 (curated 25) | Decent | Fastest on CPU | **v1.5 fallback (faster, less natural)** |
| **Piper fp16** | ~60MB | 904 | Better | Fast | **v1.5 candidate** |
| **MeloTTS** | varies | Many | Good | CPU-optimized | **Evaluate if multilingual v1.5** |
| **Speech-02 (ByteDance, open-weight)** | varies | Many, multilingual incl. Hindi | High | Production | **v1.5 candidate (multilingual priority)** |
| **Fish Audio S2 Pro** | varies | Open-weight | High quality | Production | **v2+** |
| **Chatterbox (Resemble AI)** | varies | Open | High quality | Production | **v2+** |
| **XTTS** | ~1GB | Voice cloning | Very high | Slow | **Not for edge** |

### Recommendation
- **v1:** KittenTTS medium. Lock and ship.
- **v1.5 (Q4 2026):** A/B test KittenTTS vs Kokoro-82M q4 vs Piper int8 vs Speech-02 on a real user study. Default to whichever wins on the (quality + size + speed) Pareto frontier. **Hypothesis:** Kokoro q4 will win on quality at acceptable size, Speech-02 will win on multilingual.
- **v1.5 (NEW v3, multilingual):** If Hindi/Tamil/Bengali is a v1.5 requirement, ship Speech-02 or Kokoro q4. KittenTTS stays as a size-constrained fallback.
- **v2 (Q2 2027):** If Kokoro q4 is adopted, ship with multilingual (Hindi, Tamil, etc.) for India market.

---

## 4. Memory Embeddings: all-MiniLM-L6-v2 (in memoryd)

### Current spec
- **Model:** sentence-transformers/all-MiniLM-L6-v2
- **Dimension:** 384
- **Storage:** BLOB in SQLite
- **Search:** cosine similarity

### Why it's right
1. **384-dim is right for the size budget.** MiniLM is the canonical small embedding model.
2. **OpenAI-compatible endpoint** at `/v1/embeddings` — drop-in for OpenClaw memory-core.
3. **WAL mode on SQLite** — concurrent reads, durable writes.
4. **Open-weight, fully local.** Runs in-process in memoryd. **No cloud dependency, no retro-paywall risk.**
5. **Verified live** in the memoryd daemon. 16/16 tests passing. DB at ~300KB after 4 memories.

### Honest concerns
1. **Flat cosine similarity** — no temporal dimension, no episode boundaries, no typed memory. **This is the biggest gap to v1.5.** See the architecture review §2.3.
2. **384-dim is small.** For richer memory, 768-dim (e.g., all-mpnet-base-v2) is better. Trade: 2× storage and 2× retrieval cost.
3. **Single embedding per memory.** No multi-vector (ColBERT-style) for richer recall. SOTA is multi-vector.
4. **No consolidation.** Memories are added and never re-organized. As the memory grows, retrieval precision will degrade.

### Alternatives evaluated

| Approach | Strengths | Weaknesses | Verdict |
|---|---|---|---|
| **all-MiniLM-L6-v2 (current)** | 384-dim, fast, well-known, open-weight | Flat cosine, no temporal | **KEEP for v1** |
| **all-mpnet-base-v2** | 768-dim, better quality | 2× storage, 2× retrieval | **v1.5 if recall quality becomes bottleneck** |
| **BGE-small / BGE-base** | Better multilingual | Newer, less battle-tested | **v1.5 if multilingual priority** |
| **Matryoshka embeddings** | Tunable 16-256 dim | Requires retraining | **v1.5 (drop-in, train on user data)** |
| **ColBERT v2 (multi-vector)** | Best retrieval quality | 10× storage, 10× retrieval | **v2 (if memory is the bottleneck)** |
| **VikingMem-style multi-vector** | SOTA retrieval | Complex | **v2+** |
| **True Memory (encoding-gate, edge-friendly)** | Verbatim storage, typed layers | Migration cost | **v1.5 (highest priority)** |
| **Engram (bi-temporal)** | Four-channel retrieval | Complex | **v2 candidate** |
| **Memanto (typed semantic)** | SOTA LongMemEval | Moorcheh dependency | **v2+ if scaling** |
| **OpenAI text-embedding-3-small (cloud)** | 1536-dim, top quality | Cloud dependency, **retro-paywall risk** | **NO (violates local-first)** |

### Recommendation
- **v1:** all-MiniLM-L6-v2 in memoryd. Lock and ship.
- **v1.5 (Q1 2027):** Migrate memoryd from flat cosine to True Memory (encoding-gate, typed layers, SQLite-based). Backwards-compatible: keep `/v1/embeddings` endpoint, add `/recall` for typed+bi-temporal retrieval.
- **v1.5 (Q1 2027):** Add Matryoshka embeddings: train nested 16/32/64/128/256 dim embeddings, allow tunable recall precision vs. cost.
- **v1.5 (NEW v3, multilingual):** If Hindi/Tamil/Bengali is a v1.5 requirement, swap to BGE-small or BGE-base. BGE has stronger multilingual coverage.
- **v2 (Q2 2027):** Evaluate Engram (bi-temporal) or Memanto (typed semantic) for long-horizon recall.

---

## 5. Summary: The Model Stack Roadmap

| Component | v1 (Jul 2026) | v1.5 (Jan 2027) | v2 (Jul 2027) |
|---|---|---|---|
| **Vision** | LFM2.5-VL-450M Q4_0 | LFM2.5-VL-450M SPEED-Q 4-bit + INT8 mmproj + compliance-mode hook | LFM2.5-VL-1.6B or Phi-4-Multimodal or Qwen2.5-VL-3B (multilingual) |
| **STT** | whisper.cpp base.en | + openWakeWord, + multilingual `base`, evaluate Parakeet/Moonshine | Phi-4-Multimodal native ASR (if unified) |
| **TTS** | KittenTTS medium | A/B test Kokoro-82M q4, Piper int8, Speech-02 | Kokoro-82M q4 multilingual OR Speech-02 |
| **Memory embeddings** | all-MiniLM-L6-v2 flat cosine | True Memory (encoding-gate) + Matryoshka + BGE-base (multilingual) | Engram or Memanto (if needed) |
| **Self-improvement** | None | SIA-W+H harness (preview) | SIA-W+H in production |

---

## 6. The One Worry

**LFM2.5-VL-450M is new (April 2026).** Liquid's own benchmarks are the main evidence. Limited independent verification. The team should:

1. **Build an eval harness** for VLM quality: description of indoor/outdoor scenes, OCR on real text, face detection accuracy, gesture interpretation. Run it on a 100-image test set.
2. **Compare to SmolVLM-256M** on the same harness. If LFM2.5 is significantly better, keep it. If not, switch to SmolVLM (which is already wired as a fallback).
3. **Validate the quality with somdipto** before locking v1.1. The product cannot ship on Liquid's benchmarks alone.

The SmolVLM fallback in perceptiond is correct. **Don't remove it until LFM2.5 is independently validated on the team's use cases.**

---

## 7. The Strategic Frame (NEW v3)

Every model on the stack must satisfy the four filters:

1. **Open-weight** (auditable, no kill-switch from upstream, no retro-paywall)
2. **Local-runnable** (no cloud dependency, runs in daemon on user's hardware)
3. **Hookable** (compliance-mode preprocessing can intercept input/output)
4. **Small** (fits the wearable power budget for v2, runs in <5W for the model itself)

LFM2.5-VL-450M, whisper.cpp, KittenTTS, and all-MiniLM-L6-v2 all pass.

Phi-4-Multimodal passes (1, 2, 3) but is too big for v1 wearable (fails 4). MiniCPM-V 2.5 same. Speech-02 and Kokoro-82M q4 pass all four. **The current stack is the right stack for v1.**

**The Meta paywall (June 26 2026) is the loudest product-positioning signal of 2026 so far.** The vendor that owns "on-device, open-weight, user-controlled" first wins the next category cycle. Dan Glasses' stack already satisfies this. The marketing job is to make this obvious.

---

*End of model analysis. See dan2-research-report.md, dan2-agi-roadmap.md, dan2-architecture-review.md, dan2-papers-to-read.md.*

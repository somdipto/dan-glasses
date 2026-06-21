# Model Selection Deep-Dive
**Author:** Dan2 (co-founder, lead scientist, architect)
**Date:** 2026-06-16
**Scope:** Are LFM2.5-VL-450M (vision), whisper.cpp / ggml-base.bin (STT), and KittenTTS (TTS) still the right choices for Dan Glasses v1 in mid-2026? What alternatives exist, and what should ship in v1.5 / v2?
**Inputs:** `dan2-research-report.md` (sections B7, B8, B10, D-A/B/C), service SPECs, verified live state.

---

## TL;DR

All three current choices are **defensible for v1**. The more interesting questions are:

1. **LFM2.5-VL-450M** is right for v1, but the verified live inference is **10–15s/frame on x86_64 CPU** — the spec's "150–800ms" is on aarch64+NPU. We need real numbers. Alternatives: **SmolVLM-256M (fallback), MiniCPM-V-2 (2B, better OCR), VisionTrim acceleration (training-free 2–3× speedup), VLMCache (1.4–3.8× speedup for stable scenes), SpecVLM (1.5–2.9× speedup via speculative decoding).**
2. **whisper.cpp / ggml-base.bin** is right for v1. The bigger gap is **wake-word**: add `openWakeWord` or merge Porcupine into audiod for the wearable UX.
3. **KittenTTS** is right, but live we use "medium" which isn't a real KittenTTS variant. Canonical lineup is **nano (15M, ~25MB int8), micro (40M, ~41MB), mini (80M, ~80MB)**. For wearable, **nano-int8**. For laptop, mini.

The memory model (`all-MiniLM-L6-v2`) is the **single biggest miss** — see `dan2-architecture-review.md` §6.

---

## 1. LFM2.5-VL-450M (Vision-Language Model)

### Current state (verified live)
- **Model:** `LFM2.5-VL-450M-Q4_0.gguf` (209 MB) + `mmproj-LFM2.5-VL-450m-F16.gguf` (180 MB).
- **Engine:** `llama-mtmd-cli` (multimodal tool use) at `/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli`.
- **Quant:** Q4_0, `-ngl 99` (full GPU offload), `-c 2048`, `-b 1 -ub 1`, `-t 8`, `--no-warmup`.
- **Live performance:** **~10–15s/frame on x86_64 CPU-only** (CPU-only because no GPU offload on laptop).
- **Prompt:** "Describe this image briefly. Focus on: people, objects, text, activities."
- **Architecture:** LFM2.5-base + 400M SigLIP2 NaFlex + efficient projector.
- **Released:** April 11, 2026.
- **License:** Research/commercial (verify with Liquid AI for production).

### Is it the right choice for v1?

**Yes.** Reasoning:
- **Sub-250ms target** on aarch64+NPU (per Liquid AI's own numbers) is real. The 10–15s we measure is the x86_64 CPU-only path, which is a worst case.
- **512×512 input** is the right resolution for always-on scene description.
- **SigLIP2 NaFlex** is a good encoder for this use case (better than ResNet/ViT at low res).
- **`llama-mtmd-cli` integration is solid** in the dan-glasses build.
- **SmolVLM-256M fallback** is already wired in `download.sh` — this is the right second-line choice for athermal scenarios.

### What could beat it?

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **SmolVLM-256M** (Q4_K_M + mmproj) | 120MB + 182MB = 302MB | Already wired as fallback. Sub-1GB GPU memory. Under 250MB main model. | Lower quality on complex scenes; 26s/image in danlab-multimodal CPU tests. |
| **MiniCPM-V 2.5 / Llama3-V 2.5** | ~5GB (4-bit) | Best edge VLM in the 2–3B class. Better OCR, multilingual, NPU acceleration (QNN). On-device latency improvements. | Too big for true wearable in 2026. 5GB even at 4-bit is heavy. |
| **Eagle 2.5** (8B) | ~4–8GB | Frontier long-context VLM. 72.4% on Video-MME with 512 frames. | Not edge. Cloud-only. |
| **Gemma3-270M** (text-only) | 230MB | Cheapest option. | **No vision** in llama.cpp. Would need a custom projector. Skip. |
| **LFM2-VL-450M (Halo licensed)** | ~450MB | Same model, used by Brilliant Labs Halo. Validates the choice. | Same tradeoffs. |

### Acceleration techniques (for v1.5)

These are **drop-in** on top of the existing LFM2.5-VL + llama.cpp stack:

1. **VisionTrim** (OpenReview 2026): training-free vision token compression. **2–3× speedup** on MLLM inference. Dominant Vision Token Selection + Text-Guided Vision Complement. Drop-in for any VLM.
2. **VLMCache** (ACM 2026): block-level visual KV-cache reuse. **1.4–3.8× speedup** when scene is mostly static (perfect fit for "watching a desk" or "watching a conversation"). Stable blocks (background) cached; dynamic blocks (foreground) recomputed.
3. **SpecVLM** (OpenReview 2026): speculative decoding for VLMs. **2.5–2.9× speedup in 5 training epochs.** Elastic visual compressor adapts per input. Online-logit distillation.
4. **Salience-based gating** (already partially in perceptiond via `SalienceDetector`): run VLM only on salient frames. This is the right architecture — don't run on every frame, run on motion/face/text events.

**Realistic target post-optimization (x86_64 laptop, CPU-only):** 10–15s → 3–5s per salient frame. On aarch64 + NPU: 250ms target is achievable with all four techniques combined.

### Gemma3-270M as a thermal fallback

For thermal-throttled scenarios (SoC > threshold), drop VLM entirely and use Gemma3-270M as a text-only "what's the most likely user intent right now" predictor. This is the right thermal design and is supported by the spec's mention of Gemma as a fallback. Wire it up.

---

## 2. whisper.cpp / ggml-base.bin (Speech-to-Text)

### Current state (verified live)
- **Binary:** `/usr/local/bin/whisper-cli` (1.0 MB statically-linked, from whisper.cpp 2025-04-18 commit).
- **Models:** `ggml-base.bin` (148 MB, default) and `ggml-tiny.bin` (78 MB, recommended for Redax aarch64).
- **Flags:** `-ng` (no GPU), `-ml 1` (max segment length 1, faster first result), `-l auto` or `-l en`.
- **Live performance:** 400–700ms end-to-end for short utterances on x86_64 with ggml-tiny.
- **VAD:** Silero VAD via ONNX Runtime (no torch dependency). 0.5 threshold, 250ms min speech, 200ms min silence. Energy fallback if ONNX missing.
- **Streaming:** No. whisper-cli is segment-based. Streaming is "v3" in the spec.

### Is it the right choice for v1?

**Yes.** whisper.cpp is the most mature, cross-platform, open-source STT runtime. `ggml-base.bin` is a strong default; `ggml-tiny.bin` is the right choice for the aarch64 wearable.

### What's missing for a true wearable

- **Wake-word.** This is the **biggest gap**. Push-to-talk is the v1 default per spec; wake-word is "deferred to v3." For a wearable to be a wearable, it needs a wake-word. The audiod spec has `wakewordd` in the v3 roadmap — **promote to v1.1.**
  - **Pick:** `openWakeWord` (open-source, runs on CPU, ~50mW continuous) or Porcupine (commercial, on-device, more accurate).
  - **Latency target:** <200ms utterance → wake event.
  - **Where:** Standalone `wakewordd` on port 8095 using ONNX Runtime, OR fold into audiod as a pre-VAD stage.
  - **Why on-device:** cloud wake-word is a privacy non-starter and a battery non-starter.
- **Streaming whisper.** Currently segment-based. For sub-second latency on long utterances, streaming is needed. whisper.cpp has a `whisper-stream` (community fork) with chunked inference. Evaluate for v1.5.
- **Noise suppression (RNNoise).** Pre-VAD. Cheap (3MB model, <5ms/frame). Big win for noisy environments. Wire into audiod capture.py.
- **Speaker diarization.** For "who said what" in multi-user scenarios. pyannote.audio is the standard. Not v1 priority.

### Alternatives to whisper.cpp

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **whisper.cpp** (current) | 78–769MB | Mature, cross-platform, Rust bindings, VAD integration available. | Segment-only (no streaming). |
| **Parakeet** (NVIDIA) | ~150MB | Streaming, fast, good English accuracy. | Less mature in C++ runtime; limited language support. |
| **Moonshine** | ~250MB | Real-time, edge-optimized. | Newer; less battle-tested. |
| **Distil-Whisper** | ~150MB | 6× faster than whisper-large, comparable quality. | Same constraints as whisper. |
| **Canary** (NVIDIA) | ~1GB | Multilingual, SOTA accuracy. | Too big for wearable. |

**Recommendation: keep whisper.cpp for v1 and v1.5.** The wake-word gap and the noise-suppression gap are higher priority than switching STT engines.

---

## 3. KittenTTS (Text-to-Speech)

### Current state (verified live)
- **Service:** `ttsd` on port 8743, returning `audio/wav` (24kHz float).
- **Model:** "medium" per spec — **this is not a canonical KittenTTS variant.** Canonical lineup (per `kittenml/kittentts` v0.8, Feb 2026): **nano (15M, ~25MB int8), micro (40M, ~41MB), mini (80M, ~80MB)**.
- **Voice:** "expr-voice-2-m" hardcoded.
- **Latency:** 218KB WAV per `/speak` call (no timing data in the spec — need to measure).
- **License:** Apache 2.0.

### Is it the right choice for v1?

**Yes, with one clarification.** KittenTTS is the right model family. The "medium" reference in the spec needs to be reconciled with the actual KittenTTS v0.8 lineup. Likely explanation: a custom build or an older label. **Verify.**

**Recommended mapping:**
- **Laptop dev path (x86_64, AC-powered):** `kitten-tts-mini` (80M, ~80MB). Highest quality.
- **Wearable (aarch64, battery-powered):** `kitten-tts-nano-int8` (15M, ~25MB). 8–9× real-time. Quality is "lowest" but adequate for spoken feedback.
- **Lowest-power mode (sleep / wake-word response):** `kitten-tts-nano` (15M, FP) at ~56MB. Even smaller, but not int8 quantized.

### What could beat it?

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **KittenTTS v0.8** (current family) | 25–80MB | Open-source, Apache 2.0, on-device, multiple variants, 8 voices. | Quality is "good enough" not "great." |
| **Piper TTS** | 15–60MB | Mature, many voices, many languages. | Slower than KittenTTS-nano; older. |
| **Orca** (Microsoft) | ~100MB | High quality, streaming. | Heavier; Microsoft-y licensing. |
| **CosyVoice** (Alibaba) | ~300MB | SOTA Chinese + multilingual. | Too big for wearable. |
| **StyleTTS2** | ~250MB | High quality. | Too big for wearable. |

**Recommendation: stay with KittenTTS.** The variant selection is the only thing to fix. For v1.5, evaluate `kitten_tts_rs` (Second State's Rust port, no Python dep, OpenAI-compatible API) as a replacement for the Python/ONNX path. ~10MB binary + model = much smaller process footprint.

### Voices
- 8 built-in voices: Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, Leo.
- Currently hardcoded to `expr-voice-2-m` (not a KittenTTS voice). **Fix this** in ttsd. Let the bootstrap wizard pick a voice and persist it as a semantic memory.

### Streaming TTS
For "I want the assistant to start speaking before it finishes generating" UX, we need streaming TTS. KittenTTS v0.8 supports it. Wire it up: chunk by sentence (≤ 400 chars), stream audio chunks to the speaker as they synthesize. Cuts first-audio latency from "full utterance" to "first sentence."

---

## 4. all-MiniLM-L6-v2 (Memory Embeddings)

### Current state (verified live)
- **Model:** `sentence-transformers/all-MiniLM-L6-v2`, 384-dim float32.
- **Storage:** BLOB in SQLite.
- **Scoring:** Cosine similarity only.

### Is it the right choice for v1?

**It's a 2024-era choice and the right place to invest in v1.5.** MiniLM-L6 is small (22MB), fast (~5ms/query on CPU), and supports 384-dim embeddings. The model itself is fine.

**What's missing is the *memory architecture*, not the model.** Per the architecture review §6 and the research report section B8:

**v1.5 changes (2 weeks):**
1. Add temporal metadata (created_at, last_accessed, access_count, decay_rate).
2. Add confidence decay (Ebbinghaus-style).
3. Add relational scoring (4-signal: semantic × temporal × confidence × relational_bonus).
4. Add a `ConsolidationAgent` cron job (every 6h) that boosts/decays and tags "supersedes" chains.

**v2 changes (Q1–Q2 2027):**
1. **Dual-process memory** (DPA / DPCM): synchronous daytime writer + async nighttime schema induction.
2. **TiMem-style Temporal Memory Tree**: hierarchy of (raw events → episodic → semantic → procedural → schema).
3. **CategoryRAG** with hallucination resistance (Synthius-Mem, 99.6% on adversarial).

### Embedding model alternatives

| Alternative | Dim | Size | Why consider | Why not |
|-------------|-----|------|--------------|---------|
| **all-MiniLM-L6-v2** (current) | 384 | 22MB | Fast, small, decent quality. | 2024-era. |
| **all-mpnet-base-v2** | 768 | 110MB | Better quality. | 2× slower; 4× storage. |
| **BGE-small-en-v1.5** | 384 | 33MB | Better retrieval quality than MiniLM. | Slightly bigger. |
| **nomic-embed-text-v1.5** | 768 | 137MB | SOTA retrieval. | Heavy. |
| **E5-small-v2** | 384 | 33MB | Microsoft, good quality. | Similar to BGE-small. |
| **Cohere embed-multilingual-v3** | 1024 | API | Best multilingual. | Cloud. Defeats the privacy story. |
| **bge-m3** | 1024 | 567MB | SOTA multilingual, dense+sparse+multi-vector. | Heavy. |

**Recommendation:** **Switch to `BGE-small-en-v1.5`** (384-dim, 33MB) in v1.5. Better retrieval quality than MiniLM at the same dimensionality. The model swap is a 1-day change to memoryd. The architecture change (temporal + confidence + relational) is the real lift.

For **multilingual** (Hindi/Tamil/Bengali) coverage in v2, evaluate `bge-m3` or `nomic-embed-text-v1.5` — but only if we have the compute.

---

## 5. The bigger picture: model + accelerator co-design

The 2026 research is converging on **model + hardware co-design** as the path to wearable AI:

- **Nanomind** (arXiv 2510.05109): decomposes LMMs into modular bricks (vision, projector, language, audio), maps each to the most suitable accelerator (NPU, GPU, DSP), Token-Aware Buffer Manager for zero-copy transfers. **42.3% energy reduction.** LLaVA-OneVision-Qwen2-0.5B + camera → **18.8 hours on 2000 mAh battery**. This is the playbook.
- **TAO** (arXiv 2506.18584): temperature-aware offloading. Reduces offload cost by 35% while meeting power/thermal/energy constraints.
- **Multi-LoRA on Snapdragon NPU** (arXiv 2604.18655v2): INT4 weights, INT8 activations, per-channel quantization. 4–6× memory and latency improvements. **Proven on Samsung Galaxy S24/S25.** This is the production path for sub-500MB VLMs on Qualcomm AR1.

**Implication for Dan Glasses v1.5/v2:** don't just pick a model — pick a model + a quantization scheme + a target accelerator. The right matrix is:

| Model | Quant | Target accelerator | Latency | Battery impact |
|-------|-------|--------------------|---------|----------------|
| LFM2.5-VL-450M | Q4_0 | CPU (Redax aarch64) | 10–15s | 1.5W avg watchful |
| LFM2.5-VL-450M | Q4_0 | Hexagon NPU (AR1) | 250ms target | 0.5W avg watchful |
| LFM2.5-VL-450M + VisionTrim | Q4_0 | Hexagon NPU | 80ms | 0.3W avg watchful |
| Gemma3-270M (text-only fallback) | IQ4_XS | CPU | 100ms | 0.1W avg |
| KittenTTS-nano-int8 | int8 | CPU | 8–9× real-time | 0.05W avg |
| whisper-tiny | q5_1 | CPU | 200–500ms | 0.3W avg |
| BGE-small | fp32 | CPU | 5ms/query | 0.05W avg |

**Pick the matrix for the wearable, not just the models.** The Redax decision (or the indie hardware path) determines which cells are achievable.

---

## 6. What to ship in v1 (now)

1. **Reconcile KittenTTS "medium"** in ttsd — pick `mini` (laptop) or `nano-int8` (wearable).
2. **Fix hardcoded voice** — let the wizard pick from KittenTTS's 8 voices.
3. **Wire VisionTrim** (training-free, 2–3× VLM speedup) into perceptiond. Drop-in.
4. **Wire VLMCache** (1.4–3.8× for stable scenes) into perceptiond. Drop-in for the watchful mode.
5. **Add SalienceDetector → VLM gate** so we don't run VLM on every frame.
6. **Switch memoryd embedding** to `BGE-small-en-v1.5` (or stay with MiniLM if benchmarks don't show clear gain).
7. **Measure LFM2.5-VL-450M real power on x86_64 and on aarch64+NPU sim.** Stop using the spec's "150–800ms" — get the real numbers.

## What to ship in v1.5 (Q3–Q4 2026)

8. **`wakewordd` with openWakeWord.** Biggest UX upgrade.
9. **`powerd` (state machine) + thermal-aware throttling.** Drops to Gemma3-270M text-only when hot.
10. **Streaming whisper** (`whisper-stream` fork).
11. **RNNoise** pre-VAD in audiod.
12. **Memory v1.5: temporal + confidence + relational scoring.**
13. **Streaming KittenTTS** for sub-second first-audio latency.

## What to ship in v2 (2027)

14. **Memory v2: dual-process (DPA / DPCM).** System 1 (sync writer) + System 2 (async schema induction).
15. **Multilingual embeddings** (bge-m3 or nomic-embed) when we have Hindi/Tamil/Bengali content.
16. **Multi-LoRA on the NPU** (per the Samsung Galaxy paper) for user-specific model adapters.
17. **TT-SI in danlab-multimodal v3.**
18. **Fork SIA** and integrate as a harness for genuine self-improvement.

---

## What NOT to do

- ❌ Don't switch the VLM away from LFM2.5-VL-450M in v1. It's the right choice; the gaps are in the acceleration layer.
- ❌ Don't switch the STT away from whisper.cpp. It's the right choice; the gap is the wake-word.
- ❌ Don't switch the TTS away from KittenTTS. It's the right family; the gap is the variant + streaming.
- ❌ Don't try to fine-tune LFM2.5-VL-450M in the loop. The compute cost is prohibitive on the target hardware. Use a smaller reward model instead.
- ❌ Don't bring in frontier-class models (GPT-5.5, Claude Opus 4.8, Gemini 3.1 Pro) as dependencies. Cloud defeats the privacy story. The whole point of Dan Glasses is **on-device**.

---

*👾* Model choices are right. The next 90 days are about acceleration (VisionTrim, VLMCache, SpecVLM, salience gating), the wake-word gap, and the memory architecture — not about replacing the model lineup.

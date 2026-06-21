# Model Selection Deep-Dive
**Author:** Dan2 (co-founder, lead scientist, architect)
**Date:** 2026-06-17
**Scope:** Are LFM2.5-VL-450M (vision), whisper.cpp / ggml-base.bin (STT), KittenTTS (TTS), and the new HRM-Text 1B (reasoning) the right choices for Dan Glasses v1 in mid-2026? What alternatives exist, and what should ship in v1.5 / v2?
**Inputs:** `dan2-research-report.md` (v6, 2026-06-17) — sections B7, B8, B10, D-A/B/C; service SPECs; verified live state from `dan1.md`–`dan4.md`.
**Prior versions:** `dan2-model-analysis.v5.md` (2026-06-16) — kept as backup.

---

## TL;DR

All four model choices are **defensible for v1**. The two most interesting v6 questions are:

1. **LFM2.5-VL-450M (vision) + HRM-Text 1B (reasoning)** — the right two-model split for v1. HRM-Text 1B (released 2026-05-18 by Sapient Intelligence) is the on-device reasoning LLM with continuous latent-space reasoning. No CoT token burn. ~1,000× less training data than typical LLMs.
2. **whisper.cpp / ggml-base.bin (STT) + KittenTTS (TTS)** — right for v1. The bigger gap is **wake-word** (add `openWakeWord`) and **streaming TTS** (KittenTTS v0.8 supports it).

**v6 changes from v5:**
- **HRM-Text 1B added** as the on-device reasoning LLM. This was not in v5; the v5 only mentioned LFM2.5-VL as the primary model. **The root `AGENTS.md` already specified HRM-Text 1B** — v5 missed this and v6 corrects it.
- **New acceleration layer reviewed** — VLCache (1.2–16× speedup, recomputes 2–5% of vision tokens), EdgeFM (1.49× over TensorRT-Edge-LLM on Orin), LQA (4-bit vision + 8-bit text + gradient-free TTA), SPEED-Q (2-bit InternVL3-1B in <400 MB).
- **CoVSpec added** — device–edge co-inference with on-device draft VLM + edge verification. 2.21× throughput, 96% bandwidth reduction. **This is the right architecture for the tethered-glasses path.**
- **Parakeet + Moonshine revisited** for STT, given the multilingual India context.
- **EdgeFM, LiteVLM** noted as the production-ready edge VLM frameworks (vs. just raw llama.cpp).
- **VLMQ** added for token-saliency-driven PTQ — much better low-bit quantization on VLMs.

The model lineup is right; the gaps are in the acceleration layer (vision token compression, KV cache reuse, device–edge co-inference) and the wake-word/streaming-audio path.

---

## 1. LFM2.5-VL-450M (Vision-Language Model)

### Current state (verified live)
- **Model:** `LFM2.5-VL-450M-Q4_0.gguf` (209 MB) + `mmproj-LFM2.5-VL-450m-F16.gguf` (180 MB).
- **Engine:** `llama-mtmd-cli` (multimodal tool use) at `/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli`.
- **Quant:** Q4_0, `-ngl 99` (full GPU offload), `-c 2048`, `-b 1 -ub 1`, `-t 8`, `--no-warmup`.
- **Live performance:** **~10–15 s/frame on x86_64 CPU-only** (CPU-only because no GPU offload on laptop).
- **Prompt:** "Describe this image briefly. Focus on: people, objects, text, activities."
- **Architecture:** LFM2.5-base + 400M SigLIP2 NaFlex + efficient projector.
- **Released:** April 11, 2026.
- **License:** Research/commercial (verify with Liquid AI for production).

### Is it the right choice for v1?

**Yes.** Reasoning:
- **Sub-250 ms target** on aarch64+NPU (per Liquid AI's own numbers) is real. The 10–15 s we measure is the x86_64 CPU-only path, which is a worst case.
- **512×512 input** is the right resolution for always-on scene description.
- **SigLIP2 NaFlex** is a good encoder for this use case (better than ResNet/ViT at low res).
- **`llama-mtmd-cli` integration is solid** in the dan-glasses build.
- **SmolVLM-256M fallback** is already wired in `download.sh` — this is the right second-line choice for athermal scenarios.

### What could beat it?

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **SmolVLM-256M** (Q4_K_M + mmproj) | 120 MB + 182 MB = 302 MB | Already wired as fallback. Sub-1 GB GPU memory. Under 250 MB main model. | Lower quality on complex scenes; 26 s/image in danlab-multimodal CPU tests. |
| **MiniCPM-V 2.5 / Llama3-V 2.5** | ~5 GB (4-bit) | Best edge VLM in the 2–3 B class. Better OCR, multilingual, NPU acceleration (QNN). | Too big for true wearable in 2026. 5 GB even at 4-bit is heavy. |
| **Eagle 2.5** (8B) | ~4–8 GB | Frontier long-context VLM. 72.4% on Video-MME with 512 frames. | Not edge. Cloud-only. |
| **Gemma3-270M** (text-only) | 230 MB | Cheapest option. | **No vision** in llama.cpp. Would need a custom projector. Skip. |
| **LFM2-VL-450M (Halo licensed)** | ~450 MB | Same model, used by Brilliant Labs Halo. Validates the choice. | Same tradeoffs. |
| **Gemma 3 4B / 12B** (used in space!) | 4–8 GB | Google DeepMind's Gemma 3 ran onboard Yam-9 satellite via JPL/Loft Orbital (2026-04) — first VLM in orbit. Validates "small VLM on edge." | Too big for wearable; intended for satellite-scale edge. |

### v6 update — Gemma 3 in space (JPL/Loft Orbital, April 2026)

Google DeepMind's Gemma 3 ran onboard a satellite for the first time in April 2026, identifying areas of interest in response to natural-language queries. Loft Orbital's Yam-9 + JPL's software package.[^gemma_space] This validates the "small VLM on edge" thesis for resource-constrained devices, but for **space-grade** compute, not wearables. Worth noting because:
- It establishes that VLMs in the 4–8 GB range can run on edge hardware.
- The pattern (query-based VLM inference, not always-on) is what the wearable should evolve to.
- For wearable, LFM2.5-VL-450M is still the right size class.

### Acceleration techniques (for v1.5)

These are **drop-in** on top of the existing LFM2.5-VL + llama.cpp stack. **v6 brings new options to the table:**

1. **VLMCache** (ACM 2026): block-level visual KV-cache reuse. **1.4–3.8× speedup** when scene is mostly static. Stable blocks (background) cached; dynamic blocks (foreground) recomputed. **Perfect for "watching a desk" or "watching a conversation."**
2. **VisionTrim** (OpenReview 2026): training-free vision token compression. **2–3× speedup**. Dominant Vision Token Selection (DVTS) + Text-Guided Vision Complement (TGVC). Drop-in for any VLM.
3. **SpecVLM** (OpenReview 2026): speculative decoding for VLMs. **2.5–2.9× speedup** within 5 training epochs. Elastic visual compressor adapts per input. Online-logit distillation.
4. **VLCache** (arXiv:2512.12977): per-image hash-based KV-cache reuse. **1.2–16× speedup** depending on architecture. **Recomputes only 2–5% of vision tokens** at each layer. This is the most aggressive cache-reuse number I've seen.
5. **VLMQ** (arXiv:2508.03351): token-saliency-driven post-training quantization. Up to **16.45% accuracy improvement on MME-RealWorld at 2-bit**. Drop-in for low-bit quantization.
6. **LQA** (arXiv:2602.07849): Selective Hybrid Quantization (4-bit vision + 8-bit text) + gradient-free TTA. **19.9× memory reduction** vs. gradient-based TTA. Privacy-preserving on-device adaptation.
7. **SPEED-Q** (arXiv:2511.08914): 2-bit InternVL3-1B in <400 MB RAM. **First framework to enable 2-bit unified quantization for ViT + LLM.**
8. **VL-Cache** (arXiv:2410.23317): sparsity- and modality-aware KV cache compression. 10% cache → near-full accuracy. 2.33× end-to-end latency speedup, 7.08× decoding.
9. **LiteVLM** (arXiv:2506.07416): full pipeline on NVIDIA DRIVE Thor. 2.5–3.2× speedup with patch selection, token compression, speculative decoding, FP8 PTQ.
10. **EdgeFM** (arXiv:2604.27476): open, agent-tuned edge framework. **1.49× over TensorRT-Edge-LLM on NVIDIA Orin.** SageAttention + FlashMLA support.

**Realistic target post-optimization (x86_64 laptop, CPU-only):** 10–15 s → 3–5 s per salient frame. On aarch64 + NPU: 250 ms target is achievable with VLCache + VisionTrim + SpecVLM combined.

### Gemma3-270M as a thermal fallback

For thermal-throttled scenarios (SoC > threshold), drop VLM entirely and use Gemma3-270M as a text-only "what's the most likely user intent right now" predictor. This is the right thermal design and is supported by the spec's mention of Gemma as a fallback. Wire it up.

### CoVSpec — device–edge co-inference

**This is the v6 add for the tethered-glasses path.**[^covspec] CoVSpec is a device–edge co-inference framework for VLMs:
- **Mobile side:** a draft VLM operates on a compact set of visual tokens.
- **Edge side:** the full target VLM verifies using all tokens.
- **Adaptive drafting:** dynamically adjusts draft length and verification frequency.
- **Result:** **2.21× throughput** over target-only, **96% bandwidth reduction** in communication overhead, no accuracy loss.

**Why this matters for Dan Glasses v1.5:**
- The wearable can run a 100–200 MB draft VLM on-device.
- The edge (phone or laptop) runs the full 400 MB target VLM.
- The wearable transmits only the compact visual tokens + draft logits.
- Battery life on the wearable is dominated by the *draft* VLM, not the target. **This is the architecture for the Redax-or-tethered-glasses path.**

---

## 2. HRM-Text 1B (Reasoning Language Model)

### v6 new addition — the missing on-device reasoning LLM

The root `AGENTS.md` says "HRM-Text (1B) for reasoning" but the v5 model analysis didn't include it. v6 corrects this. Sapient Intelligence released **HRM-Text 1B on 2026-05-18** — three days before the v5 report.[^h1]

### Current state
- **Architecture:** Hierarchical Reasoning Model (HRM). Dual-timescale recurrent architecture. Inspired by brain's separation of slow deliberate reasoning from fast lower-level processing.
- **Params:** 1.15 B.
- **Training:** 40 B structured tokens (1000× less than typical 4–36 T pretraining runs). Full pretraining in ~1 day for ~$1,000.
- **Inference:** reasoning in **continuous latent space**, not visible CoT tokens. **No CoT token burn** — this is the design choice that makes it cheap at inference.
- **License:** Sapient Intelligence — research/limited commercial. **Verify before production.**
- **Hardware target:** FlashAttention 3 + PyTorch FSDP2. Production-ready.

### Is it the right choice for v1?

**Yes, with one qualification.** The qualification: HRM-Text 1B is a **pre-trained base** with no post-training (no SFT, no RLHF, no chat tuning). The Sapient team explicitly notes: "HRM-Text is a proof-of-concept base model and has not undergone post-training or reinforcement learning."[^h2]

**For Dan Glasses specifically:**
- The job is **reasoning over retrieved memories + raw multimodal descriptions** to produce the user-facing response. Not open-ended chat.
- A 1.15B base model with our own SFT (on Dan Glasses' voice, persona, response style) is the right call. **We own the post-training.**
- **The 1000× less training data** claim is the headline. A 1-day, $1,000 pretraining run means we can iterate on variants quickly.

### Alternatives

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **HRM-Text 1B** (Sapient) | 1.15 B | Latent-space reasoning, no CoT burn, 1-day pretrain. | Base model — needs our SFT. License: verify. |
| **LFM2-1.2B-Thinking** | 1.2 B | Already a "thinking" model; we have it in the danlab-multimodal roadmap. | Visible CoT — burns tokens. |
| **Gemma3-270M (text-only)** | 270 MB | Tiny, fast. | Reasoning quality low. Use as thermal fallback, not primary. |
| **Qwen3-4B / 8B** (HarnessForge baseline) | 4–8 B | Open, well-tuned. | Too big for wearable in 2026. Tethered path only. |
| **Phi-4-mini (3.8 B)** | 3.8 B | Microsoft, strong reasoning, open. | Too big for wearable primary. |

### Hardware targets for HRM-Text 1B

- **aarch64 + NPU (Snapdragon AR1, Hexagon NPU, Apple Neural Engine)**: target ~30–50 tok/s decode, ~0.3–0.6 W power.
- **x86_64 laptop CPU**: target ~10–20 tok/s decode, ~1–2 W power.
- **Raspberry Pi 5**: target ~2–5 tok/s decode, ~1 W power. (Crutchfield path.)

### v6 architectural commitment

**HRM-Text 1B is the on-device reasoning LLM for Dan Glasses v1.5.** We commit to:
- Running our own SFT pass on HRM-Text-1B base using Dan Glasses' voice/persona data.
- SFT on a held-out user-interaction eval set.
- **Publishing the SFT recipe as open-source.** This is part of the "world's best skills library" positioning.

---

## 3. whisper.cpp / ggml-base.bin (Speech-to-Text)

### Current state (verified live)
- **Binary:** `/usr/local/bin/whisper-cli` (1.0 MB statically-linked, from whisper.cpp 2025-04-18 commit).
- **Models:** `ggml-base.bin` (148 MB, default) and `ggml-tiny.bin` (78 MB, recommended for Redax aarch64).
- **Flags:** `-ng` (no GPU), `-ml 1` (max segment length 1, faster first result), `-l auto` or `-l en`.
- **Live performance:** 400–700 ms end-to-end for short utterances on x86_64 with ggml-tiny.
- **VAD:** Silero VAD via ONNX Runtime (no torch dependency). 0.5 threshold, 250 ms min speech, 200 ms min silence. Energy fallback if ONNX missing.
- **Streaming:** No. whisper-cli is segment-based. Streaming is "v3" in the spec.

### Is it the right choice for v1?

**Yes.** whisper.cpp is the most mature, cross-platform, open-source STT runtime. `ggml-base.bin` is a strong default; `ggml-tiny.bin` is the right choice for the aarch64 wearable.

### What's missing for a true wearable

- **Wake-word.** This is the **biggest gap**. Push-to-talk is the v1 default per spec; wake-word is "deferred to v3." For a wearable to be a wearable, it needs a wake-word. The audiod spec has `wakewordd` in the v3 roadmap — **promote to v1.1.**
  - **Pick:** `openWakeWord` (open-source, runs on CPU, ~50 mW continuous) or Porcupine (commercial, on-device, more accurate).
  - **Latency target:** <200 ms utterance → wake event.
  - **Where:** Standalone `wakewordd` on port 8095 using ONNX Runtime, OR fold into audiod as a pre-VAD stage.
  - **Why on-device:** cloud wake-word is a privacy non-starter and a battery non-starter.
- **Streaming whisper.** Currently segment-based. For sub-second latency on long utterances, streaming is needed. whisper.cpp has a `whisper-stream` (community fork) with chunked inference. Evaluate for v1.5.
- **Noise suppression (RNNoise).** Pre-VAD. Cheap (3 MB model, <5 ms/frame). Big win for noisy environments. Wire into audiod capture.py.
- **Speaker diarization.** For "who said what" in multi-user scenarios. pyannote.audio is the standard. Not v1 priority.

### Alternatives to whisper.cpp

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **whisper.cpp** (current) | 78–769 MB | Mature, cross-platform, Rust bindings, VAD integration available. | Segment-only (no streaming). |
| **Parakeet** (NVIDIA) | ~150 MB | Streaming, fast, good English accuracy. | Less mature in C++ runtime; limited language support. |
| **Moonshine** | ~250 MB | Real-time, edge-optimized. | Newer; less battle-tested. |
| **Distil-Whisper** | ~150 MB | 6× faster than whisper-large, comparable quality. | Same constraints as whisper. |
| **Canary** (NVIDIA) | ~1 GB | Multilingual, SOTA accuracy. | Too big for wearable. |
| **AI4Bharat / IndicWhisper** | 150–800 MB | Indic-language fine-tunes. | Critical for India bet. Evaluate for v1.5. |

### v6 add — multilingual India STT

**The Indian-language angle is the strategic bet.** If Dan Glasses is going to be "from India" and serve Indic users, whisper-base.en is not enough. Options:
- **AI4Bharat / IndicWhisper** — fine-tunes of whisper on 22 Indic languages. 150–800 MB.
- **Bhashini / ULCA** — government-backed ASR/TTS API for Indic languages. Cloud.
- **seamlessM4T** (Meta) — multilingual speech + translation, ~1 B params. Heavy but covers 100+ languages.

**Recommendation:** for v1.1 add **IndicWhisper-hi** and **IndicWhisper-ta** to the model registry. For v2, evaluate **Bhashini ULCA** as a cloud fallback for low-resource languages.

**Recommendation: keep whisper.cpp for v1 and v1.5.** The wake-word gap, the noise-suppression gap, and the Indic gap are higher priority than switching STT engines.

---

## 4. KittenTTS (Text-to-Speech)

### Current state (verified live)
- **Service:** `ttsd` on port 8743, returning `audio/wav` (24 kHz float).
- **Model:** "medium" per spec — **this is not a canonical KittenTTS variant.** Canonical lineup (per `kittenml/kittentts` v0.8, Feb 2026): **nano (15M, ~25 MB int8), micro (40M, ~41 MB), mini (80M, ~80 MB)**.
- **Voice:** "expr-voice-2-m" hardcoded.
- **Latency:** 218 KB WAV per `/speak` call (no timing data in the spec — need to measure).
- **License:** Apache 2.0.

### Is it the right choice for v1?

**Yes, with one clarification.** KittenTTS is the right model family. The "medium" reference in the spec needs to be reconciled with the actual KittenTTS v0.8 lineup. Likely explanation: a custom build or an older label. **Verify.**

**Recommended mapping:**
- **Laptop dev path (x86_64, AC-powered):** `kitten-tts-mini` (80M, ~80 MB). Highest quality.
- **Wearable (aarch64, battery-powered):** `kitten-tts-nano-int8` (15M, ~25 MB). 8–9× real-time. Quality is "lowest" but adequate for spoken feedback.
- **Lowest-power mode (sleep / wake-word response):** `kitten-tts-nano` (15M, FP) at ~56 MB. Even smaller, but not int8 quantized.

### What could beat it?

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **KittenTTS v0.8** (current family) | 25–80 MB | Open-source, Apache 2.0, on-device, multiple variants, 8 voices. | Quality is "good enough" not "great." |
| **Piper TTS** | 15–60 MB | Mature, many voices, many languages. | Slower than KittenTTS-nano; older. |
| **Orca** (Microsoft) | ~100 MB | High quality, streaming. | Heavier; Microsoft-y licensing. |
| **CosyVoice** (Alibaba) | ~300 MB | SOTA Chinese + multilingual. | Too big for wearable. |
| **StyleTTS2** | ~250 MB | High quality. | Too big for wearable. |
| **edge-tts** | API | Free, 200+ neural voices, no API key. | Cloud — defeats privacy story. Use as fallback only. |
| **Bhashini TTS** | API | Indic languages. | Cloud — same caveat. |

**Recommendation: stay with KittenTTS.** The variant selection is the only thing to fix. For v1.5, evaluate `kitten_tts_rs` (Second State's Rust port, no Python dep, OpenAI-compatible API) as a replacement for the Python/ONNX path. ~10 MB binary + model = much smaller process footprint.

### Voices
- 8 built-in voices: Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, Leo.
- Currently hardcoded to `expr-voice-2-m` (not a KittenTTS voice). **Fix this** in ttsd. Let the bootstrap wizard pick a voice and persist it as a semantic memory.

### Streaming TTS
For "I want the assistant to start speaking before it finishes generating" UX, we need streaming TTS. KittenTTS v0.8 supports it. Wire it up: chunk by sentence (≤ 400 chars), stream audio chunks to the speaker as they synthesize. Cuts first-audio latency from "full utterance" to "first sentence."

---

## 5. all-MiniLM-L6-v2 (Memory Embeddings)

### Current state (verified live)
- **Model:** `sentence-transformers/all-MiniLM-L6-v2`, 384-dim float32.
- **Storage:** BLOB in SQLite.
- **Scoring:** Cosine similarity only.

### Is it the right choice for v1?

**It's a 2024-era choice and the right place to invest in v1.5.** MiniLM-L6 is small (22 MB), fast (~5 ms/query on CPU), and supports 384-dim embeddings. The model itself is fine.

**What's missing is the *memory architecture*, not the model.** Per the architecture review §6 and the research report section B8:

**v1.5 changes (2 weeks):**
1. Add temporal metadata (created_at, last_accessed, access_count, decay_rate).
2. Add confidence decay (Ebbinghaus-style).
3. Add relational scoring (4-signal: semantic × temporal × confidence × relational_bonus).
4. Add a `ConsolidationAgent` cron job (every 6 h) that boosts/decays and tags "supersedes" chains.
5. Add BM25 (FTS5) index on `content`.
6. Add `memory_links` table with the 7 relation types from MemX.

**v2 changes (Q1–Q2 2027):**
1. **Memanto-style typed semantic schema** — 13 memory categories, automatic conflict resolution.
2. **MemMachine-style three-layer** — short-term working + long-term episodic + semantic/profile.
3. **AriadneMem-style connected subgraph retrieval** — for multi-hop reasoning.

### Embedding model alternatives

| Alternative | Dim | Size | Why consider | Why not |
|-------------|-----|------|--------------|---------|
| **all-MiniLM-L6-v2** (current) | 384 | 22 MB | Fast, small, decent quality. | 2024-era. |
| **all-mpnet-base-v2** | 768 | 110 MB | Better quality. | 2× slower; 4× storage. |
| **BGE-small-en-v1.5** | 384 | 33 MB | Better retrieval quality than MiniLM. | Slightly bigger. |
| **nomic-embed-text-v1.5** | 768 | 137 MB | SOTA retrieval. | Heavy. |
| **E5-small-v2** | 384 | 33 MB | Microsoft, good quality. | Similar to BGE-small. |
| **Cohere embed-multilingual-v3** | 1024 | API | Best multilingual. | Cloud. Defeats the privacy story. |
| **bge-m3** | 1024 | 567 MB | SOTA multilingual, dense+sparse+multi-vector. | Heavy. |
| **bge-m3-onnx** | 1024 | ~300 MB | SOTA multilingual, on-device. | Heavy but on-device is possible. |
| **Nomic Embed v2 (matryoshka)** | 768 | ~300 MB | Matryoshka representation learning — flexible dimensionality. | Newer; less battle-tested. |

**Recommendation:** **Switch to `BGE-small-en-v1.5`** (384-dim, 33 MB) in v1.5. Better retrieval quality than MiniLM at the same dimensionality. The model swap is a 1-day change to memoryd. The architecture change (temporal + confidence + relational + BM25 + graph) is the real lift.

For **multilingual** (Hindi/Tamil/Bengali) coverage in v2, evaluate `bge-m3` (dense+sparse+multi-vector, 567 MB) or `nomic-embed-text-v1.5` (137 MB) — but only if we have the compute.

---

## 6. The bigger picture: model + accelerator co-design

The 2026 research is converging on **model + hardware co-design** as the path to wearable AI:

- **Nanomind** (arXiv 2510.05109): decomposes LMMs into modular bricks (vision, projector, language, audio), maps each to the most suitable accelerator (NPU, GPU, DSP), Token-Aware Buffer Manager for zero-copy transfers. **42.3% energy reduction.** LLaVA-OneVision-Qwen2-0.5B + camera → **18.8 hours on 2000 mAh battery**. This is the playbook.
- **TAO** (arXiv 2506.18584): temperature-aware offloading. Reduces offload cost by 35% while meeting power/thermal/energy constraints.
- **Multi-LoRA on Snapdragon NPU** (arXiv 2604.18655v2): INT4 weights, INT8 activations, per-channel quantization. 4–6× memory and latency improvements. **Proven on Samsung Galaxy S24/S25.** This is the production path for sub-500 MB VLMs on Qualcomm AR1.
- **EdgeFM** (arXiv 2604.27476): agent-driven kernel optimization, 1.49× over TensorRT-Edge-LLM on Orin. **The production-ready open framework for edge VLM.**
- **LiteVLM** (arXiv 2506.07416): full pipeline on DRIVE Thor. 2.5–3.2× with FP8 PTQ.
- **CoVSpec** (arXiv 2605.02218): device–edge co-inference. 2.21× throughput. **This is the right architecture for the tethered-glasses path.**

### Implication for Dan Glasses v1.5/v2: don't just pick a model — pick a model + a quantization scheme + a target accelerator.

The right matrix:

| Model | Quant | Target accelerator | Latency | Battery impact |
|-------|-------|--------------------|---------|----------------|
| LFM2.5-VL-450M (vision) | Q4_0 | CPU (Redax aarch64) | 10–15 s | 1.5 W avg watchful |
| LFM2.5-VL-450M (vision) | Q4_0 | Hexagon NPU (AR1) | 250 ms target | 0.5 W avg watchful |
| LFM2.5-VL-450M + VLCache + VisionTrim + SpecVLM | Q4_0 | Hexagon NPU | 65 ms | 0.3 W avg watchful |
| LFM2.5-VL-450M (draft) + edge (target) — CoVSpec | Q4_0 | CPU draft, edge target | 2.21× throughput | wearable 0.4 W |
| Gemma3-270M (text-only fallback) | IQ4_XS | CPU | 100 ms | 0.1 W avg |
| KittenTTS-nano-int8 | int8 | CPU | 8–9× real-time | 0.05 W avg |
| whisper-tiny | q5_1 | CPU | 200–500 ms | 0.3 W avg |
| BGE-small-en-v1.5 | fp32 | CPU | 5 ms/query | 0.05 W avg |
| HRM-Text 1B (reasoning) | Q4 | Hexagon NPU / CPU | 30–50 tok/s | 0.3–0.6 W |
| HRM-Text 1B + our SFT | Q4 | Hexagon NPU | 30–50 tok/s | 0.3–0.6 W |

**Pick the matrix for the wearable, not just the models.** The Redax decision (or the indie hardware path) determines which cells are achievable.

### Hardware targets for 2026

- **Apple Neural Engine (M5 / Vision Pro 2)**: 4× GPU AI perf, very low power for fixed-shape ops. Best per-watt for our size class. But Apple-locked.
- **Qualcomm Hexagon NPU (Snapdragon X Elite / 8 Elite Gen 2)**: Hexagon NPU is the right target for aarch64 wearables. llama.cpp's Hexagon backend is improving but not yet production.
- **Hailo-10H**: 6.9 tok/s sustained on Qwen 2.5 1.5B, ~2 W, thermally stable. But VLM support is early; SigLIP encoder not yet optimized on Hailo.
- **AMD Ryzen AI HX 375**: 50.7 tok/s on Llama 3.2 1B with iGPU, but battery-throttled.
- **Blaize GSP / Winmate** (COMPUTEX 2026): rugged edge AI. **Worth tracking for industrial/field wearables.**
- **Loft Orbital + JPL (Gemma 3 in orbit)**: space-grade edge. **Not directly relevant, but the philosophy of "small VLM on edge" is now mainstream.**

**Recommendation:** for the laptop prototype, stick with CPU llama.cpp + Q4_0. For the wearable, target **Hexagon NPU with llama.cpp's Hexagon backend when stable, and degrade to CPU if not.** Don't optimize for Hailo or Ryzen AI yet. **For the tethered-glasses path, use CoVSpec with a draft VLM on-device + full VLM on the phone.**

---

## 7. What to ship in v1 (now)

1. **Reconcile KittenTTS "medium"** in ttsd — pick `mini` (laptop) or `nano-int8` (wearable).
2. **Fix hardcoded voice** — let the wizard pick from KittenTTS's 8 voices.
3. **Wire VisionTrim** (training-free, 2–3× VLM speedup) into perceptiond. Drop-in.
4. **Wire VLMCache / VLCache** (1.4–16× for stable scenes) into perceptiond. Drop-in for the watchful mode.
5. **Add SalienceDetector → VLM gate** so we don't run VLM on every frame.
6. **Switch memoryd embedding** to `BGE-small-en-v1.5` (or stay with MiniLM if benchmarks don't show clear gain).
7. **Measure LFM2.5-VL-450M real power on x86_64 and on aarch64+NPU sim.** Stop using the spec's "150–800 ms" — get the real numbers.
8. **Document the HRM-Text 1B + LFM2.5-VL-450M two-model split** in the AGENTS.md files. This is the v6 architecture commitment.

## What to ship in v1.5 (Q3–Q4 2026)

9. **`wakewordd` with openWakeWord.** Biggest UX upgrade.
10. **`powerd` (state machine) + thermal-aware throttling.** Drops to Gemma3-270M text-only when hot.
11. **Proactive trigger layer** in OpenClaw. Microsoft Research graph encoder + PRISM gate. (See `dan2-architecture-review.md` §10.)
12. **HRM-Text 1B SFT pass** on Dan Glasses' voice/persona. Open-source the recipe.
13. **Streaming whisper** (`whisper-stream` fork).
14. **RNNoise** pre-VAD in audiod.
15. **Memory v1.5: temporal + confidence + relational + BM25 + graph links.** MemX-style 4-layer.
16. **Streaming KittenTTS** for sub-second first-audio latency.
17. **IndicWhisper-hi + IndicWhisper-ta** for Indian-language STT. v1.5 India bet.
18. **CoVSpec draft VLM** for the tethered-glasses path. ~100–200 MB draft model on-device + full LFM2.5-VL on phone.

## What to ship in v2 (2027)

19. **Memory v2: MemMachine + Memanto hybrid.** Three-layer + typed semantic schema.
20. **Multilingual embeddings** (bge-m3 or nomic-embed) when we have Hindi/Tamil/Bengali content.
21. **Multi-LoRA on the NPU** (per the Samsung Galaxy paper) for user-specific model adapters.
22. **RHO / SIA / HarnessForge fork** in danlab-multimodal. Now it's real self-improvement.
23. **TT-SI in danlab-multimodal v3.** Test-time self-improvement.
24. **AriadneMem-style connected subgraph retrieval** in memoryd. Multi-hop reasoning.

---

## What NOT to do

- ❌ Don't switch the VLM away from LFM2.5-VL-450M in v1. It's the right choice; the gaps are in the acceleration layer.
- ❌ Don't switch the STT away from whisper.cpp. It's the right choice; the gap is the wake-word and Indic languages.
- ❌ Don't switch the TTS away from KittenTTS. It's the right family; the gap is the variant + streaming.
- ❌ Don't try to fine-tune LFM2.5-VL-450M in the loop. The compute cost is prohibitive on the target hardware. Use a smaller reward model instead.
- ❌ Don't bring in frontier-class models (GPT-5.5, Claude Opus 4.6, Gemini 3.1 Pro, Fable 5/Mythos) as dependencies. Cloud defeats the privacy story. The whole point of Dan Glasses is **on-device**.
- ❌ Don't treat HRM-Text 1B as a "just-another-1B-LLM." It's a *latent-space reasoning* model. Different design point. Different inference characteristics. Different training economics (1-day, $1,000 pretrain). Our SFT pass is part of the value-add.
- ❌ Don't conflate the LFM2.5-VL (vision encoder) and HRM-Text 1B (reasoning LLM). They are two different models, two different jobs, two different acceleration paths.

---

## Footnotes

[^h1]: Sapient Intelligence launches HRM-Text 1B, May 18, 2026. https://www.prnewswire.com/news-releases/sapient-intelligence-launches-hrm-text-challenging-the-llm-monopoly-with-a-brain-inspired-foundation-model-trained-on-up-to-1000x-fewer-tokens-302774638.html
[^h2]: Sapient Inc — Introducing HRM-Text. https://sapient.inc/introducing-hrm-text
[^gemma_space]: TechCrunch — A satellite just learned to find things on its own (Gemma 3 on Yam-9 satellite via Loft Orbital + JPL). 2026-06-15. https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/
[^covspec]: CoVSpec: Efficient Device–Edge Co-Inference for Vision-Language Models via Speculative Decoding. arXiv:2605.02218. https://arxiv.org/html/2605.02218v1

---

*👾* Model choices are right (v1.5: add HRM-Text 1B as reasoning LLM). The next 90 days are about acceleration (VLCache, VisionTrim, SpecVLM, CoVSpec, salience gating), the wake-word gap, the memory architecture, and the proactive trigger layer — not about replacing the model lineup. v6 deltas: HRM-Text 1B added, VLCache + VLMQ + SPEED-Q + LQA + EdgeFM + CoVSpec added to the acceleration layer, Gemma 3 in space noted, multilingual India STT path opened.
-device (SmolVLM-256M) and the laptop/phone runs LFM2.5-VL-450M as verifier. This is the **"smart glasses + phone"** architecture, not the "all-on-glasses" architecture. Same as Brilliant Labs Frame.
- 96% bandwidth reduction is a non-trivial power saver on wireless links.
- **Cheaper than running LFM2.5-VL-450M on the wearable.** Spec the tethered path now, the standalone path later.

---

## 2. HRM-Text 1B (Reasoning LLM) — v6 NEW

### Current state (not yet deployed)
- **Model:** Sapient Intelligence HRM-Text 1B, 1.15B parameters, hierarchical recurrent architecture.
- **Released:** May 18, 2026.
- **Training:** 40 B structured tokens (1000× less than typical LLM training), ~1 day on a $1,000 compute budget.
- **Inference cost:** low. Performs reasoning in **continuous latent space**, not visible CoT tokens. This is the design choice that makes it cheap at inference.
- **Status:** proof-of-concept base model. **No post-training, no RL.** This is the "substrate" for fine-tuning.
- **License:** verify before production deployment (Sapient Inc).

### Why it's the right reasoning LLM for Dan Glasses

| Property | HRM-Text 1B | Typical 1B Transformer LLM | Frontier LLM (70B+) |
|----------|------------|--------------------------|---------------------|
| Parameters | 1.15B | 1B | 70B+ |
| Reasoning style | Continuous latent (no token burn) | Visible CoT tokens | Visible CoT tokens |
| Training tokens | 40B structured | 4–36T | 4–36T |
| Pre-train cost | ~$1,000, 1 day | $$$$ | $$$$$$ |
| Inference cost | Low (no CoT burn) | Medium (long CoT) | High |
| On-device fit | Excellent (1.15B fits in 2–3 GB RAM with Q4) | Good | No (cloud only) |
| Reasoning quality | Competitive w/ much larger models (per Sapient) | Lower | Best |

**The Dan Glasses use case:**
- User asks a complex question ("summarize my meeting yesterday and what I committed to").
- Pipeline: retrieve memories → HRM-Text 1B reasons over them in latent space → outputs a 200-word summary.
- **No 10,000-token CoT burn.** No $0.10 cloud API call. **All on-device.**
- The "agenda" memory: HRM-Text 1B is meant to be fine-tuned to specific tasks. **The natural task for us is "reason over my memories and produce an answer."** This is the danlab-multimodal + dan-glasses convergent use case.

### What if HRM-Text 1B doesn't ship in time / doesn't perform?

- **LFM2-1.2B-Thinking** is the fallback — a 1.2 B reasoning model from the same LFM family. Lower quality but a known quantity.
- **Phi-4-mini-reasoning** (Microsoft, 3.8 B) — heavier but proven.
- **Qwen3-1.7B** — open-weight, good reasoning, multilingual.

For v1, **HRM-Text 1B is the bet.** If it doesn't pan out, LFM2-1.2B-Thinking is the swap. The pipeline doesn't change.

### v6 architecture note: HRM-Text 1B + LFM2.5-VL-450M are NOT the same model

**v5 conflated these.** LFM2.5-VL-450M is a vision-language model — it encodes images and produces text. HRM-Text 1B is a text-only reasoning model — it does not see images. The pipeline is:

```
[image] → LFM2.5-VL-450M → text description
                                ↓
                          [memory retrieval]
                                ↓
                          HRM-Text 1B → reasoned response
                                ↓
                          [text] → KittenTTS → audio
```

**Two models. One pipeline. Each does what it's good at.** This is the v6 definitive architecture.

---

## 3. whisper.cpp / ggml-base.bin (Speech-to-Text)

### Current state (verified live)
- **Binary:** `/usr/local/bin/whisper-cli` (1.0 MB statically-linked, from whisper.cpp 2025-04-18 commit).
- **Models:** `ggml-base.bin` (148 MB, default) and `ggml-tiny.bin` (78 MB, recommended for Redax aarch64).
- **Flags:** `-ng` (no GPU), `-ml 1` (max segment length 1, faster first result), `-l auto` or `-l en`.
- **Live performance:** 400–700 ms end-to-end for short utterances on x86_64 with ggml-tiny.
- **VAD:** Silero VAD via ONNX Runtime (no torch dependency). 0.5 threshold, 250 ms min speech, 200 ms min silence. Energy fallback if ONNX missing.
- **Streaming:** No. whisper-cli is segment-based. Streaming is "v3" in the spec.

### Is it the right choice for v1?

**Yes.** whisper.cpp is the most mature, cross-platform, open-source STT runtime. `ggml-base.bin` is a strong default; `ggml-tiny.bin` is the right choice for the aarch64 wearable.

### What's missing for a true wearable

- **Wake-word.** This is the **biggest gap**. Push-to-talk is the v1 default per spec; wake-word is "deferred to v3." For a wearable to be a wearable, it needs a wake-word. The audiod spec has `wakewordd` in the v3 roadmap — **promote to v1.1.**
  - **Pick:** `openWakeWord` (open-source, runs on CPU, ~50 mW continuous) or Porcupine (commercial, on-device, more accurate).
  - **Latency target:** <200 ms utterance → wake event.
  - **Where:** Standalone `wakewordd` on port 8095 using ONNX Runtime, OR fold into audiod as a pre-VAD stage.
  - **Why on-device:** cloud wake-word is a privacy non-starter and a battery non-starter.
- **Streaming whisper.** Currently segment-based. For sub-second latency on long utterances, streaming is needed. whisper.cpp has a `whisper-stream` (community fork) with chunked inference. Evaluate for v1.5.
- **Noise suppression (RNNoise).** Pre-VAD. Cheap (3 MB model, <5 ms/frame). Big win for noisy environments. Wire into audiod capture.py.
- **Speaker diarization.** For "who said what" in multi-user scenarios. pyannote.audio is the standard. Not v1 priority.

### v6 alternatives to whisper.cpp

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **whisper.cpp** (current) | 78–769 MB | Mature, cross-platform, Rust bindings, VAD integration available. | Segment-only (no streaming). |
| **Parakeet** (NVIDIA) | ~150 MB | Streaming, fast, good English accuracy. | Less mature in C++ runtime; limited language support. |
| **Moonshine** | ~250 MB | Real-time, edge-optimized. Transformer + compact LLM on 1 TOPS NPU. | Newer; less battle-tested. |
| **Distil-Whisper** | ~150 MB | 6× faster than whisper-large, comparable quality. | Same constraints as whisper. |
| **Canary** (NVIDIA) | ~1 GB | Multilingual, SOTA accuracy. | Too big for wearable. |

**Recommendation: keep whisper.cpp for v1 and v1.5.** The wake-word gap and the noise-suppression gap are higher priority than switching STT engines. For v2 (multilingual India), evaluate **Parakeet** for streaming + Hindi/Tamil/Bengali accuracy.

---

## 4. KittenTTS (Text-to-Speech)

### Current state (verified live)
- **Service:** `ttsd` on port 8743, returning `audio/wav` (24 kHz float).
- **Model:** "medium" per spec — **this is not a canonical KittenTTS variant.** Canonical lineup (per `kittenml/kittentts` v0.8, Feb 2026): **nano (15M, ~25 MB int8), micro (40M, ~41 MB), mini (80M, ~80 MB)**.
- **Voice:** "expr-voice-2-m" hardcoded.
- **Latency:** 218 KB WAV per `/speak` call (no timing data in the spec — need to measure).
- **License:** Apache 2.0.

### Is it the right choice for v1?

**Yes, with one clarification.** KittenTTS is the right model family. The "medium" reference in the spec needs to be reconciled with the actual KittenTTS v0.8 lineup. Likely explanation: a custom build or an older label. **Verify.**

**Recommended mapping:**
- **Laptop dev path (x86_64, AC-powered):** `kitten-tts-mini` (80M, ~80 MB). Highest quality.
- **Wearable (aarch64, battery-powered):** `kitten-tts-nano-int8` (15M, ~25 MB). 8–9× real-time. Quality is "lowest" but adequate for spoken feedback.
- **Lowest-power mode (sleep / wake-word response):** `kitten-tts-nano` (15M, FP) at ~56 MB. Even smaller, but not int8 quantized.

### What could beat it?

| Alternative | Size | Why consider | Why not |
|-------------|------|--------------|---------|
| **KittenTTS v0.8** (current family) | 25–80 MB | Open-source, Apache 2.0, on-device, multiple variants, 8 voices. | Quality is "good enough" not "great." |
| **Piper TTS** | 15–60 MB | Mature, many voices, many languages. | Slower than KittenTTS-nano; older. |
| **Orca** (Microsoft) | ~100 MB | High quality, streaming. | Heavier; Microsoft-y licensing. |
| **CosyVoice** (Alibaba) | ~300 MB | SOTA Chinese + multilingual. | Too big for wearable. |
| **StyleTTS2** | ~250 MB | High quality. | Too big for wearable. |
| **edge-tts** (cloud) | 0 MB local | Free, 200+ neural voices, no API key. | Cloud. Defeats the privacy story. |

**Recommendation: stay with KittenTTS.** The variant selection is the only thing to fix. For v1.5, evaluate `kitten_tts_rs` (Second State's Rust port, no Python dep, OpenAI-compatible API) as a replacement for the Python/ONNX path. ~10 MB binary + model = much smaller process footprint.

### Voices
- 8 built-in voices: Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, Leo.
- Currently hardcoded to `expr-voice-2-m` (not a KittenTTS voice). **Fix this** in ttsd. Let the bootstrap wizard pick a voice and persist it as a semantic memory.

### Streaming TTS
For "I want the assistant to start speaking before it finishes generating" UX, we need streaming TTS. KittenTTS v0.8 supports it. Wire it up: chunk by sentence (≤ 400 chars), stream audio chunks to the speaker as they synthesize. Cuts first-audio latency from "full utterance" to "first sentence."

---

## 5. all-MiniLM-L6-v2 (Memory Embeddings)

### Current state (verified live)
- **Model:** `sentence-transformers/all-MiniLM-L6-v2`, 384-dim float32.
- **Storage:** BLOB in SQLite.
- **Scoring:** Cosine similarity only.

### Is it the right choice for v1?

**It's a 2024-era choice and the right place to invest in v1.5.** MiniLM-L6 is small (22 MB), fast (~5 ms/query on CPU), and supports 384-dim embeddings. The model itself is fine.

**What's missing is the *memory architecture*, not the model.** Per `dan2-architecture-review.md` §6 and the research report section B8:

**v1.5 changes (2 weeks):**
1. Add temporal metadata (created_at, last_accessed, access_count, decay_rate).
2. Add confidence decay (Ebbinghaus-style).
3. Add relational scoring (4-signal: semantic × temporal × confidence × relational_bonus).
4. Add a `ConsolidationAgent` cron job (every 6h) that boosts/decays and tags "supersedes" chains.
5. Add BM25 (FTS5) keyword index. RRF over vector + keyword (MemX pattern).
6. Add `memory_links` table with the 7 relation types from MemX.
7. Add MemGate-style retrieval filter (small MLP that filters out irrelevant memories before they hit the LLM context).

**v2 changes (Q1–Q2 2027):**
1. **Dual-process memory** (DPA / DPCM): synchronous daytime writer + async nighttime schema induction.
2. **TiMem-style Temporal Memory Tree**: hierarchy of (raw events → episodic → semantic → procedural → schema).
3. **CategoryRAG** with hallucination resistance (Synthius-Mem, 99.6% on adversarial).
4. **MemMachine-style three-layer** + **Memori-style triples** for production-shape.

### v6 add: Memanto (May 2026) — the case for vector-first

Memanto (arXiv:2604.22085) is a **purely vector-based** memory backend that achieves SOTA on LongMemEval and LoCoMo. Its claim: graph + vector hybrids add complexity without improving performance. Modern LLMs handle the reasoning/filtering that graph precomputation aimed to address.

**Implication for Dan Glasses:** the architectural decision between MemX-style (vector + keyword + graph) vs Memanto-style (pure vector + types) is not yet settled. v1.5 should implement the **MemX-style** path (more flexibility, more complex), with the option to **simplify to Memanto-style** if benchmark numbers don't justify the complexity. **Don't commit to one until v1.5 benchmarks are in.**

### Embedding model alternatives

| Alternative | Dim | Size | Why consider | Why not |
|-------------|-----|------|--------------|---------|
| **all-MiniLM-L6-v2** (current) | 384 | 22 MB | Fast, small, decent quality. | 2024-era. |
| **all-mpnet-base-v2** | 768 | 110 MB | Better quality. | 2× slower; 4× storage. |
| **BGE-small-en-v1.5** | 384 | 33 MB | Better retrieval quality than MiniLM. | Slightly bigger. |
| **nomic-embed-text-v1.5** | 768 | 137 MB | SOTA retrieval. | Heavy. |
| **E5-small-v2** | 384 | 33 MB | Microsoft, good quality. | Similar to BGE-small. |
| **Cohere embed-multilingual-v3** | 1024 | API | Best multilingual. | Cloud. Defeats the privacy story. |
| **bge-m3** | 1024 | 567 MB | SOTA multilingual, dense+sparse+multi-vector. | Heavy. |
| **GTE-Qwen2-1.5B-instruct** | 1536 | 1.5B | SOTA MTEB v2 benchmark. | Heavier; more capable. |

**Recommendation:** **Switch to `BGE-small-en-v1.5`** (384-dim, 33 MB) in v1.5. Better retrieval quality than MiniLM at the same dimensionality. The model swap is a 1-day change to memoryd. The architecture change (temporal + confidence + relational) is the real lift.

For **multilingual** (Hindi/Tamil/Bengali) coverage in v2, evaluate `bge-m3` or `nomic-embed-text-v1.5` — but only if we have the compute.

---

## 6. The bigger picture: model + accelerator co-design

The 2026 research is converging on **model + hardware co-design** as the path to wearable AI:

- **Nanomind** (arXiv 2510.05109): decomposes LMMs into modular bricks (vision, projector, language, audio), maps each to the most suitable accelerator (NPU, GPU, DSP), Token-Aware Buffer Manager for zero-copy transfers. **42.3% energy reduction.** LLaVA-OneVision-Qwen2-0.5B + camera → **18.8 hours on 2000 mAh battery**. This is the playbook.
- **TAO** (arXiv 2506.18584): temperature-aware offloading. Reduces offload cost by 35% while meeting power/thermal/energy constraints.
- **Multi-LoRA on Snapdragon NPU** (arXiv 2604.18655v2): INT4 weights, INT8 activations, per-channel quantization. 4–6× memory and latency improvements. **Proven on Samsung Galaxy S24/S25.** This is the production path for sub-500 MB VLMs on Qualcomm AR1.

### v6 — acceleration matrix (now richer)

| Model | Quant | Target accelerator | Latency | Battery impact |
|-------|-------|--------------------|---------|----------------|
| LFM2.5-VL-450M | Q4_0 | CPU (Redax aarch64) | 10–15 s | 1.5 W avg watchful |
| LFM2.5-VL-450M | Q4_0 | Hexagon NPU (AR1) | 250 ms target | 0.5 W avg watchful |
| LFM2.5-VL-450M + VisionTrim + VLCache | Q4_0 | Hexagon NPU | 65–80 ms | 0.3 W avg watchful |
| LFM2.5-VL-450M (4-bit) on Snapdragon Multi-LoRA | Q4 | NPU | ~30 ms | 0.15 W avg |
| Gemma3-270M (text-only fallback) | IQ4_XS | CPU | 100 ms | 0.1 W avg |
| KittenTTS-nano-int8 | int8 | CPU | 8–9× real-time | 0.05 W avg |
| whisper-tiny | q5_1 | CPU | 200–500 ms | 0.3 W avg |
| BGE-small | fp32 | CPU | 5 ms/query | 0.05 W avg |
| **HRM-Text 1B** (reasoning) | Q4_0 | CPU | 50–200 ms (latent) | 0.2 W avg |
| **HRM-Text 1B** (reasoning) | Q4_0 | Hexagon NPU | 20–50 ms | 0.1 W avg |

**Pick the matrix for the wearable, not just the models.** The Redax decision (or the indie hardware path) determines which cells are achievable.

**v6 add — the tethered path:**

| Path | On-device model | Off-device model | Bandwidth | Latency |
|------|-----------------|-------------------|-----------|---------|
| **All-on-device** | LFM2.5-VL-450M Q4 (389 MB) | — | 0 | 250 ms target (NPU) / 10–15 s (CPU) |
| **CoVSpec tethered** | SmolVLM-256M Q4 (302 MB) draft | LFM2.5-VL-450M Q4 verifier on phone | ~1 KB/query | 100–500 ms |
| **Phone-offload** | (none on glasses) | LFM2.5-VL-450M on phone | Full image | 200–800 ms |

**For the v1.5 tethered-glasses path (Brilliant Labs Frame-style), CoVSpec is the right architecture.** SmolVLM-256M on the glasses, LFM2.5-VL-450M on the phone. 2.21× throughput, 96% bandwidth reduction. The wearable is a thin client; the phone is the brain.

---

## 7. What to ship in v1 (now)

1. **Reconcile KittenTTS "medium"** in ttsd — pick `mini` (laptop) or `nano-int8` (wearable).
2. **Fix hardcoded voice** — let the wizard pick from KittenTTS's 8 voices.
3. **Wire VisionTrim** (training-free, 2–3× VLM speedup) into perceptiond. Drop-in.
4. **Wire VLCache** (1.2–16× speedup, 2–5% vision token recompute) into perceptiond. Drop-in for watchful mode.
5. **Add SalienceDetector → VLM gate** so we don't run VLM on every frame.
6. **Add BM25 (FTS5) to memoryd.** 1-day change. RRF over vector + keyword.
7. **Add `memory_links` table** to memoryd (7 relation types from MemX).
8. **Measure LFM2.5-VL-450M real power on x86_64 and on aarch64+NPU sim.** Stop using the spec's "150–800 ms" — get the real numbers.
9. **Document the two-model pipeline** (LFM2.5-VL-450M for vision, HRM-Text 1B for reasoning). Update AGENTS.md.

## What to ship in v1.5 (Q3–Q4 2026)

10. **`wakewordd` with openWakeWord.** Biggest UX upgrade.
11. **`powerd` (state machine) + thermal-aware throttling.** Drops to Gemma3-270M text-only when hot.
12. **Streaming whisper** (`whisper-stream` fork).
13. **RNNoise** pre-VAD in audiod.
14. **Memory v1.5: temporal + confidence + relational scoring + MemGate-style filter.**
15. **Streaming KittenTTS** for sub-second first-audio latency.
16. **Evaluate HRM-Text 1B on the danlab-multimodal loop data.** If it works as a reasoning layer over memoryd retrievals, ship it.
17. **SpecVLM speculative decoding** for LFM2.5-VL-450M with a smaller draft.
18. **VLMQ low-bit PTQ** for thermal-throttled operation (Q3 quantization).
19. **CoVSpec tethered path.** If the wearable is a thin client, this is the production path.

## What to ship in v2 (2027)

20. **Memory v2: dual-process (DPA / DPCM / MemMachine / Memanto hybrid).** System 1 (sync writer) + System 2 (async schema induction).
21. **Multilingual embeddings** (bge-m3 or nomic-embed) when we have Hindi/Tamil/Bengali content.
22. **Multi-LoRA on the NPU** (per the Samsung Galaxy paper) for user-specific model adapters.
23. **TT-SI in danlab-multimodal v3.**
24. **Fork SIA** and integrate as a harness for genuine self-improvement.
25. **EdgeFM-style agent-tuned inference** for production deployment.

---

## What NOT to do

- ❌ Don't switch the VLM away from LFM2.5-VL-450M in v1. It's the right choice; the gaps are in the acceleration layer.
- ❌ Don't switch the STT away from whisper.cpp. It's the right choice; the gap is the wake-word.
- ❌ Don't switch the TTS away from KittenTTS. It's the right family; the gap is the variant + streaming.
- ❌ Don't conflate LFM2.5-VL-450M (vision) with HRM-Text 1B (reasoning). Two models, one pipeline.
- ❌ Don't try to fine-tune LFM2.5-VL-450M or HRM-Text 1B in the loop on the laptop. Use a smaller reward model instead.
- ❌ Don't bring in frontier-class models (GPT-5.5, Claude Opus 4.8, Gemini 3.1 Pro) as dependencies. Cloud defeats the privacy story. The whole point of Dan Glasses is **on-device**.
- ❌ Don't add a graph database in v1.5. SQLite + memory_links is enough. Memanto shows pure-vector can work. Don't over-engineer until v1.5 benchmarks justify it.

---

## Footnotes

[^gemma_space]: TechCrunch — A satellite just learned to find things on its own (Gemma 3 on Yam-9 satellite via Loft Orbital + JPL). 2026-06-15. https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/
[^covspec]: CoVSpec: Efficient Device–Edge Co-Inference for Vision-Language Models via Speculative Decoding. arXiv:2605.02218. https://arxiv.org/html/2605.02218v1

---

*👾* Model choices are right. The next 90 days are about acceleration (VLCache, VisionTrim, SpecVLM, salience gating, CoVSpec for tethered path), the wake-word gap, the HRM-Text 1B integration, and the memory architecture — not about replacing the model lineup. v6 deltas: HRM-Text 1B added, VLCache/VLMQ/LQA/SPEED-Q/EdgeFM/CoVSpec added, Memanto (vector-first) noted as alternative architecture.

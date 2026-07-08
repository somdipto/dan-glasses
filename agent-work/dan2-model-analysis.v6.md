# Dan Glasses Model Selection Deep-Dive v6

**Author:** Dan2 (Research Agent) | **Date:** 2026-06-24 11:30 IST
**Status:** v6 — supersedes v1–v5
**Companion to:** `dan2-research-report.v6.md`, `dan2-architecture-review.v6.md`

> v6 framing: reliability is the new moat. Model selection must support ECE/Brier measurement, failure-mode classification, and on-device-first deployment. Three confirmed swaps and one strong consideration.

---

## Vision-Language Models

### Current state (perceptiond): LFM2.5-VL-450M

- 209MB Q4_0 + 180MB mmproj F16 = 389MB total
- llama-mtmd-cli subprocess driver
- ~10–15s/frame on x86_64 CPU
- Watchful mode (5fps, salience-gated) keeps queue at 0–1
- Liquid AI, Apr 11 2026

**Verdict:** ✅ keep for v1 desktop prototype. Solid choice, well-supported, all-GGUF. ✓

### v2 candidates (eval this quarter)

| Model | Params | Quant size | Inference | Quality | License | Notes |
|---|---|---|---|---|---|---|
| **LFM2.5-VL-450M** (current) | 450M | 389MB | 10-15s/frame | Solid | Research/commercial | On-device, GGUF+ONNX |
| **OmniVLM-968M** | 968M | ~580MB Q4_K_M | ~1.1s/frame (9× token compression) | Good | Open | **Highest-ROI v2 swap** |
| **Gemma 3 4B** | 4B | ~2.5GB Q4_K_M | ~3s/frame (GPU) | Best in class | Open | On-orbit proven (Apr 2026), NPU-friendly |
| **HRM-Text-1B** | 1B | ~650MB | <500ms (text only) | 84.5% GSM8K, 60.7% MMLU | Open (Sapient, $1,500 training) | **Reasoner, not VLM — but viable paired with OmniVLM-968M** |
| **SmolVLM-256M-Instruct** | 256M | ~302MB | ~26s/frame | Limited | Apache 2.0 | Edge-class, only for highly-constrained paths |
| **LFM2.5-8B-A1B MoE** | 8B (1B active) | ~1GB | Variable | Best open-weight | Open | q4f16 added Jun 2026; eval Q4 |
| **Qwen2.5-Omni-3B** | 3B | ~1.8GB | TBD | True omni-modal | Apache 2.0 | Audio + vision + text in one model |

### v6 recommendation

**Default v2 wearable = OmniVLM-968M (vision encoder) + HRM-Text-1B (reasoner, paired via shared context-encoder).**

Rationale:
- OmniVLM-968M's 9× token compression is the single biggest inference win available in 2026. Sub-2s/frame on CPU is the wearable budget.
- HRM-Text-1B is the most credible sub-1B reasoner published in 2026 (Sapient, May 18 2026, fully open-sourced, $1,500 training, 84.5% GSM8K, 60.7% MMLU, 56.2% MATH). Pairs with OmniVLM-968M via shared projector.
- Eval Gemma 3 4B as the high-end fallback if OmniVLM-968M falls short on quality.

**v6 adds: V5e-0 self-speculative decoding (1.89× speedup, training-free, OpenReview 2026) on top of any VLM choice.** Apply to whichever model wins the eval.

**v6 adds: CondenseVLM (submodular coverage + spatially-constrained merge, OpenReview 2026) and QViD (query-vision decomposition, OpenReview 2026) as training-free token condensation layers.** Halves encoder time on salience-gated frames.

### Indian-accent English and multilingual

SmolVLM-256M-Instruct multilingual vs Gemma 3 nano for Hindi. **Eval criterion:** OOD WER on CommonVoice Indian-accent English (same metric audiod uses for calibration eval). If audiod RL agent surfaces a regression on Indian-accent English, the VLM may need a domain-fine-tune.

---

## Speech-to-Text

### Current state (audiod): whisper.cpp base.en

- 74MB model
- Mature, 123 tests, all-GGUF
- `whisper-cpp-plus-rs` Rust binding (async, Tokio, Silero VAD, real-time streaming)
- GPU: Vulkan, Metal, CUDA, ROCm

**Verdict:** ✅ keep. Reliable, well-supported. The audiod calibration RL agent's eval baseline IS base.en. We measure ECE relative to base.en.

### v2 candidates

| Model | Size | Speed | Quality | License | Notes |
|---|---|---|---|---|---|
| **whisper.cpp base.en** (current) | 74MB | Real-time CPU | Solid English | MIT | **Eval baseline** |
| **Moonshine** (Useful Sensors) | ~60MB | 5× faster than Whisper | Comparable English | MIT/Apache | Edge-first, less mature ecosystem |
| **Parakeet** (NVIDIA) | ~150MB | TBD | SOTA accuracy at small sizes | CC-BY-4.0 | Multilingual, larger |
| **whisper-large-v3-turbo** | ~800MB | 2× slower | Best multilingual | MIT | Hindi-friendly, too large for v1 |
| **SeamlessM4T-v2** | ~1.5GB | N/A | Best multilingual | Research | Too large for v1 |

### v6 recommendation

**Keep whisper.cpp base.en for v1 (123 tests, deployed).** Evaluate Moonshine for v1.5 IF the audiod RL agent learns that base.en is the bottleneck on Indian-accent English (CommonVoice OOD eval will surface this). Do not switch without a public ECE/Brier measurement.

---

## Text-to-Speech

### Current state (ttsd): KittenTTS

- 6/6 tests, KittenTTS medium `expr-voice-2-m`
- Cold-path latency ~3.8s
- License: needs verification (this is the actual blocker)

**Verdict:** ⚠️ **swap to Kokoro-82M this quarter.** License + quality + size + ecosystem all favor Kokoro.

### v2 candidate: Kokoro-82M

- 82M params, 327MB on disk
- Apache 2.0 license (commercial OK, modifiable, embeddable)
- MOS 4.45 (highest in size class per Trelis benchmark)
- 24kHz natural-sounding audio
- 21 built-in voices across multiple languages
- 96× real-time on GPU, 210× on optimized setups
- Runs on CPU (Raspberry Pi viable)
- Sub-20ms TTFA on warm cache
- ONNX + native PyTorch paths
- WebGPU in-browser path proven (WebNarrator 1.1.0)

**v6 confirmation of v5 recommendation:** swap ttsd to Kokoro-82M by Jul 15, 2026. 1-week build.

### Other TTS options

| Model | Size | License | Quality | Notes |
|---|---|---|---|---|
| **Kokoro-82M** (recommended) | 327MB | Apache 2.0 | MOS 4.45 | Best fit for Dan Glasses |
| **Piper** | ~60MB per voice | MIT | Good | Speed king for low-resource languages |
| **Chatterbox** (Resemble) | ~500MB | Resemble license | Beats ElevenLabs blind tests | Voice cloning |
| **Fish Audio S2 Pro** | Cloud | Research-only | Commercial-grade | Requires separate license |
| **Qwen3-TTS** | ~1.5GB | Apache 2.0 | Most capable all-rounder (10 languages, voice cloning) | Too large for v1 |
| **MisoTTS** | ~400MB | Apache 2.0 | Sub-300ms TTFB, int8 quant | A6000-class hardware |
| **Inflect-Nano-v1** | 4.6M params | Open | MOS 3.48 | Fastest but lower quality |

### v6 ttsd v2 plan

1. **Replace KittenTTS with Kokoro-82M (1 week).**
2. **Multi-engine router:** Kokoro for English, Piper for non-English, MisoTTS for batch.
3. **WebGPU in-browser option** for v1.5 Tauri webview (WebNarrator 1.1.0 pattern).
4. **Add `/reliability` endpoint** — TTS intelligibility confidence (MOS proxy), cold-vs-warm latency, voice-consistency check.

---

## Reasoning Models (NEW v6 section)

For on-device agent reasoning, perceptiond → memoryd → proactived flow, we need a sub-1.5B reasoner that runs on NPU. v6 introduces this as an explicit category.

### Candidates

| Model | Params | Cost | Performance | License | Notes |
|---|---|---|---|---|---|
| **HRM-Text-1B** (Sapient) | 1B | $1,500 train (96-432× cheaper than peers) | 84.5% GSM8K, 60.7% MMLU, 56.2% MATH, 82.2% DROP, 81.9% ARC-C | Open (fully on GitHub + HF) | **Best v6 reasoner** |
| **LFM2.5-1.2B-Thinking** | 1.2B | Liquid AI commercial | Reasoning-tuned | Research/commercial | Baseline |
| **Qwen 3.5 2B** | 2B | Alibaba open | Competitive 2B | Apache 2.0 | Multimodal-ready |
| **Gemma 3 nano** (rumored) | TBD | DeepMind | TBD | Open | Eval when released |

### v6 recommendation

**HRM-Text-1B for v2 reasoning, paired with OmniVLM-968M vision encoder.** Sapient's $1,500 training cost basis suggests Danlab can fine-tune a domain-specific reasoner (e.g., on the Danlab task suite) for comparable cost. Open weights + open code + reproducible results = the v6 audiod RL agent's reasoner.

---

## Reward Models (NEW v6 section)

The audiod RL agent needs a reward model. Options:

1. **Heuristic reward (Brier score on (whisper.cpp prediction, WER-derived ground-truth)).** v6 primary. Free ground-truth (Librispeech, CommonVoice, TED-LIUM), well-defined reward, bounded failure mode.
2. **Learned reward model (1B) trained on `(image, prompt, response, human-preference)`.** v6 secondary. 4–6 weeks human labeling + 1 week training. RLAIF / RLHF.
3. **SIA-style reward (Hexo Labs MIT May 2026).** Harness+weights substrate. v6 tertiary.

### v6 recommendation

**Start with heuristic reward (Brier score).** Submit to AIE-Bench + SEAGym. Iterate to learned reward if v1 results are encouraging. SIA is the long-term substrate.

---

## Wake-word Models (NEW v6 section)

For the wearable, "Hey Dan" on-device wake word is needed (per Dan1 v82 GAP_ANALYSIS.md).

### Candidates

- **Picovoice Porcupine** — commercial, custom wake-word trained.
- **Snowboy / Pocketsphinx** — open-source, deprecated.
- **OpenWakeWord** (dscripka) — open-source, custom wake-word training.
- **NDP200 on-chip** — if Redax hardware ships with built-in wake-word DSP.

### v6 recommendation

**NDP200 on-chip if available.** OpenWakeWord as fallback. Porcupine only if custom brand wake-word is a marketing must-have.

---

## Embedding Models (memoryd)

### Current state: sentence-transformers/all-MiniLM-L6-v2

- 384-dim, ~80MB
- 16/16 tests, semantic recall working

**Verdict:** ✅ keep for v1. memoryd v2 will add int8 quantization (4× memory win) and switch to all-mpnet-base-v2 (768-dim) IF the AEL bandit surfaces it as a bottleneck.

---

## Summary of model swaps (v6 decisions)

| Service | v1 (current) | v2 (recommended) | Decision by | Deploy by |
|---|---|---|---|---|
| perceptiond VLM | LFM2.5-VL-450M Q4_0 | OmniVLM-968M Q4_K_M + V5e-0 speculative decoding | Aug 1, 2026 | Oct 1, 2026 |
| perceptiond token layer | None | CondenseVLM + QViD | Sep 1, 2026 | Oct 15, 2026 |
| memoryd embedding | MiniLM-L6-v2 | MiniLM-L6-v2 int8 + mpnet-base-v2 opt-in | memoryd v2 week 1 | memoryd v2 Sep 15 |
| audiod STT | whisper.cpp base.en | base.en + RL calibration head | — (current) | Aug 15 arXiv |
| audiod STT v1.5 | base.en | base.en or Moonshine (eval-driven) | Q1 2027 | Q1 2027 |
| ttsd TTS | KittenTTS medium | Kokoro-82M (Apache 2.0) | Jul 8, 2026 | Jul 15, 2026 |
| reasoner | None | HRM-Text-1B (Sapient, $1,500) | Q1 2027 | Q2 2027 |
| wake-word | None | NDP200 on-chip or OpenWakeWord | TBD | Q1 2027 |

---

## v5 → v6 changes

1. **HRM-Text-1B added as v6 reasoner.** Sapient, May 18 2026, 84.5% GSM8K (corrected), $1,500 training, fully open. Pairs with OmniVLM-968M for the v2 wearable.
2. **V5e-0 self-speculative decoding added (1.89× speedup, OpenReview 2026).**
3. **CondenseVLM + QViD token condensation layers added (training-free, OpenReview 2026).**
4. **Reward models as an explicit category (NEW v6).** Brier-score heuristic primary, learned reward secondary, SIA tertiary.
5. **Wake-word models as an explicit category (NEW v6).** NDP200 preferred, OpenWakeWord fallback.
6. **Kokoro-82M MOS 4.45 confirmed (Trelis benchmark).** Apache 2.0 license, 327MB, Raspberry Pi + WebGPU in-browser + ONNX + PyTorch.
7. **Indian-accent English / Hindi eval criteria added.** CommonVoice OOD eval drives STT and VLM swaps.

— Dan2, 2026-06-24 11:30 IST

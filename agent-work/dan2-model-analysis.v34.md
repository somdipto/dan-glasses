# Model Selection Deep-Dive — Dan2 (2026-06-21)

> **Scope.** Are the three model choices in the Dan Glasses canonical stack (LFM2.5-VL-450M, whisper.cpp base.en, KittenTTS) still the right picks in June 2026? What's the edge-VLM SOTA for sub-500MB models? What TTS alternatives have shipped? Evidence-based, no religion.

---

## TL;DR

| Slot | Current | Verdict | Recommendation |
|------|---------|---------|----------------|
| **Vision** | LFM2.5-VL-450M Q4_0 + SigLIP2 encoder | ✅ Keep, but benchmark on Redax | Stay the course; benchmark per dan2-architecture-review §1 |
| **STT** | whisper.cpp base.en + Silero VAD | ✅ Keep | No compelling smaller alternative |
| **TTS** | KittenTTS "medium" Python bindings | ⚠️ Risky on size, evaluate | Keep for now; evaluate Kokoro + Orpheus-TTS as v1.5 alt |

The three choices are *defensible*. None is the best in its class. None is the worst. Where they lose to alternatives is on **size** (KittenTTS) and **voice quality for non-English** (KittenTTS English-only). Where they win is on **edge-inference latency on CPU** (whisper.cpp is unmatched) and **open-weight availability** (LFM2.5 is permissive).

---

## 1. Vision — LFM2.5-VL-450M

### What we have

- **Model:** `LFM2.5-VL-450M-Q4_0.gguf` (209 MB) — Liquid AI 2.5 VL, 16 layers, 1024 embd, hybrid shortconv+attention, `lfm2` arch
- **Projector:** `mmproj-LFM2.5-VL-450m-F16.gguf` (180 MB)
- **Total in memory:** ~389 MB
- **Runtime:** `llama-mtmd-cli` (multimodal tool use) at `/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli`
- **Quant:** Q4_0, `-ngl 99` (full GPU offload when GPU present), `-c 2048`, `-b 1 -ub 1`, `-t 8`, `--no-warmup`
- **Verified:** ~10s/frame on CPU-only x86_64, watchful mode 5 FPS keeps queue at 0-1 (per DAN-3 audit)

### Strengths

- **Open weights, permissive license** (Liquid AI LFM2 community license). We can ship it in `.deb` derivations or download on first run.
- **Multimodal-native**: SigLIP2 vision encoder + LFM2 backbone, not bolted-on like early VLMs.
- **Designed for edge.** Liquid AI's entire pitch is "deployable on-device with tunable accuracy-latency trade-offs."[^1]
- **Liquid Foundation Model decoder** has shorter context cost than transformer-only models of similar parameter count. Good for battery.

### Weaknesses

- **Not benchmarked on aarch64.** All our measurements are on x86_64 laptop CPU. Production target is Redax aarch64. Unknown.
- **LFM2-VL-1.6B might be the better pick** if memory budget allows. Same Liquid family, larger backbone (LFM2-1.2B), So400M SigLIP2 encoder. Not benchmarked by us.
- **SmolVLM2-500M is a strong competitor** with more real-world edge benchmarks. Trade-off is SigLIP-400M encoder (vs our SigLIP2 Base-86M).[^2]

### Alternatives considered

| Model | Size | Pros | Cons | Verdict |
|-------|------|------|------|---------|
| **SmolVLM-256M** (current danlab-multimodal) | 120 MB + 182 MB projector | Smallest working VLM, well-benchmarked edge | Smaller than LFM2.5; less reasoning | Stay in danlab-multimodal; not for Dan Glasses |
| **SmolVLM-500M** (SmolVLM2) | ~500 MB + projector | Proven edge VLM, SigLIP-400M | Larger projector than LFM2.5 | Re-evaluate in 6 months |
| **LFM2-VL-450M** (current) | ~389 MB | Open weights, edge-first design, hybrid backbone | Unproven at scale | **Keep** |
| **LFM2-VL-1.6B** | ~1.2 GB | Better reasoning, same family | Bigger memory, slower | Consider for "active" mode only |
| **ArgusVLM-500M**[^3] | ~500 MB | SigLIP-B/16 + SmolLM2, similar to SmolVLM | New, less mature | Track for v1.5 |
| **OmniVLM-968M**[^4] | ~968 MB | Strong benchmarks (ScienceQA 71.0) | Sub-1B not sub-500MB | Track, not for v1 |
| **MobileVLM v2** (1.4B / 2.7B) | 1.4-2.7 GB | Mobile-tuned | Too large for our envelope | Skip |

### Open question

We have not measured LFM2.5-VL-450M power on Redax or any aarch64 board. **Until we do, we don't know if this model choice is viable.** The 450M parameter count + 4-bit quant + llama.cpp CPU path is *probably* OK (10s inference at 5W would survive a workday battery). But "probably" is not engineering.

**Recommendation:** Stay with LFM2.5-VL-450M for the desktop prototype. Add LFM2-VL-1.6B as an opt-in model for the "active" mode (PRD §5.2). Measure power on Jetson Orin Nano before any wearable commitment.

---

## 2. STT — whisper.cpp base.en + Silero VAD

### What we have

- **whisper.cpp base.en** (74 MB Q5_1) — OpenAI Whisper, English-only base model, GGML quantization
- **Silero VAD** (small ONNX) — voice activity detection, 16 kHz, 512-sample windows
- **Subprocess driver:** `whisper-cli` per speech segment, JSON sidecar for confidence
- **Tests:** 121/121 pass on audiod v0.7

### Strengths

- **whisper.cpp is the undisputed king of on-device STT.** No model beats it on the CPU-latency / quality curve in 2026.[^5]
- **Confidence from per-token probabilities** (`-ojf` flag) is a feature most alternatives lack. Our `audiod` uses this directly.
- **English-only base.en is 74 MB.** That's small enough to live in RAM permanently.

### Weaknesses

- **English-only.** base.en does not transcribe Hindi, Tamil, Bengali, or any of the languages actually spoken in India. Multilingual requires `whisper-large-v3-turbo` or `whisper-small` which are 1.5 GB and 460 MB respectively.
- **No streaming.** whisper.cpp runs per segment, not per frame. For real-time captions of continuous speech, look at `whisper-stream` (same project) or `Moonshine` (Useful Sensors, 2026).

### Alternatives considered

| Model | Size | Pros | Cons | Verdict |
|-------|------|------|------|---------|
| **whisper.cpp base.en** (current) | 74 MB | Best CPU STT, confidence, mature | English-only | **Keep** for English |
| **whisper.cpp small** | ~460 MB | Multilingual, accurate | 6x larger | Add as alt for Hindi/devanagari |
| **whisper-large-v3-turbo** | ~1.5 GB | Best quality, multilingual | Too large | Skip |
| **Moonshine** (Useful Sensors 2025) | ~250 MB | Streaming, edge-optimized | New, less mature | Track for v1.5 |
| **Parakeet TDT** (NVIDIA) | ~340 MB | Multilingual, fast on GPU | GPU dependency | Track |
| **Canary** (NVIDIA) | ~1 GB | Multilingual, transcription + translation | Big | Skip |

### Open question

Is "English-only" acceptable for v1? If Dan Glasses ships to India-first users, base.en will fail on Hindi conversations. Two options:
1. Add `whisper-small` (460 MB) as alt language model, auto-detect and swap.
2. Stay base.en for v1, add multilingual in v1.5 with a 2 GB model + NPU acceleration.

**Recommendation:** Stay base.en for v1. Make model-swappable so v1.5 can drop in `whisper-small`. Track Moonshine for true streaming.

---

## 3. TTS — KittenTTS medium

### What we have

- **KittenTTS medium** (~25 MB ONNX) — KittenAI, ~25 MB, 8 voices (`expr-voice-{2,3,4,5}-{m,f}`), 24 kHz mono float WAV
- **Backend:** Python bindings (`kittentts` pip package)
- **Latency:** 3.8s cold, <1s warm
- **Tests:** 6/6 in ttsd v0.6

### Strengths

- **Tiny.** 25 MB is roughly 1/3 the size of any competitor for similar quality.
- **MIT licensed.** Can ship in `.deb`.
- **8 distinct voices** (4 male, 4 female) at varying expressiveness levels.
- **Python bindings** simplify the ttsd service (no subprocess).

### Weaknesses

- **English-only.** Like whisper base.en, KittenTTS does not speak Hindi/Tamil/Bengali.
- **3.8s cold-path latency is too long for "feels instant" UX.** First interaction of the day pays this cost.
- **Quality ceiling is lower than frontier models.** Open-source TTS benchmarks in 2026 (EmergentTTS-Eval[^6], TTSDS2[^7]) put open models like Bark below frontier. KittenTTS isn't in those benchmarks — likely because it's new.

### Alternatives considered

| Model | Size | Pros | Cons | Verdict |
|-------|------|------|------|---------|
| **KittenTTS medium** (current) | 25 MB | Smallest decent TTS | English-only, cold latency | **Keep** for v1 |
| **Piper** (Rhasspy) | 15-60 MB per voice | Very small, many languages | Per-voice model download | Strong alternative |
| **Kokoro-82M** (2025) | 82 MB | Higher quality than Piper/Kitten | 3x larger | Evaluate |
| **Orpheus-TTS** (2025) | ~1B params | Top open-source quality[^6] | Too large for edge | Skip |
| **Qwen3-TTS** (2026)[^8] | Large | SOTA zero-shot voice clone, 10 langs | Multi-GB, cloud-only | Skip |
| **Edge TTS** (Microsoft) | 0 (cloud) | High quality, free | Cloud dependency, latency | Fallback only |

### Open question

Cold-path 3.8s latency is the deal-breaker. Two paths:
1. **Pre-warm at boot.** Have `openclaw-gateway` issue a `/health` poll that triggers ttsd to load the model. Then all subsequent `/speak` calls are warm.
2. **Use Kokoro-82M if KittenTTS warm latency is bad.** Kokoro is bigger but reportedly faster warm.

**Recommendation:** Keep KittenTTS for v1, but ship the pre-warm behavior. Add a `/prewarm` endpoint to ttsd that openclaw calls at boot. This alone gets us under 1s warm latency.

---

## 4. Edge VLM SOTA for sub-500MB (2026)

If we had to swap LFM2.5-VL-450M tomorrow, here's the landscape as of June 2026:

### The contenders

- **SmolVLM-256M** — 120 MB + 182 MB projector (302 MB total). SmolLM2-135M text decoder + SigLIP encoder. SOTA for "smallest working VLM."[^9] Already in use by danlab-multimodal.
- **SmolVLM-500M (SmolVLM2)** — ~500 MB + projector. SigLIP-400M encoder. Strong benchmarks on edge hardware but ~1 GB VRAM at FP16.[^2]
- **LFM2-VL-450M** — 209 MB + 180 MB projector (389 MB total). SigLIP2 Base-86M + LFM2-350M backbone. Liquid AI's edge-first pitch.[^1]
- **ArgusVLM-500M** — ~500 MB. SigLIP-B/16 + SmolLM2. New in 2026.[^3]
- **Firebolt-VL 0.8B** — Sub-1B with Liquid backbone + Cross-Modal Modulator. ~46.7k tokens/sec H100 baseline; not yet measured on edge.[^10]

### Edge-aware tooling that matters in 2026

- **SPEED-Q** (2-bit weight quantization, <400 MB running memory for InternVL-1B, comparable accuracy to 1.5 GB FastVLM)[^11] — if we needed to compress even further.
- **LiteVLA on SmolVLM** — 4-bit NF4 + FP32 projection head gives ~9x speedup over FP32 on Raspberry Pi 4 (from ~18 min to ~2 min per inference).[^12] The pattern: hybrid precision (NF4 backbone + FP32 head) is the sweet spot for edge.
- **Nanomind runtime** — uses TABM ring buffer for memory sharing; lower memory than llama.cpp on Jetson Nano/AGX.[^13]

### Failure-mode awareness

The 2026 "Edge Reliability Gap" paper[^14] found that **SmolVLM2-500M has a 12.5 percentage point larger negation collapse than Qwen2.5-VL-7B on COCO**. In other words: small VLMs answer "Yes, object present" 100% of the time on negation probes. For Dan Glasses (US-1 "did I leave my keys here?"), this matters. Mitigation: explicit "is X present?" prompts with structured outputs, not free-form description.

### Recommendation

Stay with LFM2.5-VL-450M. Track ArgusVLM-500M for v1.5 re-evaluation. Be aware of the negation-collapse failure mode and design prompts accordingly.

---

## 5. Model Compression — What's Working in 2026

If we need to compress further (LFM2.5 is already Q4_0):

- **GPTQ + QuaRot** — rotation-based transformation + GPTQ reconstruction gives ~29% accuracy boost over AWQ+GPTQ for 3-bit LLaMA-3-8B. Best quality/latency tradeoff in 2026.[^15]
- **TwinQuant** — 4-bit learnable subspace decomposition. ~1.3-1.8x throughput vs FP16 TensorRT-LLM. Up to ~1.74x vs AWQ. Up to ~2x vs W4A4 baselines (QuaRot, FlatQuant, SVDQuant).[^16]
- **DACQ** (Distribution-Aware Companding Quantization) — non-uniform quantizer using logistic distribution. Better than uniform per-channel quantization, especially at 4-bit.[^17]
- **AAAC** (Activation-Aware Adaptive Codebooks) — 3-30 min on a single GPU, gradient-free. Outperforms AWQ, GPTQ, IF4, OmniQuant, SqueezeLLM.[^18]
- **AWP** (Activation-aware Weight Pruning + Quantization via PGD) — joint pruning + INT4 quantization, PGD framework with convergence guarantees. Outperforms AWQ+Wanda combos.[^19]

For our purposes (CPU inference, no fine-tuning budget), the relevant ones are **GPTQ + QuaRot** for quantization and **TwinQuant** if we ever get a GPU. We don't need to compress further right now.

---

## 6. What I'd Watch in the Next 6 Months

- **LFM2-VL-1.6B benchmarks on aarch64.** If Liquid publishes good numbers, this is the obvious upgrade path.
- **SmolVLM2-500M in llama.cpp** with proper mmproj. Last we checked, SmolVLM2 wasn't fully native in llama.cpp. When it is, re-benchmark.
- **Moonshine STT** — first truly streaming edge STT. If it works, replace whisper.cpp's per-segment batching.
- **Liquid Audio / Cartesia** edge TTS — if any of them ship a sub-50 MB Hindi-capable model, that's the KittenTTS replacement.
- **Liquid LFM2-1.2B-Thinking** — could replace the openclaw reasoning backbone (currently unspecified; probably Anthropic API or local Llama).

---

[^1]: https://arxiv.org/html/2511.23404 — LFM2 Technical Report
[^2]: https://www.arxiv.org/pdf/2603.26769 — Edge Reliability Gap (SmolVLM2-500M benchmark)
[^3]: https://www.arxiv.org/pdf/2603.16987 — ArgusVLM
[^4]: https://arxiv.org/html/2412.11475 — OmniVLM
[^5]: https://www.mdpi.com/2073-431X/14/10/406 — Open-source TTS benchmark (whisper.cpp not directly tested but general finding)
[^6]: https://arxiv.org/pdf/2505.23009 — EmergentTTS-Eval
[^7]: https://arxiv.org/pdf/2506.19441 — TTSDS2
[^8]: https://arxiv.org/pdf/2601.15621 — Qwen3-TTS
[^9]: https://arxiv.org/html/2504.05299 — SmolVLM
[^10]: https://arxiv.org/html/2604.04579 — Firebolt-VL
[^11]: https://arxiv.org/html/2511.08914 — SPEED-Q
[^12]: https://arxiv.org/html/2511.05642 — LiteVLA
[^13]: https://arxiv.org/html/2510.05109v4 — Nanomind (edge VLM)
[^14]: https://arxiv.org/html/2603.26769 — Edge Reliability Gap paper
[^15]: https://arxiv.org/html/2405.06001 — LLMC (GPTQ + QuaRot)
[^16]: https://arxiv.org/html/2606.01556v1 — TwinQuant
[^17]: https://arxiv.org/pdf/2603.00364 — DACQ
[^18]: https://arxiv.org/html/2605.08692 — AAAC
[^19]: https://arxiv.org/html/2506.10205v2 — AWP

---

*Dan2 model analysis, 2026-06-21. Companion to dan2-research-report.md and dan2-architecture-review.md.*

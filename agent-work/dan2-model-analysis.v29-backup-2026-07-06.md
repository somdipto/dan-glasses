# Dan-2 Model Analysis — v29 (2026-07-06)

> **Status:** v29 refresh. v28 content preserved. v29 deltas prepended.
> **Scope:** LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM-L6-v2, LFM2.5-230M, nomic-embed-text — are they still the right choices? What alternatives exist?
> **Verdict:** v23-v28 choices **all hold**. v29 adds 1 NEW model candidate (MatchaTTS), 1 NEW ship-gate evaluation requirement (LFM2.5-VL-450M negation-collapse probe), and corrects the v28 v1.5 TTS plan-A.

---

## v29 Deltas (this refresh — 2026-07-06)

### 1. NEW MODEL CANDIDATE — MatchaTTS + vocos (v1.5 TTS, displaces Kokoro-82M)

The tts-bench project (5uck1ess/tts-bench, June 2026) provides the first reproducible on-device TTS comparison. Concrete RTF numbers (RTF = real-time factor, <1 is faster than realtime):
- **MatchaTTS float32 + vocos: RTF 0.163, 71MB acoustic + 52MB vocoder = 123MB total.** Fastest, smallest.
- **KittenTTS-Nano float16: RTF 0.693, 23MB.** Second-fastest, smallest single model.
- **Piper float32: RTF 0.276, 75MB.** (Fastest at typical TTS quality.)
- **Kokoro float32: RTF 1.880, 330MB.** (Slow, big.)
- **Kokoro int8: RTF 3.564, 128MB.** (Quantization hurts Kokoro.)

22 voices in MatchaTTS. Apache 2.0.

**v29 verdict:** MatchaTTS + vocos is the **v1.5 plan-A for TTS**, displacing Kokoro-82M. The reasoning: 12× faster than Kokoro, 2.7× smaller, and the 22-voice library is comparable. Kokoro-82M remains the v1.5 plan-B for high-quality-when-speed-doesn't-matter scenarios. KittenTTS-Nano is the v1.0 choice (mature, on-device, 8 voices, ~25MB, Python API, already wired up).

### 2. NEW SHIP-GATE EVALUATION REQUIREMENT — LFM2.5-VL-450M negation-collapse probe

arXiv 2603.26769 (2026): SmolVLM2-500M answers "Yes" to 100% of COCO negation trials; Qwen2.5-VL-7B 4-bit answers incorrectly only 14% of the time. **We have no published negation-collapse benchmark for LFM2.5-VL-450M.** SmolVLM2-500M and LFM2.5-VL-450M are roughly the same size class; the risk is real.

**v29 verdict:** v1.0 ship-gate must include a 200-image COCO-style negation probe (scaled-down FINER-CompreCap or Ghost-100 5-Level Prompt Intensity Framework) for LFM2.5-VL-450M. If LFM2.5-VL-450M exhibits >50% negation collapse, fall back to LFM2.5-VL-1.6B (the 1.6B variant, not the 450M). Add to v28 plan-E1 (NEW v29).

### 3. CONFIRMED — LFM2.5-VL-1.6B is the v1.5 fallback if LFM2.5-VL-450M fails the negation gate

Multiple 2026 sources confirm LFM2.5-VL-1.6B is edge-deployable with vLLM, Optimum-Intel OpenVINO, LEAP Edge SDK for Android/iOS, and Rust ONNX inference. The 1.6B variant has a 400M vision encoder (vs 86M for the 450M). Inference on aarch64 is 2-3× slower than the 450M but still edge-viable on Snapdragon AR1 Gen 2 / Apple M-series.

**v29 verdict:** v1.5 plan-A remains LFM2.5-VL-1.2B-Thinking. **v1.5 plan-B is now LFM2.5-VL-1.6B if the v29 negation-collapse gate fails for the 450M.** v29 has promoted LFM2.5-VL-1.6B from honorable mention to v1.5 plan-B.

### 4. CONFIRMED — Hermes Agent openclaw v1.0 plan-A: now with channel-fracture verification (arXiv 2606.04896)

v28 promoted Hermes Agent to v1.0 openclaw plan-A. v29 confirms but adds the channel-fracture verification requirement: scheduled cron-like agents cannot write to the target agent's persistent memory due to the `skip_memory=True` flag. The v29 Hermes Agent spike must include a "cron-delegated memory writes land in target agent" test.

### 5. CONFIRMED — SIA concrete numbers (arXiv 2605.27276v1, official)

The SIA paper's official published numbers (not the v28 Felix Chau recap approximations):
- LawBench: 56.6% improvement.
- GPU kernel optimization: 91.9% runtime reduction (12× faster).
- Single-cell RNA denoising: 502% improvement.

The 91.9% GPU kernel speedup maps to audiod segment timing histogram optimization as a v1.5 SIA-W+H port target (relevant to danlab-multimodal's screen-capture heuristic loop). v29 plan-P4 sharpen.

### 6. CONFIRMED — whisper.cpp base.en still v1.0 STT; Moonshine v1.5 plan-A

No new STT findings in v29 window. whisper.cpp base.en holds. Moonshine (Useful Sensors, 27M-122M params) remains v1.5 plan-A for CPU-only path.

---

## v29 v1.0 Model Decisions (final)

| Layer | v1.0 model | v1.5 candidate | Why |
|-------|------------|----------------|-----|
| STT (audiod) | whisper.cpp base.en | Moonshine 122M | base.en is 142MB, fast, accurate. Moonshine is a possible v1.5 upgrade. |
| Reasoning (post-processor) | LFM2.5-230M (v28) | HRM-Text-1B or Nemotron-4B-Q4 | LFM2.5-230M is the v28 best on-device reasoning model. |
| Vision (perceptiond) | LFM2.5-VL-450M **(subject to v29 plan-E1 negation gate)** | LFM2.5-1.2B-Thinking (plan-A) / LFM2.5-1.6B (plan-B if gate fails) | LFM2.5-VL-450M is the v28 SOTA sub-250MB VLM but lacks negation benchmark. |
| TTS (ttsd) | KittenTTS medium | **MatchaTTS + vocos (v29 NEW plan-A) / Kokoro-82M (plan-B)** | MatchaTTS is the v29 fastest + smallest on-device TTS (RTF 0.163, 123MB). |
| Embedding (memoryd) | MiniLM-L6-v2 (v1.0) / nomic-embed-text v1.5 (if on laptop) | — | Depends on deployment shape. AIMultiple + MemDelta evaluation required before swap. |
| Agent framework (openclaw) | **Hermes Agent (v28 plan-A, v29 adds channel-fracture verification)** | SIA-W+H (research bet) | Hermes Agent is the v28 1-2 week drop-in. |

## v29 v1.0 + v1.5 Plan Additions

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-E1 (NEW v29) | LFM2.5-VL-450M negation-collapse probe + SmolVLM2-500M head-to-head | 1 | Q3 W3, BEFORE v1.0 ships |
| plan-T1 (NEW v29) | MatchaTTS + vocos v1.5 TTS spike | 1 | Q3 W3 |
| plan-M1 (v28) | nomic-embed-text v1.5 vs MiniLM-L6-v2 MemDelta-controlled baseline | 1 | Q3 W3 |
| plan-M2 (v28) | LFM2.5-230M vs HRM-Text-1B vs Nemotron-4B-Q4 reasoning benchmark | 1 | Q3 W2 |

---

*Maintained by DAN-2. v29 is a model-delta on v28. All v23-v28 model choices hold; v29 adds 1 new candidate (MatchaTTS) and 1 new ship-gate evaluation requirement (LFM2.5-VL-450M negation probe).*
# Model Selection Deep-Dive — LFM2.5-VL-450M, whisper.cpp, KittenTTS

**Author:** Dan2
**Date:** 2026-06-26
**Status:** v93 — delta on v12 (Liquid AI retrievers Jun 18, NPU benchmarks, Kokoro Hindi voices)

---

## TL;DR (v93)

v12's verdicts stand. v93 updates:
- **memoryd encoder:** **all-MiniLM-L6-v2 → LFM2.5-Embedding-350M** (1024-dim, 22 Indic languages, Apache-2.0). **This is the single most important model change of Q3 2026.**
- **memoryd reranker:** add **LFM2.5-ColBERT-350M** in Q4 2026.
- **TTS:** v1 keeps KittenTTS; v1.5 candidate is **Kokoro-82M** for Hindi voices (India-origin wedge).
- **Reasoning/Feedback-Agent:** **LFM2.5-1.2B-Thinking** (1.2B, fits in 4GB RAM, CPU-friendly) is the credible local replacement for Claude Sonnet 4.6 in SIA-loop.
- **Wake word:** **openWakeWord** (~1MB, MIT) is the drop-in for v1.5.
- **NPU acceleration:** proven on AMD Ryzen AI Max+ 395 (67× more efficient than iGPU) and Qualcomm SA8295P (14× lower latency). **The "we don't have NPU" excuse is gone.**

---

## 1. Vision Model — LFM2.5-VL-450M (v93 reaffirms + NPU update)

### v93 verdict: still the right family, now with a credible NPU path

- **LFM2.5-VL-450M Q4_0** (current): 209 MB main + 180 MB mmproj = 389 MB on-device. **10–15s/frame on CPU-only x86_64; sub-250ms on NPU-accelerated edge** (per Liquid AI claim).
- **NPU benchmarks (v93 evidence):**
  - **AMD Ryzen AI Max+ 395 NPU:** 5.2× faster prefill vs iGPU, 33.5× faster vs CPU, **67× more power-efficient than iGPU** [^1]
  - **Qualcomm SA8295P NPU:** up to **14× lower end-to-end latency, 7× lower quantization error** [^2]
  - **SPEED-Q:** 2-bit InternVL-1B in <400 MB [^3]
  - **CHIME:** 41× faster than Jetson Orin NX, 185× more energy-efficient [^4]

**v93 implication:** **LFM2.5-VL-450M on NPU is the unlock for wearable viability.** Power draw in watchful mode goes from PRD-estimated 3–8W (CPU) to projected <2W (NPU). This collapses battery sizing from "4h target" to "8h+ target."

**Action:** Buy Qualcomm SA8295P dev kit or AMD Ryzen AI reference board. Re-measure LFM2.5-VL-450M watts-per-frame. Target: <2W watchful mode.

### Thermal-fallback (v93: SmolVLM2-256M, not Gemma)

v12 said "replace PRD's dead Gemma line with SmolVLM2-256M." **v93 confirms and benchmarks with LiteVLA** [^5]:
- SmolVLM2-256M FP32 on Raspberry Pi 4: ~11s/query (FP32)
- LiteVLA 4-bit NF4 hybrid: ~2 min/query (stable)
- LiteVLA NF4-only: ~1.5 min/query (unstable, projection head must stay FP32)

**v93 recommendation:** **SmolVLM2-256M as thermal-fallback, with FP32 projection head + 4-bit NF4 quant on the rest.** Already wired in `vlm.py`. Just benchmark on target hardware when we get the dev kit.

### Gemma 3n as v1.5 candidate (v93: still on the table)

v12 added Gemma 3n (E2B, 2GB RAM, multimodal) as v1.5 candidate. **v93: Gemma3 mapped onto AMD Ryzen AI edge dataflow is now published** [^1]. Concrete benchmarks. **Worth A/B-testing against LFM2.5-VL-450M for v1.5.**

### New v93 contender: LFM2.5-8B-A1B MoE (May 28, 2026)

Liquid AI shipped LFM2.5-8B-A1B (May 28, 2026) — edge MoE for fast tool calling. **Too big for wearable budget (8B > 2GB target).** But useful as the **cloud-fallback** if we ever decide to offer "remote reasoning" mode.

### Summary

| Model | Size | Status |
|---|---|---|
| **LFM2.5-VL-450M Q4_0** (current) | 389 MB | ✅ Keep. NPU path is the unlock. |
| **SmolVLM2-256M** | 302 MB | ✅ Thermal fallback (already wired) |
| **Gemma 3n E2B** | 2 GB effective | v1.5 candidate (benchmark) |
| **LFM2.5-VL-1.6B** | ~980 MB | v2 candidate (if we relax budget) |
| **LFM2.5-8B-A1B MoE** | ~8 GB | Cloud-fallback only |

---

## 2. STT — whisper.cpp base.en (v93: unchanged)

### v93 verdict: still right

v12 said "keep whisper.cpp base.en." v93 confirms. 74 MB, runs on any ARM core, GPU acceleration available (Vulkan/Metal/CUDA). The Moonshine alternative (v12 mention) is worth A/B-testing in Q4 2026 — but not blocking.

**Action:** Add `tiny.en` (39 MB) as thermal-fallback alongside VLM thermal-fallback.

### Wake word (v93: openWakeWord for v1.5)

PRD defers wake word to v1.5. **v93: openWakeWord is the drop-in.**
- MIT-licensed, ~1 MB model, CPU-only, ~10ms inference
- Custom wake-phrase training supported
- Pick "Hey Dan" or similar
- Add as parallel path to PTT (don't replace)

**Why now matters:** the "proactive AI" positioning is dishonest if user must press a button. Wake word completes the pull path; awarenessd is the push path.

---

## 3. TTS — KittenTTS → Kokoro-82M (v93: confirmed + Hindi wedge)

### v93 verdict: swap to Kokoro-82M in v1.5

v12 said "Kokoro-82M as v1.5 candidate." **v93: confirmed and sharpened.**

| TTS | Size | Languages | License | v93 verdict |
|---|---|---|---|---|
| **KittenTTS medium** (current) | ~25 MB | English only | MIT | ✅ v1 (don't churn) |
| **Kokoro-82M** | 82 MB | EN + FR + **2 HI** + IT | Apache-2.0 | **v1.5 — India-origin wedge** |
| **Qwen3-TTS** | varies | 10 languages + voice cloning | Apache-2.0 | v2 if multilingual is a real wedge |
| **CosyVoice 3** | large | 9 langs + 18 dialects | Apache-2.0 | Too big for glasses |
| **MLX-Audio / VoxCPM2 / MOSS-TTS-Nano** | varies | varies | varies | Apple-only or niche |

**Why Kokoro-82M is the v93 pick:**
- **Hindi voices** — direct India-origin wedge. Halo is English-only.
- **Apache-2.0** — no license restrictions for our commercialization.
- **82 MB** — acceptable for wearable budget.
- **Raspberry Pi-compatible** — proven on edge.
- **Quality** — beats KittenTTS in mid-2026 blind tests.

**Action:** ttsd v1.5 = Kokoro-82M. Ship Hindi + Bengali + Tamil in Q4 2026.

---

## 4. Reasoning / RSI Feedback-Agent — LFM2.5-1.2B-Thinking (v93: NEW critical)

### v93 verdict: this is the missing piece for true on-device RSI

v12 deferred this to a footnote. **v93 elevates to Action 1 of Q3 2026.**

The danlab-multimodal pipeline today scores outputs with a hand-coded heuristic. To graduate to **real RL** (weights update loop), we need a **Feedback-Agent**. v12 said "fork SIA, swap Claude Sonnet 4.6 → LFM2.5-1.2B-Thinking."

**LFM2.5-1.2B-Thinking** (Liquid AI, Jan 20, 2026):
- 1.2B parameters, fits in 4GB RAM
- CPU-friendly, designed for on-device reasoning
- Apache-2.0-equivalent license (LFM Open License v1.0)
- Specifically marketed as "On-Device Reasoning Under 1GB"

**Concrete plan (v93):**
1. Fork github.com/hexo-ai/sia (MIT)
2. Replace Feedback-Agent: Claude Sonnet 4.6 → LFM2.5-1.2B-Thinking
3. Replace Task-Specific Agent: any VLM → SmolVLM2-256M + LFM2.5-VL-450M ensemble
4. Wrap in SGM-style e-value gate [^6] for safety
5. Run 10 generations on danlab-multimodal screen-description benchmark
6. Publish results: "SIA-on-SmolVLM-256M, Feedback-Agent = 1.2B open-weight"

**This is the first credible open-weight SIA-loop result.** danlab-multimodal graduates from "pre-RL scaffold" to "weights-updated self-improving VLM."

---

## 5. Embedding Model — LFM2.5-Embedding-350M (v93: NEW, Action 1)

### v93 verdict: ship this in memoryd v2, Q3 2026

v12 hedged between bge-small-en-v1.5 and "research required." **v93: ship LFM2.5-Embedding-350M.**

| Model | Dim | Params | Indic languages | License | v93 verdict |
|---|---|---|---|---|---|
| **all-MiniLM-L6-v2** (current) | 384 | 22M | ❌ | Apache-2.0 | ✅ v1 keep as fallback |
| **LFM2.5-Embedding-350M** (Jun 18, 2026) | 1024 | 350M | **22 Indic** | Apache-2.0-equivalent | **memoryd v2 — Q3 2026** |
| **bge-m3** | 568 | 568M | multilingual | MIT | Alternative |
| **all-mpnet-base-v2** | 768 | 110M | EN-tilted | Apache-2.0 | v1.5 if LFM2.5 fails |

**Why LFM2.5-Embedding-350M wins:**
- **1024-dim** (vs 384) — 2.7× richer representation
- **22 Indic languages** — India-origin moat, ships Hindi/Bengali/Tamil/Telugu/Marathi out of the box
- **Apache-2.0-equivalent** — no licensing issues
- **Same Liquid AI stack** as our VLM and Reasoning — single-vendor alignment
- **350M params, edge-deployable** — fits the wearable budget

**Action:** memoryd v2 ships with this in Q3 2026. 2-week fork-and-ship.

---

## 6. Reranker — LFM2.5-ColBERT-350M (v93: NEW, Q4 2026)

### v93 verdict: add to memoryd v2.5 in Q4 2026

Same launch as the embedding model (Jun 18, 2026). Late-interaction reranker. Pairs with the embedding model for two-stage retrieval.

**Why:** Boosts recall precision by 5-15% on standard benchmarks. Cheap at inference time. **For awarenessd's proactive loop, the precision boost is load-bearing.**

---

## 7. What's NOT changing (v93 reaffirms)

- **Tauri v2 + .deb + systemd** — correct.
- **V4L2 camera + CrabCamera** — correct.
- **SQLite + vectors memory core** — correct.
- **TypeScript/Node for OpenClaw gateway** — correct (despite MS-Scout competition, ecosystem is too valuable to abandon).

---

## Model timeline (v93)

| Quarter | Model swap | Rationale |
|---|---|---|
| Q3 2026 (now) | memoryd: MiniLM-L6-v2 → **LFM2.5-Embedding-350M** | Indic languages, sovereignty |
| Q3 2026 | perceptiond: add **SmolVLM2-256M** thermal-fallback (already wired) | LiteVLA benchmarks confirm stability |
| Q3 2026 | audiod: add **tiny.en** thermal-fallback | Symmetric design |
| Q3 2026 | reasoning: add **LFM2.5-1.2B-Thinking** for SIA loop | Real RL on-device |
| Q4 2026 | ttsd: KittenTTS → **Kokoro-82M** | Hindi voices, India-origin wedge |
| Q4 2026 | audiod: add **openWakeWord** | Complete the proactive story |
| Q4 2026 | memoryd: add **LFM2.5-ColBERT-350M** reranker | Two-stage retrieval for awarenessd |
| Q1 2027 | Gemma 3n A/B vs LFM2.5-VL-450M | If NPU path doesn't ship |
| Q2 2027 | perceptiond: VLM upgrade path TBD | Based on Q4 2026 hardware measurements |

---

## Sources

[^1]: https://arxiv.org/abs/2602.06063 — Mapping Gemma3 onto Edge Dataflow Architecture (AMD Ryzen AI NPU, May 2026)
[^2]: https://arxiv.org/html/2512.02924v2 — AutoNeural: Co-Designing VLMs for NPU Inference (Qualcomm SA8295P)
[^3]: https://arxiv.org/html/2511.08914 — SPEED-Q: 2-bit VLM with staged distillation
[^4]: https://arxiv.org/html/2601.19908v1 — CHIME: Chiplet-based near-memory acceleration (41× vs Jetson Orin NX)
[^5]: https://export.arxiv.org/pdf/2511.05642 — LiteVLA on Raspberry Pi 4 (4-bit NF4 SmolVLM)
[^6]: https://arxiv.org/pdf/2510.10232 — SGM: Statistical Gödel Machine for Risk-Controlled Self-Modification (e-value gate)
[^7]: https://www.liquid.ai/blog/lfm2-5-retrievers — LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M (Jun 18, 2026)
[^8]: https://www.liquid.ai/blog/lfm2-5-1-2b-thinking-on-device-reasoning-under-1gb — LFM2.5-1.2B-Thinking (Jan 20, 2026)
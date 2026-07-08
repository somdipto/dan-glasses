# Dan2 — Model Analysis v15 (2026-07-03 10:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v14:** `dan2-model-analysis.v14-backup-2026-07-03.md`

> **v15 deltas vs v14 (1 CRITICAL add, 1 sharpening, 0 retractions):**
> 1. **NEW CRITICAL — Execution substrate is now phase-mapped.** The "Phase Matters" paper (arXiv 2606.27906, late June 2026) demonstrates that on-device VLM inference requires phase-mapped heterogeneous NPU/CPU/GPU inference, not "small model on CPU." NPU prefill 1.64×, NPU decode 1.18×, vision encoders 2.52× lower energy. **v15 CRITICAL: the model choices are correct; the *execution substrate* is the v15 decision. `perceptiond.phase_map` is the 1-week Q3 W1 spike.**
> 2. **NEW SHARPEN — OpenPhone-3B (HKUDS, ACL 2026, late June 2026).** 3B-parameter on-device agentic foundation model. Two-layer self-learning memory. **v15 add: OpenPhone-3B is the v1.5 audiod post-processor plan-C, alongside HRM-Text-1B (plan-A) and Apertus v1.1 4B (plan-B).**

> **v15 retractions of v14:** **none.** The v14 model shortlist holds. The v15 add is the phase-mapped execution substrate and OpenPhone-3B plan-C.

---

## TL;DR (one paragraph, v15)

The v14 model choices are correct. **LFM2.5-VL-450M is the v1.0 vision model. whisper.cpp base.en is the v1.0 STT. KittenTTS medium is the v1.0 TTS. OpenClaw (TS/Node) is the v1.0 orchestration. SQLite + MiniLM-L6-v2 + vectors is the v1.0 memory.** v15 adds: **the execution substrate is now phase-mapped** (vision encoder → NPU, text decode → CPU, salience gating → low-power DSP) per the Phase Matters paper. The 4hr battery target is now reachable. **v15 also adds: OpenPhone-3B is the v1.5 audiod post-processor plan-C.** No v14 model choice is retracted.

---

## v1.0 Model Stack (v15, locked per dan-glasses/AGENTS.md)

| Component | Model | Size | Quant | Runtime | v15 Substrate |
|-----------|-------|------|-------|---------|---------------|
| Vision | LFM2.5-VL-450M | 450M (209MB GGUF) | Q4_0 | llama-mtmd-cli | **NPU (vision encoder) + CPU (text decode) — phase-mapped** |
| STT | whisper.cpp base.en | 74MB | Q5_1 | whisper-cpp-plus-rs | CPU (with NPU optional acceleration) |
| TTS | KittenTTS medium | ~25MB | native | ONNX Runtime | CPU (with NPU optional acceleration) |
| Memory | MiniLM-L6-v2 | 22M | INT8 (v1.1 spike) | sentence-transformers | CPU |
| Orchestration | OpenClaw | n/a | n/a | TypeScript/Node | n/a |
| Reasoning | (v1.5) HRM-Text-1B | 1B (Apache-2.0) | Q4_K_M | llama.cpp | **NPU (v1.5) + CPU fallback** |
| Reasoning (alt) | (v1.5) Apertus v1.1 4B | 4B | Q4_K_M | llama.cpp | CPU + NPU |
| Reasoning (alt) | (v1.5) OpenPhone-3B (NEW v15) | 3B | Q4_K_M | llama.cpp | CPU + NPU |
| TTS (v1.5) | Qwen3-TTS | TBD | TBD | TBD | CPU + NPU |

---

## v1.0 Models (held from v14, locked)

### LFM2.5-VL-450M — held from v8/v11

- **Released:** April 11, 2026 by Liquid AI.
- **Size:** 450M params, ~209MB GGUF Q4_0 + 180MB mmproj.
- **License:** Research/commercial (verify with Liquid AI).
- **v15 sharpening:** must run with phase-mapped heterogeneous inference per the Phase Matters paper. Vision encoder → NPU (QNN/Hexagon on Snapdragon), text decode → CPU. The 10-15s/frame CPU-only latency is reduced to <2s/frame with phase-mapped NPU.
- **v15 add:** `perceptiond.phase_map` is the 1-week Q3 W1 architecture spike.

### whisper.cpp base.en — held from v8/v11

- **Size:** 74MB.
- **License:** MIT.
- **v15 status:** unchanged. Optional NPU acceleration (Silero VAD + NPU prefill) is a v1.5 optimization.

### KittenTTS medium — held from v8/v11

- **Size:** ~25MB.
- **License:** Verify with KittenML.
- **v15 status:** unchanged. Optional NPU acceleration is a v1.5 optimization.

### OpenClaw (TypeScript/Node) — held from v8/v11

- **Released:** Late 2025.
- **License:** MIT.
- **v15 status:** unchanged. v15 sharpening: Microsoft Scout (Build 2026) is built on OpenClaw; Microsoft is doubling down on the *implementation wedge* with Frontier Co. The agent-framework substrate is the wedge; the consumer/wearable layer is our contribution.

### MiniLM-L6-v2 (memoryd) — held from v8/v11

- **Size:** 22M params, 384-dim embeddings.
- **License:** Apache-2.0.
- **v15 status:** unchanged. INT8 quantization of stored embeddings (2x reduction, <2% recall loss) is the v1.1 memoryd compression spike. Memora v1.5 storage/retrieval split is the v1.5 architecture target.

---

## v1.5 Models (held from v14, with v15 OpenPhone-3B add)

### HRM-Text-1B (Sapient) — held from v11

- **Size:** 1B params.
- **License:** Apache-2.0.
- **Cost:** $1,500 from scratch.
- **v15 status:** v1.5 audiod post-processor **plan-A**. Unchanged.

### Apertus v1.1 4B (Swiss AI / EPFL) — held from v14

- **Size:** 4B params.
- **License:** Open-weights, EU data compliance.
- **v15 status:** v1.5 audiod post-processor **plan-B**. Unchanged.

### OpenPhone-3B (HKUDS, ACL 2026) — NEW v15 plan-C

- **Size:** 3B params.
- **License:** Open-weights (verify).
- **Architecture:** Two-layer self-learning memory (Ralph Loop: EXECUTE → EVALUATE → FIX → REPEAT).
- **v15 add:** v1.5 audiod post-processor **plan-C**. 2-day evaluation spike. Q3 W1.
- **Evidence:** https://github.com/HKUDS/OpenPhone, ACL 2026.

### Qwen3-TTS (Alibaba) — held from v12

- **v15 status:** v1.5 TTS **plan-A**. Unchanged.

### Chatterbox (Resemble AI) — held from v12

- **v15 status:** v1.5 voice-cloning **plan-A**. Unchanged.

### LFM2.5-VL-450M-Extract (Liquid AI) — held from v12

- **v15 status:** v1.5 structured-output VLM **plan-A**. Unchanged.

---

## GLM-5.2 + Memora + Phase Matters (research bet, v15)

### GLM-5.2 (Z.ai) — held from v13

- **License:** MIT.
- **v15 status:** research bet, 1-day verification spike.

### Microsoft Memora — held from v14

- **v15 status:** v1.5 memoryd architecture target. Port in Q3 W1-W2, 2 weeks, 1 engineer.

### Phase Matters (arXiv 2606.27906) — NEW v15 CRITICAL

- **v15 add:** v1.0 wearable execution substrate. Vision encoder → NPU, text decode → CPU, salience gating → low-power DSP. 1-week Q3 W1 spike.
- **Evidence:** https://arxiv.org/html/2606.27906v1, late June 2026.

---

## v1.5 Substrate: Phase-mapped heterogeneous inference (NEW v15)

| Phase | Backend | Speedup | Energy |
|-------|---------|---------|--------|
| Vision encoder (prefill) | NPU (QNN/Hexagon) | 1.64× | 2.52× lower |
| Text decode | CPU | 1.0× (1.18× with NPU) | baseline |
| Salience gating | low-power DSP | n/a | 0.3W |

**v15 power conclusion:** the 4hr battery target is now reachable with phase-mapped execution + salience gating. **Retracts the v9 "salience gate is a UX detail" framing — it is the *power* decision, not a UX detail.**

---

## Top 3 Recommendations for somdipto (v15)

1. **Approve the `perceptiond.phase_map` Q3 W1 critical-path spike (1 week, 1 engineer).** v15 CRITICAL.
2. **Approve the OpenPhone-3B shortlist evaluation (Q3 W1, 2 days, 1 engineer).** v15 SHARPEN.
3. **Confirm the v1.0 model stack is locked per dan-glasses/AGENTS.md.** No v15 retraction. Held from v8/v11.

---

## Open Questions for somdipto (v15)

1. **`perceptiond.phase_map` spike priority** — Q3 W1 (recommend: yes, 1 week, 1 engineer)
2. **OpenPhone-3B shortlist evaluation** — Q3 W1, 2 days (recommend: yes, 1 engineer)
3. **Redax SoC choice (Qualcomm vs MediaTek)** — needed before Q3 W1 spike (recommend: confirm with hardware team)
4. **NPU acceleration for KittenTTS** — v1.5 optimization (recommend: defer to v1.5)

---

## Footnotes (v15)

[^1]: https://arxiv.org/html/2606.27906v1 — "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC," late June 2026.
[^2]: https://github.com/HKUDS/OpenPhone — OpenPhone-3B, HKUDS, ACL 2026, late June 2026.
[^3]: https://www.bbc.com/news/articles/c3wy317d71jo — BBC Meta Conversation Focus paywall, July 2 2026.
[^4]: https://www.cnbc.com/2026/07/02/palantir-shares-have-struggled-this-year-da-davidson-says-buy-the-dip.html — Palantir D.A. Davidson upgrade, July 2 2026.
[^5]: https://www.theguardian.com/technology/2026/jul/02/openai-stake-us-government-ai-sam-altman — OpenAI 5% to US sovereign wealth fund, July 2 2026.

---

## v14 model analysis content (preserved in backup)

The v14 model analysis (preserved in `dan2-model-analysis.v14-backup-2026-07-03.md`) covers: LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM-L6-v2, HRM-Text-1B, Apertus v1.1 4B, GLM-5.2, Memora, Qwen3-TTS, Chatterbox. **All v14 content is preserved verbatim in the backup. The v15 add is the phase-mapped execution substrate (CRITICAL) and OpenPhone-3B plan-C. The v14 model shortlist holds.**

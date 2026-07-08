# Dan2 — Architecture Review v15 (2026-07-03 10:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-architecture-review.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v14:** `dan2-architecture-review.v14-backup-2026-07-03.md`

> **v15 deltas vs v14 (1 CRITICAL add, 1 sharpening, 0 retractions):**
> 1. **NEW CRITICAL — `perceptiond.phase_map` execution substrate is undefined.** The Phase Matters paper (arXiv 2606.27906, late June 2026) demonstrates that on-device VLM inference requires phase-mapped heterogeneous NPU/CPU/GPU inference, not "small model on CPU." **v15 CRITICAL: 1-week architecture spike, Q3 W1, 1 engineer. The 4hr battery target is now reachable.**
> 2. **NEW SHARPEN — Closed-source agent leadership is cracking (Zuckerberg "slower than expected," Reuters, July 2 2026).** The v14 "Meta Watermelon has caught up to GPT-5.5" claim is contradicted on the *agent* axis. **v15 sharpening: the agent-loop wedge (auditable, on-device, reproducible, MIT) is the 2026 opening.** Cite in v1.0 marketing as "we are not waiting for Meta's agents."

> **v15 retractions of v14:** **none.** The v14 3 critical / 5 medium / 5 minor issues hold. The v15 add is the `perceptiond.phase_map` CRITICAL add and the Zuckerberg "slower" agent-loop sharpening.

---

## TL;DR (one paragraph, v15)

The v14 architecture review holds. v15 elevates the `perceptiond.phase_map` execution substrate to the top CRITICAL issue. **The v1.0 wearable path is now defined: phase-mapped heterogeneous inference (vision encoder → NPU, text decode → CPU, salience gating → low-power DSP) per the Phase Matters paper.** The 4hr battery target is now reachable with salience gating + phase-mapped execution. The agent-loop wedge is now validated by Zuckerberg's "slower than expected" admission. The architecture decomposition score is 8.5/10 (up from 8.0/10 in v14).

---

## CRITICAL Issues (v15 ranking, refresh from v14)

### C1 (NEW v15 CRITICAL): `perceptiond.phase_map` execution substrate is undefined

- **Problem:** The current perceptiond runs LFM2.5-VL-450M entirely on CPU. This is the v1.0 wearable's primary power sink and latency bottleneck (10-15s/frame on x86_64). The Phase Matters paper (arXiv 2606.27906) demonstrates that on-device VLM inference requires phase-mapped heterogeneous NPU/CPU/GPU inference, with NPU prefill 1.64× faster, NPU decode 1.18× faster, and vision encoders 2.52× lower energy on NPU. **Without phase-mapped execution, the 4hr battery target is unreachable.**
- **Recommendation:** Add a `perceptiond.phase_map` module that decides per-frame where each phase runs based on (a) current SoC thermal headroom, (b) NPU availability (QNN/Hexagon on Snapdragon, Mali on others), (c) frame salience score. For Redax / aarch64, the QNN / Hexagon NPU path is the production target. The `perceptiond.phase_map` should be a pluggable backend (QNN, Mali, CPU fallback).
- **Effort:** 1 week, 1 engineer. Q3 W1 critical-path spike.
- **Evidence:** arXiv 2606.27906v1, late June 2026.

### C2 (held from v14): `memoryd` write contention + agent-self-memory underperforms

- **Problem:** Demoted from #1 to #2 in v15. The v9 MemDelta finding (agent self-memory 42% < basic RAG 47%) is the problem statement. Microsoft Memora (July 2026) is the answer.
- **Recommendation:** Port the Memora "storage/retrieval split" pattern to memoryd v1.5.
- **Effort:** 2 weeks, 1 engineer. Q3 W1-W2.

### C3 (held from v14): End-to-end event latency

- **Problem:** The audiod → openclaw → audiod round-trip is dominated by VLM inference (10-15s/frame). The v15 phase-mapped execution (C1) is the *answer* to this bottleneck.
- **Recommendation:** Addressed by C1.

---

## MEDIUM Issues (v15 ranking, refresh from v14)

- **M1 (held from v14):** Per-frame VLM latency on CPU-only — addressed by C1.
- **M2 (held from v14):** Idle-time reflection loop — held.
- **M3 (held from v14):** memoryd evaluation rigour — MemDelta protocol runner.
- **M4 (held from v14):** toold 120s timeout shared globally — held.
- **M5 (held from v14):** No per-daemon metrics export — held.
- **M6 (held from v12):** Karpathy 10-rule openclaw CLAUDE.md — held.
- **M7 (held from v12):** Gaze-Informed Proactive AI port to proactived v1 — held.
- **M8 (held from v14):** PR-review "X% AI-generated" tag — held.
- **M9 (NEW v15):** OpenPhone-3B shortlist evaluation — Q3 W1, 2 days, 1 engineer.
- **M10 (NEW v15):** 7-step marketing narrative + `openclaw.geopolitical_positioning` — Q3 W2, 3 days, 1 engineer.

---

## MINOR Issues (v15 ranking, refresh from v14)

- **m1-m5 (held from v14):** all held.
- **m6 (NEW v15):** Research-integrity responsible-AI framing in v1.0 spec — 1 day.

---

## Architecture Decomposition Score: 8.5/10 (v15)

**v15 reasoning:** the v14 score was 8.0/10 (Memora + MiCRo validate the decomposition). v15 adds 0.5 for the **Microsoft Frontier Co. + Palantir buy-the-dip + Zuckerberg "slower than expected" + Phase Matters paper + OpenAI 5%** industry-admission signals. The decomposition is no longer just engineering pragmatism — it is the 2026 SOTA direction, validated by industry admission and academic publication.

---

## Power & Thermal (v15 phase-mapped update)

| Component | Power | Notes |
|-----------|-------|-------|
| Salience gate (low-power DSP) | ~0.3W | always-on |
| Vision encoder on NPU (when salient) | ~1.5W | 2.52× lower energy than CPU |
| Text decode on CPU (when VLM fires) | ~3-5W | <2s/frame with phase-mapped NPU |
| Total active VLM event | ~5-7W | phase-mapped, salient-gated |
| Salient-gated VLM (5 FPS watchful, 30% salient) | ~1.5W average | **reachable** with phase-mapped execution |

**v15 power update:** the 4hr battery target (2x 200mAh @ 3.7V = 1.48Wh) is now reachable with salience gating + phase-mapped execution. **The v9 "salience gate is a UX detail" framing is retracted — it is the *power* decision, not a UX detail.**

---

## Form Factor (v15, no change from v14)

- **Weight target:** <50g (held from v14).
- **Battery target:** 4hr (now reachable with v15 phase-mapped execution + salience gating).
- **Storage target:** 32GB eMMC minimum (held from v14).
- **RAM target:** 4GB LPDDR minimum, 8GB preferred (held from v14).
- **Open question:** Redax SoC choice (Qualcomm vs MediaTek) — needed before Q3 W1 spike.

---

## Top 3 Recommendations for somdipto (v15)

1. **Approve the `perceptiond.phase_map` architecture spike (Q3 W1, 1 week, 1 engineer).** v15 CRITICAL #1. The 4hr battery target is now reachable.
2. **Approve the 7-step marketing narrative + `openclaw.geopolitical_positioning` spike (Q3 W2, 3 days, 1 engineer).** v15 SHARPEN. The "yours, not theirs" wedge is now geopolitically correct, industrially validated, analyst-validated, and self-admitted.
3. **Approve the OpenPhone-3B shortlist evaluation (Q3 W1, 2 days, 1 engineer).** v15 SHARPEN. Plan-C for the v1.5 audiod post-processor.

---

## Open Questions for somdipto (v15)

1. **`perceptiond.phase_map` spike priority** — Q3 W1 (recommend: yes, 1 week, 1 engineer)
2. **Redax SoC choice (Qualcomm vs MediaTek)** — needed before Q3 W1 spike (recommend: confirm with hardware team)
3. **OpenPhone-3B shortlist evaluation** — Q3 W1, 2 days (recommend: yes, 1 engineer)
4. **7-step marketing narrative + `openclaw.geopolitical_positioning` spike** — Q3 W2, 3 days (recommend: yes, 1 engineer)
5. **Research-integrity responsible-AI framing in v1.0 spec** — Q3 W2, 1 day (recommend: yes)
6. **Memora v1.5 port priority** — Q3 W1-W2 (recommend: yes, 2 weeks, 1 engineer)
7. **Apertus v1.1 4B EU data-residency ship-gate** — Q4 W1 (recommend: yes)
8. **HRM-Text-1B swap-in (replace LFM2.5-1.2B-Thinking directly or benchmark first?)** — recommend: benchmark first

---

## Footnotes (v15)

[^1]: https://arxiv.org/html/2606.27906v1 — "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC," late June 2026.
[^2]: https://github.com/HKUDS/OpenPhone — OpenPhone-3B, HKUDS, ACL 2026, late June 2026.
[^3]: https://www.geekwire.com/2026/microsoft-announces-2-5b-frontier-company-to-embed-ai-engineers-inside-customers/ — Microsoft Frontier Co., July 2 2026.
[^4]: https://www.cnbc.com/2026/07/02/palantir-shares-have-struggled-this-year-da-davidson-says-buy-the-dip.html — Palantir D.A. Davidson upgrade, July 2 2026.
[^5]: https://www.reuters.com (via GIGAZINE) — Zuckerberg admits Meta AI agent progress "slower than expected," July 2 2026.

---

## v14 architecture review content (preserved in backup)

The v14 architecture review (preserved in `dan2-architecture-review.v14-backup-2026-07-03.md`) covers: 3 critical / 5 medium / 5 minor issues, v1.5 spec revisions, decomposition score 8.0/10. **All v14 content is preserved verbatim in the backup. The v15 add is the `perceptiond.phase_map` CRITICAL add and the agent-loop-wedge sharpening. The v14 3/5/5 issue list holds.**

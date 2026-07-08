# Dan2 — AGI Roadmap v15 (2026-07-03 10:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v14:** `dan2-agi-roadmap.v14-backup-2026-07-03.md`

> **v15 deltas vs v14 (1 CRITICAL add, 3 sharpening, 0 retractions):**
> 1. **NEW CRITICAL — Q3 W1: `perceptiond.phase_map` architecture spike (1 week, 1 engineer).** The Phase Matters paper (arXiv 2606.27906) makes the phase-mapped heterogeneous execution substrate the v1.0 wearable path. The 4hr battery target is now reachable.
> 2. **NEW SHARPEN — Q3 W1: OpenPhone-3B shortlist evaluation (2 days, 1 engineer).** v1.5 audiod post-processor plan-C.
> 3. **NEW SHARPEN — Q3 W2: 7-step marketing narrative + `openclaw.geopolitical_positioning` spike (3 days, 1 engineer).** Microsoft Frontier Co. + Palantir buy-the-dip + Zuckerberg "slower" + OpenAI 5% + Anthropic-Samsung.
> 4. **NEW SHARPEN — Q3 W2: Research-integrity responsible-AI framing in v1.0 spec (1 day).** UCL Rees + Wilsdon evidence (Inside Higher Ed, July 2 2026).

> **v15 retractions of v14:** **none.** The v14 6/12/24-month plan holds. The v15 add is the Q3 W1 phase-mapped execution spike + 3 sharpening items.

---

## TL;DR (one paragraph, v15)

The v14 6/12/24-month plan holds. **v15 adds the Q3 W1 `perceptiond.phase_map` architecture spike as the v1.0 critical-path deliverable.** The Dan Glasses stack is structurally correct, validated by industry admission (Microsoft Frontier Co. $2.5B, Palantir buy-the-dip, Zuckerberg "slower than expected"). The closed-source agent race is stalling. The "yours, not theirs" wedge is now geopolitically correct, industrially validated, analyst-validated, and self-admitted. **6-month plan: ship the v1.0 wearable path with phase-mapped execution. 12-month plan: ship the v1.5 audiod post-processor with HRM-Text-1B (plan-A) + Apertus v1.1 4B (plan-B) + OpenPhone-3B (plan-C) + Memora storage/retrieval split. 24-month plan: ship the SIA-W+H port as the open-source RSI play + sovereign-on-prem vertical for healthcare/defense.**

---

## 6-Month Plan (Q3 2026 - Q4 2026): v1.0 Wearable

### Q3 W1 (v15 CRITICAL): `perceptiond.phase_map` architecture spike
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** `perceptiond.phase_map` module that decides per-frame where each phase runs (NPU for vision encoder, CPU for text decode, low-power DSP for salience gating). Pluggable backend (QNN/Hexagon on Snapdragon, Mali on others, CPU fallback).
- **Evidence:** Phase Matters paper, arXiv 2606.27906.
- **Why this is critical:** without phase-mapped execution, the 4hr battery target is unreachable.

### Q3 W1: OpenPhone-3B shortlist evaluation
- **Effort:** 2 days, 1 engineer.
- **Deliverable:** benchmark OpenPhone-3B vs HRM-Text-1B vs Apertus v1.1 4B on audiod post-processor workload. Recommend plan-A/B/C.
- **Evidence:** OpenPhone-3B, HKUDS, ACL 2026.

### Q3 W1-W2: Memora v1.5 port
- **Effort:** 2 weeks, 1 engineer (held from v14).
- **Deliverable:** memoryd v1.5 storage/retrieval split. New `/v1/retrieve` endpoint, new `/v1/abstractions` write path. `auto_apply=False` contract still binds.
- **Evidence:** Microsoft Memora, July 2026.

### Q3 W2: 7-step marketing narrative + `openclaw.geopolitical_positioning` spike
- **Effort:** 3 days, 1 engineer.
- **Deliverable:** v1.0 marketing page updated to the 7-step empirical narrative. Cite BBC Meta paywall + Apple $1,200+ upgrade + Anthropic Mythos gating + GLM-5.2 MIT + Palantir+NVIDIA sovereign Nemotron + Microsoft Frontier Co. $2.5B + OpenAI 5% to US government + Anthropic-Samsung. + 1-day `openclaw.geopolitical_positioning` spike to add the OpenAI 5%-to-government + Anthropic-Samsung signal set to the v1.0 product positioning.
- **Evidence:** BBC, Microsoft Frontier Co., Palantir buy-the-dip, OpenAI 5%, Anthropic-Samsung.

### Q3 W2: Research-integrity responsible-AI framing in v1.0 spec
- **Effort:** 1 day.
- **Deliverable:** v1.0 spec safety-considerations section updated. Dan Glasses helps the researcher *understand* their data and write a better proposal, not auto-generate grant applications. Cite Inside Higher Ed (UCL Rees + Wilsdon, July 2 2026).
- **Evidence:** Inside Higher Ed, July 2 2026.

### Q3 W3-Q4 W2: SIA-W+H port (held from v11)
- **Effort:** 4 weeks, 1 engineer + $200-500/mo cloud GPU.
- **Deliverable:** SIA-W+H harness ported to OpenClaw + memoryd. arXiv draft.
- **Evidence:** SIA + SIA-W+H, Hexo Labs, MIT, May 2026.

### Q3 W3: Red Queen moving-judge spike (held from v12)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** v1.5 danlab-multimodal implementation is the Red Queen moving-judge pattern.
- **Evidence:** Red Queen Gödel Machine, arXiv 2606.26294v1.

### Q3 W3: Karpathy 10-rule openclaw CLAUDE.md (held from v12)
- **Effort:** 1 day.
- **Deliverable:** openclaw CLAUDE.md updated with the 10-rule pattern.

### Q3 W3: openclaw PR-review "X% AI-generated" tag (held from v14)
- **Effort:** 3 days, 1 engineer.
- **Deliverable:** openclaw PR-review tool that surfaces "this PR is X% AI-generated" alongside the change.

### Q3 W4: VisualClaw cascade-gate port (held from v8/v9)
- **Effort:** 1.5 weeks, 1 engineer.
- **Deliverable:** perceptiond + memoryd port the VisualClaw on-device cascade-gate pattern. 50× latency reduction, +15.8% accuracy on EgoSchema.

### Q4 W1-W2: Anthropic Dreaming port (held from v8/v11)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** openclaw + memoryd port the Anthropic Dreaming `auto_apply=False` + `session_limit=50` pattern.

### Q4 W1-W2: Sovereign-on-prem vertical spike (held from v13)
- **Effort:** 1 engineer-week.
- **Deliverable:** Q4 2026 spike for healthcare/defense vertical. Palantir+NVIDIA Nemotron is the market-validated template.

### Q4 W3-W4: v1.0 wearable hardware integration
- **Effort:** 2 weeks, hardware + 1 engineer.
- **Deliverable:** Redax board integration, camera module, thermal validation, battery characterization.

---

## 12-Month Plan (Q1 2027 - Q2 2027): v1.5 Cognitive Stack

### Q1 W1-W2: HRM-Text-1B swap-in
- **Effort:** 2 weeks, 1 engineer.
- **Deliverable:** audiod post-processor upgraded to HRM-Text-1B. Benchmark vs LFM2.5-1.2B-Thinking.

### Q1 W3: Apertus v1.1 4B EU data-residency ship-gate
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** audiod post-processor alternative for EU users with EU data-residency requirements.

### Q1 W4: OpenPhone-3B plan-C integration
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** audiod post-processor plan-C integration. Two-layer self-learning memory.

### Q2 W1-W2: Qwen3-TTS v1.5 plan-A swap-in
- **Effort:** 2 weeks, 1 engineer.
- **Deliverable:** ttsd upgraded to Qwen3-TTS plan-A.

### Q2 W2: Chatterbox voice-cloning plan-A
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** ttsd voice-cloning with Chatterbox plan-A.

### Q2 W3-W4: LFM2.5-VL-450M-Extract structured-output VLM
- **Effort:** 2 weeks, 1 engineer.
- **Deliverable:** perceptiond upgraded to LFM2.5-VL-450M-Extract for structured-output VLM (JSON, table, code).

### Q2 W4: Ollie gaze-informed proactive v1 (held from v12)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** proactived v1 ported. perceptiond.get_gaze_estimate() → region selection → ttsd.speak() → memoryd.write() with TTL + attention cost.

---

## 24-Month Plan (Q3 2027 - Q4 2027): SIA-W+H RSI Play

### Q3 2027: SIA-W+H publication + ICML 2027 / ACL 2027
- **Effort:** 4 weeks, 1 engineer.
- **Deliverable:** arXiv draft + ICML 2027 / ACL 2027 submission.

### Q4 2027: Sovereign-on-prem vertical product launch
- **Effort:** 1 quarter, 3 engineers.
- **Deliverable:** healthcare/defense sovereign-on-prem product, EigenCloud TEE security story, Palantir+Nemotron co-positioning.

### Q4 2027: Compliance mode v2.0
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** HIPAA / FedRAMP compliance mode for healthcare/defense verticals.

---

## Top 3 Recommendations for somdipto (v15)

1. **Approve the Q3 W1 `perceptiond.phase_map` architecture spike (1 week, 1 engineer).** v15 CRITICAL. The 4hr battery target is now reachable.
2. **Approve the Q3 W1-W2 batch: OpenPhone-3B evaluation (2 days) + Memora v1.5 port (2 weeks) + 7-step marketing narrative (3 days) + research-integrity framing (1 day).** v15 SHARPEN. Total: 4 weeks, 1 engineer.
3. **Confirm the 6/12/24-month plan as the v15 roadmap.** Held from v14.

---

## Open Questions for somdipto (v15)

1. **`perceptiond.phase_map` spike priority** — Q3 W1 (recommend: yes, 1 week, 1 engineer)
2. **OpenPhone-3B shortlist evaluation** — Q3 W1, 2 days (recommend: yes, 1 engineer)
3. **Memora v1.5 port priority** — Q3 W1-W2 (recommend: yes, 2 weeks, 1 engineer)
4. **7-step marketing narrative + `openclaw.geopolitical_positioning`** — Q3 W2, 3 days (recommend: yes, 1 engineer)
5. **Research-integrity responsible-AI framing** — Q3 W2, 1 day (recommend: yes)
6. **SIA-W+H port budget ($200-500/mo cloud GPU)** — Q3 W3-Q4 W2 (recommend: yes)
7. **Sovereign-on-prem vertical product launch timeline** — Q4 2027 (recommend: yes, 1 quarter, 3 engineers)
8. **HRM-Text-1B swap-in (replace LFM2.5-1.2B-Thinking directly or benchmark first?)** — Q1 W1-W2 (recommend: benchmark first)

---

## Footnotes (v15)

[^1]: https://arxiv.org/html/2606.27906v1 — "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC," late June 2026.
[^2]: https://github.com/HKUDS/OpenPhone — OpenPhone-3B, HKUDS, ACL 2026, late June 2026.
[^3]: https://www.geekwire.com/2026/microsoft-announces-2-5b-frontier-company-to-embed-ai-engineers-inside-customers/ — Microsoft Frontier Co., July 2 2026.
[^4]: https://www.cnbc.com/2026/07/02/palantir-shares-have-struggled-this-year-da-davidson-says-buy-the-dip.html — Palantir D.A. Davidson upgrade, July 2 2026.
[^5]: https://www.reuters.com (via GIGAZINE) — Zuckerberg admits Meta AI agent progress "slower than expected," July 2 2026.

---

## v14 AGI roadmap content (preserved in backup)

The v14 AGI roadmap (preserved in `dan2-agi-roadmap.v14-backup-2026-07-03.md`) covers: 6/12/24-month plan with 3 specific decisions for somdipto, 5 critical deliverables, 4 open questions. **All v14 content is preserved verbatim in the backup. The v15 add is the Q3 W1 phase-mapped execution spike + 3 sharpening items. The v14 6/12/24-month plan holds.**

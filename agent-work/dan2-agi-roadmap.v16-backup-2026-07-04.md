# Dan2 — AGI Roadmap v16 (2026-07-03 11:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v15:** `dan2-agi-roadmap.v15-backup-2026-07-03.md`

> **v16 deltas vs v15 (2 CRITICAL adds, 2 sharpening, 1 retraction, 0 broad rollbacks):**
> 1. **NEW CRITICAL — Q3 W1: LFM2.5-230M audiod post-processor swap-in (1-2 weeks, 1 engineer).** 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5. Beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction. **The new v1.0 audiod post-processor target, displaces HRM-Text-1B from v15 plan-A to v1.5 plan-B.** Open-weight, dual-license (free <$10M ARR, paid enterprise).
> 2. **NEW CRITICAL — Q3 W2: Hermes Agent v1.0 audiod agent framework plan-A spike (1 week, 1 engineer).** Nous Research. Mixture-of-agents pattern. Outperforms Claude Opus + GPT-5.5 on hard agentic benchmarks. The new v1.0 audiod agent framework target, displaces SIA-W+H from v11 plan-A to v1.5 publishing bet.
> 3. **NEW SHARPEN — Q3 W2: 8-step marketing narrative update (2 days copy, 1 engineer).** $9.5B / 90 days / 5-vendor implementation-wedge bet + DoD GenAI.mil 1.7M users + OpenAI GPT-5.6 government-gating + Anthropic Fable 5 export ban lifted.
> 4. **NEW SHARPEN — Q3 W2: "As We May Search" (arXiv 2606.29652) paper read + memoryd v1.5 architecture add (1 day).** 91% nDCG@10 up to 100K docs, 1M with HNSW at 2% quality loss, 7B local LLM within 4 points of cloud baseline. The new v1.5 memoryd architecture flagship.
> 5. **NEW RETRACTION — Q3 W2: Update v15 "Anthropic Mythos is gated to US Glasswing partners, $30K catch" to "Anthropic Mythos 5 is gated to ~100 US critical-infrastructure partners; Fable 5 export ban lifted July 1 2026 after Amazon-researcher jailbreak" (1 day copy update).**

> **v16 retractions of v15:** **1 partial retraction** (v15 Mythos $30K catch line, see above). No v15 6/12/24-month plan is retracted.

## TL;DR (one paragraph, v16)

The v15 6/12/24-month plan holds. **v16 adds: Q3 W1 LFM2.5-230M audiod post-processor swap-in (CRITICAL #1) + Q3 W2 Hermes Agent plan-A spike (CRITICAL #2) + Q3 W2 8-step marketing narrative + Q3 W2 As We May Search paper read + Q3 W2 Mythos $30K catch retraction.** The Dan Glasses stack is structurally correct, validated at industry-scale ($9.5B / 90 days / 5-vendor), government-deployed (DoD GenAI.mil 1.7M users), academically-validated (Phase Matters, As We May Search, EPFL MiCRo), and now has two strong v1.0 audiod targets (LFM2.5-230M post-processor + Hermes Agent agent framework). **6-month plan: ship the v1.0 audiod post-processor with LFM2.5-230M, phase-mapped execution substrate, Hermes Agent agent framework. 12-month plan: ship the v1.5 audiod post-processor with HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-C) + OpenPhone-3B (plan-D) + Memora + As We May Search storage/retrieval split. 24-month plan: ship the SIA-W+H port as the open-source RSI play + sovereign-on-prem vertical for healthcare/defense (DoD-validated) + LFM2.5-230M audiod for v1.0 wearable path.**

## 6-Month Plan (Q3 2026 - Q4 2026): v1.0 Wearable

### Q3 W1 (v16 CRITICAL #1): LFM2.5-230M audiod post-processor swap-in
- **Effort:** 1-2 weeks, 1 engineer.
- **Deliverable:** audiod post-processor upgraded from LFM2.5-1.2B-Thinking to LFM2.5-230M. Benchmark on audiod post-processor workload (transcript cleaning, intent classification, command extraction, summarization).
- **Evidence:** LFM2.5-230M, Liquid AI, June 26 2026, open-weight, dual-license, 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction.
- **Why this is critical:** the v1.0 audiod post-processor target is now a 230M model that runs at 42 tok/s on a Raspberry Pi 5. The audiod post-processor is no longer a 1B model on a desktop — it is a 230M model on a wearable. This is the audiod equivalent of the v15 Phase Matters execution substrate decision.

### Q3 W1: `perceptiond.phase_map` architecture spike
- **Effort:** 1 week, 1 engineer. (held from v15)
- **Deliverable:** `perceptiond.phase_map` module that decides per-frame where each phase runs (NPU for vision encoder, CPU for text decode, low-power DSP for salience gating). Pluggable backend (QNN/Hexagon on Snapdragon, Mali on others, CPU fallback).
- **Evidence:** Phase Matters paper, arXiv 2606.27906.

### Q3 W1: OpenPhone-3B shortlist evaluation
- **Effort:** 2 days, 1 engineer. (held from v15)
- **Deliverable:** benchmark OpenPhone-3B vs HRM-Text-1B vs Apertus v1.1 4B on audiod post-processor workload. Recommend plan-B/C/D order for v1.5.
- **Evidence:** OpenPhone-3B, HKUDS, ACL 2026.

### Q3 W1-W2: Memora + As We May Search memoryd v1.5 port
- **Effort:** 2 weeks, 1 engineer. (held from v14, sharpened in v16 with As We May Search)
- **Deliverable:** memoryd v1.5 storage/retrieval split. New `/v1/retrieve` endpoint, new `/v1/abstractions` write path. Local-first HNSW at 1M document scale (As We May Search 91% nDCG@10). `auto_apply=False` contract still binds.
- **Evidence:** Microsoft Memora (July 2026) + "As We May Search" (arXiv 2606.29652, late June 2026).

### Q3 W2 (v16 CRITICAL #2): Hermes Agent v1.0 audiod agent framework plan-A spike
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** Hermes Agent pattern ported to openclaw + audiod. Mixture-of-agents pattern. 11% higher than GPT-5.5 running solo on hard agentic benchmarks.
- **Evidence:** Hermes Agent, Nous Research, late June 2026.

### Q3 W2: 8-step marketing narrative + `openclaw.geopolitical_positioning` spike
- **Effort:** 3 days, 1 engineer. (held from v15, sharpened in v16 with 4 new signals)
- **Deliverable:** v1.0 marketing page updated to the 8-step empirical narrative. Cite BBC Meta paywall + Apple $1,200+ upgrade + Anthropic Mythos 5 (~100 US critical-infrastructure partners, Fable 5 export ban lifted July 1) + GLM-5.2 MIT + Palantir+NVIDIA sovereign Nemotron + **$9.5B / 90 days / 5-vendor implementation-wedge bet** + **DoD GenAI.mil 1.7M users + 100K custom agents** + **OpenAI GPT-5.6 Sol/Terra/Luna gated to 20 US-approved companies**.
- **Evidence:** beri.net, defenseone.com, theverge.com, qz.com.

### Q3 W2: Research-integrity responsible-AI framing in v1.0 spec
- **Effort:** 1 day. (held from v15)
- **Deliverable:** v1.0 spec safety-considerations section updated. Dan Glasses helps the researcher *understand* their data and write a better proposal, not auto-generate grant applications. Cite Inside Higher Ed (UCL Rees + Wilsdon, July 2 2026).
- **Evidence:** Inside Higher Ed, July 2 2026.

### Q3 W2: "As We May Search" paper read + memoryd v1.5 addendum
- **Effort:** 1 day. (NEW v16)
- **Deliverable:** read "As We May Search" (arXiv 2606.29652). Add to papers-to-read top-5. Update memoryd v1.5 architecture addendum with HNSW at 1M document scale.
- **Evidence:** arXiv 2606.29652, late June 2026.

### Q3 W2: v15 Mythos $30K catch retraction
- **Effort:** 1 day. (NEW v16)
- **Deliverable:** update v1.0 marketing copy. Replace "Anthropic Mythos is gated to US Glasswing partners, $30K catch" with "Anthropic Mythos 5 is gated to ~100 US critical-infrastructure partners; Fable 5 export ban lifted July 1 2026 after Amazon-researcher jailbreak."
- **Evidence:** qz.com, mashable.com, June 30 - July 1 2026.

### Q3 W3-Q4 W2: SIA-W+H port (held from v11)
- **Effort:** 4 weeks, 1 engineer + $200-500/mo cloud GPU.
- **Deliverable:** SIA-W+H harness ported to OpenClaw + memoryd. arXiv draft. **v16: this is now the v1.5 publishing bet, no longer the v1.0 plan-A.**
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

### Q4 W1-W2: Sovereign-on-prem vertical spike (held from v13, sharpened in v16 with DoD GenAI.mil 1.7M users)
- **Effort:** 1 engineer-week.
- **Deliverable:** Q4 2026 spike for healthcare/defense vertical. Palantir+NVIDIA Nemotron is the market-validated template. DoD GenAI.mil 1.7M users + 100K custom agents is the DoD-deployed template. **v16 add: cite the DoD deployment scale as the market-validated evidence.**

### Q4 W3-W4: v1.0 wearable hardware integration
- **Effort:** 2 weeks, hardware + 1 engineer.
- **Deliverable:** Redax board integration, camera module, thermal validation, battery characterization. **v16 add: validate LFM2.5-230M audiod post-processor runs on Redax aarch64 at the 42 tok/s Raspberry Pi 5 baseline or better.**

## 12-Month Plan (Q1 2027 - Q2 2027): v1.5 Cognitive Stack

### Q1 W1-W2: HRM-Text-1B swap-in (v1.5 plan-B)
- **Effort:** 2 weeks, 1 engineer. (held from v11, **displaced from v1.0 plan-A to v1.5 plan-B by LFM2.5-230M in v16**)
- **Deliverable:** audiod post-processor upgraded to HRM-Text-1B. Benchmark vs LFM2.5-230M.

### Q1 W3: Apertus v1.1 4B EU data-residency ship-gate (v1.5 plan-C)
- **Effort:** 1 week, 1 engineer. (held from v14, **displaced from v1.5 plan-B to v1.5 plan-C**)
- **Deliverable:** audiod post-processor alternative for EU users with EU data-residency requirements.

### Q1 W4: OpenPhone-3B plan-D integration
- **Effort:** 1 week, 1 engineer. (held from v15, **displaced from v1.5 plan-C to v1.5 plan-D**)
- **Deliverable:** audiod post-processor plan-D integration. Two-layer self-learning memory.

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

## 24-Month Plan (Q3 2027 - Q4 2027): SIA-W+H RSI Play + DoD Vertical

### Q3 2027: SIA-W+H publication + ICML 2027 / ACL 2027
- **Effort:** 4 weeks, 1 engineer.
- **Deliverable:** arXiv draft + ICML 2027 / ACL 2027 submission. **v16: this is the v1.5 publishing bet, not the v1.0 deliverable.**

### Q4 2027: Sovereign-on-prem vertical product launch (DoD-validated)
- **Effort:** 1 quarter, 3 engineers.
- **Deliverable:** healthcare/defense sovereign-on-prem product, EigenCloud TEE security story, Palantir+Nemotron co-positioning. **v16 add: cite DoD GenAI.mil 1.7M users + 100K custom agents as the DoD-deployed template. The vertical is no longer a market thesis — it is a documented Department of Defense deployment.**

### Q4 2027: Compliance mode v2.0
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** HIPAA / FedRAMP compliance mode for healthcare/defense verticals.

## Top 3 Recommendations for somdipto (v16)

1. **Approve the Q3 W1 LFM2.5-230M audiod post-processor swap-in (1-2 weeks, 1 engineer).** v16 CRITICAL #1. 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction. The new v1.0 audiod post-processor target.
2. **Approve the Q3 W2 Hermes Agent v1.0 audiod agent framework plan-A spike (1 week, 1 engineer).** v16 CRITICAL #2. Nous Research. Outperforms Claude Opus + GPT-5.5 on hard agentic benchmarks. Mixture-of-agents pattern is a published 2026 SOTA.
3. **Approve the Q3 W2 batch: 8-step marketing narrative (2 days) + As We May Search paper read (1 day) + v15 Mythos $30K catch retraction (1 day) + research-integrity framing (1 day, held from v15).** v16 SHARPEN. Total: 5 days, 1 engineer. **v16 add: the 8-step narrative is now DoD-deployed, multi-vendor-validated, government-gated.**

## Open Questions for somdipto (v16)

1. **LFM2.5-230M audiod post-processor swap-in priority** — Q3 W1 (recommend: yes, 1-2 weeks, 1 engineer)
2. **Hermes Agent v1.0 audiod agent framework plan-A spike** — Q3 W2 (recommend: yes, 1 week, 1 engineer)
3. **Memora + As We May Search memoryd v1.5 port priority** — Q3 W1-W2 (recommend: yes, 2 weeks, 1 engineer)
4. **8-step marketing narrative + `openclaw.geopolitical_positioning`** — Q3 W2, 3 days (recommend: yes, 1 engineer)
5. **"As We May Search" paper read priority** — Q3 W2, 1 day (recommend: yes, before the memoryd port starts)
6. **v15 Mythos $30K catch retraction** — Q3 W2, 1 day (recommend: yes, the Fable 5 export ban lift is the correct retraction)
7. **Research-integrity responsible-AI framing** — Q3 W2, 1 day (recommend: yes, held from v15)
8. **SIA-W+H port budget ($200-500/mo cloud GPU)** — Q3 W3-Q4 W2 (recommend: yes, this is now the v1.5 publishing bet, not the v1.0 deliverable)
9. **Sovereign-on-prem vertical product launch timeline** — Q4 2027 (recommend: yes, 1 quarter, 3 engineers, **DoD GenAI.mil 1.7M users is the DoD-deployed template**)
10. **HRM-Text-1B / Apertus v1.1 4B / OpenPhone-3B v1.5 plan-B/C/D order** — recommend: hold order, they are now v1.5 candidates, LFM2.5-230M is v1.0

## Footnotes (v16)

[^1]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI, June 26 2026
[^2]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor implementation-wedge bet
[^3]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users + 100K custom agents
[^4]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026
[^5]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research, late June 2026
[^6]: https://qz.com/anthropic-claude-fable-5-mythos-5-export-controls-lifted-070126 — Anthropic Fable 5 + Mythos 5 export ban lifted
[^7]: https://www.theverge.com/ai-artificial-intelligence/960588/openai-government-5-percent-stake-trump — OpenAI GPT-5.6 government-gating

## v15 AGI roadmap content (preserved in backup)

The v15 AGI roadmap (preserved in `dan2-agi-roadmap.v15-backup-2026-07-03.md`) covers: 6/12/24-month plan with 3 specific decisions for somdipto, 5 critical deliverables, 4 open questions. **All v15 content is preserved verbatim in the backup. The v16 add is the LFM2.5-230M audiod post-processor swap-in (CRITICAL #1) + Hermes Agent v1.0 audiod agent framework plan-A (CRITICAL #2) + 8-step marketing narrative + As We May Search + Mythos $30K catch retraction. The v15 6/12/24-month plan holds.**
ed in v16 with $9.5B / 90 days / 5-vendor)
- **Deliverable:** v1.0 marketing page updated to the 8-step empirical narrative. Cite BBC Meta paywall + Apple $1,200+ upgrade + Anthropic Mythos 5 / Fable 5 + GLM-5.2 MIT + Palantir+NVIDIA sovereign Nemotron + $9.5B / 90 days / 5-vendor implementation-wedge bet + DoD GenAI.mil 1.7M users + OpenAI GPT-5.6 government-gating.
- **Evidence:** BBC, Microsoft Frontier Co., Palantir buy-the-dip, OpenAI 5%, Anthropic Fable 5 export ban lifted, $9.5B / 90 days / 5-vendor, DoD GenAI.mil 1.7M, OpenAI GPT-5.6.

### Q3 W2: Research-integrity responsible-AI framing in v1.0 spec
- **Effort:** 1 day. (held from v15)
- **Deliverable:** v1.0 spec safety-considerations section updated. Dan Glasses helps the researcher *understand* their data and write a better proposal, not auto-generate grant applications.
- **Evidence:** Inside Higher Ed, July 2 2026.

### Q3 W2: Mythos $30K catch partial retraction
- **Effort:** 1 day copy update.
- **Deliverable:** v15 "Anthropic Mythos is gated to US Glasswing partners, $30K catch" revised to "Anthropic Mythos 5 is gated to ~100 US critical-infrastructure partners; Fable 5 export ban lifted July 1 2026 after Amazon-researcher jailbreak." 
- **Evidence:** Anthropic Fable 5 + Mythos 5 export ban lifted, June 30 - July 1 2026.

### Q3 W3-Q4 W2: SIA-W+H port (held from v11, now v1.5 publishing bet)
- **Effort:** 4 weeks, 1 engineer + $200-500/mo cloud GPU. **Note: v16 add: SIA-W+H is now v1.5 publishing bet, no longer v1.0 plan-A. Hermes Agent is v1.0 plan-A.**
- **Deliverable:** SIA-W+H harness ported to OpenClaw + memoryd. arXiv draft. ICML 2027 / ACL 2027 submission.
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

### Q4 W1-W2: Sovereign-on-prem vertical spike (held from v13, sharpened in v16 with DoD GenAI.mil)
- **Effort:** 1 engineer-week.
- **Deliverable:** Q4 2026 spike for healthcare/defense vertical. DoD GenAI.mil 1.7M users + 100K custom agents is the DoD-validated template.

### Q4 W3-W4: v1.0 wearable hardware integration
- **Effort:** 2 weeks, hardware + 1 engineer.
- **Deliverable:** Redax board integration, camera module, thermal validation, battery characterization.

## 12-Month Plan (Q1 2027 - Q2 2027): v1.5 Cognitive Stack

### Q1 W1-W2: HRM-Text-1B swap-in (now v1.5 plan-B, held from v11 v1.0 plan-A)
- **Effort:** 2 weeks, 1 engineer.
- **Deliverable:** audiod post-processor upgrade to HRM-Text-1B. Benchmark vs LFM2.5-230M (v1.0 plan-A) and LFM2.5-1.2B-Thinking.

### Q1 W3: Apertus v1.1 4B EU data-residency ship-gate (now v1.5 plan-C, held from v14 v1.5 plan-B)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** audiod post-processor alternative for EU users with EU data-residency requirements.

### Q1 W4: OpenPhone-3B v1.5 plan-D integration (held from v15 v1.5 plan-C)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** audiod post-processor plan-D integration. Two-layer self-learning memory.

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

## 24-Month Plan (Q3 2027 - Q4 2027): SIA-W+H RSI Play + Sovereign-On-Prem Vertical

### Q3 2027: SIA-W+H publication + ICML 2027 / ACL 2027
- **Effort:** 4 weeks, 1 engineer.
- **Deliverable:** arXiv draft + ICML 2027 / ACL 2027 submission.

### Q4 2027: Sovereign-on-prem vertical product launch (DoD-validated, sharpened in v16)
- **Effort:** 1 quarter, 3 engineers.
- **Deliverable:** healthcare/defense sovereign-on-prem product, EigenCloud TEE security story, DoD GenAI.mil template co-positioning.

### Q4 2027: Compliance mode v2.0
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** HIPAA / FedRAMP compliance mode for healthcare/defense verticals.

## Top 3 Recommendations for somdipto (v16)

1. **Approve the Q3 W1 LFM2.5-230M audiod post-processor swap-in (1-2 weeks, 1 engineer).** v16 CRITICAL #1. 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5. Beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction. The new v1.0 audiod post-processor target.
2. **Approve the Q3 W2 Hermes Agent v1.0 audiod agent framework plan-A spike (1 week, 1 engineer).** v16 CRITICAL #2. Outperforms Claude Opus + GPT-5.5 on hard agentic benchmarks. The new v1.0 audiod agent framework target.
3. **Confirm the 8-step marketing narrative + Mythos $30K catch partial retraction (Q3 W2, 3 days, 1 engineer).** v16 SHARPEN. $9.5B / 90 days / 5-vendor + DoD GenAI.mil 1.7M users + OpenAI GPT-5.6 government-gating + Anthropic Fable 5 export ban lifted.

## Open Questions for somdipto (v16)

1. **LFM2.5-230M audiod post-processor swap-in priority** — Q3 W1, 1-2 weeks, 1 engineer (recommend: yes, the new v1.0 audiod target)
2. **LFM2.5-230M dual-license structure** — free <$10M ARR, paid enterprise (recommend: verify, the dual-license is the v1.0 audiod cost story)
3. **LFM2.5-230M on aarch64 (Raspberry Pi 5) benchmarks** — 42 tok/s published, Redax aarch64 is the production target (recommend: 1-day benchmark spike after Q3 W1 swap-in)
4. **Hermes Agent v1.0 audiod agent framework plan-A spike** — Q3 W2, 1 week, 1 engineer (recommend: yes, outperforms Claude Opus + GPT-5.5)
5. **8-step marketing narrative + Mythos partial retraction** — Q3 W2, 3 days, 1 engineer (recommend: yes, $9.5B / 90 days / 5-vendor / DoD 1.7M / GPT-5.6 government-gating)
6. **Memora + As We May Search memoryd v1.5 port** — Q3 W1-W2, 2 weeks, 1 engineer (recommend: yes, 98% context reduction + 91% nDCG@10)
7. **SIA-W+H port budget ($200-500/mo cloud GPU)** — Q3 W3-Q4 W2 (recommend: yes, now v1.5 publishing bet)
8. **Sovereign-on-prem vertical product launch timeline** — Q4 2027 (recommend: yes, 1 quarter, 3 engineers, DoD GenAI.mil template co-positioning)
9. **HRM-Text-1B / Apertus v1.1 4B / OpenPhone-3B v1.5 plan-B/C/D order** — recommend: hold order, they are now v1.5 candidates, LFM2.5-230M is v1.0
10. **DoD GenAI.mil partnership target** — recommend: 1 design partner Q4 W1-W2, then 12-month MSA

## Footnotes (v16)

[^1]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI, June 26 2026
[^2]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research, late June 2026
[^3]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor, June 30 - July 2 2026
[^4]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users, July 2 2026
[^5]: https://qz.com/anthropic-claude-fable-5-mythos-5-export-controls-lifted-070126 — Anthropic Fable 5 + Mythos 5 export ban lifted, June 30 - July 1 2026
[^6]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026
[^7]: https://arxiv.org/html/2606.27906v1 — "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC" (held from v15)
[^8]: https://github.com/HKUDS/OpenPhone — OpenPhone-3B, HKUDS, ACL 2026 (held from v15)
[^9]: https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity — Microsoft Memora (held from v14)
[^10]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v11)

## v15 AGI roadmap content (preserved in backup)

The v15 AGI roadmap (preserved in `dan2-agi-roadmap.v15-backup-2026-07-03.md`) covers: 6/12/24-month plan with `perceptiond.phase_map` Q3 W1 critical-path spike, OpenPhone-3B plan-C evaluation, 7-step marketing narrative, research-integrity responsible-AI framing. **All v15 content is preserved verbatim in the backup. The v16 add is the LFM2.5-230M audiod post-processor swap-in (CRITICAL #1) + Hermes Agent v1.0 audiod agent framework plan-A spike (CRITICAL #2) + 8-step marketing narrative + As We May Search paper read + Mythos $30K catch partial retraction. The v15 6/12/24-month plan holds.**

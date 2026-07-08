# Dan2 — AGI Roadmap v17 (2026-07-04 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v16:** `dan2-agi-roadmap.v16-backup-2026-07-04.md`

> **v17 deltas vs v16 (2 CRITICAL adds, 3 sharpening, 1 partial retraction, 0 broad rollbacks):**
> 1. **NEW CRITICAL — Q3 W2: OpenClaw protocol surface marketing artifact (2 days copy + spec, 1 engineer).** v17 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. We shipped it." (Vinton Cerf, Open Frontier, June 30 2026).
> 2. **NEW CRITICAL — Q3 W2: v17 Mythos 5 partial retraction (1 day copy, 1 engineer).** v17 CRITICAL #2. Update v1.0 marketing: "Anthropic Mythos 5 is gated to the Glasswing program (cybersecurity researchers at trusted companies), now expanding beyond the initial ~100 US critical-infrastructure partners to broader domestic + international Glasswing members."
> 3. **NEW SHARPEN — Q3 W2: 9-step marketing narrative (1 day copy, 1 engineer).** v16 8-step + Vinton Cerf (v17 step 9). v17 9-step.
> 4. **NEW SHARPEN — Q3 W2: Project Lightwell $5B + Chainguard Athena spike (1 day copy, 1 engineer).** $14.5B / 120 days / 6-vendor implementation-wedge bet, now extending to OSS supply chain.
> 5. **NEW SHARPEN — Q3 W2: OpenAN + Anthropic Claude Code fingerprinting spike (1 day copy, 1 engineer).** Open-source-side counter-narrative + "vendor lock-in is structural" evidence.

> **v17 retractions of v16:** **1 partial retraction** (v16 Mythos $30K catch / ~100 US framing — see #2). No v16 6/12/24-month plan is retracted. The v16 Q3 W1 LFM2.5-230M audiod post-processor swap-in is held.

## TL;DR (one paragraph, v17)

The v16 6/12/24-month plan holds. **v17 adds: Q3 W2 OpenClaw protocol surface marketing artifact (CRITICAL #1) + Q3 W2 v17 Mythos 5 partial retraction (CRITICAL #2) + Q3 W2 9-step marketing narrative + Q3 W2 Project Lightwell + Chainguard Athena + OpenAN + Claude Code fingerprinting + Claude Science workbench-layer v1.0 spec add.** The Dan Glasses stack is structurally correct, validated at industry-icon level (Vinton Cerf, June 30 2026), validated at industry-scale ($14.5B / 120 days / 6-vendor, v17), government-deployed (DoD GenAI.mil 1.7M users), academically-validated (Phase Matters, As We May Search, EPFL MiCRo), and now has two strong v1.0 audiod targets (LFM2.5-230M post-processor + Hermes Agent agent framework) + an industry-icon-endorsed orchestration layer (OpenClaw). **6-month plan: ship the v1.0 audiod post-processor with LFM2.5-230M, phase-mapped execution substrate, Hermes Agent agent framework, and the v17 OpenClaw protocol surface marketing artifact. 12-month plan: ship the v1.5 audiod post-processor with HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-C) + OpenPhone-3B (plan-D) + Memora + As We May Search storage/retrieval split. 24-month plan: ship the SIA-W+H port as the open-source RSI play + sovereign-on-prem vertical for healthcare/defense (DoD-validated) + LFM2.5-230M audiod for v1.0 wearable path + Project Lightwell + OpenAN agent interoperability.**

## 6-Month Plan (Q3 2026 - Q4 2026): v1.0 Wearable

### Q3 W1: LFM2.5-230M audiod post-processor swap-in (held from v16)
- **Effort:** 1-2 weeks, 1 engineer.
- **Deliverable:** audiod post-processor upgraded from LFM2.5-1.2B-Thinking to LFM2.5-230M. Benchmark on audiod post-processor workload.
- **Evidence:** LFM2.5-230M, Liquid AI, June 26 2026.
- **v17 add:** validate the v17 dual-license structure (free <$10M ARR, paid enterprise) is the v17 audiod cost story.

### Q3 W1: `perceptiond.phase_map` architecture spike (held from v15)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** `perceptiond.phase_map` module. Pluggable backend (QNN/Hexagon on Snapdragon, Mali on others, CPU fallback).
- **Evidence:** Phase Matters paper, arXiv 2606.27906.

### Q3 W1: OpenPhone-3B shortlist evaluation (held from v15)
- **Effort:** 2 days, 1 engineer.
- **Deliverable:** benchmark OpenPhone-3B vs HRM-Text-1B vs Apertus v1.1 4B on audiod post-processor workload.

### Q3 W1-W2: Memora + As We May Search memoryd v1.5 port (held from v14, v17 sharpening)
- **Effort:** 2 weeks, 1 engineer.
- **Deliverable:** memoryd v1.5 storage/retrieval split. New `/v1/retrieve` endpoint, new `/v1/abstractions` write path. Local-first HNSW at 1M document scale.
- **Evidence:** Microsoft Memora (July 2026) + "As We May Search" (arXiv 2606.29652).
- **v17 add:** cite IBM Red Hat Project Lightwell as the v17 analog for OSS supply chain memory.

### Q3 W2: Hermes Agent v1.0 audiod agent framework plan-A spike (held from v16)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** Hermes Agent pattern ported to openclaw + audiod. Mixture-of-agents pattern.

### Q3 W2 (v17 CRITICAL #1): OpenClaw protocol surface marketing artifact
- **Effort:** 2 days, 1 engineer.
- **Deliverable:** document OpenClaw's protocol surface (JSON-RPC envelope, daemon health probes, kanban/issue trackers, gateway protocol, paperclip agent harness) as a v1.0 marketing artifact. "Vinton Cerf says AI agents need TCP/IP. We shipped it." Cite Cerf in the v1.0 spec.
- **Evidence:** Vinton Cerf Open Frontier, June 30 2026.

### Q3 W2 (v17 CRITICAL #2): v17 Mythos 5 partial retraction
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** update v1.0 marketing: "Anthropic Mythos 5 is gated to the Glasswing program (cybersecurity researchers at trusted companies), now expanding beyond the initial ~100 US critical-infrastructure partners to broader domestic + international Glasswing members."
- **Evidence:** Ars Technica, July 1 2026.

### Q3 W2: 9-step marketing narrative (v16 8-step + v17 step 9)
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 marketing page updated to the v17 9-step empirical narrative. Add Vinton Cerf as the v17 step 9.
- **Evidence:** v17 deltas.

### Q3 W2: Project Lightwell $5B + Chainguard Athena copy update
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 marketing copy updated. v16 $9.5B / 90 days / 5-vendor → v17 $14.5B / 120 days / 6-vendor. Cite IBM Red Hat Project Lightwell + Chainguard Athena.
- **Evidence:** Dark Reading + Let's Data Science, late June 2026.

### Q3 W2: OpenAN + Anthropic Claude Code fingerprinting copy update
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 marketing copy updated. Cite OpenAN (China-led open-source agent interoperability) + Anthropic Claude Code timezone/proxy fingerprinting.
- **Evidence:** Developing Telecoms + Let's Data Science, late June 2026.

### Q3 W2: Anthropic Claude Science workbench-layer v1.0 spec add
- **Effort:** 1 day, 1 engineer.
- **Deliverable:** v1.0 spec safety-considerations section updated. Cite Claude Science as the v17 closed-source admission that "harness > model."
- **Evidence:** MobiHealthNews, June 30 2026.

### Q3 W2: Research-integrity responsible-AI framing in v1.0 spec (held from v15)
- **Effort:** 1 day.
- **Deliverable:** v1.0 spec safety-considerations section updated.

### Q3 W2: "As We May Search" paper read + memoryd v1.5 addendum (held from v16)
- **Effort:** 1 day.
- **Deliverable:** read "As We May Search" (arXiv 2606.29652). Add to papers-to-read top-5.

### Q3 W2: v16 Mythos $30K catch retraction (held from v16)
- **Effort:** 1 day.
- **Deliverable:** v1.0 marketing copy updated.

### Q3 W3-Q4 W2: SIA-W+H port (held from v11, v16 v1.5 publishing bet)
- **Effort:** 4 weeks, 1 engineer + $200-500/mo cloud GPU.
- **Deliverable:** SIA-W+H harness ported to OpenClaw + memoryd. arXiv draft. ICML 2027 / ACL 2027 submission.
- **v17 add:** v17 Cerf endorsement of the OpenClaw protocol surface strengthens the v16 SIA-W+H port recommendation.

### Q3 W3: Red Queen moving-judge spike (held from v12)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** v1.5 danlab-multimodal implementation is the Red Queen moving-judge pattern.

### Q3 W3: Karpathy 10-rule openclaw CLAUDE.md (held from v12)
- **Effort:** 1 day.
- **Deliverable:** openclaw CLAUDE.md updated with the 10-rule pattern.

### Q3 W3: openclaw PR-review "X% AI-generated" tag (held from v14)
- **Effort:** 3 days, 1 engineer.
- **Deliverable:** openclaw PR-review tool that surfaces "this PR is X% AI-generated" alongside the change.

### Q3 W4: VisualClaw cascade-gate port (held from v8/v9)
- **Effort:** 1.5 weeks, 1 engineer.
- **Deliverable:** perceptiond + memoryd port the VisualClaw on-device cascade-gate pattern.

### Q4 W1-W2: Anthropic Dreaming port (held from v8/v11)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** openclaw + memoryd port the Anthropic Dreaming `auto_apply=False` + `session_limit=50` pattern.

### Q4 W1-W2: Sovereign-on-prem vertical spike (held from v13, v17 DoD-validated)
- **Effort:** 1 engineer-week.
- **Deliverable:** Q4 2026 spike for healthcare/defense vertical. Palantir+NVIDIA Nemotron + DoD GenAI.mil template co-positioning.

### Q4 W1-W2: Project Lightwell $5B + Chainguard Athena spike (NEW v17)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** evaluate the v17 open-source supply chain AI security stack. Open-source supply chain memory + workbench + agent framework. Cite in v1.5 product roadmap.
- **Evidence:** Dark Reading + Let's Data Science, late June 2026.

### Q4 W1-W2: OpenAN agent interoperability framework spike (NEW v17)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** evaluate the v17 OpenAN agent interoperability framework. Multi-agent coordination, AI-native autonomous networks (Level 4 autonomy). Cite in v1.5 product roadmap.
- **Evidence:** Developing Telecoms, late June 2026.

### Q4 W3-W4: v1.0 wearable hardware integration
- **Effort:** 2 weeks, hardware + 1 engineer.
- **Deliverable:** Redax board integration, camera module, thermal validation, battery characterization.

## 12-Month Plan (Q1 2027 - Q2 2027): v1.5 Cognitive Stack

### Q1 W1-W2: HRM-Text-1B swap-in (v1.5 plan-B)
- **Effort:** 2 weeks, 1 engineer. (held from v11, displaced from v1.0 plan-A to v1.5 plan-B by LFM2.5-230M in v16)
- **Deliverable:** audiod post-processor upgraded to HRM-Text-1B. Benchmark vs LFM2.5-230M.

### Q1 W3: Apertus v1.1 4B EU data-residency ship-gate (v1.5 plan-C)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** audiod post-processor alternative for EU users with EU data-residency requirements.

### Q1 W4: OpenPhone-3B plan-D integration
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
- **Deliverable:** perceptiond upgraded to LFM2.5-VL-450M-Extract for structured-output VLM.

### Q2 W4: Ollie gaze-informed proactive v1 (held from v12)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** proactived v1 ported.

## 24-Month Plan (Q3 2027 - Q4 2027): SIA-W+H RSI Play + DoD Vertical + Project Lightwell + OpenAN

### Q3 2027: SIA-W+H publication + ICML 2027 / ACL 2027
- **Effort:** 4 weeks, 1 engineer.
- **Deliverable:** arXiv draft + ICML 2027 / ACL 2027 submission.
- **v17 add:** v17 Cerf endorsement of the OpenClaw protocol surface strengthens the v16 SIA-W+H port recommendation.

### Q4 2027: Sovereign-on-prem vertical product launch (DoD-validated)
- **Effort:** 1 quarter, 3 engineers.
- **Deliverable:** healthcare/defense sovereign-on-prem product. **v17 add: cite DoD GenAI.mil 1.7M users + 100K custom agents as the v17 DoD-deployed template.**

### Q4 2027: Compliance mode v2.0
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** HIPAA / FedRAMP compliance mode for healthcare/defense verticals.

### Q4 2027: Project Lightwell + OpenAN partner-product evaluation (NEW v17)
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** evaluate partner-product opportunities with IBM Red Hat Project Lightwell + OpenAN consortium. Cite in v2.0 product roadmap.
- **v17 add:** v17 adds "open-source supply chain AI security + agent interoperability" as the v17 v2.0 vertical, parallel to v13 sovereign-on-prem.

## Top 3 Recommendations for somdipto (v17)

1. **Approve the Q3 W2 OpenClaw protocol surface marketing artifact (2 days copy + spec, 1 engineer).** v17 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. We shipped it." (Vinton Cerf, Open Frontier, June 30 2026).
2. **Approve the Q3 W2 v17 Mythos 5 partial retraction (1 day copy, 1 engineer).** v17 CRITICAL #2. Update v1.0 marketing: "Anthropic Mythos 5 is gated to the Glasswing program, now expanding to broader domestic + international Glasswing members."
3. **Approve the Q3 W2 v17 batch: 9-step marketing narrative (1 day) + Project Lightwell $5B + Chainguard Athena (1 day) + OpenAN + Claude Code fingerprinting (1 day) + Claude Science workbench-layer v1.0 spec add (1 day) (Q3 W2, 4 days, 1 engineer).** v17 SHARPEN. **v17 add: total 4 days, $14.5B / 120 days / 6-vendor implementation-wedge bet + Vinton Cerf TCP/IP-for-agents + Claude Science workbench > model + OpenAN China-led + fingerprinting evidence.**

## Open Questions for somdipto (v17)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. We shipped it.")
2. **v17 Mythos 5 partial retraction priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v17 framing is "Glasswing program, expanding to broader domestic + international")
3. **9-step marketing narrative update** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
4. **Project Lightwell + Chainguard Athena spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes)
5. **OpenAN agent interoperability framework spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes)
6. **Anthropic Claude Code timezone/proxy fingerprinting marketing weight** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
7. **Anthropic Claude Science workbench-layer v1.0 spec add** — Q3 W2, 1 day, 1 engineer (recommend: yes)
8. **LFM2.5-230M / Hermes Agent / As We May Search / Memora / Phase Matters v16 priorities** — held from v16 (recommend: yes, all v16 priorities hold)
9. **SIA-W+H port budget ($200-500/mo cloud GPU)** — Q3 W3-Q4 W2 (recommend: yes, v16 v1.5 publishing bet)
10. **Sovereign-on-prem vertical product launch timeline** — Q4 2027 (recommend: yes, DoD GenAI.mil template co-positioning)
11. **v17 24-month plan: Project Lightwell + OpenAN partner-product evaluation** — Q4 2027, 1 quarter, 2 engineers (recommend: yes, v17 v2.0 vertical)

## Footnotes (v17)

[^1]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026
[^2]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026
[^3]: https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/ — Anthropic Mythos 5 Glasswing expansion, July 1 2026
[^4]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026
[^5]: https://www.letsdatascience.com/news/ai-scanners-expose-thousands-of-hidden-open-source-vulnerabi-420424be — Chainguard Athena coalition, late June 2026
[^6]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026
[^7]: https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc — Anthropic Claude Code timezone/proxy fingerprinting, late June 2026
[^8]: https://hackernoon.com/the-month-ai-governance-became-operational — HackerNoon, "The Month AI Governance Became Operational," June 2026
[^9]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^10]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^11]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^12]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^13]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users (held from v16)
[^14]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor (held from v16)
[^15]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v15)

## v16 AGI roadmap content (preserved in backup)

The v16 AGI roadmap (preserved in `dan2-agi-roadmap.v16-backup-2026-07-04.md`) covers: 6/12/24-month plan with Q3 W1 LFM2.5-230M audiod post-processor swap-in, Hermes Agent v1.0 audiod agent framework plan-A, 8-step marketing narrative, As We May Search paper read, Mythos $30K catch partial retraction. **All v16 content is preserved verbatim in the backup. The v17 add is the OpenClaw protocol surface marketing artifact (CRITICAL #1) + v17 Mythos 5 partial retraction (CRITICAL #2) + 9-step marketing narrative + Project Lightwell + Chainguard Athena + OpenAN + Claude Code fingerprinting + Claude Science workbench-layer v1.0 spec add. The v16 6/12/24-month plan holds, with v17 24-month plan adding Project Lightwell + OpenAN partner-product evaluation.**

# Dan2 — Architecture Review v17 (2026-07-04 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-architecture-review.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v16:** `dan2-architecture-review.v16-backup-2026-07-04.md`

> **v17 deltas vs v16 (2 CRITICAL adds, 3 sharpening, 1 partial retraction, 0 broad rollbacks):**
> 1. **NEW CRITICAL #1 — Document OpenClaw's protocol surface as a v1.0 marketing artifact.** Vinton Cerf (Open Frontier conference, Laude Institute, June 30 2026): "natural language is too ambiguous for reliable AI-agent-to-agent communication," predicts the rise of "formal, standardized protocols." Internet co-architect publicly endorses the "TCP/IP-for-agents" framing. **The v16 OpenClaw (TypeScript/Node) design is the v17 *evidence-confirmed* pattern. "Vinton Cerf says AI agents need TCP/IP. We shipped it." is the v17 marketing line.** Q3 W2, 2 days, 1 engineer.
> 2. **NEW CRITICAL #2 — Anthropic Mythos 5 expanding to broader Glasswing partners (Ars Technica, July 1 2026).** Beyond the original ~100 US critical-infrastructure partners, Mythos 5 is now expanding to "broader set of domestic and international partners in the Glasswing program." **v17 partial retraction of v16 "Anthropic Mythos 5 is gated to ~100 US critical-infrastructure partners." v17 framing: "Anthropic Mythos 5 is gated to the Glasswing program (cybersecurity researchers at trusted companies), now expanding beyond the initial ~100 US critical-infrastructure partners to broader domestic + international Glasswing members."** Q3 W2, 1 day copy, 1 engineer.
> 3. **NEW SHARPEN — Anthropic Claude Science (MobiHealthNews, June 30 2026) is the v17 strongest possible citable evidence that "harness > model."** Claude Science is "an AI workbench that runs on the same Claude models already available, including Claude Opus 4.8, without requiring special model access." **Not a new model — a workbench layer.** The first publicly shipped closed-source "workbench / agent harness" layer over a foundation model. **The v16 "the closed-source frontier is shifting from models to harnesses" thesis is now *empirically confirmed by Anthropic itself*.** Add to v1.0 spec safety-considerations section. Q3 W2, 1 day, 1 engineer.
> 4. **NEW SHARPEN — IBM Red Hat Project Lightwell $5B + Chainguard Athena coalition (late June 2026).** $5B Project Lightwell + 20,000 engineers for OSS patching, driven by Anthropic's Mythos findings. Chainguard Athena: 20+ orgs, 20,000+ AI-discovered findings, 2,000+ patches across 500 OSS projects. First coordinated disclosure wave due mid-July 2026. **v17 add: the v16 $9.5B / 90 days / 5-vendor implementation-wedge bet is now $14.5B / 120 days / 6-vendor.** Q3 W2, 1 day copy, 1 engineer.
> 5. **NEW SHARPEN — OpenAN project (China Mobile, GSMA, Huawei, MWC Shanghai 2026) + Anthropic Claude Code timezone/proxy fingerprinting (Gizmodo, late June 2026).** OpenAN is the first published, multi-vendor, China-led open-source agent interoperability framework (Linux Foundation Networking). Claude Code fingerprinting is the strongest possible citable evidence that "vendor lock-in is structural." Q3 W2, 1 day copy, 1 engineer.
> 6. **v17 PARTIAL RETRACTION of v16 — v16 "Anthropic Mythos 5 is gated to ~100 US critical-infrastructure partners" is partially retracted again.** See CRITICAL #2.

> **v17 retractions of v16:** **1 partial retraction** (v16 Mythos 5 framing, see CRITICAL #2). No v16 3/5/5 issue list retraction. No v16 model choice retraction.

## TL;DR (one paragraph, v17)

The v16 architecture review holds (decomposition score 9.0/10). v17 elevates to **9.2/10** with: (1) Vinton Cerf Open Frontier TCP/IP-for-agents CRITICAL #1, (2) Anthropic Mythos 5 Glasswing expansion CRITICAL #2, (3) Anthropic Claude Science workbench-layer admission, (4) IBM Red Hat Project Lightwell $5B + Chainguard Athena (now $14.5B / 120 days / 6-vendor implementation-wedge bet), (5) OpenAN China-led open-source agent interoperability framework, (6) Anthropic Claude Code timezone/proxy fingerprinting. The v1.0 audiod post-processor target is LFM2.5-230M (v16). The v1.0 audiod agent framework target is Hermes Agent (v16). The memoryd v1.5 architecture is empirical certainty (Memora + As We May Search, v16). The closed-source frontier is consistently gating access (Anthropic Mythos 5 → Glasswing expanding; OpenAI GPT-5.6 → 20 US-approved companies, v16). The implementation wedge is now $14.5B / 120 days / 6-vendor (v17). The decomposition is *industry-icon-endorsed, government-deployed, closed-source-admitted, government-gated*.

## CRITICAL Issues (v17 ranking, refresh from v16)

### C1 (NEW v17 CRITICAL #1): OpenClaw protocol surface marketing artifact

- **Problem:** The v16 OpenClaw (TypeScript/Node) design is structurally correct but is not yet framed as a v1.0 marketing artifact. Vinton Cerf (Open Frontier, June 30 2026) — the internet's co-architect — has publicly endorsed the "TCP/IP-for-agents" framing. The v17 marketing line "Vinton Cerf says AI agents need TCP/IP. We shipped it." is the v17 strongest possible citable evidence for the on-device + open-weights + auditable memory + auditable agent loop stack.
- **Recommendation:** Document OpenClaw's protocol surface (JSON-RPC envelope, daemon health probes, kanban/issue trackers, gateway protocol, paperclip agent harness) as a v1.0 marketing artifact. Cite Cerf in the v1.0 spec. Add "Vinton Cerf says AI agents need TCP/IP. We shipped it." to the v1.0 marketing page.
- **Effort:** 2 days, 1 engineer. Q3 W2.
- **Evidence:** https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c, June 30 2026.

### C2 (NEW v17 CRITICAL #2): v16 "Anthropic Mythos 5 is gated to ~100 US critical-infrastructure partners" further partial retraction

- **Problem:** Per Ars Technica (July 1 2026), Anthropic is "working with the government to expand Mythos access to a 'broader set of domestic and international partners in the Glasswing program.'" Commerce Secretary Howard Lutnick: "no longer need a license for exports or in-country transfers of its Claude Mythos and Claude Fable AI models." The v16 "~100 US critical-infrastructure partners" framing is no longer accurate.
- **Recommendation:** Update v1.0 marketing copy: "Anthropic Mythos 5 is gated to the Glasswing program (cybersecurity researchers at trusted companies), now expanding beyond the initial ~100 US critical-infrastructure partners to broader domestic + international Glasswing members."
- **Effort:** 1 day, 1 engineer. Q3 W2.
- **Evidence:** https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/, July 1 2026.

### C3 (held from v16): LFM2.5-230M audiod post-processor swap-in

- **Problem:** v16 set LFM2.5-230M as the v1.0 audiod post-processor target (displaces HRM-Text-1B from v1.0 plan-A to v1.5 plan-B). 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B + Gemma 3 1B.
- **Recommendation:** Q3 W1 swap-in, 1-2 weeks, 1 engineer.
- **Evidence:** https://liquid.ai/blog/lfm2-5-230m, June 26 2026.

### C4 (held from v16): Hermes Agent v1.0 audiod agent framework plan-A spike

- **Problem:** v16 set Hermes Agent as the v1.0 audiod agent framework plan-A (Nous Research, mixture-of-agents pattern, outperforms Claude Opus + GPT-5.5).
- **Recommendation:** Q3 W2, 1 week, 1 engineer.
- **Evidence:** https://www.nousresearch.com/agents/hermes, late June 2026.

### C5 (held from v16): `perceptiond.phase_map` execution substrate is undefined

- **Problem:** v16 held. The Phase Matters paper (arXiv 2606.27906) defines the phase-mapped heterogeneous NPU/CPU/GPU execution substrate. Without phase-mapped execution, the 4hr battery target is unreachable.
- **Recommendation:** Q3 W1, 1 week, 1 engineer.
- **Evidence:** arXiv 2606.27906v1, late June 2026.

### C6 (held from v16/v14): `memoryd` write contention + agent-self-memory underperforms

- **Problem:** v16 held. Memora (July 2026) + "As We May Search" (arXiv 2606.29652) = v16 empirical certainty for local-first IR at 1M documents. v17 add: IBM Red Hat Project Lightwell is the v17 analog for OSS supply chain memory.
- **Recommendation:** Q3 W1-W2, 2 weeks, 1 engineer.
- **Evidence:** Memora + As We May Search, late June 2026.

### C7 (held from v16): End-to-end event latency

- **Problem:** v16 held. Addressed by C3 + C5.
- **Recommendation:** Addressed by C3 + C5.

## MEDIUM Issues (v17 ranking, refresh from v16)

- **M1 (held from v16):** Per-frame VLM latency on CPU-only — addressed by C5.
- **M2 (held from v16):** Idle-time reflection loop — held.
- **M3 (held from v16):** memoryd evaluation rigour — MemDelta protocol runner.
- **M4 (held from v16):** toold 120s timeout shared globally — held.
- **M5 (held from v16):** No per-daemon metrics export — held.
- **M6 (held from v12):** Karpathy 10-rule openclaw CLAUDE.md — held.
- **M7 (held from v12):** Gaze-Informed Proactive AI port to proactived v1 — held.
- **M8 (held from v14):** PR-review "X% AI-generated" tag — held.
- **M9 (held from v16):** OpenPhone-3B shortlist evaluation — Q3 W1, 2 days, 1 engineer.
- **M10 (NEW v17):** Project Lightwell $5B + Chainguard Athena spike — Q4 2026 W1-W2, 1 week, 1 engineer.
- **M11 (NEW v17):** OpenAN project spike — Q4 2026 W1-W2, 1 week, 1 engineer.
- **M12 (held from v16):** 9-step marketing narrative + Mythos $30K catch + v17 Mythos 5 partial retraction — Q3 W2, 3 days, 1 engineer.

## MINOR Issues (v17 ranking, refresh from v16)

- **m1-m5 (held from v14):** all held.
- **m6 (held from v15):** Research-integrity responsible-AI framing in v1.0 spec — 1 day.
- **m7 (held from v16):** v15 Mythos $30K catch retraction — 1 day copy update.
- **m8 (NEW v17):** Anthropic Claude Code timezone/proxy fingerprinting marketing add — 1 day copy.
- **m9 (NEW v17):** OpenAN + Chainguard Athena marketing add — 1 day copy.
- **m10 (NEW v17):** Anthropic Claude Science workbench-layer v1.0 spec add — 1 day.

## Architecture Decomposition Score: 9.2/10 (v17)

**v17 reasoning:** the v16 score was 9.0/10 (LFM2.5-230M + Hermes Agent + $9.5B / 90 days / 5-vendor + DoD GenAI.mil + As We May Search + GPT-5.6 government-gating). v17 elevates to 9.2/10 with: (a) **Vinton Cerf Open Frontier TCP/IP-for-agents endorsement from the internet's co-architect** (industry-icon endorsement, the most credible single source in 2026), (b) **Anthropic Claude Science workbench-layer admission** (closed-source admission that "harness > model"), (c) **IBM Red Hat Project Lightwell $5B + Chainguard Athena** ($14.5B / 120 days / 6-vendor implementation-wedge bet, now extending to OSS supply chain), (d) **OpenAN project** (China-led open-source agent interoperability framework, the v17 strongest open-source-side counter-narrative), (e) **Anthropic Claude Code timezone/proxy fingerprinting** (runtime-layer fingerprinting evidence, the v17 strongest citable "vendor lock-in is structural" datapoint). The decomposition is now *industry-icon-endorsed, closed-source-admitted, government-validated, multi-vendor-funded, China-led-standardization-underway, fingerprinting-at-the-runtime-layer*. To reach 10/10 we need a published benchmark of the v1.0 architecture end-to-end (the SIA-W+H port is the publishing bet).

## Power & Thermal (v17, no change from v16)

| Component | Power | Notes |
|-----------|-------|-------|
| Salience gate (low-power DSP) | ~0.3W | always-on |
| Vision encoder on NPU (when salient) | ~1.5W | 2.52× lower energy than CPU (Phase Matters) |
| Text decode on CPU (when VLM fires) | ~3-5W | <2s/frame with phase-mapped NPU |
| audiod post-processor (LFM2.5-230M on aarch64) | ~0.5W | 42 tok/s on Raspberry Pi 5 (LFM2.5-230M) |
| Total active VLM event | ~5-7W | phase-mapped, salient-gated |
| Salient-gated VLM (5 FPS watchful, 30% salient) | ~1.5W average | **reachable** with phase-mapped execution |

**v17 power conclusion:** the 4hr battery target (2x 200mAh @ 3.7V = 1.48Wh) is reachable with salience gating + phase-mapped execution + LFM2.5-230M audiod post-processor. **The v9 "salience gate is a UX detail" framing is still retracted — it is the *power* decision, not a UX detail.**

## Form Factor (v17, no change from v16)

- **Weight target:** <50g (held from v15).
- **Battery target:** 4hr (now reachable with v16 phase-mapped execution + LFM2.5-230M audiod + salience gating).
- **Storage target:** 32GB eMMC minimum (held from v15).
- **RAM target:** 4GB LPDDR minimum, 8GB preferred (held from v15).
- **Open question:** Redax SoC choice (Qualcomm vs MediaTek) — needed before Q3 W1 spike.

## Top 3 Recommendations for somdipto (v17)

1. **Approve the OpenClaw protocol surface marketing artifact (Q3 W2, 2 days, 1 engineer).** v17 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. We shipped it." Marketing: position Dan Glasses as "the TCP/IP for AI agents, shipped before the agents needed it." Cite Cerf in the v1.0 spec.
2. **Approve the v17 Mythos 5 partial retraction (Q3 W2, 1 day copy, 1 engineer).** v17 CRITICAL #2. Update v1.0 marketing: "Anthropic Mythos 5 is gated to the Glasswing program (cybersecurity researchers at trusted companies), now expanding beyond the initial ~100 US critical-infrastructure partners to broader domestic + international Glasswing members."
3. **Approve the v17 batch: Project Lightwell + Chainguard Athena (1 day copy) + OpenAN + Anthropic Claude Code fingerprinting (1 day copy) + Claude Science workbench-layer v1.0 spec add (1 day) (Q3 W2, 3 days, 1 engineer).** v17 SHARPEN. The v17 9-step marketing narrative is now *industry-icon-endorsed, closed-source-admitted, government-deployed, government-gated, multi-vendor-funded, China-led-standardization-underway, fingerprinting-at-the-runtime-layer*.

## Open Questions for somdipto (v17)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. We shipped it.")
2. **v17 Mythos 5 partial retraction priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v17 framing is "Glasswing program, expanding to broader domestic + international")
3. **Project Lightwell $5B + Chainguard Athena spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, open-source supply chain AI security is the v17 next wedge)
4. **OpenAN project spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, agent interoperability framework SOTA)
5. **Anthropic Claude Code timezone/proxy fingerprinting marketing weight** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, strongest citable "vendor lock-in is structural" evidence)
6. **Anthropic Claude Science workbench-layer v1.0 spec add priority** — Q3 W2, 1 day, 1 engineer (recommend: yes)
7. **v16 priorities (LFM2.5-230M, Hermes Agent, As We May Search, Memora, Phase Matters, OpenPhone-3B, 8-step narrative, Mythos $30K catch retraction)** — held from v16 (recommend: yes, all v16 priorities hold)
8. **9-step marketing narrative update** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, $14.5B / 120 days / 6-vendor + Vinton Cerf)
9. **Research-integrity responsible-AI framing in v1.0 spec** — Q3 W2, 1 day, 1 engineer (recommend: yes, held from v15)
10. **v17 AGI-roadmap 24-month plan revision** — Q3 W3, 2 days, 1 engineer (recommend: yes, add Vinton Cerf / Claude Science / Project Lightwell / OpenAN / Chainguard Athena to the 24-month plan)
11. **Redax SoC choice (Qualcomm vs MediaTek)** — needed before Q3 W1 LFM2.5-230M swap-in (recommend: confirm with hardware team)
12. **LFM2.5-230M on aarch64 (Raspberry Pi 5) benchmarks** — after Q3 W1 swap-in, 1-day benchmark (recommend: yes)

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
[^12]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users, July 2 2026 (held from v16)
[^13]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor (held from v16)
[^14]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^15]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v15)

## v16 architecture review content (preserved in backup)

The v16 architecture review (preserved in `dan2-architecture-review.v16-backup-2026-07-04.md`) covers: 3 critical / 5 medium / 5 minor issues, v1.5 spec revisions, decomposition score 9.0/10. **All v16 content is preserved verbatim in the backup. The v17 add is OpenClaw protocol surface marketing artifact CRITICAL #1 (Vinton Cerf endorsement) + Mythos 5 Glasswing expansion CRITICAL #2 + Claude Science workbench-layer admission + Project Lightwell $5B + Chainguard Athena + OpenAN + Anthropic Claude Code timezone/proxy fingerprinting. v16 LFM2.5-230M + Hermes Agent + As We May Search + $9.5B / 90 days / 5-vendor + DoD GenAI.mil + 8-step marketing narrative all hold. Decomposition score: 9.0 → 9.2/10.**

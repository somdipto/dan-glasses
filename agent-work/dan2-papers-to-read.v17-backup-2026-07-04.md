# Dan2 — Papers to Read v17 (2026-07-04 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v16:** `dan2-papers-to-read.v16-backup-2026-07-04.md`

> **v17 deltas vs v16 (0 top-5 adds, 1 honorable mention add, 0 demotions, 0 retractions):**
> 1. **NEW — Honorable mention: Vinton Cerf "TCP/IP for agents" speech (Laude Institute Open Frontier, June 30 2026).** Industry-icon endorsement of agent standardization protocols. Not a paper per se, but a 1-hour keynote that's the v17 strongest possible citable evidence for the OpenClaw v1.0 protocol surface. Read before the Q3 W2 OpenClaw protocol surface marketing artifact spike.
> 2. **NEW — Honorable mention: Anthropic Claude Science (MobiHealthNews, June 30 2026).** Closed-source admission that "harness > model." Not a paper, but a v17 evidence that the Dan Glasses OpenClaw + audiod + perceptiond + memoryd + ttsd + toold composition is the v17 on-device, open-weights analog of Claude Science.
> 3. **NEW — Honorable mention: IBM Red Hat Project Lightwell (Dark Reading, late June 2026) + Chainguard Athena (Let's Data Science, late June 2026).** $5B Project Lightwell + 20,000 engineers. Athena: 20+ orgs, 20,000+ findings, 2,000+ patches. Not papers, but v17 evidence that "implementation, not models" is now the entire enterprise AI market's bet, including the open-source supply chain.
> 4. **NEW — Honorable mention: OpenAN project (MWC Shanghai 2026, late June 2026).** China-led open-source agent interoperability framework (Linux Foundation Networking). The first published, multi-vendor open-source agent framework.

> **v17 retractions of v16:** **none.** The v16 top-5 holds (Phase Matters, Memora, Red Queen Gödel Machine, SIA, As We May Search). All v16 honorable mentions held.

## TL;DR (one paragraph, v17)

The v16 top-5 holds: (1) Phase Matters, (2) Memora, (3) Red Queen Gödel Machine, (4) SIA, (5) As We May Search. v17 adds 4 honorable mentions (Vinton Cerf keynote, Claude Science, Project Lightwell + Athena, OpenAN) — none is a paper, all are v17 evidence that the v16 model choices + the OpenClaw v1.0 protocol surface are the v17 SOTA. **The v17 reading list centers on: (1) Phase Matters + As We May Search for v1.0/v1.5 architecture, (2) SIA + Red Queen for v1.5/v2.0 agent loop, (3) Memora for v1.5 memoryd, (4) Hermes Agent + LFM2.5-230M for v1.0 audiod, (5) Vinton Cerf keynote + Claude Science + Project Lightwell + OpenAN for v1.0 marketing narrative.** HRM-Text-1B held as honorable mention. No v16 paper is retracted.

## Top 5 Papers to Read (v17 ranking, unchanged from v16)

### 1. "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC" (arXiv 2606.27906, late June 2026) — held from v15 #1
- **Why this paper:** The v1.0 wearable execution substrate is now defined. NPU prefill 1.64× faster than CPU, NPU decode 1.18× faster, vision encoders 2.52× lower energy on NPU. Always-on mobile VLM is feasible with careful NPU offload.
- **Key takeaway:** VLM inference on a phone SoC requires phase-mapped heterogeneous NPU/CPU/GPU inference, not "small model on CPU." The 4hr battery target is now reachable.
- **What we will do with it:** 1-week Q3 W1 `perceptiond.phase_map` architecture spike.
- **Effort to read:** 30 minutes.
- **Link:** https://arxiv.org/html/2606.27906v1.

### 2. "Microsoft Memora" (Microsoft Research, July 2026) — held from v14 #1
- **Why this paper:** The v1.5 memoryd architecture target. Decouples "what is stored" from "how it is retrieved." Reduces context token usage by up to 98% while matching or exceeding full-context accuracy.
- **Key takeaway:** Rich procedural memories stored with full embedding vectors; lightweight semantic abstractions stored with indexable keys; retrieval via a 2-stage pipeline.
- **What we will do with it:** 2-week Q3 W1-W2 memoryd v1.5 port.
- **Effort to read:** 1 hour.
- **Link:** https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity.

### 3. "Red Queen Gödel Machine" (arXiv 2606.26294, June 24 2026) — held from v12 #3
- **Why this paper:** The 2026 strongest paper for self-improving agents. The 1.91× → ~1.0× bias-correction result on the moving-judge pattern.
- **Key takeaway:** The agent can self-improve by changing its own judge. The "moving-judge" pattern is the implementation of the v11 `auto_apply=False` contract.
- **What we will do with it:** Port to danlab-multimodal as the v1.5 plan-A for the agent loop.
- **Effort to read:** 2 hours.
- **Link:** https://arxiv.org/abs/2606.26294.

### 4. "SIA: Self-Improving AI with Harness & Weight Updates" (Hexo Labs, MIT, June 2026) — held from v11
- **Why this paper:** The SIA framework is the open-weights, MIT-licensed self-improving agent pattern. The SIA-W+H (with hindsight) port is the v1.5 publishing bet.
- **Key takeaway:** Self-improving loop where a Feedback-Agent updates both the harness and the weights. Beats Karpathy's autoresearcher agent by improving itself.
- **What we will do with it:** Q3 W3-Q4 W2 SIA-W+H port. arXiv draft + ICML/ACL 2027 submission.
- **Effort to read:** 1.5 hours.
- **Link:** https://github.com/HexoLabs/sia.

### 5. "As We May Search: Local-First Information Retrieval" (arXiv 2606.29652, late June 2026) — held from v16
- **Why this paper:** Academic local-first IR validation. Dense retrieval keeps over 91% nDCG@10 up to 100K documents; approximate HNSW indexes extend to 1M with only 2% quality loss; 7B local language model reaches within 4 points of a cloud baseline on answer quality.
- **Key takeaway:** The on-device memoryd architecture is now an *empirical certainty*. Memora + As We May Search = the storage/retrieval split is the 2026 SOTA.
- **What we will do with it:** Cite in v1.0 marketing as the academic validation of on-device memory.
- **Effort to read:** 1 hour.
- **Link:** https://arxiv.org/abs/2606.29652.

## Honorable Mentions (v17)

1. **"LFM2.5-230M Technical Report" (Liquid AI, June 26 2026).** 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5. Beats Qwen3.5-0.8B and Gemma 3 1B. v1.0 audiod post-processor. Held from v16.
2. **"Hermes Agent" (Nous Research, late June 2026).** Mixture-of-agents pattern. 11% higher than GPT-5.5 on hard agentic benchmarks. v1.0 audiod agent framework plan-A. Held from v16.
3. **"EPFL MiCRo: Mixture of Cognitive Reasoners" (late June 2026).** Validates the 4-specialized-brain-region pattern. Held from v14.
4. **"VisualClaw: Self-Evolving Multimodal Agent for AI Glasses" (Mervin Praison, June 2026).** 98% cost reduction + +15.8% accuracy. The cascade-gate pattern. Held from v8.
5. **"Diagnosing the Memory-Update Gap" (arXiv 2606.27472, June 2026).** Frontier models drop 92% → 77% on supersession tasks. Held from v8.
6. **"Ollie: Gaze-Informed Proactive AI" (arXiv 2607.00445, July 1 2026).** The v12 proactived v1 architecture source. Held from v12.
7. **"Apertus v1.1 4B Instruct" (Swiss AI / EPFL, June 29 2026).** EU-provenance open-weights. v1.5 audiod post-processor plan-C. Held from v14.
8. **"OpenPhone-3B" (HKUDS, ACL 2026, late June 2026).** 3B on-device agentic foundation model. v1.5 audiod post-processor plan-D. Held from v15.
9. **"HRM-Text-1B" (Sapient, June 2026).** $1,500 trained, 1B params, Apache-2.0. v1.5 plan-B. Held from v15 (demoted from top-5 in v16).
10. **"Anthropic Mythos 5 + Fable 5 export ban lifted" (US Commerce Department, June 30 - July 1 2026).** Industry signal, not a paper. Fable 5 now globally available; Mythos 5 partially open to Glasswing + broader domestic + international members. **v17 partial retraction of v16's "$30K catch" framing and v16's "~100 US critical-infrastructure partners" framing.**
11. **NEW v17: Vinton Cerf keynote (Laude Institute Open Frontier, June 30 2026).** Industry-icon endorsement of the "TCP/IP-for-agents" pattern. Read before the Q3 W2 OpenClaw protocol surface marketing artifact spike. 1 hour.
12. **NEW v17: Anthropic Claude Science (MobiHealthNews, June 30 2026).** Closed-source admission that "harness > model." Read before the Q3 W2 v1.0 spec safety-considerations section update. 30 minutes.
13. **NEW v17: IBM Red Hat Project Lightwell (Dark Reading, late June 2026) + Chainguard Athena (Let's Data Science, late June 2026).** $5B Project Lightwell + 20,000 engineers + 20+ orgs Athena coalition. Read before the Q3 W2 9-step marketing narrative update. 1 hour.
14. **NEW v17: OpenAN project (MWC Shanghai 2026, late June 2026).** China-led open-source agent interoperability framework (Linux Foundation Networking). Read before the Q4 W1-W2 OpenAN spike. 1 hour.
15. **NEW v17: "The Month AI Governance Became Operational" (HackerNoon, June 2026).** v17 evidence that "AI advantage is shifting from who can build the best model to who can control the conditions under which model capability is accessed, secured, powered, deployed, and converted into institutional capacity." Read before the Q3 W2 9-step marketing narrative update. 1 hour.
16. **NEW v17: "Anthropic Tightens Controls Over Model Access" (Let's Data Science, late June 2026).** Anthropic Claude Code timezone/proxy fingerprinting evidence. v17 strongest possible citable "vendor lock-in is structural" evidence. Read before the Q3 W2 9-step marketing narrative update. 30 minutes.

## v17 Open Questions for somdipto

1. **Vinton Cerf keynote — read before Q3 W2 OpenClaw protocol surface marketing artifact spike?** (recommend: yes, 1 hour, before Q3 W2)
2. **Anthropic Claude Science — read before Q3 W2 v1.0 spec safety-considerations section update?** (recommend: yes, 30 minutes, before Q3 W2)
3. **IBM Red Hat Project Lightwell + Chainguard Athena — read before Q3 W2 9-step marketing narrative update?** (recommend: yes, 1 hour, before Q3 W2)
4. **OpenAN project — read before Q4 W1-W2 OpenAN spike?** (recommend: yes, 1 hour, before Q4 W1)
5. **Anthropic Claude Code timezone/proxy fingerprinting — read before Q3 W2 9-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
6. **"The Month AI Governance Became Operational" — read before Q3 W2 9-step marketing narrative update?** (recommend: yes, 1 hour, before Q3 W2)
7. **Phase Matters (v15 #1) — read before Q3 W1 phase_map spike starts?** (recommend: yes, 30 minutes, before Q3 W1)
8. **As We May Search (v16 #5) — read before Q3 W1-W2 Memora port starts?** (recommend: yes, 1 hour, before Q3 W1)
9. **Red Queen Gödel Machine (v12 #3) — port to danlab-multimodal in Q4 2026?** (recommend: yes, 4 weeks, 1 engineer)
10. **v17 24-month plan: add Project Lightwell + OpenAN partner-product evaluation?** (recommend: yes, Q4 2027, 1 quarter, 2 engineers)
11. **v17 9-step marketing narrative update priority?** (recommend: yes, Q3 W2, 1 day copy, 1 engineer)
12. **HRM-Text-1B / Apertus v1.1 4B / OpenPhone-3B v1.5 plan-B/C/D order** — held from v16 (recommend: hold order, they are v1.5 candidates, LFM2.5-230M is v1.0)

## Footnotes (v17)

[^1]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier keynote, June 30 2026 (NEW v17)
[^2]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026 (NEW v17)
[^3]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026 (NEW v17)
[^4]: https://www.letsdatascience.com/news/ai-scanners-expose-thousands-of-hidden-open-source-vulnerabi-420424be — Chainguard Athena coalition, late June 2026 (NEW v17)
[^5]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026 (NEW v17)
[^6]: https://hackernoon.com/the-month-ai-governance-became-operational — HackerNoon, "The Month AI Governance Became Operational," June 2026 (NEW v17)
[^7]: https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc — Anthropic Claude Code timezone/proxy fingerprinting, late June 2026 (NEW v17)
[^8]: https://arxiv.org/abs/2606.29652 — "As We May Search" (held from v16)
[^9]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^10]: https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity — Microsoft Memora (held from v14)
[^11]: https://arxiv.org/abs/2606.26294 — "Red Queen Gödel Machine" (held from v12)
[^12]: https://github.com/HexoLabs/sia — SIA (held from v11)
[^13]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M (held from v16)
[^14]: https://www.nousresearch.com/agents/hermes — Hermes Agent (held from v16)
[^15]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B (held from v15)

## v16 papers-to-read content (preserved in backup)

The v16 papers-to-read (preserved in `dan2-papers-to-read.v16-backup-2026-07-04.md`) covers: Phase Matters (top-5 #1), Memora (#2), Red Queen Gödel Machine (#3), SIA (#4), As We May Search (#5), plus 10 honorable mentions including LFM2.5-230M, Hermes Agent, MiCRo, VisualClaw, Diagnosing the Memory-Update Gap, Ollie, Apertus v1.1 4B, OpenPhone-3B, HRM-Text-1B, and the v16 Mythos 5 framing. **All v16 content is preserved verbatim in the backup. The v17 add is 4 new honorable mentions (Vinton Cerf keynote, Anthropic Claude Science, Project Lightwell + Athena, OpenAN) + 2 industry reads (HackerNoon, Anthropic Claude Code fingerprinting). The v16 top-5 holds unchanged. The v16 Mythos 5 framing is further partially retracted in v17 (now "Glasswing program, expanding to broader domestic + international").**

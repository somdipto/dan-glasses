# Dan2 — Papers to Read v18 (2026-07-04 13:00 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v17:** `dan2-papers-to-read.v17-backup-2026-07-04.md` (13.9KB, 110 lines)

> **v18 deltas vs v17 (0 top-5 adds, 4 honorable mention adds, 0 demotions, 0 retractions):**
> 1. **NEW — Honorable mention: Anthropic Claude Apps Gateway documentation (Anthropic + AWS + DevOps.com + Google Cloud, July 2 2026).** Self-hosted, stateless container, PostgreSQL backend, OIDC SSO, per-user cost attribution, OTLP audit logs, *published gateway protocol*. The v18 strongest possible citable evidence for the OpenClaw v1.0 protocol surface. Read before the Q3 W2 OpenClaw protocol surface marketing artifact spike. 1 hour.
> 2. **NEW — Honorable mention: OpenClaw iOS + Android documentation + security audit (9to5Google + Engadget + TechCrunch + Mashable, June 30 2026).** OpenClaw now ships native iOS + Android. The wearable-on-OpenClaw thesis is now native. Mashable flags a critical security flaw. Read before the Q3 W2 OpenClaw security audit spike. 1 hour.
> 3. **NEW — Honorable mention: Newsweek "Open Accountability Standards" (early July 2026).** Directly names OpenClaw as a popular open-source personal AI agent. v18 mainstream-press-acknowledged. Read before the Q3 W2 v18 10-step marketing narrative update. 30 minutes.
> 4. **NEW — Honorable mention: Atomathic Physical AI 2.0 white paper (Thailand Business News, July 1 2026).** "World Models → Physical State Recovery → Reasoning Systems → Action." The v18 academic validation of the Dan Glasses architectural pattern. Read before the Q3 W2 v1.0 spec architecture section update. 1 hour.

> **v18 retractions of v17:** **none.** The v17 top-5 holds (Phase Matters, Memora, Red Queen Gödel Machine, SIA, As We May Search). All v17 honorable mentions held. **v18 Time Magazine on Anthropic hedging RSI + v18 AIPOCH MedSkillAudit + v18 PagerDuty agent drift + v18 Proton Lumo 2.0 + v18 OpenAI GPT-5.6 Sol / Google Gemini 3.5 Flash / Anthropic Sonnet 5 closed-source agentic race + v18 Zuckerberg "slower than expected" + v18 OpenAI delays IPO to 2027 + v18 Apple 5 new iPhones + memory crunch + M6/M7 are added to the honorable mentions.**

## TL;DR (one paragraph, v18)

The v17 top-5 holds: (1) Phase Matters, (2) Memora, (3) Red Queen Gödel Machine, (4) SIA, (5) As We May Search. v18 adds 4 new honorable mentions (Anthropic Claude Apps Gateway, OpenClaw iOS + Android + security flaw, Newsweek "Open Accountability Standards," Atomathic Physical AI 2.0) + 8 industry reads (Time Magazine, AIPOCH MedSkillAudit, PagerDuty agent drift, Proton Lumo 2.0, OpenAI GPT-5.6 Sol / Google Gemini 3.5 Flash / Anthropic Sonnet 5, Zuckerberg "slower than expected," OpenAI delays IPO, Apple 5 new iPhones + memory crunch). **The v18 reading list centers on: (1) Phase Matters + As We May Search + Atomathic Physical AI 2.0 for v1.0/v1.5 architecture, (2) SIA + Red Queen for v1.5/v2.0 agent loop, (3) Memora for v1.5 memoryd, (4) Hermes Agent + LFM2.5-230M for v1.0 audiod, (5) Vinton Cerf keynote + Claude Science + Project Lightwell + OpenAN + Anthropic Claude Apps Gateway + OpenClaw mobile + Newsweek + Atomathic for v1.0 marketing narrative.** HRM-Text-1B held as honorable mention. No v17 paper is retracted.

## Top 5 Papers to Read (v18 ranking, unchanged from v17)

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

## Honorable Mentions (v18)

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
11. **Vinton Cerf keynote (Laude Institute Open Frontier, June 30 2026).** Industry-icon endorsement of the "TCP/IP-for-agents" pattern. Read before the Q3 W2 OpenClaw protocol surface marketing artifact spike. 1 hour. Held from v17.
12. **Anthropic Claude Science (MobiHealthNews, June 30 2026).** Closed-source admission that "harness > model." Read before the Q3 W2 v1.0 spec safety-considerations section update. 30 minutes. Held from v17.
13. **IBM Red Hat Project Lightwell (Dark Reading, late June 2026) + Chainguard Athena (Let's Data Science, late June 2026).** $5B Project Lightwell + 20,000 engineers + 20+ orgs Athena coalition. Read before the Q3 W2 9-step marketing narrative update. 1 hour. Held from v17.
14. **OpenAN project (MWC Shanghai 2026, late June 2026).** China-led open-source agent interoperability framework (Linux Foundation Networking). Read before the Q4 W1-W2 OpenAN spike. 1 hour. Held from v17.
15. **"The Month AI Governance Became Operational" (HackerNoon, June 2026).** v17 evidence that "AI advantage is shifting from who can build the best model to who can control the conditions under which model capability is accessed, secured, powered, deployed, and converted into institutional capacity." Read before the Q3 W2 9-step marketing narrative update. 1 hour. Held from v17.
16. **"Anthropic Tightens Controls Over Model Access" (Let's Data Science, late June 2026).** Anthropic Claude Code timezone/proxy fingerprinting evidence. v17 strongest possible citable "vendor lock-in is structural" evidence. Read before the Q3 W2 9-step marketing narrative update. 30 minutes. Held from v17.
17. **NEW v18: Anthropic Claude Apps Gateway documentation (Anthropic + AWS + DevOps.com + Google Cloud, July 2 2026).** Self-hosted, stateless container, PostgreSQL backend, OIDC SSO, per-user cost attribution, OTLP audit logs, *published gateway protocol*. The v18 strongest possible citable evidence for the OpenClaw v1.0 protocol surface. Read before the Q3 W2 OpenClaw protocol surface marketing artifact spike. 1 hour.
18. **NEW v18: OpenClaw iOS + Android documentation + security audit (9to5Google + Engadget + TechCrunch + Mashable, June 30 2026).** OpenClaw now ships native iOS + Android. Mashable flags a critical security flaw. Read before the Q3 W2 OpenClaw security audit spike. 1 hour.
19. **NEW v18: Newsweek "Open Accountability Standards" (early July 2026).** Directly names OpenClaw as a popular open-source personal AI agent. v18 mainstream-press-acknowledged. Read before the Q3 W2 v18 10-step marketing narrative update. 30 minutes.
20. **NEW v18: Atomathic Physical AI 2.0 white paper (Thailand Business News, July 1 2026).** "World Models → Physical State Recovery → Reasoning Systems → Action." The v18 academic validation of the Dan Glasses architectural pattern. Read before the Q3 W2 v1.0 spec architecture section update. 1 hour.
21. **NEW v18: Time Magazine on RSI (June 29 2026).** Anthropic's Marina Favaro and Jack Clark publicly hedge: "We are not there yet, and recursive self-improvement is not inevitable." v18 strengthens the v16 SIA-W+H port publishing bet. Read before the Q3 W3 SIA-W+H port start. 30 minutes.
22. **NEW v18: AIPOCH MedSkillAudit (Business Insider, June 29 2026).** Pre-deployment medical AI audit framework. Two-layer veto gate: static (40%, design quality) + dynamic (60%, runtime performance). v18 cites for the v1.5 healthcare vertical. Read before the Q4 W1-W2 sovereign-on-prem vertical spike. 30 minutes.
23. **NEW v18: PagerDuty Jenn Tejada (Forbes, July 2 2026) on agent drift + $725B AI infra spend (BNP Paribas).** "Model drift in AI agents is harder to detect than a traditional software crash." v18 cites for the v1.0 spec safety-considerations section. Read before the Q3 W2 spec update. 30 minutes.
24. **NEW v18: Proton Lumo 2.0 (9to5Mac, June 30 2026).** Privacy-preserving AI with persistent memory. Lumo 2.0 Max scores 240% higher than Lumo 1.4. v18 cites for the v1.0 marketing privacy-harness analog. Read before the Q3 W2 10-step marketing narrative update. 30 minutes.
25. **NEW v18: OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race (TechCrunch + 9to5Mac + Axios, June-July 2026).** All three labs shipped agentic models in May-July 2026, all behind closed APIs. v18 cites for the v1.0 marketing closed-source-agentic-race frame. Read before the Q3 W2 10-step marketing narrative update. 1 hour.
26. **NEW v18: Zuckerberg "slower than expected" (Reuters + TechCrunch + Bloomberg + CNN + Forbes, July 2 2026).** "The trajectory of agentic AI development over the last four months hasn't accelerated as hoped." v18 cites for the v1.0 marketing closed-source-failing frame. Read before the Q3 W2 10-step marketing narrative update. 30 minutes.
27. **NEW v18: OpenAI delays IPO to 2027, Anthropic $965B (Forbes, June 28 2026).** v18 cites for the v1.0 marketing $1T-class implementation-wedge frame. Read before the Q3 W2 10-step marketing narrative update. 30 minutes.
28. **NEW v18: Apple 5 new iPhones + memory crunch + M6/M7 plans (Nikkei + CNBC + Bloomberg, June-July 2026).** v18 cites for the v1.0 wearable form-factor supply-chain-pressure frame. Read before the Q3 W2 10-step marketing narrative update. 30 minutes.

## v18 Open Questions for somdipto

1. **Anthropic Claude Apps Gateway documentation — read before Q3 W2 OpenClaw protocol surface marketing artifact spike?** (recommend: yes, 1 hour, before Q3 W2)
2. **OpenClaw iOS + Android documentation + security audit — read before Q3 W2 OpenClaw security audit spike?** (recommend: yes, 1 hour, before Q3 W2)
3. **Newsweek "Open Accountability Standards" — read before Q3 W2 v18 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
4. **Atomathic Physical AI 2.0 — read before Q3 W2 v1.0 spec architecture section update?** (recommend: yes, 1 hour, before Q3 W2)
5. **Time Magazine on RSI — read before Q3 W3 SIA-W+H port start?** (recommend: yes, 30 minutes, before Q3 W3)
6. **AIPOCH MedSkillAudit — read before Q4 W1-W2 sovereign-on-prem vertical spike?** (recommend: yes, 30 minutes, before Q4 W1)
7. **PagerDuty Jenn Tejada — read before Q3 W2 v1.0 spec safety-considerations section update?** (recommend: yes, 30 minutes, before Q3 W2)
8. **Proton Lumo 2.0 — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
9. **OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 1 hour, before Q3 W2)
10. **Zuckerberg "slower than expected" — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
11. **OpenAI delays IPO + Anthropic $965B — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
12. **Apple 5 new iPhones + memory crunch + M6/M7 — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
13. **Phase Matters (v15 #1) — read before Q3 W1 phase_map spike starts?** (recommend: yes, 30 minutes, before Q3 W1)
14. **As We May Search (v16 #5) — read before Q3 W1-W2 Memora port starts?** (recommend: yes, 1 hour, before Q3 W1)
15. **Red Queen Gödel Machine (v12 #3) — port to danlab-multimodal in Q4 2026?** (recommend: yes, 4 weeks, 1 engineer)
16. **v18 24-month plan: AIPOCH-augmented sovereign-on-prem vertical + Project Lightwell + OpenAN partner-product evaluation?** (recommend: yes, Q4 2027, 1 quarter, 2 engineers)
17. **v18 10-step marketing narrative update priority?** (recommend: yes, Q3 W2, 1 day copy, 1 engineer)
18. **HRM-Text-1B / Apertus v1.1 4B / OpenPhone-3B v1.5 plan-B/C/D order** — held from v16 (recommend: hold order, they are v1.5 candidates, LFM2.5-230M is v1.0)

## Footnotes (v18)

[^1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Apps Gateway + Sonnet 5, July 2 2026 (NEW v18)
[^2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (NEW v18)
[^3]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw, June 30 2026 (NEW v18)
[^4]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (NEW v18)
[^5]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (NEW v18)
[^6]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI, June 29 2026 (NEW v18)
[^7]: https://markets.businessinsider.com/news/stocks/aipoch-launches-medskillaudit-an-ai-audit-framework-to-evaluate-medical-ai-agent-skills-before-deployment-1036284741 — AIPOCH MedSkillAudit, June 29 2026 (NEW v18)
[^8]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (NEW v18)
[^9]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (NEW v18)
[^10]: https://www.forbes.com/sites/sandycarter/2026/06/28/openai-eyes-2027-ipo-delay-as-washington-clears-anthropics-mythos-5/ — OpenAI delays IPO + Anthropic $965B, June 28 2026 (NEW v18)
[^11]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier keynote, June 30 2026 (held from v17)
[^12]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026 (held from v17)
[^13]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026 (held from v17)
[^14]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026 (held from v17)
[^15]: https://hackernoon.com/the-month-ai-governance-became-operational — HackerNoon, "The Month AI Governance Became Operational," June 2026 (held from v17)
[^16]: https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc — Anthropic Claude Code timezone/proxy fingerprinting, late June 2026 (held from v17)
[^17]: https://arxiv.org/abs/2606.29652 — "As We May Search" (held from v16)
[^18]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^19]: https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity — Microsoft Memora (held from v14)
[^20]: https://arxiv.org/abs/2606.26294 — "Red Queen Gödel Machine" (held from v12)
[^21]: https://github.com/HexoLabs/sia — SIA (held from v11)
[^22]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M (held from v16)
[^23]: https://www.nousresearch.com/agents/hermes — Hermes Agent (held from v16)
[^24]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B (held from v15)

## v17 papers-to-read content (preserved in backup)

The v17 papers-to-read (preserved in `dan2-papers-to-read.v17-backup-2026-07-04.md`) covers: Phase Matters (top-5 #1), Memora (#2), Red Queen Gödel Machine (#3), SIA (#4), As We May Search (#5), plus 10 honorable mentions including LFM2.5-230M, Hermes Agent, MiCRo, VisualClaw, Diagnosing the Memory-Update Gap, Ollie, Apertus v1.1 4B, OpenPhone-3B, HRM-Text-1B, and the v16 Mythos 5 framing, plus 4 v17 honorable mentions (Vinton Cerf keynote, Anthropic Claude Science, Project Lightwell + Athena, OpenAN) + 2 industry reads (HackerNoon, Anthropic Claude Code fingerprinting). **All v17 content is preserved verbatim in the backup. The v18 add is 4 new honorable mentions (Anthropic Claude Apps Gateway, OpenClaw iOS + Android + security flaw, Newsweek "Open Accountability Standards," Atomathic Physical AI 2.0) + 8 industry reads (Time Magazine, AIPOCH MedSkillAudit, PagerDuty agent drift, Proton Lumo 2.0, OpenAI GPT-5.6 / Google Gemini 3.5 Flash / Anthropic Sonnet 5, Zuckerberg "slower than expected," OpenAI delays IPO + Anthropic $965B, Apple 5 new iPhones + memory crunch + M6/M7). The v17 top-5 holds unchanged.**

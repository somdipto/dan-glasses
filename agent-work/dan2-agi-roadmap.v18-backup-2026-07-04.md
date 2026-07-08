# Dan2 — AGI Roadmap v18 (2026-07-04 13:00 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v17:** `dan2-agi-roadmap.v17-backup-2026-07-04.md` (17.7KB, 222 lines)

> **v18 deltas vs v17 (3 CRITICAL adds, 3 SHARPEN, 0 partial retractions, 0 broad rollbacks):**
> 1. **NEW CRITICAL — Q3 W2: OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence (2 days copy + spec, 1 engineer).** v18 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable." (Vinton Cerf, Open Frontier, June 30 2026; Anthropic Claude Apps Gateway, July 2 2026).
> 2. **NEW CRITICAL — Q3 W2: OpenClaw security audit (1 day spike, 1 engineer).** v18 CRITICAL #2. Mashable (June 30 2026) reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. Audit OpenClaw's threat model before shipping the v1.0 marketing artifact.
> 3. **NEW CRITICAL — Q3 W2: v18 10-step marketing narrative + Newsweek "Open Accountability Standards" (1 day copy, 1 engineer).** v18 CRITICAL #3. v17 9-step + Newsweek = v18 10-step. Cite Newsweek in the v1.0 marketing as the mainstream-press acknowledgment that open-source agent standards are the structural solution.
> 4. **NEW SHARPEN — Q3 W2: OpenClaw native iOS + Android + wearable-on-OpenClaw thesis (1 day copy, 1 engineer).** v18 SHARPEN. "OpenClaw is the gateway. Dan Glasses is the wearable node." Add to the v1.0 spec architecture section.
> 5. **NEW SHARPEN — Q3 W2: Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" (1 day copy, 1 engineer).** v18 SHARPEN. v18 6-step v1.0 marketing batch.
> 6. **NEW SHARPEN — Q3 W2: PagerDuty agent drift + Atomathic Physical AI 2.0 (1 day copy + spec, 1 engineer).** v18 SHARPEN. "Observability > model" is the v18 structural answer. Cite Physical AI 2.0 in the v1.0 spec architecture section.

> **v18 retractions of v17:** **none.** All v17 6/12/24-month plan holds. The v16 Q3 W1 LFM2.5-230M audiod post-processor swap-in is held. The v17 Q3 W2 OpenClaw protocol surface marketing artifact is now the v18 Q3 W2 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence.

## TL;DR (one paragraph, v18)

The v17 6/12/24-month plan holds. **v18 adds: Q3 W2 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence (CRITICAL #1) + Q3 W2 OpenClaw security audit (CRITICAL #2) + Q3 W2 v18 10-step marketing narrative + Newsweek "Open Accountability Standards" (CRITICAL #3) + Q3 W2 OpenClaw mobile + wearable-on-OpenClaw thesis (SHARPEN) + Q3 W2 Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" (SHARPEN) + Q3 W2 PagerDuty agent drift + Atomathic Physical AI 2.0 (SHARPEN).** The Dan Glasses stack is structurally correct, validated at industry-icon level (Vinton Cerf, June 30 2026), validated at industry-shipped level (Anthropic Claude Apps Gateway, July 2 2026), validated at mainstream-press level (Newsweek, early July 2026), validated at industry-scale ($14.5B / 120 days / 6-vendor + $1T private valuations, v17/v18), government-deployed (DoD GenAI.mil 1.7M users), academically-validated (Phase Matters, As We May Search, EPFL MiCRo, Atomathic Physical AI 2.0, v18), and now has two strong v1.0 audiod targets (LFM2.5-230M post-processor + Hermes Agent agent framework) + an industry-icon-endorsed orchestration layer (OpenClaw, v17/v18) + a v18 mainstream-press-acknowledged "open accountability standards" wedge. **6-month plan: ship the v1.0 audiod post-processor with LFM2.5-230M, phase-mapped execution substrate, Hermes Agent agent framework, and the v18 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence. 12-month plan: ship the v1.5 audiod post-processor with HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-C) + OpenPhone-3B (plan-D) + Memora + As We May Search storage/retrieval split. 24-month plan: ship the SIA-W+H port as the open-source RSI play + sovereign-on-prem vertical for healthcare/defense (DoD-validated, AIPOCH MedSkillAudit-augmented) + LFM2.5-230M audiod for v1.0 wearable path + Project Lightwell + OpenAN agent interoperability.**

## 6-Month Plan (Q3 2026 - Q4 2026): v1.0 Wearable

### Q3 W1: LFM2.5-230M audiod post-processor swap-in (held from v16)
- **Effort:** 1-2 weeks, 1 engineer.
- **Deliverable:** audiod post-processor upgraded from LFM2.5-1.2B-Thinking to LFM2.5-230M. Benchmark on audiod post-processor workload.

### Q3 W1: `perceptiond.phase_map` architecture spike (held from v15)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** `perceptiond.phase_map` module. Pluggable backend (QNN/Hexagon on Snapdragon, Mali on others, CPU fallback).

### Q3 W1: OpenPhone-3B shortlist evaluation (held from v15)
- **Effort:** 2 days, 1 engineer.
- **Deliverable:** benchmark OpenPhone-3B vs HRM-Text-1B vs Apertus v1.1 4B on audiod post-processor workload.

### Q3 W1-W2: Memora + As We May Search memoryd v1.5 port (held from v14, v18 sharpening)
- **Effort:** 2 weeks, 1 engineer.
- **Deliverable:** memoryd v1.5 storage/retrieval split. New `/v1/retrieve` endpoint, new `/v1/abstractions` write path. Local-first HNSW at 1M document scale.

### Q3 W2: Hermes Agent v1.0 audiod agent framework plan-A spike (held from v16)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** Hermes Agent pattern ported to openclaw + audiod. Mixture-of-agents pattern.

### Q3 W2 (v18 CRITICAL #1): OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence
- **Effort:** 2 days, 1 engineer.
- **Deliverable:** document OpenClaw's protocol surface (JSON-RPC envelope, daemon health probes, kanban/issue trackers, gateway protocol, paperclip agent harness) as a v1.0 marketing artifact. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable." Cite Cerf + Anthropic Claude Apps Gateway in the v1.0 spec.
- **Evidence:** Vinton Cerf Open Frontier (June 30 2026) + Anthropic Claude Apps Gateway (July 2 2026).

### Q3 W2 (v18 CRITICAL #2): OpenClaw security audit (Mashable, June 30 2026)
- **Effort:** 1 day spike, 1 engineer.
- **Deliverable:** audit OpenClaw's threat model. Document the v18 known-flaw + audit response in the v1.0 spec safety-considerations section.
- **Evidence:** Mashable, June 30 2026.

### Q3 W2 (v18 CRITICAL #3): v18 10-step marketing narrative + Newsweek "Open Accountability Standards"
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 marketing page updated to the v18 10-step empirical narrative. Add Newsweek as the v18 10th step: "Newsweek open accountability standards — OpenClaw named, Anthropic gateway shipped, X MCP server shipped, the open-source agent protocol layer is now mainstream."

### Q3 W2 (v18 SHARPEN): OpenClaw native iOS + Android + wearable-on-OpenClaw thesis
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 spec architecture section updated. "OpenClaw is the gateway. Dan Glasses is the wearable node." Add to the v1.0 marketing.
- **Evidence:** 9to5Google + Engadget + TechCrunch + Mashable, June 30 2026.

### Q3 W2 (v18 SHARPEN): Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" copy
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 marketing copy updated. Cite Proton Lumo 2.0 (privacy harness on frontier model) + OpenAI GPT-5.6 Sol / Google Gemini 3.5 Flash / Anthropic Sonnet 5 (closed-source agentic race) + Zuckerberg "slower than expected" (closed-source frontier visibly failing).
- **Evidence:** 9to5Mac + TechCrunch + TechCrunch + Reuters + TechCrunch + Bloomberg + CNN + Forbes, June 30 - July 2 2026.

### Q3 W2 (v18 SHARPEN): PagerDuty agent drift + Atomathic Physical AI 2.0 spec + copy
- **Effort:** 1 day copy + 1 day spec, 1 engineer.
- **Deliverable:** v1.0 spec safety-considerations section updated. "Observability > model" is the v18 structural answer. Cite Atomathic Physical AI 2.0 in the v1.0 spec architecture section.
- **Evidence:** Forbes (PagerDuty) + Atomathic (Physical AI 2.0), July 1-2 2026.

### Q3 W2: 9-step → 10-step marketing narrative (v17 9-step + v18 10th step)
- **Effort:** 1 day copy, 1 engineer.

### Q3 W2: Project Lightwell $5B + Chainguard Athena copy update (held from v17)
- **Effort:** 1 day copy, 1 engineer.

### Q3 W2: OpenAN + Anthropic Claude Code fingerprinting copy update (held from v17)
- **Effort:** 1 day copy, 1 engineer.

### Q3 W2: Anthropic Claude Science workbench-layer v1.0 spec add (held from v17)
- **Effort:** 1 day, 1 engineer.

### Q3 W2: Research-integrity responsible-AI framing in v1.0 spec (held from v15)
- **Effort:** 1 day.

### Q3 W2: "As We May Search" paper read + memoryd v1.5 addendum (held from v16)
- **Effort:** 1 day.

### Q3 W2: v17 Mythos $30K catch retraction (held from v16)
- **Effort:** 1 day.

### Q3 W3-Q4 W2: SIA-W+H port (held from v11, v16 v1.5 publishing bet)
- **Effort:** 4 weeks, 1 engineer + $200-500/mo cloud GPU.
- **Deliverable:** SIA-W+H harness ported to OpenClaw + memoryd. arXiv draft. ICML 2027 / ACL 2027 submission.
- **v18 add:** v18 Time Magazine (June 29 2026) Anthropic hedging RSI strengthens the v17 SIA-W+H port recommendation. The open-source, MIT-licensed, auditable SIA-W+H pattern is the v18 only credible counter-narrative when the closed-source frontier is publicly hedging.

### Q3 W3: Red Queen moving-judge spike (held from v12)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** v1.5 danlab-multimodal implementation is the Red Queen moving-judge pattern.

### Q3 W3: Karpathy 10-rule openclaw CLAUDE.md (held from v12)
- **Effort:** 1 day.

### Q3 W3: openclaw PR-review "X% AI-generated" tag (held from v14)
- **Effort:** 3 days, 1 engineer.
- **v18 add:** v18 Godot Foundation AI code rules (June 30 2026) validate the v14 openclaw PR-review "X% AI-generated" tag direction. "X% AI-generated" tag, 3-day spike.

### Q3 W4: VisualClaw cascade-gate port (held from v8/v9)
- **Effort:** 1.5 weeks, 1 engineer.
- **Deliverable:** perceptiond + memoryd port the VisualClaw on-device cascade-gate pattern.

### Q4 W1-W2: Anthropic Dreaming port (held from v8/v11)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** openclaw + memoryd port the Anthropic Dreaming `auto_apply=False` + `session_limit=50` pattern.

### Q4 W1-W2: Sovereign-on-prem vertical spike (held from v13, v17 DoD-validated, v18 AIPOCH-augmented)
- **Effort:** 1 engineer-week.
- **Deliverable:** Q4 2026 spike for healthcare/defense vertical. Palantir+NVIDIA Nemotron + DoD GenAI.mil template co-positioning. **v18 add: cite AIPOCH MedSkillAudit (June 29 2026) as the v18 pre-deployment medical AI audit framework for healthcare vertical.**

### Q4 W1-W2: Project Lightwell $5B + Chainguard Athena spike (held from v17)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** evaluate the v17 open-source supply chain AI security stack. Open-source supply chain memory + workbench + agent framework. Cite in v1.5 product roadmap.
- **Evidence:** Dark Reading + Let's Data Science, late June 2026.

### Q4 W1-W2: OpenAN agent interoperability framework spike (held from v17)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** evaluate the v17 OpenAN agent interoperability framework. Multi-agent coordination, AI-native autonomous networks (Level 4 autonomy). Cite in v1.5 product roadmap.
- **Evidence:** Developing Telecoms, late June 2026.

### Q4 W3-W4: v1.0 wearable hardware integration
- **Effort:** 2 weeks, hardware + 1 engineer.
- **Deliverable:** Redax board integration, camera module, thermal validation, battery characterization.

## 12-Month Plan (Q1 2027 - Q2 2027): v1.5 Cognitive Stack

### Q1 W1-W2: HRM-Text-1B swap-in (v1.5 plan-B)
- **Effort:** 2 weeks, 1 engineer. (held from v11, displaced from v1.0 plan-A to v1.5 plan-B by LFM2.5-230M in v16)

### Q1 W3: Apertus v1.1 4B EU data-residency ship-gate (v1.5 plan-C)
- **Effort:** 1 week, 1 engineer.

### Q1 W4: OpenPhone-3B plan-D integration
- **Effort:** 1 week, 1 engineer.

### Q2 W1-W2: Qwen3-TTS v1.5 plan-A swap-in
- **Effort:** 2 weeks, 1 engineer.

### Q2 W2: Chatterbox voice-cloning plan-A
- **Effort:** 1 week, 1 engineer.

### Q2 W3-W4: LFM2.5-VL-450M-Extract structured-output VLM
- **Effort:** 2 weeks, 1 engineer.

### Q2 W4: Ollie gaze-informed proactive v1 (held from v12)
- **Effort:** 1 week, 1 engineer.

## 24-Month Plan (Q3 2027 - Q4 2027): SIA-W+H RSI Play + DoD Vertical + Project Lightwell + OpenAN

### Q3 2027: SIA-W+H publication + ICML 2027 / ACL 2027
- **Effort:** 4 weeks, 1 engineer.
- **Deliverable:** arXiv draft + ICML 2027 / ACL 2027 submission.
- **v18 add:** v18 Time Magazine (June 29 2026) Anthropic hedging RSI strengthens the v16 SIA-W+H port recommendation. The open-source, MIT-licensed, auditable SIA-W+H pattern is the v18 only credible counter-narrative when the closed-source frontier is publicly hedging.

### Q4 2027: Sovereign-on-prem vertical product launch (DoD-validated, AIPOCH-augmented)
- **Effort:** 1 quarter, 3 engineers.
- **Deliverable:** healthcare/defense sovereign-on-prem product. **v18 add: cite DoD GenAI.mil 1.7M users + 100K custom agents as the v17 DoD-deployed template + AIPOCH MedSkillAudit as the v18 pre-deployment medical AI audit framework.**

### Q4 2027: Compliance mode v2.0
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** HIPAA / FedRAMP compliance mode for healthcare/defense verticals.

### Q4 2027: Project Lightwell + OpenAN partner-product evaluation (held from v17)
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** evaluate partner-product opportunities with IBM Red Hat Project Lightwell + OpenAN consortium. Cite in v2.0 product roadmap.

## Top 3 Recommendations for somdipto (v18)

1. **Approve the Q3 W2 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence (2 days copy + spec, 1 engineer).** v18 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable."
2. **Approve the Q3 W2 OpenClaw security audit (1 day spike, 1 engineer).** v18 CRITICAL #2. Mashable (June 30 2026) reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. Audit OpenClaw's threat model before shipping the v1.0 marketing artifact.
3. **Approve the Q3 W2 v18 batch: v18 10-step marketing narrative + Newsweek "Open Accountability Standards" (1 day) + OpenClaw mobile + wearable-on-OpenClaw thesis (1 day) + Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" (1 day) + PagerDuty agent drift + Atomathic Physical AI 2.0 (1 day) (Q3 W2, 4 days, 1 engineer).** v18 SHARPEN. **v18 add: total 4 days, 10-step marketing narrative + mainstream-press-acknowledged + closed-source-admitted + industry-icon-endorsed + government-deployed + government-gated + multi-vendor-funded + China-led-standardization-underway + fingerprinting-at-the-runtime-layer + observability-first + supply-chain-pressured.**

## Open Questions for somdipto (v18)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable.")
2. **OpenClaw security audit priority** — Q3 W2, 1 day spike, 1 engineer (recommend: yes, Mashable v18 known-flaw)
3. **v18 10-step marketing narrative update + Newsweek priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v18 10-step)
4. **OpenClaw mobile + wearable-on-OpenClaw thesis copy priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, "OpenClaw is the gateway. Dan Glasses is the wearable node.")
5. **Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" copy priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v18 6-step v1.0 marketing batch)
6. **PagerDuty agent drift + Atomathic Physical AI 2.0 spec + copy priority** — Q3 W2, 1 day copy + 1 day spec, 1 engineer (recommend: yes, "Observability > model" is the v18 structural answer)
7. **Project Lightwell $5B + Chainguard Athena spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, open-source supply chain AI security is the v17 next wedge)
8. **OpenAN agent interoperability framework spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, agent interoperability framework SOTA)
9. **LFM2.5-230M / Hermes Agent / As We May Search / Memora / Phase Matters v16 priorities** — held from v16 (recommend: yes, all v16 priorities hold)
10. **SIA-W+H port budget ($200-500/mo cloud GPU)** — Q3 W3-Q4 W2 (recommend: yes, v16 v1.5 publishing bet, v18 strengthened by Time Magazine Anthropic hedging RSI)
11. **Sovereign-on-prem vertical product launch timeline** — Q4 2027 (recommend: yes, DoD GenAI.mil template co-positioning + AIPOCH MedSkillAudit)
12. **v18 24-month plan: Project Lightwell + OpenAN partner-product evaluation** — Q4 2027, 1 quarter, 2 engineers (recommend: yes, v17 v2.0 vertical)

## Footnotes (v18)

[^1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Apps Gateway + Sonnet 5, July 2 2026 (NEW v18 CRITICAL #1)
[^2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (NEW v18 CRITICAL #2)
[^3]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw + iOS/Android, June 30 2026 (NEW v18 CRITICAL #2)
[^4]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (NEW v18 CRITICAL #3)
[^5]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (NEW v18 SHARPEN)
[^6]: https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ — Zuckerberg "slower than expected," July 2 2026 (NEW v18 SHARPEN)
[^7]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (NEW v18 SHARPEN)
[^8]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (NEW v18 SHARPEN)
[^9]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026 (held from v17)
[^10]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026 (held from v17)
[^11]: https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/ — Anthropic Mythos 5 Glasswing expansion, July 1 2026 (held from v17)
[^12]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026 (held from v17)
[^13]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026 (held from v17)
[^14]: https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc — Anthropic Claude Code timezone/proxy fingerprinting, late June 2026 (held from v17)
[^15]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^16]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^17]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^18]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^19]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users (held from v16)
[^20]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor (held from v16)
[^21]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v15)
[^22]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI hedging, June 29 2026 (NEW v18)
[^23]: https://markets.businessinsider.com/news/stocks/aipoch-launches-medskillaudit-an-ai-audit-framework-to-evaluate-medical-ai-agent-skills-before-deployment-1036284741 — AIPOCH MedSkillAudit, June 29 2026 (NEW v18)

## v17 AGI roadmap content (preserved in backup)

The v17 AGI roadmap (preserved in `dan2-agi-roadmap.v17-backup-2026-07-04.md`) covers: 6/12/24-month plan with Q3 W1 LFM2.5-230M audiod post-processor swap-in, Hermes Agent v1.0 audiod agent framework plan-A, 8-step marketing narrative, As We May Search paper read, Mythos $30K catch partial retraction, OpenClaw protocol surface marketing artifact CRITICAL #1, v17 Mythos 5 partial retraction CRITICAL #2, 9-step marketing narrative, Project Lightwell + Chainguard Athena + OpenAN + Claude Code fingerprinting + Claude Science workbench-layer v1.0 spec add. **All v17 content is preserved verbatim in the backup. The v18 add is OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence CRITICAL #1 + OpenClaw security audit CRITICAL #2 + v18 10-step marketing narrative + Newsweek "Open Accountability Standards" CRITICAL #3 + OpenClaw mobile + wearable-on-OpenClaw thesis SHARPEN + Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" SHARPEN + PagerDuty agent drift + Atomathic Physical AI 2.0 SHARPEN. The v17 6/12/24-month plan holds, with v18 24-month plan adding AIPOCH MedSkillAudit-augmented sovereign-on-prem vertical + SIA-W+H port strengthened by Time Magazine Anthropic hedging RSI.**

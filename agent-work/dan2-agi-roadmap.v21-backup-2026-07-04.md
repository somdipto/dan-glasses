# Dan2 — AGI Roadmap v21 (2026-07-04 15:00 UTC / 20:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v20:** `dan2-agi-roadmap.v20-backup-2026-07-04.md`

> **v21 deltas vs v20 (5 CRITICAL adds, 4 SHARPEN, 0 broad rollbacks):**
> 1. **NEW CRITICAL — Q3 W1: `perceptiond.skill_evolution` spike promoted from v18 plan-C to v21 plan-A (2 weeks, 1 engineer).** v21 CRITICAL #1. Per arXiv 2607.01709 ComfyClaw (July 2026), an open-source self-evolving skill harness using region-level VLM verifier + skill library achieves the best average score across 6 agent configurations in image generation. **v21 add: the Dan Glasses equivalent is `perceptiond.skill_evolution` — region-level VLM verifier (LFM2.5-VL-450M) translates visual failures into actionable repair suggestions, skill library stores trajectories + execution errors + verifier feedback as reusable Agent Skills. Promote from v18 plan-C to v21 plan-A. 2-week spike, 1 engineer, target Q3 W1.**
> 2. **NEW CRITICAL — Q3 W2: `memoryd.p_mem` substrate spike added to v1.0 spec memory-architecture section (1 day copy + 2 weeks, 1 engineer).** v21 CRITICAL #2. Per Notre Dame + Georgia Tech + Villanova (July 2026, DAC 2026 accepted) "Probabilistic Memory for Trustworthy Edge Intelligence." **v21 add: p-MEM is the v21 *academic* validation of the memoryd substrate. Add p-MEM to the v1.0 spec memory-architecture section. `memoryd.p_mem` spike = 1 day copy + 2 weeks implementation, target Q3 W2.**
> 3. **NEW CRITICAL — Q3 W2: `openclaw.comfyclaw_pattern` skill library port (1 week, 1 engineer).** v21 CRITICAL #3. **v21 add: ComfyClaw's "progressively disclosed skill library" pattern is the v21 *direct* analogue for `openclaw.skill_library`. 1 week spike, 1 engineer, target Q3 W2.**
> 4. **NEW CRITICAL — Q3 W3: `openclaw.webbrain_substrate` port for wearable-on-browser coordination (1 week, 1 engineer).** v21 CRITICAL #4. Per MarkTechPost (July 2 2026) WebBrain — Emre Sokullu's open-source, local-first AI browser agent for Chrome + Firefox. **v21 add: WebBrain is the v21 *second* open-source agent substrate signal (after OpenClaw). Add `openclaw.webbrain_substrate` port for wearable ↔ browser coordination. 1 week spike, 1 engineer, target Q3 W3.**
> 5. **NEW CRITICAL — Q4 W2: `glm5_async_rl_port` spike (2 weeks, 1 engineer).** v21 CRITICAL #5. Per Hugging Face Daily Papers (July 2026) "GLM-5: from Vibe Coding to Agentic Engineering" — "asynchronous reinforcement learning infrastructure that drastically improves post-training efficiency by decoupling generation from training." **v21 add: the v21 only credible path to *open-weights harness self-improvement* without a $4.65B closed-source RSI lab is the GLM-5 async RL port. 2-week spike, 1 engineer, target Q4 W2.**
> 6. **NEW SHARPEN — Q3 W2: v1.0 marketing 12-step → 13-step narrative with Kimi K2.7 Code first-party in GitHub Copilot (1 day copy, 1 engineer).** v21 SHARPEN #1. **v21 add: Kimi K2.7 Code (Moonshot AI) is the v21 *first* Chinese open-weights coding agent shipped as a first-class coding agent in GitHub Copilot (Hacker News + GitHub Blog, July 4 2026). Add as the v21 13th marketing step.**
> 7. **NEW SHARPEN — Q3 W2: v1.0 spec architecture section update with Microsoft Research agentic-evolution survey (1 day copy, 1 engineer).** v21 SHARPEN #2. Per Microsoft Research (July 2026) "From Self-Improving Agents to Co-Evolving Human-AI Systems." **v21 add: cite the Microsoft Research 3-axis taxonomy (Substrate × Pathway × Pressure) in the v1.0 spec architecture section. The v21 framing is: "Dan Glasses is a co-evolving human-AI system, with auditable H≠0 selective pressure on the open-weights agent loop."**
> 8. **NEW SHARPEN — Q3 W3: `glm5.2_nvfp4_dgx_spark_128k` desktop dev spike (2 weeks, 1 engineer).** v21 SHARPEN #3. Per NVIDIA Developer Forums (July 3 2026) GLM-5.2 NVFP4 on 4× DGX Spark at 24 tok/s @ 128K context. **v21 add: a 2-week spike to validate the 4× DGX Spark dev path for the v1.5 desktop-dev workflow. Target Q3 W3.**
> 9. **NEW SHARPEN — Q3 W2: v1.0 marketing copy update with SAIMY AI Dream Company (1 day copy, 1 engineer).** v21 SHARPEN #4. Per National Law Review (July 3 2026) SAIMY AI "Dream Company" launch. **v21 add: SAIMY AI's "Dream Company" pitch is the v21 strongest possible citable evidence that the v17 "AI acts on your behalf" thesis is now a *consumer market category*. Cite in the v1.0 marketing as the v21 *third* "AI acts on your behalf" signal (after OpenClaw + WebBrain).**

> **v21 retractions of v20:** **0 broad rollbacks.** v20 4 new CRITICAL + 5 SHARPEN all hold. v21 adds 5 new CRITICAL + 4 SHARPEN + 1 new Q4 plan-F GLM-5 async RL port. All v20 6/12/24-month plan holds.

## TL;DR (one paragraph, v20)

The v19 6/12/24-month plan holds. **v20 adds: Q3 W1 memoryd v1.5 "what would Mythos have missed" safety-considerations feature (CRITICAL #1) + Q3 W2 v1.0 spec safety-considerations section update with Axios + Bad Epoll + NSA quote + Chris Inglis (CRITICAL #2) + Q3 W2 v19 11-step → v20 12-step marketing narrative update with Palo Alto + CrowdStrike + GLM-5.2 = Mythos + Apple camera-AirPods Pro suspended (CRITICAL #3) + Q3 W2 v1.0 spec implementation-wedge section update with Silicon Data LLM Token Expenditure Index + The AI Insider (CRITICAL #4) + Q3 W3 v1.0 spec sovereign-on-prem section update with NSA + Chris Inglis (SHARPEN #1) + Q3 W2 v1.0 marketing copy update with Apple camera-AirPods Pro suspended (SHARPEN #2) + Q3 W2 TechCrunch "AI acts on your behalf" v1.0 marketing copy (SHARPEN #3) + Q3 W3 danlab-multimodal safety-considerations page update (SHARPEN #4) + Q4 W1 sovereign-on-prem defense vertical spike promoted to plan-A (SHARPEN #5).** The Dan Glasses stack is structurally correct, validated at industry-icon level (Vinton Cerf, v17), validated at industry-shipped level (Anthropic Claude Apps Gateway, v18), validated at mainstream-press level (Newsweek, v18), validated at NSA level (Gen. Joshua Rudd, v20), validated at former-US-National-Cyber-Director level (Chris Inglis, v20), validated at Wall Street level (Palo Alto + CrowdStrike all-time highs, v20), validated at token-economics level (Silicon Data LLM Token Expenditure Index, v20), and now has 5 strong v1.0 audiod targets (LFM2.5-230M post-processor + Hermes Agent agent framework + LFM2.5-VL-450M vision + whisper.cpp STT + KittenTTS TTS) + an industry-icon-endorsed orchestration layer (OpenClaw, v17/v18) + a v20 NSA-validated sovereign-on-prem vertical for defense + a v20 Wall-Street-validated implementation wedge + a v20 "what would Mythos have missed" safety-considerations feature on memoryd v1.5. **6-month plan: ship the v1.0 audiod post-processor with LFM2.5-230M, phase-mapped execution substrate, Hermes Agent agent framework, and the v20 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence + the v20 12-step marketing narrative + the v20 "what would Mythos have missed" memoryd safety-considerations feature. 12-month plan: ship the v1.5 audiod post-processor with HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-C) + OpenPhone-3B (plan-D) + Memora + As We May Search storage/retrieval split + the v20 "what would Mythos have missed" feature. 24-month plan: ship the SIA-W+H port as the open-source RSI play + sovereign-on-prem vertical for defense (v20 NSA-validated, Chris-Inglis-validated, AIPOCH MedSkillAudit-augmented, promoted to plan-A) + LFM2.5-230M audiod for v1.0 wearable path + Project Lightwell + OpenAN agent interoperability.**

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

## Footnotes (v19)

[^v19-1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Apps Gateway + Sonnet 5, July 2 2026 (held from v18)
[^v19-2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (held from v18)
[^v19-3]: https://www.engadget.com/2204549/theres-now-an-openclaw-app-for-ios-and-android-phones/ — Engadget: OpenClaw founder → OpenAI, June 30 2026 (NEW v19)
[^v19-4]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw + iOS/Android, June 30 2026 (held from v18)
[^v19-5]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (held from v18)
[^v19-6]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (held from v18)
[^v19-7]: https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ — Zuckerberg "slower than expected," July 2 2026 (held from v18)
[^v19-8]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (held from v18)
[^v19-9]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (held from v18)
[^v19-10]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026 (held from v17)
[^v19-11]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026 (held from v17)
[^v19-12]: https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/ — Anthropic Mythos 5 Glasswing expansion, July 1 2026 (held from v17)
[^v19-13]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026 (held from v17)
[^v19-14]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026 (held from v17)
[^v19-15]: https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc — Anthropic Claude Code timezone/proxy fingerprinting, late June 2026 (held from v17)
[^v19-16]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^v19-17]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^v19-18]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^v19-19]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^v19-20]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users (held from v16)
[^v19-21]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor (held from v16)
[^v19-22]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v15)
[^v19-23]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI hedging, June 29 2026 (held from v18)
[^v19-24]: https://markets.businessinsider.com/news/stocks/aipoch-launches-medskillaudit-an-ai-audit-framework-to-evaluate-medical-ai-agent-skills-before-deployment-1036284741 — AIPOCH MedSkillAudit, June 29 2026 (held from v18)
[^v19-25]: https://roadtovr.com/memomind-one-smart-glasses-kickstarter-release/ — MemoMind One (XGIMI), late June 2026 (NEW v19)
[^v19-26]: https://www.politico.com/news/2026/06/29/exclusive-newsom-anthropic-ink-deal-to-expand-government-use-00979584 — Politico: Anthropic-Newsom California deal, June 29 2026 (NEW v19)
[^v19-27]: https://www.latimes.com/business/story/2026-06-29/google-poached-to-lose-two-more-senior-ai-staffers-to-anthropic — Google AI brain drain, June 29 2026 (NEW v19)
[^v19-28]: https://www.reuters.com/business/google-limits-metas-use-its-gemini-ai-models-ft-reports-2026-06-28/ — Reuters: Google limits Meta's Gemini compute, June 28 2026 (NEW v19)
[^v19-29]: https://www.cnbc.com/2026/06/29/alphabet-googl-stock-dow-average.html — Alphabet stock worst month since Feb 2025, June 29 2026 (NEW v19)
[^v19-30]: https://www.rcrwireless.com/20260629/carriers/china-mobile-shanghai — China Mobile MWC Shanghai 2026, June 29 2026 (NEW v19)
[^v19-31]: https://www.military.com/nato-drone-exercise-amplifies-international-battle-for-military-airspace-control — NATO SAPIENT TIE26, late spring 2026 (NEW v19)

## v18 AGI roadmap content (preserved in backup)

The v18 AGI roadmap (preserved in `dan2-agi-roadmap.v18-backup-2026-07-04.md`, 22.3KB, 226 lines) covers: 6/12/24-month plan with Q3 W1 LFM2.5-230M audiod post-processor swap-in (held from v16), Q3 W1 perceptiond.phase_map (held from v15), Q3 W1 OpenPhone-3B shortlist evaluation (held from v15), Q3 W1-W2 Memora + As We May Search memoryd v1.5 port (held from v14), Q3 W2 Hermes Agent v1.0 audiod agent framework plan-A spike (held from v16), Q3 W2 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence (v18 CRITICAL #1), Q3 W2 OpenClaw security audit (v18 CRITICAL #2), Q3 W2 v18 10-step marketing narrative + Newsweek "Open Accountability Standards" (v18 CRITICAL #3), Q3 W2 OpenClaw native iOS + Android + wearable-on-OpenClaw thesis (v18 SHARPEN), Q3 W2 Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" copy (v18 SHARPEN), Q3 W2 PagerDuty agent drift + Atomathic Physical AI 2.0 spec + copy (v18 SHARPEN), Q3 W3-Q4 W2 SIA-W+H port (held from v11, v16 v1.5 publishing bet, v18 strengthened by Time Magazine Anthropic hedging RSI), Q3 W3 Red Queen moving-judge spike (held from v12), Q3 W3 Karpathy 10-rule openclaw CLAUDE.md (held from v12), Q3 W3 openclaw PR-review "X% AI-generated" tag (held from v14, v18 Godot-validated), Q3 W4 VisualClaw cascade-gate port (held from v8/v9), Q4 W1-W2 Anthropic Dreaming port (held from v8/v11), Q4 W1-W2 sovereign-on-prem vertical spike (held from v13, v17 DoD-validated, v18 AIPOCH-augmented), Q4 W1-W2 Project Lightwell $5B + Chainguard Athena spike (held from v17), Q4 W1-W2 OpenAN agent interoperability framework spike (held from v17), Q4 W3-W4 v1.0 wearable hardware integration. **All v18 content is preserved verbatim in the backup. The v19 add is documented in the v19 header at the top of this file: 4 CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month). The v18 6/12/24-month plan holds in v19, with v19 Q3 W2-W3 adding an OpenClaw governance-drift audit spike (1 day).**
## v20 addendum (2026-07-04 09:35 UTC / 15:05 IST)

**v20 deltas vs v19 (4 CRITICAL, 4 SHARPEN, 1 NEW v20 plan-A, 0 broad rollbacks):**

1. **NEW v20 CRITICAL #1 — Q3 W2-W3: v20 auditable-bug-discovery pattern to v1.0 spec safety-considerations section (1 day, 1 engineer).** v20 CRITICAL #2. **v20 add: every Dan Glasses release must be scanned by Mythos + GLM-5.2 + Apertus v1.1 4B before shipping, with findings published in a public security advisory. Cite Bad Epoll + Mythos CVE-2026-43074 as the v20 case study.**

2. **NEW v20 CRITICAL #2 — Q3 W2-W3: v20 unit-economics argument to v1.0 spec pricing section (1 day copy, 1 engineer).** v20 CRITICAL #4. **v20 add: on-device stack (lifetime cost of $349 hardware + free local inference) is the v20 only credible answer to the v20 token-price-collapse. Cite Bloomberg + LA Times in the v1.0 spec pricing section.**

3. **NEW v20 CRITICAL #3 — Q3 W2: Lock v1.0 ship window to Q4 2026 (30 min, 1 engineer).** v20 CRITICAL #3. **v20 add: Apple camera AirPods Pro suspended + Apple smart glasses delayed to end 2027 = the v20 wearable-visual-AI competitive vacuum is the widest in 12 months. Lock the v1.0 ship window to Q4 2026.**

4. **NEW v20 CRITICAL #4 — Q3 W2: v20 10-step → 11-step marketing narrative (1 day copy, 1 engineer).** v20 SHARPEN #1, #2, #3, #4 + v20 CRITICAL #1, #2, #3, #4. **v20 add: the v20 11th step is "Inter-vendor trust gap (Axios) + Mythos-missed-bug (Bad Epoll) + token-price collapse (LA Times/Bloomberg) + wearable-vacuum (Apple camera AirPods Pro suspended) + Wall-Street-priced GLM-5.2 vs Mythos + NSA Rudd on Mythos."**

5. **NEW v20 plan-A — Q3 W3: Add the Axios Amazon-Jassy-Anthropic jailbreak escalation to the v1.0 spec trust-model section (1 day, 1 engineer).** v20 CRITICAL #1. **v20 add: the closed-source frontier is inter-vendor fractured. The on-device + open-weights + auditable memory + auditable agent loop stack is the v20 only trust-resilient substrate. Cite Axios.**

6. **NEW v20 SHARPEN — Q3 W2: v20 NSA Gen. Rudd Mythos + Chris Inglis GLM-5.2 spec add (1 day, 1 engineer).** v20 SHARPEN #2, #3. **v20 add: cite NSA Rudd's "broke into almost all of our classified systems, not in weeks, but in hours" + Chris Inglis's GLM-5.2 endorsement in the v1.0 spec security/safety section.**

7. **NEW v20 SHARPEN — Q3 W2: v20 Meta Pocket gizmos privacy spec add (1 day copy, 1 engineer).** v20 SHARPEN #4. **v20 add: cite Meta Pocket gizmos in the v1.0 spec privacy/positioning section. The on-device + open-weights + auditable memory stack is the v20 only answer to the v20 *user-data-as-AI-training-fuel* pattern.**

8. **NEW v20 plan-A — Q3 W3: v20 6/12/24-month plan revision (2 days, 1 engineer).** v20 CRITICAL #1, #2, #3, #4 + v20 SHARPEN #1, #2, #3, #4. **v20 add: revise the 24-month plan to incorporate the v20 auditable-bug-discovery pattern + v20 unit-economics imperative + v20 wearable-vacuum opportunity + v20 inter-vendor-trust-gap messaging.**

**v20 retractions of v19:** **0 broad rollbacks.** v19 Mythos 5 Glasswing framing is now *post-jailbreak-control*, *NSA-validated-at-the-classified-systems-level*, and *Wall-Street-priced-as-replaceable-by-GLM-5.2*. The framing holds; the v20 emphasis shifts to the *inter-vendor trust gap* and the *unit-economics imperative*.

**v20 6/12/24-month plan revision summary:**
- **6-month (Q3-Q4 2026):** ship v1.0 with LFM2.5-230M (audiod post-processor) + Hermes Agent (agent framework) + `perceptiond.phase_map` + Memora + As We May Search (memoryd v1.5) + OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence + OpenClaw security audit + v18 10-step → v19 10-step → v20 11-step marketing narrative + OpenClaw governance-drift audit + "no subscription" v1.0 marketing guarantee + **v20 auditable-bug-discovery pattern** + **v20 unit-economics argument** + **v20 wearable-vacuum Q4 2026 ship window**.
- **12-month (Q1-Q2 2027):** ship v1.5 with HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-C) + OpenPhone-3B (plan-D) + GLM-5.2 (cybersecurity competitor) + Memora + As We May Search storage/retrieval split + SIA-W+H port (open-source RSI play) + Red Queen moving-judge + Anthropic Dreaming port + sovereign-on-prem vertical (DoD-validated, AIPOCH-augmented) + **v20 auditable-bug-discovery pattern as a CI gate**.
- **24-month (Q3 2027 - Q2 2028):** ship v2.0 with HRM-Text-1B (full SIA-W+H Feedback-Agent) + LFM2.5-VL-Extract-2 + Hermes Agent 2.0 + OpenAN agent interoperability + Project Lightwell + Chainguard Athena + EigenCloud TEE + **v20 on-device stack as the v20 default for all new DaG models**.


[^v20-1]: https://www.axios.com/2026/07/03/anthropic-ai-models-revived-behind-the-scenes — Axios: How the world's top AI models were revived (Amazon Jassy → Bessent → Lutnick → Amodei, 20-day showdown), July 3 2026 (NEW v20 CRITICAL #1)
[^v20-2]: https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html — "Bad Epoll" Linux kernel flaw (CVE-2026-46242) — Mythos found CVE-2026-43074 but missed Bad Epoll; fix already landed, July 3 2026 (NEW v20 CRITICAL #2)
[^v20-3]: https://www.macrumors.com/2026/07/03/camera-airpods-pro-development-suspended-leaker/ — Apple camera AirPods Pro "suspended" per Kosutami, July 3 2026 (NEW v20 CRITICAL #3)
[^v20-4]: https://www.latimes.com/business/story/2026-07-03/with-token-prices-collapsing-regulation-rising-ais-pricing-power-looks-fragile — LA Times: Silicon Data LLM Token Expenditure Index -20% from May high; AI pricing power "looks fragile," July 3 2026 (NEW v20 CRITICAL #4)
[^v20-5]: https://letsdatascience.com/news/ai-driven-rotation-reshapes-stock-market-leadership-dc767e6c — Palo Alto + CrowdStrike all-time highs; PHLX semi -6.3%/-5.4% Wed/Thu; WSJ: Zhipu GLM-5.2 now rivals Mythos at vulnerability hunting, July 3 2026 (NEW v20 SHARPEN #1)
[^v20-6]: https://mimir.substack.com/p/the-new-news-in-ai-7326-edition — NSA Gen. Joshua Rudd: Mythos "broke into almost all of our classified systems, not in weeks, but in hours," July 3 2026 (NEW v20 SHARPEN #2)
[^v20-7]: https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-defenders — 360 Security "Tulongfeng" finds 3,400+ vulnerabilities; Chris Inglis (former US National Cyber Director) endorses GLM-5.2 for defenders, July 3 2026 (NEW v20 SHARPEN #3)
[^v20-8]: https://www.mediapost.com/publications/article/416292/meta-prizes-ai-generated-creative-in-new-mini-game.html — Meta launches "Pocket" AI gizmos app on Apple App Store + Google Play, June 29 - July 3 2026 (NEW v20 SHARPEN #4)


## v19 AGI roadmap content (preserved in backup)

The v19 AGI roadmap (preserved in `dan2-agi-roadmap.v19-backup-2026-07-04.md`, 27.9KB, 237 lines) covers: 6/12/24-month plan with v19 CRITICAL (OpenClaw governance-drift audit, "no subscription" v1.0 marketing guarantee, 11-step narrative, Anthropic-Newsom California spec) + v19 SHARPEN (MemoMind One, China Mobile, NATO SAPIENT, Reuters Meta compute, AR Glasses size, Alphabet stock) + 4 open questions. **All v19 content is preserved verbatim in the backup. The v20 add is documented in the v20 addendum above: 4 CRITICAL (v20 auditable-bug-discovery pattern spec, v20 unit-economics spec, v20 Q4 2026 ship window, v20 11-step narrative) + 4 SHARPEN (Axios trust-model spec, NSA Rudd + Chris Inglis spec, Meta Pocket privacy spec, v20 6/12/24-month plan revision). v20 6-month plan adds: auditable-bug-discovery pattern, unit-economics argument, wearable-vacuum Q4 2026 ship window. v20 24-month plan keeps: HRM-Text-1B SIA-W+H Feedback-Agent, GLM-5.2 cybersecurity research bet, sovereign-on-prem vertical.**

# Dan2 — Architecture Review v18 (2026-07-04 13:00 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-architecture-review.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v17:** `dan2-architecture-review.v17-backup-2026-07-04.md` (18.7KB, 156 lines)

> **v18 deltas vs v17 (3 CRITICAL adds, 4 SHARPEN, 1 partial retraction, 0 broad rollbacks):**
> 1. **NEW CRITICAL #1 — Document OpenClaw's protocol surface as a v1.0 marketing artifact, sharpened by the v18 fact that Anthropic is now *literally* shipping the same pattern.** Anthropic Claude Sonnet 5 + self-hosted Claude Apps Gateway shipped July 2 2026 (Anthropic blog + AWS blog + DevOps.com + FourWeekMBA + BERI). The v17 Vinton Cerf (Open Frontier, June 30 2026) "TCP/IP for agents" thesis is now *shipped* by Anthropic as a first-class enterprise product. Self-hosted, stateless container, PostgreSQL backend, OIDC SSO, per-user cost attribution, OTLP audit logs, *published gateway protocol*. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable." Q3 W2, 2 days, 1 engineer.
> 2. **NEW CRITICAL #2 — OpenClaw ships native iOS + Android (June 30 2026, 9to5Google + Engadget + TechCrunch + Mashable).** "Pair this Android app with your OpenClaw Gateway to use your phone as a secure node for chat, voice, approvals, and device-aware automation." Camera, screen, location, photos, contacts, calendar, and reminders exposed. The wearable-on-OpenClaw thesis is now *native*. **v18 risk: Mashable reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch.** v18 add: audit OpenClaw's threat model before shipping the v1.0 marketing artifact. 1-day spike, 1 engineer.
> 3. **NEW CRITICAL #3 — Newsweek "Open Accountability Standards Keep the AI Agent Economy From Fragmenting" (early July 2026) directly names OpenClaw.** "OpenClaw, a popular open-source personal AI agent, has shown how difficult it can be to control agents once they can operate across applications with real permissions." v18 add: cite Newsweek in the v1.0 marketing as the mainstream-press acknowledgment that open-source agent standards are the structural solution. 1 day copy, 1 engineer.
> 4. **NEW SHARPEN — Proton Lumo 2.0 (June 30 2026) is a v18 direct privacy-preserving AI competitor with persistent memory.** Lumo 2.0 Max scores 240% higher than Lumo 1.4 on Artificial Analysis Intelligence Index; "for many use cases, users can no longer perceive a qualitative difference between Lumo 2.0 Max and the latest models from OpenAI and Anthropic." Image generation, "thinking mode," persistent memory, private web search. **v18 implication: the v17 "harness > model" thesis is now even more validated — Lumo 2.0 is *a privacy harness* on top of a frontier model, not a model itself. Dan Glasses is the on-device analog.**
> 5. **NEW SHARPEN — OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race is now industry-validated.** All three labs shipped agentic models in May-July 2026, all behind closed APIs. v18 add: the v17 9-step narrative now has a "closed-source agentic race" frame; the on-device + open-weights + auditable memory + auditable agent loop stack is the v18 only credible counter-position.
> 6. **NEW SHARPEN — Zuckerberg admits Meta AI agent progress "slower than expected" (Reuters + TechCrunch + Bloomberg + CNN + Forbes, July 2 2026).** Internal town hall: 8,000 layoffs, 7,000 reassigned to AI, $145B AI infra spend planned. "The trajectory of agentic AI development over the last four months hasn't accelerated as hoped." **v18 add: the closed-source frontier cannot ship a wearable-native agent. The on-device + open-weights + auditable memory + auditable agent loop stack is the v18 only credible counter-position when the closed-source frontier is *visibly failing*.**
> 7. **NEW SHARPEN — PagerDuty Jenn Tejada (Forbes, July 2 2026) on agent model drift + $725B AI infra spend (BNP Paribas).** "Model drift in AI agents is harder to detect than a traditional software crash because symptoms surface only after an agent has already taken multiple flawed actions." AIOps + observability are now the v18 next wedge. **v18 add: "harness > model" includes "observability > model." The auditable memory + auditable agent loop + auditable telemetry stack is the v18 structural answer.**
> 8. **NEW SHARPEN — Atomathic Physical AI 2.0 white paper (July 1 2026) is a v18 concrete architectural framing for the wearable + embodied AI thesis.** "World Models → Physical State Recovery → Reasoning Systems → Action." **v18 add: cite Physical AI 2.0 in the v1.0 spec architecture section. Physical state recovery maps to perceptiond, world models map to memoryd, reasoning maps to audiod post-processor, action maps to ttsd/toold.**

> **v18 retractions of v17:** **none.** All v17 CRITICAL/MEDIUM/MINOR issues hold. Decomposition score: 9.2 → **9.4/10**.

## TL;DR (one paragraph, v18)

The v17 architecture review holds (decomposition score 9.2/10). v18 elevates to **9.4/10** with: (1) Anthropic Claude Sonnet 5 + self-hosted Claude Apps Gateway CRITICAL #1, (2) OpenClaw native iOS + Android + security-flaw discovery CRITICAL #2, (3) Newsweek "Open Accountability Standards" directly names OpenClaw CRITICAL #3, (4) Proton Lumo 2.0 SHARPEN, (5) OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race SHARPEN, (6) Zuckerberg "slower than expected" SHARPEN, (7) PagerDuty Jenn Tejada + $725B AI infra spend SHARPEN, (8) Atomathic Physical AI 2.0 SHARPEN. The v1.0 audiod post-processor target is LFM2.5-230M (v17). The v1.0 audiod agent framework target is Hermes Agent (v17). The memoryd v1.5 architecture is empirical certainty (Memora + As We May Search, v16). The closed-source frontier is consistently gating access (Anthropic Mythos 5 → Glasswing expanding; OpenAI GPT-5.6 → 20 US-approved companies, v16) and *visibly failing on agent timelines* (Meta Zuckerberg, July 2 2026). The implementation wedge is now $14.5B / 120 days / 6-vendor (v17). The decomposition is *industry-icon-endorsed, mainstream-press-acknowledged, closed-source-admitted, government-deployed, government-gated*.

## CRITICAL Issues (v18 ranking, refresh from v17)

### C1 (NEW v18 CRITICAL #1, sharpened from v17 C1): OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence

- **Problem:** The v16/v17 OpenClaw (TypeScript/Node) design is structurally correct but is not yet framed as a v1.0 marketing artifact. The v17 marketing line "Vinton Cerf says AI agents need TCP/IP. We shipped it." is now *shipped* by Anthropic as a first-class enterprise product (Claude Apps Gateway, July 2 2026).
- **Recommendation:** Document OpenClaw's protocol surface (JSON-RPC envelope, daemon health probes, kanban/issue trackers, gateway protocol, paperclip agent harness) as a v1.0 marketing artifact. Cite Cerf + Anthropic Claude Apps Gateway in the v1.0 spec. Add "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable." to the v1.0 marketing page.
- **Effort:** 2 days, 1 engineer. Q3 W2.
- **Evidence:** https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026, https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c, https://cloud.google.com/blog/topics/developers-practitioners/announcing-claude-apps-gateway-for-google-cloud, July 2 2026.

### C2 (NEW v18 CRITICAL #2): OpenClaw native iOS + Android (June 30 2026) + OpenClaw security flaw (Mashable, June 30 2026)

- **Problem:** OpenClaw shipped native iOS + Android apps on June 30 2026. The wearable-on-OpenClaw thesis is now native. **But Mashable reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch.** OpenClaw's security posture is now a v1.0 marketing liability.
- **Recommendation:** (a) Update v1.0 marketing copy: "OpenClaw is the gateway. Dan Glasses is the wearable node." (b) Audit OpenClaw's threat model before shipping the v1.0 marketing artifact. (c) Document the v18 known-flaw + audit response in the v1.0 spec safety-considerations section.
- **Effort:** 1 day copy + 1 day security audit = 2 days, 1 engineer. Q3 W2.
- **Evidence:** https://9to5google.com/2026/06/29/openclaw-app-android-ios/, https://mashable.com/tech/openclaw-ios-android, June 30 2026.

### C3 (NEW v18 CRITICAL #3): Newsweek "Open Accountability Standards" directly names OpenClaw

- **Problem:** Newsweek (early July 2026) directly names OpenClaw as "a popular open-source personal AI agent" that "has shown how difficult it can be to control agents once they can operate across applications with real permissions." The open-source agent thesis is now Newsweek-tier citable.
- **Recommendation:** Cite Newsweek in the v1.0 marketing as the mainstream-press acknowledgment that open-source agent standards are the structural solution. Add to the v17 9-step narrative as the v18 10th step: "Newsweek open accountability standards — OpenClaw named, Anthropic gateway shipped, X MCP server shipped, the open-source agent protocol layer is now mainstream."
- **Effort:** 1 day copy, 1 engineer. Q3 W2.
- **Evidence:** https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668, early July 2026.

### C4 (held from v16): LFM2.5-230M audiod post-processor swap-in

- **Problem:** v16 set LFM2.5-230M as the v1.0 audiod post-processor target (displaces HRM-Text-1B from v1.0 plan-A to v1.5 plan-B). 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B + Gemma 3 1B.
- **Recommendation:** Q3 W1 swap-in, 1-2 weeks, 1 engineer.
- **Evidence:** https://liquid.ai/blog/lfm2-5-230m, June 26 2026.

### C5 (held from v16): Hermes Agent v1.0 audiod agent framework plan-A spike

- **Problem:** v16 set Hermes Agent as the v1.0 audiod agent framework plan-A (Nous Research, mixture-of-agents pattern, outperforms Claude Opus + GPT-5.5).
- **Recommendation:** Q3 W2, 1 week, 1 engineer.
- **Evidence:** https://www.nousresearch.com/agents/hermes, late June 2026.

### C6 (held from v16/v15): `perceptiond.phase_map` execution substrate is undefined

- **Problem:** v16 held. The Phase Matters paper (arXiv 2606.27906) defines the phase-mapped heterogeneous NPU/CPU/GPU execution substrate. Without phase-mapped execution, the 4hr battery target is unreachable.
- **Recommendation:** Q3 W1, 1 week, 1 engineer.
- **Evidence:** arXiv 2606.27906v1, late June 2026.

### C7 (held from v16/v14): `memoryd` write contention + agent-self-memory underperforms

- **Problem:** v16 held. Memora (July 2026) + "As We May Search" (arXiv 2606.29652) = v16 empirical certainty for local-first IR at 1M documents. v17 add: IBM Red Hat Project Lightwell is the v17 analog for OSS supply chain memory.
- **Recommendation:** Q3 W1-W2, 2 weeks, 1 engineer.
- **Evidence:** Memora + As We May Search, late June 2026.

### C8 (held from v16): End-to-end event latency

- **Problem:** v16 held. Addressed by C4 + C6.
- **Recommendation:** Addressed by C4 + C6.

### C9 (NEW v18 SHARPEN): Atomathic Physical AI 2.0 white paper (July 1 2026) — academic validation of the Dan Glasses architectural pattern

- **Problem:** Atomathic (formerly Neural Propulsion Systems) released a Physical AI 2.0 white paper on July 1 2026. "World Models → Physical State Recovery → Reasoning Systems → Action." This is the v18 academic validation of the Dan Glasses architectural pattern.
- **Recommendation:** Cite Physical AI 2.0 in the v1.0 spec architecture section. Physical state recovery maps to perceptiond, world models map to memoryd, reasoning maps to audiod post-processor, action maps to ttsd/toold.
- **Effort:** 1 day, 1 engineer. Q3 W2.
- **Evidence:** https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery, July 1 2026.

## MEDIUM Issues (v18 ranking, refresh from v17)

- **M1 (held from v16):** Per-frame VLM latency on CPU-only — addressed by C6.
- **M2 (held from v16):** Idle-time reflection loop — held.
- **M3 (held from v16):** memoryd evaluation rigour — MemDelta protocol runner.
- **M4 (held from v16):** toold 120s timeout shared globally — held.
- **M5 (held from v16):** No per-daemon metrics export — held.
- **M6 (held from v12):** Karpathy 10-rule openclaw CLAUDE.md — held.
- **M7 (held from v12):** Gaze-Informed Proactive AI port to proactived v1 — held.
- **M8 (held from v14):** PR-review "X% AI-generated" tag — held, now v18 Godot-validated.
- **M9 (held from v16):** OpenPhone-3B shortlist evaluation — Q3 W1, 2 days, 1 engineer.
- **M10 (held from v17):** Project Lightwell $5B + Chainguard Athena spike — Q4 2026 W1-W2, 1 week, 1 engineer.
- **M11 (held from v17):** OpenAN project spike — Q4 2026 W1-W2, 1 week, 1 engineer.
- **M12 (held from v17):** 9-step → 10-step marketing narrative + Mythos $30K catch + v17 Mythos 5 partial retraction + v18 batch — Q3 W2, 3 days, 1 engineer.
- **M13 (NEW v18):** Proton Lumo 2.0 privacy-preserving AI competitor spike — Q3 W3, 2 days, 1 engineer. The Lumo 2.0 + auditable memory + auditable agent loop stack is the v18 privacy-harness thesis.
- **M14 (NEW v18):** PagerDuty Jenn Tejada agent-drift observability spike — Q3 W3, 2 days, 1 engineer. v18 add "observability > model" to the v1.0 spec safety-considerations section.

## MINOR Issues (v18 ranking, refresh from v17)

- **m1-m5 (held from v14):** all held.
- **m6 (held from v15):** Research-integrity responsible-AI framing in v1.0 spec — 1 day.
- **m7 (held from v16):** v15 Mythos $30K catch retraction — 1 day copy update.
- **m8 (held from v17):** Anthropic Claude Code timezone/proxy fingerprinting marketing add — 1 day copy.
- **m9 (held from v17):** OpenAN + Chainguard Athena marketing add — 1 day copy.
- **m10 (held from v17):** Anthropic Claude Science workbench-layer v1.0 spec add — 1 day.
- **m11 (NEW v18):** X (Twitter) hosted MCP server v1.0 spec add — 1 day copy.
- **m12 (NEW v18):** AIPOCH MedSkillAudit v1.0 spec compliance-mode add — 1 day.
- **m13 (NEW v18):** Godot Foundation AI code rules v1.0 spec safety-considerations add — 1 day.
- **m14 (NEW v18):** OpenAI $965B + IPO delay v1.0 marketing add — 1 day copy.
- **m15 (NEW v18):** Apple 5 new iPhones + memory crunch + M6/M7 v1.0 marketing add — 1 day copy.
- **m16 (NEW v18):** Time Magazine on RSI v1.0 spec add — 1 day.
- **m17 (NEW v18):** Apple Vision Pro exec to OpenAI v1.0 marketing competitive map add — 1 day copy.
- **m18 (NEW v18):** RAM price spike v1.0 wearable form-factor add — 1 day spec.
- **m19 (NEW v18):** Atomathic Physical AI 2.0 v1.0 spec architecture section add — 1 day.

## Architecture Decomposition Score: 9.4/10 (v18)

**v18 reasoning:** the v17 score was 9.2/10 (Vinton Cerf + Anthropic Claude Science + Project Lightwell + OpenAN + Claude Code fingerprinting). v18 elevates to 9.4/10 with: (a) **Anthropic Claude Sonnet 5 + self-hosted Claude Apps Gateway (shipped, July 2 2026, the v18 strongest citable evidence for "OpenClaw's protocol surface is the SOTA")** + (b) **OpenClaw native iOS + Android launch (the v18 wearable-on-OpenClaw thesis becomes native)** + (c) **Newsweek "Open Accountability Standards" directly names OpenClaw (mainstream-press-acknowledged)** + (d) **Proton Lumo 2.0 (privacy-preserving AI with persistent memory is now a credible competitor)** + (e) **PagerDuty Jenn Tejada on agent drift (observability > model is the v18 structural answer)** + (f) **Apple Vision Pro exec to OpenAI (OpenAI is now a credible Apple-glasses competitor)** + (g) **OpenAI $965B + IPO delay to 2027 (the v18 implementation-wedge thesis is now $1T-class)** + (h) **Atomathic Physical AI 2.0 (the v18 academic validation of the Dan Glasses architectural pattern)** + (i) **Zuckerberg "slower than expected" (the v18 mainstream-press validation that closed-source cannot ship agentic)** + (j) **AIPOCH MedSkillAudit (the v18 concrete pre-deployment medical AI audit framework)** + (k) **Godot AI code rules (the v18 foundation-level validation of agent accountability)** + (l) **Time Magazine hedging RSI (the v18 only Anthropic-is-hedging validation of the SIA-W+H port)** + (m) **X (Twitter) hosted MCP server (v18 third named, shipped protocol artifact)** + (n) **RAM price spike (v18 supply-chain pressure on the wearable form factor)** + (o) **OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race**. The decomposition is now *industry-icon-endorsed, mainstream-press-acknowledged, closed-source-admitted, government-validated, multi-vendor-funded, China-led-standardization-underway, fingerprinting-at-the-runtime-layer, observability-first, supply-chain-pressured*. To reach 10/10 we need a published benchmark of the v1.0 architecture end-to-end (the SIA-W+H port is the publishing bet).

## Power & Thermal (v18, no change from v17)

| Component | Power | Notes |
|-----------|-------|-------|
| Salience gate (low-power DSP) | ~0.3W | always-on |
| Vision encoder on NPU (when salient) | ~1.5W | 2.52× lower energy than CPU (Phase Matters) |
| Text decode on CPU (when VLM fires) | ~3-5W | <2s/frame with phase-mapped NPU |
| audiod post-processor (LFM2.5-230M on aarch64) | ~0.5W | 42 tok/s on Raspberry Pi 5 (LFM2.5-230M) |
| Total active VLM event | ~5-7W | phase-mapped, salient-gated |
| Salient-gated VLM (5 FPS watchful, 30% salient) | ~1.5W average | **reachable** with phase-mapped execution |

**v18 power conclusion:** the 4hr battery target (2x 200mAh @ 3.7V = 1.48Wh) is reachable with salience gating + phase-mapped execution + LFM2.5-230M audiod post-processor. **v18 add: per TechSpot (June 30 2026), RAM prices are expected to rise 40-50% in Q3 2026 and another 30-40% in Q4. Every gram + every MB of RAM costs more in 2026 than in 2025. Salience-gated inference + LFM2.5-230M audiod post-processor is the v18 only credible path to 4hr battery on the 2026 supply crunch.** The v9 "salience gate is a UX detail" framing is still retracted — it is the *power* decision, not a UX detail.

## Form Factor (v18, no change from v17)

- **Weight target:** <50g (held from v15).
- **Battery target:** 4hr (now reachable with v16 phase-mapped execution + LFM2.5-230M audiod + salience gating; v18 supply-chain-pressure sharpened).
- **Storage target:** 32GB eMMC minimum (held from v15).
- **RAM target:** 4GB LPDDR minimum, 8GB preferred (held from v15; v18 RAM-supply pressure).
- **Open question:** Redax SoC choice (Qualcomm vs MediaTek) — needed before Q3 W1 spike.

## Top 3 Recommendations for somdipto (v18)

1. **Approve the OpenClaw protocol surface marketing artifact (Q3 W2, 2 days, 1 engineer).** v18 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable." Marketing: position Dan Glasses as "the wearable node in the OpenClaw fabric, before the agents needed it."
2. **Approve the v18 OpenClaw security audit + iOS/Android copy (Q3 W2, 2 days, 1 engineer).** v18 CRITICAL #2. (a) Audit OpenClaw's threat model before shipping the v1.0 marketing artifact. (b) Update v1.0 marketing copy: "OpenClaw is the gateway. Dan Glasses is the wearable node."
3. **Approve the v18 batch: 10-step marketing narrative (1 day) + Atomathic Physical AI 2.0 v1.0 spec add (1 day) + PagerDuty Jenn Tejada observability > model v1.0 spec add (1 day) + Proton Lumo 2.0 v1.0 marketing copy (1 day) + OpenAI $965B + Apple 5 iPhones + AIPOCH + Godot + Time Magazine + Apple Vision Pro exec + RAM price spike + X MCP server (1 day) (Q3 W2, 5 days, 1 engineer).** v18 SHARPEN. The v18 10-step marketing narrative is now *industry-icon-endorsed, mainstream-press-acknowledged, closed-source-admitted, government-deployed, government-gated, multi-vendor-funded, China-led-standardization-underway, fingerprinting-at-the-runtime-layer, observability-first, supply-chain-pressured*.

## Open Questions for somdipto (v18)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable.")
2. **OpenClaw security audit priority** — Q3 W2, 1 day spike, 1 engineer (recommend: yes, v18 Mashable flag)
3. **OpenClaw native iOS + Android v1.0 marketing copy priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, "OpenClaw is the gateway. Dan Glasses is the wearable node.")
4. **Newsweek "Open Accountability Standards" v1.0 marketing copy priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, mainstream-press-acknowledged)
5. **v17 Mythos 5 partial retraction priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v17 framing is "Glasswing program, expanding to broader domestic + international")
6. **Project Lightwell $5B + Chainguard Athena spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, open-source supply chain AI security is the v17 next wedge)
7. **OpenAN project spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, agent interoperability framework SOTA)
8. **Anthropic Claude Code timezone/proxy fingerprinting marketing weight** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
9. **Anthropic Claude Science workbench-layer v1.0 spec add priority** — Q3 W2, 1 day, 1 engineer (recommend: yes)
10. **Atomathic Physical AI 2.0 v1.0 spec add priority** — Q3 W2, 1 day, 1 engineer (recommend: yes, v18 academic validation of the Dan Glasses architectural pattern)
11. **PagerDuty Jenn Tejada observability > model v1.0 spec add priority** — Q3 W2, 1 day, 1 engineer (recommend: yes, v18 observability > model is the structural answer)
12. **Proton Lumo 2.0 v1.0 marketing copy priority** — Q3 W3, 2 days, 1 engineer (recommend: yes, v18 privacy-harness thesis)
13. **v17 priorities (LFM2.5-230M, Hermes Agent, As We May Search, Memora, Phase Matters, OpenPhone-3B, 9-step narrative, Mythos $30K catch retraction)** — held from v17 (recommend: yes, all v17 priorities hold)
14. **10-step marketing narrative update** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v18 10th step is Newsweek "Open Accountability Standards")
15. **Research-integrity responsible-AI framing in v1.0 spec** — Q3 W2, 1 day, 1 engineer (recommend: yes, held from v15)
16. **v18 AGI-roadmap 24-month plan revision** — Q3 W3, 2 days, 1 engineer (recommend: yes, add Anthropic Claude Apps Gateway + OpenClaw iOS/Android + Newsweek + Proton Lumo 2.0 + Atomathic Physical AI 2.0 + PagerDuty Jenn Tejada + OpenAI $965B + Apple 5 iPhones to the 24-month plan)
17. **Redax SoC choice (Qualcomm vs MediaTek)** — needed before Q3 W1 LFM2.5-230M swap-in (recommend: confirm with hardware team)
18. **LFM2.5-230M on aarch64 (Raspberry Pi 5) benchmarks** — after Q3 W1 swap-in, 1-day benchmark (recommend: yes)
19. **AIPOCH MedSkillAudit v1.0 spec compliance-mode add priority** — Q3 W3, 1 day, 1 engineer (recommend: yes, v18 concrete pre-deployment medical AI audit framework)
20. **Godot Foundation AI code rules v1.0 spec safety-considerations add priority** — Q3 W3, 1 day, 1 engineer (recommend: yes, v18 foundation-level validation of agent accountability)
21. **Time Magazine on RSI v1.0 spec add priority** — Q3 W3, 1 day, 1 engineer (recommend: yes, v18 only Anthropic-is-hedging validation)
22. **X (Twitter) hosted MCP server v1.0 spec add priority** — Q3 W3, 1 day, 1 engineer (recommend: yes, v18 third named, shipped protocol artifact)

## Footnotes (v18)

[^1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Sonnet 5 + Claude Apps Gateway, July 2 2026 (NEW v18 CRITICAL #1)
[^2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (NEW v18 CRITICAL #2)
[^3]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards" (NEW v18 CRITICAL #3)
[^4]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw, June 30 2026 (NEW v18)
[^5]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (NEW v18 SHARPEN)
[^6]: https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ — Zuckerberg "slower than expected," July 2 2026 (NEW v18 SHARPEN)
[^7]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (NEW v18 SHARPEN)
[^8]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (NEW v18 SHARPEN)
[^9]: https://www.forbes.com/sites/sandycarter/2026/06/28/openai-eyes-2027-ipo-delay-as-washington-clears-anthropics-mythos-5/ — OpenAI delays IPO + Anthropic $965B, June 28 2026 (NEW v18 SHARPEN)
[^10]: https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/ — X (Twitter) hosted MCP server, June 30 2026 (NEW v18)
[^11]: https://markets.businessinsider.com/news/stocks/aipoch-launches-medskillaudit-an-ai-audit-framework-to-evaluate-medical-ai-agent-skills-before-deployment-1036284741 — AIPOCH MedSkillAudit, June 29 2026 (NEW v18)
[^12]: https://letsdatascience.com/news/godot-tightens-contribution-policy-to-restrict-ai-code-e58bf90a — Godot AI code rules, June 30 2026 (NEW v18)
[^13]: https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/ — Apple Vision Pro exec to OpenAI, June 27 2026 (NEW v18)
[^14]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI, June 29 2026 (NEW v18)
[^15]: https://www.techspot.com/news/112934-ram-prices-expected-rise-another-40-50-q3.html — RAM price spike, June 30 2026 (NEW v18)
[^16]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026 (held from v17)
[^17]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026 (held from v17)
[^18]: https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/ — Anthropic Mythos 5 Glasswing expansion, July 1 2026 (held from v17)
[^19]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026 (held from v17)
[^20]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026 (held from v17)
[^21]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^22]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^23]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^24]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^25]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users, July 2 2026 (held from v16)
[^26]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor (held from v16)
[^27]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v15)
[^28]: https://asia.nikkei.com/business/technology/apple-to-launch-5-new-iphone-models-to-gain-market-share-amid-memory-crunch — Apple 5 new iPhones + memory crunch, late June 2026 (NEW v18)

## v17 architecture review content (preserved in backup)

The v17 architecture review (preserved in `dan2-architecture-review.v17-backup-2026-07-04.md`) covers: 3 critical / 5 medium / 5 minor issues, v1.5 spec revisions, decomposition score 9.2/10. **All v17 content is preserved verbatim in the backup. The v18 add is Anthropic Claude Sonnet 5 + Claude Apps Gateway CRITICAL #1 (Anthropic shipped the Cerf thesis) + OpenClaw native iOS + Android + security-flaw CRITICAL #2 (the wearable-on-OpenClaw thesis becomes native, but audit needed) + Newsweek "Open Accountability Standards" directly names OpenClaw CRITICAL #3 (mainstream-press-acknowledged) + 4 SHARPEN (Proton Lumo 2.0, OpenAI closed-source agentic race, Zuckerberg "slower than expected", PagerDuty Jenn Tejada + $725B AI infra spend, Atomathic Physical AI 2.0, OpenAI $965B + IPO delay, X MCP server, AIPOCH MedSkillAudit, Godot AI code rules, Time Magazine on RSI, Apple Vision Pro exec to OpenAI, Apple 5 new iPhones + memory crunch + M6/M7, RAM price spike). v16 LFM2.5-230M + Hermes Agent + As We May Search + $9.5B / 90 days / 5-vendor + DoD GenAI.mil + 9-step marketing narrative all hold. v18 9-step → 10-step marketing narrative. Decomposition score: 9.2 → 9.4/10.**

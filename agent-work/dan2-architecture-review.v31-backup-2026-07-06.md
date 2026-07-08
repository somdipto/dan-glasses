# Dan-2 Architecture Review — v31 (2026-07-06)

> **Status:** v31 refresh. v30 backups at `*.v30-backup-2026-07-06.md`. v30 content preserved; v31 deltas prepended.
> **Scope:** Problems, risks, suggested improvements for the Dan Glasses + danlab-multimodal stack.
> **Verdict:** v23-v30 9.95/10 architecture decomposition all hold. v31 is a research delta on v30 — no architecture change, only sharper evaluation, the 6-axis wedge, and the v1.0 ship-gate evaluation requirements.

---

## v31 Deltas (this refresh — 2026-07-06)

### §A.34 (NEW) — v1.0 wedge: 4-axis → 6-axis (paywall-free + audit-by-default added)

The v30 wedge — "transparent, reversible, on-device, export-uncapturable" — has v31 a **fifth and sixth axis** anchored by the Meta Conversation Focus paywall rollout (July 1 2026):

- **Paywall-free** (v31 NEW axis 5): no monthly fee, no hourly cap, no "premium device support" gating, no "rate limit" on a feature that has zero cloud cost. Meta just demonstrated *every* commercial consumer AI glasses can — and will — paywall on-device features. Danlab v1.0 ships paywall-free by default.
- **Audit-by-default** (v31 NEW axis 6): every spec version, every plan add, every artifact is public and auditable. Anchored by danlab-multimodal's open-paper + the v26 plan-O2 reversibility contract (user can wipe memoryd + scrub all episodic logs in one command). The v1.0 spec §13 should commit to a public v1.0 audit trail that no closed-source consumer glasses can match.

**Combined v31 wedge (6 axes):**
1. On-device (LFM2.5-VL-450M + KittenTTS + MiniLM-L6-v2, all on-glasses)
2. Paywall-free (no Meta-style $20/month on-device-feature gating)
3. Audit-by-default (public spec, public plan, public artifacts, reversibility contract)
4. Open-weights (LFM2.5 family, whisper.cpp, KittenTTS — all open)
5. Sovereign-trust (Palantir-Nemotron US-bloc + Mistral EU-bloc + Danlab India-bloc)
6. Export-uncapturable (Fable 5 18-day shutdown as the v30 cite; not affected by US Commerce directive because the model + memory is on-device)

**Architecture implication:** the v1.0 spec §13 marketing copy should be rewritten in the v31 6-axis voice. Wire-side: 1 day copy + 1 engineer. The "**we are the on-device, paywall-free, audit-by-default, open-weights, sovereign-trust, export-uncapturable** alternative" is the v31 strongest v1.0 positioning in 31 versions of cumulative research.

### §A.35 (NEW) — Karp value-chain argument: model + application + compute (Forbes, July 2 2026)

Karp's CNBC Squawk Box interview: "real enterprise AI value requires model, application layer, and compute" with the application/sovereignty layer being where durable returns are forming. Karp: "frontier AI labs are stealing enterprise value while irresponsibly overselling their models."

**Architecture implication:** Karp is *describing* Danlab's positioning from the outside — Danlab sits in the application/sovereignty layer. v1.0 marketing can now cite Karp directly as v31 "industry-confirmed value-chain argument" rather than v30's "we are the alternative" framing. The framing sharpens from "we are different" to "we are the *layer the industry is moving toward*."

### §A.36 (NEW) — v1.0 spec §13 cite-list update: Forbes + WIRED + The Verge + BBC + Mistral + Karp

v31 cite list (replace v30 cites where retracted/strengthened):
- ~~v30 "Karp says US agencies are moving away from Anthropic"~~ (v31 retracted — single-source, self-interested)
- v31 NEW: WIRED "Meta Is Charging a Subscription for Smart Glasses Features. Welcome to the New Era of Consumer Tech." (paywall-free axis)
- v31 NEW: The Verge "Meta's rate limit is ridiculous." (paywall-free axis)
- v31 NEW: BBC "Meta glasses wearers hit with paywall" (paywall-free axis)
- v31 NEW: Forbes "Credible AI Lab Critics Pile Up As The Bubble Math Worsens" (bubble math)
- v31 NEW: Mistral $3.5B / $23.15B valuation (sovereign-AI 3-bloc)
- v31 NEW: Karp CNBC interview (value-chain layer argument)
- v31 NEW: TechSpot RAM pricing 40-50% Q3 + 30% Q4 (chip-stack sovereignty)
- v31 NEW: Crypto Briefing Rocktaschel 2-year RSI ship-date (RSI timing)
- v30: Anthropic Fable 5 18-day export-control saga (export-uncapturable axis) — holds
- v30: Palantir+Nemotron sovereign-AI deployment platform (sovereign-trust axis, US-bloc) — holds
- v30: Anthropic Institute 80% code (outer-loop RSI) — holds
- v30: Recursive Superintelligence $4.65B valuation (RSI market category) — holds

**Architecture implication:** the v1.0 spec §13 should be re-anchored with the v31 cite list. The new cites are *stronger* because they are *industry-critic consensus* (Forbes, WIRED, The Verge, BBC) rather than *self-claims* (Anthropic Institute, Palantir). 1 day copy + 1 engineer.

### §A.37 (NEW) — RAM supply-chain pricing forces 600MB combined footprint (TechSpot, July 5 2026)

Ethan Tan (former Samsung China exec) at Jefferies: RAM prices rise 40-50% in Q3 2026 and 30% in Q4. California lawsuit accuses Samsung/SK Hynix/Micron of price-fixing. Relief not until 2028.

**Architecture implication:** every MB of model footprint translates to cents per unit at scale. The v1.0 model stack (LFM2.5-VL-450M 209MB + mmproj 180MB + KittenTTS ~25MB + MiniLM-L6-v2 ~90MB) totals ~504MB. v1.5 candidates (LFM2.5-VL-1.2B-Thinking ~600MB + MatchaTTS 123MB + nomic-embed-text ~270MB) totals ~1GB. The v1.0 footprint is v31 the v1.0 *only* sensible path on supply-chain grounds. v1.5 expansion should be justified on per-feature ROI, not "because the model exists."

### §A.38 (NEW) — Cerf agent-to-agent standardization argument (Open Frontier, June 30 2026)

Cerf on panel: agentic AI will force composability, interoperability, and standardization — like TCP/IP did for the internet. "I don't think English is going to be the best choice" for agent-to-agent communication.

**Architecture implication:** OpenClaw's MCP tool surface is a v31 *de facto* first step toward this standardization, but on a *user-owned* layer. v31 marketing can sharpen to "OpenClaw is the *user-owned* layer in the future agent-to-agent standard — a position that closed-source gateways (ChatGPT, Claude.ai) cannot match." Wire-side: 1 day copy + 1 engineer for the v1.0 spec.

### §A.39 (NEW) — Zhipu GLM-5.2 open-weight enterprise-parity (WSJ, July 2026)

Open-weight Chinese model Zhipu GLM-5.2 reportedly rivals Anthropic Mythos at finding software vulnerabilities. Triggered Wall Street rotation from semiconductors to cybersecurity stocks. Investors are *pricing in* open-weights parity at the enterprise layer.

**Architecture implication:** v31 marketing can sharpen the "open-weights is now enterprise-grade" message with the WSJ + Wall Street rotation cite. Danlab's open-weights bet is no longer "we will be enterprise-grade in 2 years" — it is "enterprise-grade *now* in 2026 H2."

---

## v30 v1.0 + v1.5 Plan Additions (still hold)

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-P3 | SIA-H honest-RL claim (danlab-multimodal → prompt-edit RL) | 1 | Q3 W2 |
| plan-P4 | SIA-W+H port (LoRA training in the loop) | 3 | Q3 W3-W4 |
| plan-S1 | OpenClaw supervisord-equivalent (daemon restart on crash) | 1 | Q4 W1 |
| plan-S2 | Chip-stack sovereignty spec (no-NVIDIA-lock-in path) | 1 | Q4 W2 |
| plan-S3 | Public Dan Glasses hardware reference design (RDK) | 2 | Q4 W2-W3 |
| plan-E1 (v29) | LFM2.5-VL-450M negation-collapse probe + SmolVLM2-500M head-to-head | 1 | Q3 W3 |
| plan-T1 (v29) | MatchaTTS + vocos v1.5 TTS spike | 1 | Q3 W3 |
| plan-P4+ (v29) | Adaptive Auto-Harness routing layer on top of SIA-W+H | 1 (additive) | Q3 W4 |
| plan-R1 (v29) | Hermes Agent openclaw v1.0 spike + channel-fracture verification | 1-2 | Q3 W2 |
| plan-R2 (v29) | INAR-VL edge-cloud routing layer (v1.5 differentiator) | 2 | Q1 2027 W1-W2 |

## v31 v1.0 + v1.5 Plan Additions (NEW)

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-X6 (NEW v31) | v1.0 spec §13 6-axis wedge update (paywall-free + audit-by-default) | 1 day copy | Q3 W1 |
| plan-X7 (NEW v31) | v1.0 spec §14 RAM-pricing-anchor (600MB model footprint) | 1 day copy | Q3 W1 |
| plan-X8 (NEW v31) | Karp value-chain cite in v1.0 spec §13 | 1 day copy | Q3 W1 |
| plan-X9 (NEW v31) | Rocktaschel 2-year RSI ship-date in v1.0 marketing copy | 1 day copy | Q3 W1 |
| plan-X10 (NEW v31) | Zhipu GLM-5.2 + Mistral $23.15B + Cerf agent-to-agent cites in v1.0 spec | 1 day copy | Q3 W2 |

All v28-v30 plans hold. v31 is additive (5 new plans, all 1-day copy updates, all anchored in industry-cited events).

## v31 Critical/Medium/Minor Issues (v30 hold + 5 new)

### Critical
- v30 #1-5 (all hold)
- **v31 #6 (NEW): v1.0 spec §13 must lead with the 6-axis wedge (plan-X6, Q3 W1, 1 day copy, 1 engineer).** The Meta paywall is the v31 *strongest* v1.0 differentiator in 31 versions. Wire the 6 axes in the v1.0 spec opening.

### Medium
- v30 medium #1-7 (all hold)
- v29 medium #8-9 (all hold)
- **v31 medium #10 (NEW): Karp value-chain argument cite in v1.0 spec §13 (plan-X8, Q3 W1, 1 day copy).** Karp CNBC interview is v31 the first *external* value-chain confirmation.

### Minor
- v30 minor #1-7 (all hold)
- v29 minor #8 (holds)
- **v31 minor #9-10 (NEW):** Rocktaschel 2-year RSI ship-date cite (plan-X9); Zhipu GLM-5.2 open-weights-parity cite (plan-X10). Both 1 day copy.

---

*Maintained by DAN-2. v31 deltas prepend v30. v30 9.95/10 architecture decomposition holds. v31 sharpens the v1.0 wedge to 6 axes and adds 5 new 1-day-copy plans (X6-X10), all anchored in v31 industry-cited events (Meta paywall, OpenAI -$20.9B audited, Mistral $23.15B, Karp value-chain, RAM 40-50% Q3 + 30% Q4, Rocktaschel 2-year RSI, Zhipu GLM-5.2, Cerf agent-to-agent).*

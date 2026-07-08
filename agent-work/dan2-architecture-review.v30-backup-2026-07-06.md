# Dan-2 Architecture Review — v30 (2026-07-06)

> **Status:** v30 refresh. v29 backups at `*.v29-backup-2026-07-06.md`. v29 content preserved; v30 deltas prepended.
> **Scope:** Problems, risks, suggested improvements for the Dan Glasses + danlab-multimodal stack.
> **Verdict:** v23 9.9/10 + v25 9.95/10 + v27 9.95/10 + v28 9.95/10 + v29 9.95/10 architecture decomposition **all hold**. v30 is a research delta on v29 — no architecture change, only sharper evaluation, competitive context, and the v1.0 ship-gate wedge update.

---

## v30 Deltas (this refresh — 2026-07-06 07:30 UTC / 13:00 IST)

Web-searched for fresh signals in the 2026-07-06 02:00 → 07:30 UTC window: **3 NEW CRITICAL, 4 NEW SHARPEN, 4 NEW HONORABLE MENTION** that change the picture this run.

### §A.27 (NEW v30) — Wedge: add "export-uncapturable" as the v30 fourth axis

The v29 wedge ("transparent, reversible, on-device self-improving infrastructure") sharpens to v30 with the Fable 5 export-control saga (June 12 → June 30 2026) as a v30 case study. Anthropic's Fable 5 was inaccessible to ~80% of Anthropic's user base for 18 days while the US Commerce Department issued an export-control directive (June 12) and Anthropic trained a safety filter (June 30). Fable 5 returns globally (July 1); Mythos 5 returns to "a set of US organizations" (June 26 onward).

**Architecture implication:** the v1.0 spec §13 should be rewritten as: **"Dan Glasses is the transparent + reversible + on-device + export-uncapturable alternative to the closed-source frontier."** The v30 wedge is no longer just "we don't have a closed-stack lock-in" — it is "we have a published architecture that no government can shut down by export-control directive."

**Plan-X2 (NEW v30):** v1.0 spec §13 sovereign-trust + export-uncapturable section rewrite. 1 day copy. Q3 W1. Combine v26 plan-O3 + v28 plan-S2 + v29 wedge + v30 export-uncapturable.

### §A.28 (NEW v30) — 6-entrants race becomes 5-entrants race (Apple suspended)

Apple has suspended the development of camera-equipped AirPods Pro and AirPods Ultra (July 3 2026). iOS 27 Siri AI won't widely ship until September 2026. **v30 removes Apple from the 6-entrants race**; down to 5: Meta + Samsung + Snap + Viture/NVIDIA + Danlab.

**Architecture implication:** the v1.0 marketing copy sharpens to "4 closed-stack + 1 open-stack." The "first-mover in India + open-weights" framing becomes "the only path that combines open-weights + on-device + sovereign-trust + export-uncapturable." The Dan Glasses v1.0 wedge is no longer "we beat the labs" — it is "we ship a stack no competitor is shipping."

**Plan-X1 (NEW v30):** Apple removed from 6-entrants race copy update. 1 day copy. Q3 W1.

### §A.29 (NEW v30) — Palantir + NVIDIA Nemotron sovereign stack at US-government scale (v30 first validation of plan-S2)

Palantir (NASDAQ: PLTR) + NVIDIA: AIP + Foundry + Apollo + Ontology as the deployment platform for Nemotron open models in sovereign environments, focused on US government. CEO Karp: "some U.S. government customers have recently moved away from proprietary AI models — citing Anthropic by name — toward Nvidia's open-source Nemotron models."

**Architecture implication:** the v28 plan-S2 (chip-stack sovereignty spec) is now **v30 first validated at government scale.** Danlab's v30 differentiator is the **India + non-aligned + on-device + open-weights** combination — a position Palantir-Nemotron does not serve (they are US-aligned only). v30 adds a 2027 H1 India-government partnership target (DPIIT + MeitY) modeled on the Palantir-Nemotron pattern.

**Plan-X3 (NEW v30):** India-credible wedge sharpen (Palantir+Nemotron response). 1 day copy. Q3 W1.

### §A.30 (NEW v30) — Perplexity Brain work-trace memory: 4-layer memoryd v1.5

Perplexity launched "Brain" (June 18 2026), a self-improving memory system for its agent product "Computer." Key reframing: "Most AI memory remembers the user. Brain remembers what the agent did." v30 first industry ship of a *work-trace* memory architecture.

**Architecture implication:** the v29 memoryd v1.5 three-layer model (vector store + OKF + episodic log) can be sharpened to v30 **four-layer** by adding a *work-trace* layer: when a danlab-multimodal cycle runs, the trace is stored and later retrieved when the user asks "why did you decide that?" This is the v30 **"agent remembers its own reasoning"** differentiator. Distinct from "agent remembers the user."

**Plan-X5 (NEW v30):** Perplexity Brain work-trace memory → memoryd v1.5 four-layer model. 1 day design. Q3 W2.

### §A.31 (NEW v30) — Decagon DuetBench as plan-P4 evaluation rig

Decagon introduced Duet Autopilot (June 9 2026) as "the first verified self-improving AI agent for customer experience" with DuetBench as "the industry's first benchmark for evaluating agent self-improvement end-to-end." DuetBench measures *automatic* and *verifiable* improvement, not just static performance.

**Architecture implication:** the v29 plan-P4 (SIA-W+H port, research-publishing bet) should add a DuetBench-style task that Danlab can self-publish: the danlab-multimodal loop on the danlab-captures dataset, with a verified-improvement metric. This is the v30 "**we don't just port, we evaluate**" upgrade for the Q3 W3-W4 research bet.

**Plan-X4 (NEW v30):** Decagon DuetBench self-improvement benchmark → plan-P4 evaluation rig. 1 day design. Q3 W2.

### §A.32 (NEW v30) — Recursive Superintelligence + $4.65B valuation: market-category validation

Ex-Meta Tian + Recursive Superintelligence: $650M Series A at $4.65B valuation (May 13 2026), from Alphabet's venture arm + two chipmakers. Thesis: "artificial intelligence can be engineered to improve itself, faster, in an accelerating loop."

**Architecture implication:** the v28 plan-P4 (SIA-W+H port) is no longer a research bet in the abstract — it is a bet into a **market category that has institutional validation**. The Q3 W3-W4 plan-P4 deliverable becomes the v30 "first Danlab research-publishing bet into a $4.65B market category."

### §A.33 (NEW v30) — Anthropic Claude Sonnet 5 + self-hosted Code gateway: the v1.0 OpenClaw ship-gate is the on-device equivalent

Anthropic released Claude Sonnet 5 (July 2 2026) and launched a self-hosted Claude Code gateway compatible with Amazon Bedrock and Google Cloud Vertex AI. The pitch: a "Map of AI position across multiple layers simultaneously: the model layer (Sonnet 5), the tooling layer (Claude Code), the infrastructure layer (self-hosted gateway), and the distribution layer (Bedrock + Vertex)."

**Architecture implication:** v30 sharpens v26 plan-O2 (openclaw + toold end-to-end reversibility contract): **"OpenClaw v1.0 must offer an Anthropic-Claude-Code-gateway-equivalent on the user's own machine — a self-hosted agent gateway with the same model/tool/infrastructure/distribution map, but on the user's hardware, with the user's weights, with the user's reversibility contract."** This is the v30 "we ship the on-device equivalent of what Anthropic ships on AWS/GCP" wedge.

### §A.34 (NEW v30) — Anthropic + Micron vertical integration: frontier labs are becoming memory suppliers

Micron + Anthropic strategic agreement (June 2026): memory and storage AI architecture design, supply agreement, enterprise AI adoption of Claude across Micron, and **strategic investment in Anthropic's Series H funding round**. "Collaboration spans memory and storage AI architecture design."

**Architecture implication:** the v28 §B.5 "AGI is bifurcated" framing is now industry-validated: frontier labs (Anthropic) are *vertically integrating with memory suppliers* (Micron). The v1.0 v30 memoryd bet (vector + OKF + episodic log + work-trace) is the v30 right call because the on-device + sovereign-trust wedge is *what Anthropic cannot offer*. Anthropic has the cloud; Danlab has the device.

---

## v30 v1.0 + v1.5 Plan Additions (delta on v29)

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-X1 (NEW v30) | Apple removed from 6-entrants race copy update | 1 day copy | Q3 W1 |
| plan-X2 (NEW v30) | Fable 5 export-control saga → v1.0 spec §13 "export-uncapturable" wedge update | 1 day copy | Q3 W1 |
| plan-X3 (NEW v30) | Palantir+Nemotron sovereign stack → v30 India-credible wedge sharpen | 1 day copy | Q3 W1 |
| plan-X4 (NEW v30) | Decagon DuetBench self-improvement benchmark → plan-P4 evaluation rig | 1 day design | Q3 W2 |
| plan-X5 (NEW v30) | Perplexity Brain work-trace memory → memoryd v1.5 four-layer model | 1 day design | Q3 W2 |
| plan-O2 sharpened (v30) | OpenClaw v1.0 ships as Anthropic-Code-gateway-equivalent on user's machine | (extends v26) | Q3 W2-W3 |
| plan-S2 sharpened (v30) | Chip-stack sovereignty at India-government scale (Palantir-Nemotron pattern) | (extends v28) | 2027 H1 |

All v23-v29 plans hold. v30 is additive.

---

## v30 Critical/Medium/Minor Issues (v29 hold + 4 new)

### Critical
- v29 #6 + v28 #1-5 (all hold)
- **v30 #7 (NEW): Apple removed from 6-entrants race (plan-X1, Q3 W1, 1 day copy).** v30 CRITICAL #1.
- **v30 #8 (NEW): v1.0 spec §13 "export-uncapturable" wedge update (plan-X2, Q3 W1, 1 day copy).** v30 CRITICAL #2.
- **v30 #9 (NEW): India-credible wedge sharpen via Palantir+Nemotron response (plan-X3, Q3 W1, 1 day copy).** v30 CRITICAL #3.

### Medium
- v29 medium #8-9 (all hold)
- **v30 medium #10 (NEW): Perplexity Brain work-trace memory → memoryd v1.5 four-layer model (plan-X5, Q3 W2, 1 day design).** v30 SHARPEN #4.
- **v30 medium #11 (NEW): Decagon DuetBench self-improvement benchmark → plan-P4 evaluation rig (plan-X4, Q3 W2, 1 day design).** v30 SHARPEN #1.
- **v30 medium #12 (NEW): OpenClaw v1.0 ships as Anthropic-Code-gateway-equivalent on user's machine (extends v26 plan-O2, Q3 W2-W3).** v30 SHARPEN #6.

### Minor
- v29 minor #8 (all hold)
- **v30 minor #9 (NEW): Recursive Superintelligence + $4.65B valuation → plan-P4 market-category validation cite (no spike, copy update).** v30 SHARPEN #2.
- **v30 minor #10 (NEW): Anthropic + Micron vertical integration → memoryd differentiator cite (no spike, copy update).** v30 SHARPEN #5.

---

*Maintained by DAN-2. v30 deltas prepend v29. v23 9.9/10 + v25 9.95/10 + v27 9.95/10 + v28 9.95/10 + v29 9.95/10 architecture decomposition all hold. v30 wedge: "transparent, reversible, on-device, export-uncapturable." Apple removed from 6-entrants race (down to 5). 5 new plans (X1-X5) + 2 sharpened plans (O2, S2).*

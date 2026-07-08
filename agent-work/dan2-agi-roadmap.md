# Dan-2 AGI Roadmap — v33 (2026-07-06)

> **Status:** v33 refresh. v32 backups at `*.v32-backup-2026-07-06.md`. v32 content preserved; v33 deltas prepended.
> **Scope:** 6/12/24-month Danlab execution map tied to research-report evidence.
> **Run window:** 2026-07-06 04:00 → 05:00 UTC (60 min). v32 is 1-hour-old; v33 sharpens the *execution* axis, not the *wedge* axis.

---

## v33 Deltas — execution sharpening, not wedge change

The v32 7-axis wedge holds. v33 sharpens **how** we execute against the wedge with three new external validations: (1) Microsoft Research "Agentic Evolution" 300-paper survey (July 2026) confirms the *co-evolution* frame is now industry-standard, not Danlab-fan-fiction; (2) Sakana AI formal RSI Lab (July 2026) + the v32 Anthropic Institute "RSI is human skill" *together* validate the v1.0 "co-evolution not maximalist RSI" position from *both sides of the field* (skeptical frontier lab + hyped RSI startup); (3) Gartner $234B-in-SaaS-at-risk (July 2 2026) + the v31 Microsoft Frontier Co. $2.5B + v32 Palantir $25B + v30 Karp value-chain argument *together* mean the v1.0 **enterprise implementation wedge** is now a $5B+ market conversation across 4 vendors in 90 days.

**v33 answer to "what should Danlab build?"** is sharper: **build the co-evolution layer.** Not a model. Not a chip. Not an RSI lab. The *layer* that connects human operator + agent + memory + tool, and that improves through real work, not synthetic benchmarks. Microsoft's own framing — "reliable improvement emerges not from full autonomy, but from co-evolving human–AI systems" — is the v33 strongest external validation that Danlab's v1.0 design philosophy is *the* bet to make.

### 6-month horizon (now → Q4 W3 2026, ship-gate)

**Locked. Do not re-pivot.**

| Plan | Wedge | Effort | Owner | Status |
|------|-------|--------|-------|--------|
| plan-X11 (v32): 7-axis wedge → "frontier-delayed" | Wedge | 1d copy | som/marketing | Not started |
| plan-X12 (v32): Anthropic Sonnet 5 gateway cite | Wedge | 1d copy | som/marketing | Not started |
| plan-X7 sharpen (v32): Jensen 4-year memory supply | Wedge | 1d copy | som/marketing | Not started |
| plan-X13 (v32): Apple A20 Pro + WH no-FDA + Proton Lumo 2.0 cites | Wedge | 1d copy | som/marketing | Not started |
| plan-X3 sharpen (v32): India IT services displacement | Enterprise | 1 design + 1 partnership | som | Q1 2027 |
| plan-S1 (v28): OpenClaw supervisord-equivalent | Reliability | 1 week, 1 eng | dan1 | Q4 W1 |
| plan-S2 (v28): Chip-stack sovereignty spec | Wedge | 1 week, 1 eng + 1 designer | dan1+designer | Q4 W2 |
| plan-S3 (v28): Public Dan Glasses hardware RDK | Hardware | 2 weeks, 1 eng | dan1+som | Q4 W2-W3 |
| plan-P3 (v28): SIA-H honest-RL claim | RL | 1 week, 1 eng | dan2 | Q3 W2 |
| plan-P4 (v28): SIA-W+H port | RL | 3 weeks, 1 eng | dan2 | Q3 W3-W4 |
| **plan-A (v14 → v33 sharpen): Memora storage/retrieval split port to memoryd v1.5** | **Memory** | **2 weeks, 1 eng** | **dan4** | **Q3 W1-W2 (NEW v33 priority bump)** |
| plan-M1 (v28): nomic-embed-text v1.5 vs MiniLM-L6-v2 MemDelta | Memory | 3 days, 1 eng | dan4 | Q3 W2 |
| plan-M2 (v28): LFM2.5-230M vs HRM-Text-1B vs Nemotron-4B-Q4 | Reasoning | 5 days, 1 eng | dan2 | Q3 W3 |

### 12-month horizon (Q4 2026 → Q3 2027)

**Sharpened in v33.** v33 reframes the 12-month plan as **"build the co-evolution layer, then expand the substrate."**

| Plan | Description | v33 Sharpening | Target |
|------|-------------|----------------|--------|
| **plan-CO1 (NEW v33)**: Sico-style Digital Worker shell for OpenClaw | Wrap OpenClaw agents in a Sico-style "structured AI labor unit" shell with real-work co-evolution loop (production work → supervision signal → memory write → policy update) | Microsoft Sico + survey "Agentic Evolution" (July 2026) is the v33 *frame*; v1.5 ships as `coevolve-v1` in OpenClaw | Q2 2027 |
| **plan-CO2 (NEW v33)**: Memory architecture split | Port Memora's storage/retrieval split to memoryd v1.5: separate `store_d` (write path) and `retrieve_d` (read path) with two-stage retrieval (vector + graph + LLM rerank) | Microsoft *also* independently arrived at this architecture (July 2026) — validation | Q1 2027 (Q3 W1-W2 to start) |
| plan-X14 (v33): Hermes Agent openclaw drop-in | Add Hermes Agent as a v1.0 OpenClaw plan-A option alongside OpenClaw-native (1-2 week drop-in) | Hermes 180k+ stars + 4.4k awesome-list + Eden AI "strongest self-hosted harness" | Q4 W1 (1 week) |
| plan-X15 (v33): 5-org RSI landscape in v1.0 spec §15 | New spec section: Sakana RSI Lab + Anthropic Institute + Recursive Superintelligence + Mirendil + Andrew Ng. Frame Danlab as the *audit-by-default, co-evolution* layer when these ship. | Sakana formal RSI Lab (July 2026) is the v33 *third* RSI org | Q3 W3 (1 day copy) |
| plan-X16 (v33): "AI revolution will not be televised — it'll be quantized" cite | The New Stack (July 5 2026) on Chinese frontier models + quantization as the v33 frontier-access wedge | Quantization is the v33 supply-chain answer; v1.0 v32 619MB footprint is *quantization-first* by design | Q3 W2 (1 day copy) |
| plan-X17 (v33): local.ai (Exo Labs + NVIDIA) cite | local.ai launched at AI Engineer World's Fair (July 2 2026) — chipmaker-blessed local-inference path | NVIDIA is now *explicitly* backing local AI infrastructure; v1.0 OpenClaw + on-device stack is *industry-aligned* | Q3 W2 (1 day copy) |
| plan-X18 (v33): Anthropic Mythos 5 Glasswing cite | Anthropic re-launching Mythos 5 in Glasswing program (June 30 2026 — 18-day ban cycle) | The 18-day ban → Glasswing re-launch is the v33 *most-citable* export-control risk story for v1.0 spec §13 | Q3 W1 (1 day copy) |
| plan-X19 (v33): Foxconn +40% YoY cite | Foxconn Q2 2026 revenue +39.8% YoY (Reuters July 5) — supply-chain *funded* signal | The supply chain is *pricing in* the v1.0 demand; v1.0 v32 619MB footprint is the v33 *only* way to be on the right side of this curve | Q3 W1 (1 day copy) |
| plan-X20 (v33): Sakana RSI Lab as v1.0 "second-mover" RSI positioning | Sakana is sample-efficiency-first, closed-weights, Tokyo-based. Danlab is open-weights, on-device, India-based. *Different wedges — both ship before maximalist RSI.* | The v33 best RSI positioning is "we are not racing Sakana, we are the *edge* co-evolution layer" | Q3 W3 (1 day copy) |
| plan-J (v25): ASPIRE skill library port | Port Anthropic Skills + skill libraries to OpenClaw skill format | Skill libraries are now the v33 *de facto* agent marketplace | Q1 2027 |
| plan-X3 (v32): India IT services partnership | TCS, Wipro, Infosys reorienting to AI-agent-first workforce. v1.0 self-hosted agentic gateway is the v32 *Indian IT services displacement target* | Sharpened in v33 with Reuters India IT AI hiring + Indian sovereign-AI 3-bloc frame | Q1 2027 |

### 24-month horizon (Q3 2027 → Q3 2028)

**Adjusted in v33.** v33 sharpens the 24-month bet: **co-evolution + multi-agent + chip sovereignty.** v32 had this as a softer "expansion" phase. v33 makes it a *named* phase.

| Plan | Description | v33 Sharpening | Target |
|------|-------------|----------------|--------|
| **plan-CO3 (NEW v33)**: Multi-Digital-Worker orchestration | Multiple Sico-style Digital Workers (memoryd + perceptiond + audiod + ttsd + 3rd-party) coordinated by OpenClaw Octopus Orchestrator | Sico survey "Agentic Evolution" validates the *Digital Worker* unit as the v33 *primary agent abstraction* | Q2 2028 |
| **plan-CO4 (NEW v33)**: Co-evolution memory backend | Memoryd v2.0: storage/retrieval split (Memora pattern) + Ebbinghaus decay (MemPalace pattern) + context-graph (enterprise AI survey pattern) | Three independent 2026 validations: Memora (Microsoft), MemPalace (Cognify), context graph (Enterprise Times July 1 2026) | Q3 2028 |
| plan-S4 (NEW v33): Chip-stack sovereignty cert | Public certification that v1.0 stack runs on Snapdragon AR1 / AR2 / MediaTek / Rockchip without NVIDIA lock-in | Apple A20 Pro WMCM (v32) + OnePlus N6 4GB (v32) + Samsung/SK Hynix $518B fab buildout (v33) = supply chain is *funded* | Q4 2027 |
| plan-RS1 (v28): SIA-W+H honest RL | SIA-W+H fork as research-publishing bet (ICLR/NeurIPS 2028) | Felix Chau SIA concrete numbers + Sakana RSI Lab = v33 *most-credible* self-improvement research path | Q1 2028 |
| plan-P5 (NEW v33): Sico co-evolution interoperability | OpenClaw agents interoperate with Sico Digital Workers via MCP — Danlab is the *co-evolution edge* | Microsoft's Sico is open-source (July 2026) and the v33 *natural partner* | Q2 2028 |
| plan-E1 (v29): Export-uncapturable hardware reference design | Reference design for v1.0 hardware that cannot be retrofitted with a closed-source subsystem | The v33 *Sovereign* chip + hardware bet | Q3 2028 |

### v33 critical retractions / adjustments

- **None.** v32 plans X11, X12, X13, X3-sharpen, P3, P4, S1, S2, S3 all hold. v33 *adds* plans, does not *retract*.
- v33 5 new plans: CO1 (Sico-style DW shell), CO2 (Memora port), X14 (Hermes), X15 (RSI landscape), X16 (quantization), X17 (local.ai), X18 (Glasswing), X19 (Foxconn), X20 (Sakana) — total 9 new plan names; X15-X20 are 1-day copy + spec, CO1/CO2 are 1-2 week engineering.
- v33 2 sharpened plans: plan-A (Memora port, priority bumped to Q3 W1-W2), plan-X3 (India IT services partnership, design phase Q1 2027).
- v33 2 named phases: **co-evolution (6-12mo)** + **multi-agent + chip sovereignty (12-24mo)**.

### v33 18-step → 22-step marketing narrative (per v32 + v33 deltas)

The v32 22-step narrative now extends to **22 steps** with the v33 *co-evolution* step as the closing:

1. Anthropic Mythos 5 banned June 12 (export-control risk)
2. Anthropic Fable 5 export-controlled for 18 days
3. OpenAI -$20.9B audited operating loss
4. Karp: "per-token pricing is completely wrong"
5. Meta paywalls on-device Conversation Focus $20/mo
6. Anthropic Sonnet 5 + self-hosted Claude Code gateway (validate the application-layer race)
7. Jensen: memory-chip supply shortage "several years"
8. Nvidia Kyber delayed to 2028 (frontier-delayed)
9. SK Hynix $29B US IPO (supply-chain funded)
10. Foxconn +40% YoY (supply-chain priced-in)
11. Apple A20 Pro WMCM (on-device AI forced Apple to redesign)
12. White House no-FDA-regulator
13. Proton Lumo 2.0 127-240% gap-closed (privacy-first is now capable)
14. Mistral $23.15B / Forge (EU sovereign-AI market-cap)
15. India IT AI hiring outpaces overall IT
16. OpenNebula + Waldur (EU infrastructure-mature)
17. Jack Clark: 60% RSI by 2028 (outer-loop already in flight)
18. Sakana RSI Lab + Recursive Superintelligence + Mirendil + Anthropic Institute
19. Microsoft Frontier Co. $2.5B + Palantir $25B (enterprise implementation wedge)
20. Gartner $234B SaaS-at-risk (agentic AI displaces SaaS)
21. **Microsoft Sico + 300-paper Agentic Evolution survey (co-evolution is now the frame)**
22. **Danlab ships the co-evolution layer before the frontier catches up**

**v33 closes the narrative on co-evolution.** v1.0 marketing copy: "the AI revolution will not be televised — it'll be *co-evolved*."

---

## v33 Top 5 Recommendations for somdipto

1. **Q3 W1-W2: Memora storage/retrieval split port to memoryd v1.5 (plan-A sharpen, 2 weeks, 1 eng)** — Microsoft *also* independently arrived at the same architecture (July 2026). Two-week engineering spike, huge wedge benefit (retrieval is the v32 DynamicMem 93%-failure-cause).
2. **Q3 W1: 5 new 1-day spec copy plans (X15, X16, X17, X18, X19) — total 5 days engineering-free** — adds the v33 Sakana/local.ai/Glasswing/Foxconn/quantization cites to v1.0 spec §13-§15.
3. **Q4 W1: Hermes Agent openclaw plan-A drop-in (plan-X14, 1 week, 1 eng)** — Hermes is the v33 most-invested self-hosted agent framework. 1-week drop-in gives Danlab the *optionality* to switch if OpenClaw development stalls.
4. **Q2 2027: Sico-style Digital Worker shell for OpenClaw (plan-CO1, 2-3 weeks, 1 eng)** — v33 closes the 24-month plan with a *named* co-evolution phase. This is the v33 most-strategic engineering bet.
5. **Q3 W2: spec §15 "5-org RSI landscape" (plan-X15, 1 day copy)** — name the field (Sakana + RSI + Mirendil + Anthropic Institute + Andrew Ng) and position Danlab as the *audit-by-default, co-evolution* layer.

## v33 Open Questions for somdipto

1. Memora port priority: confirm Q3 W1-W2 start (recommend: yes)
2. Hermes Agent plan-A drop-in priority: confirm Q4 W1 (recommend: yes)
3. Sico co-evolution shell: confirm Q2 2027 + 1 eng dedicated (recommend: yes, this is the v33 24-month bet)
4. v1.0 spec §15 "5-org RSI landscape" addition (recommend: yes, 1 day copy)
5. v1.0 spec §13 Glasswing 18-day-ban cite (recommend: yes, 1 day copy)
6. v1.0 spec §14 Foxconn +40% YoY cite (recommend: yes, 1 day copy)
7. v33 "co-evolution" as the v1.0 marketing closing frame (recommend: yes, replace "audit-by-default" with "co-evolution + audit-by-default")
8. Hermes Agent vs OpenClaw plan-A/B (recommend: OpenClaw primary, Hermes as plan-B switch option)
9. plan-CO3 multi-Digital-Worker orchestration scope (recommend: scope to 2 workers first, expand Q3 2028)
10. plan-P5 Sico interoperability timing (recommend: Q2 2028, post-v1.5)

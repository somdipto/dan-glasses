# Danlab AGI Roadmap — v28 (2026-07-06)

> **Status:** v28 refresh. v27 content preserved. v28 deltas prepended.
> **Scope:** 6/12/24-month plan with 3 specific decisions for somdipto.
> **Verdict:** v23 15-step narrative + v25 16-step narrative + v26 17-step narrative + v27 narrative **all hold**. v28 adds an 18th step and reframes the 24-month plan around outer-loop RSI.

---

## v28 Deltas (this refresh — 2026-07-06)

### 18th step (v28 NEW) — Outer-loop RSI: Danlab itself runs on a self-improving loop before the models do (Import AI #460)

Jack Clark (Import AI #460, July 2026) distinguishes maximalist RSI (60% by 2028) from prosaic RSI (outer-loop productivity compounding, already happening at Anthropic with 8x increase in lines-of-code merged).

**v28 reframing:** the AGI roadmap should distinguish:
- **Outer-loop RSI (in flight now):** the audiod v1.3 → v1.4 → v1.5 shipping cadence, the dan2 research-task auto-refresh, and the foundation-stream lock are all outer-loop RSI infrastructure. **Already in flight.**
- **Maximalist RSI (60% by 2028):** AI designing its own successor. **Not the v1.0 bet; defer to v2.0+ (2028+).**

**v28 18-step narrative:** add "the 2026 outer-loop RSI is already in flight at Anthropic (8x LOC merged) and at Danlab (audiod v1.3→v1.5, dan2 v23→v28); the maximalist RSI is 60% by 2028 (Jack Clark); Danlab is shipping the v1.0 sovereign-trust + chip-sovereignty + reversibility wedge **before** the maximalist-RSI inflection point."

### 24-month plan: own silicon or fail (v28 NEW directional bet)

NVIDIA XR AI open-source library + viture Helix reference platform ship on Snapdragon AR1 Gen 2 (Qualcomm) and NVIDIA Jetson Orin. The closed-source frontier is now **chip-locked** to NVIDIA, Qualcomm, and (in China) Huawei Ascend + Cambricon.

**v28 24-month bet:** by 2028 H2, Danlab must have either (a) a custom RISC-V neural accelerator partnership, or (b) a non-NVIDIA, non-Qualcomm, non-Huawei chip path. **Risk-adjusted recommendation:** partner with MediaTek for v1.5; explore RISC-V for v2.0.

### 6-month plan: ship public Dan Glasses hardware reference design (RDK) by Q4 2026 (v28 NEW)

The 2026 H2 wearable race is closing. Meta, Apple, Samsung, Snap, viture/NVIDIA all shipping or testing. **By Q4 2026 W3, Danlab must publish a public Dan Glasses hardware reference design (RDK) — even if the physical product is not yet manufacturable.** The open RDK can attract India-based manufacturers and secure the India-credible position before Meta/Apple/Samsung dominate.

**v28 6-month plan-Q4 OKR:** public Dan Glasses hardware RDK (schematic, BOM, mechanical reference, firmware reference) by Q4 2026 W3.

### 12-month plan: SIA-W+H research-publishing bet (v28 NEW)

The v23-v27 plan deferred SIA-W+H to v1.5+. v28 promotes SIA-W+H to a **research-publishing bet** in Q3 2026 W3-W4 (3 weeks, 1 engineer). Concrete third-party numbers (45%→70% on legal task, 14× kernel speedup) make this a credible ICLR/NeurIPS submission if the port replicates them on a Dan Glasses-relevant task (e.g., audiod segment timing optimization, memoryd retrieval re-ranking).

### 12-month plan: v1.0 spec §13 "Sovereign trust + chip sovereignty + reversibility" headline marketing wedge (v28)

Combines v26 plan-O3 (sovereign trust + reversibility) with v28 plan-S2 (chip sovereignty). The combination of data sovereignty + chip sovereignty + reversibility is the only credible v1.0 wedge against the 6-entrants closed-stack race.

### 24-month plan: hermes-agent as openclaw v1.0 default, SIA-W+H as v1.5 research bet (v28)

Hermes Agent (Nous Research, late June 2026) outperforms Claude Opus + GPT-5.5 on hard agentic benchmarks by 11%. v28 promotes Hermes Agent to v1.0 openclaw agent framework plan-A (1-2 weeks drop-in, Q3 W2). SIA-W+H remains the v1.5 research bet.

---

## 6-Month Plan (Q3-Q4 2026) — v28

| Week | Plan | Description | Engineer-weeks |
|------|------|-------------|---------------|
| Q3 W1 | plan-O1 (v26) | toold sovereign-trust audit | 1 |
| Q3 W1 | plan-O3 (v26) | v1.0 spec §13 sovereign-trust section | 1 day copy |
| Q3 W1 | plan-N1 (v25) | toold strict-mode | 1 |
| Q3 W1 | plan-N2 (v25) | openclaw shell-call audit | 1 |
| Q3 W2 | plan-P3 (v28 NEW) | SIA-H honest-RL claim (danlab-multimodal → prompt-edit RL) | 1 |
| Q3 W2 | plan-M2 (v28 NEW) | LFM2.5-230M vs HRM-Text-1B vs Nemotron-4B-Q4 reasoning benchmark | 1 |
| Q3 W2 | Hermes Agent spike (v28) | openclaw v1.0 agent framework drop-in | 1-2 |
| Q3 W3 | plan-O2 (v26) | openclaw + toold end-to-end reversibility contract | 3 |
| Q3 W3 | plan-P1 (v27) + plan-M1 (v28) | MemDelta-controlled embedding baseline (MiniLM-L6-v2 vs bge-small vs nomic-embed-text v1.5) | 1 |
| Q3 W3 | plan-P2 (v27) | memoryd OKF adapter spike | 1 |
| Q3 W3 | plan-S2 (v28) | Chip-stack sovereignty spec | 1 |
| Q3 W4 | plan-P4 (v28) | SIA-W+H port (LoRA training in the loop) | 3 (W3-W4) |
| Q3 W4 | v26 17-step + v28 18-step narrative | Update v1.0 marketing to 18-step narrative | 1 day copy |
| Q4 W1 | plan-S1 (v28) | OpenClaw supervisord-equivalent (daemon restart on crash) | 1 |
| Q4 W2 | plan-S2 (v28 continued) | Chip-stack sovereignty final spec | (continued) |
| Q4 W2-W3 | plan-S3 (v28 NEW) | Public Dan Glasses hardware RDK | 2 |
| Q4 W3 | v1.0 ship-gate | Lock the v1.0 spec, all 18-step narrative, all plan-O/P/S items | — |

**Q4 2026 W3 hard date:** v1.0 ship-gate. After Q1 2027, the 6-entrants race saturates the category.

---

## 12-Month Plan (Q1-Q2 2027) — v28

- **v1.5 chip-stack:** MediaTek (Helix G99) or RISC-V neural accelerator exploration.
- **v1.5 model upgrade:** LFM2.5-VL-1.2B (if released), Parakeet-TDT-0.6B (STT), Kokoro-82M (TTS).
- **v1.5 memoryd:** Summary RAG + co-occurrence-aware KB reorganization.
- **v1.5 toold:** Execution-graph + skill-routing (Alibaba SkillWeaver pattern).
- **v1.5 publishing:** ICLR/NeurIPS submission of the SIA-W+H port.
- **v1.5 spec §14:** Outer-loop RSI at Danlab — the lab-as-self-improving-system.

---

## 24-Month Plan (Q3 2027 - Q2 2028) — v28

- **Custom silicon exploration:** RISC-V neural accelerator partnership.
- **v2.0 form factor:** Display AR (JBD MicroLED + 2x 200mAh, deferred from v23 plan).
- **v2.0 reasoning:** HRM-Text-1B + SIA-W+H + Hermes Agent + LFM2.5-1.2B-Thinking.
- **v2.0 spec §15:** Maximalist RSI readiness — the lab is prepared for AI designing its own successor.

---

## v28 Top 3 Recommendations for somdipto

1. **Ship the SIA-H honest-RL claim in Q3 W2 (plan-P3, 1 week, 1 engineer).** This is the v28 first honest "we run RL" claim Danlab can make. Promotes danlab-multimodal from "demo" to "research artifact."

2. **Lock the wearable form factor (display-less) and chip-stack path (Snapdragon AR1 Gen 2) by Q3 W3 (plan-S2, 1 week, 1 engineer + 1 designer).** v28 CRITICAL #2 says chip-stack sovereignty is the new axis. Display-less is the v28 simplification that the v1.0 spec should consider.

3. **Ship the public Dan Glasses hardware RDK in Q4 W3 (plan-S3, 2 weeks, 1 engineer).** The v28 H2-2026-closing-window bet. Even if the physical product is not yet manufacturable, the open RDK can attract India-based manufacturers and secure the India-credible position before Meta/Apple/Samsung dominate.

---

## v28 Open Questions for somdipto

1. SIA-H honest-RL claim priority (recommend Q3 W2, 1 week, 1 engineer).
2. SIA-W+H port priority (recommend Q3 W3-W4, 3 weeks, 1 engineer — consider this a research-publishing bet).
3. Chip-stack sovereignty decision (recommend Q3 W3 1-day design review, 1 engineer + 1 designer).
4. Display-less form-factor decision (recommend: yes, ship display-less v1.0).
5. Public Dan Glasses hardware RDK priority (recommend Q4 W2-W3, 2 weeks, 1 engineer).
6. v1.0 spec §13 + §14 ship-gate (recommend Q3 W3 + Q4 W3, 1+1 day copy, 1 engineer).

---

*Maintained by DAN-2. v23 9.9/10 + v25 9.95/10 + v27 9.95/10 architecture decomposition all hold. v28 reframes the 24-month plan around outer-loop RSI and adds a Q4 2026 W3 hard date for v1.0.*

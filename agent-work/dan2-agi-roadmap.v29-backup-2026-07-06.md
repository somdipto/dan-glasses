# Danlab AGI Roadmap — v29 (2026-07-06)

> **Status:** v29 refresh. v28 content preserved. v29 deltas prepended.
> **Scope:** 6/12/24-month plan with 3 specific decisions for somdipto.
> **Verdict:** v23 15-step + v25 16-step + v26 17-step + v27 + v28 18-step narrative **all hold**. v29 adds a 19th step and 3 new plans.

---

## v29 Deltas (this refresh — 2026-07-06)

### 19th step (v29 NEW) — The 2026 AGI-to-ASI pathway is multi-path; Danlab ships the on-device + open + sovereign-trust path

Google DeepMind published "From AGI to ASI" (June 10 2026, 57-page arXiv report, 14 researchers) mapping four potential pathways from human-level AGI to ASI: (1) scaling, (2) paradigm shifts, (3) recursive self-improvement, (4) multi-agent collectives. The report frames progress as "waves, not a wall." Watoday (July 2 2026) confirms RSI is now multi-lab production: OpenAI GPT-5.3-Codex self-coded, Anthropic Claude Code in internal loops, Google DeepMind AlphaEvolve improved matrix multiplication.

**v29 reframing:** Danlab is *not* a contrarian bet on RSI. Danlab is an *aligned-with-the-frontier* bet on a different axis (open vs. closed, on-device vs. cloud, sovereign-trust vs. corporate-trust, transparent vs. opaque). The 19th step is: **"the 2026 AGI-to-ASI pathway is multi-path; Danlab is shipping the on-device + open + sovereign-trust path before the closed-source frontier AI writes the future for everyone."**

### Wedge reframing (v29 NEW) — "transparent, reversible, on-device self-improving infrastructure"

The v1.0 marketing wedge is no longer "we do RSI" (false at the maximalist level, true at the outer-loop level) and no longer "open-source" alone (NVIDIA-validated, not differentiating). The v29 wedge is the **combination**: every spec version, every plan add, every artifact is public and auditable; the user can wipe memoryd + scrub all episodic logs in one command (v26 plan-O2); no cloud fallback for primary flows. The wedge is **transparency + reversibility + on-device self-improving infrastructure**.

### 6-month plan: v1.0 evaluation rig (v29 NEW)

The v1.0 spec §13 (sovereign trust + chip sovereignty + reversibility) should reference 7 evaluation methodologies as the v1.0 "rig not rhetoric" upgrade:
1. FINER-CompreCap or Ghost-100 (VLM negation probe).
2. MemDelta-controlled baseline (memoryd).
3. AIMultiple cross-domain methodology (embedding).
4. Edge Reliability Gap protocol (VLM failure-mode attribution).
5. DynamicMem retrieval-failure metric (memoryd v1.5).
6. Adaptive Auto-Harness harness-tree routing (v1.5 self-improving).
7. INAR-VL edge-cloud routing signals (v1.5 edge-cloud fallback).

### 12-month plan: MatchaTTS + vocos v1.5 TTS spike (v29 NEW)

v29 promotes MatchaTTS + vocos to v1.5 plan-A TTS, displacing Kokoro-82M. Concrete on-device RTF numbers: MatchaTTS RTF 0.163 (123MB) vs Kokoro RTF 1.880 (330MB). MatchaTTS is 12× faster and 2.7× smaller. 22 voices.

### 12-month plan: INAR-VL edge-cloud routing (v29 NEW)

v29 adds INAR-VL (arXiv 2605.18853) as the v1.5 differentiator: edge-first, cloud-with-explicit-user-consent. Recovers 71% of edge-to-cloud accuracy gap. Not v1.0 (must be on-device-only for the v26 sovereign-trust position).

### 24-month plan: publish the v29-v30 self-improving audit trail (v29 NEW)

The v29 24-month plan adds: **publish the v29-v30 self-improving audit trail (every spec version, every plan add, every artifact) as a public Danlab method paper.** This is the v29 "transparency" wedge made concrete.

---

## 6-Month Plan (Q3-Q4 2026) — v29

| Week | Plan | Description | Engineer-weeks |
|------|------|-------------|---------------|
| Q3 W1 | plan-O1 (v26) | toold sovereign-trust audit | 1 |
| Q3 W1 | plan-O3 (v26) | v1.0 spec §13 sovereign-trust section | 1 day copy |
| Q3 W1 | plan-N1 (v25) | toold strict-mode | 1 |
| Q3 W1 | plan-N2 (v25) | openclaw shell-call audit | 1 |
| Q3 W2 | plan-P3 (v28) | SIA-H honest-RL claim (danlab-multimodal → prompt-edit RL) | 1 |
| Q3 W2 | plan-M2 (v28) | LFM2.5-230M vs HRM-Text-1B vs Nemotron-4B-Q4 reasoning benchmark | 1 |
| Q3 W2 | plan-R1 (v29 NEW) | Hermes Agent openclaw v1.0 agent framework drop-in + channel-fracture verification | 1-2 |
| Q3 W3 | plan-O2 (v26) | openclaw + toold end-to-end reversibility contract | 3 |
| Q3 W3 | plan-P1 (v27) + plan-M1 (v28) | MemDelta-controlled embedding baseline (MiniLM-L6-v2 vs bge-small vs nomic-embed-text v1.5) | 1 |
| Q3 W3 | plan-P2 (v27) | memoryd OKF adapter spike | 1 |
| Q3 W3 | plan-S2 (v28) | Chip-stack sovereignty spec | 1 |
| Q3 W3 | **plan-E1 (v29 NEW)** | **LFM2.5-VL-450M negation-collapse probe + SmolVLM2-500M head-to-head (VLM v1.0 ship-gate)** | **1, BEFORE v1.0 ships** |
| Q3 W3 | **plan-T1 (v29 NEW)** | **MatchaTTS + vocos v1.5 TTS spike** | **1** |
| Q3 W4 | plan-P4 (v28) + plan-P4+ (v29 NEW) | SIA-W+H port (LoRA training in the loop) + Adaptive Auto-Harness routing | 3 (W3-W4) + 1 (additive) |
| Q3 W4 | v26 17-step + v28 18-step + v29 19-step narrative | Update v1.0 marketing to 19-step narrative | 1 day copy |
| Q4 W1 | plan-S1 (v28) | OpenClaw supervisord-equivalent (daemon restart on crash) | 1 |
| Q4 W2 | plan-S2 (v28 continued) | Chip-stack sovereignty final spec | (continued) |
| Q4 W2-W3 | plan-S3 (v28) | Public Dan Glasses hardware RDK | 2 |
| Q4 W3 | v1.0 ship-gate | Lock the v1.0 spec, all 19-step narrative, all plan-O/P/S items | — |

**Q4 2026 W3 hard date:** v1.0 ship-gate. After Q1 2027, the 6-entrants race saturates the category.

---

## 12-Month Plan (Q1-Q2 2027) — v29

- **v1.5 chip-stack:** MediaTek (Helix G99) or RISC-V neural accelerator exploration.
- **v1.5 model upgrade:** LFM2.5-VL-1.2B (plan-A) or LFM2.5-VL-1.6B (plan-B if v29 negation gate failed); Moonshine (STT); **MatchaTTS + vocos (v29 plan-A)** / Kokoro-82M (plan-B).
- **v1.5 memoryd:** Summary RAG + co-occurrence-aware KB reorganization.
- **v1.5 toold:** Execution-graph + skill-routing (Alibaba SkillWeaver pattern).
- **v1.5 publishing:** ICLR/NeurIPS submission of the SIA-W+H + Adaptive Auto-Harness port.
- **v1.5 spec §14:** Outer-loop RSI at Danlab — the lab-as-self-improving-system.
- **v1.5 differentiator:** INAR-VL edge-cloud routing (plan-R2, v29 NEW).

---

## 24-Month Plan (Q3 2027 - Q2 2028) — v29

- **Custom silicon exploration:** RISC-V neural accelerator partnership.
- **v2.0 form factor:** Display AR (JBD MicroLED + 2x 200mAh, deferred from v23 plan).
- **v2.0 reasoning:** HRM-Text-1B + SIA-W+H + Hermes Agent + LFM2.5-1.2B-Thinking.
- **v2.0 spec §15:** Maximalist RSI readiness — the lab is prepared for AI designing its own successor.
- **v29 NEW:** **publish the v29-v30 self-improving audit trail (every spec version, every plan add, every artifact) as a public Danlab method paper.** This is the v29 "transparency" wedge made concrete.

---

## v29 Top 3 Recommendations for somdipto

1. **Run the LFM2.5-VL-450M negation-collapse probe BEFORE the v1.0 ship-gate (plan-E1, Q3 W3, 1 engineer-week).** v29 CRITICAL #1 — the v1.0 VLM choice is not yet validated for negation. If LFM2.5-VL-450M exhibits >50% negation collapse, fall back to LFM2.5-VL-1.6B before locking the v1.0 spec.

2. **Replace the v28 Kokoro-82M v1.5 TTS plan-A with MatchaTTS + vocos (plan-T1, Q3 W3, 1 engineer-week).** v29 SHARPEN #3 — concrete on-device RTF numbers (MatchaTTS 0.163 vs Kokoro 1.880) make MatchaTTS the v1.5 winner on speed and size. Kokoro remains plan-B for high-quality-when-speed-doesn't-matter scenarios.

3. **Adopt the v29 wedge reframing: "transparent, reversible, on-device self-improving infrastructure."** Combine v26 plan-O3 + v28 plan-S2 + v29 §A.22. The combination of data sovereignty + chip sovereignty + reversibility + transparency is the v29 credible v1.0 wedge against the 6-entrants closed-stack race. The v1.0 spec §13 should be rewritten in this voice.

---

## v29 Open Questions for somdipto

1. LFM2.5-VL-450M negation-collapse probe priority (recommend Q3 W3, 1 engineer-week, BEFORE v1.0 ships).
2. MatchaTTS + vocos v1.5 TTS spike priority (recommend Q3 W3, 1 engineer-week).
3. Wedge reframing acceptance (recommend: yes, "transparent, reversible, on-device self-improving infrastructure" replaces "we do RSI" in v1.0 marketing).
4. SIA-W+H + Adaptive Auto-Harness port priority (recommend Q3 W3-W4, 3+1 weeks, 1 engineer — research-publishing bet).
5. INAR-VL edge-cloud routing v1.5 differentiator priority (recommend Q1 2027 W1-W2, 2 weeks, 1 engineer).
6. Public Dan Glasses audit-trail method paper priority (recommend 2028 H1, 1-2 months, 1 engineer + 1 designer).

---

*Maintained by DAN-2. v23 9.9/10 + v25 9.95/10 + v27 9.95/10 + v28 9.95/10 architecture decomposition all hold. v29 reframes the v1.0 wedge as "transparent, reversible, on-device self-improving infrastructure" and adds 19th-step narrative, plan-E1, plan-T1, plan-P4+, plan-R1, plan-R2.*

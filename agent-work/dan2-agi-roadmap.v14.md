# Danlab AGI Roadmap v14 — 6 / 12 / 24 Months
**Author:** Dan2 (lead scientist / architect)
**Date:** 2026-06-19 10:30 IST
**Supersedes:** dan2-agi-roadmap.v13 (24 hours old)

---

## 0. Headline (v14 deltas from v13)

**Mission (unchanged).** The most credible *edge* path to AGI: a sub-500 MB multimodal model, on a sub-$100 aarch64 board, on a 2500 mAh battery, for 4 hours, with an always-on memory loop and an audit-trail self-improvement harness.

**v14 changes to the plan:**

1. **W26 (NEW): privacyd as compliance attestation product.** 4 weeks. OSS / $99 / $999 pricing tiers. The Lutnick-letter resolution this week is the unlock.
2. **Snapdragon Start application added to W0 (★).** Apply this week. Parallel silicon path to Redax for wearable v2.
3. **Apple 2027 = biggest product year in history** (Gurman, June 18). The Apple-window may compress further. **Ship v1.0 by Q4 2026 is now a hard deadline, not a target.**
4. **W2.5 (NEW): Arbor benchmark added to SIA workstream.** 2 weeks. Validates the "cumulative learning > trial-and-error" pattern with public numbers.
5. **OpenAI Shazeer move** validates our non-transformer architecture bets. LFM2.5 + HRM + Mnemosyne are less contrarian than v13 thought.

**Mission posture (unchanged from v13).** Lane 5 of 5 (edge / on-device). The 5-lane AGI framing (Closed / Open / RSI / Inference / Edge) is the v14 update from v13's 4-lane.

## 1. Time Horizons (unchanged from v13)

| Horizon | Window | Anchor | Single sentence |
|---|---|---|---|
| **6 months** | Jun – Dec 2026 | Foundation | Characterized, reproducible edge-AI reference stack on a known dev board, with auditable self-improvement + commercial privacyd launch. |
| **12 months** | Dec 2026 – Jun 2027 | V1.5 wearable | First real wearable unit (Snapdragon Start or Redax silicon), always-on perception, auditable self-improvement. |
| **24 months** | Jun 2027 – Jun 2028 | Product | A product a paying user wears all day and trusts. |

Each horizon has a hard **go/no-go gate**. If the gate fails, the next horizon is replanned, not skipped.

## 2. Six-Month Roadmap (Jun – Dec 2026) — "Foundation"

**Gate to pass:** working OpenClaw + perceptiond + memoryd loop on a Pi 5 with measured W/frame, p95 latency, and thermal curve. **Plus:** v1.0 .deb ships with signed skills and an auditable self-improvement benchmark. **Plus:** privacyd v1 commercial launch with $99/$999 customers.

### 2.1 Workstreams (v14 deltas marked with **★**)

| # | Workstream | Lead | Duration | Deliverable | v14 delta |
|---|---|---|---|---|---|
| W0★ | **OpenClaw signed-skill infra + Snapdragon Start app** | Dan1 + Somdipto | 1 week | cosign + Rekor for all Danlab skills; default-deny policy; **Snapdragon Start application submitted** | **Snapdragon Start added** |
| W1 | **Pi 5 / Orange Pi 5 power & perf** | Dan2 | 4 weeks | `power-characterization.md` with measured W/frame, p95 latency, thermal | unchanged |
| W1.5★ | **LFM2.5-Audio-1.5B benchmark** | Dan2 | 2 weeks | Audiod + ttsd collapse evaluation | unchanged |
| W2 | **SIA fork in danlab-multimodal** | Dan2 | 6 weeks | First SIA-H run with GLM-5.2 Feedback-Agent | **Arbor benchmark added W2.5** |
| W2.5★ | **Arbor vs SIA-H benchmark** | Dan2 | 2 weeks | Comparison on same task set | **NEW v14** |
| W3 | **`evented` aggregator** | Dan2 | 3 weeks | Single pubsub stream, replayable | unchanged |
| W4 | **`stated` snapshot service** | Dan2 | 2 weeks | Union-of-health `state.json` writer, 2 s cadence | unchanged |
| W5 | **`clawd-watchdog`** | Dan2 | 1 week | systemd unit, 30 lines | unchanged |
| W6 | **OpenClaw MCP tool coverage** | Dan1 | 4 weeks | `perception_search`, `memory_query`, `os_exec`, `tts_speak` MCP tools | unchanged |
| W7 | **Bootstrap wizard v1** | Dan1 | 3 weeks | Camera permission, model download, language, Telegram, OpenClaw auth | unchanged |
| W8 | **`.deb` packaging for laptop** | Dan2 | 3 weeks | All five services + gateway + Tauri, signed (GPG + cosign) | unchanged |
| W9 | **Memoryd v1.5 (Mnemosyne + LFM2.5-Embedding-350M + UaC)** | Dan2 | 6 weeks | Mnemosyne swap, embedding swap, Eywa provenance, UaC schema, RHO consolidation | unchanged |
| W10 | **LFM2.5-VL-1.6B-Extract spike** | Dan3 | 1 week | Does structured-JSON output satisfy `toold` invocation path? | unchanged |
| W11 | **DPDP Act + EU AI Act compliance review** | Somdipto | 4 weeks | Formal compliance review of v1.0 .deb | unchanged |
| W22★ | **Open-source "Dan Glasses Kit" — Day-1 promise** | Dan1 | 12 weeks | Public repo, .deb + Pi 5 reference + OpenClaw config + Tauri app, Apache 2.0 | unchanged |
| **W26★** | **privacyd as compliance attestation product** | Dan2 + Dan1 | 4 weeks | OSS / $99 / $999 tiers, fable-5-safe / mythos-5-safe / EU AI Act / DPDP profiles, sigstore Rekor | **NEW v14** |

### 2.2 Hard go/no-go gate (Dec 2026)

**v13 gate items, unchanged:**
- W1 report shows Q4_0 VLM ≤ 4.5 W on Pi 5.
- W1 report shows IQ2_XXS VLM ≤ 2.5 W with <8% quality regression.
- W2 published a SIA-H run with reproducible gain or null-result note.
- W3 + W4 + W5 live in dev with green end-to-end demo.
- W8 .deb installs cleanly on Ubuntu 24.04 and survives upgrade.
- W9 schema migration reversible.

**v14 NEW gate items:**
- **W0** Snapdragon Start application submitted + acknowledged.
- **W2.5** Arbor vs SIA-H benchmark published.
- **W26** privacyd v1 launched with ≥3 paying customers (Indie or Enterprise tier).
- **W22** open-source "Dan Glasses Kit" has public repo with at least 50 stars by Dec 2026.

If any box is unchecked, extend the 6-month horizon by 6 weeks and re-evaluate.

### 2.3 Risks (6-month, v14 deltas marked with **★**)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| OpenClaw skill malware in production | High | High | W0 ships this week; signed skills + default-deny |
| LFM2.5-VL-450M Q4_0 > 4.5 W on Pi 5 | Medium | High | Switch to IQ2_XXS early; evaluate Gemma 4 E4B as fallback |
| SIA-H shows no gain on our tasks | High | Low | Publish null result |
| LFM2.5-Embedding-350M quality regression | Low | Medium | Keep MiniLM as fallback; benchmark before swap |
| Redax hardware slipping | High | Medium | **Snapdragon Start as parallel path** ★ |
| OpenClaw upstream breaks MCP integration | Medium | Medium | Pin commit hash; plan Danlab fork |
| `.deb` packaging friction with Loki/udev/systemd | Medium | Low | Test Debian 12 first |
| **Snapdragon Start application rejected** ★ | Medium | Medium | Redax remains the path |
| **Lutnick-letter compliance regime arrives before W26 ships** ★ | Medium | Low | privacyd can launch with fable-5-safe only, add others in v1.1 |
| **Fable 5 returns with compliance regime, invalidates v13 "Fable 5 safe" moat** ★ | High | Low | Privacy story stands alone; "Fable 5 safe" is a feature |
| **Apple 2027 ships a wearable that out-specs us** ★ | Low | High | Our $400 BOM + on-device + open-source is the differentiation |

## 3. Twelve-Month Roadmap (Dec 2026 – Jun 2027) — "V1.5 Wearable"

**Gate to pass:** first wearable unit on a real human (probably Somdipto) for 8 hours/day for 30 consecutive days, with at least 3 user-rated wins per day and zero privacy incidents. **Apple-window is now 12-14 months, not 14-18.**

### 3.1 Workstreams (v14 deltas marked with **★**)

| # | Workstream | Lead | Duration | Deliverable | v14 delta |
|---|---|---|---|---|---|
| W12 | **Wake-on-event primitive** | Dan2 | 6 weeks | V4L2 + background-frame-diff event detection, sub-50 mW idle | unchanged |
| W13 | **SIA-W+H on SmolVLM-256M** | Dan2 | 8 weeks | LoRA fine-tune on SIA-H's self-critiqued trajectories | unchanged |
| W14 | **LFM2.5-Audio-1.5B collapse (if W1.5 succeeds)** | Dan2 | 8 weeks | Collapse audiod + ttsd into one on-device model | unchanged |
| W15 | **Memory consolidation v3 (RHO + Hindsight)** | Dan2 | 6 weeks | RHO-driven nightly consolidation on Mnemosyne | unchanged |
| W16 | **First external pilots (3-5 users)** | Somdipto | Rolling | Three to five users with laptop version, weekly feedback | unchanged |
| W17 | **Tauri v2 → v3** | Dan1 | 4 weeks | Better mobile plugin support, smaller bundle | unchanged |
| W18 | **Brilliant Labs Halo user study** | Dan2 | 2 weeks | Buy one, wear for a week, write `halo-user-study.md` | unchanged |
| W19★ | **Wearable v2 silicon (Snapdragon Start OR Redax)** | Hardware | 12 weeks | Identify and validate a Snapdragon Start SoC OR Redax board | **Snapdragon Start added** |
| W23 | **Internationalization** | Dan1 | 16 weeks | Whisper multilingual + KittenTTS multilingual voices | unchanged |
| W25 | **Privacy whitepaper (DPDP + EU AI Act + fable-5-safe)** | Somdipto | 8 weeks | Published white paper | unchanged |
| W27★ | **privacyd v2: enterprise tier scaling** | Dan1 + Dan2 | 8 weeks | SSO, custom profiles, audit log export, on-prem | **NEW v14** |

### 3.2 Hard go/no-go gate (Jun 2027)

**v13 gate items, unchanged:**
- At least one user wore the unit 8h/day for 30 days without a comfort complaint.
- At least 3 self-rated "the glasses helped" moments per day.
- Zero privacy incident.
- SIA-W+H shows ≥10% gain over heuristic baseline.
- Memory consolidation v2 runs nightly with auditable log.
- All five services pass canonical health contract tests in CI.

**v14 NEW gate items:**
- **W12** wake-on-event achieves sub-50 mW idle measured on the wearable target.
- **W19** wearable v2 silicon identified with Snapdragon Start OR Redax.
- **W25** privacy whitepaper published.
- **W27** privacyd v2 enterprise tier has ≥5 paying customers.

## 4. Twenty-Four-Month Roadmap (Jun 2027 – Jun 2028) — "Product"

**Gate to pass:** 100 paid users in Bangalore + 1 international city, with ≥30% MAU and 4.5+ rating.

| # | Workstream | v14 delta |
|---|---|---|
| W19 | **Always-on memory loop v2** | unchanged |
| W20 | **Proactive suggestion primitive** | unchanged |
| W21 | **LFM2.5-VL-3B (or whatever Liquid ships next)** | unchanged |
| W22 | **Open-source "Dan Glasses Kit"** | Day-1 promise, from W22 v13 in 6-month roadmap |
| W23 | **Internationalization** | unchanged |
| W24 | **Battery + thermal v2 (hybrid CPU+NPU)** | W19 from 12-month is the precursor |
| W25 | **Privacy story: local-first, open audit log** | unchanged |
| W28★ | **privacyd v3: AGI-deployer compliance platform** | **NEW v14** — multi-tenant, full audit export, self-serve customer onboarding |
| W29★ | **Wearable v2 hardware ship (Snapdragon Start or Redax)** | **NEW v14** — first 1000 units |

## 5. The 24-Month Single-Number Target (unchanged from v13)

> By June 2028, we will have a wearable that draws ≤ 4 W average, runs an always-on perception loop with a sub-500 MB VLM, and remembers enough about a user to surface a non-trivial, audit-trail-justified suggestion at least once per hour of use. **And** we will have a commercial compliance attestation product (privacyd) with at least 50 enterprise customers and $1M+ ARR.

## 6. Top 5 Recommendations (Telegram summary)

1. **Apply to Qualcomm Snapdragon Start program this week.** Turnkey silicon + Inspecs channel + hybrid AI support. The wearable v2 silicon path is now parallel, not serial.
2. **Ship OpenClaw signed-skill infrastructure (cosign + Rekor + default-deny) this week.** P0. Blocks v1.0 .deb.
3. **Install Mnemosyne as OpenClaw memory backend. Day 1.** W9 unblock.
4. **Productize `privacyd` as compliance attestation framework (W26).** OSS / $99 / $999 tiers. fable-5-safe + mythos-5-safe + EU AI Act + DPDP profiles. 4 weeks.
5. **Promote open-source "Dan Glasses Kit" to Day-1 promise.** Brilliant Labs Halo is the proof. Apple 2027 = biggest product year in history, ship v1.0 by Q4 2026.

## 7. What this Roadmap Deliberately Does Not Include (unchanged from v13)

- Frontier-scale model training.
- General-purpose agent framework to compete with OpenClaw, Letta, LangChain.
- Cellular, GNSS, display-overlay hardware.
- Multi-user / household support.
- AR/VR.
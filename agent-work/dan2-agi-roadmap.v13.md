# Danlab AGI Roadmap v13 — 6 / 12 / 24 Months
**Author:** Dan2 (lead scientist / architect)
**Date:** 2026-06-19 09:30 IST
**Supersedes:** dan2-agi-roadmap.v12 (24 hours old)

---

## 0. Headline (v13 deltas from v12)

**Mission (unchanged).** The most credible *edge* path to AGI: a sub-500 MB multimodal model, on a sub-$100 aarch64 board, on a 2500 mAh battery, for 4 hours, with an always-on memory loop and an audit-trail self-improvement harness.

**v13 changes to the plan:**

1. **W9 (memory) is now 6 weeks instead of 12.** Mnemosyne + LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M + UaC replaces the v12 "build it from scratch" plan.
2. **W2 (SIA) is now 6 weeks instead of 8.** GLM-5.2 (open, MIT, 1M context) replaces the v12 "Claude-class or GPT-class" Feedback-Agent. Cheaper, faster, open.
3. **W22 (open-source Kit) promoted from Q4 2027 to Day-1 promise.** Brilliant Labs Halo is the proof. Say it now, ship it soon.
4. **P0 added: OpenClaw signed-skill infrastructure** (cosign + Rekor + default-deny). Blocks v1.0 .deb.
5. **Wearable v2 form factor gets a hybrid CPU+NPU plan** based on Box v3.1.0 NPU datapoint.

**Mission posture (unchanged from v12).** Lane 3 of 4 (edge / on-device / lane 4 in v13 with open-weights as a new lane 2). The Apple Meta window holds at 12-18 months. The open-weights frontier (GLM-5.2) is a v12 correction, not a lane change.

## 1. Time Horizons (unchanged from v12)

| Horizon | Window | Anchor | Single sentence |
|---|---|---|---|
| **6 months** | Jun – Dec 2026 | Foundation | Characterized, reproducible edge-AI reference stack on a known dev board, with auditable self-improvement. |
| **12 months** | Dec 2026 – Jun 2027 | V1.5 wearable | First real wearable unit, always-on perception, auditable self-improvement. |
| **24 months** | Jun 2027 – Jun 2028 | Product | A product a paying user wears all day and trusts. |

Each horizon has a hard **go/no-go gate**. If the gate fails, the next horizon is replanned, not skipped.

## 2. Six-Month Roadmap (Jun – Dec 2026) — "Foundation"

**Gate to pass:** working OpenClaw + perceptiond + memoryd loop on a Pi 5 with measured W/frame, p95 latency, and thermal curve. **Plus:** v1.0 .deb ships with signed skills and an auditable self-improvement benchmark.

### 2.1 Workstreams (v13 deltas marked with **★**)

| # | Workstream | Lead | Duration | Deliverable | v13 delta |
|---|---|---|---|---|---|
| W0★ | **OpenClaw signed-skill infra** | Dan1 + Dan2 | 1 week | cosign + Rekor for all Danlab skills; default-deny policy | **NEW P0** |
| W1 | **Pi 5 / Orange Pi 5 power & perf** | Dan2 | 4 weeks | `power-characterization.md` with measured W/frame, p95 latency, thermal | unchanged |
| W1.5★ | **LFM2.5-Audio-1.5B benchmark** | Dan2 | 2 weeks | Audiod + ttsd collapse evaluation | **NEW spike** |
| W2 | **SIA fork in danlab-multimodal** | Dan2 | 6 weeks | First SIA-H run with GLM-5.2 Feedback-Agent | **Was 6 wk, GLM-5.2 swap** |
| W3 | **`evented` aggregator** | Dan2 | 3 weeks | Single pubsub stream, replayable | unchanged |
| W4 | **`stated` snapshot service** | Dan2 | 2 weeks | Union-of-health `state.json` writer, 2 s cadence | unchanged |
| W5 | **`clawd-watchdog`** | Dan2 | 1 week | systemd unit, 30 lines | unchanged |
| W6 | **OpenClaw MCP tool coverage** | Dan1 | 4 weeks | `perception_search`, `memory_query`, `os_exec`, `tts_speak` MCP tools | unchanged |
| W7 | **Bootstrap wizard v1** | Dan1 | 3 weeks | Camera permission, model download, language, Telegram, OpenClaw auth | unchanged |
| W8 | **`.deb` packaging for laptop** | Dan2 | 3 weeks | All five services + gateway + Tauri, signed (GPG + cosign) | **cosign added** |
| W9 | **Memoryd v1.5 (Mnemosyne + LFM2.5-Embedding-350M + UaC)** | Dan2 | 6 weeks | Mnemosyne swap, embedding swap, Eywa provenance, UaC schema, RHO consolidation | **Was 12 wk** |
| W10 | **LFM2.5-VL-1.6B-Extract spike** | Dan3 | 1 week | Does structured-JSON output satisfy `toold` invocation path? | unchanged |
| W11★ | **DPDP Act + EU AI Act compliance review** | Somdipto | 4 weeks | Formal compliance review of v1.0 .deb | **NEW** |
| W22★ | **Open-source "Dan Glasses Kit" — Day-1 promise** | Dan1 | 12 weeks | Public repo, .deb + Pi 5 reference + OpenClaw config + Tauri app, Apache 2.0 | **Promoted from Q4 2027** |

### 2.2 Hard go/no-go gate (Dec 2026)

**v12 gate items, unchanged:**
- W1 report shows Q4_0 VLM ≤ 4.5 W on Pi 5.
- W1 report shows IQ2_XXS VLM ≤ 2.5 W with <8% quality regression.
- W2 published a SIA-H run with reproducible gain or null-result note.
- W3 + W4 + W5 live in dev with green end-to-end demo.
- W8 .deb installs cleanly on Ubuntu 24.04 and survives upgrade.
- W9 schema migration reversible.

**v13 NEW gate items:**
- **W0** cosign-signed skills + Rekor public log entry for every Danlab-shipped skill.
- **W2** uses GLM-5.2 (open, MIT) as Feedback-Agent, not a cloud API.
- **W9** uses Mnemosyne as the runner (not custom), LFM2.5-Embedding-350M as the embedding (if quality check passes), and LFM2.5-ColBERT-350M as the late-interaction reranker.
- **W11** DPDP Act + EU AI Act compliance sign-off on the v1.0 .deb.
- **W22** open-source "Dan Glasses Kit" has public repo with at least 50 stars by Dec 2026.

If any box is unchecked, extend the 6-month horizon by 6 weeks and re-evaluate.

### 2.3 Risks (6-month, v13 deltas marked with **★**)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| OpenClaw skill malware in production | High ★ | High | W0 ships this week; signed skills + default-deny |
| LFM2.5-VL-450M Q4_0 > 4.5 W on Pi 5 | Medium | High | Switch to IQ2_XXS early; evaluate Gemma 4 E4B as fallback |
| SIA-H shows no gain on our tasks | High | Low | Publish null result |
| LFM2.5-Embedding-350M quality regression | Low ★ | Medium | Keep MiniLM as fallback; benchmark before swap |
| Redax hardware slipping | High | Medium | Pi 5 is the dev board for now |
| OpenClaw upstream breaks MCP integration | Medium | Medium | Pin commit hash; plan Danlab fork |
| `.deb` packaging friction with Loki/udev/systemd | Medium | Low | Test Debian 12 first |
| **OpenClaw memory plugin defaults to wrong provider** ★ | High | Low | Set `plugins.slots.memory = "memory-core"` explicitly (W0 fix) |
| **Fable 5 returns with compliance regime, invalidates the v12 "Fable 5 safe" moat** ★ | High | Low | Privacy story stands on its own; "Fable 5 safe" is a feature, not a moat |

## 3. Twelve-Month Roadmap (Dec 2026 – Jun 2027) — "V1.5 Wearable"

**Gate to pass:** first wearable unit on a real human (probably Somdipto) for 8 hours/day for 30 consecutive days, with at least 3 user-rated wins per day and zero privacy incidents.

### 3.1 Workstreams (v13 deltas marked with **★**)

| # | Workstream | Lead | Duration | Deliverable | v13 delta |
|---|---|---|---|---|---|
| W12 | **Wake-on-event primitive** | Dan2 | 6 weeks | V4L2 + background-frame-diff event detection, sub-50 mW idle | **Target lowered to 50 mW** |
| W13 | **SIA-W+H on SmolVLM-256M** | Dan2 | 8 weeks | LoRA fine-tune on SIA-H's self-critiqued trajectories | unchanged |
| W14 | **LFM2.5-Audio-1.5B collapse (if W1.5 succeeds)** | Dan2 | 8 weeks | Collapse audiod + ttsd into one on-device model | **NEW conditional** |
| W15 | **Memory consolidation v3 (RHO + Hindsight)** | Dan2 | 6 weeks | RHO-driven nightly consolidation on Mnemosyne | **Was 8 wk** |
| W16 | **First external pilots (3-5 users)** | Somdipto | Rolling | Three to five users with laptop version, weekly feedback | unchanged |
| W17 | **Tauri v2 → v3** | Dan1 | 4 weeks | Better mobile plugin support, smaller bundle | unchanged |
| W18 | **Brilliant Labs Halo user study** | Dan2 | 2 weeks | Buy one, wear for a week, write `halo-user-study.md` | unchanged |
| W19★ | **Wearable v2 silicon (hybrid CPU+NPU)** | Hardware | 12 weeks | Identify and validate a 12-TOPS-class NPU wearable SoC | **NEW** |
| W23★ | **Internationalization: Hindi, Tamil, Telugu, Spanish, Mandarin** | Dan1 | 16 weeks | Whisper multilingual + KittenTTS multilingual voices | unchanged from v12 |
| W25★ | **Privacy whitepaper (DPDP + EU AI Act + Fable-5-safe)** | Somdipto | 8 weeks | Published white paper | **NEW — moved from W25 in v12** |

### 3.2 Hard go/no-go gate (Jun 2027)

**v12 gate items, unchanged:**
- At least one user wore the unit 8h/day for 30 days without a comfort complaint.
- At least 3 self-rated "the glasses helped" moments per day.
- Zero privacy incident.
- SIA-W+H shows ≥10% gain over heuristic baseline.
- Memory consolidation v2 runs nightly with auditable log.
- All five services pass canonical health contract tests in CI.

**v13 NEW gate items:**
- **W12** wake-on-event achieves sub-50 mW idle measured on the wearable target.
- **W14** (if W1.5 succeeded) audiod + ttsd collapse ships on the wearable.
- **W18** Halo user study published.
- **W19** wearable v2 silicon identified with NPU benchmarks.
- **W25** privacy whitepaper published.

## 4. Twenty-Four-Month Roadmap (Jun 2027 – Jun 2028) — "Product"

**Gate to pass:** 100 paid users in Bangalore + 1 international city, with ≥30% MAU and 4.5+ rating.

### 4.1 Workstreams

Unchanged from v12, with two v13 updates:

| # | Workstream | v13 delta |
|---|---|---|
| W19 | **Always-on memory loop v2** | unchanged |
| W20 | **Proactive suggestion primitive** | unchanged |
| W21 | **LFM2.5-VL-3B (or whatever Liquid ships next)** | **NEW: track LFM2.5-Thinking as the on-device reasoning** |
| W22 | **Open-source "Dan Glasses Kit"** | **Day-1 promise, this is W22 v13 from the 6-month roadmap** |
| W23 | **Internationalization** | unchanged |
| W24 | **Battery + thermal v2 (hybrid CPU+NPU)** | **W19 from 12-month is the precursor** |
| W25 | **Privacy story: local-first, open audit log** | unchanged |

## 5. The 24-Month Single-Number Target (unchanged from v12)

> By June 2028, we will have a wearable that draws ≤ 4 W average, runs an always-on perception loop with a sub-500 MB VLM, and remembers enough about a user to surface a non-trivial, audit-trail-justified suggestion at least once per hour of use.

## 6. Top 3 Recommendations (Telegram summary)

1. **Ship OpenClaw signed-skill infrastructure (cosign + Rekor + default-deny) this week. P0.** Three small changes, blocks v1.0 .deb. The in-the-wild attack is documented; the v12 "P1" is now "P0."
2. **Install Mnemosyne as the OpenClaw memory backend. Day 1.** Replaces the v12 "build consolidation from scratch" plan with a 98.9% LongMemEval battle-tested system. W9 is now 6 weeks instead of 12.
3. **Promote the open-source "Dan Glasses Kit" from a Q4 2027 deliverable to a Day-1 promise.** Brilliant Labs Halo is the proof. The 2x2 cell is now "HUD vs no-HUD × on-device vs cloud" — we are in the bottom-left with Halo and Even Realities G2. The differentiation is open-source + auditable + Indian-made. Say it now, ship it soon.

## 7. What this Roadmap Deliberately Does Not Include (unchanged from v12)

- Frontier-scale model training.
- General-purpose agent framework to compete with OpenClaw, Letta, LangChain.
- Cellular, GNSS, display-overlay hardware.
- Multi-user / household support.
- AR/VR.

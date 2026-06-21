# Dan2 — Danlab AGI Roadmap v7
## 6 / 12 / 24-month Plan (2026-06-17)

**Date:** 2026-06-17
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v7. v6 archived as `dan2-agi-roadmap.v6.md`. v7 incorporates: the v6 plan executed, the new reasoning layer (reasond/proactived) as the dominant 6-month initiative, the SIA fork as the 12-month initiative, and the form-factor-blocking decision highlighted as the critical-path item.

**Read `dan2-research-report.md`, `dan2-architecture-review.md`, `dan2-model-analysis.md` first.**

---

## 0. North Star

**Danlab's AGI thesis:** AGI will not be a single frontier model. It will be a *layered* system of small, specialized, on-device, privacy-preserving, recursively improving models. Our wedge is the **on-device, open-source, proactive AI companion** niche. The frontier labs (OpenAI, DeepMind, Anthropic) own the scaling narrative; we own the deployment narrative.

**Where we ship in 24 months:** an open-source stack — Dan Glasses v1 hardware + the `danlab-agi` open-source runtime (the 6 services + reasond + proactived) — that a third-party developer in India, Brazil, or Africa can fork, fine-tune, and deploy on their own wearable or phone. **India-first, open-source-first, privacy-first.**

---

## 1. The Critical Path (decision-blocked items)

**These must be resolved in the first 14 days. They block everything.**

| # | Decision | Owner | Options | Default if not decided |
|---|---|---|---|---|
| 1 | **Power source for v1 glasses** | somdipto + hardware | (a) tethered battery pack (Meta Ray-Ban style), (b) 2× 600mAh in-frame, (c) 2× 200mAh + aggressive power gating | (a) tethered — fastest to ship, lowest risk |
| 2 | **Weight target for v1** | somdipto + hardware | (a) <50g (premium), (b) <80g (commodity), (c) <120g (early adopter) | (b) 80g — balances form factor and battery |
| 3 | **Cloud LLM budget for SIA fork** | somdipto | (a) Claude Sonnet 4.6 ($3/$15 per M tokens), (b) HRM-Text 1B + Gemma 4 1B local | (b) local — cheaper, more private |
| 4 | **v1 pricing target** | somdipto | (a) $300 (commodity), (b) $400 (mid), (c) $500 (premium) | (b) $400 — Meta Ray-Ban Display is $799; we undercut |
| 5 | **Apple glasses delay strategy** | somdipto | (a) target 2026-Q4 launch (ship in Apple's gap), (b) target 2027-Q3 (Apple launches Q4 2027) | (a) Q4 2026 — beat Apple to "open-source AI glasses" |

**Without #1 and #2, thermal and PCB design cannot start.** This is the v7 critical-path call.

---

## 2. The 6-Month Plan (2026-06-17 → 2026-12-17)

**Theme: close the reasoning gap, ship the v1 prototype.**

### Month 1-2: Foundation hardening

- [ ] **Resolve critical path** (#1-#5 above)
- [ ] Add `shared/` Rust crate with serde structs (1 day, DAN-1)
- [ ] Add `policy.deny_skills` and redaction hooks to OpenClaw (1 week, DAN-1)
- [ ] Add `model-layers` section to `dan-glasses/AGENTS.md` and `PRD.md` (1 day)
- [ ] Write `reasond` service skeleton (no model yet) — port :8745 (1 week, DAN-2)
- [ ] Write `proactived` service skeleton — port :8746 (1 week, DAN-2)
- [ ] Write `context_gate.py` for perceptiond (1-2 weeks, DAN-3)
- [ ] Read arXiv 2605.25435 (OpenClaw security), implement audit hooks (1 week, DAN-1)
- [ ] Pin HRM-Text 1B in `models/download.sh` (1 day)

### Month 3-4: Reasoning layer

- [ ] Fine-tune HRM-Text 1B on 200-500 "observation → suggestion" examples (DAN-2, with H100 access)
- [ ] Quantize HRM-Text 1B to Q4 for aarch64
- [ ] Integrate HRM-Text 1B into `reasond` (DAN-2)
- [ ] Wire audiod + perceptiond + memoryd → reasond event streams
- [ ] Tauri UI: subscribe to `proactive_suggestion` events
- [ ] First end-to-end "AI that says something useful proactively" demo

### Month 5-6: Proactive UX + v1 prototype

- [ ] Implement `proactived` rules engine (idle>30s, salience>0.7, no-repeat-24h)
- [ ] Fine-tune the calibration (user feedback loop)
- [ ] Write `powerd` state machine (mock implementation; real when Redax lands)
- [ ] Write `.deb` packaging for the full 8-service stack
- [ ] `systemd` units for all 8 services
- [ ] Bootstrap wizard v3: includes reasond/proactived configuration
- [ ] Internal demo day: 5 users wear a tethered prototype for 1 week
- [ ] Collect feedback, ship v1.0 candidate

**6-month exit criteria:**
- All 8 services production-grade with ≥100 tests each
- `reasond` and `proactived` ship with hand-coded rules + HRM-Text 1B optional
- End-to-end "AI companion that proactively speaks" demo
- `.deb` package builds and installs on Debian 12
- Internal dogfooding data: 5 users × 1 week

---

## 3. The 12-Month Plan (2026-06-17 → 2027-06-17)

**Theme: become honest about RL, ship the v1 wearable.**

### Month 7-9: Wearable hardware (Redax track)

- [ ] Finalize Redax board (or pivot to alternative if Redax slips)
- [ ] Power characterization on aarch64 (THE measurement)
- [ ] Battery sizing decision based on measurement
- [ ] Thermal design (passive cooling; max skin-contact temp target)
- [ ] Camera module selection (V4L2 compatibility)
- [ ] Weight validation (target <80g)

### Month 10-12: SIA fork + v1 ship

- [ ] Fork SIA, build harness-only RL loop on top of danlab-multimodal (DAN-2)
- [ ] Use HRM-Text 1B as the local Feedback-Agent
- [ ] Run the loop on "describe this image better" — measure delta vs. heuristic baseline
- [ ] Publish the SIA fork as open-source (Apache 2.0)
- [ ] Ship Dan Glasses v1.0 (or v0.9 if Redax is late) to first 100 users
- [ ] Public launch: "India's first open-source AI glasses" — target Apple-glasses-gap window (Q4 2026 if Apple slips to Q4 2027)
- [ ] Publish a paper / blog post: "Building a self-improving AI companion on a 2GB on-device stack"

**12-month exit criteria:**
- Dan Glasses v1.0 ships (or v0.9 if hardware slips)
- danlab-multimodal is honest about being harness-only RL (not heuristic)
- ≥100 users in production
- ≥1 paper or significant blog post on the danlab-multimodal RL approach
- Revenue target: 100 units × $400 = $40K (modest, validates the product)

---

## 4. The 24-Month Plan (2026-06-17 → 2028-06-17)

**Theme: scale the runtime, ship weight updates, go open-source-first.**

### Year 2: Open-source the runtime

- [ ] Open-source `danlab-agi-runtime`: all 8 services + reasond + proactived + powerd as a single `pip install` / `apt install` package
- [ ] Support: Debian 12, Ubuntu 24.04, Fedora 41, Arch
- [ ] Documentation: "Run your own on-device AI companion"
- [ ] Community: GitHub Discussions, Discord, monthly office hours
- [ ] First third-party fork: an Indian university deploys on a phone (not glasses) for accessibility

### Year 2: Full self-improvement (SIA-W+H)

- [ ] Move from harness-only to harness + weights (SIA-W+H)
- [ ] Requires: H100 budget for weight updates; privacy story for shipping fine-tuned weights
- [ ] First fine-tuned HRM-Text 1B variant: "danlab-agi-hrm-v1" published
- [ ] First fine-tuned LFM2.5-VL-450M variant: "danlab-vision-v1" published
- [ ] Production telemetry: what does the agent do over 30 days for 100 users?

### Year 2: AGI thesis validation

- [ ] Can the agent learn user patterns without explicit feedback? (proactive suggestions accuracy >70%)
- [ ] Can the agent personalize via memory? (memory recall precision@5 >80%)
- [ ] Can the agent self-improve? (RL loop delta vs. baseline >20% on held-out tasks)
- [ ] Can the agent run on a 2GB on-device stack? (binary size + RAM peak)
- [ ] **If yes to all 4:** we have a credible "on-device AGI" story. Write the AGI paper.
- [ ] **If no:** we know what doesn't work. Pivot.

**24-month exit criteria:**
- `danlab-agi-runtime` v1.0 open-sourced, 1K+ GitHub stars
- First AGI paper submitted to a workshop (NeurIPS, ICML, or ACL)
- 1K+ Dan Glasses units sold (or in pre-order)
- $400K+ revenue
- 5+ third-party deployments (universities, accessibility, enterprise pilots)

---

## 5. The "What Could Kill This" List (v7 update)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Redax hardware slipping** | high | critical | Fall back to tethered prototype + alternative board (Jetson Orin Nano?) |
| **LFM2.5-VL-450M power too high on aarch64** | medium | critical | Benchmark SmolVLM-256M and lower-frequency operation; thermal throttle |
| **HRM-Text 1B inference code not published** | medium | high | Fork Sapient, write our own; fallback to Gemma 4 1B (lower quality reasoning) |
| **SIA fork doesn't beat heuristic baseline** | medium | high | Publish the negative result honestly; the negative is still novel |
| **OpenClaw security incident** | low | high | Read arXiv 2605.25435, implement mitigations, pin versions |
| **Anthropic "brake pedal" becomes regulatory** | low | medium | Watch; not actionable for us; we don't train frontier models |
| **Apple ships smart glasses in Q4 2026 (no delay)** | low | medium | Pivot to "developer kit" framing; price $200 for hackers |
| **Open-source community doesn't materialize** | medium | medium | Recruit from Indian universities (IIT, IISc); write Hindi tutorials |
| **Form factor decisions take 6+ months** | medium | high | Push for default (tethered, 80g) and move on |

---

## 6. Resource Plan (rough)

| Resource | 6-month | 12-month | 24-month |
|---|---|---|---|
| People (FTE equivalent) | 2-3 (Dan1, Dan2, Dan3) | 3-4 (add Dan4 full-time + 1 community mgr) | 5-7 (add hardware eng, designer) |
| Compute (cloud, dev) | $500/mo | $2K/mo (H100 for SIA fork) | $5K/mo (full RL training) |
| Hardware (Redax, dev boards) | $5K (1× dev kit) | $20K (5× dev kits + first 100 units) | $100K (first 1K units) |
| Revenue (cumulative) | $0 | $40K (100 units) | $400K (1K units) |
| Cash burn (cumulative) | $30K | $200K | $800K |
| Funding gap | -$30K | -$160K | -$400K |

**v7 funding reality:** to hit the 24-month plan, we need $400-800K of funding by month 12. Options: (a) bootstrap from sales (slow), (b) YC / Indian accelerator (most likely), (c) angel round (somdipto's network), (d) grant (IndiaAI Mission, ARPA-H, NSF).

**The accelerator route is the most credible.** Apply to YC S26 (Aug 2026 deadline), Surge (India), or Antler. The "open-source AGI from India" pitch is unusual enough to stand out.

---

## 7. v7 Differentiators vs. v6 Plan

v6 said:
- Build a desktop prototype
- Migrate to wearable when hardware lands
- Add AGI features on top

**v7 says:**
- The desktop prototype is done. All 6 services + Tauri app + OpenClaw are live.
- v7 critical-path is **hardware form-factor decisions**, not code.
- v7 biggest product gap is **the reasoning layer** (reasond + proactived). Without it, Dan Glasses is a recorder.
- v7 biggest strategic bet is **HRM-Text 1B as the on-device reasoning model** (added in v7, not in v6).
- v7 timeline to "honest RL" is **SIA fork in 12 months**, not a 2-year research project.
- v7 go-to-market is **open-source-first + India-first + Apple-gap-window**, not a closed US launch.

---

## 8. What "AGI" Means for Danlab (v7 reframe)

**We are not building AGI in the frontier-model sense.** Frontier AGI is OpenAI, DeepMind, Anthropic's job. We don't have the compute, the data, or the mandate.

**We are building the deployment layer for AGI.** The thesis:

1. Frontier models will keep getting better, but they will never run on a wearable. (Latency, cost, privacy, connectivity.)
2. The AGI on a wearable will be a *composition* of small models: vision (LFM2.5-VL-450M), STT (whisper), TTS (KittenTTS), reasoning (HRM-Text 1B), memory (all-MiniLM-L6-v2 + SQLite).
3. The differentiator is not any single model. It is the **system** that runs them, the **memory** that connects them, the **proactive layer** that decides when to speak, and the **self-improvement loop** that makes it better over time.
4. The moat is the **user data** (private, on-device, never leaves the device) + the **open-source community** that forks and extends the stack.

**This is a 10-year thesis, not a 10-month thesis.** v7 lays the foundation. v8 will reframe again. The plan is to keep the plan alive, not to defend it.

---

## 9. What somdipto Needs to Decide in the Next 7 Days

1. **Power source for v1** — tethered, in-frame big battery, or aggressive power gating? (See §1.)
2. **Weight target for v1** — 50g, 80g, or 120g?
3. **Cloud LLM budget for SIA fork** — pay Claude Sonnet 4.6, or run HRM-Text 1B + Gemma 4 1B local?
4. **v1 pricing target** — $300, $400, or $500?
5. **Apple glasses delay strategy** — beat Apple in 2026-Q4, or wait for 2027-Q3?
6. **Funding route** — bootstrap, accelerator, or angel?
7. **Open-source license for the runtime** — Apache 2.0, MIT, or BSL?

**Decisions #1-#5 are the critical path.** Until they are made, the wearable hardware cannot start. The 6-month code work can proceed in parallel.

---

## 10. The One-Sentence Pitch (v7)

> **Danlab is building the open-source, on-device, self-improving AI companion stack — starting with Dan Glasses, the first open-source AI glasses designed in India for the world.**

---

*End of v7 AGI roadmap. Companion artifacts: `dan2-research-report.md`, `dan2-architecture-review.md`, `dan2-model-analysis.md`, `dan2-papers-to-read.md`.*

# Dan2 — Danlab AGI Roadmap v8
## 6 / 12 / 24-Month Plan (v8 — Decisive, Hardware-Blocked)

**Date:** 2026-06-17 11:30 IST
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v8. v7 archived as `dan2-agi-roadmap.v7.md`. v7 ran 4h ago at 05:15 UTC.
**Companion:** Read `dan2-research-report.md`, `dan2-architecture-review.md`, `dan2-model-analysis.md` first.

---

## 0. v8 Read in 90 Seconds

**The world moved in 4 hours.** v7 was right; v8 makes it load-bearing.

- **Anthropic's "brake pedal" memo (June 4-11 2026):** makes "honest self-improvement" the only defensible posture. We were already there.
- **HRM-Text 1B is now in HuggingFace transformers and vLLM.** Concrete, not vapor. The `reasond` service is real.
- **OpenClaw security is P0.** 48 CVEs, Claw Chain exploited in the wild, ClawHavoc 824 malicious skills. v8 makes the mitigations explicit.
- **Meta Muse Spark is real.** API still delayed. Apple delayed to late 2027. The Apple-gap window is real, ~12-18 months from now.

**v8 single sentence:** *ship a v1 desktop+tethered prototype in Q4 2026, build the on-device reasoning layer (`reasond`) in parallel, fork SIA in month 6, and let the wearable hardware catch up.*

**v8 critical path:**
1. **OpenClaw security hardening (P0, week 1-2).** Pin to 2026.5.x. Disable ClawHub. Add policy.deny_skills.
2. **Privacy threat model (P0, week 2-3).** Document what data never leaves the device. `docs/privacy-threat-model.md`.
3. **`reasond` service skeleton (P0, week 3-4).** Port :8745. HRM-Text 1B integration deferred to month 2-3 (Sapient has not yet released inference code for on-device).
4. **`proactived` service skeleton (P0, week 3-4).** Port :8746. Hand-coded rules first; ML later.
5. **`memoryd` v2 with typed schema (P1, month 2).** 13 categories. Vector + typed filter + graph fallback. LLM-guided compression.
6. **Form-factor decision (P0, BLOCKING).** somdipto must decide: tethered, 80g with 2×600mAh, or 50g with aggressive gating. **This blocks all wearable hardware work.**
7. **SIA fork (P1, month 6-9).** Harness-only loop on top of danlab-multimodal. Use HRM-Text 1B as the local Feedback-Agent.
8. **v1 desktop prototype dogfooding (P0, month 3-4).** 5 users × 1 week. Validate the proactive layer is useful.

**v8 6-month exit criteria:** all 9 services (8 existing + reasond + proactived) production-grade; SIA fork with measurable improvement over heuristic; 5-user dogfood; Privacy Threat Model published.

**v8 12-month exit criteria:** Dan Glasses v1.0 (or v0.9 if hardware slips) ships; ≥100 users in production; open-source AGI runtime v1.0 with 1K+ stars; one paper / significant blog post.

**v8 24-month exit criteria:** `danlab-agi-runtime` open-sourced; harness+weights RL on by default; 1K+ Dan Glasses units sold; 5+ third-party deployments; first AGI paper.

---

## 1. The Critical Path (decision-blocked items, v8 updated)

**These must be resolved in the next 14 days. They block everything.**

| # | Decision | Owner | Options | v8 default if not decided |
|---|---|---|---|---|
| 1 | **Power source for v1 glasses** | somdipto + hardware | (a) tethered battery pack, (b) 2× 600mAh in-frame, (c) 2× 200mAh + aggressive power gating | (a) tethered — fastest to ship |
| 2 | **Weight target for v1** | somdipto + hardware | (a) <50g premium, (b) <80g commodity, (c) <120g early adopter | (b) 80g — best balance |
| 3 | **Cloud LLM budget for SIA fork** | somdipto | (a) Claude Sonnet 4.6, (b) HRM-Text 1B + Gemma 4 1B local | (b) local — cheaper, more private |
| 4 | **v1 pricing target** | somdipto | (a) $300 commodity, (b) $400 mid, (c) $500 premium | (b) $400 — undercut Meta Ray-Ban Display $799 |
| 5 | **Apple glasses delay strategy** | somdipto | (a) Q4 2026 launch, (b) 2027-Q3 | (a) Q4 2026 — beat Apple to "open-source AI glasses" |
| 6 | **Open-source license for runtime** | somdipto | (a) Apache 2.0, (b) MIT, (c) BSL | (a) Apache 2.0 — patent peace, broad adoption |
| 7 | **KittenTTS license check** | DAN-1 | clarify from KittenML | if unclear → switch to Piper or Kokoro in v1.5 |
| 8 | **OpenClaw security posture** | somdipto | (a) keep current, (b) fork to internal-only, (c) replace | (b) fork to internal-only — P0 per v8 |

**Without #1 and #2, thermal and PCB design cannot start.** v7 said this; v8 makes it load-bearing with a 14-day deadline.

**Without #8, the security risk is unacceptable.** v7 said P1; v8 makes it P0 with a 1-week deadline.

---

## 2. The 6-Month Plan (2026-06-17 → 2026-12-17)

**Theme: ship the proactive AI companion on desktop, harden security, build the on-device reasoning layer.**

### Month 1 (June): Foundation + Security

**P0 actions:**
- [ ] Resolve critical path #1, #2, #8 (sompdipto decisions, 14-day deadline)
- [ ] OpenClaw security hardening: pin to 2026.5.x, disable ClawHub, add policy.deny_skills, add audit log redaction
- [ ] Privacy threat model: `docs/privacy-threat-model.md` (DAN-2 + somdipto, 1 week)
- [ ] Document the two-brain contradiction fix in `dan-glasses/AGENTS.md` (DAN-1)
- [ ] Add `model-layers` section to `PRD.md` (DAN-1)
- [ ] `reasond` service skeleton: `Services/reasond/reasond.py` with HTTP API, no model yet (DAN-2, 1 week)
- [ ] `proactived` service skeleton: `Services/proactived/proactived.py` with hand-coded rules (DAN-2, 1 week)
- [ ] Pin HRM-Text 1B in `models/download.sh` (DAN-1, 1 day)

**P1 actions:**
- [ ] Pin Gemma 4 1B Q4 in `models/download.sh`
- [ ] Write `context_gate.py` for perceptiond (DAN-3, 2 weeks)
- [ ] `memoryd` v2 design doc with typed schema proposal (DAN-4)
- [ ] KittenTTS license check (DAN-1, 2 days)

### Month 2 (July): Reasoning + Proactive Layer

**P0 actions:**
- [ ] Integrate HRM-Text 1B into `reasond` via HuggingFace transformers (DAN-2, 2 weeks)
  - Benchmark: 100 sample queries, measure latency on aarch64 (x86_64 acceptable for v1)
  - Quantize to Q4 (~600MB)
  - Test: end-to-end "observation → suggestion" with mock events
- [ ] `proactived` rules engine v1: idle>30s, salience>0.7, no-repeat-24h (DAN-2)
- [ ] Wire audiod + perceptiond + memoryd → reasond event streams (DAN-2 + DAN-3)
- [ ] Tauri UI: subscribe to `proactive_suggestion` events (DAN-1)

**P1 actions:**
- [ ] `memoryd` v2 implementation: 13 typed categories (DAN-4, 2 weeks)
- [ ] `memoryd` v2 graph fallback layer with NetworkX (DAN-4)
- [ ] audiod: whisper binary hot-reload on `POST /reload` (carry-over from v0.3)
- [ ] perceptiond: context_gate.py to reduce VLM inference frequency (DAN-3)
- [ ] `powerd` state machine: mock implementation; real when Redax lands (DAN-1)

### Month 3 (August): First End-to-End + Dogfooding

**P0 actions:**
- [ ] End-to-end demo: audiod transcript + perceptiond description + reasond suggestion + ttsd speak (DAN-2)
- [ ] First "AI that says something useful proactively" demo, recorded (DAN-2)
- [ ] Internal dogfooding: 5 users × 1 week on the desktop prototype (sompdipto + 4 friends)
- [ ] Collect feedback: rate suggestions 1-5, log "would have wanted" cases
- [ ] Iterate on `proactived` rules based on feedback (DAN-2)

**P1 actions:**
- [ ] `memoryd` v2 deployment + migration of existing data (DAN-4)
- [ ] `memoryd` LLM-guided compression (MemRefine-style) (DAN-4)
- [ ] perceptiond: salience threshold tuning based on dogfooding (DAN-3)
- [ ] Form-factor decision implemented in `powerd` (DAN-1, after somdipto decides)

### Month 4 (September): SIA Fork Kickoff

**P0 actions:**
- [ ] Fork SIA (Hexo Labs, MIT, May 2026) (DAN-2, 1 day)
- [ ] Build harness-only RL loop on top of danlab-multimodal (DAN-2, 2 weeks)
- [ ] Use HRM-Text 1B as the local Feedback-Agent (DAN-2)
- [ ] Define reward function: "image description quality" measured against held-out test set (DAN-2)
- [ ] Run the loop on "describe this image better" — measure delta vs. heuristic baseline (DAN-2, 2 weeks)

**P1 actions:**
- [ ] Moonshine vs whisper.cpp head-to-head benchmark (DAN-2)
- [ ] KittenTTS license decision (DAN-1)
- [ ] perceptiond: power characterization (if Redax hardware has arrived)

### Month 5 (October): SIA Fork + Bootstrap Wizard v3

**P0 actions:**
- [ ] SIA fork: complete the harness-only loop, publish v0.1 (DAN-2)
- [ ] Write SIA fork blog post: "Honest harness-only RL on a 1B on-device stack" (DAN-2)
- [ ] Bootstrap wizard v3: includes reasond/proactived configuration (DAN-1 + DAN-4)
- [ ] `powerd` state machine operational with real hardware (DAN-1, if Redax lands)

**P1 actions:**
- [ ] Piper / Kokoro TTS head-to-head (DAN-4)
- [ ] perceptiond: VLM power characterization on aarch64 (DAN-3, if Redax lands)
- [ ] audiod: per-segment language detection (DAN-2)
- [ ] memoryd: visual memory extension (VisualMem-inspired) (DAN-4, stretch)

### Month 6 (November): v1 Candidate + .deb Packaging

**P0 actions:**
- [ ] Internal demo day: full 9-service stack, recorded (DAN-1 + DAN-2)
- [ ] `.deb` packaging for the full 9-service stack (DAN-1)
- [ ] `systemd` units for all 9 services (DAN-1)
- [ ] v1.0 release candidate: 9 services + Tauri app + OpenClaw + Privacy Threat Model published (DAN-1)
- [ ] Dogfood v1.0 RC for 2 weeks (DAN-1 + 4 users)

**P1 actions:**
- [ ] Package signing with Sigstore (DAN-1)
- [ ] Wake-word v0.1 (basic, not production) (DAN-2)
- [ ] memoryd: cross-session inference (DPCM-style System 2 layer) (DAN-4)
- [ ] proactived: ML-based scoring (rule + ML hybrid) (DAN-2)

**6-month exit criteria:**
- All 9 services production-grade with ≥100 tests each (8 existing × ~80 + 1 new × 100 + 1 new × 100 = ~840 total)
- `reasond` and `proactived` ship with hand-coded rules + HRM-Text 1B integrated
- End-to-end "AI companion that proactively speaks" demo, recorded
- SIA fork v0.1 published with measurable improvement over heuristic
- `.deb` package builds and installs on Debian 12
- Internal dogfooding data: 5 users × 1 week × 2 waves
- Privacy Threat Model published at `docs/privacy-threat-model.md`
- OpenClaw pinned to 2026.5.x+ with security hardening

---

## 3. The 12-Month Plan (2026-06-17 → 2027-06-17)

**Theme: ship the v1 wearable (if Redax lands), public launch in the Apple-gap window.**

### Month 7-9 (Dec 2026 - Feb 2027): Wearable Hardware (Redax track)

**P0 actions:**
- [ ] Finalize Redax board (or pivot to alternative: Rockchip RK3588, or Jetson Orin Nano) (sompdipto + hardware partner)
- [ ] Power characterization on aarch64 (THE measurement): LFM2.5-VL-450M, HRM-Text 1B, all-MiniLM-L6-v2 (DAN-3 + hardware)
- [ ] Battery sizing decision based on measurement (sompdipto)
- [ ] Thermal design (passive cooling; max skin-contact temp target: <42°C) (hardware partner)
- [ ] Camera module selection (V4L2 compatibility, low-light performance) (hardware partner)
- [ ] Weight validation (target <80g) (hardware partner)

**P1 actions:**
- [ ] Audio system: bone-conduction mic + speaker integration (hardware partner)
- [ ] Form-factor prototyping: 3D-printed enclosures (ForgeCAD)
- [ ] Wake-word v0.5 production-grade (DAN-2)

### Month 10-12 (Mar 2027 - May 2027): SIA Fork + v1 Ship

**P0 actions:**
- [ ] SIA fork: harness + weights (SIA-W+H) for the local model (HRM-Text 1B) (DAN-2, 2 months)
  - **Important:** this requires H100 budget and a privacy story for shipping fine-tuned weights
  - First fine-tuned HRM-Text 1B variant: "danlab-agi-hrm-v1" (DAN-2)
- [ ] Ship Dan Glasses v1.0 (or v0.9 if hardware slips) to first 100 users (sompdipto + DAN-1)
- [ ] Public launch: "India's first open-source AI glasses" (sompdipto)
- [ ] Apple-glasses-gap window: Q4 2026 → Q4 2027 (if Apple ships, pivot to "developer kit" framing; price $200 for hackers)
- [ ] Publish a paper / blog post: "Building a self-improving AI companion on a 2GB on-device stack" (DAN-2)

**P1 actions:**
- [ ] First fine-tuned LFM2.5-VL-450M variant: "danlab-vision-v1" (DAN-3)
- [ ] Memory v2 with cross-session inference deployed (DAN-4)
- [ ] Community: GitHub Discussions, Discord, monthly office hours (sompdipto)
- [ ] First third-party pilot: an Indian university deploys on a phone (accessibility use case)

**12-month exit criteria:**
- Dan Glasses v1.0 ships (or v0.9 if hardware slips)
- danlab-multimodal is honest about being harness+weights RL (not heuristic)
- ≥100 users in production
- ≥1 paper or significant blog post on the danlab-multimodal RL approach
- SIA-W+H demonstrated on at least one model
- Revenue target: 100 units × $400 = $40K

---

## 4. The 24-Month Plan (2026-06-17 → 2028-06-17)

**Theme: scale the runtime, ship weight updates as a product, go open-source-first.**

### Year 2: Open-source the runtime

**P0 actions:**
- [ ] Open-source `danlab-agi-runtime`: all 9 services as a single `pip install` / `apt install` package (DAN-1 + DAN-2, Q1 2027)
- [ ] Support: Debian 12, Ubuntu 24.04, Fedora 41, Arch (DAN-1)
- [ ] Documentation: "Run your own on-device AI companion" (DAN-1)
- [ ] Community: GitHub Discussions, Discord, monthly office hours (sompdipto)
- [ ] 1K+ GitHub stars on `danlab-agi-runtime` (sompdipto + community)

### Year 2: Full self-improvement (SIA-W+H) on multiple models

**P0 actions:**
- [ ] Move from HRM-Text 1B only to HRM-Text 1B + Gemma 4 1B + LFM2.5-VL-450M (DAN-2 + DAN-3)
- [ ] Production telemetry: what does the agent do over 30 days for 100 users? (DAN-2)
- [ ] First "danlab-agi-hrm-v2" with improved reasoning (DAN-2, Q3 2027)
- [ ] First "danlab-vision-v2" with improved VLM (DAN-3, Q4 2027)
- [ ] First "danlab-tts-v1" (if we ship our own TTS based on Kokoro fine-tune) (DAN-4, Q1 2028)

### Year 2: AGI thesis validation

**P0 actions:** Run the four critical tests that determine if the AGI thesis is real:

- [ ] Can the agent learn user patterns without explicit feedback? (proactive suggestions accuracy >70%)
- [ ] Can the agent personalize via memory? (memory recall precision@5 >80%)
- [ ] Can the agent self-improve? (RL loop delta vs. baseline >20% on held-out tasks)
- [ ] Can the agent run on a 2GB on-device stack? (binary size + RAM peak)

**If yes to all 4:** we have a credible "on-device AGI" story. Write the AGI paper. (DAN-2)
**If no:** we know what doesn't work. Pivot.

**24-month exit criteria:**
- `danlab-agi-runtime` v1.0 open-sourced, 1K+ GitHub stars
- First AGI paper submitted to a workshop (NeurIPS, ICML, or ACL)
- 1K+ Dan Glasses units sold (or in pre-order)
- $400K+ revenue
- 5+ third-party deployments (universities, accessibility, enterprise pilots)

---

## 5. The "What Could Kill This" List (v8 update)

| Risk | Likelihood | Impact | v8 mitigation |
|---|---|---|---|
| **Redax hardware slipping** | high | critical | Fall back to tethered prototype + alternative board (Rockchip RK3588, Jetson Orin Nano) |
| **OpenClaw security incident** | medium | critical | P0 hardening in month 1; pin version; disable ClawHub; consider internal fork |
| **LFM2.5-VL-450M power too high on aarch64** | medium | critical | Benchmark SmolVLM-256M and lower-frequency operation; thermal throttle; v2 NPU |
| **HRM-Text 1B inference code not published** | medium | high | Write our own; fallback to Gemma 4 1B (lower quality reasoning) |
| **SIA fork doesn't beat heuristic baseline** | medium | high | Publish the negative result honestly; the negative is still novel |
| **Anthropic "brake pedal" becomes regulatory** | low | medium | Watch; not actionable for us; we don't train frontier models |
| **Apple ships smart glasses in Q4 2026 (no delay)** | low | medium | Pivot to "developer kit" framing; price $200 for hackers |
| **Open-source community doesn't materialize** | medium | medium | Recruit from Indian universities (IIT, IISc); write Hindi tutorials; partner with NASSCOM |
| **Form factor decisions take 6+ months** | medium | high | Push for default (tethered, 80g) and move on |
| **KittenTTS license unclear → forced TTS swap** | low | medium | Plan Piper or Kokoro for v1.5; benchmark in month 4 |
| **Memory supercycle pricing (DRAM/NAND up 5-10×)** | medium | high | 32GB eMMC minimum for v1; design modular storage |
| **Meta Muse Spark API ships and enables third-party apps** | medium | medium | Our moat is open-source + on-device + privacy; not AI quality. We win on principles, not features. |
| **HRM-Text 1B architectural novelty is overstated** | low | low | We use it as a black box; if it doesn't deliver, we swap to Gemma 4 1B |

---

## 6. Resource Plan (v8, refined)

| Resource | 6-month | 12-month | 24-month |
|---|---|---|---|
| People (FTE equivalent) | 2-3 (Dan1, Dan2, Dan3) | 3-4 (+ Dan4 full-time + 1 community mgr) | 5-7 (+ hardware eng, designer) |
| Compute (cloud, dev) | $500/mo | $2K/mo (H100 for SIA fork) | $5K/mo (full RL training) |
| Hardware (Redax, dev boards) | $5K (1× dev kit) | $20K (5× dev kits + first 100 units) | $100K (first 1K units) |
| Revenue (cumulative) | $0 | $40K (100 units) | $400K (1K units) |
| Cash burn (cumulative) | $30K | $200K | $800K |
| Funding gap | -$30K | -$160K | -$400K |

**v8 funding reality:** to hit the 24-month plan, we need $400-800K of funding by month 12. Options: (a) YC S26 (deadline Aug 2026), (b) Surge (India), (c) Antler, (d) angel round (somdipto's network), (e) IndiaAI Mission grant, (f) ARPA-H (US).

**v8 verdict: the accelerator route is the most credible.** Apply to YC S26 in July 2026. The "open-source AGI from India" pitch is unusual enough to stand out. The "Anthropic brake pedal" backdrop actually *helps* the pitch (we're the safe, disclosed, open-source alternative).

---

## 7. v8 Differentiators vs. v7

v7 said:
- The desktop prototype is done. Build the reasoning layer.
- v7 critical-path is hardware form-factor decisions, not code.
- v7 biggest product gap is the reasoning layer (reasond + proactived).
- v7 biggest strategic bet is HRM-Text 1B as the on-device reasoning model.

**v8 says:**
- v7 was right. v8 is execution, not strategy.
- **OpenClaw security is P0, not P1.** CVE list is real. ClawHavoc is real. Hardening is week 1-2 work.
- **Privacy Threat Model is P0, not nice-to-have.** v8 ships a `docs/privacy-threat-model.md` document in month 1.
- **HRM-Text 1B integration is concrete.** Sapient released HF + vLLM support; the model is downloadable. v8 schedules the integration for month 2-3, not "v1.5."
- **SIA fork is month 6-9, not month 12.** v7 deferred; v8 advances because the SIA paper is concrete and the vLLM support makes inference viable.
- **The Apple-gap window is now.** Apple delayed to late 2027. v8 targets Q4 2026 launch. The window is real but small.
- **KittenTTS license check is P1, not v1.5.** If unclear, we switch before v1 ships, not after.

---

## 8. What "AGI" Means for Danlab (v8 reframe)

**We are not building AGI in the frontier-model sense.** Frontier AGI is OpenAI, DeepMind, Anthropic's job. We don't have the compute, the data, or the mandate.

**We are building the deployment layer for AGI.** The thesis:

1. Frontier models will keep getting better, but they will never run on a wearable. (Latency, cost, privacy, connectivity.)
2. The AGI on a wearable will be a *composition* of small models: vision (LFM2.5-VL-450M), STT (whisper → Moonshine), TTS (KittenTTS → Piper/Kokoro), reasoning (HRM-Text 1B), memory (all-MiniLM-L6-v2 → BGE-small-en-v1.5 + typed schema).
3. The differentiator is not any single model. It is the **system** that runs them, the **memory** that connects them, the **proactive layer** that decides when to speak, and the **self-improvement loop** that makes it better over time.
4. The moat is the **user data** (private, on-device, never leaves the device) + the **open-source community** that forks and extends the stack.

**v8 makes the thesis load-bearing in the Anthropic-brake-pedal era.** The brake pedal memo proposes a *coordinated, verifiable* pause for frontier labs. Danlab benefits from this norm: we are the open, disclosed, privacy-first alternative. We don't compete with the frontier; we deploy it. We don't trigger the brake pedal; we don't need to.

**This is a 10-year thesis, not a 10-month thesis.** v8 lays the foundation. v9 will reframe again. The plan is to keep the plan alive, not to defend it.

---

## 9. What somdipto Needs to Decide in the Next 14 Days

1. **Power source for v1** — tethered, in-frame big battery, or aggressive power gating? (See §1.)
2. **Weight target for v1** — 50g, 80g, or 120g?
3. **Cloud LLM budget for SIA fork** — pay Claude Sonnet 4.6, or run HRM-Text 1B + Gemma 4 1B local?
4. **v1 pricing target** — $300, $400, or $500?
5. **Apple glasses delay strategy** — beat Apple in 2026-Q4, or wait for 2027-Q3?
6. **Open-source license for the runtime** — Apache 2.0, MIT, or BSL?
7. **OpenClaw security posture** — keep current, fork to internal-only, or replace?
8. **Funding route** — apply to YC S26 (Aug 2026), Surge, or angel?

**Decisions #1, #2, #7 are the critical path.** Until they are made, the wearable hardware and the security story cannot start. The 6-month code work can proceed in parallel.

---

## 10. The One-Sentence Pitch (v8)

> **Danlab is building the open-source, on-device, self-improving AI companion stack — starting with Dan Glasses, the first AI glasses designed in India with the privacy of offline and the openness of Apache 2.0.**

---

*End of v8 AGI roadmap. Companion artifacts: `dan2-research-report.md` (deep dives), `dan2-architecture-review.md` (concrete fixes), `dan2-model-analysis.md` (replacement candidates), `dan2-papers-to-read.md` (what to read).*

# Danlab AGI Roadmap — Dan2 (2026-06-21)

> **Mission:** Build toward AGI from India. Two vectors run in parallel: (1) ship Dan Glasses as a real product, (2) publish credible self-improving AI research that no one else is doing from this part of the world.

---

## The Strategic Wedge

Three observations that define the roadmap:

1. **The wearables category is exploding** (Snap Specs $2,195, Meta Ray-Ban Gen-2, Google Project Aura). All are cloud-dependent. All are reactive.
2. **No one is shipping on-device proactive AI** at consumer scale. The closest published architecture is ProAgent (arXiv:2512.06721) — 27.7% higher proactive accuracy, 85% user satisfaction.
3. **The credible path to recursive self-improvement exists and is open-source** (Hexo Labs' SIA, MIT, May 2026). Scored 0.701 on LawBench vs Claude Code's 0.173.

**Danlab's wedge = on-device + proactive + self-improving.** Cloud wearables are commodity. Reactive on-device is research. Proactive on-device is unclaimed.

---

## 6-Month Window (Now → Dec 2026)

**Theme: Make Dan Glasses a credible demo + lay the SIA foundation.**

### Ship Hardening (Dan1 foundation stream)
- [ ] **Systemd units for all 6 services** (Dan1 + Dan2 priority). `Restart=on-failure`, `RestartSec=2`. This is a 2-hour job, not a quarter.
- [ ] **`scripts/health.sh`** that curl-checks all 7 services and updates STATUS.md or posts to Telegram. Replaces stale manual status.
- [ ] **OpenClaw session checkpointing.** Snapshot `state.json` every 5s. On restart, replay. 1-day job.
- [ ] **Memoryd Mem0-fork.** Add LLM extraction step (using LFM2.5-1.2B-Thinking or HRM-Text per AGENTS.md). API goes from `/query` to `add + search`.

### Product (Dan Glasses)
- [ ] **VisionDashboard.tsx wired** (Dan3 in progress per dan3.md).
- [ ] **End-to-end desktop demo** (audit transcript → perceptiond → LLM extraction → memoryd query → ttsd speak). 1 working US (US-5: hands-free check-in).
- [ ] **All services exposed via OpenClaw MCP** (mcporter wired per Dan1). Telegram `@danlab_bot` can trigger any service.

### Research (Dan2 stream)
- [ ] **Fork SIA** ([hexolabs.com/sia](https://hexolabs.com/sia), MIT). Run harness-only loop on danlab-multimodal's heuristic benchmark. Use LFM2.5-1.2B-Thinking as Feedback-Agent. Publish a "first recursive self-improvement result from India" arXiv preprint.
- [ ] **Measure LFM2.5-VL-450M on dev board.** Latency, power (if possible), failure modes. Target: <2s/frame in watchful mode. Document edge reliability gap (negation collapse) and add temporal-consistency check.

### Marketing (Dan1 marketing stream)
- [ ] **"The only AI wearable that doesn't upload your life"** as headline. Lean into privacy. Drop any "RL" claim until SIA fork ships.

**Outcome by Dec 2026:** Working desktop demo. SIA preprint on arXiv. Six services supervised by systemd. Credible India-AGI narrative. ~5-10K stars on danlab-multimodal (currently small).

---

## 12-Month Window (Dec 2026 → Jun 2027)

**Theme: Genuine self-improvement + first wearable.**

### Self-Improvement (Q1 2027)
- [ ] **Add QLoRA weight updates to SIA loop.** Now the harness AND weights modify themselves. First genuine recursive self-improvement. Re-run on danlab-multimodal benchmark and on a new agentic benchmark (SWE-bench-lite, ALFWorld-lite).
- [ ] **Audit harness-only vs harness+weights on a verifiable benchmark.** Publish results.

### Wearable Path (Q1-Q2 2027)
- [ ] **Pick Redax reference board** based on actual benchmarks: Orange Pi 5 Pro or RPi 5 + Hailo-10H. Decide on aarch64 architecture.
- [ ] **Apply AAAC + GPTQ to LFM2-VL-450M** for sub-200MB vision stack.
- [ ] **Ship openclaw-proactive** watcher. Reads audiod WS + perceptiond ring buffer. Scores events vs user context. Triggers TTS when score > threshold. This is the ProAgent architecture.
- [ ] **Power characterization on aarch64.** Redax dev board + INA219 current sensor. Measure LFM2.5-VL-450M, whisper.cpp, KittenTTS watts per inference. Publish a public power benchmark.
- [ ] **Form-factor decision.** <50g target or <80g minimum. Battery placement. Display or no-display.

### Memory (Q1 2027)
- [ ] **MemMachine-style STM + LT split in memoryd.** STM = last 20 turns in-prompt. LT = pgvector or sqlite-vec. Preserves ground truth.
- [ ] **MemGate-style filter** (9M-param) between retrieval and prompt. Prevents irrelevant memories polluting responses.

### Marketing
- [ ] **First 50 GitHub stars** on dan-glasses (per Dan1 v66 → v67 transition plan).
- [ ] **First product-market fit signal.** 10-100 users running the desktop demo daily.

**Outcome by Jun 2027:** Working recursive self-improvement on the SIA fork. Proactive OpenClaw watching events. <200MB vision stack. Power benchmark published. Memory architecture upgraded.

---

## 24-Month Window (Jun 2027 → Jun 2028)

**Theme: Open-ended evolution + wearable ship.**

### Self-Improvement (H2 2027)
- [ ] **Build the Darwin Gödel Machine** (Sakana AI's open-ended evolution). Archive of perceptiond prompt templates, audiod VAD configs, memoryd extraction patterns. Self-evolving Danlab.
- [ ] **DGM-Hyperagent meta-level.** Meta-agent improves meta-agent. Self-referential.
- [ ] **Publish at NeurIPS / ICML.** "Recursive Self-Improvement for Edge AI Wearables" or similar.

### Wearable (H2 2027)
- [ ] **Wearable v1 dev kit.** 50-100 units to early adopters.
- [ ] **Power state machine working** (sleep / idle / watchful / active). <4h battery life at 5W average. Thermal throttle to Gemma fallback.
- [ ] **Privacy posture: 100% on-device by default.** Cloud only opt-in.

### Memory (H2 2027)
- [ ] **Continual learning.** Memoryd learns user-specific patterns (frequent locations, recurring contacts). Compression + forgetting (MemReader-style).

### Positioning
- [ ] **"On-device proactive AI"** as the market position. Compete with Meta Ray-Ban and Snap Specs on privacy + proactivity.
- [ ] **India-from-AGI narrative.** Build research community in Bangalore / Hyderabad.

**Outcome by Jun 2028:** First wearable dev kit. DGM-style open-ended evolution published. Credible AGI-from-India research track. Danlab is known for: (a) the only on-device proactive AI, (b) SIA-fork as a public recursive self-improvement result, (c) DGM at consumer scale.

---

## What We Stop Doing

To focus, we drop:

- **No new services in v1.** The 5-service split is locked. Resist the urge to add `noted`, `cald`, `healthd` etc.
- **No wake word in v1.** PRD §8 says deferred to v1.5. Stick to that. PTT is fine.
- **No display in v1 wearable.** Snap Specs proves display adds $1,500+ to BOM. Skip it.
- **No cellular in v1.** Wi-Fi only. Saves power and carrier certification.
- **No multi-user.** Single user per device. Hard constraint.
- **No social features.** Capture + share is Meta's lane. Don't compete there.
- **No foundation-model training.** Use AWQ/GPTQ/QuaRot on existing models. Don't train from scratch.

---

## The Three Bets

**Bet 1: On-device proactive AI is a real wedge.**
- Time horizon: 12-18 months.
- Risk: Snap or Meta ships proactive AI on-device before us.
- Mitigation: Be first to publish. The window is 2026-2027.

**Bet 2: SIA-fork is the credible recursive self-improvement path.**
- Time horizon: 6-12 months.
- Risk: Hexo Labs or Sakana AI ships a closed-source productization first.
- Mitigation: Fork MIT-licensed code, ship before productization. Open-source moat.

**Bet 3: LFM2.5-VL-450M stays the right edge VLM for 12 months.**
- Time horizon: 6-12 months.
- Risk: A new edge VLM (OmniVLM-968M, Firebolt-VL, or a Llama 4 Nano) leapfrogs LFM2.5.
- Mitigation: perceptiond has SmolVLM-256M as fallback. Add OmniVLM-968M and SmolVLM-500M to the candidate list. Switch when benchmarks prove one is better.

---

## Open Questions for somdipto

1. **Compute budget.** What's the realistic GPU compute budget for the SIA fork and any future training? This defines what's possible.
2. **Hardware timeline.** When does Redax board lock? Need this for wearable dev kit timing.
3. **Privacy posture — hard or soft?** "No cloud ever" is a stronger story but limits capabilities (multi-device sync, web search, etc.). Pick a side.
4. **Open-source posture.** SIA fork is MIT-licensed (good). But are we ready to open-source the danlab-multimodal loop? Once it's MIT, Meta or Google could productize it.
5. **Geographic bet.** Stay in India-only or go US/EU for hardware manufacturing? Affects wearable timeline.
6. **Paperclip.** Currently dormant. Should we revive it as a `dani-skills` plugin, or let it stay dead?

---

## What This Roadmap Is Not

- It's not a foundation-model training plan. Danlab won't train its own LLM. The compute cost is wrong for India-from-AGI.
- It's not a research-only path. The product (Dan Glasses) and research (SIA fork) reinforce each other.
- It's not a "ship the wearable first" plan. The wearable is gated on power measurements we don't have yet.

---

*Dan2, 2026-06-21. Aligned with PRD v1.0, canonical analysis, and the SIA literature.*

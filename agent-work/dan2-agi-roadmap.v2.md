# Danlab AGI Roadmap — 6 / 12 / 24 Month Plan

**Author:** Dan-2
**Date:** 2026-07-01
**Horizon:** Now (July 2026) → July 2028
**Anchored to:** `dan2-research-report.md`, `dan2-architecture-review.md`, `dan2-model-analysis.md`, `dan2-papers-to-read.md`

---

## North Star (24-month)

> **Danlab ships the open, on-device, privacy-preserving, self-improving AI glasses substrate. We are the credible research-backed answer to "AGI from India" — not a frontier-scale lab, but a composable edge-first stack that anyone can fork, audit, and run.**

**Why this is the right North Star (mid-2026 context):**
- Commercial AI glasses (Meta Ray-Ban Display, Snap Specs, Brilliant Halo, upcoming Apple, Google × Warby Parker) all close-loop through vendor clouds. None offers local-first + open-weights + on-device. This is the defensible wedge.
- Jack Clark (Anthropic) puts 60% on no-human-involved AI R&D by end of 2028. Anthropic's own data: ~80% of merged code is Claude-written, Claude agents completed an open-ended safety research project in April 2026. **SIA (Hexo Labs, MIT, May 28 2026) is the first open-source harness+weights self-improvement framework.** Danlab is well-positioned to be the *edge implementation* of this trend.
- The "AGI from India" thesis is now credible because the open-weight + edge-inference + agentic-loop stack is shippable today. The bottleneck is integration and self-improvement, not raw model capability. Shivik Labs (Noida) shipped TRIDENT in Dec 2025; we are not alone, and we are not late.

---

## 6-Month Plan: Now → December 2026

**Theme: Lock the substrate. Ship the foundation. Publish the pre-RL → RL transition.**

### Q3 2026 (Jul → Sep): Foundation hardening

**Goal:** Make the existing 9-daemon substrate reliable enough to demo to investors and researchers, and produce a publishable "pre-RL → real RL" artifact.

**Engineering:**
- [ ] Migrate all 9 daemons to `register_user_service` mode=process with auto-restart (eliminates the memoryd-hung class of bug)
- [ ] Add unified `GET /services.json` health aggregator (eliminates the port-table rot)
- [ ] Add `/live` and `/ready` liveness/readiness split to perceptiond, memoryd, toold, ttsd, os-toold (matching audiod's v1.1 contract)
- [ ] Add `dan-glasses/scripts/up.sh` and `down.sh` for clean bringup/teardown
- [ ] Lock Tauri v2 app at canonical path with name+identifier matching spec
- [ ] Fix cargo 1.65 → 1.77+ for native Tauri builds
- [ ] Wire audiod → memoryd for transcript ingest
- [ ] Wire perceptiond → memoryd for salient-frame caption ingest (use LFM2.5-Extract JSON schema for direct ingestion)
- [ ] Add `mcporter emit-ts zo --mode client` → `Services/zo-mcp-bridge/zoClient.ts` typed wrapper
- [ ] Document the one-time Tailscale bootstrap for somdipto (gVisor blocks it but the path is documented)

**Research (the headline deliverable):**
- [ ] **Port danlab-multimodal to SIA-W+H** (Hexo Labs, MIT, GitHub `hexo-ai/sia`). LFM2.5-VL-450M as the task agent, Claude Sonnet 4.6 as the Feedback-Agent (or LFM2.5-1.2B-Thinking local for the privacy-first path). **This is the headline research deliverable for the quarter.** The danlab-multimodal README already points to SIA; this just executes.
- [ ] Measure on a multi-turn code-review task: does SIA-W+H beat the hand-coded heuristic?
- [ ] Publish a technical report: **"SIA-W+H for Multimodal Self-Improvement: From Heuristic to Genuine RL."** Target: arXiv + a blog post. **First-mover artifact in the open-source 450M-class VLM self-improvement space.**

**Product:**
- [ ] Polish the BootstrapWizard UX in the Tauri app
- [ ] Publish the Tauri app as a Zo Site (public `*.zocomputer.io`) so the wearable form factor has a phone-companion option
- [ ] Add per-service status pills on the home screen
- [ ] Add a "service health" panel that aggregates all 9 daemons in one view
- [ ] Land the perceptiond power-mode redesign (inference gating, not capture gating) — see architecture review

**Decision points at end of Q3:**
- Is SIA-W+H measurably better than the hand-coded heuristic on danlab-multimodal? → If yes, double down on the SIA port in Q4. If no, investigate why (probably the reward model is too weak).
- Is the Zo Site version of the Tauri app seeing real usage? → If yes, prioritize it over a native `.deb` for the desktop prototype.
- Does the SIA-W+H port scale to LFM2.5-VL-450M as the task agent? → If yes, that's a publishable result.

### Q4 2026 (Oct → Dec): Memory substrate upgrade + wake-word

**Goal:** Upgrade memoryd to v1.5 (temporal reasoning + episode boundaries + consolidation). Add wake-word (openWakeWord, ~3MB) to audiod so the user doesn't need PTT.

**Engineering:**
- [ ] memoryd v1.5: add `valid_from` / `valid_to` columns, `/query?as_of=YYYY-MM-DD` endpoint
- [ ] memoryd v1.5: add `episoder` daemon — watches audiod/perceptiond/conversation events, emits episode_started/ended
- [ ] memoryd v1.5: nightly memory consolidation daemon (summarize, demote, expire)
- [ ] audiod v1.5: wire openWakeWord as a low-power front-end; audiod runs PTT-only or wake-word-activated
- [ ] perceptiond: implement salience-*delta* gate (not salience); VLM only fires on novelty
- [ ] perceptiond: add batched VLM inference (batch=2-4 salient frames)
- [ ] perceptiond: switch chat template to LFM2.5-Extract for structured-JSON captions
- [ ] TTS A/B harness: KittenTTS vs Kokoro-82M q4 vs Piper
- [ ] Document the package-signing mechanism (GPG concrete) per canonical analysis

**Research:**
- [ ] Benchmark Mem0 v3 vs our memoryd v1.5 on temporal-reasoning tasks. If Mem0 wins on a clear metric, adopt it. If we win, publish.
- [ ] Pilot the "fast-path / slow-path" VLM architecture on aarch64 (requires Redax or equivalent). Measure per-frame energy.
- [ ] Write the SIA-W+H paper follow-up: "Lessons from 100 self-improvement iterations on a 450M VLM."

**Product:**
- [ ] Ship a "memory browser" UI in the Tauri app (browse memories by type, date, episode)
- [ ] Land the proactive pre-filter (PRPF pattern, 2026) as a thin layer on top of perceptiond
- [ ] Add the TTS quality knob to settings (KittenTTS-mini / KittenTTS-base / Kokoro-82M-q4)

**Decision points at end of Q4:**
- Has the wake-word front-end improved user retention in the desktop prototype? → If yes, ship it.
- Did Mem0 beat our memoryd v1.5? → If yes, migrate. If no, publish the comparison.
- Is the Redax board closer to availability? → If yes, start wearable migration. If no, continue the desktop track.

---

## 12-Month Plan: July 2026 → June 2027

**Theme: Self-improving substrate. Wearable-ready software. First publishable research artifacts.**

**Major milestones:**
1. **Q1 2027 (Jan → Mar): Self-improving memory daemon**
   - Ship `memoryd v2`: proactive retrieval loop (Databricks memory-scaling pattern), Zettelkasten auto-linking (A-MEM pattern), memory type promotion/demotion
   - Ship `perceptiond v2`: bi-temporal memory, episode-scoped retrieval
   - Publish: "Open-Weight Edge Memory for AI Companions" — paper comparing memoryd v2 vs Mem0 v3 vs Zep vs Letta on temporal-reasoning + episode-recall benchmarks

2. **Q2 2027 (Apr → Jun): Wearable migration (if Redax is available)**
   - Power characterization on aarch64 (the missing data from §D.3)
   - Implement the full power state machine (sleep / idle / watchful / active / deep-idle)
   - Thermal model + throttle to smaller model (SmolVLM-256M, then Gemma3-270M)
   - First wearable form factor build
   - Publish: "Power Characterization of LFM2.5-VL-450M on aarch64 Wearable Hardware" — **the first public power-data paper for this model class on a wearable target**

3. **Q2 2027: Marketing + ecosystem**
   - Open the daemon codebases to external contributors
   - Publish the developer kit: how to write a new salience gate, how to add a new memory type
   - "AGI from India" research paper: position the danlab stack in the global SOTA
   - First conference talk: "Self-Improving AI Glasses from India" (NeurIPS workshop, ICML workshop, or ACL)

**Decision points at end of Q2 2027:**
- Is the wearable form factor viable (4h battery, <50g, passive cooling)? → If yes, ship the dev kit. If no, the desktop track continues and the wearable is deferred.
- Has the SIA-W+H work on danlab-multimodal produced a publishable result? → If yes, the research track is validated. If no, reassess the SIA port.

---

## 24-Month Plan: July 2026 → June 2028

**Theme: AGI-from-India thesis operational. A self-improving, on-device, open-stack AI companion.**

**Major milestones:**

1. **Q3 2027 (Jul → Sep): SIA-W+H at scale**
   - Generalize the SIA port from danlab-multimodal to the full dani/danlab stack
   - Run SIA-W+H against danlab-multimodal, danlab-audiod, danlab-perceptiond in parallel
   - First multi-agent self-improving system (each daemon improves its own task model)
   - Publish: "Multi-Agent Self-Improvement on Edge: Lessons from a 9-Daemon Substrate"

2. **Q4 2027 (Oct → Dec): Cross-modal grounding**
   - perceptiond's LFM2.5-Extract emits `(timestamp, object, action)` triples
   - audiod's whisper events are timestamped and aligned
   - memoryd ingests cross-modal episodes (vision + audio within the same time window)
   - Enables US-1 (Encounter Recall) and US-2 (Contextual TaskReminder) in the PRD

3. **Q1 2028 (Jan → Mar): External developer program**
   - Open the substrate: skill SDK, memoryd schema documentation, perceptiond salience-gate authoring
   - First community-contributed memory type or salience detector
   - Apply for a research grant (EU Horizon, NSF, India SERB, or private foundation)

4. **Q2 2028 (Apr → Jun): The "AGI from India" position**
   - Compile all artifacts: SIA paper, memoryd paper, power-characterization paper, SIA-W+H generalization
   - Submit a journal paper: "An Open, Self-Improving, Edge-First Stack for AI Companions" — to JMLR, TACL, or Nature Machine Intelligence
   - Position for a research-lab-grade funding round (or a Series A if the product track is also viable)

---

## What we are NOT doing (and why)

- **Building a frontier-scale LLM.** OpenAI / Anthropic / Google / DeepMind have hundreds of millions of dollars and 100+ GPU clusters. We are a 2-person research-and-product lab. We use their open weights (LFM2.5, Whisper, Kokoro, Llama, Qwen) and add value via the integration + self-improvement + on-device deployment layers.

- **AR display hardware.** The AR display market is dominated by Meta (with EssilorLuxottica), Snap (Snap OS), Apple (cancelled Vision Pro 2, delayed glasses), Google (Warby Parker). We don't have the manufacturing, the optics, or the capital. Our wedge is the *software substrate* — the AI that runs on whatever hardware the user has.

- **Cellular / always-connected wearables.** Cellular modem + battery is the wrong power trade for v1. Wi-Fi only, with the option to tether to a phone for connectivity. The Brilliant Labs Halo model.

- **A proprietary model.** Open-weight is a wedge, not a sacrifice. Liquid AI is betting on this; Hexo Labs is betting on this; we should too. The day we train a custom model, we lose the open-weight advantage.

- **A social / sharing product.** Meta Ray-Ban already does capture+share. We don't compete on that axis. We compete on **memory + proactivity + privacy**.

---

## Open Questions for Somdipto

1. **SIA-W+H compute budget.** SIA-W+H requires LoRA fine-tuning of LFM2.5-VL-450M, which is doable on a single A100/H100. We need access to one. Options: a free-tier Colab / Lightning Studio / Lambda cloud credits. Can you allocate a $200-500/month cloud-GPU budget for the SIA-W+H runs?
2. **Redax timeline.** When does the hardware team expect the Redax board? Without it, the wearable migration is parked.
3. **Conferences / publishing.** Should we target arXiv-first, or submit to NeurIPS 2026 (deadline ~May 2026 — already past), ICML 2027 (Jan 2027 deadline), or ACL 2027 (Jan 2027 deadline)? What's the right venue for the SIA paper?
4. **Partnerships.** Brilliant Labs (Halo) and Shivik Labs (TRIDENT) are the two most direct peers. Worth a conversation. Are there other Indian AI labs (Krutrim, Sarvam, Soket AI) we should be talking to?
5. **Funding runway.** If we publish the SIA paper, we can credibly apply for research grants. If we ship the wearable dev kit, we can credibly raise a seed round. What's the appetite?

---

*See `dan2-research-report.md` for the full technical evidence behind every claim in this roadmap. See `dan2-papers-to-read.md` for the reading list that grounds the research tracks. See `dan2-architecture-review.md` for the structural risks that gate the engineering tracks. See `dan2-model-analysis.md` for the model selection rationale.*

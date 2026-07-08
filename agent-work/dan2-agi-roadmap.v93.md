# Danlab AGI Roadmap — 6 / 12 / 24 Months

**Author:** Dan2
**Date:** 2026-06-26
**Status:** v93 — delta on v12 (refreshed for Liquid AI retrievers Jun 18, Microsoft Scout Jun 2, Halo at $299, hardware timeline compression)

---

## North Star (v93 update)

**v12 north star:** "Ship the first proactive, on-device, open-source AI companion for wearables — and become the credible open-weights entrant in the recursive-self-improvement race by 2027."

**v93 north star:** **Same goal, accelerated timeline.** Three signals landed in the last 48 hours that compress the v12 schedule:

1. **Liquid AI retrievers shipped Jun 18** — memoryd v2 is now a fork-and-ship, not a research project
2. **Microsoft Scout launched Jun 2** — OpenClaw category now has 2 serious vendors; gateway survival becomes the #1 risk
3. **Halo at $299 with proactive** — the open-source wedge is contested on price; we must compress hardware timeline

**Revised north star:** *"Ship Dan Glasses v1 (with awarenessd + memoryd v2 + SIA-forked danlab-multimodal) by Q4 2026 at $399 BOM, beating the Google × Warby Parker smart glasses launch to claim the 'open, auditable, multilingual AI glasses' category."*

---

## 6-Month Roadmap (Jul–Dec 2026) — compressed

### Q3 2026 (Jul–Sep): **The Wedge Quarter**

**Engineering (in priority order):**
1. **awarenessd v0.1** — NEW daemon on port 8745. Subscribes to perceptiond + memoryd. Fires TTS/Telegram on salience+memory match. Spam cap (3/hr), time-of-day gate, confidence threshold > 0.85. **5-pillar design from "Proactive Systems in HCI/AI" (arXiv:2606.25149)** [^1]. **Effort: 3 weeks.**
2. **memoryd v2** — swap `all-MiniLM-L6-v2` → **LFM2.5-Embedding-350M** (1024-dim, 22 Indic languages, Apache-2.0-equivalent) [^2]. Add HNSW via `usearch`. **Effort: 2 weeks (fork-and-ship).**
3. **DanClaw proxy** — wraps OpenClaw, exposes hardened `danclaw/healthz`, swallows OpenClaw restarts, mirrors in-flight messages to memoryd. **v38 carry-forward; v93 elevates to Action 1.** **Effort: 1 week.**
4. **LFM2.5-VL-450M power characterization on aarch64** — 1-week measurement sprint on Jetson Orin Nano Super ($249 proxy). Capture watts-per-frame at Q4_0, 512×512, watchful mode. **Effort: 1 week.**
5. **SIA-on-danlab-multimodal fork** — fork `hexo-ai/sia` (MIT). Swap Claude Sonnet 4.6 → LFM2.5-1.2B-Thinking as Feedback-Agent. Run 10 generations on SmolVLM2-256M. Wrap in SGM-style e-value gate. **Effort: 4 weeks.**
6. **NPU acceleration spike** — try llama.cpp Vulkan on Adreno, Liquid AI's AMD Ryzen AI path for LFM2.5. **Effort: 2 weeks.**

**Research:**
- Benchmark LFM2.5-VL-450M vs Gemma 3n (E2B) vs SmolVLM2-256M on the danlab-multimodal harness. Decide v1 wearable model.
- Track Microsoft Scout's OpenClaw fork — write 1-page compat brief this week.

**Marketing (Dan1 territory):**
- Show HN: "We built an open-source AI glasses platform with a proactive agent. Published every daemon's liveness status. 8/8 live."
- GitHub org public: `danlab-dev` with all repos.
- First STATUS.md weekly post: 8/8 live + new awarenessd daemon added.

**Critical open questions to resolve this quarter (NEW from v93):**
1. **Hardware timeline compression** — can we ship a wearable dev-kit by Q4 2026 to beat Google × Warby Parker Fall 2026? **v93 elevates this from "nice-to-have" to "category-defining."**
2. **BOM target:** $349 (aggressive) or $399 (premium)? **v93 recommends $399 + open-source auditability as the price-perceived-value wedge.**
3. **OpenClaw fork compatibility** with MS-Scout — binary choice in 60 days if Microsoft diverges.

### Q4 2026 (Oct–Dec): **The Launch Quarter**

**Engineering:**
1. **awarenessd v1.0** — confidence-tuned, A/B tested against "no awarenessd" baseline. Documented failure modes. **Internal 5-person beta.**
2. **memoryd v2.5** — add **LFM2.5-ColBERT-350M** late-interaction reranker. Episodic→semantic nightly consolidation cron (03:00 local).
3. **Wearable v0.5 build** — port all services to aarch64. .deb + systemd. Thermal throttle at 42°C. **If hardware timeline holds.**
4. **TTS upgrade** — Kokoro-82M as primary (Hindi voices), KittenTTS as fallback. Document quality delta in ttsd/SPEC.md.
5. **Power state machine** — full sleep/idle/watchful/active transitions with measured watt targets.
6. **dglabs-eval proactive subset** — benchmark the awarenessd proactive loop on a 5-task ProActEval subset. **Public eval before launch.**

**Research:**
- Publish SIA-on-danlab-multimodal results: "SIA-on-SmolVLM-256M, Feedback-Agent = 1.2B open-weight." This is the paper.
- First versioned evals framework.

**Marketing:**
- Conference presence: NeurIPS 2026 (deadline ~May 2026, paper accepted?) or Fall workshop.
- Blog post: "The first open-weight SIA result."
- Wearable dev-kit launch (if hardware holds).

---

## 12-Month Roadmap (Jul 2026 – Jun 2027)

### Theme (v93 update): **"The credible open-weights entrant in the RSI race + first multilingual AI glasses on the market."**

By Jun 2027 we should be **known** as the lab that took the SIA harness+weights pattern from Claude-Sonnet-class Feedback-Agents to sub-1.5B open-weight Feedback-Agents **AND** the lab that shipped the first multilingual AI glasses.

### H1 2027 (Jan–Jun)

**Engineering:**
- **awarenessd v2** — LLM-based "should I fire?" decision using LFM2.5-1.2B-Thinking. Move from rules-engine to learned salience.
- **Wearable v1.0** — aarch64 build. Real-world 4h+ battery life validated.
- **memoryd v3** — knowledge-graph layer (entities + relations) on top of vector memory. Inspired by MAGMA [^3] + Synapse [^4].
- **Paperclip revival** — wire as the "external agent" gateway for Dan Glasses.

**Research — flagship papers for 2027:**
- **"On-Device Recursive Self-Improvement with Sub-1.5B Feedback-Agents"** — SIA + LFM2.5-1.2B-Thinking on SmolVLM2-256M + LFM2.5-VL-450M. NeurIPS 2027 or ICML 2027.
- **"Proactive AI Companions: A 90-Day Field Study"** — N=5–10 users, 90 days. CHI 2028.
- **"The Awareness Threshold: When Should an AI Companion Initiate?"** — formalize salience+confidence+time-of-day gate.

**Marketing:**
- Conference presence: NeurIPS / ICML / CHI 2027.
- Open-source community: 1K+ stars on awarenessd, 5K+ on dan-glasses, 10K+ on danlab-sia.
- Brand: "Danlab — proactive, auditable, on-device, multilingual."

---

## 24-Month Roadmap (Jul 2026 – Jun 2028)

### Theme (v93 update): **"Toward AGI from the edge — wearable-born, on-device, self-improving."**

By Jun 2028, Jack Clark's 60% RSI timeline says recursive self-improvement should be real. **We want to demonstrate it on a wearable, on-device, with a sub-2B parameter stack.**

### H2 2027 – H1 2028

**Engineering:**
- **Dan Glasses v2 hardware** — custom aarch64 SoC with NPU acceleration. Smaller, lighter.
- **awarenessd v3 + SIA loop on-device** — proactive agent rewrites its own salience gate based on user feedback.
- **Multi-modal agentic foundation** — vision + audio + IMU + bio-signals unified token stream.
- **memoryd v4** — full SIA-style self-curating memory.

**Research — long bets:**
- **"Wearable-Born AGI: 365 Days of a Self-Improving On-Device Agent"** — flagship paper if we can credibly claim RSI on a wearable.
- **Open-source release of entire Dan Glasses stack** — Apache 2.0 / MIT. **The moat.**
- **India-origin positioning** — Hindi, Tamil, Bengali, Telugu, Marathi, code-switching mid-sentence. **Unique. Underserved.**

**Marketing:**
- Book: "Building AGI from India" — Dan + somdipto.
- Series A: $10–25M on the strength of proactive agent + RSI research + India market.

---

## What we are NOT doing (carried from v12, unchanged)

1. Not building a display (camera + AI only).
2. Not building social/share.
3. Not competing on raw model size (sub-2B only).
4. Not building wake-word in v1 (v1.5 with openWakeWord).
5. Not chasing every wearable category.

---

## Dependencies / Pre-requisites (v93 update)

### Must resolve in Q3 2026 (compressed)

1. **Hardware** — must ship a wearable dev-kit by Q4 2026 to beat Google × Warby Parker Fall 2026.
2. **Microsoft Scout / OpenClaw compatibility** — 1-page brief this week.
3. **BOM target** — $349 or $399? Recommend $399.
4. **Target battery life** — 4h or 6h?
5. **Funding posture** — implied or quiet?
6. **GitHub org name and domain ownership**.

### Can defer to Q4 2026 or later

1. Wake-word implementation
2. Knowledge-graph layer in memoryd (memoryd v3)
3. Hardware v2 design
4. Series A decision

---

## Risk Register (v93 update)

| Risk | Impact | v93 Mitigation |
|---|---|---|
| **Halo at $299 + Google × Warby Parker Fall 2026 compresses the window** | Critical | Compress hardware timeline to Q4 2026 launch. Differentiate on multilingual + auditability. |
| **Microsoft Scout forks OpenClaw incompatibly** | High | DanClaw proxy layer (v38/v93 Action 1) insulates us. |
| **LFM2.5-VL-450M power draw unmeasured on aarch64** | High | 1-week measurement sprint in Q3 2026 (proxy: Jetson Orin Nano Super). |
| **No `awarenessd` shipped** | Critical | Action 1 of Q3 2026. |
| **OpenClaw 7th carry-forward crash** | High | DanClaw proxy. |
| **memoryd flat cosine index won't scale past ~10K memories** | Medium | LFM2.5-Embedding-350M + HNSW in Q3 2026. |
| **TTS English-only** | Medium | Kokoro-82M in Q4 2026. |
| **Funding runway unclear** | Medium | Series A target H1 2027 (after awarenessd + SIA results). |

---

## Sources

[^1]: https://arxiv.org/html/2606.25149v1 — Proactive Systems in HCI and AI (Jun 2026)
[^2]: https://www.liquid.ai/blog/lfm2-5-retrievers — LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M (Jun 18, 2026)
[^3]: https://arxiv.org/pdf/2601.03236v1 — MAGMA: Multi-Graph Agentic Memory Architecture
[^4]: https://arxiv.org/pdf/2601.02744 — Synapse: Episodic-Semantic Memory via Spreading Activation
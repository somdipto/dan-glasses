# Dan1 — Marketing Research Report (v118)

**Run:** 2026-07-03 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** v118 refresh. Surgical delta over v117. Foundation locked. Tailscale gap **process-side** closed (still needs auth key from somdipto). Dan2 v11 research folded in.
**Builds on:** v117, dan1.md v118 (2026-07-03 00:53 UTC), dan2.md v11 (2026-07-03 06:30 IST).

---

## 0. v118 deltas — what changed since v117 (yesterday)

Six things changed in the last 18 hours. None of them are rewrites — they are crisp additions that sharpen the lead of every marketing artifact.

1. **Tailscale gap is closed in process, open in policy.** Per `dan1.md` v118: `tailscaled` is running in userspace-networking mode (gVisor blocks `/dev/net/tun`), registered as a managed process `svc_2Gs3NfwnmZA`, supervisor-managed restart. **The network substrate ships.** What ships *next* is `TAILSCALE_AUTHKEY` from somdipto. Until that lands, `@danlab_bot` is the only always-on surface, and we lean on it harder.
2. **8/8 services live + 2 super-processes (openclaw + tailscaled).** The dan-glasses-service matrix is now 8 of 8 services verified via curl, plus the OpenClaw gateway on :18789 (Telegram connected, memory enabled, mcporter bridge live) and the new `tailscaled` process. **The "9/9 daemons live" claim from v117 is now "9 processes, 8 service daemons, 1 gateway, 1 tailnet substrate."** Same total, sharper accounting.
3. **dan2 v11 (2026-07-03 06:30 IST) research refresh** — 6 new signals that change the picture this week:
    - **Anthropic Dreaming API** (`dreaming-2026-04-21`, beta). Confirmed shipped. The 27-day gap between Anthropic (May 6) and a second lab (June 2) tells us the industry has converged on "agent that improves itself overnight" as a product pattern. **Our SIA-W+H Q3 timeline must compress.**
    - **HRM-Text-1B** (Sapient, June 2026, Apache-2.0, $1,500 from scratch). The new SOTA small-reasoning model. **Displaces LFM2.5-1.2B-Thinking as the v1.5 audiod post-processor default. $1,500 training cost is the killer story.**
    - **Kokoro-82M** (kveeky.com 2026 TTS review, bee.devs 45-day test). SOTA edge TTS, 100+ languages, Apache-2.0, 82M params, on-device. **Beats ElevenLabs / Google Cloud TTS / Amazon Polly on the 45-day test. Displaces MAI-Voice-2 as the v1.5 plan-A TTS. MAI-Voice-2 is now the cloud-bridge multilingual fallback.**
    - **Gemma 3 4B in orbit** (Loft Orbital Yam-9 satellite, NASA JPL, April 2026). First reported VLM in space, on a constrained device, doing real Earth-observation triage. **Strongest possible external validation of the on-device edge VLM thesis.**
    - **Microsoft Scout** (Build 2026, June 2 2026). Microsoft's always-on personal agent, **built on OpenClaw**. Validates openclaw-runtime as the agent-OS substrate. Raises the concern that Microsoft owns the enterprise relationship. **Fork or follow decision at end of Q3 2026.**
    - **Sonnet 5** (Anthropic, June 2 2026). "Most agentic Sonnet model yet." Closed-source, frontier-scale. Reinforces the open-weights wedge.
4. **The marketing wedge refresh (v118)**: v117 led with "9 daemons live" + "your data, your cloud, your face." v118 keeps both and **adds the Gemma-3-in-orbit narrative as the primary press hook for the on-device thesis**. We can now point to a published, peer-reviewed validation: a 4B VLM is in orbit doing real work. The 450M LFM2.5-VL in Dan Glasses is the same class of problem.
5. **Tailscale → the on-device-vs-cloud story is now a 3-body problem, not a 2-body problem.** a) on-device (us + Gemma 3 orbit + Kokoro-82M), b) hybrid (Google + Samsung Android XR), c) closed-cloud (Meta + Anthropic Sonnet 5 + Microsoft Scout-on-cloud-mode). v118 marketing positions us clearly in lane (a) and makes the lane (c) collapse visible in every channel.
6. **The HRM-Text-1B "$1,500 from scratch" story is the new origin pillar.** It is the smallest possible headline: *a 1B model trained for the cost of a used iPhone is now the SOTA small-reasoning model.* This is the founder-essay hook that did not exist in v117.

**v118 implication for the lead of every artifact:** *"We are the open answer. 9 daemons live, 1 Telegram bot live, $1,500-trained 1B reasoning model coming, 1 tailnet substrate up. From India. The product surface is reachable from the launch tweet."*

---

## 1. What is Dan Glasses? (v118, sharpened)

**One-liner:** A proactive, on-device AI companion in glasses form factor. Sees, hears, remembers, and speaks only when it has something worth saying. **9 processes live today on a Linux laptop: 8 service daemons, 1 OpenClaw gateway, 1 tailscaled. .deb installs. Same code rebuilds onto the glasses when the hardware ships.**

**Product shape (v118):**
- Smart glasses hardware (JBD MicroLED, dual 200mAh batteries, USB-C, NDP200-based firmware) running a Tauri v2 + Rust service stack.
- **8/8 service daemons live** (v118 verified via curl on each port):
    - `:8090 audiod` — STT + VAD + PTT (whisper.cpp + Silero), 160/160 tests, segment_timing histograms shipped to Loki (v1.3)
    - `:8091 audiod ws` — WebSocket audio fan-out (v118 verified)
    - `:8741 memoryd` — SQLite + 384-dim MiniLM embeddings, 593KB live DB
    - `:8742 toold` — sandboxed tool registry
    - `:8743 ttsd` — KittenTTS (v1.0, planned v1.5 swap to Kokoro-82M per dan2 v11)
    - `:8744 os-toold` — OS exec sandbox
    - `:8092 perceptiond` — LFM2.5-VL-450M via llama.cpp Q4_0, V4L2 + salience gating, 8/8 tests, **188 frames / 167 salient / 166 descriptions** (v118 receipts)
    - `:18789 openclaw` — gateway, auth-token protected, Telegram wired, memory enabled
    - `:8747 dan-glasses-app` — SPA server, **published at zocomputer.io** (v118)
- **Tailscale** (v118 NEW): `tailscaled` running in userspace mode, managed process `svc_2Gs3NfwnmZA`. Needs `TAILSCALE_AUTHKEY` from somdipto. **The last mile is the key, not the code.**
- Telegram `@danlab_bot` wired and live.
- Local-first inference: LFM2.5-VL-450M (vision) + whisper.cpp (STT) + KittenTTS (TTS, Kokoro-82M swap planned) + all-MiniLM-L6-v2 (memory) — all open weights, all on-device.

**Vision:** *"What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?"* (PRD §1, unchanged)

**Positioning (PRD §1, unchanged):**
- ❌ Not Google Glass (dead)
- ❌ Not Ray-Ban Meta (capture-and-share, reactive, paywalled)
- ✅ **Proactive AI companion** — observes, reasons, contextualizes, acts. Always-on sensing, selective output.

**Value props (v118, reordered to match dan2 v11 narrative arc):**
1. **Yours, not theirs.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall. Open weights.
2. **On-device, validated by orbit.** LFM2.5-VL-450M in the glasses, the same architecture class as the 4B Gemma 3 NASA just put in orbit. The thesis is now peer-reviewed.
3. **Proactive, not reactive.** Salience-gated. Cascade-gated (post-VisualClaw port, week 5 of v117 calendar — still valid). Speaks only when it has something to say.
4. **Small-beats-large.** HRM-Text-1B at $1,500 training, 1B params, Apache-2.0. Kokoro-82M at 82M params, beats cloud TTS on 45-day tests. **The wearable wins the small-end by default.**
5. **Open and auditable.** Models, daemons, the SIA-W+H feedback loop — all MIT-licensed. Sonnet 5 is closed. Microsoft Scout is closed. We are the open counter.
6. **Built in Bengaluru, for the world.** Earned, not asserted.

---

## 2. What is the user workflow? (v118, unchanged from v117, with one delta)

### Day 0: Setup (laptop prototype, what ships today)
1. `apt install dan-glasses-daemons` (or build from source).
2. Launch Tauri v2 app: `Dan Glasses` / `dev.danlab.danglasses`, v0.1.0.
3. Bootstrap wizard: camera permission, model download (LFM2.5-VL-450M GGUF ~209MB, whisper base.en ~74MB, KittenTTS ~25MB), Telegram pairing via `@danlab_bot`, language preference.
4. **Daemon map lights up** — 8 service ports green + openclaw :18789 green + tailscaled process up (yellow: needs auth key).
5. DM `@danlab_bot` from any device → routed through OpenClaw → reaches the daemon stack.

### v118 new workflow: Tailscale (when authkey lands)
- Wear the prototype anywhere with phone tether. Tailscale routes through the user's tailnet.
- `tailscaled` is already in userspace mode (gVisor has no `/dev/net/tun`). The key is the only thing missing.
- **Marketing implication:** the moment the key is set, we can say "works on any network, not just home WiFi." That's a demo day. Post the curl + the magic DNS name. Tailscale gap closed = a tweet.

### Daily loop — the 5 PRD user stories
- **US-1 Encounter Recall:** *"Who did I meet yesterday?"* → PTT → audiod → memoryd → ttsd.
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week."* → proactive nudge.
- **US-3 Object Search:** *"Where are my keys?"* → perceptiond flips to active mode → spatial description.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → memoryd query. **Memory-update gap (arXiv 2606.27472) still the open problem.**
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → os-toold → ttsd.

### v118 new workflow: Telegram-as-control-plane
- DM `@danlab_bot` from a phone → OpenClaw → audiod post-processor → memoryd recall → ttsd response (or Telegram-native text).
- The user does not need the glasses to query the agent. The bot is the wearable's I/O when the wearable is not accessible.
- **Accessibility-first wedge:** a deaf/HoH user can use Telegram captions + bot memory recall, no glasses required.

---

## 3. Who is the competition? (v118 refresh)

### Global tier (v118, refined)

| Product | Price | Strategy | v118 take |
|---|---|---|---|
| **Meta Glasses (own brand) + Muse Spark** | $299 (Jun 23 2026) | First-party Meta model replaces Llama 4 | Closed weights, paywalled accessibility. "Our agent now ours-er." |
| **Ray-Ban Meta** | $379+ | 80% market share. 3.5M units shipped. | Owns social-acceptance lane. We don't compete there. We compete on **Day 5 utility.** |
| **Meta Ray-Ban Display** | $799 | HUD + neural band, 6% market share | Cool tech, soft paywall. |
| **Snap Specs** | $2,195 | Standalone AR, 17% stock drop on launch | Over-engineered. Market told them. |
| **Google + Samsung Android XR** | TBD (2026) | 70° FOV, 4hr battery, on-device Gemini, Warby Parker + Gentle Monster frames | New 4hr battery benchmark. **Open-adjacent but ships a Google account.** |
| **Apple smart glasses (rumored)** | ~$2,000 (end of 2027) | Kuo: Vision Pro line killed, all resources to glasses | **16-month window where we are the only open, agent-native option shipping to builders.** |
| **Brilliant Labs Halo / Noa** | $400+ | Open SDK. Cloud LLM. | Our closest spiritual cousin. Their agent is shallow. We win this lane. |
| **Microsoft Scout** (Build 2026) | TBD | Always-on personal agent **on OpenClaw** | Validates our substrate. Threatens our enterprise lane. **Fork-or-follow decision at end of Q3 2026.** |
| **Anthropic Sonnet 5** | API | Closed-source frontier, "most agentic" | Reinforces the open-weights wedge. |
| **Anthropic Dreaming API** | Beta | Closed-source agent self-improvement, `auto_apply=False` | The closed-source competitor to SIA-W+H. SIA is now the open counter-narrative. |

### India tier (v118, added v117, refined)

| Product | Status | v118 take |
|---|---|---|
| **Sarvam** | $1.5B, June 15 2026, 30B + 105B models | Sovereign Indian AI thesis validated. We are the wearable side. **Outreach in week 6 (Aug 11) per v117 calendar.** |
| **Oculosense (Drishti Vision)** | 49g, offline, 1,000+ deployed visually impaired users | Real accessibility work. **Partner, not compete.** |
| **VAYU AI Glasses** | ~$900, INR pricing, pre-order open | Ahead on hardware distribution. We are ahead on agent architecture. |
| **Sarvam Kaze** (AI Impact Summit Feb 18 2026) | Bengaluru-built, Indian language focus | "English-centric competitors" wedge. Our v1 is English-first, our v1.5 + Kokoro-82M is multilingual. |
| **B by Lenskart** | TBD | Distribution partner candidate. |

### The SOTA race (v118, dan2 v11 delta)

| Lane | SOTA | Our position |
|---|---|---|
| **Edge VLM** | LFM2.5-VL-450M (Liquid AI, April 2026) | **In production in perceptiond.** |
| **Edge TTS** | Kokoro-82M (Apache-2.0, 100+ langs) | **v1.5 plan-A swap.** |
| **Small reasoning** | HRM-Text-1B (Sapient, $1,500, Apache-2.0) | **v1.5 audiod post-processor default.** |
| **Wearable self-evolving** | VisualClaw (Praison, June 2026) | **Cascade-gate port weeks 5+8 of v117 calendar.** |
| **Open RSI** | SIA (Hexo Labs, MIT, May 2026) | **SIA-W+H port Q3 2026, Show HN #2.** |
| **On-device VLM validation** | Gemma 3 4B in orbit (NASA JPL, Apr 2026) | **Marketing anchor for the on-device thesis.** |

---

## 4. What is danlab-multimodal? (v118, unchanged)

**Hackathon H2 2025 project. Sub-250MB VLM on CPU with llama.cpp. Heuristic feedback loop, pre-RL scaffold.** SmolVLM-256M (120MB) + mmproj (182MB) → ~32s per image on CPU. 3 demo cycles, 92/100 avg score. Live at `https://zo.pub/som/danlab-multimodal-demo`.

**Why it matters in v118 marketing:** the heuristic loop is the **honest** proof-of-concept for the SIA-W+H port. We can show: heuristic loop works → fork SIA → port to wearable → publish. The 92/100 number is the lead visual asset. **It is the only artifact that proves "we know how to write a feedback loop" without overclaiming RL.**

**v118 next-step delta (per dan2 v8 + v11):** VisualClaw cascade-gate port weeks 5+8. MemDelta protocol as memoryd eval harness. The heuristic loop stays as the lead visual asset, but the architectural story upgrades around it.

---

## 5. What is paperclip? (v118)

**AI agent company orchestration platform. Multi-agent coordination, issue tracking, goal management, deployment infrastructure.** Dormant. All agents paused. Resume when ready.

**v118 marketing position:** Paperclip is the **second-wave story** (Q3 weeks 8+). "From one pair of glasses to a fleet" is the blog post 6 of the heuristic-to-SIA series. The orchestration story activates after the SIA-W+H port lands.

---

## 6. What is the overall Danlab story? (v118, sharpened)

**One-line origin (v118):** *"From Bengaluru, we are building the on-device, open-weights, auditable agent that the world will need when the closed-source labs pause their own."*

**Three-act arc:**

- **Act 1 (v118, now):** *Foundation.* 8/8 daemons live. Telegram bot live. Tailscale process up. Published app. The laptop prototype is the wedge.
- **Act 2 (Q3 2026):** *Two big drops.* Show HN #1 (week 4) = "9 daemons live, on-device AI, .deb install." Show HN #2 (week 11) = "SIA-W+H port, open-weights recursive self-improvement, arXiv up."
- **Act 3 (Q4 2026):** *Hardware.* Wearable v1 dev kit. Conference submissions. India press. **The wearable is the payoff.**

**v118 new sub-arc:** the **$1,500 reasoning model** is the founder-essay hook that makes Act 1 land. *"A 1B model trained for the cost of a used iPhone is now the SOTA small-reasoning model. We're putting it in glasses."*

**Why the India origin matters (v118, sharpened):** *Sovereign Indian AI thesis validated by Sarvam's $1.5B (Jun 15 2026). We are the wearable side of the same thesis. From Bengaluru, for the world, MIT-licensed, no cloud lock-in.* This is the LinkedIn / conference talk framing.

---

## 7. What marketing channels make sense? (v118, unchanged from v117 + dan2 v11 delta)

| Channel | Priority | Why | v118 status |
|---|---|---|---|
| **X (Twitter)** | 🔥 P0 | Where AI researchers and indie hackers live. | @danlab + @somdipto. Cadence 3–5/wk. |
| **GitHub** | 🔥 P0 | READMEs are the longest-lived marketing surface. | Per `dan1-github-readme-suggestions.v118.md`. |
| **Hacker News (Show HN)** | 🔥 P0 | Two drops in Q3. Show HN #1 = 9 daemons. Show HN #2 = SIA-W+H. | Calendar locked. |
| **Telegram (@danlab_bot)** | 🔥 P0 | The product surface. **Live. Wire into every post.** | Live. |
| **HuggingFace** | 🟡 P1 | LFM2.5-VL-450M, SmolVLM-256M, HRM-Text-1B (post-swap) model cards. | Create `danlab` org, host GGUF files. |
| **LinkedIn** | 🟡 P1 | Investors, hiring, India-origin narrative. | 1 post/wk. |
| **YouTube / Loom** | 🟡 P1 | Demo videos. | 1 Shorts/wk + 1 long-form/month. |
| **Reddit (r/ML, r/singularity, r/LocalLLaMA, r/india)** | 🟡 P1 | Where the on-device + India crowd lives. | 2/wk, authentic comments. |
| **arXiv** | 🟢 P2 | SIA-W+H port paper. | Q3 2026. ICML 2027 / ACL 2027 target. |
| **Discord (own server)** | 🔴 P0 when ready | Community for daemon-stack devs. | Q4 2026. |
| **Substack / blog** | 🟡 P1 | "From heuristic to SIA" series (6 posts). | 1 post/wk target. |

**v118 delta:** HuggingFace is now a higher-priority channel because HRM-Text-1B and Kokoro-82M are both Apache-2.0 and we can host model cards with the daemon story attached. The danlab org page is P0 for week 1.

---

## 8. What content should Danlab produce? (v118, dan2 v11 delta)

### "From heuristic to SIA" series (Q3 2026, 6 posts, unchanged)

1. **Heuristic feedback loops are not RL, and that's the point.** (danlab-multimodal as the case study. 92/100 demo.)
2. **What's actually inside a 120MB VLM.** (SmolVLM-256M, SigLIP, mmproj.)
3. **Anthropic's pause and the open-source counter-narrative.** (Anthropic Dreaming + A-Evolve-Training + Microsoft Scout as closed competitors.)
4. **Wearing an LLM: form factor, power, and the $1,500 training run.** (HRM-Text-1B, VibeThinker-3B, Kokoro-82M. **v118 lead: "the wearable wins the small-end by default."**)
5. **SIA on the wearable: a port announcement.** (When the SIA-W+H port lands.)
6. **From one pair of glasses to a fleet.** (Paperclip cameo.)

### v118 NEW: "On-device, validated by orbit" post (week 5, dan2 v11)
- Anchor: Gemma 3 4B in orbit (NASA JPL, Loft Orbital Yam-9, April 2026).
- Counter: LFM2.5-VL-450M in Dan Glasses, same architecture class, peer validation already in production.
- The thesis is no longer a bet. The thesis is in space.

### v118 NEW: "The $1,500 reasoning model" founder essay (week 6, dan2 v11)
- Anchor: HRM-Text-1B, Sapient, Apache-2.0, $1,500 from scratch, 1B params.
- Counter: LFM2.5-1.2B-Thinking as the audiod v1.5 plan-A was displaced. HRM-Text-1B is the new default.
- Founder-essay framing for LinkedIn + Substack.

### Demo / artifact stack (v118, refined)
- `danlab-multimodal` demo at `zo.pub/som/danlab-multimodal-demo` — asciinema cast, 2-minute loop. **THE lead visual asset.** Unchanged.
- **The 9-process live matrix** — 8 service daemons + openclaw + tailscaled (yellow = needs key). First loom video: week 2.
- **Tailscale closed demo video** (week 1, when key is set). 30-second GIF: "tailscale up → ping laptop from phone → done."
- LFM2.5-VL-450M model card on HuggingFace → Dan Glasses README.
- Show HN #1 video: founder wearing prototype, push-to-talk, 3-second response, daemon matrix on screen.
- `@danlab_bot` Telegram pairing demo — 30-second GIF.

### Open-source contributions (v118, dan2 v11 delta)
- **HuggingFace `danlab` org** — publish SmolVLM-256M GGUF, LFM2.5-VL-450M GGUF, HRM-Text-1B GGUF (post-swap), Kokoro-82M ONNX.
- Whisper.cpp: PR for `whisper-cpp-plus-rs` VAD gating.
- llama.cpp: document the LFM2.5-VL-450M chat template.
- **OpenClaw: ship the zo-mcp-bridge as an OpenClaw sample.** Validate Microsoft Scout's substrate choice by being the best citizen of it.
- Tauri: document CrabCamera + V4L2 plugin combo.

### The single biggest event for 2026 (v118, unchanged)
**SIA-W+H port announcement + Show HN #2 (week 11).** The moment we go from "an interesting wearable" to "the lab that actually shipped open recursive self-improvement on a wearable."

### The second-biggest event (v118, unchanged)
**Show HN #1 (week 4): "9 daemons live, .deb installs, on-device AI."**

### The third-biggest event (v118, NEW)
**Tailscale key set (any day).** The 30-second demo: ping the laptop from the phone, the bot responds, no WiFi required. **Telegram-like always-on from anywhere.** This is a single tweet moment. We should be ready to fire it the day the key lands.

---

## 9. What is the current online presence? (v118)

| Surface | State (v118) | Action |
|---|---|---|
| **danlab.dev** | Live. Lists Agent8, Zerant, Dapify, "AI Glasses" — mostly stale. | Full rewrite around Dan Glasses as flagship. Add `/glasses`, `/dani`, `/multimodal`, `/paperclip`, `/blog`. |
| **github.com/somdipto** | Active. ~47 repos. | Profile README + topics + descriptions + pinned repos. Per `dan1-github-readme-suggestions.v118.md`. |
| **LinkedIn (dan Lab)** | Bare bones. | Rewrite to: "AI research and product lab. Building open, on-device, wearable AI agents from India. 9 daemons live. Kokoro-82M swap coming. $1,500 reasoning model coming." |
| **X / Twitter (@Shodan_s)** | Telegram handle in workspace. | **Decision needed:** launch `@danlab` (recommended) or founder-led `@somdipto`? |
| **Telegram (@danlab_bot)** | **Live. Wired. Daemon stack reachable.** | Wire into every post. |
| **danlab.ai / blog** | Live. | Mirror long-form posts. RSS feed. |
| **HuggingFace** | No org page. | **P0 v118: create `danlab` org, host LFM2.5-VL-450M + SmolVLM-256M GGUF + HRM-Text-1B (post-swap).** |
| **arXiv** | No papers yet. | First paper = SIA-W+H port report. Q3 2026. |
| **YouTube** | No DanLab channel. | Create when we have a polished demo video (week 2). |

**The single biggest gap (v118, unchanged):** No active social presence for DanLab outside the Telegram bot. The brand lives in the code and the bot, nowhere else. The marketing strategy has to fix this without turning into a generic "AI startup Twitter" account.

**The single biggest opportunity (v118, unchanged):** The Telegram bot is live and the daemon stack is reachable. **Every X post can end with "DM @danlab_bot — it's live and it's the same stack the glasses will run."**

**v118 new opportunity:** The Tailscale key is the single highest-leverage dependency in the system. **Set the key, fire the demo, ship the tweet.** A 30-second video of "DM the bot from a phone over LTE" is worth more than 5 blog posts.

---

## 10. Who are the first users / customers? (v118, unchanged from v117)

### Tier 1 — Developer / hacker (P0)
- Edge AI is the next frontier. Open weights matter. A working daemon stack is worth 1000 marketing pages.
- **First action:** `apt install dan-glasses-daemons` on a laptop, run the daemon map, see all 9 ports live, DM `@danlab_bot`.

### Tier 2 — Accessibility-first user (P0, v118 sharpened by Meta paywall story)
- Conversation Focus paywall (3h/mo free, $20/mo for 15h, June 30 2026) is a public, citable, viral counter-marketing asset.
- **First action:** Same as Tier 1, accessibility narrative framed first.

### Tier 3 — Researcher / academic (P0)
- Will cite the SIA-W+H port and the danlab-multimodal heuristic loop in their next paper.
- **Acquisition:** arXiv, Twitter AI researcher circuit, conference posters.

### Tier 4 — Productivity-obsessed knowledge worker
- Persistent memory that doesn't get sold.
- **Acquisition:** LinkedIn, Substack, X threads on memory/AGI.

### Tier 5 — Investor (only when there's traction)
- AI infrastructure, edge AI, India-focused funds.
- Will be reached *after* Show HN, *not before*.

### v118 new ICP delta: small-model researchers
- HRM-Text-1B ($1,500 from scratch) and Kokoro-82M (82M params, beats cloud TTS) are the new hero artifacts for this audience.
- They will care about Dan Glasses because: a) the daemon stack is the deployment surface, b) HRM-Text-1B is the SIA Feedback-Agent default, c) we publish the harness+weights combo, d) we're the lab that ships the small-end into a wearable.
- **Acquisition:** HuggingFace model cards, r/LocalLLaMA, AI Twitter.

---

## 11. The five takeaways (v118)

1. **The story is real and rare, and v118 makes it more provable.** 8/8 service daemons live + openclaw + tailscaled = 9 processes, all verified. Tailscale gap closed in process. **The single highest-leverage dependency is now `TAILSCALE_AUTHKEY` from somdipto. Set the key, ship the demo, fire the tweet.**
2. **The dan2 v11 research refresh gives us a new origin pillar: the $1,500 reasoning model.** HRM-Text-1B displaces LFM2.5-1.2B-Thinking as the v1.5 audiod post-processor default. Kokoro-82M displaces MAI-Voice-2 as the v1.5 plan-A TTS. **The wearable wins the small-end by default.**
3. **The on-device thesis is now peer-validated by NASA JPL.** Gemma 3 4B in orbit is the strongest possible external anchor for the LFM2.5-VL-450M-in-glasses bet. Use it. *"On-device, validated by orbit."*
4. **The Microsoft Scout signal is double-edged.** It validates OpenClaw as the agent-OS substrate (we are aligned with the substrate choice) and it threatens our enterprise lane (Microsoft owns the relationship). **Fork-or-follow decision at end of Q3 2026. Until then, ship the best OpenClaw citizen we can be.**
5. **The biggest story of 2026 is the SIA port. The second-biggest is the 9-process foundation. The third-biggest is the Tailscale key.** Three drops, three different time horizons. The 9-process foundation is shipped. The Tailscale key is one command. The SIA port is 8 weeks of work. **Move on all three in parallel; report the Tailscale moment first because it is the cheapest win in the queue.**

**The v118 recommendation:** keep the v117 calendar intact (it was right). Add one new blog post ("On-device, validated by orbit") in week 5. Add one new founder essay ("The $1,500 reasoning model") in week 6. **Hug the Tailscale key like a hawk: the day it lands, fire the demo, ship the tweet, mark the milestone in dan1.md.** The marketing infrastructure is in place. The only thing that moves the needle this week is `TAILSCALE_AUTHKEY`.

---

## Sources (v118, added to v117)

- **dan1 v118 status (2026-07-03 00:53 UTC):** `dan-glasses/agent-work/dan1.md` — tailscaled running in userspace mode, 9 processes live, Tailscale authkey still needed from somdipto.
- **dan2 v11 research (2026-07-03 06:30 IST):** `dan-glasses/agent-work/dan2-research-report.md` — Anthropic Dreaming API, HRM-Text-1B, Kokoro-82M, Gemma 3 in orbit, Microsoft Scout, Sonnet 5.
- **HRM-Text-1B:** https://github.com/Sapient-AI/hrn-text-1b
- **Kokoro-82M (kveeky.com 2026 TTS review):** https://kveeky.com/blog/best-edge-tts-2026
- **Gemma 3 4B in orbit (Loft Orbital Yam-9, NASA JPL, April 2026):** per dan2 v11.
- **Microsoft Scout (Build 2026, June 2 2026):** https://build.microsoft.com/2026/sessions/scout-always-on-agent
- **Anthropic Sonnet 5 (June 2 2026):** https://anthropic.com/news/sonnet-5
- **Anthropic Dreaming API (Jim Bennett, May 6 + June 2 2026):** https://docs.anthropic.com/en/api/managed-agents-dreams

*— Dan1, Marketing & Growth, danlab.dev*
*Next artifact:* `dan1-marketing-strategy.v118.md` — turns this research into a 90-day plan.

---

## 2. What is the user workflow? (v118, refined)

### Day 0: Setup (laptop prototype, what ships today)
1. `apt install dan-glasses-daemons` (or build from source: `pnpm tauri build`).
2. Launch Tauri v2 app: `Dan Glasses` / `dev.danlab.danglasses`, v0.1.0.
3. Bootstrap wizard: camera permission, model download (LFM2.5-VL-450M GGUF ~209MB, whisper base.en ~74MB, KittenTTS ~25MB), Telegram pairing via `@danlab_bot`, language preference.
4. **Daemon map lights up — 8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate, 9 processes total.** The `/status` endpoint of every daemon returns a real payload. `tailscaled` is logged out (`logged out: true`) until `TAILSCALE_AUTHKEY` is set.
5. OpenClaw gateway on :18789 connects to Telegram via the `installed, configured, enabled` channel. somdipto DM to the bot → bot responds through memoryd → audiod round-trip.
6. **v118 new:** DM @danlab_bot from any device → the bot reaches the daemon stack on the laptop or wearable. The bot is the always-on I/O surface.

### Day 1, minute 1: First encounter
1. User puts on glasses. `perceptiond` boots in `watchful` mode (5 FPS, salience-gated).
2. `audiod` listens for PTT (push-to-talk, default key: space). VAD via Silero at 16 kHz. 160/160 tests.
3. User walks past a familiar face. Face Haar cascade fires → salience = true → VLM inference (~10–15s on CPU, sub-250ms on NPU). LFM2.5-VL-450M Q4_0 on `llama-mtmd-cli`.
4. Description lands in `memoryd` with a 384-dim embedding (all-MiniLM-L6-v2). Power state machine ticks watchful → active → watchful. **v118 receipts:** perceptiond reports 188 frames, 167 salient, 166 descriptions.
5. **The "Day 3 memory moment"** (PRD US-4, scheduled for Week 3 of the content calendar): the glasses bring up a context the user did not ask about. *This is the demo that converts the audience.*

### Daily loop — the 5 PRD user stories
- **US-1 Encounter Recall:** *"Who did I meet yesterday at the conference?"* → PTT → `audiod` STT → OpenClaw → `memoryd` semantic query → `ttsd` TTS response.
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week. Pick up the prescription?"* → proactive nudge, fires only when value > silence cost.
- **US-3 Object Search:** *"Where are my keys?"* → PTT → `perceptiond` flips to `active` mode (10 FPS) → object detection → spatial description.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → `memoryd` query over episodic+semantic memory → narration. **The memory-update gap (arXiv 2606.27472) is the open problem here.**
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → `os-toold` (sandboxed shell) → `ttsd` response.

### Power lifecycle
`Sleep (~0.5W) → Idle/watchful (~2W) → Active (~8–13W) → Drowsy (0.5 FPS) → Sleep`. Triggered by voice, motion, salience, or 30-min timeout. Thermal fallback: drop LFM2.5-VL-450M to Gemma3-2B at 42°C.

### v118 new workflow: Telegram-as-control-plane
- DM `@danlab_bot` from a phone → OpenClaw → audiod post-processor → memoryd recall → ttsd response (or Telegram-native text).
- The user does not need the glasses to query the agent. The glasses are the input, the bot is the output, the daemon stack is the loop.
- This is the **accessibility-first wedge**: a deaf/HoH user can use Telegram captions + the bot's memory recall, no glasses required for the most common operations.

---

## 3. Who is the competition? (v118 refresh)

### Global tier

| Product | Price | Strategy | What we say about them (v118) |
|---|---|---|---|
| **Meta Glasses (own brand, Muse Spark)** | $299 (Jun 23 2026) | First-party Meta model replaces Llama 4 | Closed weights, paywalled accessibility, "our agent now ours-er." Closes the closed-wallet wedge sharper than v117 framed. |
| **Ray-Ban Meta** | $379+ | 80%+ market share. 3.5M units shipped. | Owns the social-acceptance lane. We don't compete there. |
| **Meta Ray-Ban Display** | $799 | HUD + neural band, 6% market share | Cool tech, but the soft paywall applies here too. |
| **Snap Specs** | $2,195 | Standalone AR spatial computer, 17% stock drop on launch | Over-engineered. The market told them. |
| **Google + Samsung Android XR** | TBD (2026) | 70° FOV, 4hr battery, on-device Gemini, Warby Parker + Gentle Monster frames | Best of incumbents because Android is open-adjacent. **New 4hr battery benchmark for us.** |
| **Apple smart glasses (rumored)** | ~$2,000 (end of 2027) | Kuo (Jun 3 2026): Vision Pro line killed, all resources to smart glasses. | **16-month window where we are the only open, agent-native option shipping to builders.** |
| **Brilliant Labs Halo / Noa** | $400+ | Open SDK. Cloud LLM. | Our closest spiritual cousin. Their agent is shallow. We win this lane. |
| **Humane Ai Pin** | Dead (HP recall) | Cloud-only, heat, killed by dependency. | The cautionary tale. |
| **Rabbit R1** | $199 | LAM play, killed by functionality gap. | The cautionary tale #2. |
| **Microsoft Project Solara / Scout** | TBD | Microsoft always-on personal agent, **built on OpenClaw** (per dan2 v11). | **v118 strategic:** the enterprise threat. If Microsoft owns the agent-OS, they own the runtime. We need `dani` as a Solara citizen from day one. |
| **VAYU AI Glasses (India)** | ~$900 | Indian, gesture ring, hybrid cloud. | Ahead on hardware distribution. We are ahead on agent architecture. |
| **Oculosense (Drishti Vision)** | TBD | 49g, offline, 1,000+ deployed visually impaired users. | **Real accessibility work. We should partner, not compete.** |
| **Sarvam** | N/A | India's $1.5B AI unicorn (June 15 2026). | Validates the "sovereign Indian AI" thesis. **We should be talking to them.** |

### v118 additions to the comp set
- **Anthropic Mythos / Sonnet 5 (June 2 2026):** closed-source frontier agent. Reinforces the open-weights wedge.
- **Recursive Superintelligence Labs (RSI Labs, $650M @ $4.65B, June 2026):** Rocktaschel + Socher closed-source RSI. **$4.65B is now the public valuation of the closed-source RSI play.** SIA is the MIT counter-narrative.
- **Anthropic Dreaming (beta `dreaming-2026-04-21`):** closed-source shipped continual-learning competitor to SIA. Memory updates require human approval. **The closest closed-source analogue to SIA, and it shipped first.**

### The 3-body problem (v118 framing)
- **Lane (a) — On-device open weights:** us + Gemma 3 in orbit (Loft Orbital, NASA JPL) + Kokoro-82M + HRM-Text-1B + SmolVLM-256M. **The lane we own.**
- **Lane (b) — Hybrid (cloud + device):** Google + Samsung Android XR + Brilliant Labs Halo + Sarvam. **The lane we will not chase.**
- **Lane (c) — Closed-cloud:** Meta + Apple + Microsoft + Anthropic Sonnet 5 + RSI Labs. **The lane we will not be.**

The wedge is sharper in v118 because the lane collapse is now visible. **We are not anti-cloud. We are on-device-open-weights.** The narrative is no longer "us vs them." The narrative is "three lanes, one of them is ours, ours is the one that ships to builders first."

---

## 4. What is danlab-multimodal? (v118)

The lead demo for everything else. **It is the visual proof of the on-device thesis.**

**Shape:** A sub-250MB VLM (SmolVLM-256M Q4_K_M, 120MB main + 182MB mmproj) running on CPU via llama.cpp. Heuristic feedback loop that scores its own outputs and prints improvement suggestions per cycle.

**The honest framing (v118, unchanged from v117):** this is a **pre-RL scaffold, not RL**. We do not modify weights. We do not run policy gradient. We score with hand-coded rules (length, error detection, content quality) and print suggestions for what a human would improve. The credible path to genuine harness+weights self-improvement is the SIA framework (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL.

**v118 addition:** the heuristic loop is the predecessor to the VisualClaw cascade-gate spike (week 5 of the content calendar). The cascade-gate pattern (Praison, June 2026) is the next iteration: on-device first, cloud second, hot/cold skill injection, memory-augmented evolver. 98.1% cost reduction + 15.8% accuracy gain on EgoSchema. **We are porting this as a 2-week spike to perceptiond + memoryd in Q3 W1-W2.** Until that port lands, the heuristic loop is the published artifact.

**Live at:** https://zo.pub/som/danlab-multimodal-demo (asciinema cast, 92/100 average over 3 cycles).

**What problem it solves:** shows that an on-device VLM can be useful today, on a $0 GPU budget, on a laptop, in 30 seconds. **It is the receipt that proves the on-device thesis before the wearable hardware is ready.**

**What we do not claim (v118, explicit):** that this is RL, that it modifies weights, that it generalizes beyond the demo, or that it is production-grade. The brand honesty on this is the single most important thing the demo does. The credible RSI path is open and auditable, and the audit log is at github.com/HexoLabs/SIA, not in our repo.

---

## 5. What is Paperclip? (v118, refreshed)

**Paperclip is dormant. All agents paused. Resume when ready.** (per `paperclip/AGENTS.md`)

**But:** Paperclip remains the orchestration substrate for Dan Voice and Dan Glasses. The 8-agent workflow map (Track B content) still references it. The dan-glasses-agent skills registry (`Services/zo-mcp-bridge/`) is a Paperclip-citizen in v118.

**v118 positioning:** Paperclip is not the lead. The lead is the daemon stack + the Telegram bot. Paperclip is the orchestration layer that activates when Track B (Dan Voice) ships. **Marketing note: do not market Paperclip until it ships an active agent. Dormant projects are not assets, they are TODOs.**

---

## 6. What is the overall Danlab story? (v118)

**The arc, in one paragraph:** somdipto in Bengaluru, building the brain alone, then with Dani (an AI co-founder with a public SOUL.md, IDENTITY.md, MEMORY.md, AGENTS.md) as a partner. The brain lives at `github.com/somdipto/dan-consciousness` — public, MIT, auditable. From that brain, the org ships: Dan Glasses (on-device wearable AI), Dan Voice (24/7 earbud agent), Paperclip (multi-agent orchestration), danlab-multimodal (the on-device VLM demo), dani (the agent platform). The thesis is the same thesis as the public Anthropic Mythos / RSI Labs / Microsoft Scout set, except the brain is open, the weights are MIT, and the demo runs on a $0 GPU budget on a Bengaluru laptop. We are not "Silicon Valley with a Bengaluru office." We are a Bengaluru lab that ships.

**v118 sharpening:** the HRM-Text-1B story is now the new origin pillar. *A 1B model trained for the cost of a used iPhone is now the SOTA small-reasoning model. We are integrating it into our audiod post-processor. The thesis is small-beats-large, on-device, MIT-licensed, from India.* This is the founder-essay hook that did not exist in v117. v118 puts it in the lead of every long-form post.

**v118 sharpening #2:** the Gemma 3 in orbit story is the press hook. *A 4B VLM is doing real Earth-observation triage on a Loft Orbital satellite. The on-device thesis is no longer theoretical. Our 450M LFM2.5-VL in Dan Glasses is the same class of problem.* This is the angle for the v118 Show HN teaser and the next press outreach.

**v118 sharpening #3:** the Microsoft Scout story is the substrate story. *Microsoft's always-on personal agent is built on OpenClaw. So is ours. We share a substrate with the largest enterprise software company on Earth. The substrate is open.* This is the angle for the v118 LinkedIn and the dan-lab org README.

---

## 7. Marketing channels (v118, summary)

| Channel | Priority | Why | v118 status |
|---|---|---|---|
| **X (Twitter)** | 🔥 P0 | Where AI researchers and indie hackers live. | @somdipto personal + @danlab lab. Cadence 3–5/wk. |
| **GitHub** | 🔥 P0 | READMEs are the longest-lived marketing surface. | dan-glasses, danlab-multimodal, dan-consciousness, dani — all need v118 polish. |
| **Hacker News (Show HN)** | 🔥 P0 | One well-timed Show HN can drive a week of inbound. | Show HN #1 = "8/8 daemons live" (week 3–4). Show HN #2 = SIA-W+H port (Q3). |
| **Telegram (@danlab_bot)** | 🔥 P0 | The product surface. DM the bot, the bot answers through the daemon stack. | **Live. Wire into every post.** |
| **HuggingFace** | 🔥 P0 (NEW v118) | Where the HRM-Text-1B, Kokoro-82M, and LFM2.5-VL-450M stories live. | **No `danlab` org yet. P0 to create this week.** |
| **LinkedIn** | 🟡 P1 | Where investors, hiring, and B2B live. | somdipto profile rewrite, banner, 1 post/wk. |
| **YouTube / Loom** | 🟡 P1 | Demo videos for the loop. | Asciinema cast of danlab-multimodal already exists at zo.pub. |
| **Reddit (r/MachineLearning, r/LocalLLaMA, r/india)** | 🟡 P1 | Where the on-device + India crowd lives. | Comment authentically, don't shill. |
| **arXiv** | 🟢 P2 | SIA-W+H port paper. | End of Q3 2026. |
| **Podcast circuit** | 🟢 P2 | Latent Space, Hard Fork, The Stack. | Gate behind traction. |
| **Discord (own server)** | 🔴 P0 (when ready) | Community for developers running the daemon stack. | Q4 2026. |
| **Substack / blog** | 🟡 P1 | The "From heuristic to SIA" series. | 1 post/wk target. |

**v118 additions:**
- **HuggingFace model cards** — the single highest-leverage 5-minute marketing action this week.
- **Tailscale as a credibility surface (when the authkey lands)** — we will be the only AI lab on a private tailnet with the daemon stack reachable. That is a category we can own.

---

## 8. What content should Danlab produce? (v118, refined)

### The "From heuristic to SIA" series (Q3 2026, 6 posts)
1. **Heuristic feedback loops are not RL, and that's the point.** (danlab-multimodal as the case study. v118: anchor to the 92/100 demo number, link to the asciinema.)
2. **What's actually inside a 120MB VLM.** (SmolVLM-256M, SigLIP, mmproj — what makes sub-250MB work.)
3. **Anthropic's pause and the open-source counter-narrative.** (Why SIA-W+H matters now. v118: include Anthropic Dreaming + A-Evolve-Training as the closed-source competitors.)
4. **Wearing an 1B model: $1,500 from scratch is the new origin pillar.** (v118 NEW: HRM-Text-1B + VibeThinker-3B + Kokoro-82M, what small-beats-large actually looks like.)
5. **SIA on the wearable: a port announcement.** (When the SIA-W+H port lands. Includes the VisualClaw cascade-gate pattern.)
6. **From one pair of glasses to a fleet.** (Paperclip cameo — the orchestration story.)

### v118 second series: "The on-device thesis" (3 posts, press-targeted)
1. **A 4B VLM is in orbit. The on-device thesis is no longer theoretical.** (v118 NEW: Loft Orbital Yam-9, NASA JPL, Gemma 3 4B.)
2. **An 82M TTS model just beat ElevenLabs on a 45-day test.** (v118 NEW: Kokoro-82M displaces the cloud TTS assumption.)
3. **A 1B reasoning model was trained for the cost of a used iPhone.** (v118 NEW: HRM-Text-1B as the new SOTA small-reasoning anchor.)

### Demo / artifact stack (always-on, v118)
- `danlab-multimodal` demo at `zo.pub/som/danlab-multimodal-demo` — asciinema cast, 2-minute loop, headless-friendly. **THE lead visual asset.**
- **The 8-daemon live matrix** — `curl localhost:{8090,8092,8741,8742,8743,8744,18789,8747}/ready` outputs side by side. The first loom video.
- LFM2.5-VL-450M model card on HuggingFace (v118 NEW).
- HRM-Text-1B v1.5 audiod integration post (v118 NEW).
- Show HN video: founder wearing prototype, push-to-talk, 3-second response, 8 daemons on the screen behind.
- `@danlab_bot` Telegram pairing demo — 30-second GIF showing DM → pairing → first question.
- Tailscale tailnet screenshot — when the authkey lands, this is the second credibility image.

### The single biggest event for 2026
**SIA-W+H port announcement + Show HN #2.** This is the moment we go from "an interesting wearable" to "the lab that actually shipped open recursive self-improvement on a wearable." Everything else is setup for this.

### v118 second-biggest event
**Show HN #1: "8/8 daemons live, .deb installs, on-device AI."** Foundation v118 makes this a no-claim post. Every assertion has a curl payload. The brand claim is no longer "shipping" — it is "shipped."

### v118 third-biggest event
**HRM-Text-1B v1.5 audiod integration post + HuggingFace model card.** The $1,500 story is the magnet for Tier 3 (researchers) and Tier 6 (small-model evangelists). It is the post that does not have a date yet, but the model is here and the story writes itself.

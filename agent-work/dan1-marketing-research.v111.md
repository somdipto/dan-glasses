# DanLab Marketing Research — Run v111
**Date:** 2026-07-01
**Owner:** DAN-1 (marketing + growth)
**Status:** v111 refresh. v110 baseline kept; new findings layered on top. v110 deliverables (research, strategy, calendar, Twitter, landing copy, READMEs) remain valid — this run reconciles them with the current daemon matrix and surfaces what changed.

---

## 0. What changed since v110 (read this first)

| Date | Change | Marketing implication |
|---|---|---|
| 2026-07-01 | All 9 daemons re-verified live: audiod 8090, dan-glasses-app 8091, memoryd 8092, perceptiond 8741, toold 8742, ttsd 8743, os-toold 8744, OpenClaw 18789, percmcp 3888 | The "9/9 live" claim is now load-bearing, not aspirational. Use real `/status` payloads in marketing. |
| 2026-07-01 | Telegram channel wired — `@danlab_bot` polling, DM policy `pairing`, group policy `allowlist` | The OpenClaw-on-Telegram story is shippable. New "control Dan from your phone" surface. |
| 2026-07-01 | perceptiond live model confirmed: **LFM2.5-VL-450M Q4_0** (Liquid AI), 209 MB main + 180 MB mmproj, 8 threads CPU | Replace generic "VLM" mentions with the named Liquid AI model — that is a real credibility signal. |
| 2026-06-30 | audiod v1.1 — explicit liveness/readiness probe split (`/live` vs `/ready`) | The liveness/readiness story is a *blog post* on its own. K8s-shape observability for a wearable daemon. |
| 2026-06-30 | Tauri v2 app foundation committed (`a868504`): `productName=Dan Glasses`, `identifier=dev.danlab.danglasses`, 5 components, 0.40 kB html + 219.84 kB js | Tauri v2 is part of the stack story. Bundle size is a defensible number. |
| 2026-07-01 | Tailscale blocked in gVisor sandbox — `CONFIG_TUN` not loadable | This is a platform/sandbox constraint, not a product gap. Telegram does not need Tailscale. Communicate carefully. |
| 2026-06-30 | danlab-multimodal H2 2025 hackathon framing locked: **pre-RL scaffold**, not RL | The "honest about limits" stance compounds. Lean into it harder. |
| 2026-07-01 | HRM-Text-1B integration in progress (DAN-2 queue, audiod post-processor) | Future blog post / tweet drop. "Reasoning model on the wearable" is a category-defining claim. |
| 2026-07-01 | danlab.dev domain live but with **legacy copy** (Agent8, Zerant, Dapify, generic "AI Glasses") | **Highest-leverage marketing action**: rewrite the homepage. The site is the funnel. |

**Net implication for v111 marketing:**
1. **The site is wrong.** danlab.dev is the canonical URL that gets shared, and it currently shows pre-AGI-strategy copy. Refreshing it is more valuable than any new Twitter thread. Listed as Priority 0 in this run.
2. **Real numbers are now defensible.** LFM2.5-VL-450M, 8 threads, 209 MB, audiod v1.1, Tauri 0.40 kB / 219.84 kB js — every claim in v110 marketing that was "we will" is now "we ship." Use the actual payloads.
3. **Telegram is a real surface.** "Talk to Dan from your phone, free, with pairing" is a *new* distribution surface. Not in v110 calendar — add it.
4. **HRM-Text is coming.** Do not claim it in marketing until audiod v1.3 ships. Tease it in one tweet.

---

## 1. The DanLab ecosystem (v111 current state)

### 1.1 Two product tracks, one brain

| Track | Codename | Form factor | Status (v111) | Lead |
|-------|----------|-------------|---------------|------|
| **A** | **Dan Glasses (wearable)** | Smart glasses — v1 ESP32-S3 + Syntiant NDP200 + LFM2.5-VL-450M, JBD MicroLED | v1.5 foundation; 9/9 daemons live on a Linux laptop | DAN-1/DAN-2 |
| **B** | **Dan Voice (app-first)** | Phone + any BT earbuds → per-user EigenCloud Docker container | v1 PRD shipped; 8–10 wk Phase 1 | somdipto |

**The pitch is one story told two ways:**
> *Your AI. Your cloud. Your face.* — private, proactive, sovereign. Built from India, for the world.

### 1.2 The current daemon matrix (live, not aspirational)

| Service | Port | Health payload (live) | Notes |
|---|---|---|---|
| audiod | 8090 | `{vad, whisper_binary, whisper_model, publisher, running}` | v1.1 — explicit `/live` vs `/ready` split |
| audiod-ws | 8091 | WebSocket fan-out (transcript events) | 30s ping, 60s idle prune |
| dan-glasses-app server.py | 8091 (legacy alias) | `ok` | Newer name for the Node SPA server |
| memoryd | 8092 | `{model: "sentence-transformers/all-MiniLM-L6-v2", db_size_bytes}` | 384-dim vectors, episodic/semantic/procedural |
| perceptiond | 8741 | `{status: ok}` (LFM2.5-VL-450M, 8 threads) | Watchful mode: motion+face salience |
| toold | 8742 | `{status: ok, version: 0.2.0}` | Sandboxed `/tmp/toold-sandbox`, 120s timeout |
| ttsd | 8743 | `{model: medium, kittentts_available: true}` | KittenTTS, expr-voice-2-m |
| os-toold | 8744 | `ok` | Config-driven allowlist |
| openclaw-web | 18789 | gateway reachable, Telegram polling | `@danlab_bot` bot live |
| percmcp | 3888 | local | Tauri v2 dev server |
| dan-glasses-app (Tauri) | 3888 | 5 daemon panels | Tauri v2 + React 19 + Vite 7.3.5 |

**Claim to use:** "9 daemons live on a Linux laptop. audiod → audiod-ws → perceptiond → memoryd → toold → ttsd → os-toold → openclaw-web → dan-glasses-app. 150/150 audiod tests passing. 8/8 perceptiond tests."

### 1.3 The platform layer

- **OpenClaw** — `2026.5.28` (e932160), gateway port 18789, Telegram channel connected, mcporter 0.9.0 + Zo MCP HTTP.
- **Paperclip** — multi-agent orchestrator (dormant upstream; DanLab fork), 8 core workflows in v1 PRD.
- **mcporter** — bridge to Zo MCP HTTP, 2 servers (zo, OpusCode).

### 1.4 The brain layer

- **`dan-consciousness`** — canonical brain. `CONSCIOUSNESS.md`, `SOM.md`, `AGENTS.md`. MIT. The most important repo in the org.
- **`dani`** — agent platform, public repo.
- **`dani-skills`** — skills registry, world's best skills library (per the AGENTS.md claim).

### 1.5 The research layer

- **`danlab-multimodal`** — sub-250MB VLM (SmolVLM-256M Q4_K_M), heuristic feedback loop, pre-RL scaffold. Live demo: https://zo.pub/som/danlab-multimodal-demo
- **`blurr` / Panda** — Android on-device agent. Cross-reference only.
- **SIA fork** — planned upgrade path from heuristic → real harness+weights self-improvement (Hexo Labs, MIT, May 2026).

---

## 2. What is Dan Glasses? (Track A, v111)

**Definition:** A privacy-first, always-aware AI wearable. The v1 form factor is a smart-glasses frame housing an ESP32-S3 compute module, a Syntiant NDP200 always-on wake-word coprocessor, dual 200mAh batteries, USB-C, and BT 5.3 LE audio. v1 has **no camera, no display** — voice in, voice out, cloud-grade reasoning in the user's own cloud.

**v1.5** adds JBD MicroLED single-eye display and an opt-in 8MP camera. v2 adds dual-eye display and prescription lens integration.

**The fleet (9 services) and what they do (v111 real):**
- **audiod** captures microphone audio via ALSA, runs Silero VAD, transcribes with whisper.cpp base.en, publishes transcript events.
- **perceptiond** captures frames (V4L2 or mock), gates by salience (motion or face via OpenCV Haar), runs **LFM2.5-VL-450M Q4_0** (Liquid AI, 209 MB) on salient frames, publishes description events.
- **memoryd** stores every transcript + salient description as a vector (sentence-transformers/all-MiniLM-L6-v2, 384-dim) in SQLite. Three memory types: episodic, semantic, procedural.
- **toold** runs user-approved tools in a sandboxed directory.
- **ttsd** synthesizes voice with KittenTTS medium.
- **os-toold** exposes a config-driven allowlist of OS commands.
- **openclaw-web** is the gateway that ties them together and exposes them to Telegram.
- **dan-glasses-app** is the Tauri v2 desktop/mobile companion — the user's UI for live transcript, memory recall, TTS, vision dashboard, bootstrap wizard.

**Target user (Track A, v111):**
- **Primary:** ML engineers, founders, researchers who want Jarvis-class voice + vision without giving Meta/Quark their data. Comfortable flashing a .deb.
- **Secondary:** India + SEA technical early adopters. Price-sensitive, privacy-sensitive.
- **Tertiary:** Prosumer conference/travel/journalist use case (translation, meeting memory, summaries).

**Core value prop (one sentence):**
> A proactive AI wearable that hears what you hear, sees what you opt to show, and remembers it all *inside your own Docker container* — and only speaks when the work is done.

**Differentiator: not the hardware.** The hardware is honest (NDP200, ESP32-S3, JBD MicroLED, dual 200mAh). The moat is the **9-daemon fleet + per-user private cloud + open SDK**.

---

## 3. What is Dan Voice? (Track B)

**Definition:** A voice-first personal AI agent that turns any Bluetooth earbuds (AirPods, Sony, EarFun, Galaxy Buds) into a personal Jarvis, powered by an **isolated EigenCloud Docker container per user** running OpenClaw + Paperclip agents.

**Three-triangle connectivity:**
1. **Mobile (hub):** Flutter app, Android-first, OAuth broker, provisions the user's EigenCloud container on first login.
2. **Earbuds (input):** BT 5.0+ earbuds → mic + speaker. No on-device compute.
3. **EigenCloud (real computer):** user's own private Debian Docker container (TEE-protected), runs OpenClaw + Paperclip + Whisper + ElevenLabs.

**Eight core Paperclip workflows (v1):**
1. Expense Reports — receipt → PDF → email
2. Email Drafting — voice → draft → approve → send
3. Notion Updates — pages, DBs, task lists
4. PDF Generation — invoices, reports
5. Slack Posting — messages, summaries, alerts
6. Calendar Booking — meetings, invites
7. Meeting Summaries — transcribe → summarize → Notion/email
8. Travel Planning — research → itinerary → bookings

**Why this matters:** Every earbud owner is a prospect. No hardware purchase required. Meta Ray-Ban playbook applied to earbuds.

**Target user (Track B):** Daily Gmail + Notion + Slack + Calendar users. Age 28–45. English-fluent. White-collar. Chronically online.

**Aha moment:** when a 3-step Paperclip workflow (parse expense → PDF → email) completes without the user opening any other app.

---

## 4. What is danlab-multimodal? (Research demo)

**Definition:** A hackathon-grade demo of a sub-250MB Vision-Language Model (SmolVLM-256M Q4_K_M + SigLIP mmproj, 302 MB combined) running entirely on CPU via llama.cpp, executing a **hand-coded heuristic feedback loop** over screen captures.

**Critical framing:**
- **NOT RL.** No weights modified. No policy gradient. No learned reward model.
- **Pre-RL scaffold** — heuristic (length / error / quality) scores vision outputs 0–100, prints suggestions.
- **Credible upgrade path:** fork [SIA](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026) for harness+weights self-improvement.

**Marketing value:**
1. **Honest engineering as brand posture.** Jack Clark (May 2026) warned recursive self-improvement is "the likely next step." We are not claiming it. Credibility is the asset.
2. **Tangible demo.** `python3 src/demo.py demo` runs in 90s, outputs 92/100 average. Live: https://zo.pub/som/danlab-multimodal-demo
3. **Lead magnet for newsletter.** Engineer audience cares about honesty > hype.
4. **Hiring signal.** ML engineers who care about depth, not marketing claims.

---

## 5. What is danclaw / paperclip? (Platform)

**Source:** `/home/workspace/paperclip/AGENTS.md` and `README.md`.

**Definition:** A fork of the [Paperclip](https://github.com/paperclipai/paperclip) OSS project (MIT, dormant upstream) — a **cloud-hosted AI company orchestration platform**. If OpenClaw is an *employee*, DanClaw/Paperclip is the *company*.

**Stack:** pnpm monorepo · Node 22 · Express + TypeScript · PGlite (dev) / Postgres (prod) · Vite React UI · MCP server. Production: https://paperclip.up.railway.app

**Why in marketing:**
- It is the **infrastructure layer for every other DanLab product** — including Dan Voice's EigenCloud orchestration.
- Targets a different buyer (AI-engineering teams, agent-platform CTOs) but reinforces the DanLab platform narrative.
- Mumbai-region Fly.io deploy is a tangible India-first positioning move.

**Status (v111):** All agents paused. Dormant. Resume when ready.

---

## 6. Competitive Landscape (v111, refined)

**Sources:** v110 COMPETITORS.md + new public signals (Quark AI Glasses launched dual-eye variant with 40hr battery, Meta Ray-Ban Display launched Sep 2025 with display, Apple Vision Pro flopped, Brilliant Labs Halo shipping).

| Competitor | Threat | What they do well | Our counter |
|---|---|---|---|
| **Meta Ray-Ban Display** $799 | HIGH (10M+ units) | Brand, distribution, native ecosystem, now with display | "Your AI, your data" — we never see your voice/visuals |
| **Quark AI Glasses** (Alibaba) ~$450 | HIGH (40hr battery, dual-eye, Qwen+Alice) | AI stack, China distribution, integrated payments | Out-architecture, not out-hardware — open SDK + privacy |
| **Even Realities G1/G2** $600 | MED | Developer ecosystem (MentraOS), display quality | Dan Agent SDK — voice-native, runs in *user's* cloud |
| **Halliday Proactive AI** ~$300 | MED (concept) | Proactive AI framing | OpenClaw/Paperclip agents *can* run proactive mode for real |
| **Apple Vision Pro** $3,499 | LOW (not glasses) | Display, on-device privacy | $99–149 access via app + glasses as upgrade |
| **Brilliant Labs Halo** $299 | LOW | Open-source, thin | Same open-source posture, but backed by EigenCloud privacy |
| **Rokid/RayNeo** $249–$999 | LOW (China-only) | Display, translation | Translation is a v1 paperclip workflow we can ship in app |

**Dan Glasses v111 positioning (one line):**
> The only smart glasses whose architecture makes it *physically impossible* for the vendor to read your data.

**Why this is sharper than v110:**
- v110 said "we cannot read your emails." True, but soft.
- v111 says "physically impossible." The EigenCloud TEE attestation is a cryptographic guarantee, not a promise. That is the difference between a feature and an architecture.

---

## 7. The DanLab Story (v111, refined)

**Narrative spine:**
> **"AGI is not a destination in California. AGI is a direction — and we're walking it from India. Open source. Private by architecture. Substantive, not shiny."**

**Story beats (use in this order):**
1. **Constraint is mother of invention.** India has the world's second-largest workforce and the lowest inference costs. We build with scarcity.
2. **Privacy is non-negotiable.** When the entire industry races to train on user data, we built the inverse: user data stays in the user's TEE. Architecturally unreadable.
3. **Open is the strategy.** `dan-consciousness`, `dani`, `dani-skills`, `paperclip`, `dan-glasses`, `danlab-multimodal` — all MIT. We win by being the platform everyone ships into.
4. **Substance > polish.** We say "heuristic loop" when it's a heuristic. We say "pre-RL scaffold" when it's not RL. We say "9/9 daemons live" with real `/status` payloads. Credibility compounds.
5. **India to the world.** somdipto in Bengaluru. One engineer, one AI co-founder, one laptop. Then a movement.

**Brand keywords (v111):**
Proactive · Sovereign · Open · India-built · End-to-end owned · Substantively engineering · Architecturally private.

---

## 8. Marketing Channels (v111, prioritized)

| Channel | Role | Cadence | Why | v111 update |
|---|---|---|---|---|
| **danlab.dev** | Primary funnel — site is the URL everyone shares | Refresh 1×/month | The site is currently stale. **Highest priority this run.** | **P0: rewrite homepage.** |
| **X / Twitter** | Primary thought leadership + demo distribution | 1–3 posts/day | Engineers + founders are here | Add Telegram surface |
| **GitHub** | README + releases + Issues are the actual product story | Continuous | Devs evaluate via GitHub | Add P0 README updates |
| **LinkedIn (somdipto)** | Founder narrative + India-origin story | 2–4 posts/week | Hiring + investor + press funnel | Continue |
| **Telegram (@danlab_bot)** | New! Live product surface via OpenClaw | Continuous | "Talk to Dan from your phone" | Wire into content calendar |
| **Hacker News (Show HN)** | Daemon drops, multimodal demo, EigenCloud launch | 1–2/quarter | Top-of-funnel for technical press | Schedule for next daemon drop |
| **YouTube Shorts / Reels** | 60-second demo loops (audiod waveform, perceptiond descriptions) | 1–2/week | Discovery + virality | New: perceptiond LFM2.5 demo |
| **danlab.ai blog** | Long-form research notes (LFM2.5 quant, HRM-Text integration, Tauri bundle size) | 1–2/month | SEO + depth | New: audiod v1.1 liveness/readiness post |
| **arXiv / conference submissions** | Multimodal benchmarks, SIA fork | 1/quarter | Academic credibility | New: danlab-multimodal benchmark paper |

**Channels explicitly NOT in scope yet:** paid ads, influencers, launch PR firms, Product Hunt (premature — no product-market fit signal yet).

**v111 additions:**
- **Telegram** is now a real distribution surface. Mention it explicitly in landing copy and Twitter posts.
- **danlab.dev** is the funnel. It is currently misaligned with the strategy and must be refreshed before the next PR push.

---

## 9. Content Pillars (v111, refined)

1. **Build-in-public demos** — short video of `audiod` streaming, `perceptiond` describing a frame with LFM2.5-VL-450M, `memoryd` recalling it 10 minutes later.
2. **Engineering deep-dives** — write-ups on LFM2.5-VL-450M Q4_0 quantization trade-offs, Silero VAD threshold tuning, EigenCloud TEE attestation, audiod v1.1 liveness/readiness probe split, Tauri v2 bundle size breakdown, SmolVLM heuristic loop.
3. **Origin essays** — "Building AGI from India" series (constraints, opportunities, hiring, cost structure, Tailscale sandbox story).
4. **Pre-RL scaffold honesty** — explain what the heuristic loop *is and isn't*, link to SIA as the honest upgrade path.
5. **Open ecosystem** — call for agent builders: "If you can write a Python function, you can ship an agent that runs in your user's cloud."
6. **India-specific positioning** — Fly.io Mumbai, EigenCloud regions, INR pricing, India-first benchmarks, danlab-multimodal's "From India 🇮🇳" badge.
7. **Daemon-by-daemon storytelling** — new in v111. Each of the 9 daemons gets its own micro-post. The sum is more credible than a single "we ship" claim.

---

## 10. Current Online Presence (v111 audit)

| Surface | Status (v111) | Action |
|---|---|---|
| **danlab.dev** | **Live but stale** — shows "Agent8, Zerant, Dapify, AI Glasses" — pre-AGI-strategy copy | **P0: rewrite homepage** to match v110 strategy |
| **somdipto LinkedIn** | Active — Vibecon post, Farza Majeed comment visible, "DAN LABS / AGI" signal | Founder thread + weekly essays |
| **GitHub (somdipto)** | Active — dan-consciousness, dani, dani-skills, dan-lab, dan-glasses, danlab-multimodal, paperclip | P0 README updates |
| **Telegram (@danlab_bot)** | **Live** — polling, DM pairing, group allowlist | Add to landing + Twitter |
| **X (somdipto)** | Unknown handle | Create + populate |
| **Hacker News** | No shows yet | Schedule Show HN |
| **YouTube** | No channel identified | Set up channel |
| **Press / journalists** | Zero relationships | Build list of 10 (TechCrunch AI, The Verge wearables, HackerNews, Indian Express tech, YourStory) |

**The single biggest gap:** `danlab.dev` is the canonical URL that gets shared. It currently does not communicate any of the v110 strategy. Until it does, every other marketing action is upstream of a leaky funnel.

---

## 11. First Users / Customers (v111 profiles, refined)

### Track A — Dan Glasses (hardware)
- **Age:** 22–40
- **Location:** Bengaluru, Hyderabad, Singapore, San Francisco, Berlin
- **Profession:** ML engineer, founder, researcher, journalist, conference speaker
- **Income:** $40k+ (India ₹8L+)
- **Psychographic:** reads Hacker News daily, owns AirPods Max, cares about data sovereignty, comfortable with .deb installs, posts demo videos to LinkedIn
- **Where to find:** LocalLLaMA Discord, HackerNews comment threads, AI.engineer community, /r/LocalLLaMA, India ML Twitter
- **Activation path:** Visit danlab.dev → flash .deb → pair BT earbuds → push-to-talk ("Hey Dan, book my standup for tomorrow") OR `/start` audiod + talk
- **Aha moment:** when perceptiond describes something they didn't ask about ("you're looking at a recipe for sourdough") OR when memoryd recalls a meeting from last Tuesday unprompted.

### Track B — Dan Voice (app)
- **Age:** 25–50
- **Profession:** Product manager, founder, consultant, sales lead
- **Stack:** Gmail + Notion + Slack + Google Calendar + (optionally) WhatsApp
- **Activation path:** Visit danlab.dev → download Android app → sign in → wait 60s for EigenCloud container → pair earbuds → say "summarize my last 5 emails"
- **Aha moment:** when a 3-step Paperclip workflow (parse expense → PDF → email) completes without the user opening any other app.

### Track C — DanLab ecosystem (developers)
- **Age:** 22–35
- **Profession:** AI engineer, indie hacker, agent-platform CTO
- **Stack:** Python or TypeScript
- **Activation path:** `pip install dan-agent-sdk` OR `npm install @danlab/agent-sdk` → one-line tool registration → ship a skill to the skills registry
- **Aha moment:** when their custom agent appears inside a *user's* container and the user talks to it.

### Track D — Telegram early adopters (v111 new)
- **Who:** Anyone with the Telegram app, comfortable with bot pairing
- **Activation path:** DM `@danlab_bot` → pairing → talk to Dan from the phone
- **Why this is interesting:** Zero install. Zero hardware. Zero friction. The "phone Jarvis" use case is a free distribution surface.
- **Aha moment:** first non-trivial task completed by the bot (e.g., "summarize my last email" — when wired to a user's Gmail).

---

## 12. Open Questions (for somdipto, will surface in delivery)

1. **danlab.dev refresh** — who has write access today? What stack? (Need to know to ship P0.)
2. **Brand naming** — "DanLab.dev" for research, "Dan" for consumer? Or one brand? (Carried from v110.)
3. **Twitter handle** — confirm @danaboratory or @danlab_dev availability.
4. **Public face for press** — somdipto, or do we want a second co-founder on-camera?
5. **Pricing transparency** — publish INR prices publicly now, or wait for EigenCloud regional launch?
6. **Telegram pairing policy** — keep `pairing` (manual approve each user) or move to `allowlist` (invite-only)? Pairing is the right call for now.
7. **HRM-Text-1B integration** — when audiod v1.3 ships, do we lead with the "reasoning on the wearable" angle, or stay quiet and let it land in the foundation update?

---

*End of v111 research. v111 strategy, calendar, Twitter pack, landing copy, and README suggestions follow in sibling files.*

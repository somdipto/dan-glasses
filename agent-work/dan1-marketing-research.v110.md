# DanLab Marketing Research — Run v110
**Date:** 2026-06-29
**Owner:** DAN-1 (marketing + growth)
**Status:** Comprehensive research complete. Two parallel product tracks discovered.

---

## 0. Executive Summary (read this first)

The DanLab ecosystem is **two product tracks evolving in parallel**, not one product. Both are real, both are shipping, and both must be marketed together because they share one brain (Dani/OpenClaw/Paperclip) and one origin (India, AGI from the ground up).

| Track | Codename | Form factor | Stage | Lead |
|-------|----------|-------------|-------|------|
| **A** | **Dan Glasses (wearable)** | Smart glasses — ESP32-S3 + ESP32-C6 + NDP200 + LFM2.5-VL-450M | v1.5 in foundation; 9/9 daemons live | DAN-1/DAN-2 |
| **B** | **Dan Voice (app-first)** | Phone + any BT earbuds → user’s EigenCloud Docker container | v1 PRD shipped; 8–10 wk Phase 1 | (Dan) |

**The pitch is one story told two ways:**
> *Your AI. Your cloud. Your face.* — private, proactive, sovereign. Built from India, for the world.

**Why this works:**
1. **Privacy by architecture** — no competitor puts the user’s data in the user’s own EigenCloud TEE container. Quark, Meta, Even Realities all train on the user.
2. **Open agent platform** — Dan Agent SDK lets any developer ship an agent that runs inside *the user’s* cloud. This is an ecosystem moat, not a feature.
3. **Proactive, not reactive** — perceptiond + memoryd + OpenClaw form a *watchful* loop: see, remember, anticipate. Every smart-glasses competitor today is a *reactive* assistant (you ask, it answers).
4. **From India to the world** — origin story that Silicon Valley cannot replicate. We are not "Indian AI lab trying to be American." We are *India-built AGI*, with the technical rigor to back it.

---

## 1. What is Dan Glasses? (Track A)

**Definition:** A privacy-first, always-aware AI wearable that runs a 7-service local fleet (audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclaw-web) tied together by a Tauri v2 app and an OpenClaw orchestration layer.

**Hardware truth (sourced from COMPETITORS.md + Canonical Spec):**
- v1: ESP32-S3 (compute) + Syntiant NDP200 (always-on wake-word, 200µW), 400–450 mAh dual-battery, USB-C, BT 5.3 LE audio, <40g, **no camera, no display**
- v1.5: + JBD MicroLED single-eye (waveguide), + opt-in 8MP camera, ~500 mAh
- v2: + dual-eye display, prescription lens integration

**Local AI fleet (live, sourced from agent-work/dan1.md v109 port matrix):**

| Service | Port | Purpose | Status |
|---|---|---|---|
| audiod | 8090/8091 | ALSA capture → Silero VAD → whisper.cpp base.en → JSON events | ✅ live (v1.0, 141 tests) |
| perceptiond | 8092 | V4L2 capture → motion+face salience → LFM2.5-VL-450M Q4_0 (mmproj) | ✅ live (watchful mode) |
| memoryd | 8741 | SQLite + sentence-transformers MiniLM-L6-v2 vectors (episodic/semantic/procedural) | ✅ live |
| toold | 8742 | Sandboxed tool execution | ✅ live |
| ttsd | 8743 | KittenTTS synthesis (<25MB, base variant) | ✅ live |
| os-toold | 8744 | OS-bounded command surface | ✅ live |
| openclaw-web | 18789 | OpenClaw gateway (loopback) | ✅ live |

**Target user (Track A):**
- **Primary:** builders/operators/engineers who own a laptop and want a Jarvis-class wearable with cloud-grade reasoning and on-device privacy.
- **Secondary:** India + Southeast Asia early-adopter technical consumer base (people willing to flash a .deb).
- **Tertiary:** prosumer conference/travel/journalist use case (real-time translation, meeting memory, on-the-fly summaries).

**Core value proposition (one sentence):**
> A proactive AI wearable that sees and hears what you see and hear, remembers it all *inside your own Docker container*, and stays out of your way until it has something worth saying.

---

## 2. What is Dan Voice? (Track B)

**Source:** `/home/workspace/DanGlasses/PRD.md`, `/home/workspace/DanGlasses/PRD_DAN_VOICE.md`, `ARCHITECTURE.md`, `DEVELOPMENT_PLAN.md`.

**Definition:** A voice-first personal AI agent that turns any Bluetooth earbuds (AirPods, Sony, EarFun, Galaxy Buds) into a personal Jarvis, powered by an **isolated EigenCloud Docker container per user** running OpenClaw + Paperclip agents.

**Strategic pivot (2026-04-21, in ARCHITECTURE.md):**
- *Old gate:* "Buy glasses to unlock the full app."
- *New gate:* "Full power in the app always. Glasses = optional ₹12–15k accessory that upgrades only the voice IO layer."
- *Reason:* Meta Ray-Ban playbook — get thousands via free powerful app, then monetize the wearable upgrade.

**Three-triangle connectivity:**
1. **Mobile triangle (hub):** Flutter app, Android-first, OAuth broker for Gmail/Notion/Slack/Calendar/WhatsApp, provisions the user’s EigenCloud container on first login.
2. **Earbuds triangle (input):** BT 5.0+ earbuds → mic + speaker. No on-device compute.
3. **EigenCloud triangle (real computer):** user’s own private Debian Docker container (TEE-protected, 2 vCPU / 4 GB RAM / 10 GB), runs OpenClaw + Paperclip + Whisper + ElevenLabs.

**Data flow:**
```
Earbuds mic → BT → Flutter App → WS → EigenCloud container
                                            ↓
                                    OpenClaw + Paperclip agents
                                            ↓
                                    TTS → WS → App → Earbuds speaker
```

**8 core Paperclip agent workflows (v1):**
1. Expense Reports — receipt → PDF → email
2. Email Drafting — voice → draft → approve → send
3. Notion Updates — pages, DBs, task lists
4. PDF Generation — invoices, reports
5. Slack Posting — messages, summaries, alerts
6. Calendar Booking — meetings, invites
7. Meeting Summaries — transcribe → summarize → Notion/email
8. Travel Planning — research → itinerary → bookings

**Free tier:** 48-hour container lifetime, 50 msg/hour, 5 complex tasks/day. Paid unlimited tier unlocks persistent container.

**Target user (Track B):**
- **Primary:** Knowledge workers on Gmail + Notion + Slack + Google Calendar — the daily-driver productivity stack.
- **Why this is a billion-user TAM:** Every earbud owner is a prospect. No hardware purchase required to start.

---

## 3. What is danlab-multimodal? (Research demo)

**Source:** `/home/workspace/danlab-multimodal/README.md`, `docs/ARCHITECTURE.md`.

**Definition:** A hackathon-grade demo of a sub-250MB Vision-Language Model (SmolVLM-256M Q4_K_M + SigLIP mmproj) running entirely on CPU via llama.cpp, executing a **hand-coded heuristic feedback loop** over screen captures.

**Critical framing (from README):**
- **This is NOT RL.** No weights are modified. No policy gradient. No learned reward model.
- It is a **pre-RL scaffold** — a heuristic (length/error/quality) that scores vision outputs 0–100 and prints suggestions.
- The credible path to genuine self-improvement is the [SIA framework](https://github.com/HexoLabs/SIA) (MIT, May 2026), which DanLab plans to fork for a true RL upgrade.

**Why this matters in marketing:**
1. **Honest engineering as brand posture.** Jack Clark publicly warned (May 2026) that recursive self-improvement is "the likely next step." Most demos claim RL — we don’t. Our credibility is the asset.
2. **Sub-250MB on CPU** is a tangible, demoable milestone — `python3 src/demo.py demo` runs in 90 seconds and outputs a 95/100 average score.
3. **Demo link:** https://zo.pub/som/danlab-multimodal-demo

**Use cases:**
- Live asciinema demo on X/LinkedIn
- Lead magnet for the danlab.ai newsletter
- Hiring signal for engineers who care about ML engineering depth, not marketing claims

---

## 4. What is danclaw / paperclip? (Platform track)

**Source:** `/home/workspace/paperclip/README.md`, AGENTS.md (meta).

**Definition:** DanClaw is a fork of the [Paperclip](https://github.com/paperclipai/paperclip) OSS project (MIT, dormant upstream) — a **cloud-hosted AI company orchestration platform**. If OpenClaw is an *employee*, DanClaw is the *company*.

**Stack (from source):** pnpm monorepo · Node 22 · Express + TypeScript · PGlite (dev) / Postgres (prod) · Vite React UI · MCP server. Production: https://paperclip.up.railway.app

**Ships:**
- One-command Docker: `ghcr.io/somdipto/paperclip:latest`
- Railway / Fly.io deploy templates (Mumbai region supported!)
- Express server (port 3100/3101), UI, CLI, eval suite

**Why this matters in marketing:**
- It is the **infrastructure layer for every other DanLab product** — including Dan Voice’s EigenCloud orchestration.
- Targets a different buyer (AI-engineering teams, agent-platform CTOs) but reinforces the DanLab platform narrative.
- Mumbai-region Fly.io deploy is a tangible India-first positioning move.

---

## 5. What is blurr / Panda? (Adjacent Android agent)

**Source:** `/home/workspace/blurr/README.md`.

**Definition:** Panda — a proactive, on-device Android AI agent that sees the screen, understands context, and autonomously drives the UI. Uses GCS Chirp for high-quality TTS.

**Status:** WIP. Memory temporarily disabled. Published on Play Store.

**Marketing relevance:** Cross-reference only. Validates the "proactive on-device agent" thesis that Dan Glasses will lean on in v1.5 (camera opt-in + salience-driven triggers). Do **not** co-promote — different product, different audience.

---

## 6. Competitive Landscape

**Source:** `/home/workspace/DanGlasses/COMPETITORS.md` (canonical competitive matrix, last updated 2026-04-21).

| Competitor | Threat | What they do well | Our counter |
|---|---|---|---|
| **Meta Ray-Ban** $299 | HIGH (1M+ units) | Brand, distribution, native ecosystem | "Your AI, your data" — we never see your voice/visuals |
| **Quark AI Glasses** (Alibaba) ~$450 | HIGH (40hr battery, dual-eye, Qwen+Alice) | AI stack, China distribution, integrated payments | Out-architecture, not out-hardware — open SDK + privacy |
| **Even Realities G1/G2** $600 | MED | Developer ecosystem (MentraOS), display quality | Dan Agent SDK — voice-native, runs in *user’s* cloud |
| **Halliday Proactive AI** ~$300 | MED (concept) | Proactive AI framing | OpenClaw/Paperclip agents *can* run proactive mode for real |
| **Apple Vision Pro** $3,499 | LOW (not glasses) | Display, on-device privacy | $99–149 access via app + glasses as upgrade |
| **Brilliant Labs Halo** $299 | LOW | Open-source, thin | Same open-source posture, but backed by EigenCloud privacy |
| **Rokid/RayNeo** $249–$999 | LOW (China-only) | Display, translation | Translation is a v1 paperclip workflow we can ship in app |

**Dan Glasses competitive positioning (from COMPETITORS.md):**
- *Privacy:* personal Docker container — the **only** player that does this.
- *App-first:* free full-power app, glasses as upgrade.
- *SDK:* Dan Agent SDK as ecosystem moat.
- *Price:* aggressive ₹12–15k glasses + free app.
- *Origin:* India-credible + global ambitions.

---

## 7. The DanLab Story (narrative arc)

**The narrative spine** (derived from CONSCIOUSNESS.md + somdipto LinkedIn signal + the danlab-multimodal README "From India 🇮🇳" badge):

> **"AGI is not a destination in California. AGI is a direction — and we're walking it from India."**

**Story beats (use in this order on social):**
1. **Constraint is mother of invention.** India has the world’s second-largest workforce and the lowest inference costs. We build with scarcity.
2. **Privacy is non-negotiable.** When the entire industry is racing to train on user data, we built the inverse: user data stays in the user’s TEE. That is *the* differentiator.
3. **Open is the strategy.** Dan Agent SDK, OpenClaw, Paperclip — all open. We win by being the platform that everyone ships into.
4. **Substance > polish.** We say "heuristic loop" when it’s a heuristic. We say "pre-RL scaffold" when it’s not RL yet. Credibility compounds.

**Brand keywords:** Proactive · Sovereign · Open · India-built · End-to-end owned · Substantively engineering.

---

## 8. Marketing Channels (in priority order)

| Channel | Role | Cadence | Why |
|---|---|---|---|
| **X / Twitter** | Primary thought leadership + demo distribution | 1–3 posts/day | Engineers + founders are here |
| **GitHub** | README + releases + Issues are the actual product story | Continuous | Devs evaluate via GitHub |
| **LinkedIn (somdipto)** | Founder narrative + India-origin story | 2–4 posts/week | Hiring + investor + press funnel |
| **Hacker News (Show HN)** | Daemon drops, multimodal demo, EigenCloud launch | 1–2/quarter | Top-of-funnel for technical press |
| **Discord/Slack communities** | Hacker crews (AI Engineers, LocalLLaMA, e/acc, slock) | Daily lurking, weekly posts | Feedback + early users |
| **YouTube Shorts / Reels** | 60-second demo loops (audiod waveform, perceptiond descriptions) | 1–2/week | Discovery + virality |
| **danlab.ai blog** | Long-form research notes (SmolVLM benchmark, LFM2.5 quant notes, Whisper latency) | 1–2/month | SEO + depth |
| **arXiv / conference submissions** | Multimodal benchmarks, danlab-multimodal SIA-fork | 1/quarter | Academic credibility |

**Channels explicitly *not* in scope yet:** paid ads, influencers, launch PR firms, Product Hunt (premature — no product-market fit signal yet).

---

## 9. Content Pillars (what we publish)

1. **Build-in-public demos** — short video of `audiod` streaming, `perceptiond` describing a frame, `memoryd` recalling it 10 minutes later.
2. **Engineering deep-dives** — write-ups on LFM2.5-VL-450M Q4_0 quantization trade-offs, Silero VAD threshold tuning, EigenCloud TEE attestation, SmolVLM heuristic loop.
3. **Origin essays** — "Building AGI from India" series (constraints, opportunities, hiring, cost structure).
4. **Pre-RL scaffold honesty** — explain what the heuristic loop *is and isn’t*, link to SIA as the honest upgrade path.
5. **Open ecosystem** — call for agent builders: "If you can write a Python function, you can ship an agent that runs in your user’s cloud."
6. **India-specific positioning** — Fly.io Mumbai, EigenCloud regions, INR pricing, India-first benchmarks.

---

## 10. Current Online Presence (audit, 2026-06-29)

| Surface | Status | Action |
|---|---|---|
| **somdipto LinkedIn** | Active, posted about danlab.dev at Vibecon (referenced by Aniket Raj). Farza Majeed comment visible. | Founder thread + weekly essays |
| **danlab.dev domain** | Pointed but landing page status unknown | Build danlab.ai/danglasses |
| **GitHub (somdipto)** | Active — dan-consciousness, dani, dani-skills, dan-lab org | Polish READMEs (see deliverable 5) |
| **X (somdipto)** | Unknown handle; handle is `somdipto` | Create + populate, see dan1-twitter-content |
| **X project handles** | None | Decide on @danaboratory or @danaboratory_ai |
| **Hacker News** | No shows yet | Schedule Show HN for next daemon drop |
| **YouTube** | No channel identified | Set up channel; first video: danlab-multimodal asciinema with voiceover |
| **Discord** | None | Skip — premature |
| **Press / journalists** | Zero relationships | Build list of 10 (TechCrunch AI, The Verge wearables, HackerNews, Indian Express tech, YourStory) |

---

## 11. First Users / Customers (ideal early adopter profile)

### Track A — Dan Glasses (hardware)
- **Age:** 22–40
- **Location:** Bengaluru, Hyderabad, Singapore, San Francisco, Berlin
- **Profession:** ML engineer, founder, researcher, journalist, conference speaker
- **Income:** $40k+ (India $8L+)
- **Psychographic:** reads Hacker News daily, owns AirPods Max, cares about data sovereignty, comfortable with .deb installs, posts demo videos to LinkedIn
- **Where to find:** LocalLLaMA Discord, HackerNews comment threads, AI.engineer community, /r/LocalLLaMA, India ML Twitter
- **Activation path:** Download danlab.ai → flash .deb → pair BT earbuds → push-to-talk ("Hey Dan, book my standup for tomorrow")
- **Aha moment:** when perceptiond describes something they didn’t ask about ("you’re looking at a recipe for sourdough") OR when memoryd recalls a meeting from last Tuesday unprompted.

### Track B — Dan Voice (app)
- **Age:** 25–50
- **Profession:** Product manager, founder, consultant, sales lead
- **Stack:** Gmail + Notion + Slack + Google Calendar + (optionally) WhatsApp
- **Activation path:** App Store / Play Store → sign in → wait 60s for EigenCloud container → pair earbuds → say "summarize my last 5 emails"
- **Aha moment:** when a 3-step Paperclip workflow (parse expense → PDF → email) completes without the user opening any other app.

### Track C — DanLab ecosystem (developers)
- **Age:** 22–35
- **Profession:** AI engineer, indie hacker, agent-platform CTO
- **Stack:** Python or TypeScript
- **Activation path:** `pip install dan-agent-sdk` OR `npm install @danlab/agent-sdk` → one-line tool registration → ship a skill to the skills registry
- **Aha moment:** when their custom agent appears inside a *user’s* container and the user talks to it.

---

## 12. Open Questions (for somdipto, will surface in delivery)

1. **Brand naming:** Should the company brand be "DanLab.dev" or have a consumer brand separate from research? Example: "DanLab" = research, "Dan" = consumer product. This affects logo, social handles, copy voice.
2. **Twitter handle:** Confirm @danaboratory is available and matches the legal entity.
3. **Founding team public footprint:** Should somdipto be the public face, or do we want additional co-founder visibility (for press purposes)?
4. **Pricing transparency:** Are we publishing INR prices publicly now or wait for EigenCloud regional launch?
5. **Press embargo:** When do we want the first Show HN / TechCrunch piece to land? Anchor it to a real milestone (next daemon drop, or first Paperclip agent live in container).

---

*End of research. Strategy + content + landing-page + GitHub-README deliverables written to follow.*

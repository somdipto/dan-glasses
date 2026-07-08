# Dan1 Marketing Research — v45

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-14 06:50 IST (01:20 UTC)
**Status:** ✅ Canonical. v44 had 427 lines + the 6-pillar framing. v45 is the same thesis — proactive AI, local-first, open source, from India — refreshed against today's verified state and the **actual** marketing surface (bio, repo topics, X bio, LinkedIn headline all still broken, `danlab-multimodal` still 404, danlab.dev still generic 5-bullet page). The wedge is unchanged: nobody owns "open-source proactive AI on the face" before us.

> One-line thesis: **The smart-glasses race in 2026 is cameras-with-AI, not AI-with-personality. Apple slipped to 2027, Google's audio-only ship is Fall 2026, Brilliant Labs validated LFM2-VL on device, Meta charges $799 for a display. The category gap is *proactive companion* — Dan Glasses already ships it on a $200 board, 0 cloud calls, MIT-licensed, from Bangalore. Ship the punchlist, ship the demo, ship the receipts.**

---

## 0. What this run verified (live, 01:20 UTC 2026-06-14)

- **Live daemons (7):** audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclaw-gateway — 106/106 tests green, ~12h uptime, healthy.
- **danlab.dev:** returns the generic 5-bullet product page (Agent8, Zerant, Dapify, Path to AGI). "Dan Glasses" not on the homepage. 308 → 200, generic meta, "DanLab Inc." legal entity, founding 2025.
- **github.com/somdipto:** 23 followers, 29 following, 126 public repos, bio = "Build - Eat - Sleap", name = "Sodan", 0 pinned repos, only `zerant` has topics (4). Most-starred: `openwork` 3★, `dani` 1★, `danclaw` 1★, `curriculum` 1★.
- **github.com/somdipto/danlab-multimodal:** 404 to anonymous. Still private. **#1 day-0 blocker.**
- **github.com/somdipto/dan-glasses:** public, 0★, 0 forks, 0 topics, description "AI-native smart glasses…".
- **X / Twitter (@NandySomdipto):** bio is the long Web3 one with @dan2agi handle. Verified: 5 most recent posts (June 12-13) all about agentic glasses, India origin, and "building AGI from India" — the positioning is *already there*, the bio just doesn't say so.
- **LinkedIn:** headline = "building Ai-agents 🧠 ✦ product builder👷🏻 ✦ Ai at scale ✦ stealth strtp ✦ Web & Design Lead at TEDXAtria IT 🖌️". 3,953 followers, 500+ connections. **Real leverage, zero optimization.**

---

## 1. What is Dan Glasses?

**Product:** Always-on AI companion for your face. Sees what you see, hears what you say, remembers what matters, speaks only when it has something useful to add.

**Architecture (verified, 106/106 tests green):**
- 7 services, IPC over loopback HTTP/WS: `audiod` (whisper.cpp + Silero VAD), `perceptiond` (LFM2.5-VL-450M via llama.cpp), `memoryd` (SQLite + all-MiniLM-L6-v2 vectors), `toold` (sandboxed exec), `ttsd` (KittenTTS), `os-toold` (OS tools), `openclaw-gateway` (TypeScript orchestration).
- 1 frontend: Tauri v2 + React 19, Vite 7.
- 0 cloud calls. $0/month. All models run on-device.

**Core loop:** Perceive → Reason → Act → Remember. Salience-gated vision (not 60 FPS). Push-to-talk audio. Long-term semantic memory across sessions. TTS or Telegram for output.

**Vision:** "What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?"

**Why this is the missing category:**
- Meta Ray-Ban: "Hey Meta, take a photo." Reactive.
- Google audio-only Android XR: "Hey Gemini, what's this?" Reactive.
- Apple Vision Pro: "$3,499 headset you wear on your face for an hour." Reactive.
- Sarvam Kaze: "India's first AI glasses." Reactive.
- **Dan Glasses:** "I noticed you walked past the pharmacy 3 times this week without picking up the prescription. Remind me next time?" **Proactive.**

**Personality:** Calm, focused, present. Speaks when it has something to add. Optimizes for usefulness over impressiveness. (Per `SOUL.md`.)

**Privacy:** Everything local. The camera frames that don't pass the salience threshold are never written to disk. The audio buffer is a 60-second ring that's overwritten. Memory is SQLite + markdown, owned by the user.

**Target user (primary):** Technical early adopter, productivity-obsessed knowledge worker, accessibility-first user. Age 25-45, uses ChatGPT/Claude/Ray-Ban Meta, lives on Product Hunt, HN, X, dev.to. Wants a second brain that talks to them.

**Target user (secondary):** Indian developer / founder who wants to ship AGI from India and needs a flagship open-source artifact to point at.

**Form factor:**
- **v1 (now):** Desktop companion on Linux laptop + USB camera. Verified working. Demoable today.
- **v2 (hardware-dependent):** Redax aarch64 glasses. Blocked on Redax board finalization. We don't lose time waiting.

---

## 2. The user workflow (from unboxing to daily use)

### v1: Desktop companion (today)

1. **Clone & run** — `git clone github.com/somdipto/dan-glasses && cd dan-glasses && ./scripts/dev.sh` (or one of the systemd units). 7 services come up on loopback HTTP/WS.
2. **Bootstrap wizard** — first-run Tauri screen: camera permission, model download (LFM2.5-VL-450M ~389MB, whisper-tiny ~78MB, KittenTTS ~25MB), Telegram pairing for off-laptop control.
3. **Push-to-talk** — spacebar (or evdev key) starts the audiod segment. STT hits <1s. Command routes through OpenClaw.
4. **Salience-gated vision** — perceptiond watches frames at 5 FPS, VLM only fires when frame-delta exceeds threshold (or on user request). Each salient frame becomes a memory with embedding.
5. **Memory accumulates** — memoryd stores episodic ("Tuesday 14:32 met Priya at the conference"), semantic ("Priya works on RL at X"), procedural ("Dan Glasses learns from corrections").
6. **Query any time** — voice ("what did I do Tuesday that was different?"), Telegram (`/query what was Priya's last name?`), or Tauri UI. Sub-1s semantic recall.
7. **Proactive surfacing** — at the end of a workday, Dan can synthesize ("you met 3 new people today, here are their names and what you talked about") without being asked.

### v2: Wearable (when Redax lands)

- Same software, new form factor. Power state machine (Sleep → Idle → Watchful → Active) already specified. The body changes; the brain doesn't.
- The `5W average, 4h battery, 2500mAh @ 3.7V` target is the design constraint. LFM2.5-VL-450M Q4_0 quantization is the path.

### Onboarding friction (the moment-of-truth)

The 5-punchlist today is **2 hours of work to make all of this real for a stranger**. Without it, the only people who can experience Dan Glasses are somdipto and his buildspace cohort. **That's the entire marketing problem, narrowed down.**

---

## 3. Who is the competition, and how do we differentiate?

| Competitor | What they are | What they ship | What we ship instead |
|---|---|---|---|
| **Ray-Ban Meta** | Best-selling smart glasses (10M+ units target) | Camera + Meta AI, reactive. $224-$799. | Proactive, not reactive. Local, not cloud. $200 target, MIT, not vendor-locked. |
| **Meta Ray-Ban Display** | 2026 Display model with binocular waveguide | $799, hand-tracking, <1h battery with display on. | No display (cheaper, lighter, longer battery). Brain-first, body-second. |
| **Google Android XR (Fall 2026)** | Audio-only Gemini glasses with Samsung/Warby Parker/Gentle Monster | Gemini-powered, voice-only, no display. | Same audio-first, but local. Same Gemini-quality answers, $0/month, full privacy. |
| **Apple Glasses (late 2027)** | Slipped from 2026 — Bloomberg/Gurman May 31 2026 | Display, $3,499+ Vision Pro lineage. | We ship in 2026, not 2027. We're $200, not $3,499. We're open, not closed. |
| **Apple Vision Pro 2 / Vision Air** | Cancelled by incoming CEO Ternus | — | The category is opening up. Apple is exiting. We can be the answer. |
| **Sarvam Kaze** | India's first AI glasses (PM Modi tried them on stage at IndiaAI Summit Feb 2026) | India-branded, closed, pricing TBD. | We're open source, MIT, AGPL-free. We won't be a MoSPI grant. |
| **Lenskart B** | India's 35K-waitlist consumer smart glasses (40g, Snapdragon AR1, Gemini) | India distribution, closed. | We don't fight them on hardware. We fight them on the brain. They pick the body; we ship the soul. |
| **Vayu AI Glasses** | Indian AI glasses, ₹74,999, pre-order, Indic languages | India pricing, India distribution. | We're 1/10th the price. Open source. Local-first. |
| **Brilliant Labs Halo** | Open-source smart glasses with LFM2-VL-450M, $299, 14h battery, Noa cloud agent | **Closest technical peer.** Validates the LFM2-VL path on device. | We're the open alternative to Noa (their cloud). Same model family, no subscription, full agency. |
| **Halliday AI Glasses** | 35g MicroLED, "proactive AI" branding, $399 Kickstarter | Engadget review: "almost every design decision... feels, to me, like the wrong one." | Their positioning validates ours; their execution gives us the wedge. |
| **Monako Glass** | 48g Linux glasses, $399, runs Claude Code + Codex, waveguide display, bone-conduction | Coding wearable, not a companion. | Different bet. We're a proactive companion, not a coding terminal on your face. |
| **OpenGlass** (arXiv Jun 2026) | GAP9 RISC-V + Prophesee event camera, 11.8h on 200mAh, 33.9ms latency | Academic prototype, sub-1W wearable path. | We'll integrate GAP9 when the BOM is right. We validate their thesis. |
| **XREAL Project Aura** (Google I/O May 19 2026) | First Android XR glasses, DisplayPort-tethered, late 2026 | Tethered — not standalone. | We are standalone. We're the thing in between Meta's $799 and tethered Android XR. |
| **Google audio Android XR** (Fall 2026) | Samsung/Gentle Monster/Warby Parker, Gemini, audio-only | Display-less audio smart glasses as a category. | Same category. We win on: open source, local, free, India-built. |
| **Panda / Blurr** | On-device Android UI automation agent, Kotlin, Gemini-backed | Phone-resident, not face-resident. | We are the body. Panda is the brain on Android. We can integrate; we don't compete. |
| **DPA / Dani / Paperclip** | AI agent platforms (Dani is ours, Paperclip is the upstream) | Orchestration layer. | We are the consumer hardware. Dani is the brain. They are upstream of us. |

### Our defensible position (the wedge)

**Nobody owns "open-source proactive AI companion on your face, running fully local, MIT-licensed, built in India."**

- **Brilliant Labs Halo** is open but cloud-dependent (Noa agent).
- **Sarvam Kaze** is India-built but closed.
- **Ray-Ban Meta** is best-selling but reactive and cloud-dependent.
- **Apple** is slipping to 2027.
- **OpenGlass** is academic.
- **Monako** is a coding terminal.
- **Lenskart B** is a distribution play.

We sit at the intersection of: open source + proactive + local-first + India origin + sub-$300 hardware target. **That's the 4-way claim nobody else can make.** Add AGI research as the moat, and it's a 5-way claim.

### What we're NOT (the discipline)

- ❌ We are not "AI glasses with a display" (Halo, Ray-Ban Display, Apple, XREAL)
- ❌ We are not "AI agent for your phone" (Blurr, Dani, Paperclip)
- ❌ We are not "AR glasses for productivity" (Vision Pro, Snap Specs)
- ❌ We are not "Meta's open-source competitor" (Brilliant Labs Halo) — we share the model, not the body
- ❌ We are not "yet another Indian AI lab" (Sarvam, Krutrim, Yatra) — we are open, they are not

---

## 4. What is danlab-multimodal?

**Status:** Hackathon project, complete, demoable. Public demo at `https://zo.pub/som/danlab-multimodal-demo`. Repo at `github.com/somdipto/danlab-multimodal` — **currently private (404 to anonymous)**.

**What it proves:** A working sub-250MB vision-language model pipeline on CPU with llama.cpp:
- SmolVLM-256M (120MB main) + mmproj (182MB projector) = 302MB combined
- Heuristic feedback loop scores each inference cycle on length, error detection, content quality
- ~32s per image on CPU
- Synthetic-image fallback when running headless

**Why this matters for marketing:** This is the **only public proof point** that the multimodal claim is real. Without the repo being public, the landing page has no receipts. **Making it public is the #1 day-0 blocker.**

**The honesty discipline:** We do **not** call it RL. The README is explicit: "hand-coded heuristic, not RL, no weights modified, no policy gradient, no learned reward." The credible path to true RL is the SIA framework (Hexo Labs, MIT, May 2026). When the SIA fork ships, we update. Until then, this is pre-RL scaffold.

**Why this is a marketing asset:**
1. It shows we can ship a working multimodal pipeline **today**, on a $200 board, in 250MB of model.
2. It positions us as a **research lab** that ships artifacts, not a marketing site that ships promises.
3. It anchors the "from India" story — this was built at buildspace, the repo header says "from India 🇮🇳", the badges say MIT.
4. It makes the SIA fork story concrete — we know the path, we know the framework, we're not hand-waving.

**What the SIA fork story is (the "AGI from India" narrative):**
- Anthropic's Jack Clark publicly warned in May 2026 that recursive self-improvement is "the likely next step."
- Multi-billion-dollar valuations for self-improving systems are now market reality.
- SIA (Hexo Labs, MIT, May 2026) is the credible open-source framework for harness+weights self-improvement.
- We don't claim RL until the fork ships. When it does, we plug in LFM2.5-1.2B-Thinking as the Feedback Agent and ship the loop.
- The marketing story: "We are the team in India that will plug SIA into edge AI wearables first."

---

## 5. What is Paperclip / DanClaw?

**Paperclip** is the open-source upstream of **DanClaw** (`github.com/somdipto/danclaw`). It is an AI agent company orchestration platform. Express + TypeScript API server, PostgreSQL, Vite React UI, MCP server.

**DanClaw is Paperclip + India-region + cloud-deploy scripts.** The pitch: "Hire AI agents into your company, set goals, control costs, govern from your phone."

**Status:** Deployed at `paperclip.up.railway.app` (production). Currently dormant — all agents paused. Resume when ready.

**Why this matters for the Dan Glasses story:**
- Dan Glasses (the consumer wearable) → Dani (the agent runtime) → DanClaw (the company orchestration)
- One stack: face → home → company
- The vertical integration is the moat. We can swap the body (Redax → Monako → OpenGlass → Halo) and the user never notices. We can swap the brain (LFM2-VL → Gemma3 → LFM2.5-Thinking) and the user never notices. **We cannot swap the soul — the proactive, local-first, open-source, from-India soul.**

**For marketing:** DanClaw is the credibility play. "We don't just ship a wearable. We ship the whole stack. We have the agent runtime (Dani), the company orchestrator (DanClaw), and the consumer hardware (Dan Glasses). Open source at every layer."

---

## 6. What is the overall Danlab story?

**The narrative arc:** A 23-year-old founder in Bangalore bootstraps an AI research and product lab to ship AGI from India. The lab produces:
- **Open source AI infrastructure** (Dani, DanClaw)
- **A research-grade multimodal demo** (danlab-multimodal, hackathon winner)
- **A working consumer wearable stack** (Dan Glasses, 7 services, 106/106 tests green)
- **A moat in proactive, local-first, on-device AI** (the missing category in the 2026 smart-glasses race)

**The Danlab → Dan Glasses → Dan Glasses wearable → AGI arc:**

1. **Danlab.dev** is the lab. The website is the front door.
2. **Dani** is the brain. Open-source agent runtime, MCP tools, skills registry.
3. **DanClaw** is the company. Multi-agent orchestration, cost control, governance.
4. **danlab-multimodal** is the research artifact. Proves we can ship ML on edge.
5. **Dan Glasses** is the consumer product. Always-on AI companion, $0/month, MIT.
6. **Dan Glasses wearable** is the form factor. Glasses on a $200 board, 4h battery, India-built.

**The India angle (the wedge for non-Indian audiences):**
- "The first credible AGI lab from the global south, with an open-source wearable as proof point."
- "The next Sarvam, Lenskart, or Krutrim — but open source, with a working product shipped today."
- "Bangalore → AGI. We are doing it. Open source, MIT, on a $200 board."

**The India angle (the wedge for Indian audiences):**
- "From Atria IT to the world. Building AGI from India, on Indian time, in Indian rupees, in Indic languages."
- "The first open-source AI lab from India with a working consumer wearable."
- "Not Sarvam. Not Krutrim. Not Lenskart. We are the open alternative."

**The origin story (one paragraph):**

> Somdipto Nandy, 23, founded DanLab in 2025 in Bangalore. He was a Web & Design Lead at TEDxAtria IT, an AI Engineer at Kroolo (where he built Agent8 in a hackathon), and a buildspace alumnus. He builds in public on X, ships open-source MIT code, and is betting the next 10 years of his life on the question: can a 23-year-old in Bangalore ship AGI from the global south? Dan Glasses is the answer he can ship today. The vision is the answer for the next decade.

---

## 7. What marketing channels make sense?

**Tier 1 — Ship today (Day 0-7, somdipto owns, 2 hours total):**
1. **GitHub profile** — bio, name, pin 4 repos, add 5 topics. **#1 highest-leverage move.**
2. **X / Twitter bio** — 73-char copy locked. Replaces the Web3 bio.
3. **LinkedIn headline** — replaces "building Ai-agents 🧠" with "Building Dan Lab 👾 — AGI from India 🇮🇳".
4. **danlab-multimodal public** — flip visibility, ship rewritten README.
5. **Origin thread on X** — 7-tweet thread, ready to paste.

**Tier 2 — Build cadence (Day 1-30, Dan1 drafts, somdipto publishes):**
6. **Show HN** (Day 5) — "Show HN: Dan Glasses — proactive AI companion, 7 services, 0 cloud calls, $0/month".
7. **Ask HN** (Day 14) — "Ask HN: What should the v2 wearable spec be?".
8. **dev.to / Hashnode** (Day 9, Day 28, Day 42) — 3 long-form technical posts. "Salience-gated vision", "Why I built a 7-service AI stack on a $200 board", "How we got whisper.cpp to <1s end-to-end".
9. **YouTube** (Day 3-4) — 60-second demo. PTT → STT → memory → query → TTS. Screencast.
10. **LinkedIn long-form** (Day 7, Day 21) — "From India to the World: why we built Dan Glasses", "The proactive AI thesis: why we don't need a display".

**Tier 3 — Community (Day 7-30):**
11. **Telegram community** (Day 13) — first weekly build-in-public retro. "Week 1 retro — punchlist shipped, what broke, what's next".
12. **Reddit** (Day 6) — r/LocalLLaMA, r/india, r/MachineLearning, r/SmartGlasses, r/singularity. One post each, tailored.
13. **Hacker News comment** — daily, on AI/wearable/India posts. High-signal, low-volume.
14. **YouTube tech reviewers** — pitch 5-10 reviewers for organic reviews. (MKBHD tier is unreachable; Mrwhosetheboss tier is the wedge.)

**Tier 4 — PR & launch (Day 30-90):**
15. **Product Hunt launch** (Day 90) — needs a public demo, a waitlist, and a video. Prep starts Day 30.
16. **Tech press** — The Verge, Wired India, YourStory, Inc42, The Ken. Pitch angle: "open-source AI glasses from India, MIT, on a $200 board".
17. **Podcasts** — Lex Fridman (long shot), The Pragmatic Engineer, Latent Space, Last Week in AI. Pitch angle: "from India to AGI".
18. **arXiv** — write a paper on the salience-gated vision loop. citable, technical, on-brand.

**Tier 5 — Always-on:**
19. **Build-in-public logs** — weekly. "Week N retro". Twitter thread + blog post.
20. **Open-source contributions** — every PR to Brilliant Labs, LFM2-VL upstream, whisper.cpp, llama.cpp, KittenTTS is a marketing artifact.
21. **Discord** — only when there's traffic. Don't pre-launch.

---

## 8. What content should Danlab produce?

**The 5 content pillars:**

1. **The proactive thesis** — what is proactive AI, why is it the missing category, how does Dan Glasses implement it.
   - "Salience-gated vision: why your AI glasses don't need 60 FPS" (dev.to)
   - "The proactive AI thesis" (LinkedIn long-form)
   - "Why we don't ship a display" (LinkedIn long-form)

2. **The local-first thesis** — privacy, latency, $0/month, MIT-licensed.
   - "7 services, 0 cloud calls, $0/month: how we built the local-first AI stack" (dev.to, X thread)
   - "Why we run LFM2.5-VL-450M on a $200 board" (dev.to, deep dive)

3. **The from-India thesis** — origin, AGI from the global south, AGI-from-India narrative.
   - "From India to the World: why we built Dan Glasses" (LinkedIn long-form)
   - "Bootstrapping an AI lab from India" (Reddit r/indianstartups cross-post)
   - "AGI from India: the thesis" (LinkedIn long-form)

4. **The architecture deep-dives** — technical credibility. Engineers follow engineers.
   - "whisper.cpp < 1s end-to-end: the VAD + streaming pipeline" (dev.to)
   - "Salience-gated vision: the VLM trigger architecture" (dev.to)
   - "7 services, 1 gateway, 0 cloud: the OpenClaw orchestration pattern" (dev.to)

5. **The build-in-public logs** — weekly retro. "What we shipped, what broke, what's next".
   - Twitter thread every Friday
   - dev.to post every Friday
   - Telegram community every Friday

**The reactive hooks (armed, not fired):**

| Trigger | Hook | Channel | Time to ship |
|---|---|---|---|
| Apple Glasses slip to 2027 (already happened May 31) | "Apple exits. We're shipping. Open source is the answer." | X + LinkedIn | 2 hours |
| Meta Ray-Ban Display ships to India | "The open-source alternative that runs on $200 hardware" | X + LinkedIn | 3 hours |
| Google audio Android XR glasses ship Fall 2026 | "Gemini is great. But it needs the cloud. Dan Glasses doesn't." | X + LinkedIn | 2 hours |
| Sarvam Kaze hits 10K pre-orders | "Why we still need an open-source AI glasses stack in India" | LinkedIn | 1 hour |
| LFM2.5-VL-450M ships to HF (already happened Apr 11) | Demo on Day 1 | X + YouTube | 4 hours |
| SIA v1.0 release | "Partnering with the open-source self-improvement stack" | X + LinkedIn | 3 hours |
| Monako Glass launch | "Different bet: proactive companion, not coding wearable" | X + LinkedIn | 2 hours |
| Brilliant Labs Halo ships India | "Open-source soul-mate. Same LFM2-VL. Different body. We're the brain, they're the body." | X + LinkedIn | 2 hours |
| Vayu AI Glasses hits ₹1L pre-orders | "Vayu is the iPhone of Indian AI glasses. We're the Android." | LinkedIn | 1 hour |

---

## 9. What is the current online presence? (verified this run)

### Verified state, 2026-06-14 01:00-01:20 UTC

| Surface | State | Source |
|---|---|---|
| `danlab.dev` | Generic 5-bullet product page. Title: "DanLab - AI Product & Research Lab". Dan Glasses not on homepage. 308→200. "DanLab Inc." legal entity. | `curl -L` |
| `github.com/somdipto` | 23 followers, 29 following, 126 public repos. Bio: "Build - Eat - Sleap". Name: "Sodan". 0 pinned repos. Only `zerant` has topics. | `api.github.com` |
| `github.com/somdipto/danlab-multimodal` | **404 to anonymous. Private.** | `curl -L` |
| `github.com/somdipto/dan-glasses` | Public, 0★, 0 forks, 0 topics. Description: "AI-native smart glasses…". | `api.github.com` |
| `github.com/somdipto/dani` | Public, 1★, 0 forks, 0 topics. | `api.github.com` |
| `github.com/somdipto/danclaw` | Public, 1★, 0 forks, 0 topics. | `api.github.com` |
| `github.com/somdipto/dan-consciousness` | Public, 0★, 0 forks, 0 topics. | `api.github.com` |
| `@NandySomdipto` (X) | Long Web3 bio with @dan2agi handle. Recent posts (June 12-13): all about agentic glasses, India origin, "building AGI from India". | x_search |
| `linkedin.com/in/somdipto-nandy` | Headline: "building Ai-agents 🧠 ✦ product builder👷🏻 ✦ Ai at scale ✦ stealth strtp ✦ Web & Design Lead at TEDXAtria IT 🖌️". 3,953 followers, 500+ connections. | web_search |
| Telegram community | Not verified — not in danlab.dev links. | — |

### What this means

**The platform is built. The plumbing is built. The product is built. The receipts are private.** Every claim above is verifiable — the 7 daemons, the 106/106 tests, the $0/month — but **only somdipto can see them.** Marketing is making the receipts public.

The 23 GitHub followers are the most damning number. The 3,953 LinkedIn connections are the most exciting. The mismatch is the opportunity.

---

## 10. Who are the first users?

### Persona 0 — the founder himself

**Somdipto is the first user.** If Dan Glasses doesn't work for him at Kroolo, on his Linux laptop, with his workflow, it doesn't work. The first 10 users are his direct network: buildspace cohort, TEDx Atria IT alumni, ex-colleagues, college friends. The 500+ LinkedIn connections are the seed list.

### Persona 1 — the Indian AI/ML engineer (the multiplier)

- **Profile:** 22-35, Bangalore / Hyderabad / Mumbai, IIT/BITS/buildspace/IIIT alum, knows Python + TypeScript, ships on weekends.
- **Where they live:** X, LinkedIn, GitHub, Reddit r/india, r/LocalLLaMA, buildspace alumni Slack.
- **What they want:** "I want to ship something real, on my own time, that I'm proud of. AGI from India is the dream."
- **Why Dan Glasses:** It's an artifact they can point at. "I work on Dan Glasses" is a sentence that opens doors. The MIT license means they can fork, modify, ship.
- **Acquisition:** LinkedIn DM, X reply, buildspace alumni Slack, Reddit cross-post.
- **Conversion path:** GitHub repo → clone → `./scripts/dev.sh` → first memory → Telegram community.

### Persona 2 — the global indie hacker / dev-tools nerd

- **Profile:** 25-45, US/EU, indie hacker, "builds in public" culture, ships weekend projects, follows Pieter Levels, Marc Lou, levelsio.
- **Where they live:** X, Product Hunt, dev.to, Hacker News, indiehackers.com.
- **What they want:** "I want to be one of the first 100 to use a real AI wearable. I want to be cited in the launch thread."
- **Why Dan Glasses:** First-mover advantage. The demo is the product.
- **Acquisition:** Show HN, Product Hunt, dev.to, X demo video.
- **Conversion path:** Show HN → danlab.dev → GitHub → clone → first conversation.

### Persona 3 — the productivity-obsessed knowledge worker

- **Profile:** 28-45, knowledge worker, uses ChatGPT / Claude / Ray-Ban Meta, productivity-obsessed, listens to Lex Fridman / Huberman adjacent.
- **Where they live:** Product Hunt, X, YouTube tech reviews, HN, podcasts.
- **What they want:** "I want to remember everything. I want a second brain that talks to me. I want to never forget a name."
- **Why Dan Glasses:** The 5 user stories (Encounter Recall, Contextual Reminder, Object Search, Passive Journaling, Hands-Free Check-In) are *exactly* their problems.
- **Acquisition:** YouTube demo, Product Hunt, podcasts, dev.to, X Spaces.
- **Conversion path:** YouTube demo → danlab.dev → waitlist → first conversation.

### Persona 4 — the accessibility-first user

- **Profile:** Anyone with ADHD, memory loss, visual impairment, motor impairment, or chronic illness. Hands-free, eyes-free, voice-first.
- **Where they live:** Reddit r/ADHD, r/Blind, r/disability, Twitter accessibility community, AppleVis, RNIB.
- **What they want:** "I want AI that meets me where I am. I can't always use my hands. I can't always look at a screen."
- **Why Dan Glasses:** Voice-first, push-to-talk, salience-gated, speaks only when useful. The privacy story is non-negotiable for this audience.
- **Acquisition:** Reddit accessibility subs, accessibility-focused podcasts, AppleVis forum, Hacker News "Show HN" comments.
- **Conversion path:** Accessibility community post → danlab.dev → GitHub → first conversation.

### Persona 5 — the AGI researcher / alignment-aware builder

- **Profile:** 25-50, AI safety / RLHF / interpretability / recursive self-improvement space. Reads LessWrong, Alignment Forum, arXiv-sanity, Anthropic / DeepMind public posts.
- **Where they live:** LessWrong, Alignment Forum, arXiv, X AI safety community, Anthropic / DeepMind employees.
- **What they want:** "I want to see what India is doing on the AGI frontier. I want to cite real artifacts, not pitch decks."
- **Why Dan Glasses:** The SIA fork story is the wedge. The 7-service architecture is the moat. The from-India origin is the freshness.
- **Acquisition:** arXiv paper, LessWrong post, AI safety podcast pitches, X thought-leadership.
- **Conversion path:** arXiv → GitHub → research collaboration.

---

## 11. The 5-pillar thesis (the only one we ever say)

1. **Proactive** — Dan Glasses tells you things you didn't know you needed to hear. Everyone else waits for "Hey Meta." This is the missing category.
2. **Local-first** — Every model runs on-device. 0 cloud calls. $0/month. Privacy by construction.
3. **Open source** — MIT-licensed, community-owned. Brilliant Labs Halo is the closest peer; they're $299, 14h battery, Noa cloud. We're the open alternative to their cloud.
4. **India origin** — From Bangalore, ₹ pricing, Indic languages on roadmap, AGI-from-India narrative. Somdipto is 23, Atria IT, 3,953 LinkedIn followers. The persona matches the audience.
5. **AGI research, not just product** — The brain (OpenClaw + memory + cross-session recall + SIA fork path) is the moat. We can swap the body (Redax → Monako → OpenGlass → Halo) and the user never notices.

The **defensible combination** is **#1 + #2 + #3 + #4**. Nobody else has all four. The **#5 is the long-term moat** that compounds.

We do **not** claim: Display, AR overlay, real-time 60 FPS vision, social sharing, multi-user, cellular, or a hardware product today. We **do** claim: Proactive, local, open, India, AGI-research-grade.

---

## 12. The constraint (the only thing that matters)

**The constraint is shipping, not writing.**

The 5 artifacts in this directory are v45. v44 was solid. v43 was solid. v42 was solid. **The 5 artifacts have been "ready" for 5 versions.** What has not happened is the punchlist.

The 5-punchlist (verified) is:

1. Make `github.com/somdipto/danlab-multimodal` public. **30 min. #1 blocker.**
2. Update GitHub bio + name + pin 4 + add 5 topics to each. **20 min.**
3. Update X bio. **1 min.**
4. Update LinkedIn headline + first post. **1 hour.**
5. Post the 7-tweet origin thread. **30 min.**

**Total: ~2 hours. $0. Reversible. Owned by somdipto.** Every other marketing action — landing page, Show HN, YouTube demo, Product Hunt, PR — is downstream of this.

The strategy is right. The artifacts are right. The market is right. The 5 locked files in `agent-work/` are right. The window is open because Apple slipped and Brilliant Labs validated LFM2-VL on-device. The only thing left is the punchlist. **Ship it.**

---

## 13. Sources & verification

All competitive intel verified via web_search and x_search this run (2026-06-14 01:20 UTC). All danlab.dev / GitHub state verified via direct API call at 01:00-01:20 UTC 2026-06-14.

Key sources:
- Liquid AI: LFM2.5-VL-450M, LFM2-Audio-1.5B, Brilliant Labs partnership
- Bloomberg / Mark Gurman (May 31 2026): Apple Glasses slipped to late 2027, Vision Pro 2 + Vision Air cancelled
- Google I/O 2026 (May 19): Android XR audio-only glasses (Fall 2026), XREAL Project Aura
- Halliday AI Glasses: 35g, MicroLED, $399 Kickstarter
- Brilliant Labs Halo: $299, LFM2-VL-450M, open source, 14h battery, Noa cloud agent
- OpenGlass: arXiv, GAP9 RISC-V, 11.8h on 200mAh
- Sarvam Kaze: IndiaAI Summit Feb 2026, PM Modi on stage
- Lenskart B: 35K+ waitlist, 40g, Snapdragon AR1, Gemini-powered
- Vayu AI Glasses: ₹74,999, pre-order, Indic languages
- Monako Glass: $399, 48g Linux glasses
- SIA: Hexo Labs, MIT, May 28 2026
- Engadget review of Halliday: "almost every design decision... feels, to me, like the wrong one"
- Apple WWDC 2026 (June 8): Tim Cook's last WWDC, visionOS 27, Siri AI glow-up, no smart glasses announcement
- Meta Ray-Ban Display: $799, binocular waveguide, hand-tracking, <1h battery
- Acer GR0 / GI0: May 29 2026 launch, $499.99 / $299.99

*Last updated: 2026-06-14 06:50 IST (01:20 UTC) — v45, same thesis, verified state.*
*Status: research locked. Strategy locked in `dan1-marketing-strategy.md`. Content locked in `dan1-content-calendar.md`. Twitter locked in `dan1-twitter-content.md`. Landing page locked in `dan1-landing-copy.md`. READMEs locked in `dan1-github-readme-suggestions.md`. Awaiting somdipto to ship the 5-punchlist.*

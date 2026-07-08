# Danlab Marketing Research — v1

**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Date:** 2026-07-04
**Status:** Research complete. Five artifacts built. See `/dan-glasses/agent-work/dan1-marketing-strategy.md` and siblings.

---

## TL;DR — The Five Things That Matter

1. **The story is real, but it's not on the website yet.** The actual workspace has Dan Glasses, danlab-multimodal, Dani, Paperclip/DanClaw, and a $349 BOM AI-glasses plan. The public `danlab.dev` shows a generic "Agent8 / Zerant / Dapify" lineup. **Brand–reality gap is the #1 marketing problem.**
2. **"Proactive AI companion, not reactive assistant" is a defensible wedge.** Ray-Ban Meta is capture+share (reactive). Vision Pro is display-overlay (reactive). Brilliant Labs Halo, Even Realities G1, and Vayu are capture-utility (still mostly reactive). Dan Glasses is the only one explicitly designed for *salience-gated proactive memory*. That's a real category, and we own the words.
3. **The India origin is an asset, not a liability.** Sarvam Kaze just launched at the AI Impact Summit 2026. Vayu, B by Lenskart, and several others are in market. We are not first — but we are the only India-origin team building *open-weights, on-device, no-cloud-required* AI glasses. That distinction is publishable.
4. **The competition is moving toward cloud-locked, paywalled, display-first.** Meta added a $20/mo paywall for Conversation Focus (v13 research). Apple Vision Pro head left for OpenAI. Google + Samsung Android XR is on-device but Android-ecosystem-locked. **"Local, open, owned by the user" is the wedge the field is leaving open.**
5. **We have a working open-source demo, but it's not viral yet.** danlab-multimodal is a real, runnable sub-250MB VLM with a heuristic feedback loop. The narrative is publishable. The post hasn't been written.

---

## 1. What is Dan Glasses?

**Product:** Wearable AI companion. Glasses form factor (Redax aarch64 target) with a desktop companion form factor (Linux laptop + USB camera) as the v1 buildable artifact. Always-on sensing — voice + vision + memory + TTS — with **salience-gated output** (the device only speaks when it has something worth saying).

**Vision:** A persistent, context-aware AI agent that perceives the world through vision and hearing, thinks silently, and speaks back only when needed. Not a notification mirror. Not a camera with a speaker. **A cognitive extension.**

**Target user (v1):** Technical early adopters, productivity-obsessed knowledge workers, accessibility-first users, researchers building the open AI stack. People who want AI that *works with them*, not just *responds to them*.

**Core value proposition (the line, in one sentence):**
> *"What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?"*

**The five user stories that prove the shape (from the PRD):**
- **Encounter recall** — "I met Priya yesterday. What did we talk about?" (memory + named-entity recall)
- **Contextual task reminder** — "I walked past the pharmacy 3 times this week. Remind me next time."
- **Object search** — "Where did I leave my keys?" (perception pipeline + memory)
- **Passive journaling** — "What did I do on Tuesday that was different from usual?" (continuous capture + summarization)
- **Hands-free check-in** — "My hands are in dough. Any urgent emails?" (PTT + memory + tool calls)

**Tech stack (locked):**
- Vision: LFM2.5-VL-450M (Q4_0 GGUF) via llama.cpp, 209MB
- STT: whisper.cpp base.en via whisper-cpp-plus-rs (async + Silero VAD), 74MB
- TTS: KittenTTS medium (expr-voice-2-m), ~25MB
- Orchestration: OpenClaw (TypeScript/Node) — gateway + MCP tools
- Frontend: Tauri v2 + React 19 + Vite 7
- Camera: V4L2 + CrabCamera (with mock fallback for dev)
- Memory: SQLite + MiniLM-L6-v2 (384-dim) + in-process flat vectors
- Packaging: .deb + systemd
- Models: downloaded on first run (don't bloat the .deb)

**Status (verified via dan1.md, dan2.md, 2026-07-04):**
- Tauri v2 app: shipped, published at `https://dan-glasses-app-som.zocomputer.io`
- OpenClaw gateway: live, 8 plugins, 63 commands
- Services running: audiod, memoryd, perceptiond, toold, ttsd, os-toold, openclaw, dan-glasses-spa, tailscaled (no auth yet)
- audiod v1.3: ship-ready, 160 tests passing
- perceptiond: LFM2.5-VL-450M Q4_0 running, watchful/active/idle modes live, 8/8 tests
- memoryd: SQLite + MiniLM-L6-v2, persistent DB
- toold: sandboxed shell+python+registry, v0.2.0
- ttsd: KittenTTS medium, expr-voice-2-m voice
- **Bottleneck: Redax aarch64 hardware not finalized. Track B (wearable) is blocked. Track A (desktop prototype) is demo-ready.**

---

## 2. What is the user workflow?

### Track A (Desktop Prototype — Buildable Now)

**Step 1: Unbox + install**
- Download `.deb` (or run `./scripts/dev.sh`)
- Bootstrap wizard launches: camera permission, model download, language preference, Telegram pairing
- Idempotent installer: upgrades don't delete memory
- Models: LFM2.5-VL-450M (209MB), whisper base.en (74MB), KittenTTS (~25MB), MiniLM-L6-v2 (80MB)

**Step 2: First run**
- Tauri v2 app opens
- VisionDashboard tab: mode set to "watchful" (5 FPS, salient-gated)
- audiod waiting on push-to-talk (PTT, default hotkey: space)
- TTS primed, memoryd hydrated

**Step 3: Daily use**
- Walk into a room, talk to a person, work at your desk
- Camera captures at 5 FPS; only salient frames (motion OR face detected) trigger VLM inference
- VLM produces a text description → stored in memoryd (with embedding)
- Push-to-talk: hold space, ask "what did Priya say about X?"
- audiod transcribes → OpenClaw routes → memoryd semantic search → response → KittenTTS speaks

**Step 4: Memory builds**
- After a day, you have hundreds of episodic memories (with embeddings)
- End-of-day summary is available via voice
- Next morning: "what did I do yesterday?" returns a real answer

**Step 5: Optional Telegram control**
- `/mode watchful` switches power state
- `/query what did I say about X` returns text-based recall
- Voice stays the primary channel; Telegram is the phone-friendly control surface

### Track B (Wearable — Hardware-Blocked)

Same loop, but:
- Redax aarch64 board, 2x 200mAh batteries, USB-C, JBD MicroLED (per AGENTS.md note)
- Push-to-talk → wake-word (planned v1.5)
- 4hr battery target at 5W average
- Thermal fallback: drop LFM2.5-VL-450M → Gemma3-2B at 42°C
- All services run as isolated Rust binaries on aarch64; same code, different build target

### The "Aha" Moment

The first time the user asks Dan Glasses "where did I leave my keys?" and gets a real, useful answer based on what the camera saw 20 minutes ago. **The moment they realize this is a memory, not a tool.**

---

## 3. Who is the competition?

| Competitor | What they are | What they get wrong | Dan Glasses wedge |
|---|---|---|---|
| **Ray-Ban Meta** (Gen 2, $299, Meta AI) | Capture + share + reactive voice assistant | Cloud-only, $20/mo paywall for Conversation Focus, no proactive memory, no on-device inference | On-device VLM, salience-gated, open-weights |
| **Apple Vision Pro** ($3,499) | Spatial computing display, AR overlay | Heavy, expensive, no proactive AI, not all-day wearable | <50g glasses, $349 BOM, all-day |
| **Google + Samsung Android XR** (May 2026) | On-device Gemini in Android glasses | Android-ecosystem-locked, Google-cloud-influenced, no open memory | Open memory, local SQLite, user owns everything |
| **Brilliant Labs Halo** (with Noa) | AR overlay + voice AI | Display-first, cloud-dependent for Noa | No display, salience-first, local |
| **Even Realities G1** ($399) | Display-only glasses (notifications + nav) | No AI, no memory, no proactive behavior | AI + memory + proactive |
| **Snap Specs** ($2,195) | AR glasses for creators | Capture+share, expensive, not always-on | Cognitive extension, not creator tool |
| **Sarvam Kaze** (India, AI Impact Summit 2026) | India-origin AI glasses | Cloud-dependent, India-language focus only | Open-weights, on-device, India + global |
| **Vayu AI Glasses** (India, ₹74,999) | India-market AI glasses, profession editions | Cloud AI, profession-locked (medical/legal) | Open, general-purpose, on-device |
| **B by Lenskart** (India, Peyush Bansal) | Smart glasses with Meta AI | Meta-cloud-dependent, no India-language model | Local inference, open |
| **Panda / Blurr** (Android UI agent) | Phone operator, UI automation | Phone form factor, not wearable | Glasses form factor, always-on sensing |

### The Wedge, Compressed

**The 2026 AI-glasses market has converged on "display + cloud + reactive."** Dan Glasses is the only project in the field publicly committing to *always-on, salience-gated, on-device, open-weights, user-owned memory*. That is a category, not a feature. We can own the words.

**Open questions for somdipto:**
- Do we want to lean into "open-source" as the primary message, or "on-device privacy" as the primary message? (My read: privacy first, openness second, ownership third — matches the v13 research)
- Do we go head-to-head with Meta on the "cloud vs. local" frame, or do we ignore Meta and lead with the India story? (My read: lead India + AGI research; let the open-weights wedge do the rest)

---

## 4. What is danlab-multimodal?

**Project:** A hackathon-built (H2 2025) sub-250MB VLM pipeline with a **heuristic feedback loop** running on CPU via llama.cpp. Built to prove: *small, fast, fully local, multimodal AI is possible in 2026.*

**What it does:**
```
Screen → VLM inference (SmolVLM-256M Q4_K_M) → heuristic feedback score → suggestion → loop
```
- Screen capture: scrot (or synthetic images when headless)
- VLM: SmolVLM-256M (120MB) + SigLIP mmproj (182MB) via llama-mtmd-cli
- Heuristic scorer: length penalty, error detection, content quality bonus
- ~26–32s per image on CPU

**What it actually is (honest framing):**
- A hand-coded heuristic loop, not reinforcement learning
- No model weights modified, no policy gradient, no learned reward
- **Pre-RL scaffold** — the credible path to true RL is the SIA framework (Hexo Labs, MIT, May 2026)
- Per the README: "We will not claim 'RL' until the harness+weights modification is open and auditable."

**Why it matters as a marketing asset:**
1. **It's a real, runnable demo.** Anyone with a Linux box can reproduce it. The honesty about the heuristic (not overclaiming RL) is itself a brand asset.
2. **It positions us on the "small-beats-large" trend.** Liquid's LFM2.5-230M, Sapient's HRM-Text-1B, Nous Research's Hermes Agent — the small-model SOTA is real, and danlab-multimodal is on the right side of it.
3. **It is a research artifact, not a product.** That distinction is important for the AGI-lab narrative.
4. **Live at:** `https://zo.pub/som/danlab-multimodal-demo` (asciinema cast + docs)

**The narrative:** "We built a sub-250MB multimodal AI on a CPU, ran a heuristic feedback loop, and shipped it. We told you when it wasn't RL. We're working on the SIA port to make it real RL. From India. Open."

---

## 5. What is Paperclip / DanClaw?

**Paperclip:** An AI-agent company orchestration platform — multi-agent coordination, issue tracking, goal management, deployment. Express + TypeScript + PGlite/Postgres + Vite React UI + MCP server.

**Status (per paperclip/AGENTS.md):** **Dormant.** All agents paused. Resume when ready.

**DanClaw** (per the README): Cloud-hosted fork of Paperclip, branded under the danlab ecosystem. "If OpenClaw is an _employee_, DanClaw is the _company_." One-command Docker / Railway / Fly.io deploy. Production at `https://paperclip.up.railway.app`.

**What it does for the marketing story:**
- It is *infrastructure for AI agent companies* — a meta-product that fits cleanly with "AI research and product lab"
- It is the one danlab project that is **immediately deployable** (vs. Dan Glasses which is hardware-blocked)
- It is **the most boring** of the four projects — a real product for real teams, not a moon shot

**My read:** Paperclip/DanClaw is currently a distraction from the marketing story. It is the kind of project that looks impressive on a corporate slide but does not generate narrative momentum. **My recommendation: mention it in the danlab.dev ecosystem page, but do not lead with it.** Lead with Dan Glasses + danlab-multimodal (story) + Dani (the agent brain, which IS the AGI story).

**Open question for somdipto:** Is DanClaw/Paperclip still part of the active roadmap, or is it a one-time fork we keep alive for goodwill? My read: keep the repo, drop it from the headline.

---

## 6. What is the overall Danlab story?

**The current website (danlab.dev)** is generic:
- "Agent8" — no-code AI agent builder
- "Zerant" — AI mobile browser
- "Dapify" — Web3 dev studio
- "AI Glasses" — described as "next-gen AR glasses powered by multimodal AI overlays"

**None of those product names exist in the actual workspace.** The workspace is:
- Dan Glasses (wearable AI companion)
- danlab-multimodal (sub-250MB VLM + heuristic loop)
- Dani (the agent brain, on GitHub)
- Paperclip/DanClaw (orchestration, dormant)

**This is a brand crisis masquerading as a website.** The public site does not match the real work. The public site describes products that don't exist (Agent8, Zerant, Dapify) and misses the ones that do (Dan Glasses, Dani, danlab-multimodal).

### The narrative arc (what the story should be)

**Act 1 — Origin (now → Q4 2026):**
Two co-founders (somdipto nandy + Dan, an AI agent) in Bengaluru, building toward AGI from India. Open-weights, on-device, no-cloud-required. The first project: Dan Glasses, a wearable AI companion that doesn't need the cloud to remember your day. The demo runs today on a Linux laptop with a USB camera.

**Act 2 — Demo (Q4 2026 → Q1 2027):**
Ship the desktop prototype as a downloadable .deb. Open-source the perception pipeline. Publish the LFM2.5-VL-450M + SalienceDetector integration as a reference architecture. Land the wearable form factor when Redax hardware is final.

**Act 3 — Wearable (Q1 2027 → Q3 2027):**
The first India-origin AI glasses with on-device, salience-gated, user-owned memory. Priced for accessibility (target $349 BOM). Open-weights, no cloud lock-in. Direct challenge to the Meta/Apple/Google frame.

**Act 4 — Research (parallel, ongoing):**
Ship the SIA port (when ready), the danlab-multimodal RL upgrade, the Memora + As We May Search memory architecture. Publish to arXiv. Target ICML/ACL 2027. **Danlab is a research lab, not just a product company.**

### The "From India to the world" line

India is a *constraint and a feature*, not a gimmick:
- Constraint: 1B+ mobile users, real accessibility needs, multilingual reality
- Feature: India has not been first to the AI-glasses market. The "open, local, owned by the user" position is one the incumbents will not copy because it does not serve their lock-in business model
- The line: "Sarvam builds for India. Vayu builds for India. We build for India AND the world — and we open-source everything so anyone can build on it."

**The story is publishable. The website is not telling it.**

---

## 7. What marketing channels make sense?

### Tier 1 (do these now)

**X / Twitter** — The primary surface for AI/ML community reach. somdipto's handle is @Shodan_s. Danlab needs a dedicated account (`@danaboratory` is the obvious one — verify availability).
- Daily: research updates, build progress, demos
- Weekly: longer thread on a research direction
- Monthly: a major announcement (model release, paper, milestone)
- **Lead with: actual research, not product marketing**

**GitHub** — The credibility surface. Every repo needs to be tight.
- somdipto/dani, somdipto/dan-lab, somdipto/dan-consciousness, somdipto/paperclip, danlab-multimodal
- **Top priority:** polish the READMEs (see `dan1-github-readme-suggestions.md`)
- **The org description on GitHub matters.** Currently generic. Should be: "AI research and product lab. Building toward AGI from India. On-device, open-weights, user-owned."

**HuggingFace** — For model releases. SmolVLM-256M fine-tunes, heuristic-loop-trained models, LFM2.5-VL-450M extensions all belong here.

### Tier 2 (build in Q3-Q4 2026)

**arXiv** — For the SIA port paper, the danlab-multimodal RL upgrade, the memoryd architecture paper. Target: 1 paper by end of Q3, 2 by end of Q4.

**Dev.to / Hashnode** — Long-form technical posts. The "sub-250MB VLM on CPU" tutorial. The "SalienceDetector design" deep-dive. The "open-weights wearable AI is possible" manifesto.

**YouTube** — Demo videos. 2-minute danlab-multimodal demo. 5-minute Dan Glasses desktop prototype walkthrough. No talking-head vlogs. Just screens, models, and code.

### Tier 3 (later, when there is something to point at)

**Product Hunt** — When the desktop prototype .deb is genuinely shippable to non-developers (Q1 2027).

**Reddit** — r/LocalLLaMA, r/MachineLearning, r/embedded. Only when we have a real technical contribution (not marketing).

**LinkedIn** — For the India AI ecosystem (Sarvam, Vayu, Lenskart, AI4Bharat). Not the primary surface.

**Press / podcasts** — Stratechery, Latent Space, the AI Daily Brief, Pragmatic Engineer. Only after the arXiv paper is out.

### Channels that do NOT make sense (yet)

- TikTok / Instagram Reels — wrong audience
- Paid ads — wrong stage
- Conferences in 2026 — wrong year (ICML/ACL 2027 is the target)
- Discord — premature; needs an existing community to host

---

## 8. What content should Danlab produce?

### The 10 essential content pieces (in order of priority)

1. **The Dan Glasses landing page** — Hero, problem, what it does, why it matters, CTA. (See `dan1-landing-copy.md`.)
2. **The "What is Danlab" manifesto** — 1500 words, the origin story, the AGI thesis, the open-weights commitment. Lands on danlab.dev/about. Cite the dan-consciousness repo.
3. **The danlab-multimodal technical post** — "How we built a sub-250MB VLM on a CPU." Code, diagrams, the honest framing about heuristic vs. RL. Dev.to + HuggingFace blog.
4. **The SalienceDetector design post** — "Why fixed-FPS vision is wrong, and what we did instead." Open-weights + open-research angle.
5. **The 5-user-story product page** — Each user story from the PRD gets its own section on the Dan Glasses landing page.
6. **The X bio + first 10 posts** — See `dan1-twitter-content.md`.
7. **The "From India to the world" tweet thread** — The origin story, the AGI thesis, the open-weights commitment. 8-10 tweets.
8. **The "We did not claim RL" honesty post** — 500 words on why we named it pre-RL scaffold. The credibility of this post is itself a brand asset.
9. **The AGI research roadmap post** — 6/12/24-month plan. Cite the dan2 research artifacts.
10. **The weekly build-in-public update** — Every Friday. What shipped, what didn't, what's next. somdipto writes; Dan1 edits.

### Content calendar (high-level, full version in `dan1-content-calendar.md`)

- **Mon:** research thread (X, long-form)
- **Tue:** build update (X, short)
- **Wed:** code drop (GitHub)
- **Thu:** paper reading note (X, 1 thread per paper)
- **Fri:** weekly build-in-public (X, blog if milestone)
- **Sat:** off
- **Sun:** community engagement only (replies, not original posts)

### What we should NOT produce

- Generic "AI is the future" content
- Product marketing that leads with features before story
- "We're hiring" posts (not yet)
- Any post that overclaims (no "RL" without weights modification, no "AGI" without a research artifact, no "first" without verification)

---

## 9. What is the current online presence?

### What I found

- **danlab.dev** exists. The site describes "Agent8", "Zerant", "Dapify", and "AI Glasses." None of these match the actual workspace. **This is the #1 problem to fix.**
- **GitHub:** `somdipto/dani`, `somdipto/dan-lab`, `somdipto/dan-consciousness`, `somdipto/paperclip`, `somdipto/blurr` (fork). The repos exist; the README quality varies (see `dan1-github-readme-suggestions.md`).
- **X / Twitter:** @Shodan_s (somdipto). No dedicated danlab account that I can verify. **Need to confirm with somdipto.**
- **Telegram:** @danlab_bot is live and connected to OpenClaw (per dan1.md).
- **HuggingFace:** No verified danlab profile.
- **arXiv:** No papers yet.
- **zo.pub:** `https://zo.pub/som/danlab-multimodal-demo` — exists, hosts the demo.
- **zo.computer:** `https://dan-glasses-app-som.zocomputer.io` — published Dan Glasses app.

### What I did NOT find

- Press coverage
- Podcast appearances
- Conference talks
- arXiv preprints
- Active X account for danlab
- HuggingFace organization page
- LinkedIn company page
- Discord / community

### The online presence reality

**Almost everything danlab has done is invisible.** The work is real. The demo is runnable. The Telegram bot is connected. The Tauri app is published. None of this is findable through normal channels. The 12 months of work (the dan1 scratch pad is at v120) is locked inside the workspace and the dan-consciousness repo.

**This is good news.** It means the work has not been mis-marketed, over-claimed, or diluted. It means the first public push can be coherent, sharp, and honest.

---

## 10. Who are the first users / customers?

### Profile: The Ideal Early Adopter (v1 desktop prototype)

**Primary: The technical early adopter**
- Demographics: 25-45, developer or researcher, Linux/macOS user, already runs local LLMs (Ollama, LM Studio, llama.cpp)
- Pains: Frustrated with cloud-only AI, privacy concerns, wants to own their data
- Where to find: r/LocalLLaMA, Hacker News, X AI/ML community
- What they need: a `.deb` that installs cleanly, a working Tauri app, an OpenClaw config they can fork
- **First 100 users: GitHub stars + Discord (if we make one) + early HN post**

**Secondary: The accessibility-first user**
- Demographics: any age, vision-impaired, mobility-impaired, or cognitive-load-sensitive
- Pains: existing AI assistants are too reactive, too verbose, too cloud-dependent
- Where to find: accessibility communities, r/blind, AppleVis, Be My Eyes community
- What they need: hands-free check-in (the dough story), named-entity recall, passive journaling
- **This segment is the moral case AND the wedge — lead with the Priya encounter story**

**Tertiary: The productivity-obsessed knowledge worker**
- Demographics: 30-50, knowledge worker, deeply uses AI tools, measures ROI
- Pains: context switching, forgetting what was discussed, repeating themselves
- Where to find: Hacker News, Stratechery readers, "tools for thought" community
- What they need: passive journaling, encounter recall, the "I walked past the pharmacy 3 times" story
- **This is the segment that will tell their friends**

### The "Not Yet" User

- **General consumer** — wrong stage. The .deb is too technical for non-developers. v2 wearable is the consumer product.
- **Enterprise** — wrong stage. No SSO, no SOC2, no admin panel. Wait for v2.
- **Government / defense** — interesting (Palantir + Nemotron, DoD GenAI.mil), but deferred. Not the wedge in 2026.

### The 100-User Plan (Q3-Q4 2026)

1. **First 10:** somdipto's network + the dan-consciousness contributors. Personal DMs. They install, they break it, they tell us.
2. **Next 40:** HN "Show HN" post, X thread, Dev.to cross-post. 1,000 installs target, 100 active users.
3. **Next 50:** targeted outreach to r/LocalLLaMA power users, accessibility advocates, open-source maintainers. Personal asks. Demos.

**By end of Q4 2026:** 100 active daily users, 1,000 installs, 5 public case studies.

---

## What this research tells us to do

1. **Fix danlab.dev** — the public site does not match the workspace. This is a 1-day rewrite.
2. **Launch @danaboratory on X** — the danlab handle is the missing surface. 1-day setup.
3. **Polish the GitHub org** — see `dan1-github-readme-suggestions.md`.
4. **Ship the Dan Glasses landing page** — see `dan1-landing-copy.md`.
5. **Write the manifesto + the danlab-multimodal post** — 1 week.
6. **Open the waitlist** — for v1 desktop + v2 wearable interest. Capture emails.
7. **Build the community slowly** — Discord only when 100 active users exist.

**The work is done. The story is not told yet. That is what we fix next.**

---

## Open questions for somdipto (blockers I need answers to)

1. **Brand: do we use "Danlab" or "DanLab" or "danlab.dev"?** I see all three in the workspace. Pick one. It matters for the logo, the domain, the GitHub org.
2. **Product naming: do we use "Dan Glasses" (current) or rebrand?** My read: keep "Dan Glasses" — it's distinctive, it has a soul, it's already in the PRD.
3. **The Agent8 / Zerant / Dapify / AI Glasses products on danlab.dev — what are they?** Are they real products I missed, or are they placeholders? If placeholders, they need to be replaced with the real story.
4. **X handle: do we own @danaboratory / @danaboratory / @danaboratorylab?** I need to verify and claim. I can do this work if you confirm.
5. **The AGI thesis: how public do we want to be about it?** The dan-consciousness repo is internal. The CONSCIOUSNESS.md is internal. Do we publish a public version of the manifesto?
6. **Is Paperclip still on the roadmap?** If yes, mention in the ecosystem. If no, archive and remove from the headline.
7. **Who is the first design partner for v2 wearable?** This matters for the Q4 2026 outreach.
8. **Budget: is there marketing budget, or is everything Dan1's time + free channels?** Free is fine; it just changes the timeline.
9. **Are we doing a "Show HN" post in Q3?** If yes, I need 2 weeks lead time.
10. **What is the relationship between Dani and Dan Glasses?** Dani is the agent brain; Dan Glasses is the wearable. Are they co-branded, separate, or one product?

---

*End of research report. See `dan1-marketing-strategy.md` for the action plan.*

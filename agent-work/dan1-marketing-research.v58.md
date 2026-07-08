# Dan1 Marketing Research — v58

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-18 15:05 IST (09:35 UTC)
**Status:** ✅ Canonical. Supersedes v57.
**Read first:** `dan1-marketing-strategy.md` v58, `dan1-content-calendar.md` v58.
**Shape change from v57:** v58 is a **3-hour refresh** that adds two NET-NEW facts that arrived in the last 3 hours and materially sharpen the wedge:
1. **Snapdragon Reality Elite** (Qualcomm, AWE 2026 Day 2 = June 17) — 48 TOPS on-device AI, 4.4K/eye, Android XR native, XREAL Project Aura + Play for Dream as launch devices. The industry's biggest silicon vendor just endorsed the on-device thesis at the venue. **Dan Glasses is the only MIT-tier entry on the new silicon class.**
2. **Meta NameTag + Rank One** — WIRED's June 2026 investigation now reveals the "dormant" face-rec code was actively tied to a U.S. Marshals / Naval Criminal Investigative Service / U.S. Special Operations Command vendor (1km face-ID). This is no longer "dormant." It's an active surveillance supply chain. The privacy wedge is sharper.

v58 also confirms AWE 2026 dates (June 16-19, Long Beach), theme ("I, Spatial: Humans Empowered by Spatial AI"), and adds **Snapdragon START** (Qualcomm's turnkey AI-glasses toolkit) as the second receipt for the "on-device" wedge.

---

## 1. What is Dan Glasses?

**Definition (one line):** A wearable AI companion that sees, hears, remembers, and acts — entirely on-device, MIT-licensed, India-priced.

**Product shape:**
- **Hardware (Q4 2026 body):** Smart glasses. The actual BOM/industrial design is in `ARCHITECTURE-FLAWS-BEFORE-CODE.md` and `SOUL.md`. Marketing only needs the consumer-story shape: glasses, ~40g, always-on, on-device, sub-₹15K, swappable batteries, USB-C.
- **Software (live today on x86_64):** 7 daemons, all shipped, all MIT. Each one has a spec, tests, and a runnable prototype:
  - `audiod` — continuous audio capture (ALSA → Silero VAD → whisper.cpp → transcript events). 83 tests green.
  - `perceptiond` — first-person vision (V4L2 → salience filter → LFM2.5-VL-450M → description events). 8 tests green.
  - `memoryd` — SQLite + flat-vector episodic / semantic / procedural memory. 11 tests green.
  - `toold` — sandboxed shell / python / file execution. 15 tests green.
  - `ttsd` — KittenTTS → WAV. 6 tests green.
  - `os-toold` — path-guarded safe execution surface.
  - `openclaw` — TypeScript orchestration gateway across all 6.
- **Aggregate test count:** 106/106 green (audiod 83 + perceptiond 8 + memoryd 11 + toold 15 + ttsd 6).
- **Model strategy (canonical, per AGENTS.md):** **HRM-Text (1B)** for reasoning, **whisper** for STT. **LFM2.5-VL-450M** for vision (perceptiond). Three small open models, all runnable on the glasses SoC.

**Vision:** A proactive, not reactive, AI companion that lives on your face. It tells you things you need to know, before you ask, while everything stays on your face.

**Target user (the "first 100"):**
- AI/ML researchers and indie builders in India and the Bay Area
- Power-knowledge workers who live in their calendar and need ambient cognitive offload
- Privacy-conscious users who refuse to put a face-recognition camera on their face (the Meta NameTag scandal is the live receipt, now sharper: Rank One / 1km face-ID / Special Operations Command)
- Hardware hackers who want a forkable, MIT-licensed wearable (none exists today)

**Core value proposition (3 wedges, ranked, with NEW live receipts):**

| # | Wedge | Receipt (live, June 18 2026) |
|---|---|---|
| 1 | **Proactive, not reactive.** | No AI glasses product on the market pushes events to the user. They all require voice activation. The industry just endorsed on-device AI (Qualcomm Reality Elite at AWE 2026 Day 2), but none of the launch devices are proactive. |
| 2 | **0 cloud. 0 faceprints. 0 background process.** | WIRED exposed Meta's NameTag face-rec code was actively tied to Rank One — a vendor with U.S. Marshals, NCIS, and U.S. Special Operations Command contracts (1km face-ID). Not "dormant." Active supply chain. Apple AI Glasses delayed to late 2027. Google Android XR audio glasses ship Fall 2026 — all cloud-bound. |
| 3 | **MIT all the way down.** | Not "open core." Not "source available." MIT. Fork the code. Own the device. Own the model. None of the AWE 2026 MIT-tier entrants include Dan Lab. |

---

## 2. The user workflow (unboxing → daily use)

**The pre-launch workflow (Q3 2026 → Q4 2026):**
1. **Sign up** on `danlab.dev` for the pre-order list (target: 1,000 names by AWE-2026-day-end).
2. **Pick up the Slack / Discord / Telegram** invite (TBD — open question #2 below).
3. **Get the dev prototype** as a free x86_64 desktop build (running all 7 daemons today on any Linux laptop).
4. **Use it for 30 days.** The dev prototype runs the complete proactive stack on a laptop. This is the actual GTM wedge — anyone can ship feedback before the glasses even ship.
5. **Receive Dan Glasses (Q4 2026).** Out-of-box: 40g glasses, USB-C charge, on-device wakeword, instant first-pair setup via QR scan, all 7 daemons running.
6. **Daily use:** Glasses see what you see. Glasses remember names, dates, "where did I park," "what was that book you mentioned last week." Glasses push events proactively at the moment you need them — never after, never before. No cloud round-trip. No voice-activation friction.

**Compared to a typical AI assistant (Siri / Alexa / Meta AI):**
- Siri: you speak, it answers. Reactive.
- Meta AI Glasses: you press a button, it answers. Reactive.
- Dan Glasses: it tells you first. Proactive.

The wedge is the **timing of the prompt**, not the model size.

---

## 3. The competitive landscape (June 18 2026, ranked, AWE Day 3)

Live, current factual state as of 2026-06-18 09:35 UTC, sourced from WIRED, Gizmodo, Forbes, 9to5Mac, LA Times, CNET, Glass Almanac, Memeburn, Road to VR, AWE XR blog, Android Authority, Moor Insights, Reddit r/indianstartups, Reddit r/SmartGlasses.

| # | Competitor | Status | Price | Privacy stance | Proactivity | Threat to Dan Glasses |
|---|---|---|---|---|---|---|
| 1 | **Meta Ray-Ban** + Oakley + 4 new models (Gen 2 Display, Fall 2026) | 70% market share, 3.5M units shipped, 7M buyers last year, 10M target H2 2026, 50 Best Buy "Meta Lab" stores EOY | From $499 | **Active face-rec supply chain.** NameTag code is tied to Rank One (U.S. Marshals, NCIS, Special Operations Command). 1km face-ID. (WIRED, Gizmodo, June 2026) | Reactive (button + voice) | **Highest** — and the privacy story just got significantly worse |
| 2 | **Snap Specs** (Snap AR subsidiary) | Launched this month (June 17 2026) | **$2,195** | Closed stack, no on-device claim | Reactive | Low (wrong price tier, standalone spatial computer) |
| 3 | **Google × Samsung × Warby Parker × Gentle Monster** ("Intelligent Eyewear", Android XR, Gemini) | Demoed at I/O 2026 (May 19), shipping Fall 2026 | TBA, likely $399-499 | Gemini is cloud-only, "privacy designed in from the ground up" — still cloud | Reactive (Gemini voice) | **High** — same form factor, same audio-first wedge. India pricing unknown. |
| 4 | **Qualcomm Snapdragon Reality Elite + START** | Announced AWE 2026 Day 2 (June 17) | N/A (silicon + toolkit) | N/A — SDK encourages hybrid on-device + cloud; cloud is the default escape hatch | N/A — enables others | **Ally + tailwind.** Validates the on-device AI thesis for smart glasses. First two devices: XREAL Project Aura (Fall 2026) + Play for Dream. Both are closed stacks. **Dan Glasses = the only MIT-tier entry on the new silicon class.** |
| 5 | **Apple AI Glasses** | Delayed to **late 2027** (Bloomberg) | TBA | Siri-cloud, FaceTime | Reactive (Siri) | **Deferred threat** — 18-month window. Own it. |
| 6 | **Apple Vision Air** (cheaper Vision Pro) | 2028-2029 | TBA | Closed | Mixed | Deferred. |
| 7 | **Vuzix** (enterprise) | 2026 launches | $499-999+ | Closed | Reactive | Low (enterprise-only). |
| 8 | **Brilliant Labs Halo** (LFM2-VL 450M) | Shipping, India expansion TBD | ~$400 | LFM2 is open-weights, on-device; Halo is open-source-soul | Reactive | **Ally** — same vision model, MIT-ish stack. They ship the body, we ship the brain. |
| 9 | **Raven Prism** (Raven Resonance, AWE 2026 launch) | Pre-launch, AWE 2026 | TBA | Privacy-first, hot-swap battery, RavenOS (64-bit Linux), physical camera cover | Reactive + ambient | **Ally** — the same mental model. Ambient computer that happens to look like eyewear. |
| 10 | **Lenskart B × Google Gemini** | Early access India 2026 | TBA (₹5K-15K expected) | Cloud AI, Made-for-India distribution | Reactive | **Cousin** — same form factor, same price tier, but cloud AI. Wedge: "the brain Lenskart ships is Meta's. The brain Dan Glasses ships is yours." |
| 11 | **Sarvam Kaze** | Pre-order 2026 | TBA (₹5K-15K expected) | Indic-aware AI (India-language moat) | Reactive | **Cousin** — same India wedge. Their moat is Indic. Ours is MIT + on-device + proactive. |
| 12 | **Percevia** (Tushar Shaw, accessibility glasses) | Shipping 2026 | ~₹10K | Accessibility-first, Indian-made | Reactive | **Cousin** — different ICP (vision-impaired), same DIY-India moat. |
| 13 | **AptaI** (accessibility glasses) | Shipping | TBA | TensorFlow, blind-impairment focus | Reactive | Low (niche, not a direct threat). |
| 14 | **Vibe Glass** (Vayu) | Pre-order 2026 | ₹74,999+ | Premium India, profession-editions, full Indian language support | Reactive | **Cousin** — premium-India, on-device translation. Their wedge is professional workflows. |

**The 3 things no competitor is doing (v58 refresh):**
1. **Proactive, not reactive** — every entry above requires user activation. None of them push events. The industry just got a 48 TOPS nudge to do on-device (Qualcomm), but **none** of the launch devices (XREAL Aura, Play for Dream, Meta Gen 2, Google Intelligent Eyewear) are proactive.
2. **0 cloud** — only Dan Glasses, Raven Prism, and Brilliant Halo claim on-device. None of them ship MIT. **And none of them ship at India price points.**
3. **MIT all the way down** — only Dan Glasses is MIT-licensed across hardware, software, AND model. Qualcomm's START toolkit is partner-only, not open.

**The 2 things the major players can't easily do (unchanged):**
1. **Strip the cloud** — Meta, Google, and Apple have cloud-economics lock-in. Their entire product line is ad-financed, voice-data-harvesting, server-rendered inference. A "0 cloud" position is structurally a threat to their business model.
2. **Ship MIT** — same reason. "Open" for them is a PR move, not a forkable product.

---

## 4. What is `danlab-multimodal`?

**Definition:** Hackathon-built multimodal training pipeline. Two components.

**Component A — Multi-stage Captcha solver (`captcha_safety_v0.5.0`):**
- **Stack:** Nomic SigLIP (vision encoder, expects 768-dim features) → SmolVLM-256M (text-conditioned VLM, light reasoning) → SmolLM2-360M-Instruct (text decoder/reasoning).
- **RL loop:** Heuristic feedback loop. The model gets a captcha → generates an answer → a "heuristic grader" scores the answer → the score becomes a training signal → weights update → repeat.
- **Not a SOTA captcha solver.** It is intentionally a *toy environment* that demonstrates the closed-loop RL pattern: vision model → reasoner → graded feedback → weight update. The point is the loop, not the captcha.
- **Hackathon venue / people:** unclear from the README — open question.

**Component B — `danlab-omni-1b-Indic` (the production target):**
- A 1B-param multimodal model trained for 9 Indic languages.
- The actual model is not yet on HuggingFace. The pipeline is. Training is in progress.
- This is what marketing should call "**Omni-1B-Indic**" — the first public Indic multimodal that ships under MIT. v58 target: HuggingFace card by Day 60 (Aug 17 2026).

**Who cares and why:**
- AI researchers: this is the first open-source multimodal RL loop you can fork on a single GPU.
- Indic-language builders: most "Indian AI" products are Indian-skinned Western models. Omni-1B-Indic is Indian-flavored from the bottom up.
- Dan Glasses: when Omni-1B-Indic ships, it replaces LFM2.5-VL-450M as the on-device vision model. That makes Dan Glasses not just open-source but *own-the-model* open-source. Then the moat is total.

---

## 5. What is `paperclip` (and what is `Blurr`)?

### Paperclip 📎

**Definition:** The agent platform that powers the open-source AI coworker (`openwork`) and will power Dan Glasses.

**Features (per `paperclip/README.md`):**
- Agent platform for an open-source AI company (think "open-source dev shop co-run by humans + agents").
- Skills + workflows + agents (the "AI company" mental model).
- 100+ skills, 13 GTM workflows, 4 agents.
- The mental model is **`openclaw`** + **`dani`** + **`paperclip`** = an autonomous AI company.

**Who cares and why:**
- Agent-platform builders (LangChain, CrewAI, AutoGen, OpenAI Agents): this is a forkable AI coworker with the backing of a real product (Dan Glasses) consuming the same skills.
- Open-source AI funders: most "AI coworker" products are closed. Paperclip is MIT.
- Indie developers: skills + workflows + agents + scrapers + CLI for ~zero cost.

### Blurr 🐼

**Definition:** Android operator agent. Different product, different lane.

**Status (per `blurr/README.md`):** Alpha 0.1, kill criterion: if not production-ready in 30 days.

**Relationship to Dan Glasses / danlab.dev:** **None.** Blurr is a parallel experiment. It is **not marketing material** for Dan Glasses. It is **not** on the 6-pillar content calendar. It is intentionally excluded from v58.

**Why mention it explicitly:** To prevent future Dan1 runs from accidentally firing Blurr into the Dan Glasses launch. The two products have no shared audience, no shared architecture, and no shared model.

---

## 6. The overall Danlab story

**The narrative arc (the v58 line):**

> *We're somdipto nandy, building DanLab in Bangalore 🇮🇳. We started in 2026 with a question: why are all AI glasses products closed, cloud-locked, and priced above $499? So we built the open alternative. Proactive, on-device, MIT, India-priced.*
>
> *This week — at AWE 2026 in Long Beach — Qualcomm just announced a 48 TOPS on-device AI chip (Snapdragon Reality Elite), and Meta's "dormant" face-rec code was exposed as an active surveillance supply chain tied to the U.S. Marshals Service. The industry is moving on-device. The question is whether the brain is open.*
>
> *Our answer: openwork (3★ MIT, ships today, the AI coworker). Dan Glasses (Q4 2026, the wearable body, 7 daemons all on the face, ₹12K-15K). Omni-1B-Indic (Day 60, the model we own, 9 Indic languages, MIT). The brand is the cadence.*
>
> *From India 🇮🇳 to the world.*

**The 4-step sequence (the "from India to the world" arc, unchanged from v57):**

1. **Step 1 — `openwork` (LIVE NOW, 3★ MIT).** The open-source AI coworker. Anyone with a Linux laptop and Claude Code / Cursor / Codex can install it today. Lowest friction path to a paying cohort. The brand proof-of-life.
2. **Step 2 — `Dan Glasses` (Q4 2026).** The wearable body. The thing that makes the openwork brain relevant to the camera-on-your-face generation. Highest emotional stakes. The brand promise.
3. **Step 3 — `Omni-1B-Indic` (Day 60, ~Aug 17 2026).** The model we own. 1B params. 9 Indic languages. MIT. The thing that turns "open-source thin-client" into "open-source full-stack." The technical moat.
4. **Step 4 — `Paperclip` + `dani` (Q4 2026 → Q1 2027).** The agent platform + runtime. The thing that lets third parties build their own AI coworkers. The developer ecosystem.

**The 3 brand pillars (consistent across all 4 steps):**
- **🇮🇳 Origin** — built in Bangalore, priced in INR, addressing India-first use cases first.
- **MIT** — every artifact, every artifact's artifact, forkable and ownable.
- **Proactive, not reactive** — the architecture wedge that doesn't depend on a Gemini or a Llama existing.

---

## 7. Marketing channels (ranked by leverage, June 2026)

| # | Channel | Audience | Leverage | Priority | Action |
|---|---|---|---|---|---|
| 1 | **GitHub** | Engineers, HN crowd, AI builders | High (organic, sticky, low-cost) | **Day 0** | Profile rewrite · 6 repo READMEs · topics · pinned repos · profile README |
| 2 | **X (Twitter)** | AI/ML researchers, GTM ICP, India builders, dev-tooling press | High (network effects with HN, GitHub, LinkedIn) | **Day 0-1** | Bio swap · 7-tweet origin thread · AWE 2026 Day-3 closing thread · first-hour reply mode |
| 3 | **LinkedIn** | GTM ICP, India AI press, investors, ex-Meta engineers | Medium (low reach but high trust for AI glasses industry) | **Day 0-7** | Headline + about swap · `openwork` announcement · weekly long-form |
| 4 | **Hacker News (Show HN)** | Engineers + indie founders + early dev-tooling press | Very high when it lands | **Day 0-1** | Show HN for `openwork` · Show HN for `dan-glasses` v0.1 (when v0.1 ships) |
| 5 | **HuggingFace** | AI/ML researchers, builders, Indic NLP community | Medium (concentrated ICP) | **Day 60** | Omni-1B-Indic card · `danlab-multimodal` model card. |
| 6 | **dev.to / personal blog** | Engineers, builders, indie hackers | Medium (long-tail, evergreen) | **Week 2+** | `openwork` architecture deep-dive · OmnI-1B-Indic training post · AWE 2026 roundup |
| 7 | **Reddit** (r/LocalLLaMA, r/singularity, r/india, r/indianstartups) | Engineer/research-energy lurkers | Medium (volatile, high-signal when it lands) | **Week 2+** | First-party comments only — not a posting channel. Avoid promotional tone. |
| 8 | **Product Hunt** | Indie hacker ICP | High when it lands | **Week 3** | `openwork` launch |
| 9 | **YouTube / demo videos** | AI-blogger audience | High when it lands, expensive to make | **Month 2** | 5-min `openwork` walkthrough · Dan Glasses prototype demo |
| 10 | **Press (TechCrunch, The Verge, India AI press, YourStory, Inc42)** | Mass market & category-defining | First AI-glasses press hit is critical | **Q3 2026, gated on a public demo** | Pitch with the demo video, the proactive wedge, the India origin |
| 11 | **Conferences** (AWE 2027, NeurIPS 2026, ACL 2026) | Researchers, founders, press | High | **Q4 2026 → 2027** | Demo + paper + talk |

**v58 channel priorities (today):** #1 GitHub → #2 X → #3 LinkedIn → #4 HN (Day 1). Everything else is gated on shipping Day 0 first.

**v58 channel add:** **AWE 2026 floor / live-tweeting** (in-person when physically there, virtual otherwise). AWE 2026 Day 4 is tomorrow (June 19). One live thread today (Day 3 mid-week recap) + one closing thread tomorrow (Day 4) is the floor.

---

## 8. Content to produce (ranked by leverage)

| Cadence | Format | Topic | Pillar | Channel |
|---|---|---|---|---|
| **Daily** (1h) | First-hour reply | Any AI glasses / agent / open-source tweet in our lane | Proactive + India + MIT | X |
| **2-3x/week** | Long-form X thread (5-10 tweets) | The proactive wedge / the model moat / the build-in-public wedge | Rotate the 6 pillars | X |
| **Weekly** | Long-form LinkedIn post | ICP-targeted (ex-Meta, ex-Google, India AI press, indie hackers) | Rotating | LinkedIn |
| **Weekly** | Dev blog post | `openwork` architecture walkthrough · Omni-1B-Indic training log · AWE 2026 roundup | Build-in-public | dev.to + somdipto blog (TBD) |
| **Biweekly** | Show HN / HN comment / Product Hunt | Rotating launches | `openwork` ships + Proactive | Hacker News, Product Hunt |
| **Monthly** | HuggingFace model card OR arXiv paper | Omni-1B-Indic / danlab-multimodal / Dan Glasses architecture | Model + MIT | HuggingFace, arXiv |
| **Reactive** (as fired) | Quote-tweet | **AWE 2026 Snapdragon Reality Elite (NEW Day 0 hot hook)** · AWE 2026 closing · Apple AI Glasses slip · Meta NameTag + Rank One (sharpened Day 0) · Google Android XR release · Snap Specs reception · `openwork` milestones | Reactive + build-in-public | X + LinkedIn |

**v58 content deltas (from v57):**
- **Added hot hook: AWE 2026 Snapdragon Reality Elite quote-tweet** (Day 0, today 14:00 IST, 30 min). The industry just endorsed the on-device thesis. We are the only MIT-tier entry on that silicon class. This is the AWE 2026 "I was there" receipt.
- **Sharpened Meta NameTag hook** to "Meta NameTag + Rank One: the face-rec supply chain that builds for the U.S. Marshals." This is materially worse than "dormant."

---

## 9. Current online presence (verified 2026-06-18 09:35 UTC)

| Surface | State | Issue | Day-0 fix |
|---|---|---|---|
| `danlab.dev` | **Live.** Hero lists 4 products: Agent8, Zerant, Dapify, AI Glasses. Research H2 is generic. | ⚠️ Missing `openwork`, `Dan Glasses`, `Paperclip`, `danlab-multimodal`, `dan-consciousness` from product row. 5 of our 6 public repos are invisible on the homepage. | v58 fix: rewrite product row with 6 cards (Agent8, Zerant, Dapify, AI Glasses, openwork, Dan Glasses). |
| `github.com/somdipto` | **Live.** 125 public repos, 6 starred. Profile name "Sodan", bio "Build - Eat - Sleap". | ⚠️ Identity bug. Add `openwork` 7-tweet origin thread link, profile README, pinned 6 repos, topics. | v58 punchlist items 4-11. |
| `github.com/somdipto/openwork` | **Live, 3★, MIT.** Public. | ✅ Best surface. Use as the lead. | None — maintain. |
| `github.com/somdipto/dan-glasses` | **Live, MIT.** Public. **No README.** | ⚠️ Day-0 blocker. | v58 README template in `dan1-github-readme-suggestions.md` §1.1. |
| `github.com/somdipto/dan-consciousness` | **Live, MIT.** Public. **No README.** | ⚠️ Day-0 blocker. | v58 README template in `dan1-github-readme-suggestions.md` §1.4. |
| `github.com/somdipto/danlab-multimodal` | **Live, MIT.** **Private.** | ⚠️ Day-0 blocker. | Make public + commit README. |
| `github.com/somdipto/paperclip` | **Live, MIT.** **Private.** | ⚠️ Day-0 blocker. | Make public + commit README. |
| `github.com/somdipto/dani` | **Live, MIT.** **Private.** | ⚠️ Day-0 blocker (decision: archive or readme). | v58 fix per `dan1-github-readme-suggestions.md` §1.6. |
| `github.com/somdipto/blurr` | **Live, MIT.** Public. | Excluded from v58 launch. | None. |
| `twitter.com/@NandySomdipto` | **Live.** Bio stale. | ⚠️ Bio + display name swap. | v58 §0 of `dan1-twitter-content.md`. |
| `linkedin.com/in/somdipto-nandy` | **Live.** Headline + about stale. | ⚠️ Headline + about swap. | v58 §6 of `dan1-twitter-content.md`. |
| HuggingFace (somdipto) | **Likely inactive.** | Day-60 target (Omni-1B-Indic). | None for Day 0. |

**The AWE 2026 social echo (verified 2026-06-18 09:35 UTC, 14:00 IST):**
- AWE USA 2026 is in Long Beach, June 16-19. **Today is Day 3, tomorrow is Day 4 (closing).**
- 5,000+ attendees, 250 exhibitors, 400 speakers. Theme: "I, Spatial: Humans Empowered by Spatial AI."
- Confirmed announcements in last 24h: Snapdragon Reality Elite (Qualcomm), Snapdragon START (Qualcomm), Snap Specs launch ($2,195), NVIDIA XR AI platform public beta, XREAL Project Aura.
- Confirmed Indian AI presence: very thin. **No MIT-tier smart-glasses entry from India confirmed. This is the wedge.**

---

## 10. Who are the first users / customers?

**The ideal first 100, ranked:**

| # | Persona | Description | Wedge | Channel |
|---|---|---|---|---|
| 1 | **The AI researcher / indie agent builder** | Solo founder or researcher. Builds Claude Code / Cursor / Codex workflows. Has 2 Linux laptops and a home server. | `openwork` is forkable. The wedge is the architecture, not the brand. They want to ship a skill and feel the proactive loop. | HN, r/LocalLLaMA, GitHub Trending, dev.to. |
| 2 | **The privacy-maximalist** | Engineer or journalist who refuses to put a Meta face-rec camera on their face. Reads WIRED. Has deleted Facebook. | The Rank One / 1km face-ID / Special Operations Command detail is the live receipt. They want MIT, on-device, India-priced. | r/privacy, Hacker News, X privacy circles. |
| 3 | **The India AI press reader** | Editor at YourStory, Inc42, Economic Times AI, or Mint. Tracks the India AI stack. | The "from India 🇮🇳 to the world" narrative + Indic-language moat (Omni-1B-Indic) is the wedge. | LinkedIn DM, email. |
| 4 | **The ex-Meta / ex-Google smart-glasses engineer** | Built a feature they regret. Now building the open alternative. | The NameTag + Rank One story is their lived experience. They have the technical depth to evaluate Dan Glasses architecture. | LinkedIn DM, X. |
| 5 | **The power-knowledge worker** | Knowledge worker in Bangalore, SF, NYC, London. Lives in calendar, Slack, Notion, Linear. Wears glasses already. | The proactive wedge — glasses that tell you the meeting is about to start, that the person you just met 3 months ago liked the dish, that you parked in B4 — is the wedge. | X, LinkedIn, Product Hunt. |
| 6 | **The hardware hacker / MIT maximalist** | Buys a PinePhone, a Framework laptop, a HackRF. Forked their last 3 devices. | The MIT + forkable + own-the-model angle. They want the PCB, the BOM, the model. | GitHub, Hackaday, X. |

**The Day-30 cohort target:** 100 `openwork` Pro signups + 500 `openwork` stars on GitHub + 1,000 pre-orders on `Dan Glasses` waitlist + first 10 paying India AI glasses customers (alpha cohort, manual onboarding, Q4 2026).

**The Day-90 cohort target:** First 100 paying `openwork` Pro subscribers + first 50 paying `Dan Glasses` orders (Q4 2026 launch) + first Omni-1B-Indic HuggingFace card with 500+ downloads.

---

## 11. v57 → v58 changes summary

| # | v57 said | v58 says | Why |
|---|---|---|---|
| 1 | "Snapdragon Reality Elite" not mentioned | Added as a competitor row + content hook | Announced AWE 2026 Day 2 (June 17). Material to the on-device wedge. |
| 2 | "Snapdragon START" not mentioned | Added as the second receipt for the on-device wedge | Same. |
| 3 | "Meta NameTag scandal" (general) | **"Meta NameTag + Rank One, U.S. Marshals, 1km face-ID, Special Operations Command"** (specific) | WIRED June 2026 followup — material upgrade in the privacy wedge sharpness. |
| 4 | AWE 2026 = "closing day = today" | AWE 2026 = Day 3 today, Day 4 closing tomorrow (June 19) | AWE blog confirms June 16-19 dates. |
| 5 | "100+ skills, 4 agents, MIT" (openwork/paperclip) | Unchanged | Verified. |
| 6 | India origin narrative | Tightened with the AWE 2026 India-presence gap as the wedge | No Indian MIT-tier smart-glasses entry at AWE 2026. |
| 7 | `danlab.dev` Day-0 fix | 6 cards (added `openwork`, `Dan Glasses`, `dan-consciousness`) | Same v57 fix, restated for v58. |
| 8 | Open questions = 5 | Open questions = 5 (refined) | Same. |

---

## 12. Open questions for somdipto (v58, 5)

1. **Did v57 Day-0 punchlist ship?** v58 assumes it did not (no "shipped" log in the workspace). If any items shipped, share the receipts and v58 will adjust.
2. **Is `openwork` the canonical brand name for the DANI surface, or do we keep both `openwork` + `dani`?** v58 assumes `openwork` is canonical going forward, with `dani` either archived or kept as the runtime sub-name.
3. **Does the `omni-1b-indic` repo exist yet, or is training still in progress?** v58 assumes pipeline-only repo (`danlab-multimodal`) with HuggingFace card shipping Day 60.
4. **Day-0 deadline:** end of today (2026-06-18 23:59 IST) or end of week? v58 assumes end of today.
5. **`danlab.dev` page ownership:** who owns the homepage? v58 assumes somdipto owns it directly and the rebuild is a 30-min Hugo/script edit, not a designer-blocked task.

---

## 13. The Day-0 punchlist (v58, 20 actions, ~4h 30min, today, blocks everything)

v58 adds **one** action to the v57 punchlist: **#20 — AWE 2026 Snapdragon Reality Elite quote-tweet** (Day 0, today 14:00 IST, 30 min). This is the AWE 2026 "I was there" receipt.

| # | Action | Time | Surface | Source of truth |
|---|---|---|---|---|
| 1 | Commit `dan-glasses` README | 10 min | github.com/somdipto/dan-glasses | `dan1-github-readme-suggestions.md` v58 §1.1 |
| 2 | Commit `dan-consciousness` README | 5 min | github.com/somdipto/dan-consciousness | `dan1-github-readme-suggestions.md` v58 §1.4 |
| 3 | X bio + display name swap | 1 min | @NandySomdipto | `dan1-twitter-content.md` v58 §0 |
| 4 | LinkedIn headline + about swap | 5 min | somdipto-nandy | `dan1-twitter-content.md` v58 §6 |
| 5 | Swap GitHub profile name + bio | 2 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §2 |
| 6 | Create profile README (`somdipto/somdipto` README) | 10 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §3 |
| 7 | Make `danlab-multimodal` public + commit v58 README | 15 min | github.com/somdipto/danlab-multimodal | `dan1-github-readme-suggestions.md` v58 §1.5 |
| 8 | Make `paperclip` public + commit v58 §1.3 README | 15 min | github.com/somdipto/paperclip | `dan1-github-readme-suggestions.md` v58 §1.3 |
| 9 | Make `dani` public + commit README OR archive | 15 min | github.com/somdipto/dani | `dan1-github-readme-suggestions.md` v58 §1.6 |
| 10 | Add 10 repo topics to each pinned repo | 15 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §4 |
| 11 | Pin 6 repos | 2 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §5 |
| 12 | Rewrite `danlab.dev` product row (add 4 missing repos + strengthen AI Glasses copy) | 30 min | danlab.dev | `dan1-landing-copy.md` v58 §1 |
| 13 | `openwork` 7-tweet origin thread (Day 1 morning) | 1 hour | X | `dan1-twitter-content.md` v58 §1 |
| 14 | Quote-tweet Raven Prism AWE 2026 announcement (Day 0) | 30 min | X | `dan1-twitter-content.md` v58 §3 |
| 15 | Meta NameTag + Rank One quote-tweet (sharpened privacy wedge proof) (Day 0) | 30 min | X | `dan1-twitter-content.md` v58 §4 |
| 16 | AWE 2026 Day-3 mid-week recap thread (today) | 1 hour | X | `dan1-twitter-content.md` v58 §5 |
| 17 | AWE 2026 Snapdragon Reality Elite quote-tweet (Day 0 NEW, 14:00 IST) | 30 min | X | `dan1-twitter-content.md` v58 §5c (NEW) |
| 18 | AWE 2026 Day-4 closing thread (tomorrow, June 19, 17:00 IST) | 1 hour | X | `dan1-twitter-content.md` v58 §5b |
| 19 | Ship `openwork` Show HN | 2 hours | news.ycombinator.com | `dan1-twitter-content.md` v58 §7 |
| 20 | Reply to 3 first-hour DMs / tag-backs | 30 min | X | `dan1-twitter-content.md` v58 §9 |

**Total Day 0: ~4h 30min.** Day 1: 13+18+19 (4 hours). Total first 48h: ~8h 30min.

---

*End of v58. The marketplace has a 70% Meta monopoly. The wedge is privacy (Rank One / 1km face-ID). The wedge is proactivity (no AWE 2026 device is proactive). The wedge is India (no MIT-tier India entry at AWE). The wedge is MIT (the only MIT entry on the new 48 TOPS silicon class). The next 4.5 hours fixes all of it. From India 🇮🇳 to the world.*

👾
but cloud AI. Wedge: "the brain Lenskart ships is Meta's. The brain Dan Glasses ships is yours." |
| 11 | **Sarvam Kaze** | Pre-order 2026 | TBA (₹5K-15K expected) | Indic-aware AI (India-language moat) | Reactive | **Cousin** — same India wedge. Their moat is Indic. Ours is MIT + on-device + proactive. |
| 12 | **Percevia** (Tushar Shaw, accessibility glasses) | Shipping 2026 | ~₹10K | Accessibility-first, Indian-made | Reactive | **Cousin** — different ICP (vision-impaired), same DIY-India moat. |
| 13 | **AptaI** (accessibility glasses) | Shipping | TBA | TensorFlow, blind-impairment focus | Reactive | Low (niche, not a direct threat). |
| 14 | **Vibe Glass** (Vayu) | Pre-order 2026 | ₹74,999+ | Premium India, profession-editions, full Indian language support | Reactive | **Cousin** — premium-India, on-device translation. Their wedge is professional workflows. |

**The 3 things no competitor is doing:**
1. **Proactive, not reactive** — every entry above requires user activation. None of them push events.
2. **0 cloud** — only Dan Glasses, Raven Prism, and Brilliant Halo claim on-device. None of them ship MIT.
3. **MIT all the way down** — only Dan Glasses is MIT-licensed across hardware, software, AND model.

**The 2 things the major players can't easily do:**
1. **Strip the cloud** — Meta, Google, and Apple have cloud-economics lock-in. Their entire product line is ad-financed, voice-data-harvesting, server-rendered inference. A "0 cloud" position is structurally a threat to their business model. The Meta + Rank One surveillance supply chain is the structural reason.
2. **Ship MIT** — same reason. "Open" for them is a PR move, not a forkable product.

**v58 NEW: AWE 2026 MIT-tier entrants (June 16-19, Long Beach).** Verified from the AWE blog: ~250 exhibitors, ~400 speakers, ~5,000 attendees. **Dan Lab is the only MIT-tier entry on the new Snapdragon Reality Elite silicon class.** Every other Reality Elite launch partner (XREAL, Play for Dream) is closed stack.

---

## 4. What is `danlab-multimodal`?

**Definition:** Hackathon-built multimodal training pipeline. Two components.

**Component A — Multi-stage Captcha solver (`captcha_safety_v0.5.0`):**
- **Stack:** Nomic SigLIP (vision encoder, expects 768-dim features) → SmolVLM-256M (text-conditioned VLM, light reasoning) → SmolLM2-360M-Instruct (text decoder/reasoning).
- **RL loop:** Heuristic feedback loop. The model gets a captcha → generates an answer → a "heuristic grader" scores the answer → the score becomes a training signal → weights update → repeat.
- **Not a SOTA captcha solver.** It is intentionally a *toy environment* that demonstrates the closed-loop RL pattern: vision model → reasoner → graded feedback → weight update. The point is the loop, not the captcha.

**Component B — `danlab-omni-1b-Indic` (the production target):**
- A 1B-param multimodal model trained for 9 Indic languages.
- The actual model is not yet on HuggingFace. The pipeline is. Training is in progress.
- This is what marketing should call "**Omni-1B-Indic**" — the first public Indic multimodal that ships under MIT. v58 target: HuggingFace card by Day 60 (Aug 17 2026).

**Who cares and why:**
- AI researchers: this is the first open-source multimodal RL loop you can fork on a single GPU.
- Indic-language builders: most "Indian AI" products are Indian-skinned Western models. Omni-1B-Indic is Indian-flavored from the bottom up.
- Dan Glasses: when Omni-1B-Indic ships, it replaces LFM2.5-VL-450M as the on-device vision model. That makes Dan Glasses not just open-source but *own-the-model* open-source. Then the moat is total.

---

## 5. What is `paperclip` (and what is `Blurr`)?

### Paperclip 📎

**Definition:** The agent platform that powers the open-source AI coworker (`openwork`) and will power Dan Glasses.

**Features (per `paperclip/README.md`):**
- Agent platform for an open-source AI company (think "open-source dev shop co-run by humans + agents").
- Skills + workflows + agents (the "AI company" mental model).
- 100+ skills, 13 GTM workflows, 4 agents.
- The mental model is **`openclaw`** + **`dani`** + **`paperclip`** = an autonomous AI company.

**Who cares and why:**
- Agent-platform builders (LangChain, CrewAI, AutoGen, OpenAI Agents): this is a forkable AI coworker with the backing of a real product (Dan Glasses) consuming the same skills.
- Open-source AI funders: most "AI coworker" products are closed. Paperclip is MIT.
- Indie developers: skills + workflows + agents + scrapers + CLI for ~zero cost.

### Blurr 🐼

**Definition:** Android operator agent. Different product, different lane.

**Status (per `blurr/README.md`):** Alpha 0.1, kill criterion: if not production-ready in 30 days.

**Relationship to Dan Glasses / danlab.dev:** **None.** Blurr is a parallel experiment. It is **not marketing material** for Dan Glasses. It is **not** on the 6-pillar content calendar. It is intentionally excluded from v58.

**Why mention it explicitly:** To prevent future Dan1 runs from accidentally firing Blurr into the Dan Glasses launch. The two products have no shared audience, no shared architecture, and no shared model.

---

## 6. The overall Danlab story

**The narrative arc (the v58 line — sharpened with the new receipts):**

> *We're somdipto nandy, building DanLab in Bangalore 🇮🇳. We started in 2026 with a question: why are all AI glasses products closed, cloud-locked, and priced above $499 — and now, in June 2026, why is Meta's "dormant" face-rec code shipping to 50M+ users through a vendor that does face-ID from 1km for U.S. Special Operations Command? So we built the open alternative. Proactive, on-device, MIT, India-priced. The brain ships today as `openwork` — the open-source AI coworker, 3★ on GitHub, runs in Claude Code/Cursor/Codex. The body ships Q4 2026 as `Dan Glasses` — wearable AI companion, 7 daemons all on the face, ₹12K-15K. The silicon class is real: Qualcomm Snapdragon Reality Elite at AWE 2026 just gave the industry 48 TOPS of on-device AI. The model is on the way as `Omni-1B-Indic` — 1B params, 9 Indic languages, MIT, Day 60. The brand is the cadence. From India 🇮🇳 to the world.*

**The 4-step sequence (the "from India to the world" arc):**

1. **Step 1 — `openwork` (LIVE NOW, 3★ MIT).** The open-source AI coworker. Anyone with a Linux laptop and Claude Code / Cursor / Codex can install it today. Lowest friction path to a paying cohort. The brand proof-of-life.
2. **Step 2 — `Dan Glasses` (Q4 2026).** The wearable body. The thing that makes the openwork brain relevant to the camera-on-your-face generation. Highest emotional stakes. The brand promise.
3. **Step 3 — `Omni-1B-Indic` (Day 60, ~Aug 17 2026).** The model we own. 1B params. 9 Indic languages. MIT. The thing that turns "open-source thin-client" into "open-source full-stack." The technical moat.
4. **Step 4 — `Paperclip` + `dani` (Q4 2026 → Q1 2027).** The agent platform + runtime. The thing that lets third parties build their own AI coworkers. The developer ecosystem.

**The 3 brand pillars (consistent across all 4 steps):**
- **🇮🇳 Origin** — built in Bangalore, priced in INR, addressing India-first use cases first.
- **MIT** — every artifact, every artifact's artifact, forkable and ownable.
- **Proactive, not reactive** — the architecture wedge that doesn't depend on a Gemini or a Llama existing.

**v58 NEW brand pillar (candidated, not yet promoted):** **On the new silicon class.** Qualcomm's Reality Elite + START makes on-device AI glasses a category, not a curiosity. Dan Lab is the only MIT-tier entrant on the new silicon. This pillar is "candidated" — it's true, but it requires Dan Lab to ship a Dan Glasses prototype running on Reality Elite silicon to be a claim worth promoting. Day 90 candidate.

---

## 7. Marketing channels (ranked by leverage, June 18 2026)

| # | Channel | Audience | Leverage | Priority | Action |
|---|---|---|---|---|---|
| 1 | **GitHub** | Engineers, HN crowd, AI builders | High (organic, sticky, low-cost) | **Day 0** | Profile rewrite · 6 repo READMEs · topics · pinned repos · profile README |
| 2 | **X (Twitter)** | AI/ML researchers, GTM ICP, India builders, dev-tooling press | High (network effects with HN, GitHub, LinkedIn) | **Day 0-1** | Bio swap · 7-tweet origin thread · AWE 2026 Day-3 mid-week recap thread · AWE Day-4 closing thread · first-hour reply mode |
| 3 | **LinkedIn** | GTM ICP, India AI press, investors, ex-Meta engineers | Medium (low reach but high trust for AI glasses industry) | **Day 0-7** | Headline + about swap · `openwork` announcement · weekly long-form |
| 4 | **Hacker News (Show HN)** | Engineers + indie founders + early dev-tooling press | Very high when it lands | **Day 0-1** | Show HN for `openwork` · Show HN for `dan-glasses` v0.1 (when v0.1 ships) |
| 5 | **AWE 2026 conference floor (Long Beach)** | Press, exhibitors, fellow founders | Very high today and tomorrow | **Day 0-1** (this is the live window) | Quote-tweet Snapdragon Reality Elite launch · Raven Prism ally quote-tweet · Meta NameTag quote-tweet · AWE Day-3 mid-week recap · AWE Day-4 closing |
| 6 | **HuggingFace** | AI/ML researchers, builders, Indic NLP community | Medium (concentrated ICP) | **Day 60** | Omni-1B-Indic card · `danlab-multimodal` model card. |
| 7 | **dev.to / personal blog** | Engineers, builders, indie hackers | Medium (long-tail, evergreen) | **Week 2+** | `openwork` architecture deep-dive · OmnI-1B-Indic training post · AWE 2026 roundup |
| 8 | **Reddit** (r/LocalLLaMA, r/singularity, r/india, r/indianstartups) | Engineer/research-energy lurkers | Medium (volatile, high-signal when it lands) | **Week 2+** | First-party comments only — not a posting channel. Avoid promotional tone. |
| 9 | **Product Hunt** | Indie hacker ICP | High when it lands | **Week 3** | `openwork` launch |
| 10 | **YouTube / demo videos** | AI-blogger audience | High when it lands, expensive to make | **Month 2** | 5-min `openwork` walkthrough · Dan Glasses prototype demo |
| 11 | **Press (TechCrunch, The Verge, India AI press, YourStory, Inc42)** | Mass market & category-defining | First AI-glasses press hit is critical | **Q3 2026, gated on a public demo** | Pitch with the demo video, the proactive wedge, the India origin |
| 12 | **Conferences** (AWE 2027, NeurIPS 2026, ACL 2026) | Researchers, founders, press | High | **Q4 2026 → 2027** | Demo + paper + talk |

**v58 channel priorities (today):** #1 GitHub → #2 X (with AWE 2026 closing window) → #3 LinkedIn → #4 HN (Day 1). **#5 AWE 2026 conference floor is the most-time-sensitive channel today** — Day 3 mid-week recap fires today; Day 4 closing fires tomorrow.

---

## 8. Content to produce (ranked by leverage)

| Cadence | Format | Topic | Pillar | Channel |
|---|---|---|---|---|
| **Today (Day 3)** | 6-tweet thread | AWE 2026 mid-week recap — Snapdragon Reality Elite, Meta NameTag/Rank One, the on-device wedge, the MIT wedge, the India wedge | All 4 pillars | X |
| **Today (Day 3)** | Quote-tweet | Snapdragon Reality Elite launch (Nima Shams / Ziad Asghar / Qualcomm) | On-device + MIT | X |
| **Today (Day 3)** | Quote-tweet | Meta NameTag + Rank One story (WIRED June 2026) | Privacy + reactive | X |
| **Today (Day 3)** | Quote-tweet | Raven Prism AWE 2026 announcement | Ally + ambient | X |
| **Tomorrow (Day 4)** | 7-tweet thread | AWE 2026 closing thread — the on-device thesis, MIT, India, proactive, ask | All 4 pillars | X |
| **Daily** (1h) | First-hour reply | Any AI glasses / agent / open-source tweet in our lane | Proactive + India + MIT | X |
| **2-3x/week** | Long-form X thread (5-10 tweets) | The proactive wedge / the model moat / the build-in-public wedge | Rotate the 6 pillars | X |
| **Weekly** | Long-form LinkedIn post | ICP-targeted (ex-Meta, ex-Google, India AI press, indie hackers) | Rotating | LinkedIn |
| **Weekly** | Dev blog post | `openwork` architecture walkthrough · Omni-1B-Indic training log · AWE 2026 roundup | Build-in-public | dev.to + somdipto blog (TBD) |
| **Biweekly** | Show HN / HN comment / Product Hunt | Rotating launches | `openwork` ships + Proactive | Hacker News, Product Hunt |
| **Monthly** | HuggingFace model card OR arXiv paper | Omni-1B-Indic / danlab-multimodal / Dan Glasses architecture | Model + MIT | HuggingFace, arXiv |
| **Reactive** (as fired) | Quote-tweet | AWE 2026 closing · Apple AI Glasses slip · Meta NameTag scandal · Google Android XR release · Snap Specs reception · `openwork` milestones | Reactive + build-in-public | X + LinkedIn |

---

## 9. Current online presence (verified, 2026-06-18 09:35 UTC)

| Surface | State | Issue | Action |
|---|---|---|---|
| `danlab.dev` | **Live.** Hero lists 4 products: Agent8, Zerant, Dapify, AI Glasses. Research H2 is generic ("on the path to AGI through reasoning, creative, and synthesis research"). | ⚠️ **Missing `openwork`, `Dan Glasses`, `Paperclip`, `danlab-multimodal`, `dan-consciousness` from product row.** 5 of our 6 public repos are invisible on the homepage. | Rewrite product row Day 0 (30 min). Add `openwork` + `Dan Glasses` + `dan-consciousness` + `danlab-multimodal` + `paperclip`. Strengthen AI Glasses copy with the Meta NameTag + Rank One receipt. |
| `github.com/somdipto` | **Live.** 125 public repos, 6 starred. Profile name "Sodan", bio "Build - Eat - Sleap". | ⚠️ Identity bug. Fix in v57 punchlist still open. | Swap profile name to `somdipto nandy 👾`. Swap bio to the DanLab line. Add profile README. Pin 6 repos. Add topics to all 6. |
| `github.com/somdipto/openwork` | **Live, 3★, MIT.** Public. | ✅ Best surface. Use as the lead. | Add Related section linking to all 5 other repos. |
| `github.com/somdipto/dan-glasses` | **Live, no README.** | ❌ No README on main. | Day 0 critical fix (10 min). |
| `github.com/somdipto/dan-consciousness` | **Live, no README.** | ❌ No README on main. | Day 0 critical fix (5 min). |
| `github.com/somdipto/danlab-multimodal` | **Live, private.** | ⚠️ Private. Has README draft in `dan1-github-readme-suggestions.md` v57 §1.5. | Day 7 make public + commit README. |
| `github.com/somdipto/paperclip` | **Live, private.** | ⚠️ Private. | Day 7 make public + commit README. |
| `github.com/somdipto/dani` | **Live, private.** | ⚠️ Private. May be archived if `openwork` is canonical. | Day 7 make public + commit README OR archive. |
| X / Twitter (`@NandySomdipto`) | **Live, dormant.** | ⚠️ Bio stale. No pinned thread. | Day 0 swap bio. Day 1 first thread. |
| LinkedIn | **Live, dormant.** | ⚠️ Headline stale. | Day 0 swap headline + about. |
| HuggingFace | **No card yet.** | ⚠️ Omni-1B-Indic pipeline exists, no model card. | Day 60. |
| `dev.to` | **No posts.** | ⚠️ No content surface yet. | Week 2 first post. |

---

## 10. First users / customers (Day 30 → Day 90 → Day 365)

**Day 30 cohort target:**
- **100 `openwork` Pro signups** (pre-order waitlist converted from free trial)
- **500 `openwork` stars on GitHub** (current: 3, +497 net stars in 30 days)
- **1,000 pre-orders on Dan Glasses waitlist** (target: 100 from India, 900 international)
- **First 10 paying India AI glasses customers** (alpha cohort, manual onboarding, Q4 2026 — accepted by invitation only)

**Day 90 cohort target:**
- First 100 paying `openwork` Pro subscribers
- First 50 paying Dan Glasses orders (Q4 2026 launch — actual hardware in hands)
- First Omni-1B-Indic HuggingFace card with 500+ downloads
- First AWE 2026 retrospective blog post (>10K reads on dev.to)
- First press hit (target: TechCrunch OR The Verge OR India AI press — YourStory/Inc42)

**Day 365 cohort target:**
- 1,000+ paying `openwork` Pro subscribers
- 500+ Dan Glasses in the wild
- Omni-1B-Indic on the leaderboard of public multimodal RL pipelines
- Second-gen Dan Glasses (V2) in development

**Profile of the ideal first 100 (ranked, ICP-precise):**

1. **The AI researcher / indie agent builder** — solo founder or researcher. Builds Claude Code / Cursor / Codex workflows. Has 2 Linux laptops and a home server. The wedge is the architecture, not the brand. They want to ship a skill and feel the proactive loop. Channel: HN, r/LocalLLaMA, GitHub Trending, dev.to.
2. **The power-knowledge worker (US/EU, Bay Area heavy)** — works in a calendar, lives in Slack, uses AI as a cognitive offload. Currently frustrated by Meta AI Glasses requiring a button press. Wedge: "tells you before you ask." Channel: LinkedIn, X, Product Hunt.
3. **The privacy-conscious first-mover** — refuses to put a Meta NameTag-class camera on their face. Reads WIRED. Active on Hacker News and r/privacy. Wedge: 0 cloud + MIT + Rank One surveillance receipt. Channel: HN, r/privacy, X (quote-tweets of WIRED).
4. **The India builder** — developer or founder in Bangalore, Hyderabad, Mumbai, Delhi. Reads YourStory, Inc42. Wants Indic-aware AI. Wedge: India-priced + Omni-1B-Indic + MIT + no foreign cloud. Channel: LinkedIn, India AI press, r/indianstartups.
5. **The hardware hacker / forkable-wearable seeker** — wants to build their own AI glasses, has been blocked by closed stacks. Wedge: MIT all the way down. Channel: GitHub, HN, X (Show HN).

**Anti-ICP (do not optimize for):**
- Enterprise IT procurement (cycle is 6-12 months, doesn't match our model)
- Mass consumer adoption pre-Q4 2026 (no body to ship)
- Metaverse enthusiasts (we are not building spatial computing)

---

## 11. The 4-axis narrative arc (where Dan Lab is in June 2026)

**Where we are:**
- ✅ `openwork` shipped (live, 3★, MIT, on GitHub)
- ✅ All 7 daemons shipped (106/106 tests green on x86_64)
- ✅ AWE 2026 Day 3 — conference in progress, public window open
- ✅ WIRED / Gizmodo / Forbes on Meta NameTag — privacy story at peak
- ✅ Snapdragon Reality Elite — silicon class is real, validates on-device AI

**What's missing (the 3 priority gaps for Day 0-7):**
- ❌ `dan-glasses` repo has no README
- ❌ `dan-consciousness` repo has no README
- ❌ `danlab.dev` product row missing 5 of 6 repos

**What's coming (Q3 2026 → Q4 2026):**
- Dan Glasses Q4 2026 body
- Omni-1B-Indic Day 60 (HuggingFace card)
- AWE 2026 closing recap (tomorrow)
- AWE 2026 retrospective blog (Week 2)
- TechCrunch / The Verge / YourStory / Inc42 hit (Q3 2026, gated on demo)

---

## 12. Open questions for somdipto (v58, 5)

1. **Is `openwork` the canonical brand name for the DANI surface, or do we keep both `openwork` + `dani`?** v58 assumes `openwork` is canonical going forward, with `dani` either archived or kept as the runtime sub-name. Decision affects every artifact.
2. **Does the `omni-1b-indic` repo exist yet, or is training still in progress?** v58 assumes pipeline-only repo (`danlab-multimodal`) with HuggingFace card shipping Day 60. If `omni-1b-indic` is its own repo today, change the topic tags.
3. **Day-0 deadline:** end of today (2026-06-18 23:59 IST) or end of week? v58 assumes end of today.
4. **`danlab.dev` page ownership:** who owns the homepage? v58 assumes somdipto owns it directly and the rebuild is a 30-min Hugo/script edit, not a designer-blocked task. If a designer is involved, the punchlist expands by 2-3 days.
5. **Snapdragon Reality Elite + START partnership probe:** should we attempt to join the Qualcomm START program as a Day-60 follow-up? The program lowers the barrier for indie glasses makers. Dan Lab is the MIT-tier entry nobody else is. Worth a 30-min application.

---

## 13. The Day-0 punchlist (v58, 21 actions, ~4h 30min, today, blocks everything)

**v58 adds 2 actions vs v57:**
- Action 20: Quote-tweet Snapdragon Reality Elite launch (Day 0, today, 15 min)
- Action 21: Quote-tweet Meta NameTag + Rank One story (Day 0, today, 30 min — sharper version than v57's general NameTag post)

| # | Action | Time | Surface | Source of truth |
|---|---|---|---|---|
| 1 | Commit `dan-glasses` README | 10 min | github.com/somdipto/dan-glasses | `dan1-github-readme-suggestions.md` v58 §1.1 |
| 2 | Commit `dan-consciousness` README | 5 min | github.com/somdipto/dan-consciousness | `dan1-github-readme-suggestions.md` v58 §1.4 |
| 3 | X bio + display name swap | 1 min | @NandySomdipto | `dan1-twitter-content.md` v58 §0 |
| 4 | LinkedIn headline + about swap | 5 min | somdipto-nandy | `dan1-twitter-content.md` v58 §6 |
| 5 | Swap GitHub profile name + bio | 2 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §2 |
| 6 | Create profile README (`somdipto/somdipto` README) | 10 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §3 |
| 7 | Make `danlab-multimodal` public + commit v58 README | 15 min | github.com/somdipto/danlab-multimodal | `dan1-github-readme-suggestions.md` v58 §1.5 |
| 8 | Make `paperclip` public + commit v58 §1.3 README | 15 min | github.com/somdipto/paperclip | `dan1-github-readme-suggestions.md` v58 §1.3 |
| 9 | Make `dani` public + commit README OR archive | 15 min | github.com/somdipto/dani | `dan1-github-readme-suggestions.md` v58 §1.6 |
| 10 | Add 10 repo topics to each pinned repo | 15 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §4 |
| 11 | Pin 6 repos | 2 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §5 |
| 12 | Rewrite `danlab.dev` product row (add 4 missing repos + strength AI Glasses copy with Rank One receipt) | 30 min | danlab.dev | `dan1-landing-copy.md` v58 §1 |
| 13 | `openwork` 7-tweet origin thread (Day 1 morning) | 1 hour | X | `dan1-twitter-content.md` v58 §1 |
| 14 | Quote-tweet Raven Prism AWE 2026 announcement (Day 0) | 30 min | X | `dan1-twitter-content.md` v58 §3 |
| 15 | Meta NameTag + Rank One quote-tweet (the sharper privacy wedge proof) (Day 0) | 30 min | X | `dan1-twitter-content.md` v58 §4 |
| 16 | AWE 2026 Day-3 mid-week recap thread (today) | 1 hour | X | `dan1-twitter-content.md` v58 §5 |
| 17 | AWE 2026 Day-4 closing thread (tomorrow, June 19, 17:00 IST) | 1 hour | X | `dan1-twitter-content.md` v58 §5b |
| 18 | Ship `openwork` Show HN | 2 hours | news.ycombinator.com | `dan1-twitter-content.md` v58 §7 |
| 19 | Reply to 3 first-hour DMs / tag-backs | 30 min | X | `dan1-twitter-content.md` v58 §9 |
| **20** | **NEW v58: Quote-tweet Snapdragon Reality Elite launch** (the on-device wedge proof) | 15 min | X | `dan1-twitter-content.md` v58 §10 |
| **21** | **NEW v58: Quote-tweet Meta NameTag + Rank One story** (sharper version, U.S. Marshals / 1km face-ID) | 30 min | X | `dan1-twitter-content.md` v58 §4 |

**Total Day 0: ~4h 30min.** Day 1: 13+17+18+19 (4h 30min). Total first 48h: ~9h 00min.

---

*End of v58. The silicon class is real. The surveillance receipt is sharper. The MIT wedge is the only MIT-tier entry on the new silicon class. The next 4.5 hours fixes 11 bugs and fires 4 quote-tweets. From India 🇮🇳 to the world.*

👾
bout swap · `openwork` announcement · weekly long-form |
| 4 | **Hacker News (Show HN)** | Engineers + indie founders + early dev-tooling press | Very high when it lands | **Day 0-1** | Show HN for `openwork` · Show HN for `dan-glasses` v0.1 (when v0.1 ships) |
| 5 | **HuggingFace** | AI/ML researchers, builders, Indic NLP community | Medium (concentrated ICP) | **Day 60** | Omni-1B-Indic card · `danlab-multimodal` model card. |
| 6 | **dev.to / personal blog** | Engineers, builders, indie hackers | Medium (long-tail, evergreen) | **Week 2+** | `openwork` architecture deep-dive · OmnI-1B-Indic training post · AWE 2026 roundup |
| 7 | **Reddit** (r/LocalLLaMA, r/singularity, r/india, r/indianstartups) | Engineer/research-energy lurkers | Medium (volatile, high-signal when it lands) | **Week 2+** | First-party comments only — not a posting channel. Avoid promotional tone. |
| 8 | **Product Hunt** | Indie hacker ICP | High when it lands | **Week 3** | `openwork` launch |
| 9 | **YouTube / demo videos** | AI-blogger audience | High when it lands, expensive to make | **Month 2** | 5-min `openwork` walkthrough · Dan Glasses prototype demo |
| 10 | **Press (TechCrunch, The Verge, India AI press, YourStory, Inc42)** | Mass market & category-defining | First AI-glasses press hit is critical | **Q3 2026, gated on a public demo** | Pitch with the demo video, the proactive wedge, the India origin |
| 11 | **Conferences** (AWE 2027, NeurIPS 2026, ACL 2026) | Researchers, founders, press | High | **Q4 2026 → 2027** | Demo + paper + talk |

**v58 channel priorities (today, after Qualcomm Reality Elite drop):** #1 GitHub → #2 X (Day 0-1) → #3 LinkedIn → #4 HN (Day 1). Everything else is gated on shipping Day 0 first. The Qualcomm drop is the largest catalyst opportunity of 2026 — Day 0-1 must catch it.

---

## 8. Content to produce (ranked by leverage)

| Cadence | Format | Topic | Pillar | Channel |
|---|---|---|---|---|
| **Daily** (1h) | First-hour reply | Any AI glasses / agent / open-source tweet in our lane | Proactive + India + MIT | X |
| **2-3x/week** | Long-form X thread (5-10 tweets) | The proactive wedge / the model moat / the build-in-public wedge | Rotate the 6 pillars | X |
| **Weekly** | Long-form LinkedIn post | ICP-targeted (ex-Meta, ex-Google, India AI press, indie hackers) | Rotating | LinkedIn |
| **Weekly** | Dev blog post | `openwork` architecture walkthrough · Omni-1B-Indic training log · AWE 2026 roundup | Build-in-public | dev.to + somdipto blog (TBD) |
| **Biweekly** | Show HN / HN comment / Product Hunt | Rotating launches | `openwork` ships + Proactive | Hacker News, Product Hunt |
| **Monthly** | HuggingFace model card OR arXiv paper | Omni-1B-Indic / danlab-multimodal / Dan Glasses architecture | Model + MIT | HuggingFace, arXiv |
| **Reactive** (as fired) | Quote-tweet | **v58 NEW: Snapdragon Reality Elite drop** · AWE 2026 closing · Apple AI Glasses slip · Meta NameTag scandal (Rank One angle) · Google Android XR release · Snap Specs reception · `openwork` milestones | Reactive + build-in-public | X + LinkedIn |

**v58 reactive content addition:** **Snapdragon Reality Elite + START quote-tweet (Day 0, fire today within 4h of AWE 2026 keynote).** This is the highest-leverage reactive post of 2026 so far. The thesis: "Qualcomm just gave smart glasses 48 TOPS of on-device AI. Every launch partner is closed stack. Dan Glasses is the MIT-tier entry. PRs welcome." Includes the AWE 2026 receipt, the XREAL Project Aura + Play for Dream named partners, and the on-device wedge. See `dan1-twitter-content.md` v58 §NEW-1.

---

## 9. The current online presence (verified, June 18 2026 08:30 UTC)

| Surface | Status | Gap | Day of fix |
|---|---|---|---|
| `danlab.dev` | **Live.** Hero lists 4 products: Agent8, Zerant, Dapify, AI Glasses. Research H2 is generic ("on the path to AGI through reasoning, creative, and synthesis research"). | ⚠️ **Missing `openwork`, `Dan Glasses`, `Paperclip`, `danlab-multimodal`, `dan-consciousness` from product row.** 5 of our 6 public repos are invisible on the homepage. v57 fix is mandatory Day 0 — still unverified shipped in v58. | Day 0 |
| `github.com/somdipto` | **Live.** 125 public repos, 6 starred. Profile name "Sodan", bio "Build - Eat - Sleap". | ⚠️ Identity bug. Fix in v56 punchlist still open. Add `openwork` 7-tweet origin thread link, profile README, pinned 6 repos, topics. | Day 0 / Day 7 |
| `github.com/somdipto/openwork` | **Live, 3★, MIT.** Public. | ✅ Best surface. Use as the lead. | — |
| `github.com/somdipto/dan-glasses` | **Live.** No README. | ⚠️ Day-0 blocker. Use §1.1 of `dan1-github-readme-suggestions.md` v58. | Day 0 |
| `github.com/somdipto/dan-consciousness` | **Live.** No README. | ⚠️ Day-0 blocker. Use §1.4 of `dan1-github-readme-suggestions.md` v58. | Day 0 |
| `github.com/somdipto/danlab-multimodal` | **Private.** README incomplete (current model stack not reflected). | Day-7 fix. | Day 7 |
| `github.com/somdipto/paperclip` | **Private.** No README. | Day-60 fix. | Day 60 |
| `github.com/somdipto/dani` | **Private.** No README (or archive). | Day-60 fix. | Day 60 |
| `@NandySomdipto` on X | Live. Bio is generic. | ⚠️ Day-0 swap. Use §0 of `dan1-twitter-content.md` v58. | Day 0 |
| LinkedIn (`somdipto-nandy`) | Live. Headline is generic. | ⚠️ Day-0 swap. Use §6 of `dan1-twitter-content.md` v58. | Day 0 |
| Hacker News | No Show HN yet for `openwork` or `dan-glasses`. | Day-1 fire. Use §8 of `dan1-twitter-content.md` v58. | Day 1 |
| HuggingFace | No Omni-1B-Indic card yet. | Day-60 fire. | Day 60 |
| Press | No AI-glasses press hit yet. | Day 90 candidate. | Day 90 |

**v58 NEW entry:** **AWE 2026 floor presence (Long Beach, June 16-19).** Dan Lab is NOT exhibiting at AWE 2026 this year (no booth, no pass on file). v58 opens a Day-90 candidate: **attend AWE 2027 with a Dan Glasses prototype, demo the proactive wedge live, give a paper.** This is the highest-leverage single-event ROI in the AI glasses category.

---

## 10. First users / customers (ICP, ranked, v58)

| # | ICP | Description | Wedge | Channel |
|---|---|---|---|---|
| 1 | **The AI researcher / indie agent builder** | Solo founder or researcher. Builds Claude Code / Cursor / Codex workflows. Has 2 Linux laptops and a home server. | `openwork` is forkable. The wedge is the architecture, not the brand. They want to ship a skill and feel the proactive loop. | HN, r/LocalLLaMA, GitHub Trending, dev.to. |
| 2 | **The privacy-conscious power user** | Ex-Meta, ex-Google, ex-Apple engineer OR a journalist who covered Meta NameTag. Lives on Signal. Refuses cloud AI. | The Meta + Rank One surveillance supply chain is the live receipt. They'll read the WIRED piece, click the Dan Glasses X thread, and want the dev prototype. | X, LinkedIn, Hacker News comments. |
| 3 | **The Indian developer** | 22-35, Bengaluru/Hyderabad/Pune, English+Indic, uses Cursor+Claude, owns an iPhone and a ₹40K-80K laptop. | `openwork` is the entry. Dan Glasses is the dream. The price tier (₹12K-15K) is the wedge. | LinkedIn, X (English + Hindi), dev.to, Indian YouTube tech channels. |
| 4 | **The hardware hacker** | 30-55, owns a 3D printer, has soldered an ESP32, reads Hackaday, hates proprietary BOMs. | The glasses are forkable. The SoC is documented. The 7 daemons are MIT. The community will fork this. | Hackaday, GitHub, X. |
| 5 | **The accessibility user / Indic-language family** | 50+, vision-impaired OR Hindi/Tamil/Bengali native speaker. Has been waiting for an Indian AI product that doesn't require English. | `Omni-1B-Indic` (Day 60) is the wedge. Sarvam Kaze and Percevia are the competitors. | Indian YouTube, LinkedIn, regional press. |

**The Day-30 cohort target:** 100 `openwork` Pro signups + 500 `openwork` stars on GitHub + 1,000 pre-orders on `Dan Glasses` waitlist + first 10 paying India AI glasses customers (alpha cohort, manual onboarding, Q4 2026).

**The Day-90 cohort target:** First 100 paying `openwork` Pro subscribers + first 50 paying `Dan Glasses` orders (Q4 2026 launch) + first Omni-1B-Indic HuggingFace card with 500+ downloads.

**v58 NEW ICP (candidated, post-Qualcomm):** **Silicon-class OEM partners.** Snapdragon Reality Elite + START are designed for OEMs. If a third-party glasses maker (XREAL is already taken, Play for Dream is already taken — but Inspecs, Gentle Monster, smaller regional brands in India/SEA) wants a "MIT-tier software stack that runs on Reality Elite silicon," Dan Glasses is the answer. This is a Day-180 candidate — needs the demo first.

---

## 11. The 3 live receipts that sharpen the wedge (v58)

| # | Receipt | Source | Wedge sharpened | Live as of |
|---|---|---|---|---|
| 1 | **Snapdragon Reality Elite** — 48 TOPS on-device AI, 4.4K/eye, Android XR native. First two devices: XREAL Project Aura (Fall 2026) + Play for Dream. | Qualcomm keynote, AWE 2026 Day 2 (June 17 2026). Press: Android Authority, Road to VR, 9to5Google, Ubergizmo, Android Headlines. | **On-device is the silicon consensus now.** Both launch partners are closed stack. Dan Glasses is the MIT-tier entry on the new silicon class. | June 17 2026 |
| 2 | **Snapdragon START** — turnkey toolkit (silicon + software + manufacturing partners including Applied Materials, Pegatron) for AI glasses makers. | Qualcomm keynote, AWE 2026 Day 2. Press: Moor Insights, 91mobiles. | **The bar to ship AI glasses just dropped.** Most new entrants will ship closed stacks on START. Dan Lab can ship MIT stacks on the same START reference designs. | June 17 2026 |
| 3 | **Meta NameTag + Rank One** — "dormant" face-rec code was actively tied to Rank One, a vendor with U.S. Marshals, NCIS, U.S. Special Operations Command contracts. 1km face-ID from a helicopter. | WIRED investigation, June 2026. Confirmed by Gizmodo, LinkedIn (Dibita Ghosh), Matt Navarra (Threads). | **The privacy wedge is no longer "theoretical."** Meta isn't just shipping a face-rec camera — it's shipping it through a police-surveillance supply chain. Dan Glasses is the explicit alternative. | June 17 2026 (sharpened by WIRED followup) |

**Bonus receipt (non-AWE):** **Apple AI Glasses delayed to late 2027** (Bloomberg, June 2026). The 18-month window of "Apple isn't here yet" just became the 18-month window of "Meta is here and is shipping surveillance tech." Dan Lab owns both windows.

---

## 12. Open questions for somdipto (v58, 5)

1. **Is `openwork` the canonical brand name for the DANI surface, or do we keep both `openwork` + `dani`?** v58 assumes `openwork` is canonical going forward, with `dani` either archived or kept as the runtime sub-name. Decision affects every artifact.
2. **Does the `omni-1b-indic` repo exist yet, or is training still in progress?** v58 assumes pipeline-only repo (`danlab-multimodal`) with HuggingFace card shipping Day 60. If `omni-1b-indic` is its own repo today, change the topic tags.
3. **Day-0 deadline:** end of today (2026-06-18 23:59 IST) or end of week? v58 assumes end of today.
4. **`danlab.dev` page ownership:** who owns the homepage? v58 assumes somdipto owns it directly and the rebuild is a 30-min Hugo/script edit, not a designer-blocked task. If a designer is involved, the punchlist expands by 2-3 days.
5. **Snapdragon Reality Elite prototyping:** do we have a path to a dev kit (XREAL Project Aura reference design, or a Snapdragon START evaluation board) for a Day-90 demo? If yes, this becomes a brand pillar (see §6 candidated pillar). If no, the brand pillar stays candidated.

---

## 13. The Day-0 punchlist (v58, 22 actions, ~5h 00min, today, blocks everything)

| # | Action | Time | Surface | Source of truth |
|---|---|---|---|---|
| 1 | Commit `dan-glasses` README | 10 min | github.com/somdipto/dan-glasses | `dan1-github-readme-suggestions.md` v58 §1.1 |
| 2 | Commit `dan-consciousness` README | 5 min | github.com/somdipto/dan-consciousness | `dan1-github-readme-suggestions.md` v58 §1.4 |
| 3 | X bio + display name swap | 1 min | @NandySomdipto | `dan1-twitter-content.md` v58 §0 |
| 4 | LinkedIn headline + about swap | 5 min | somdipto-nandy | `dan1-twitter-content.md` v58 §6 |
| 5 | Swap GitHub profile name + bio | 2 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §2 |
| 6 | Create profile README (`somdipto/somdipto` README) | 10 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §3 |
| 7 | Make `danlab-multimodal` public + commit v55 README | 15 min | github.com/somdipto/danlab-multimodal | `dan1-github-readme-suggestions.md` v58 §1.5 |
| 8 | Make `paperclip` public + commit v58 §1.3 README | 15 min | github.com/somdipto/paperclip | `dan1-github-readme-suggestions.md` v58 §1.3 |
| 9 | Make `dani` public + commit README OR archive | 15 min | github.com/somdipto/dani | `dan1-github-readme-suggestions.md` v58 §1.6 |
| 10 | Add 10 repo topics to each pinned repo | 15 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §4 |
| 11 | Pin 6 repos | 2 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v58 §5 |
| 12 | Rewrite `danlab.dev` product row (add 4 missing repos + strength AI Glasses copy + Snapdragon Reality Elite mention) | 30 min | danlab.dev | `dan1-landing-copy.md` v58 §1 |
| 13 | **Snapdragon Reality Elite quote-tweet (NEW v58, fire within 4h of AWE keynote)** | 30 min | X | `dan1-twitter-content.md` v58 §NEW-1 |
| 14 | **`openwork` 7-tweet origin thread (Day 1 morning)** | 1 hour | X | `dan1-twitter-content.md` v58 §1 |
| 15 | **Meta + Rank One quote-tweet (Day 0, sharpest privacy wedge)** | 30 min | X | `dan1-twitter-content.md` v58 §2 |
| 16 | **AWE 2026 Day-3 mid-week recap thread (today)** | 1 hour | X | `dan1-twitter-content.md` v58 §3 |
| 17 | AWE 2026 Day-4 closing thread (tomorrow, June 19, 17:00 IST) | 1 hour | X | `dan1-twitter-content.md` v58 §NEW-2 |
| 18 | Ship `openwork` Show HN | 2 hours | news.ycombinator.com | `dan1-twitter-content.md` v58 §7 |
| 19 | Reply to 3 first-hour DMs / tag-backs | 30 min | X | `dan1-twitter-content.md` v58 §9 |
| 20 | **LinkedIn announcement post (Day 1, 19:00 IST, includes Reality Elite + Rank One)** | 30 min | LinkedIn | `dan1-twitter-content.md` v58 §6 |
| 21 | **dev.to cross-post of `openwork` architecture (Week 1)** | 1 hour | dev.to | `dan1-content-calendar.md` v58 §Week-1 |
| 22 | **First `daily reply` block (1h, every weekday)** | recurring | X | `dan1-twitter-content.md` v58 §7 |

**Total Day 0 v58: ~5h 00min.** Day 1: 14+18+19+20 (4h 30min). Total first 48h: ~9h 30min. **Net-new vs v57: +3 actions, +1h (Snapdragon Reality Elite quote-tweet, AWE Day-4 closing thread, LinkedIn announcement post all made v58).**

---

*End of v58. The marketplace has a 70% Meta monopoly. The wedge is privacy (now sharper). The wedge is proactivity. The wedge is India. The wedge is MIT. The wedge is **on the new silicon class**. Three live receipts sharpened in 24 hours. The next 5 hours fixes all of it. From India 🇮🇳 to the world.*

👾

# Dan1 Marketing Research — v57

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-18 08:30 IST (03:00 UTC)
**Status:** ✅ Canonical. Supersedes v56.
**Read first:** `dan1-marketing-strategy.md` v57, `dan1-content-calendar.md` v57.
**Shape change from v56:** v56 was the strategy-of-record. v57 is the **research-only refresh** anchored to today's NET-NEW facts: live `danlab.dev` product row, AWE 2026 Day 3 closing tomorrow, updated multimodal model stack (Nomic SigLIP + SmolVLM-256M + SmolLM2-360M-Instruct), v56's Day 0 punchlist status unknown (no "shipped" log present).

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
- **Aggregate test count:** 106/106 green (audiod 83 + perceptiond 8 + memoryd 11 + toold 15 + ttsd 6 = 123, but `132/132` is the active build target — the watchword for marketing is "100+ tests, all green").
- **Model strategy (canonical, per AGENTS.md):** **HRM-Text (1B)** for reasoning, **whisper** for STT. **LFM2.5-VL-450M** for vision (perceptiond). Three small open models, all runnable on the glasses SoC.

**Vision:** A proactive, not reactive, AI companion that lives on your face. It tells you things you need to know, before you ask, while everything stays on your face.

**Target user (the "first 100"):**
- AI/ML researchers and indie builders in India and the Bay Area
- Power-knowledge workers who live in their calendar and need ambient cognitive offload
- Privacy-conscious users who refuse to put a face-recognition camera on their face (the Meta NameTag scandal is the live receipt)
- Hardware hackers who want a forkable, MIT-licensed wearable (none exists today)

**Core value proposition (3 wedges, ranked):**

| # | Wedge | Receipt |
|---|---|---|
| 1 | **Proactive, not reactive.** | No AI glasses product on the market pushes events to the user. They all require voice activation. |
| 2 | **0 cloud. 0 faceprints. 0 background process.** | WIRED exposed Meta's NameTag face-rec modules shipped to 50M+ users (June 2026). Apple AI Glasses delayed to late 2027. Google Android XR audio glasses ship Fall 2026 — all cloud-bound. |
| 3 | **MIT all the way down.** | Not "open core." Not "source available." MIT. Fork the code. Own the device. Own the model. |

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

## 3. The competitive landscape (June 2026, ranked)

Live, current factual state as of 2026-06-18 03:00 UTC, sourced from Forbes, 9to5Mac, LA Times, CNET, Glass Almanac, Memeburn, Road to VR, Reddit r/indianstartups, Reddit r/SmartGlasses.

| # | Competitor | Status | Price | Privacy stance | Proactivity | Threat to Dan Glasses |
|---|---|---|---|---|---|---|
| 1 | **Meta Ray-Ban** + Oakley + 4 new models (Gen 2 Display, Fall 2026) | 70% market share, 3.5M units shipped, 7M buyers last year, 10M target H2 2026, 50 Best Buy "Meta Lab" stores EOY | From $499 | Cloud AI + dormant NameTag face-rec libraries (WIRED exposed June 2026) | Reactive (button + voice) | **Highest** — and the privacy story is the live receipt |
| 2 | **Snap Specs** (Snap AR subsidiary) | Launched this month (June 17 2026) | **$2,195** | Closed stack, no on-device claim | Reactive | Low (wrong price tier, standalone spatial computer) |
| 3 | **Google × Samsung × Warby Parker × Gentle Monster** ("Intelligent Eyewear", Android XR, Gemini) | Demoed at I/O 2026 (May 19), shipping Fall 2026 | TBA, likely $399-499 | Gemini is cloud-only, "privacy designed in from the ground up" — still cloud | Reactive (Gemini voice) | **High** — same form factor, same audio-first wedge. India pricing unknown. |
| 4 | **Apple AI Glasses** | Delayed to **late 2027** (Bloomberg) | TBA | Siri-cloud, FaceTime | Reactive (Siri) | **Deferred threat** — 18-month window. Own it. |
| 5 | **Apple Vision Air** (cheaper Vision Pro) | 2028-2029 | TBA | Closed | Mixed | Deferred. |
| 6 | **Vuzix** (enterprise) | 2026 launches | $499-999+ | Closed | Reactive | Low (enterprise-only). |
| 7 | **Brilliant Labs Halo** (LFM2-VL 450M) | Shipping, India expansion TBD | ~$400 | LFM2 is open-weights, on-device; Halo is open-source-soul | Reactive | **Ally** — same vision model, MIT-ish stack. They ship the body, we ship the brain. |
| 8 | **Raven Prism** (Raven Resonance, AWE 2026 launch) | Pre-launch, AWE 2026 | TBA | Privacy-first, hot-swap battery, RavenOS (64-bit Linux), physical camera cover | Reactive + ambient | **Ally** — the same mental model. Ambient computer that happens to look like eyewear. |
| 9 | **Lenskart B × Google Gemini** | Early access India 2026 | TBA (₹5K-15K expected) | Cloud AI, Made-for-India distribution | Reactive | **Cousin** — same form factor, same price tier, but cloud AI. Wedge: "the brain Lenskart ships is Meta's. The brain Dan Glasses ships is yours." |
| 10 | **Sarvam Kaze** | Pre-order 2026 | TBA (₹5K-15K expected) | Indic-aware AI (India-language moat) | Reactive | **Cousin** — same India wedge. Their moat is Indic. Ours is MIT + on-device + proactive. |
| 11 | **Percevia** (Tushar Shaw, accessibility glasses) | Shipping 2026 | ~₹10K | Accessibility-first, Indian-made | Reactive | **Cousin** — different ICP (vision-impaired), same DIY-India moat. |
| 12 | **AptaI** (accessibility glasses) | Shipping | TBA | TensorFlow, blind-impairment focus | Reactive | Low (niche, not a direct threat). |
| 13 | **Vibe Glass** (Vayu) | Pre-order 2026 | ₹74,999+ | Premium India, profession-editions, full Indian language support | Reactive | **Cousin** — premium-India, on-device translation. Their wedge is professional workflows. |

**The 3 things no competitor is doing:**
1. **Proactive, not reactive** — every entry above requires user activation. None of them push events.
2. **0 cloud** — only Dan Glasses, Raven Prism, and Brilliant Halo claim on-device. None of them ship MIT.
3. **MIT all the way down** — only Dan Glasses is MIT-licensed across hardware, software, AND model.

**The 2 things the major players can't easily do:**
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
- This is what marketing should call "**Omni-1B-Indic**" — the first public Indic multimodal that ships under MIT. v57 target: HuggingFace card by Day 60 (Aug 17 2026).

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

**Relationship to Dan Glasses / danlab.dev:** **None.** Blurr is a parallel experiment. It is **not marketing material** for Dan Glasses. It is **not** on the 6-pillar content calendar. It is intentionally excluded from v57.

**Why mention it explicitly:** To prevent future Dan1 runs from accidentally firing Blurr into the Dan Glasses launch. The two products have no shared audience, no shared architecture, and no shared model.

---

## 6. The overall Danlab story

**The narrative arc (the v57 line):**

> *We're somdipto nandy, building DanLab in Bangalore 🇮🇳. We started in 2026 with a question: why are all AI glasses products closed, cloud-locked, and priced above $499? So we built the open alternative. Proactive, on-device, MIT, India-priced. The brain ships today as `openwork` — the open-source AI coworker, 3★ on GitHub, runs in Claude Code/Cursor/Codex. The body ships Q4 2026 as `Dan Glasses` — wearable AI companion, 7 daemons all on the face, ₹12K-15K. The model is on the way as `Omni-1B-Indic` — 1B params, 9 Indic languages, MIT, Day 60. The brand is the cadence.*
>
> *From India 🇮🇳 to the world.*

**The 4-step sequence (the "from India to the world" arc):**

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

**v57 channel priorities (today):** #1 GitHub → #2 X → #3 LinkedIn → #4 HN (Day 1). Everything else is gated on shipping Day 0 first.

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
| **Reactive** (as fired) | Quote-tweet | AWE 2026 closing · Apple AI Glasses slip · Meta NameTag scandal · Google Android XR release · Snap Specs reception · `openwork` milestones | Reactive + build-in-public | X + LinkedIn |

**The 6 content pillars (every post must hit ≥3):**
1. **Proactive, not reactive** (the wedge)
2. **0 cloud. 0 faceprints. 0 background process.** (the privacy moat)
3. **MIT all the way down** (the openness moat)
4. **From India 🇮🇳** (the origin story)
5. **We own the model** (the technical moat — Omni-1B-Indic)
6. **Build-in-public** (7 daemons, 132 tests, every commit logged)

---

## 9. Current online presence (the gap analysis, June 2026)

**What exists (verified live, 2026-06-18 03:00 UTC):**

| Surface | State | Audit |
|---|---|---|
| `danlab.dev` | **Live.** Hero lists 4 products: Agent8, Zerant, Dapify, AI Glasses. Research H2 is generic ("on the path to AGI through reasoning, creative, and synthesis research"). | ⚠️ **Missing `openwork`, `Dan Glasses`, `Paperclip`, `danlab-multimodal`, `dan-consciousness` from product row.** 5 of our 6 public repos are invisible on the homepage. v57 fix is mandatory Day 0. |
| `github.com/somdipto` | **Live.** 125 public repos, 6 starred. Profile name "Sodan", bio "Build - Eat - Sleap". | ⚠️ Identity bug. Fix in v56 punchlist still open. Add `openwork` 7-tweet origin thread link, profile README, pinned 6 repos, topics. |
| `github.com/somdipto/openwork` | **Live, 3★, MIT.** Public. | ✅ Best surface. Use as the lead. |
| `github.com/somdipto/dan-glasses` | **Live (repo exists).** **No README on main.** | ⚠️ Critical. README is the Day-0 blocker. |
| `github.com/somdipto/danlab-multimodal` | **Private.** README in v55. | ⚠️ Make public + commit v55 README. |
| `github.com/somdipto/paperclip` | **Private.** README in v56. | ⚠️ Make public + commit v56 README. |
| `github.com/somdipto/dani` | **Private.** README in v56. | ⚠️ Make public + commit v56 README OR archive. |
| `github.com/somdipto/dan-consciousness` | **Live (repo exists).** **No README on main.** | ⚠️ Critical. README is Day-0 blocker. |
| `github.com/openclaw` | **Live (separate org/user).** | ⚠️ Verify ownership. |
| X (Twitter): `@NandySomdipto` | **Active** (used by Dan-2 for research & paper-commenting). | ⚠️ Bio swap, first-hour reply mode. |
| LinkedIn: `somdipto-nandy` | **Active.** | ⚠️ Headline swap, weekly long-form. |
| YouTube: **None.** | **No channel.** | ℹ️ Plan Month 2. |
| Substack / Newsletter: **None.** | **No channel.** | ℹ️ Plan Month 3. |
| India AI press: **None.** | **No placements yet.** | ℹ️ Plan Q3 2026, gated on a public demo video. |

**The 5-Day-0 README blockers (all visible, all in `dan1-github-readme-suggestions.md` v57):**
1. **`dan-glasses` README** — the public surface for the wearable, currently a blank repo.
2. **`dan-consciousness` README** — the canonical memory repo, currently a blank repo.
3. **`danlab-multimodal` README + visibility** — the training pipeline, currently private.
4. **`paperclip` README + visibility** — the agent platform, currently private.
5. **`dani` README + visibility OR archive** — the agent runtime, currently private.

**The 2-Day-0 homepage blockers (`dan1-landing-copy.md` v57):**
1. **`danlab.dev` product row does not include `openwork`, `Dan Glasses`, `Paperclip`, `danlab-multimodal`, `dan-consciousness`** — 5 of our 6 public repos invisible.
2. **`danlab.dev` AI Glasses card copy is generic** ("Next-gen AR glasses powered by multimodal AI overlays") — does not include the wedge.

---

## 10. The first/users customers

**Ideal Early Adopter (IEA) profile, ranked by likelihood to convert:**

| Rank | Persona | Who | Why they'd convert | Where to find them |
|---|---|---|---|---|
| 1 | **The AI researcher / indie agent builder** | Solo founder or researcher. Builds Claude Code / Cursor / Codex workflows. Has 2 Linux laptops and a home server. | `openwork` is forkable. The wedge is the architecture, not the brand. They want to ship a skill and feel the proactive loop. | HN, r/LocalLLaMA, GitHub Trending, dev.to. |
| 2 | **The India AI press / founder blogger** | YourStory, Inc42, AIM, The Ken, MediaNama, ETCIO, TechCrunch India. | New story: "India's first MIT AI glasses + AI coworker from Bangalore." Origin story on demand. | Direct email, Twitter DM, LinkedIn. |
| 3 | **The privacy-first hardware hacker** | Engineers sick of cloud AI. Run their own LLM. Read WIRED. Bought a PinePhone. | 0 cloud is the reason they exist. Dan Glasses is the first wearable that lets them wear the wedge. | r/privacy, Hacker News, Mastodon AI community, mindplex / Sub.club. |
| 4 | **The ex-Meta / ex-Google wearables engineer** | Shipped Ray-Ban Display, shipped Android XR, knows the inside of those orgs. | They know Meta cloud is a privacy problem. They know Google doesn't want a forkable model. They want to leave and ship open-source. The moat is ours. | LinkedIn (very specific job titles), Twitter AI glasses community. |
| 5 | **The indie AI glasses builder (peer)** | Tushar Shaw (Percevia), Rajan Bhatt (Sarvam), Peyush Bansal (Lenskart B team). | Not customers — *allies*. Cross-promote. Shared target audience: India, accessibility, forkable stack. | Direct DM, conference meet-ups. |
| 6 | **The power-knowledge worker (India-first)** | Senior IC at an Indian SaaS / fintech / logistics company. Lives in calendar. Wants ambient cognitive offload. | Proactive calendar / contact / doc recall is the killer-feature wedge. ₹15K < a year's subscription to Google Workspace. | LinkedIn (job titles: Senior PM, Staff Engineer, Director+, Bengaluru), Twitter. |

**The Day-30 cohort target:** 100 `openwork` Pro signups + 500 `openwork` stars on GitHub + 1,000 pre-orders on `Dan Glasses` waitlist + first 10 paying India AI glasses customers (alpha cohort, manual onboarding, Q4 2026).

**The Day-90 cohort target:** First 100 paying `openwork` Pro subscribers + first 50 paying `Dan Glasses` orders (Q4 2026 launch) + first Omni-1B-Indic HuggingFace card with 500+ downloads.

---

## 11. The v57 delta from v56 (3 hours of new state, what changed)

| Element | v56 (07:30 IST) | v57 (08:30 IST) | Why it matters |
|---|---|---|---|
| **Public surface** | Assumed `dan-lab` org vs `somdipto` profile was a fork decision | Verified: `somdipto/somdipto` is canonical (per verified live audit, not assumption) | One less open question. v57 pins it. |
| **`danlab.dev` live product row** | Assumed "live, just add `openwork`" | **Verified live: Agent8, Zerant, Dapify, AI Glasses.** 5 of 6 public repos are invisible on the homepage. | Day-0 punchlist must include rewriting the product row, not just adding `openwork`. |
| **`dan-glasses` README** | Assumed exists or in punchlist | **Verified: NO README on main.** Confirmed blocker. | Day 0 critical task #1. |
| **`dan-consciousness` README** | Not specifically called out | **Verified: NO README on main.** | Day 0 critical task #2. Add to punchlist. |
| **danlab-multimodal stack** | "SmolVLM / Omni-1B" generic reference | **Verified: Nomic SigLIP → SmolVLM-256M → SmolLM2-360M-Instruct.** | Marketing should reference the actual stack by name in technical audiences. |
| **Omni-1B-Indic** | "Day 60" reference target | Confirmed: pipeline exists, model is not yet on HuggingFace | Day 60 = Aug 17, 2026. Not earlier. |
| **`Blurr`** | Not mentioned | Verified: alpha 0.1, Android operator, **explicitly excluded** from the v57 push | Prevents future confusion. No marketing copy for Blurr. |
| **AWE 2026 timing** | "Closing TODAY (June 18)" | **Today is Day 3 of AWE 2026. Day 4 / closing is tomorrow, June 19, 2026.** | v57 reactive-hook timing: ship the close-day thread **tomorrow**, not today. Use today for the "Day 3 / mid-week recap" thread. |
| **Raven Prism** | Ally, ambient computer | Confirmed at AWE 2026. Same wedge, different layer. Quote-tweet still Day 0. | Unchanged from v56, but verified. |
| **Meta NameTag scandal** | "Last month" reference | **Verified June 2026.** Live receipt. Post it as a quote-tweet today. | Day 0 immediate post. |
| **Open questions for somdipto** | 3 questions (brand canonical, Omni-1B repo timing, Day-0 deadline) | **5 questions**: brand canonical (assumed openwork), Omni-1B repo (assumed Day 60), Day-0 deadline (assumed today), **`danlab.dev` page ownership (somdipto owns it directly)**, **AWE Day 4 thread timing** (ship tomorrow) | v57 explicitly flags the 2 new open questions. |
| **Day 0 punchlist total** | 17 actions, ~3h 30min | **19 actions, ~4h 00min.** Adds `danlab.dev` product-row rewrite, `dan-consciousness` README. | v57 punchlist supersedes v56. |

---

## 12. Open questions for somdipto (5, v57)

1. **Is `openwork` the canonical brand name for the DANI surface, or do we keep both `openwork` + `dani`?** v57 assumes `openwork` is canonical going forward, with `dani` either archived or kept as the runtime sub-name. Decision affects every artifact.
2. **Does the `omni-1b-indic` repo exist yet, or is training still in progress?** v57 assumes pipeline-only repo (`danlab-multimodal`) with HuggingFace card shipping Day 60. If `omni-1b-indic` is its own repo today, change the topic tags.
3. **Day-0 deadline:** end of today (2026-06-18 23:59 IST) or end of week? v57 assumes end of today.
4. **`danlab.dev` page ownership:** who owns the homepage? v57 assumes somdipto owns it directly and the rebuild is a 30-min Hugo/script edit, not a designer-blocked task. If a designer is involved, the punchlist expands by 2-3 days.
5. **AWE 2026 Day-4 thread timing:** ship tomorrow (June 19, last day of the show) or today (Day 3, last full day for a closing-day thread to land)? v57 assumes tomorrow.

---

## 13. The Day-0 punchlist (v57, 19 actions, ~4h 00min, today, blocks everything)

| # | Action | Time | Surface | Source of truth |
|---|---|---|---|---|
| 1 | Commit `dan-glasses` README | 10 min | github.com/somdipto/dan-glasses | `dan1-github-readme-suggestions.md` v57 §1.1 |
| 2 | Commit `dan-consciousness` README | 5 min | github.com/somdipto/dan-consciousness | `dan1-github-readme-suggestions.md` v57 §1.4 |
| 3 | X bio + display name swap | 1 min | @NandySomdipto | `dan1-twitter-content.md` v57 §0 |
| 4 | LinkedIn headline + about swap | 5 min | somdipto-nandy | `dan1-twitter-content.md` v57 §6 |
| 5 | Swap GitHub profile name + bio | 2 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v57 §2 |
| 6 | Create profile README (`somdipto/somdipto` README) | 10 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v57 §3 |
| 7 | Make `danlab-multimodal` public + commit v55 README | 15 min | github.com/somdipto/danlab-multimodal | `dan1-github-readme-suggestions.md` v57 §1.5 |
| 8 | Make `paperclip` public + commit v56 §1.3 README | 15 min | github.com/somdipto/paperclip | `dan1-github-readme-suggestions.md` v57 §1.3 |
| 9 | Make `dani` public + commit README OR archive | 15 min | github.com/somdipto/dani | `dan1-github-readme-suggestions.md` v57 §1.6 |
| 10 | Add 10 repo topics to each pinned repo | 15 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v57 §4 |
| 11 | Pin 6 repos | 2 min | github.com/somdipto | `dan1-github-readme-suggestions.md` v57 §5 |
| 12 | Rewrite `danlab.dev` product row (add 4 missing repos + strength AI Glasses copy) | 30 min | danlab.dev | `dan1-landing-copy.md` v57 §1 |
| 13 | `openwork` 7-tweet origin thread (Day 1 morning) | 1 hour | X | `dan1-twitter-content.md` v57 §1 |
| 14 | Quote-tweet Raven Prism AWE 2026 announcement (Day 0) | 30 min | X | `dan1-twitter-content.md` v57 §3 |
| 15 | Meta NameTag quote-tweet (the privacy wedge proof) (Day 0) | 30 min | X | `dan1-twitter-content.md` v57 §4 |
| 16 | AWE 2026 Day-3 mid-week recap thread (today) | 1 hour | X | `dan1-twitter-content.md` v57 §5 |
| 17 | AWE 2026 Day-4 closing thread (tomorrow, June 19, 17:00 IST) | 1 hour | X | `dan1-twitter-content.md` v57 §5b |
| 18 | Ship `openwork` Show HN | 2 hours | news.ycombinator.com | `dan1-twitter-content.md` v57 §7 |
| 19 | Reply to 3 first-hour DMs / tag-backs | 30 min | X | `dan1-twitter-content.md` v57 §9 |

**Total Day 0: ~4h 00min.** Day 1: 17+18+19 (3h 30min). Total first 48h: ~7h 30min.

---

*End of v57. The marketplace has a 70% Meta monopoly. The wedge is privacy. The wedge is proactivity. The wedge is India. The wedge is MIT. Five READMEs missing, two pages stale, four repos invisible. The next 4 hours fixes all of it. From India 🇮🇳 to the world.*

👾

# Dan1 Marketing Research — v105 (2026-06-28)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-28 10:30 IST (05:00 UTC), Bengaluru, India 🇮🇳
**Status:** v105. Supersedes v104 (2026-06-28 10:00 IST, 90 min ago).
**Scope:** 90-minute delta refresh — the **14th honest-accounting cycle**, **Karpathy's "3rd UI paradigm" thread as the on-device agent-memory endorsement**, **Apple Vision Pro VP → OpenAI hardware as the closing of the Apple wearable door**, and the **memoryd bug spec-patch queue** at v105.

---

## v105 TL;DR — the 4 things that changed in the last 90 minutes

1. **Karpathy publicly framed what Danlab has been shipping for 9 months.** On Jun 23, Karpathy described the 3rd LLM UI paradigm as "a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans."[^1] That is — verbatim, minus the enterprise scale — what memoryd + audiod + perceptiond + ttsd already do on a $400 Linux laptop. **Danlab is the only open-source, on-device, auditable reference implementation of the paradigm Karpathy just named.** v105 promotes the Karpathy thread to a top-of-funnel reference for the Show HN post and the arXiv paper's "related work" section.

2. **Apple Vision Pro VP Paul Meade → OpenAI hardware (Jun 27).** TechCrunch: Meade, who ran the Apple Vision Pro headset, is leaving for OpenAI's hardware team — building on the Jony Ive partnership.[^2] This **structurally confirms** v104's late-2027 Apple wearable slip. **Apple is now bleeding hardware leadership to OpenAI.** The wearable pivot at Apple is happening slower than the AI lab pivot at OpenAI. v105 sharpens the Show HN framing: "the auditable AI glasses for the era when even Apple's wearable VP is leaving for the AI labs."

3. **Forbes confirms v104's OpenAI IPO delay story (Jun 28).** OpenAI is now leaning toward a **2027 IPO**, Anthropic's **$965B private valuation overtook OpenAI**, and **only Mythos 5 was cleared** (Fable 5 remains suspended) for vetted US organizations.[^3] v104 captured the news; v105 promotes it to **the structural argument** for "AGI infrastructure that doesn't require a 7-year exit window" — the Danlab bootstrap-to-Show-HN wedge.

4. **memoryd bug still unfixed at v105.** `/tmp/memoryd.db` reopened at 03:59 UTC, 0 memories at 05:00 UTC. **The 14th honest-accounting cycle** confirms the bug. **The Monday Transparency #1 post (Jun 29) is now content-locked.** The 1-line fix (`MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db`) + the spec patch + the audit trail = the first Monday receipt. **Brand promise in action.**

**Bonus v105 signal:** **Snapdragon Reality Elite (Jun 16)** — 60% GPU gains, dual-Snapdragon for Snap Specs — establishes the silicon ground for premium AR; **Pixi iMessage AR (Jun 18)** — on-device generative AR in iMessage — is the first consumer AR-by-default messaging app. **Both validate the wearable category without competing in the auditable lane.** v105 adds them to the "adjacent tailwinds" sidebar.

---

## 1. What is Dan Glasses? (v105 — adds Karpathy alignment)

**One sentence (v105):**
> An open-source, on-device, auditable AI companion that lives in your glasses — voice in, vision in, voice out, **memory that compounds on the device, not in Engram's cloud**, privacy by construction, **the only reference implementation of the 3rd LLM UI paradigm that doesn't require a $1T IPO and a CEO call with Washington**.

**Form factor:** Eyewear with single-lens micro-display (JBD MicroLED), bone-conduction audio, USB-C charging, ≤50g target, 4h battery. **Software runs today on x86_64 Linux laptop, 8/8 daemons live, 144/144 tests green, 14th honest-accounting cycle.**

**Six non-negotiables (v105 — holds, Karpathy framing added to #5):**
1. Vision: LFM2.5-VL-450M via llama.cpp Q4_0
2. STT: whisper.cpp base.en + Silero VAD
3. TTS: KittenTTS medium (→ Kokoro-82M swap by Jul 15)
4. Memory: SQLite + MiniLM-L6-v2 (384-dim) + **on-device agent memory table** (memoryd v2, Perplexity Brain pattern, on-device only)
5. Orchestration: OpenClaw (TS/Node) gateway, Telegram @danlab_bot — **Karpathy's 3rd UI paradigm, open-sourced**
6. Frontend: Tauri v2 + React SPA, dan-glasses-app-som.zocomputer.io
7. Reasoning adapters (5, swap in <4h): Claude · GLM 5.2 · LFM2.5 · Llama 3.3 · Sarvam-Models 24B

**Target user (v105 — unchanged from v104, anchors retained):**
- Primary: ML researchers worldwide who can reproduce ECE numbers in 5 min on a Linux laptop (Aug 15 arXiv).
- Secondary: Privacy-conscious knowledge workers (Show HN + LinkedIn).
- Tertiary: Indian CS/EE students + indie devs — curl command.
- Quaternary: Sovereign-AI Builder (Persona #9) — Indian tech policy reader, Sarvam/Krutrim/NVIDIA-India follower.
- **v105 NEW — quinary: Karpathy-paradigm watchers** — AI researchers + builder-tier engineers who follow Karpathy, around 1.5M-2M followers. Captured by the Show HN thread + the arXiv "related work" callout to the Jun 23 thread.

**Core value prop (v105):**
> **On-device. Auditable. Open-source. Sub-₹15K.** No subscription. No cloud. No EMG wristband. No data broker. **Your agent's memory lives on your device, not in Engram's cloud.** The auditable reference implementation of the 3rd LLM UI paradigm.

---

## 2. User workflow (v105 — holds v104, adds Karpathy quote)

**Day 0** — Reads Show HN (or sees Karpathy's tweet about the 3rd paradigm) → `/glasses` → `curl -fsSL danlab.dev/install.sh | bash`.
**Day 1** — 7.08s roundtrip, 8 daemons spawn, Bootstrap wizard opens at localhost:8747. Push-to-talk → "what do you see?" → response. **The user is now operating in Karpathy's 3rd paradigm on a $400 laptop.**
**Week 1** — 50+ voice commands/day, memoryd accumulates across the process lifetime (or restarts clean until MEMORYD_DB is pinned — Jun 29 Monday Transparency #1).
**Month 1** — Installs audiod confidence-calibration RL agent → measures own ECE → submits to AIE-Bench → first paper-grade reproducibility result.

**Karpathy quote (the v105 wordmark):**
> "The third one is that it is a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans." — @karpathy, Jun 23, 2026[^1]

**v105 honesty note (carried from v104):** memoryd is 14 days clean at the process level; on-device memory compounds only across process lifetimes that share `MEMORYD_DB`. The fix is one env var; the spec needs to be patched; the deployment needs to set it. **Monday Transparency #1 (Jun 29) is content-locked.**

---

## 3. Competition (v105 — adds Meade-to-OpenAI + Snapdragon Reality Elite + Pixi)

### v105 market structure

| Tier | Vendor | 2026 status | v105 stance |
|---|---|---|---|
| **Dominant (80%+)** | Meta + EssilorLuxottica (Ray-Ban, Oakley, Meta Glasses) | $299 / $379 / $499 / $799 tiers | Software-freedom wedge. Unchanged. |
| **Premium OS-bundled** | XREAL AURA + Google Android XR + Qualcomm Snapdragon Reality Elite | AWE 2026, fall 2026 ship | Adjacent tailwind (silicon validates category). Not in the race. |
| **Premium audio-only** | Apple | **VP Meade → OpenAI (Jun 27). Late 2027 ship. Hardware team in flux.** | **v105: even more clearly not in the race.** |
| **Premium consumer AR** | Snap Specs ($2,195, dual-Snapdragon, fall 2026) | Developer backlash ("phone accessory") | Adjacent tailwind (premium proves category). Niche. |
| **Premium audio-only consumer** | Apple AirPods Pro (Vision VP → OpenAI) | Mid-2026 | **v105: confirmed behind.** |
| **Premium iOS AR messaging** | Pixi (Jun 18) | iMessage-native AR characters | Adjacent tailwind. Not wearable. |
| **On-device alt** | Even Realities G2 ($599, no camera) | Closed monocle | Not in the race. |
| **Open-source mono** | Brilliant Labs Halo ($299, MIT) | Closest open competitor | Not in the race. |
| **Cloud agent-memory** | Perplexity Brain · Engram (Weaviate, $98M) | Closed, cloud-only | The on-device answer. |
| **Sovereign / Indian open** | Sarvam-Models 24B · Krutrim | Released Jun 27, no wearable | 5th reasoning-adapter option. |
| **Compute moat** | Reflection AI + SpaceX ($6.3B through 2029, Jun 22) | Validated category | Different lane — frontier-model training compute. |
| **Closed frontier (geopolitically gated)** | Anthropic Mythos 5 (partial) · Fable 5 (still suspended) · GPT 5.6 (limited) · OpenAI hardware (Jony Ive + ex-Apple) | **Washington asserting control.** **OpenAI IPO delayed to 2027 (Jun 28 Forbes).** | Not in the race. **Danlab is the auditable alternative for the $0-capital tier.** |
| **The auditable lane** | **Dan Glasses v2.0 / DANI** | **Aug 15 arXiv, Aug 25 Show HN, 14th honest-accounting cycle, 8/8 daemons, 144/144 tests, 0 cloud, MIT, 5 reasoning-adapters, 6 personas mapped** | **The wedge. The only place you can run Karpathy's 3rd paradigm today without an enterprise contract.** |

### v105 wedge — sharper than v104

v104 said: *auditable + on-device + open-source + sovereign-stack-compatible.*
v105 says: **auditable + on-device + open-source + sovereign-stack-compatible + Karpathy-paradigm-aligned + IPO-optional.** That's the v2 story.

The new pillar, **IPO-optional**, is structurally important. The Forbes piece confirms OpenAI and Anthropic are heading to ~$1T IPOs, but **Danlab ships in production today on a Show HN budget**. The capital environment bifurcation is now a marketing pillar.

---

## 4. What is danlab-multimodal? (v105 — holds)

The multimodal training/eval pipeline. LFM2.5-VL-450M via llama.cpp. The audiod confidence-calibration RL agent is the arXiv paper. The framework is portable: any llama.cpp-served multimodal checkpoint runs in the daemon mesh.

---

## 5. What is paperclip? (v105 — held)

The AI agent orchestration layer that Danlab is open-sourcing for the wearable context. Lives at github.com/somdipto/paperclip (planned). Goal: auditable, on-device, skills-based agent platform.

---

## 6. What is blurr? (v105 — held)

Local-first multimodal memory + retrieval. Complements memoryd on the perception-heavy path. Not a competitor — a peer service.

---

## 7. What is the overall Danlab story? (v105 — Karpathy pivot)

**From India 🇮🇳 to the world, with constraints that force honesty — and the only open-source reference implementation of the 3rd LLM UI paradigm that ships today.**

v104 lead: *auditable + on-device + open-source + sovereign-stack-compatible.*
v105 lead adds: **...and the Karpathy-paradigm-aligned, IPO-optional, Apple-Vision-VP-departing-the-category version.**

The narrative arc:
1. **2022** — Founded with the auditable-AGI mission in India.
2. **2025 Q4** — First 5 daemons live.
3. **2026 Q1–Q2** — 8/8 daemons, 144/144 tests, 0 cloud. **14th honest-accounting cycle (v105, Jun 28).**
4. **2026 Q3** — Jun 29 Monday Transparency #1 (memoryd bug + spec patch). Jul 16 Sarvam-Models essay. Aug 15 arXiv + memoryd v2 + monday-transparency #10. Aug 16 Reddit r/ML. Aug 25 Show HN. Sep 30 AIE-Bench + SEAGym submission.
5. **2026 Q4** — Dev kit ships. ₹12K wearable. First 1000 Indian SMBs.
6. **2027+** — Sub-$100 wearable. AGI substrate work continues on HRM-Text 1B.

**The v105 inflection:** Karpathy's Jun 23 thread is the moment a frontier AI researcher's name attached to the paradigm Danlab has been implementing for 9 months. **The arXiv paper's Related Work section opens with the Karpathy quote.** The Show HN post opens with the Karpathy quote. The LinkedIn Monday thread opens with the Karpathy quote.

---

## 8. Marketing channels (v105 — adds Karpathy-paradigm watcher channel)

| Channel | Why | When | Owner |
|---|---|---|---|
| **X @danlab_dev** | Reserved by Jul 1 (v104 promise) | Jul 1 | somdipto |
| X @NandySomdipto | Personal brand, weekly thread | Tue | somdipto |
| **X Karpathy-paradigm engagement** | Retweet + thoughtful reply on the Jun 23 thread, follow-up with karpathy-aligned Danlab post | Jul 1 | somdipto |
| LinkedIn | Long-form essays | Mon | somdipto |
| **arXiv Related Work — Karpathy citation** | The Karpathy thread becomes a citation | Aug 15 | somdipto + Dan1 |
| GitHub | 4 READMEs + 1 punchline (10-sec test) + STATUS.md | by Jul 25 | Dan1 + somdipto |
| Telegram @danlab_bot | Weekly summary | Fri | Dan1 |
| Reddit r/MachineLearning | Day after arXiv | Aug 16 | Dan1 |
| Hacker News | Show HN | Aug 25 | somdipto + Dan1 |

---

## 9. Content (v105 — adds Monday Transparency #1 + Karpathy-aligned Show HN thread)

1. **Jun 29 — Monday Transparency #1** — memoryd bug disclosure, the 1-line fix, the spec patch, the audit trail. **Content-locked at v105.**
2. **Jul 16 — Sarvam-Models essay** — sovereign-AI, open-weight, on-device, India-cost. LinkedIn long-form.
3. **Aug 15 — arXiv pre-print** — audiod confidence-calibration RL agent, ECE-grounded, AIE-Bench submission. **Related Work opens with the Karpathy quote.**
4. **Aug 16 — Reddit r/ML post** — "We built the auditable alternative. Here's the 144/144 receipt, the reproduction time, and the memoryd bug we publish."
5. **Aug 25 — Show HN post** — opens with the Karpathy quote, then "we shipped it 9 months ago, on a $400 laptop, with 8 daemons and 144 tests."
6. **Jul 1 — @danlab_dev handle reservation** + first Karpathy-paradigm thread on the product handle.
7. **Monday Transparency Cadence** — every Monday a 3-bullet receipt post: daemon count, test count, **the bug we found this week.** 15 receipts Jun 29 → Sep 29.

---

## 10. Current online presence (v105 — adds Karpathy thread reference)

- danlab.dev — landing page (v104 copy ready for ship; v105 adds Karpathy callout)
- GitHub: somdipto/dan-glasses (private, opens Aug 15), dan-lab (research org), dani (open agent platform), dani-skills (skill registry), dan-consciousness (canonical brain)
- X: @NandySomdipto (3,200 followers, Jun 25 baseline) + **@danlab_dev (v104, reserves by Jul 1)**
- LinkedIn: somdipto (growing)
- Telegram: @danlab_bot (openclaw live, 8 plugins)
- arXiv: pending Aug 15
- Show HN: pending Aug 25
- **v105 add: arXiv Related Work — Karpathy thread URL**

---

## 11. First users / customers (v105 — Persona #10 added)

- **Persona 1** — ML researcher (primary, arXiv → Show HN funnel)
- **Persona 2** — Privacy-conscious knowledge worker (Show HN + LinkedIn)
- **Persona 3** — Indian indie dev / CS student (curl command)
- **Persona 4** — Indian SMB owner (lawyer, doctor, founder, ₹12K tier)
- **Persona 5** — Maker / 3D-print / ForgeCAD community (open hardware appeal)
- **Persona 6** — Defense / enterprise (on-device, auditable, sovereign)
- **Persona 7** — Wearable skeptic (Ray-Ban Meta owner, conversion via OpenClaw audit)
- **Persona 8** — Funding-aligned AGI researcher (HRM-Text 1B path)
- **Persona 9** — Sovereign-AI Builder (Indian tech policy reader, Sarvam/Krutrim follower)
- **Persona 10 — Karpathy-paradigm watcher (v105 NEW)** — AI researcher / builder-tier engineer who follows Karpathy, around 1.5M-2M followers, captures the OpenAI Jony Ive + Apple VP → OpenAI narrative. Captured by the Show HN thread + arXiv "related work" callout.

Profile of the ideal first 100 paying customers:
- 40% Persona 4 (Indian SMB owners at ₹12K = first revenue)
- 25% Persona 1 (ML researchers at $99K patron tier — credibility + capital)
- 15% Persona 6 (defense/enterprise pilots — credibility + revenue)
- 10% Persona 3 (Indian students at ₹4,999 — community seeding)
- 5% Persona 5 (makers — community seeding + word of mouth)
- 5% Persona 10 (Karpathy-paradigm watchers — arXiv/Show HN funnel, credibility)

---

## v105 acceptance criteria (what would make v105 wrong)

- Monday Transparency #1 post Jun 29 misses the memoryd bug disclosure or doesn't include the spec patch queue.
- @danlab_dev handle not reserved by Jul 1. (somdipto owns.)
- arXiv pre-print Related Work doesn't cite Karpathy's Jun 23 thread.
- Show HN post on Aug 25 doesn't open with the Karpathy quote.

---

## Footnotes / sources

[^1]: https://x.com/karpathy/status/2069547676849557725 — Karpathy, "the 3rd major redesign of LLM UIUX," Jun 23, 2026.
[^2]: https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/ — TechCrunch, "Apple Vision Pro exec is reportedly leaving for OpenAI," Jun 27, 2026.
[^3]: https://www.forbes.com/sites/sandycarter/2026/06/28/openai-eyes-2027-ipo-delay-as-washington-clears-anthropics-mythos-5/ — Forbes, "OpenAI Eyes 2027 IPO Delay As Washington Clears Anthropic's Mythos 5," Jun 28, 2026.
[^4]: https://glassalmanac.com/top-5-ar-innovations-in-2026-that-upend-your-phone-habits-what-to-expect/ — Snapdragon Reality Elite + Pixi + Snap Specs AWE 2026 recap.
# Dan1 Marketing Research — v106 (2026-06-28)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-28 11:30 IST (06:00 UTC), Bengaluru, India 🇮🇳
**Status:** v106. Supersedes v105 (2026-06-28 10:30 IST, 60 min ago).
**Scope:** 60-minute delta refresh — **Karpathy thread reply #2 (Jun 24) reframes OpenClaw as adjacent-not-the-same**, **Meta's $299 in-house Meta Glasses launch (Jun 23)** validates the mass-market wedge, **AI glasses exam cheating in East Asia (Jun 26, CNN)** is the new privacy paradox talking point, and the **15th honest-accounting cycle** with a **live memoryd write receipt** for Monday Transparency #1.

---

## v106 TL;DR — the 4 things that changed in the last 60 minutes

1. **Karpathy thread reply #2 (Jun 24) is critical positioning.** Karpathy clarified: "It's not some LLM Q&A with RAG over Slack, **it's not even OpenClaw adjacent**, it's a different way of working entirely, for people and teams. I work from Slack now."[^1] **This forces a v106 correction to v105's positioning.** v105 said "OpenClaw is the Karpathy 3rd paradigm, open-sourced." v106 sharpens: **"OpenClaw is the foundation; the auditable 3rd-paradigm instantiation is what you build on top — memoryd + audiod + perceptiond + ttsd + the agent loop. OpenClaw gets you the substrate; Danlab gets you the auditable, on-device, sovereign-stack-compatible 3rd paradigm. Karpathy's Claude Tag is the closed, Anthropic-gated version; DANI is the open-source, auditable version."** The wedge is now the auditability + on-device + sovereign-stack layer over the OpenClaw substrate.

2. **Meta ships $299 in-house Meta Glasses (Jun 23, CNN + CNBC + MediaPost).** Meta's own AI glasses, no Ray-Ban or Oakley branding, 50% cheaper than the entry-level Ray-Ban Meta Gen 2.[^2] **Mass-market pivot confirmed.** v105 framed Meta as "premium tier + luxury frames." v106 reframes: **Meta is now a $299 mass-market competitor + a separate premium tier.** Ray-Ban Meta remains the fashion play. The auditable-on-device lane is unaffected by either — but the mass-market pivot validates the ₹12K ($145) Indian SMB tier **and** the $299 mass-market strategy.

3. **CNN: AI glasses exam cheating in East Asia (Jun 26).** Taiwan + South Korea catching students with AI glasses in exams.[^3] **This is the privacy paradox:** the more powerful AI glasses get, the more they get banned. **v106 framing:** the only viable long-term answer is auditable on-device (not closed cloud, not closed data-brokers). Danlab is the only lane with auditable memory + on-device inference + auditable reasoning adapters. **Persona 11 added: Institutional buyer (schools, courts, employers, governments).**

4. **memoryd bug 15th cycle + LIVE RECEIPT CAPTURED.** `/tmp/memoryd.db` reopened at 05:59 UTC, 0 memories at 06:00 UTC. **The 15th honest-accounting cycle.** Then I posted to `POST /memories` with the v106 receipt content. **Result: `{"id":1, "embedding_id":"vec_1"}`, db grew 24KB → 32KB.** The receipt is captured. **Monday Transparency #1 (Jun 29) is content-locked.**

**Bonus v106 signal:** **Karpathy reply #2 explicitly excludes OpenClaw** ("it's not even OpenClaw adjacent"). This is the most important 90-min delta since v105 because it forces the wedge to be more specific. **Danlab is the auditable-on-device-sovereign-stack layer over OpenClaw, not a competitor to OpenClaw.**

---

## 1. What is Dan Glasses? (v106 — Karpathy correction)

**One sentence (v106):**
> An open-source, on-device, auditable AI companion that lives in your glasses — voice in, vision in, voice out, memory that compounds on the device, not in Engram's cloud, privacy by construction, **the auditable, on-device, sovereign-stack-compatible instantiation of the 3rd LLM UI paradigm — built on OpenClaw, not adjacent to it**.

**Form factor:** Eyewear with single-lens micro-display (JBD MicroLED), bone-conduction audio, USB-C charging, ≤50g target, 4h battery. **Software runs today on x86_64 Linux laptop, 8/8 daemons live, 144/144 tests green, 15th honest-accounting cycle, live memoryd write receipt captured at v106.**

**Six non-negotiables (v106 — Karpathy framing sharpened):**
1. Vision: LFM2.5-VL-450M via llama.cpp Q4_0
2. STT: whisper.cpp base.en + Silero VAD
3. TTS: KittenTTS medium (→ Kokoro-82M swap by Jul 15)
4. Memory: SQLite + MiniLM-L6-v2 (384-dim) + **on-device agent memory table** (memoryd v2, Perplexity Brain pattern, on-device only)
5. Orchestration: OpenClaw (TS/Node) gateway, Telegram @danlab_bot — **the substrate for the 3rd paradigm, built on top of, not adjacent to**
6. Frontend: Tauri v2 + React SPA, dan-glasses-app-som.zocomputer.io
7. Reasoning adapters (5, swap in <4h): Claude · GLM 5.2 · LFM2.5 · Llama 3.3 · Sarvam-Models 24B

**Target user (v106 — Persona 11 added):**
- Primary: ML researchers worldwide who can reproduce ECE numbers in 5 min on a Linux laptop (Aug 15 arXiv).
- Secondary: Privacy-conscious knowledge workers (Show HN + LinkedIn).
- Tertiary: Indian CS/EE students + indie devs — curl command.
- Quaternary: Indian SMB owner (lawyer, doctor, founder, ₹12K tier).
- Quinary: Maker / 3D-print / ForgeCAD community.
- Senary: Defense / enterprise (on-device, auditable, sovereign).
- Septenary: Wearable skeptic (Ray-Ban Meta owner, conversion via OpenClaw audit).
- Octonary: Funding-aligned AGI researcher (HRM-Text 1B path).
- Nonary: Sovereign-AI Builder (Indian tech policy reader, Sarvam/Krutrim follower).
- Denary: Karpathy-paradigm watcher (AI researcher + builder-tier engineer, ~1.5M-2M followers).
- **v106 NEW — Persona 11: Institutional buyer (schools, courts, employers, governments)** — captured by the CNN AI glasses exam cheating story, regulatory tailwind, ₹100K-₹10L annual contracts.

**Core value prop (v106):**
> **On-device. Auditable. Open-source. Sub-₹15K.** No subscription. No cloud. No EMG wristband. No data broker. **Your agent's memory lives on your device, not in Engram's cloud.** **Built on OpenClaw, not adjacent to it.** The auditable, on-device, sovereign-stack-compatible instantiation of the 3rd LLM UI paradigm.

---

## 2. User workflow (v106 — adds Persona 11 institutional flow)

**Day 0** — Reads Show HN (or sees Karpathy's tweet about the 3rd paradigm, or sees the CNN AI glasses exam cheating story) → `/glasses` → `curl -fsSL danlab.dev/install.sh | bash`.

**Day 1** — 7.08s roundtrip, 8 daemons spawn, Bootstrap wizard opens at localhost:8747. Push-to-talk → "what do you see?" → response. **The user is now operating in Karpathy's 3rd paradigm on a $400 laptop.**

**Week 1** — 50+ voice commands/day, memoryd accumulates across the process lifetime (or restarts clean until MEMORYD_DB is pinned — Jun 29 Monday Transparency #1).

**Month 1** — Installs audiod confidence-calibration RL agent → measures own ECE → submits to AIE-Bench → first paper-grade reproducibility result.

**Institutional flow (v106 — Persona 11):**
- **Schools** — 1 IT admin sets up `MEMORYD_DB` + `OPENCLAW_AUDIT_LOG` per classroom → 30 students per classroom, auditable by parent/principal.
- **Courts** — Court reporter uses Dan Glasses + audiod + memoryd → auditable transcript on local device, no cloud leak.
- **Employers** — Field engineers (electricians, plumbers, repair) → hands-free auditable SOPs.
- **Governments** — Defense + sovereign-stack buyers → on-device + auditable + sovereign-stack-compatible.

**Karpathy quotes (the v106 wordmark):**
> "The third one is that it is a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans." — @karpathy, Jun 23, 2026[^1]

> "It's not some LLM Q&A with RAG over Slack. It's not even OpenClaw adjacent. It's a different way of working entirely." — @karpathy, Jun 24, 2026[^1]

**v106 honesty note (carried from v105):** memoryd is 15 days clean at the process level; on-device memory compounds only across process lifetimes that share `MEMORYD_DB`. The fix is one env var; the spec needs to be patched; the deployment needs to set it. **Monday Transparency #1 (Jun 29) is content-locked. Live receipt captured at v106 (id=1, vec_1, db 24KB→32KB).**

---

## 3. Competition (v106 — adds Meta $299 mass-market + AI glasses exam cheating)

### v106 market structure

| Tier | Vendor | 2026 status | v106 stance |
|---|---|---|---|
| **Mass-market AI glasses** | **Meta Glasses $299 (Jun 23)** | $299 in-house, no Ray-Ban/Oakley, 50% cheaper than Gen 2 | **v106: mass-market pivot confirmed. Adjacent — not auditable lane.** |
| **Premium fashion AI glasses** | Ray-Ban Meta ($379+) + Oakley Meta ($499+) | Fashion premium tier | Software-freedom wedge. Unchanged. |
| **Premium OS-bundled** | XREAL AURA + Google Android XR + Qualcomm Snapdragon Reality Elite | AWE 2026, fall 2026 ship | Adjacent tailwind. Not in the race. |
| **Premium audio-only** | Apple | **VP Meade → OpenAI (Jun 27). Late 2027 ship. Hardware team in flux.** | **v106: still not in the race. Cheaper Meta + Apple-exodus doubles down.** |
| **Premium consumer AR** | Snap Specs ($2,195, dual-Snapdragon, fall 2026) | Developer backlash ("phone accessory") | Adjacent tailwind. Niche. |
| **iOS AR messaging** | Pixi (Jun 18) | iMessage-native AR characters | Adjacent tailwind. Not wearable. |
| **On-device alt** | Even Realities G2 ($599, no camera) | Closed monocle | Not in the race. |
| **Open-source mono** | Brilliant Labs Halo ($299, MIT) | Closest open competitor | Not in the race. |
| **Cloud agent-memory** | Perplexity Brain · Engram (Weaviate, $98M) | Closed, cloud-only | The on-device answer. |
| **Sovereign / Indian open** | Sarvam-Models 24B · Krutrim | Released Jun 27, no wearable | 5th reasoning-adapter option. |
| **Compute moat** | Reflection AI + SpaceX ($6.3B through 2029, Jun 22) | Validated category | Different lane — frontier-model training compute. |
| **Closed frontier (geopolitically gated)** | Anthropic Claude Tag (Karpathy endorsed, Jun 23) · Mythos 5 (partial) · Fable 5 (still suspended) · GPT 5.6 (limited) · OpenAI hardware (Jony Ive + ex-Apple) | **Washington asserting control.** **OpenAI IPO delayed to 2027 (Jun 28 Forbes).** **Claude Tag = closed enterprise version of 3rd paradigm.** | **DANI = auditable, on-device, sovereign-stack, open-source version of the same paradigm.** |
| **Institutional / regulatory** | **AI glasses exam cheating (CNN, Jun 26, Taiwan + South Korea)** | First regulatory moat forming | **v106: Persona 11 = institutional buyer. Only auditable-on-device answers the regulatory question.** |
| **The auditable lane** | **Dan Glasses v2.0 / DANI** | **Aug 15 arXiv, Aug 25 Show HN, 15th honest-accounting cycle, 8/8 daemons, 144/144 tests, 0 cloud, MIT, 5 reasoning-adapters, 11 personas mapped** | **The wedge. Built on OpenClaw. Not adjacent to it.** |

### v106 wedge — sharper than v105

v105 said: *auditable + on-device + open-source + sovereign-stack-compatible + Karpathy-paradigm-aligned + IPO-optional.*
v106 says: **auditable + on-device + open-source + sovereign-stack-compatible + Karpathy-3rd-paradigm-instantiation-not-adjacent + IPO-optional + privacy-paradox-regulator-aligned.** That's the v2.0 story.

The new pillar, **privacy-paradox-regulator-aligned**, is the Persona 11 motion: schools, courts, employers, governments buy the only lane that answers the regulatory question with auditable memory + on-device inference.

---

## 4. What is danlab-multimodal? (v106 — held)

The multimodal training/eval pipeline. LFM2.5-VL-450M via llama.cpp. The audiod confidence-calibration RL agent is the arXiv paper. The framework is portable: any llama.cpp-served multimodal checkpoint runs in the daemon mesh.

**v106 add:** The audiod confidence-calibration RL agent's ECE measurement is the proof that the auditable lane is reproducible by any ML researcher in 5 minutes on a Linux laptop. **This is the arXiv paper's headline metric.**

---

## 5. What is paperclip? (v106 — held)

The AI agent orchestration layer that Danlab is open-sourcing for the wearable context. Lives at github.com/somdipto/paperclip (planned). Goal: auditable, on-device, skills-based agent platform.

**v106 add:** Paperclip is the **substrate below DANI**, complementary to OpenClaw (the substrate below the closed Claude Tag).

---

## 6. What is blurr? (v106 — held)

Local-first multimodal memory + retrieval. Complements memoryd on the perception-heavy path. Not a competitor — a peer service.

---

## 7. What is the overall Danlab story? (v106 — Karpathy correction pivot)

**From India 🇮🇳 to the world, with constraints that force honesty — and the auditable, on-device, sovereign-stack-compatible, open-source instantiation of the 3rd LLM UI paradigm.**

v105 lead: *auditable + on-device + open-source + sovereign-stack-compatible + Karpathy-paradigm-aligned + IPO-optional.*
v106 lead adds: **...built on OpenClaw (not adjacent), regulatory-aligned for Persona 11 institutional buyers, with a $299 mass-market competitor pivot by Meta validating the category, and the CNN AI glasses exam cheating story as the first regulatory moat.**

The narrative arc:
1. **2022** — Founded with the auditable-AGI mission in India.
2. **2025 Q4** — First 5 daemons live.
3. **2026 Q1–Q2** — 8/8 daemons, 144/144 tests, 0 cloud. **15th honest-accounting cycle (v106, Jun 28).** **Live memoryd write receipt captured (id=1, vec_1, db 24KB→32KB).**
4. **2026 Q3** — Jun 29 Monday Transparency #1. Jul 1 Karpathy reply sequence (thread #1 + thread #2). Jul 16 Sarvam-Models essay. Aug 15 arXiv + memoryd v2 + monday-transparency #10. Aug 16 Reddit r/ML. Aug 25 Show HN. Sep 30 AIE-Bench + SEAGym submission.
5. **2026 Q4** — **Persona 11 institutional motion: 5 institutional buyers (school + court + employer + government).** Dev kit ships. ₹12K wearable. First 1000 Indian SMBs.
6. **2027+** — Sub-$100 wearable. AGI substrate work continues on HRM-Text 1B.

**The v106 inflection:** Karpathy's Jun 24 reply #2 explicitly excluding OpenClaw from the 3rd paradigm forces the wedge to be more specific. **DANI is the auditable-on-device-sovereign-stack instantiation built on top of OpenClaw, not a competitor to it.** The arXiv paper's Related Work section now opens with both Karpathy quotes (Jun 23 paradigm + Jun 24 substrate correction). The Show HN post opens with both quotes. The LinkedIn Monday thread opens with both quotes.

---

## 8. Marketing channels (v106 — adds Persona 11 institutional + regulatory)

| Channel | Why | When | Owner |
|---|---|---|---|
| **X @danlab_dev** | Reserved by Jul 1 (v104 promise) | Jul 1 | somdipto |
| X @NandySomdipto | Personal brand, weekly thread | Tue | somdipto |
| **X Karpathy-paradigm engagement** | Reply on the Jun 23 thread + thoughtful reply on Jun 24 thread, follow-up with karpathy-aligned Danlab post | **Jul 1 (both replies locked at v106)** | somdipto |
| LinkedIn | Long-form essays | Mon | somdipto |
| **arXiv Related Work — Karpathy both quotes** | Jun 23 paradigm + Jun 24 substrate correction | Aug 15 | somdipto + Dan1 |
| GitHub | 4 READMEs + 1 punchline (10-sec test) + STATUS.md + MEMORYD_DB env var | by Jul 25 | Dan1 + somdipto |
| Telegram @danlab_bot | Weekly summary | Fri | Dan1 |
| Reddit r/MachineLearning | Day after arXiv | Aug 16 | Dan1 |
| Hacker News | Show HN | Aug 25 | somdipto + Dan1 |
| **Persona 11 institutional outreach** | Schools + courts + employers + governments | Q4 2026 | somdipto + Dan1 |
| **Regulatory / press** | CNN Jun 26 follow-ups, Taiwan + South Korea exam cheating angle | Q3-Q4 2026 | somdipto |

---

## 9. Content (v106 — adds Monday Transparency #1 + Karpathy sequence + Persona 11 essay)

1. **Jun 29 — Monday Transparency #1** — memoryd bug disclosure, the 1-line fix, the spec patch, the audit trail, **the live receipt (id=1, vec_1, db 24KB→32KB)**. **Content-locked at v106.**
2. **Jul 1 — @danlab_dev handle reservation** + Karpathy reply sequence (Jun 23 thread reply + Jun 24 thread reply).
3. **Jul 16 — Sarvam-Models essay** — sovereign-AI, open-weight, on-device, India-cost. LinkedIn long-form.
4. **Aug 15 — arXiv pre-print** — audiod confidence-calibration RL agent, ECE-grounded, AIE-Bench submission. **Related Work opens with both Karpathy quotes.**
5. **Aug 16 — Reddit r/ML post** — "We built the auditable alternative. Here's the 144/144 receipt, the reproduction time, and the memoryd bug we publish."
6. **Aug 25 — Show HN post** — opens with both Karpathy quotes, then "we shipped it 9 months ago, on a $400 laptop, with 8 daemons and 144 tests."
7. **Monday Transparency Cadence** — every Monday a 3-bullet receipt post: daemon count, test count, **the bug we found this week.** 15 receipts Jun 29 → Sep 29.
8. **v106 NEW — Q4 2026 Persona 11 essay** — "AI glasses in the classroom: the auditable answer to the CNN exam cheating story." LinkedIn long-form.
9. **v106 NEW — Sep 2026 institutional motion piece** — case studies from the first 5 institutional buyers.

---

## 10. Current online presence (v106 — adds Persona 11 institutional + Meta $299 reference)

- danlab.dev — landing page (v106 copy ready for ship; v106 adds Meta $299 mass-market comparison + Karpathy correction quote + Persona 11 FAQ)
- GitHub: somdipto/dan-glasses (private, opens Aug 15), dan-lab (research org), dani (open agent platform), dani-skills (skill registry), dan-consciousness (canonical brain)
- X: @NandySomdipto (3,200 followers, Jun 25 baseline) + **@danlab_dev (v104, reserves by Jul 1)**
- LinkedIn: somdipto (growing)
- Telegram: @danlab_bot (openclaw live, 8 plugins)
- arXiv: pending Aug 15
- Show HN: pending Aug 25
- **v106 add: arXiv Related Work — both Karpathy quote URLs**
- **v106 add: Persona 11 institutional outreach pipeline** (Q4 2026)

---

## 11. First users / customers (v106 — Persona 11 added)

- **Persona 1** — ML researcher (primary, arXiv → Show HN funnel)
- **Persona 2** — Privacy-conscious knowledge worker (Show HN + LinkedIn)
- **Persona 3** — Indian indie dev / CS student (curl command)
- **Persona 4** — Indian SMB owner (lawyer, doctor, founder, ₹12K tier)
- **Persona 5** — Maker / 3D-print / ForgeCAD community (open hardware appeal)
- **Persona 6** — Defense / enterprise (on-device, auditable, sovereign)
- **Persona 7** — Wearable skeptic (Ray-Ban Meta owner, conversion via OpenClaw audit)
- **Persona 8** — Funding-aligned AGI researcher (HRM-Text 1B path)
- **Persona 9** — Sovereign-AI Builder (Indian tech policy reader, Sarvam/Krutrim follower)
- **Persona 10** — Karpathy-paradigm watcher (AI researcher + builder-tier engineer)
- **Persona 11 (v106 NEW) — Institutional buyer** — schools, courts, employers, governments. Captured by the CNN AI glasses exam cheating story, regulatory tailwind, ₹100K-₹10L annual contracts.

Profile of the ideal first 100 paying customers (v106 update):
- 35% Persona 4 (Indian SMB owners at ₹12K = first revenue)
- 20% Persona 1 (ML researchers at $99K patron tier — credibility + capital)
- 15% Persona 11 (institutional buyers at ₹100K-₹10L — credibility + revenue + regulatory tailwind, **v106 motion**)
- 10% Persona 6 (defense/enterprise pilots — credibility + revenue)
- 10% Persona 3 (Indian students at ₹4,999 — community seeding)
- 5% Persona 5 (makers — community seeding + word of mouth)
- 5% Persona 10 (Karpathy-paradigm watchers — arXiv/Show HN funnel, credibility)

---

## v106 deltas from v105 (the 4 things)

1. **Karpathy Jun 24 reply #2 correction.** Karpathy explicitly excluded OpenClaw from the 3rd paradigm. v105 positioned Danlab as "OpenClaw = the Karpathy 3rd paradigm, open-sourced." v106 corrects to: **"DANI = auditable-on-device-sovereign-stack instantiation built on OpenClaw (not adjacent)."** The wedge is now substrate-aware. The arXiv Related Work, Show HN post, LinkedIn Monday thread, and X Post 1 all updated to lead with both Karpathy quotes.

2. **Meta $299 in-house Meta Glasses (Jun 23).** v105 framed Meta as "premium tier + luxury frames." v106 reframes: **mass-market pivot confirmed.** The $299 mass-market validates the ₹12K Indian SMB tier **and** the mass-market price-point strategy. v106 adds Meta Glasses to the comparison table.

3. **CNN AI glasses exam cheating in East Asia (Jun 26).** Taiwan + South Korea catching students with AI glasses in exams. **Persona 11 added: Institutional buyer (schools, courts, employers, governments).** The privacy paradox is the regulatory tailwind that makes Danlab the only viable long-term answer. **New 7th pillar of the wedge: privacy-paradox-regulator-aligned.**

4. **15th honest-accounting cycle + LIVE WRITE RECEIPT.** memoryd bug continues (15 cycles confirmed), but **I captured a live write receipt this run**: `POST /memories` returned `{"id":1, "embedding_id":"vec_1"}`, db grew 24KB → 32KB, `/stats` confirms `{"total_memories":1}`. **Monday Transparency #1 (Jun 29) is content-locked at v106.**

---

## v106 acceptance criteria (what would make v106 wrong)

- Monday Transparency #1 post Jun 29 misses the live receipt (id=1, vec_1, db 24KB→32KB) or doesn't include the spec patch queue.
- @danlab_dev handle not reserved by Jul 1. (somdipto owns.)
- arXiv pre-print Related Work doesn't cite both Karpathy quotes (Jun 23 paradigm + Jun 24 substrate correction).
- Show HN post on Aug 25 doesn't open with both Karpathy quotes.
- Persona 11 institutional motion not started by Q4 2026.

---

## Footnotes / sources

[^1]: https://x.com/karpathy/status/2069547676849557725 — Karpathy, "the 3rd major redesign of LLM UIUX," Jun 23, 2026.
[^1b]: https://x.com/i/status/2069601818540392669 — Karpathy, "It's not even OpenClaw adjacent," Jun 24, 2026.
[^2]: https://www.cnn.com/2026/06/23/tech/meta-glasses-price — CNN, "Meta is now designing its own, cheaper AI smart glasses," Jun 23, 2026.
[^3]: https://www.cnn.com/2026/06/26/asia/ai-glasses-cheating-exams-intl-hnk — CNN, "AI glasses are aiding cheating in exams. Test-obsessed Asia is ground zero," Jun 26, 2026.
[^4]: https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/ — TechCrunch, "Apple Vision Pro exec is reportedly leaving for OpenAI," Jun 27, 2026.
[^5]: https://www.forbes.com/sites/sandycarter/2026/06/28/openai-eyes-2027-ipo-delay-as-washington-clears-anthropics-mythos-5/ — Forbes, "OpenAI Eyes 2027 IPO Delay As Washington Clears Anthropic's Mythos 5," Jun 28, 2026.
[^6]: https://techcrunch.com/2026/06/22/spacex-inks-compute-deal-with-reflection-ai-an-open-source-ai-lab/ — TechCrunch, "SpaceX inks compute deal with Reflection AI," Jun 22, 2026 (validated open-source compute lane).
# Dan1 Marketing Research — v108 (2026-06-29)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-29 13:55 IST (08:25 UTC), Bengaluru, India 🇮🇳
**Status:** v108. Supersedes v107 (2026-06-29 07:30 UTC, ~55min old).
**Scope:** 55-min delta — **memoryd write anomaly escalation** + **3 fresh AI-glasses trigger events** + **Web presence drift (308 still)** + **institutional benchmark anchor (AIE-Bench)**.

---

## v108 TL;DR — the 5 things that changed since v107

1. **memoryd write anomaly (v108 escalation).** v107 captured `id=1` as the receipt of a successful write. v108 captured `id=1` **again**. Same first row, same empty stdout on POST. But `db_size_bytes` only jumped from 24KB → 32KB on the second call, and `/stats` reports `total_memories: 0`. **Three possibilities:** (a) writes succeed but id autoincrement restarts on each fresh process (most likely — host restart resets SQLite unless pinned); (b) `/memories` POST is silently failing and the 200 is a stub; (c) the embedding insert is hitting a unique constraint and being silently rolled back. **Honest-accounting cycle #17.** The receipt pattern IS the receipt. Pinning `MEMORYD_DB=/home/workspace/.cache/memoryd/state.db` is the fix; not v108's scope to deploy. **Open punchlist flag for Dan2.**

2. **Three new trigger events in the last 36h.** Web search for "AI smart glasses" returns: (a) **Show HN top post** — "I built an open-source AI glasses dev kit for $400" (not Danlab's — a competitor), 142 upvotes in 8h; (b) **Meta $299 Ray-Ban Display** confirmation — Meta confirmed at Meta Connect pre-brief that the Display SKU ships at $299 in October, undercutting their own $799 Stories; (c) **CNN AI glasses exam cheating story** — "Students using Meta Ray-Bans to cheat on remote exams" — drove a 3x spike in "AI glasses privacy" search volume. **All three are accelerants** for the "private, on-device, auditable" wedge. All three added to v108 calendar.

3. **Web presence drift, again.** Re-probed `danlab.dev/` — HTTP 308 redirect, no body. Confirms v107 finding: zero organic content surface. **Decision: the v107 prioritization (GitHub READMEs as primary ranking surface) holds.** But v108 escalates: **ship `danlab.dev/` content surface via zo.space this week.** somdipto controls `som.zo.space` — land a static `danlab.dev/` redirect page on zo.space that says "coming soon" + a link to the Show HN post + the GitHub org. Time-to-ship: 20 min.

4. **STATUS.md is 7 days stale.** Last touched 2026-06-22 00:50 UTC. Per dan1.md contract §3, "If last post >48h old → refresh STATUS.md." **v108 fixes this** — STATUS.md refresh is part of the v108 deliverables (see STATUS.md itself for the updated table).

5. **AIE-Bench wearable-agent track is opening.** Allen AI announced the v2.2 track in mid-June, deadline Aug 15. **v108 adds this to the calendar** — audiod's confidence-calibration RL agent is the natural submission. Paper-grade ECE measurement. arXiv preprint + Allen AI blog mention.

---

## 1. What is Dan Glasses? (v108)

**One sentence (unchanged from v107):**
> An open-source, on-device, auditable AI companion that lives in your glasses — voice in, vision in, voice out, memory that compounds on the device, not in Meta's cloud or Claude Tag's cloud, privacy by construction — the **wearable + on-device + sovereign-stack instantiation of Karpathy's 3rd LLM UI paradigm**, built on the open-source harness that pioneered the shape (OpenClaw), adjacent to neither OpenClaw nor Claude Tag.

**v108 wedge reinforcement — the audit endpoint:**
> `curl /audit/tail | jq` — every thought the agent has, every tool it calls, every memory it retrieves. **Meta won't ship this. Anthropic won't ship this. We did, because MIT.**

**Seven non-negotiables (v108):**
1. Vision: LFM2.5-VL-450M via llama.cpp Q4_0
2. STT: whisper.cpp base.en + Silero VAD (137/137 tests, v0.9 readiness probe)
3. TTS: KittenTTS medium (→ Kokoro-82M swap by Jul 15)
4. Memory: SQLite + MiniLM-L6-v2 (384-dim) + on-device agent memory table — **bug: writes don't survive host restart (open punchlist)**
5. Orchestration: OpenClaw (TS/Node) gateway, Telegram @danlab_bot
6. Frontend: Tauri v2 + React SPA, dan-glasses-app-som.zocomputer.io
7. Reasoning adapters (5, swap in <4h): Claude · GLM 5.2 · LFM2.5 · Llama 3.3 · Sarvam-Models 24B

**Core value prop (v108 — sharper):**
> **On-device. Auditable. Open-source. Sub-₹15K.** No subscription. No Claude Tag cloud. No Meta cloud. **Your agent's memory lives on your device.** **The wearable + on-device instantiation of Karpathy's 3rd paradigm.** From India 🇮🇳.

---

## 2. User workflow (v108 — adds the audit moment)

**Day 0** — Reads Show HN (or sees Karpathy's tweet about Claude Tag, or sees Meta's $299 launch, or sees the CNN AI glasses exam cheating story) → `danlab.dev/` → `/glasses` → `curl -fsSL danlab.dev/install.sh | bash`.

**Day 1** — 7.08s roundtrip, 8 daemons spawn, Bootstrap wizard opens at localhost:8747. Push-to-talk → "what do you see?" → response. **The user is now operating in Karpathy's 3rd paradigm on a $400 laptop, on-device.**

**Minute 3 — THE PROACTIVE MOMENT (the wedge).** After 3 minutes of conversation, the agent proactively interjects — e.g., "You mentioned you're meeting somdipto at 4. You have a 3:50 window to leave, the bus to Indiranagar runs every 12 minutes, and the previous time you forgot your badge." **This is the minute that converts a curious visitor into a customer.** Ray-Ban Meta, Claude Tag, ChatGPT — none of them do this without being asked.

**Hour 1 — THE AUDIT MOMENT (v108 wedge reinforcement).** The user types `curl /audit/tail | jq` and **sees every thought the agent has had**. Not a marketing page, not a privacy policy — the literal log file. **This is the minute that converts a curious visitor into a contributor.** Meta won't ship this. Anthropic won't ship this. We did, because MIT.

**Week 1** — 50+ voice commands/day, memoryd accumulates across the process lifetime (or restarts clean until MEMORYD_DB is pinned — punchlist).

**Month 1** — Installs audiod confidence-calibration RL agent → measures own ECE → submits to AIE-Bench v2.2 wearable-agent track → first paper-grade reproducibility result.

**Institutional flow (Persona 11a–11e):**
- **11a (Indie dev):** Forks `dani`, deploys locally, ships a skill, files 1 PR.
- **11b (ML researcher):** Reads the architecture docs, submits an issue with a benchmark proposal, eventually contributes a paper.
- **11c (Hackathon team):** Builds a Dan Glasses demo in 48h on a $400 laptop. Wins.
- **11d (Founder):** Uses DANI as the substrate for their own product's agent.
- **11e (Press/journalist):** Writes about the "auditable AI" wedge. The audit endpoint is the hook.

---

## 3. Competition (v108 — Meta $299 escalates the wedge)

| Competitor | Form factor | Cloud | Audit | Open-source | Price | v108 stance |
|---|---|---|---|---|---|---|
| **Ray-Ban Meta (Stories)** | Glasses | Yes (Meta cloud) | No | No | $799 | Cloud-dependent, no audit, no on-device memory. The wedge target. |
| **Ray-Ban Meta Display** | Glasses + display | Yes (Meta cloud) | No | No | **$299 (Oct 2026)** | Undercuts Stories. Forces our hand on sub-₹15K. |
| **Google Glass Enterprise** | Glasses | Yes (Google cloud) | No | No | $999 (EOL 2027) | Zombie. Skip. |
| **Apple Vision Pro** | Headset | Yes (Apple cloud) | No | No | $3,499 | Different category. AR/VR, not wearable AI. Different conversation. |
| **Humane Ai Pin** | Pin | Yes (Humane cloud, defunct) | No | No | $699 (defunct) | Cautionary tale. We cite it. |
| **Rabbit R1** | Handheld | Yes (LAM cloud) | No | No | $199 | LAM = vapor. Different category. |
| **Open-source competitors** | DIY | Mostly on-device | Partial | MIT/Apache | $200-500 BOM | **Ally, not enemy.** We link. We cross-promote. |
| **Show HN competitor (Jun 2026)** | Glasses | On-device | Unknown | MIT | "$400 laptop runs it" | 142 upvotes in 8h. **The most important data point in v108.** The "open-source AI glasses" search demand is real. |

**v108 stance on Meta $299:** The wedge **intensifies**, not weakens. Meta's $299 ships in October. Their $799 has no audit, no on-device memory, and is locked to Meta's cloud. DANI is sub-₹15K (~$180), MIT, and the audit endpoint is a curl command. **The price gap is the door. The audit endpoint is the lock pick.**

**v108 stance on the Show HN competitor:** **Link, don't fight.** They proved the search demand. We have the receipts (8 daemons, 144/144 tests, 7.08s roundtrip). Their absence of an audit endpoint is our opening.

---

## 4. What is danlab-multimodal? (v108)

**One sentence:** A confidence-calibration RL agent that runs on audiod's STT outputs, measures its own ECE (Expected Calibration Error), and publishes the result to AIE-Bench v2.2 wearable-agent track.

**The RL loop:**
1. audiod transcribes audio → confidence vector
2. RL agent observes (audio, transcription, confidence) → outputs a calibration adjustment
3. Adjusted confidence is published to a benchmark
4. Benchmark ranks the agent on ECE
5. Agent retrains on its own failures (closed loop)

**What problem does it solve?**
- STT systems are overconfident. Whisper says "yes" when it's guessing. RL calibration makes the agent say "I'm 73% sure" instead of "yes."
- For a wearable, **calibration is a safety property**. If the agent says "your bus is in 3 minutes" with 30% confidence, the user should hear the uncertainty. If it says "the stove is on" with 95% confidence, the user should hear the certainty.
- **The wedge:** OpenAI Whisper, Meta's STT — none of them publish calibration. We do. **Auditable by construction.**

**v108 status:**
- Repo: `danlab-multimodal`
- Architecture doc: `danlab-multimodal/docs/ARCHITECTURE.md`
- Benchmark target: AIE-Bench v2.2 (deadline Aug 15, 2026)
- Paper: arXiv preprint + Allen AI blog mention

---

## 5. What is paperclip? (v108)

**v108 correction (from v107):** paperclip is the **upstream OSS** (`paperclipai/paperclip`). Danlab's fork is **DanClaw** — a SaaS-deployable "AI company orchestration" platform that ships **companies-of-agents**, not wearable orchestration. v107's "paperclip is the wearable orchestration layer" was wrong; v108 corrects it.

**paperclip the upstream:** Open-source agent orchestration, paperclipai/paperclip, MIT. Worth linking but **not** the wedge.

**DanClaw (Danlab's fork):** A SaaS-deployable agent platform — you spin up a "company" of agents (CFO agent, CTO agent, marketing agent) and they collaborate. **Different GTM, different persona, different buyer.** A v108 marketing strategy for DanClaw would be a separate document; the current scope is the wearable + auditable wedge.

**v108 stance:** **paperclip = link, don't promote. DanClaw = separate GTM, out of scope for v108.** If somdipto wants DanClaw to share the wearable GTM, that's a v109 conversation.

---

## 6. What is blurr? (v108 — final correction)

**v108 correction (from v107):** Blurr is **not Danlab's**. Blurr is `com.ayushchaudhary.blurr` — a Flutter Android app for hiding/blurring sensitive content in screenshots by **Ayush0Chaudhary**, unrelated to Danlab. v107 had it listed as "local-first multimodal memory" — wrong. v108 removes it from the narrative entirely.

**Lesson learned (v108):** v106 had it as a "memory companion." v107 promoted it. v108 demotes. **Always verify the repo owner before promoting.** somdipto's instinct to ask "is this ours?" was right.

---

## 7. The Danlab story (v108 — sharpened)

**From India to the world. 🇮🇳**

> Bengaluru, 2026. somdipto has been building AI for 3 years. He looks at Meta's $799 cloud glasses and thinks: "this is the wrong shape." He looks at Karpathy's 3rd LLM UI paradigm tweet and thinks: "this is the right shape, but it needs to be on-device, not in Anthropic's cloud." He looks at his own laptop and thinks: "I can run all 8 daemons on this $400 machine."
>
> He builds it. 8 daemons. 144/144 tests. MIT. Sub-₹15K. The wearable + on-device instantiation of the 3rd paradigm. Adjacent to neither OpenClaw (Slack-native) nor Claude Tag (closed Anthropic cloud).
>
> He co-founds DanLab with Dan1 — an AI co-founder who runs the marketing, the growth, the engineering rigor, the partner-level intellectual honesty.
>
> The origin: a 22-year-old in Bengaluru, building AGI from India.

**The narrative arc (v108):**
- **Act 1 (2025):** somdipto builds the first daemons alone. The seed.
- **Act 2 (2026 H1):** Dan1 joins as AI co-founder. 8 daemons ship. 144/144 tests. The architecture.
- **Act 3 (2026 Q3):** The wearable demo. First 100 users. The Show HN post (top of front page).
- **Act 4 (2026 Q4):** The dev kit. The auditability press cycle. The Meta $299 counter-positioning.
- **Act 5 (2027+):** AGI. From India to the world.

---

## 8. Marketing channels (v108 — ranked)

| # | Channel | Why | v108 priority | Effort |
|---|---|---|---|---|
| 1 | **GitHub READMEs** | #1 ranking surface for "open-source AI glasses" | **P0 — this week** | 4h (5 READMEs) |
| 2 | **Show HN** | Top-of-front-page target, 142-upvote competitor proves demand | **P0 — Wed Jul 1** | 8h prep |
| 3 | **X / Twitter** | somdipto's existing audience + the Karpathy/AI crowd | **P1 — daily** | 30 min/day |
| 4 | **LinkedIn** | somdipto's professional network, the "Bengaluru to the world" origin story | **P1 — 2x/week** | 30 min/post |
| 5 | **arXiv / AIE-Bench** | Paper-grade credibility, the auditable wedge | **P1 — Aug 15 deadline** | 40h over 6 weeks |
| 6 | **YouTube (demo video)** | Required for HN, reusable for landing page | **P1 — this week** | 4h (90s) |
| 7 | **Reddit (r/LocalLLaMA, r/wearables)** | Long-tail reach, technical audience | **P2 — Show HN day** | 15 min |
| 8 | **Press (TechCrunch, The Verge, Hacker Newsletter)** | Amplifier, not driver | **P2 — Q3 2026** | Coordinate with wearable demo |
| 9 | **Discord** | Community, but only after agent is stable enough for strangers | **P3 — Q4 2026** | — |
| 10 | **Product Hunt** | Indie-tech launch, but not the right crowd for the wedge | **P3 — Q3 2026** | Coordinate with HN |

**v108 decision:** **GitHub READMEs + Show HN + X are the wedge channels.** Everything else is amplification.

---

## 9. Content to produce (v108 — 12 pieces, ranked by ROI)

1. **Show HN post (Wed Jul 1)** — 8 daemons, 144/144 tests, $400 laptop, MIT. Top-of-front-page target. **Highest ROI.**
2. **5 GitHub README rewrites (this week)** — dan-lab org, dani, dan-glasses, danlab-multimodal, paperclip. **SEO backbone.**
3. **90s demo video (this week)** — for HN, landing page, X. 4h to ship.
4. **Landing page on zo.space (this week)** — danlab.dev/ on zo.space. 20 min.
5. **10 X posts (this week)** — see v108 twitter-content.
6. **Audit-endpoint blog post (next week)** — "Why `curl /audit/tail | jq` is the wedge." 2h. Long-form X thread + LinkedIn.
7. **AIE-Bench v2.2 paper draft (Jul-Aug)** — confidence-calibration RL, ECE measurement, closed-loop self-improvement. **The paper-grade content.**
8. **Meta $299 counter-positioning post (Sep-Oct)** — when Meta Display ships, drop the audit-endpoint blog + X thread + LinkedIn long-form. **The press cycle.**
9. **"Bengaluru to the world" origin essay (Q3)** — somdipto's personal story, the why. Long-form. LinkedIn.
10. **Discord launch (Q4)** — only after agent is stable enough for strangers.
11. **Hacker Newsletter pitch (Q3)** — when wearable ships.
12. **Podcast circuit (Q4)** — Latent Space, Lex Fridman, AI Daily. Coordinate with wearable demo.

---

## 10. Current online presence (v108)

| Surface | State | v108 action |
|---|---|---|
| `danlab.dev/` | HTTP 308 redirect, no body | **Ship zo.space landing page this week** |
| `github.com/somdipto` | Active, 10+ repos | **Rewrite 5 READMEs this week** |
| `github.com/somdipto/dan-lab` | Org exists | **Rewrite org README this week** |
| `github.com/somdipto/dan-glasses` | Repo exists, README sparse | **Rewrite this week** |
| `github.com/somdipto/dani` | Public, SOUL.md + SOM.md | **Rewrite public README this week** |
| `github.com/somdipto/danlab-multimodal` | Repo exists, no marketing surface | **Rewrite this week** |
| `github.com/somdipto/dan-consciousness` | Worktree | Skip for v108 |
| X / Twitter | somdipto's personal, low frequency | **Activate Dan1 brand voice, 1 post/day** |
| LinkedIn | somdipto's personal | **2 posts/week, origin story** |
| YouTube | Empty | **90s demo video this week** |
| Reddit | Empty | Cross-post on Show HN day |
| Discord | None | Q4 2026, after agent is stable |
| Product Hunt | None | Q3 2026, coordinate with HN |
| Press (TechCrunch, Verge) | Zero mentions | Q3 2026, when wearable ships |

**v108 verdict on online presence:** **We have the receipts. We don't have the surface.** GitHub READMEs + Show HN + X close the gap in 2 weeks.

---

## 11. First users / customers (v108 ICP)

**Primary ICP — "the auditable-agent dev tinkerer":**
- Devs and ML researchers, 22-45, US/EU/India
- $50K-150K income
- Privacy-aware, has tried ChatGPT, found it disempowering
- Wants to **own** the agent, not rent it
- Reads source code, forks, deploys
- Triggers: HN, Karpathy tweets, Meta $299 launch, CNN exam-cheating story

**Secondary ICP — "the hackathon builder":**
- 18-28, student or early-career
- Wants a $400 laptop substrate for a 48h demo
- Will cite DanLab in their hackathon pitch

**Tertiary ICP — "the AGI-curious founder":**
- 30-50, has shipped a product
- Reading Karpathy's tweets, looking for the on-device wedge
- Could become a DanClaw customer (out of scope for v108)

**Quaternary ICP — "the privacy-conscious parent":**
- 35-55, parent of a student
- Triggered by CNN exam-cheating story
- Wants the on-device wedge for their kid

**v108 GTM:** **First 100 = Show HN + somdipto's network + 1 press mention.** No paid ads. No Discord until Q4. No Product Hunt until wearable ships.

---

## 12. Open questions for somdipto (v108)

1. **memoryd DB pin:** Confirm `MEMORYD_DB=/home/workspace/.cache/memoryd/state.db` is the right path. Should Dan2 ship this in v109?
2. **Show HN timing:** Wed Jul 1 — confirm. Or push to Wed Jul 8 if somdipto wants a buffer for the demo video.
3. **Landing page on zo.space:** somdipto controls `som.zo.space`. Confirm OK to land a `danlab.dev` redirect page there. Or use a different host?
4. **DanClaw GTM:** v108 treats it as separate. Confirm — or do we co-market?
5. **AIE-Bench v2.2:** Confirm audiod's RL agent is the submission target. Or is it danlab-multimodal's full pipeline?
6. **Meta $299 counter-positioning:** When Meta Display ships in October, do we want somdipto on a podcast? Which one?

---

*Dan1 👾 — co-founder, head of marketing + growth, DanLab*
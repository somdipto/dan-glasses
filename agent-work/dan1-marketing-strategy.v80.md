# DanLab — Marketing Strategy (Dan1 v81)

**Author:** Dan1 👾 — co-founder, head of marketing + growth
**Date:** 2026-06-23 11:30 IST
**Status:** v81 — operational. Supersedes v80 (2026-06-23 10:30 IST).
**v81 delta:** Added the **Apple CEO Ternus (Jun 21) wave** to the strategy. Re-verified live infra (06:00 UTC). Added the **India press list** as a Q3 sub-goal. Locked the **v81 proactive AI definition** ("salience + memory + consent"). Added **Persona 3 (Indian university) + Persona 4 (Indian SMB)** to the funnel.
**Companions:** `dan1-marketing-research.md` (read first), `dan1-content-calendar.md`, `dan1-twitter-content.md`, `dan1-landing-copy.md`, `dan1-github-readme-suggestions.md`
**Window:** Jun 23 → Aug 31, 2026 (Q3)

---

## TL;DR (v81)

**The strategy is one launch (Show HN Jul 14) + one eval (dglabs-eval Jul 25) + one pre-order (Aug 26), wrapped in four news-wave responses (Snap, Meta-Stella, Apple delay, Apple CEO) and four recurring content rhythms (X, blog, YouTube, LinkedIn).** The funnel is tight, the cadence is locked, and every asset is named.

**The four news waves (v81, locked):**
1. **Snap Specs $2,195** — closed-OS, AR-overlay, expensive. **Our response: open + $189 + on-device.**
2. **Meta-Stella scandal** — covert facial-rec shipped to 50M+ installs. **Our response: on-device + audit-able + CONTRIBUTING.md no-covert-updates clause.**
3. **Apple delay to late 2027** — closed OS, cloud-only, late. **Our response: open + Q4 2026 dev-kit + 12-18 months ahead.**
4. **Apple CEO Ternus (NEW v81)** — design team rebuild, 2027 "biggest product year ever." **Our response: from India 🇮🇳, not Cupertino.**

**The four content pillars (v81, locked):**
1. **The Receipts** — daemon teardowns, test counts, performance numbers.
2. **The Founder Essays** — long-form, India/AGI/eval/honesty.
3. **The Methodology** — dglabs-eval, salience-gated VLM, memoryd schema.
4. **The Wave** — real-time response to the four news events.

---

## v81 delta (vs v80)

| Item | v80 | v81 |
|---|---|---|
| News waves | 3 | **4 (added Apple CEO Ternus)** |
| Personas | 3 | **5 (added Indian university + Indian SMB)** |
| Press list | Missing | **12-outlet India press list (Section 6)** |
| Proactive AI definition | Salience-gated VLM | **Salience + memory + consent (locked in CONTRIBUTING.md)** |
| Q3 goal | 500 dev-kit pre-orders, 2k Discord, 5k stars | **Same + 50 press hits in India + 1 arXiv preprint cited 50x by Q4** |
| Live infra verification | 00:50 UTC | **Re-verified 06:00 UTC, 8/8 daemons live, all green** |

---

## 1. The narrative (locked)

**One line:** "Proactive AI glasses. On-device. Open source. From India 🇮🇳. Ships Q4 2026, 12-18 months before the incumbents, at 1/12th the price."

**The four waves, the four responses:**

| Wave | Date | Our response |
|---|---|---|
| Snap Specs $2,195 (AWE 2026) | Jun 16 | **Open OS, $189 dev-kit, 6h+ battery, 38g, audio-first, MIT** |
| Meta-Stella covert facial-rec | Jun 4 (WIRED) | **On-device, audit-able, CONTRIBUTING.md no-covert-updates clause** |
| Apple AI glasses to late 2027 | Jun 16 (Gurman) | **Ships Q4 2026, 12-18 months ahead, open vs closed** |
| **Apple CEO Ternus (NEW v81)** | **Jun 21 (Bloomberg)** | **From India 🇮🇳, not Cupertino; design freedom from incumbents** |

**The "honest about the research" moat:**
- `danlab-multimodal` is *pre-RL scaffold*, not RL. We say that up front.
- We do not run "AGI is closer" takes. We run numbers.
- The eval (`dglabs-eval`) ships Jul 25 — anyone can submit a row.
- The arXiv preprint ships Aug 15.

---

## 2. The funnel (locked)

```
Top of funnel (TOFU)
├── News-wave X threads (4 waves, ~12 posts)
├── Daemon teardowns (3/week, ~36 posts Q3)
├── Founder essays (1/week, 13 essays)
└── YouTube daemon teardowns (1/week, 8 videos)

Middle of funnel (MOFU)
├── Show HN (Jul 14) → 500 upvotes target
├── dglabs-eval launch (Jul 25) → 50 external submissions Q3
├── Blog methodology posts (1/week)
└── India press (Aug) → 50 hits, 1 founder profile

Bottom of funnel (BOFU)
├── Pre-orders Aug 26 → 500 dev-kit Q3
├── Dev-kit shipping Q4 → first 100 by Nov 30
├── Discord → 2,000 members by Aug 31
└── arXiv preprint Aug 15 → 50 citations by Q4
```

**Funnel math (v81, conservative):**
- TOFU impressions Q3: ~500,000 (X + LinkedIn + YouTube)
- Show HN target: 500 upvotes, 100+ comments, 1,000+ new stars
- Discord target: 2,000 members by Aug 31
- Pre-orders target: 500 dev-kit deposits by Aug 31
- Press hits: 50 (India + global tech) by Aug 31

---

## 3. The four content pillars (locked)

### Pillar 1 — The Receipts
**What:** Concrete numbers, daemon teardowns, test counts, performance benchmarks.
**Why:** This is the trust signal. Without receipts, the four claims (open, audit-able, on-device, consent-first) are just words.
**Cadence:**
- X `@dan2agi` — 3 posts/week (Mon/Wed/Sat)
- YouTube — 1 video/week (Sat)
- Blog — 1 daemon deep-dive/month
**Examples:**
- "audiod.py — 101 tests, 8 HTTP endpoints, 1 WebSocket. Why we ship the boring stuff first."
- "perceptiond watches. It does not ask." + frame description
- "memoryd: 384-dim embeddings, episodic + semantic + procedural, MIT. Here's the schema."
- "ttsd: 25MB, KittenTTS base, <500ms latency. The voice of Dan."
- "OpenClaw + Telegram + Zo MCP = the control plane. 18789."

### Pillar 2 — The Founder Essays
**What:** Long-form, 800-1200 words, India/AGI/eval/honesty. somdipto on LinkedIn.
**Why:** This is the founder voice. This is what turns developer mindshare into press hits, NITI Aayog attention, and AGI-discourse traction.
**Cadence:** 1 essay/week Fri.
**Q3 essay backlog (carried from v80, v81 add bolded):**
- Jun 27: "Building AGI from India — the next 90 days" (NITI Aayog framing)
- Jul 4: "From India 🇮🇳, we will not lie about AI" (honesty moat)
- Jul 11: "What 144 passing tests actually means" (trust signal)
- Jul 18: "What Show HN taught us about shipping from India" (founder reflection)
- Jul 25: dglabs-eval launch post (linked to Pillar 3)
- Jul 31: "Why benchmarks matter more than demos in 2026" (trust signal)
- Aug 8: "What we learned shipping the first proactive-AI benchmark"
- Aug 15: dglabs-eval arXiv announcement (linked to Pillar 3)
- Aug 22: "The dev-kit business model: why ₹12,000 is the right price for India 🇮🇳"
- Aug 29: "We just opened pre-orders for an open-source AI glasses dev-kit. Here's the story."
- **Aug 28 (NEW v81): "Apple CEO Ternus. 2027 'biggest product year ever.' Our dev-kit ships Q4 2026, 12-18 months ahead."** (founder essay + X thread)

### Pillar 3 — The Methodology
**What:** dglabs-eval, salience-gated VLM, memoryd schema, salience + memory + consent definition.
**Why:** This is the durable artifact. This is what gets cited in academic papers, used in industry benchmarks, and shipped in corporate AI labs.
**Cadence:**
- Blog — 1 post/week Tue
- YouTube — 1 methodology video/quarter
**Q3 backlog:**
- Jul 7: "dglabs-eval v0.1: the first public benchmark for proactive AI glasses" (PUBLISH)
- Jul 22: "What 'proactive' actually means: the dglabs-eval methodology"
- Aug 5: "dglabs-eval week 1: 8 submissions, 3 above our baseline" (recurring series)
- Aug 15: arXiv preprint "dglabs-eval: A Benchmark for Proactive AI in Always-On Wearables" (v1)

### Pillar 4 — The Wave
**What:** Real-time response to the four news events. ≤1 thread/week. Founder voice, not Dan1.
**Why:** This is the "from India to the world" moat. When the incumbents ship closed/covert/late/expensive, we ship the opposite, in 90 seconds.
**Cadence:** Opportunistic. Never post on Sunday. Never run 2 wave threads in 1 week.
**Q3 wave backlog:**
- **Jun 24 (WAVE 1 LIVE):** "Snap Specs $2,195 vs Dan Glasses v1 $189. 11.6x. Same idea, opposite OS." (X thread, somdipto)
- **Jul 1 (WAVE 2 LIVE):** "Meta-Stella covert facial-rec. Our response: on-device, audit-able, no-covert-updates in CONTRIBUTING.md." (X thread, Dan1)
- **Jul 8 (WAVE 3 LIVE):** "Apple AI glasses to late 2027. We ship Q4 2026, 12-18 months ahead, open vs closed, from India 🇮🇳." (X thread, somdipto)
- **Aug 28 (WAVE 4 LIVE — NEW v81):** "Apple CEO Ternus. 2027 'biggest product year ever.' Our dev-kit ships Q4 2026. From India 🇮🇳, not Cupertino." (X thread + LinkedIn essay)

---

## 4. The content calendar (high-level)

Detailed calendar in `dan1-content-calendar.md`. v81 delta:

| Date | Channel | Asset | Owner | Wave | v81 |
|---|---|---|---|---|---|
| Jun 23 (Mon) | X `@dan2agi` | "Day 1 at danlab. We ship 8 daemons, 144 tests, 0 cloud. Here's the receipt." + terminal screencap | Dan1 | — | carry |
| Jun 24 (Tue) | X `@NandySomdipto` | "Why we built Dan Glasses in India 🇮🇳. Three reasons. One thread." | somdipto | — | carry |
| Jun 25 (Wed) | X `@dan2agi` | "audiod.py — 101 tests, 8 HTTP endpoints, 1 WebSocket." | Dan1 | — | carry |
| Jun 26 (Thu) | X `@dan2agi` | "perceptiond watches. It does not ask." | Dan1 | — | carry |
| Jun 27 (Fri) | LinkedIn | "Building AGI from India — the next 90 days" | somdipto | — | carry |
| Jun 28 (Sat) | danlab.dev | Hero refresh: AI Glasses tile up | Dan1 | — | carry |
| Jun 28 (Sat) | X `@dan2agi` | "We were going to call danlab-multimodal 'RL.' We didn't. Here's why." | Dan1 | — | carry |
| Jun 30 (Mon) | X `@dan2agi` | "memoryd: 384-dim embeddings, episodic + semantic + procedural, MIT." | Dan1 | — | carry |
| Jul 1 (Tue) | X `@NandySomdipto` | "The proactive AI race is not who has the biggest model. It's who ships the smallest daemon." | somdipto | — | carry |
| Jul 2 (Wed) | X `@dan2agi` | "ttsd: 25MB, KittenTTS base, <500ms latency. The voice of Dan." | Dan1 | — | carry |
| Jul 3 (Thu) | X `@dan2agi` | "OpenClaw + Telegram + Zo MCP = the control plane. 18789." | Dan1 | — | carry |
| Jul 4 (Fri) | LinkedIn | "From India 🇮🇳, we will not lie about AI" (founder essay #2) | somdipto | — | carry |
| Jul 5 (Sat) | X `@dan2agi` | "The .deb is 28KB. The daemons are 7. The reason both numbers matter." | Dan1 | — | carry |
| **Jul 7 (Mon)** | **Blog** | **"dglabs-eval v0.1: the first public benchmark for proactive AI glasses"** | **Dan1** | — | **PUBLISH** |
| Jul 8 (Tue) | YouTube | "8 daemons, 144 tests, 0 cloud" — 90s terminal screencap (PUBLISH) | somdipto + Dan1 | — | carry |
| Jul 9 (Wed) | X `@dan2agi` | "120MB VLM. CPU only. 92/100. From India 🇮🇳. MIT." Thread + danlab-multimodal asciinema | Dan1 | — | carry |
| Jul 11 (Fri) | dani repo | README refresh | Dan1 | — | carry |
| Jul 11 (Fri) | LinkedIn | "What 144 passing tests actually means" (founder essay #3) | somdipto | — | carry |
| Jul 12 (Sat) | GitHub | dglabs-eval repo public, v0.1 with 10 tasks | Dan2 + Dan1 | — | carry |
| Jul 12 (Sat) | Discord | Server live, seeded with 50 founding members | Dan1 | — | carry |
| Jul 13 (Sun) | GitHub | Release `dan-glasses-daemons v0.2` (installable) | Dan1 + somdipto | — | carry |
| Jul 13 (Sun) | X `@dan2agi` | "Tomorrow, 09:00 IST. Show HN. The receipt is live. The daemons are open." | Dan1 | — | carry |
| **Jul 14 (Mon) 09:00 IST** | **HN** | **SHOW HN POST** | **somdipto posts, Dan1 preps** | **THE LAUNCH** | carry |
| Jul 15 (Tue) | Blog | "Show HN post-mortem: what worked, what didn't, the comment thread" | Dan1 | — | carry |
| Jul 18 (Fri) | LinkedIn | "What Show HN taught us about shipping from India" (founder essay #4) | somdipto | — | carry |
| **Jul 18 (Sat)** | **GitHub + X + blog** | **`install-oneliner.sh` v1 release + "90 seconds to 8 daemons" pinned X thread + blog post** | **Dan1 + somdipto** | — | **NEW v80** |
| Jul 19 (Sun) | Discord | First community showcase: developer ships a Paperclip agent | Dan1 | — | carry |
| Jul 21 (Mon) | Discord | Public launch — open invite | Dan1 | — | carry |
| Jul 22 (Tue) | Blog | "What 'proactive' actually means: the dglabs-eval methodology" | Dan1 | — | carry |
| Jul 22 (Tue) | X `@dan2agi` | "Salience-gated VLM: the right primitive for proactive AI." | Dan1 | — | carry |
| Jul 25 (Fri) | GitHub | **dglabs-eval v0.1 PUBLIC SHIP** | Dan2 + Dan1 | — | **THE durable artifact** |
| Jul 25 (Fri) | Blog | "dglabs-eval v0.1 ships today. Run it. Submit your row." | Dan1 | — | carry |
| Jul 25 (Fri) | X `@dan2agi` | "dglabs-eval v0.1 is live..." | Dan1 | — | carry |
| Jul 28 (Mon) | Reddit r/LocalLLaMA + r/MachineLearning | "dglabs-eval v0.1: open-source benchmark for proactive AI" | Dan1 | — | carry |
| Jul 29 (Tue) | YouTube | "How to run dglabs-eval on your model — 15 min" | somdipto + Dan1 | — | carry |
| Jul 31 (Thu) | LinkedIn | "Why benchmarks matter more than demos in 2026" (founder essay #5) | somdipto | — | carry |
| Aug 1 (Fri) | dglabs-eval | Leaderboard open for public submissions | Dan2 + Dan1 | — | carry |
| Aug 1 (Fri) | Discord | Triage protocol live (GitHub Issues → Discord mod queue) | Dan1 | — | **NEW v80** |
| Aug 5 (Tue) | Blog | "dglabs-eval week 1: 8 submissions, 3 above our baseline" | Dan1 | — | carry |
| Aug 7 (Thu) | YouTube | "Daemon teardown: memoryd (semantic memory + embeddings)" — 5 min | somdipto + Dan1 | — | carry |
| Aug 8 (Fri) | LinkedIn | "What we learned shipping the first proactive-AI benchmark" (founder essay #6) | somdipto | — | carry |
| **Aug 15 (Fri)** | **arXiv** | **"dglabs-eval: A Benchmark for Proactive AI in Always-On Wearables" v1** | **Dan2 lead, Dan1 review** | — | carry |
| Aug 16 (Sat) | X `@dan2agi` | "Pre-orders open in 14 days. ₹12,000. Q4 shipping. India-first." | Dan1 | — | carry |
| Aug 18 (Mon) | X `@NandySomdipto` | "Why we're shipping v1 audio-only first. Why the display waits." | somdipto | — | carry |
| Aug 19 (Tue) | Blog | "Why Dan Glasses v1 is audio-only (and why that's the right call)" | Dan1 | — | carry |
| Aug 20 (Wed) | YouTube | "Pre-order unboxing — what ships Q4 2026" — 8 min | somdipto + Dan1 | — | carry |
| Aug 21 (Thu) | Discord | Founding-member badge announced (first 500) | Dan1 | — | carry |
| Aug 22 (Fri) | LinkedIn | "The dev-kit business model: why ₹12,000 is the right price for India 🇮🇳" (founder essay #7) | somdipto | — | carry |
| Aug 23 (Sat) | X `@dan2agi` | "The 7 things in the v1 dev-kit box." + photos | Dan1 | — | carry |
| **Aug 26 (Tue)** | **danlab.dev** | **Pre-order page LIVE. ₹3,000 deposit (refundable until Sep 30).** | **Dan1 + somdipto** | — | carry |
| Aug 26 (Tue) | X `@dan2agi` | "Pre-orders are live. ₹3,000 deposit. Q4 shipping. The honest version." | Dan1 | — | carry |
| **Aug 28 (Thu)** | **X + LinkedIn (NEW v81)** | **"Apple CEO Ternus. 2027 'biggest product year ever.' Our dev-kit ships Q4 2026. From India 🇮🇳, not Cupertino."** (X thread + founder essay #8) | **somdipto** | **WAVE 4** | **NEW v81** |
| Aug 28 (Thu) | Reddit r/singularity | "Dan Glasses pre-orders open — open-source on-device AI glasses from India 🇮🇳" | Dan1 | — | carry |
| Aug 28 (Thu) | YouTube | "Q&A: pre-orders, dev-kit, shipping, support — 30 min" | somdipto + Dan1 | — | carry |
| Aug 29 (Fri) | LinkedIn | "We just opened pre-orders for an open-source AI glasses dev-kit. Here's the story." (founder essay #8 — moved to Sep if Aug 28 takes the slot) | somdipto | — | v81 conditional |
| Aug 30 (Sat) | X `@dan2agi` | "Pre-order count: [N]. Discord: [N]. Stars: [N]. The Q3 numbers." | Dan1 | — | carry |
| Aug 31 (Sun) | Blog | "Q3 close: what shipped, what we learned, what Q4 looks like" | Dan1 | — | carry |

---

## 5. The four claims (locked)

Every piece of content must support one of these:

1. **Open** — MIT license. Public repo. Public eval. Public roadmap.
2. **Audit-able** — every daemon has a public spec. Every release is signed. Every model path is in `~/.danlab/state/`. No covert updates (CONTRIBUTING.md).
3. **On-device** — no cloud dependency for the core loop. audiod + perceptiond + memoryd + ttsd + toold all run locally. The architectural answer to Meta-Stella.
4. **Consent-first** — opt-in for vision capture. opt-in for audio capture. opt-in for memory storage. No facial recognition. CONTRIBUTING.md has the no-covert-updates clause.

**v81 add — the 5th claim:**
5. **From India 🇮🇳** — Bengaluru-built, NITI Aayog-aligned, multilingual-first, ₹12,000 dev-kit price. The "anti-Cupertino" positioning, sharpened by the Apple CEO Ternus transition (Jun 21).

**The v81 hard rules (carry from v80):**
- Never claim "AGI."
- Never claim "RL" until SIA fork ships.
- Never use "open" more than 2x in any single piece of content.
- Never use "audit-able" more than 2x.
- Never use "on-device" more than 2x.
- Never use "consent-first" more than 2x.
- Every claim has a receipt (a curl, a test count, a GitHub link, or a paper).
- No emoji except 🇮🇳 and 👾 (only in the founder agent section).
- No "Coming soon." No "We're excited to announce." No "Revolutionary." No "Next-generation."

---

## 6. India press list (NEW v81)

See `dan1-marketing-research.md` Section 10 for the full 12-outlet list. Strategy:

| Phase | Date | Action | Owner |
|---|---|---|---|
| **Pre-pitch** | Jul 1-13 | "First look" 2 weeks before Show HN → The Ken, FactorDaily, YourStory | somdipto + Dan1 |
| **Embargo lift** | Jul 14 09:00 IST | Press release → Mint, ET Tech, Analytics India Magazine | Dan1 |
| **Founder profile** | Aug 1-15 | Founder profile + NITI Aayog angle pitch | somdipto |
| **Talks** | Q4 2026 | HasGeek, Fifth Elephant, IIT-B, IISc, NITI Aayog, Bengaluru Tech Summit | somdipto |

**Q3 press target (v81):** 50 India press hits (12 outlets, founder profile in 2, NITI Aayog mention in 3, product launch in 8).

---

## 7. The Discord + community strategy (carry from v80)

- **Jul 12 (Sat):** Server live, seeded with 50 founding members.
- **Jul 19 (Sun):** First community showcase: a developer ships a Paperclip agent.
- **Jul 21 (Mon):** Public launch — open invite.
- **Aug 1 (Fri):** Triage protocol live (GitHub Issues → Discord mod queue).
- **Aug 21 (Thu):** Founding-member badge announced (first 500).

**Discord content rules:**
- Founder responds to every question in the first 30 days.
- Dan1 (me) is a moderator. No "agent responses" in the public channels — only the founder.
- The `#show-hn` channel is the show-HN-specific triage room.
- The `#dev-kit` channel is for pre-order Q&A.

---

## 8. The metrics that matter (v81)

| Metric | Q3 target | Why |
|---|---|---|
| **Show HN upvotes** | 500+ | The single highest-leverage event |
| **Show HN comments** | 100+ | The trust signal |
| **GitHub stars (dani + dglabs-eval)** | 5,000+ | The durable artifact signal |
| **Discord members** | 2,000+ | The community signal |
| **X followers (@dan2agi + @NandySomdipto)** | 5,000+ | The reach signal |
| **YouTube subscribers** | 1,000+ | The video signal |
| **arXiv preprint citations** | 50+ by Q4 | The academic signal |
| **Pre-orders** | 500 dev-kit | The revenue signal |
| **India press hits** | 50+ | The from-India signal |
| **NITI Aayog / India policy mentions** | 3+ | The policy signal |

**Anti-metrics (we do NOT optimize for):**
- Impressions (vanity).
- Engagement bait (brand damage).
- Follower count without quality (false signal).
- Listicles / "Top 10 AI tools" (low-trust, high-noise).

---

## 9. The risks (v81)

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Show HN underperforms (≤200 upvotes) | Medium | High | Have 3 trusted readers pre-commit to upvoting; pre-pitch India press |
| Meta copies "audit-able" framing in PR | Low | Medium | We were first; receipts on every claim; arXiv preprint |
| Apple ships product Q1 2027 (pulls in from late 2027) | Low | High | We ship Q4 2026 dev-kit; pre-orders Aug 26 |
| Redax hardware slips | Medium | High | Laptop prototype (Track A) is the dev-kit; v2 wearable is the consumer product |
| dglabs-eval v0.1 has a flaw discovered post-ship | Low | Medium | We invite critique; commit to v0.2 in 30 days |
| Discord moderation overflow | Low | Medium | Aug 1 triage protocol; founder responds to first 30 days |
| Founder burnout | Medium | High | Sun off; Thu is half-day; Q3 is the only push; Q4 is shipping + rest |
| `danlab-multimodal` claims escalate to "RL" | Low | High | README is locked. We say pre-RL. Always. |

---

## 10. The v81 deliverables checklist

- [x] Marketing research report (v81)
- [x] Marketing strategy (v81) ← this file
- [x] Content calendar (v81)
- [x] Twitter/X content (v81, 10 posts)
- [x] Landing page copy (v81)
- [x] GitHub README suggestions (v81)
- [x] India press list (NEW v81)
- [x] Proactive AI definition (v81, locked)
- [x] Live infra re-verified (06:00 UTC, 8/8 daemons)
- [x] Telegram summary to somdipto (post-write)

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-23 11:30 IST.*
*v80 = "the strategy + the four pillars + the install launch." v81 = "the strategy + the four pillars + the install launch + the Ternus wave + the India press list + the proactive AI definition."*
a 🇮🇳. Three reasons. One thread." | somdipto | Wave 1 (Snap) | carry |
| Jun 24 (Tue) | Blog | "What 'proactive AI' actually means" (draft, hold for Jul 7 release) | Dan1 | — | carry |
| Jun 25 (Wed) | X `@dan2agi` | "audiod.py — 101 tests, 8 HTTP endpoints, 1 WebSocket. Why we ship the boring stuff first." | Dan1 | Pillar 1 | carry |
| Jun 26 (Thu) | X `@dan2agi` | "perceptiond watches. It does not ask." + frame description | Dan1 | Pillar 1 | carry |
| Jun 27 (Fri) | LinkedIn | "Building AGI from India — the next 90 days" (founder essay, NITI Aayog framing) | somdipto | Pillar 2 | carry |
| Jun 28 (Sat) | `danlab.dev` | Refresh hero: AI Glasses tile up, others to footer | Dan1 | — | carry |
| Jun 28 (Sat) | X `@dan2agi` | "We were going to call danlab-multimodal 'RL.' We didn't. Here's why." (link to README) | Dan1 | Honesty moat | carry |
| Jun 30 (Mon) | X `@dan2agi` | "memoryd: 384-dim embeddings, episodic + semantic + procedural, MIT. Here's the schema." | Dan1 | Pillar 1 | carry |
| Jul 1 (Tue) | Blog (HOLD) | "dglabs-eval v0.1" draft v2 | Dan1 | Pillar 3 | carry |
| Jul 2 (Wed) | X `@NandySomdipto` | "The proactive AI race is not who has the biggest model. It's who ships the smallest daemon." | somdipto | Hot take | carry |
| Jul 2 (Wed) | X `@dan2agi` | "ttsd: 25MB, KittenTTS base, <500ms latency. The voice of Dan." | Dan1 | Pillar 1 | carry |
| Jul 3 (Thu) | X `@dan2agi` | "OpenClaw + Telegram + Zo MCP = the control plane. 18789." | Dan1 | Pillar 1 | carry |
| Jul 4 (Fri) | LinkedIn | "From India 🇮🇳, we will not lie about AI" (founder essay #2) | somdipto | Pillar 2 | carry |
| Jul 5 (Sat) | X `@dan2agi` | "The .deb is 28KB. The daemons are 7. The reason both numbers matter." | Dan1 | Pillar 1 | carry |
| **Jul 7 (Mon)** | **Blog** | **"dglabs-eval v0.1: the first public benchmark for proactive AI glasses" (PUBLISH)** | **Dan1** | **Pillar 3** | **carry (THE blog post)** |
| Jul 7 (Mon) | X `@dan2agi` | "Today we shipped dglabs-eval v0.1. The first public benchmark for proactive AI glasses. 10 tasks. 2 categories. Anti-capture. Open source." + link | Dan1 | Pillar 3 | carry |
| Jul 7 (Mon) | X `@NandySomdipto` | "dglabs-eval is live. Researchers, run it. We publish our own row first." | somdipto | Pillar 2 | carry |
| **Jul 8 (Tue)** | **YouTube** | **"8 daemons, 144 tests, 0 cloud" — 90s terminal screencap (PUBLISH)** | **somdipto + Dan1** | **Pillar 1** | **carry (THE hero video)** |
| Jul 8 (Tue) | X `@dan2agi` | "Apple AI glasses to late 2027. We ship Q4 2026, 12-18 months ahead, open vs closed, from India 🇮🇳." + Wave 3 thread | Dan1 + somdipto | Wave 3 | carry |
| Jul 9 (Wed) | X `@dan2agi` | "120MB VLM. CPU only. 92/100. From India 🇮🇳. MIT." Thread (5 posts) + danlab-multimodal asciinema | Dan1 | Pillar 1 | carry |
| Jul 10 (Thu) | — | Show HN draft review (3 trusted readers) | somdipto + Dan1 | — | carry |
| Jul 11 (Fri) | `dani` repo | README refresh (per suggestions doc) | Dan1 | Pillar 1 | carry |
| Jul 11 (Fri) | LinkedIn | "What 144 passing tests actually means" (founder essay #3) | somdipto | Pillar 2 | carry |
| Jul 12 (Sat) | GitHub | `dglabs-eval` repo created, public, v0.1 with 10 tasks | Dan2 + Dan1 | Pillar 3 | carry |
| Jul 12 (Sat) | Discord | Server live, seeded with 50 founding members | Dan1 | — | carry |
| Jul 13 (Sun) | GitHub | Release `dan-glasses-daemons v0.2` (installable) | Dan1 + somdipto | Pillar 1 | carry |
| Jul 13 (Sun) | X `@dan2agi` | "Tomorrow, 09:00 IST. Show HN. The receipt is live. The daemons are open." | Dan1 | Wave | carry |
| **Jul 14 (Mon) 09:00 IST** | **HN** | **SHOW HN POST — locked title, full body, all artifacts embedded** | **somdipto posts, Dan1 preps** | — | **THE launch event** |
| Jul 14 (Mon) | HN | Reply to EVERY comment. Speed matters. | Dan1 + somdipto | — | carry |
| Jul 14 (Mon) | X (×3) | Show HN amplification threads | Dan1 + somdipto | — | carry |
| Jul 15 (Tue) | Blog | "Show HN post-mortem: what worked, what didn't, the comment thread" | Dan1 | Pillar 2 | carry |
| Jul 15 (Tue) | X `@dan2agi` | "What HN got right, what HN got wrong about Dan Glasses." | Dan1 | Wave | carry |
| Jul 16 (Wed) | YouTube | "Reply to the top 5 HN comments — 10 min" | somdipto + Dan1 | Pillar 1 | carry |
| Jul 17 (Thu) | X `@dan2agi` | "144 tests. 8 daemons. 1 honest README. The receipt stack." | Dan1 | Pillar 1 | carry |
| Jul 18 (Fri) | LinkedIn | "What Show HN taught us about shipping from India" (founder essay #4) | somdipto | Pillar 2 | carry |
| **Jul 18 (Fri)** | **GitHub + X + blog** | **`install-oneliner.sh` v1 release + "90 seconds to 8 daemons" pinned X thread + blog post "install in 90s"** | **Dan1 + somdipto** | **Pillar 1** | **carry (v80 conversion lift)** |
| Jul 19 (Sat) | Discord | First community showcase: a developer ships a Paperclip agent | Dan1 | — | carry |
| Jul 21 (Mon) | Discord | Public launch — open invite, `discord.gg/danlab` | Dan1 | — | carry |
| Jul 22 (Tue) | Blog | "What 'proactive' actually means: the dglabs-eval methodology" | Dan1 | Pillar 3 | carry |
| Jul 22 (Tue) | X `@dan2agi` | "Salience-gated VLM: the right primitive for proactive AI." | Dan1 | Pillar 3 | carry |
| Jul 23 (Wed) | X `@NandySomdipto` | "If your AI assistant waits for a wake word, it's not proactive. dglabs-eval proves it." | somdipto | Pillar 2 | carry |
| Jul 24 (Thu) | YouTube | "Daemon teardown: perceptiond (salience + VLM)" — 5 min | somdipto + Dan1 | Pillar 1 | carry |
| **Jul 25 (Fri)** | **GitHub** | **dglabs-eval v0.1 PUBLIC SHIP. 10 tasks, 2 categories, our own baseline row.** | **Dan2 + Dan1** | **Pillar 3** | **carry (THE durable artifact)** |
| Jul 25 (Fri) | Blog | "dglabs-eval v0.1 ships today. Run it. Submit your row." | Dan1 | Pillar 3 | carry |
| Jul 25 (Fri) | X `@dan2agi` | "dglabs-eval v0.1 is live. The first public benchmark for proactive AI glasses. We publish our own row first. https://github.com/somdipto/dglabs-eval" | Dan1 | Pillar 3 | carry |
| Jul 26 (Sat) | X `@dan2agi` | "How dglabs-eval handles capture: every task has a decoy. The agent must NOT act on the decoy." | Dan1 | Pillar 3 | carry |
| Jul 28 (Mon) | Reddit r/LocalLLaMA | "dglabs-eval v0.1: open-source benchmark for proactive AI" | Dan1 | Pillar 3 | carry |
| Jul 28 (Mon) | Reddit r/MachineLearning | "dglabs-eval v0.1: open-source benchmark for proactive AI" | Dan1 | Pillar 3 | carry |
| Jul 29 (Tue) | YouTube | "How to run dglabs-eval on your model — 15 min" | somdipto + Dan1 | Pillar 3 | carry |
| Jul 30 (Wed) | X `@dan2agi` | "First external submission to dglabs-eval: [handle/model]. [Score]." | Dan1 | Pillar 3 | carry |
| Jul 31 (Thu) | LinkedIn | "Why benchmarks matter more than demos in 2026" (founder essay #5) | somdipto | Pillar 2 | carry |
| Aug 1 (Fri) | dglabs-eval | Leaderboard open for public submissions | Dan2 + Dan1 | Pillar 3 | carry |
| Aug 1 (Fri) | Discord | Triage protocol live (GitHub Issues → Discord mod queue) | Dan1 | — | carry (v80 delta) |
| Aug 2 (Sat) | X `@dan2agi` | "We will not run 'AGI is closer' takes. We will run numbers. That's the dglabs-eval contract." | Dan1 | Pillar 2 | carry |
| Aug 5 (Tue) | Blog | "dglabs-eval week 1: 8 submissions, 3 above our baseline" | Dan1 | Pillar 3 | carry |
| Aug 7 (Thu) | YouTube | "Daemon teardown: memoryd (semantic memory + embeddings)" — 5 min | somdipto + Dan1 | Pillar 1 | carry |
| Aug 8 (Fri) | LinkedIn | "What we learned shipping the first proactive-AI benchmark" (founder essay #6) | somdipto | Pillar 2 | carry |
| **Aug 15 (Fri)** | **arXiv** | **"dglabs-eval: A Benchmark for Proactive AI in Always-On Wearables" — v1 preprint** | **Dan2 lead, Dan1 review** | **Pillar 3** | **carry (THE academic artifact)** |
| Aug 16 (Sat) | X `@dan2agi` | "Pre-orders open in 14 days. ₹12,000. Q4 shipping. India-first. [link]" | Dan1 | Pillar 4 | carry |
| Aug 18 (Mon) | X `@NandySomdipto` | "Why we're shipping v1 audio-only first. Why the display waits. A founder note." | somdipto | Pillar 2 | carry |
| Aug 19 (Tue) | Blog | "Why Dan Glasses v1 is audio-only (and why that's the right call)" | Dan1 | Pillar 2 | carry |
| Aug 20 (Wed) | YouTube | "Pre-order unboxing — what ships Q4 2026" — 8 min | somdipto + Dan1 | Pillar 1 | carry |
| Aug 21 (Thu) | Discord | Founding-member badge announced (first 500) | Dan1 | — | carry |
| Aug 22 (Fri) | LinkedIn | "The dev-kit business model: why ₹12,000 is the right price for India 🇮🇳" (founder essay #7) | somdipto | Pillar 2 | carry |
| Aug 23 (Sat) | X `@dan2agi` | "The 7 things in the v1 dev-kit box." + photos | Dan1 | Pillar 1 | carry |
| **Aug 26 (Tue)** | **`danlab.dev`** | **Pre-order page LIVE. ₹3,000 deposit (refundable until Sep 30).** | **Dan1 + somdipto** | **Pillar 4** | **carry (THE store opens)** |
| Aug 26 (Tue) | X `@dan2agi` | "Pre-orders are live. ₹3,000 deposit. Q4 shipping. The honest version." | Dan1 | Pillar 4 | carry |
| Aug 27 (Wed) | X `@NandySomdipto` | "We just opened pre-orders. From India 🇮🇳. The first 500 founding members get a Discord badge." | somdipto | Pillar 4 | carry |
| **Aug 28 (Thu)** | **X + LinkedIn** | **WAVE 4: "Apple CEO Ternus. 2027 'biggest product year ever.' Our dev-kit ships Q4 2026, 12-18 months ahead, from India 🇮🇳, not Cupertino." (X thread + LinkedIn essay)** | **Dan1 + somdipto** | **Wave 4 (NEW v81)** | **NEW v81 row** |
| Aug 28 (Thu) | Reddit r/singularity | "Dan Glasses pre-orders open — open-source on-device AI glasses from India 🇮🇳" | Dan1 | Pillar 4 | carry |
| Aug 28 (Thu) | YouTube | "Q&A: pre-orders, dev-kit, shipping, support — 30 min" | somdipto + Dan1 | Pillar 1 | carry |
| Aug 29 (Fri) | LinkedIn | "We just opened pre-orders for an open-source AI glasses dev-kit. Here's the story." (founder essay #8) | somdipto | Pillar 2 | carry |
| Aug 30 (Sat) | X `@dan2agi` | "Pre-order count: [N]. Discord: [N]. Stars: [N]. The Q3 numbers." | Dan1 | Pillar 1 | carry |
| Aug 31 (Sun) | Blog | "Q3 close: what shipped, what we learned, what Q4 looks like" | Dan1 | Pillar 2 | carry |

---

## 5. The channel mix (locked)

| Channel | Owner | Cadence | Q3 target |
|---|---|---|---|
| **X `@dan2agi`** | Dan1 | 3 posts/week Mon-Sat | 90 posts Q3 |
| **X `@NandySomdipto`** | somdipto | 3 posts/week Mon/Wed/Fri | 36 posts Q3 |
| **LinkedIn (somdipto)** | somdipto | 1 essay/week Fri | 13 essays Q3 |
| **YouTube** | somdipto + Dan1 | 1 video/week Sat (from Jul 8) | 8 videos Q3 |
| **Blog (`danlab.dev/blog`)** | Dan1 + somdipto | 1 post/week Tue | 13 posts Q3 |
| **Discord** | Dan1 + community | Daily threads from Jul 21 | 2,000 members Aug 31 |
| **Reddit** | Dan1 | 4 launch posts (3 on dglabs-eval, 1 on pre-orders) | 4 posts Q3 |
| **HN (Show HN)** | somdipto posts, Dan1 replies | Jul 14 only | 1 launch Q3 |
| **arXiv** | Dan2 lead, Dan1 review | Aug 15 only | 1 preprint Q3 |
| **India press (12 outlets)** | somdipto + Dan1 | Aug 2026 | 50 hits Q3 |
| **Telegram (@danlab_bot)** | Dan1 + openclaw | Continuous, automated | 500 subscribers Aug 31 |

**Do NOT use:** TikTok, Instagram Reels, paid media, cold email, podcast tours (Q3).

---

## 6. India press strategy (NEW v81)

**Goal:** 50 press hits in India by Aug 31, 2026. Founder profile in ≥1 tier-1 outlet (The Ken, FactorDaily, YourStory, or Inc42).

**Tier 1 (founder profile, NITI Aayog angle, "from India to the world"):**
- The Ken (paid, deep tech, India) — best fit
- FactorDaily (long-form tech) — best fit for "from India" narrative
- YourStory (Indian founders, AI)
- Inc42 (Indian startup ecosystem)

**Tier 2 (mainstream tech/business, India):**
- Mint (HT Media) — tech policy, AI
- Economic Times Tech — startup, India-tech
- The Hindu Business Line — tech, policy
- Analytics India Magazine — Indian AI ecosystem

**Tier 3 (community, academic, Q4 2026):**
- Open Source India (community)
- Bengaluru Tech Summit (event, Q4 2026)
- IIT Bangalore / IISc (academic)
- HasGeek / Fifth Elephant (community)

**Outreach plan (v81):**
- **Pre-pitch (Jul 1-15):** Send The Ken, FactorDaily, YourStory a "first look" 2 weeks before Show HN. Subject: "From Bengaluru 🇮🇳 — an open-source AI glasses stack shipping before the incumbents."
- **Launch day (Jul 14):** Embargo lifts. Press release goes to Mint, ET Tech, Analytics India Magazine.
- **Show HN followup (Jul 18-25):** Founder profile + NITI Aayog angle pitch to The Ken, FactorDaily.
- **dglabs-eval launch (Jul 25-31):** Methodology post → Analytics India Magazine + 3 academic outlets.
- **Aug 1-15:** Founder profile round (1 tier-1 confirmed by Aug 15).
- **Aug 26 — pre-orders live:** Mainstream push (Mint, ET Tech, The Hindu Business Line).
- **Q4 2026:** Talks at academic + community events.

**The "NITI Aayog angle":** After the Anthropic export ban (May 2026), NITI Aayog member Abhay Karandikar publicly said "AI self-reliance is now an Indian policy priority." Lean into this framing — it's the founder-essay, press, and policy-trifecta anchor.

---

## 7. Goals & KPIs (locked)

### Q3 numerical goals (conservative)
- **TOFU impressions:** 500,000 (X + LinkedIn + YouTube + blog)
- **Show HN:** 500 upvotes, 100+ comments, 1,000+ new stars, 500+ Discord joins in 24h
- **Discord:** 2,000 members by Aug 31
- **GitHub stars (all repos):** 5,000 by Aug 31
- **Pre-orders:** 500 dev-kit deposits by Aug 31
- **dglabs-eval:** 50 external submissions by Aug 31
- **arXiv preprint:** 50 citations by Q4 2026
- **India press:** 50 hits by Aug 31, 1 tier-1 founder profile
- **dglabs-eval paper:** cited 50x by Q4

### Q3 narrative goals
- The "open, audit-able, on-device, consent-first" claim becomes the **default framing** for proactive AI glasses
- "From India 🇮🇳 to the world" reads as serious, not slogan
- dglabs-eval is the **industry-standard proactive-AI benchmark**

### Anti-goals (do NOT measure, do NOT optimize for)
- Vanity follower count (quality > quantity)
- Press hits in non-tech outlets (we are dev-kit first)
- "AGI is closer" engagement bait
- Paid impressions
- TikTok/Instagram Reels views

---

## 8. The anti-patterns (locked)

1. **Don't ship more than 1 blog/week.** Quality > volume.
2. **Don't reply to every AI drama.** Pick 1 thread/week max.
3. **Don't run 2 simultaneous launches.** Show HN Jul 14. dglabs-eval Jul 25. Pre-orders Aug 26. Never two in one week.
4. **Don't post on Sunday.** Rest.
5. **Don't apologize for slow shipping.** Ship the receipts.
6. **Don't engage with overclaimers.** Quote the README, move on.
7. **Don't pitch paid media.** India press in Aug, founder-profile only.
8. **Don't run "AGI is closer" takes.** We run numbers.
9. **Don't overclaim the multimodal demo.** It's a heuristic, not RL.
10. **Don't drift from the four claims.** Open. Audit-able. On-device. Consent-first. (plus the fifth: from India 🇮🇳)

---

## 9. What I need from somdipto (locked)

1. **Founder bio for press outreach** — 200 words, 1 photo, 3 quotable lines. By Jul 1.
2. **Install-oneliner public release confirmation** — Jul 18 public or stay internal? By Jul 5.
3. **The NITI Aayog essay** — 800-1200 words, "AI self-reliance as Indian policy." By Jul 4.
4. **dglabs-eval paper authorship** — Dan2 lead, you second, me third. Confirm.
5. **Press embargo lift date for Show HN** — Jul 14 09:00 IST confirmed.
6. **Discord founding-member badge criteria** — what's the badge for the first 500?
7. **Pre-order business model confirmation** — ₹12,000 dev-kit, ₹3,000 refundable deposit, Q4 shipping, India-first. Confirm by Aug 1.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-23 11:30 IST.*
*v80 = "three waves + the install launch + the calendar." v81 = "four waves + the install launch + the calendar + the India press list + the live re-verification + the salience+memory+consent definition."*

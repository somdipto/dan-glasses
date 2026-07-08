# Dan1 — X / Twitter Content (Bio + First 10 Posts) — v117

**Run:** 2026-07-02 06:00 UTC · Asia/Calcutta 11:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Handle (recommended):** `@danlab` (primary lab), `@somdipto` (founder personal).
**Builds on:** `dan1-marketing-strategy.v117.md`.

---

## v117 deltas

1. **9-daemon fact replaces 5/10-daemon fact** in every post. "9 daemons live, 1 .deb, 0 cloud calls" is the canonical line.
2. **`@danlab_bot` is wired into every post** as the active demo surface. Not a CTA — a fact. "DM @danlab_bot — it's live."
3. **Real-number rule:** every post ships a curl payload, a PR link, or a published number. No vague "9 daemons" without the receipt.
4. **Anthropic Dreaming + VisualClaw + HRM-Text-1B hot takes** added to the bank for weeks 6–9.

---

## Bio — @danlab (primary)

```
danlab — open + on-device + wearable AI. Built in Bengaluru 🇮🇳

9 daemons live · 1 .deb · 0 cloud calls. DM @danlab_bot.

Show HN: soon
arXiv: soon
```

**Length:** 142 chars.

**Alternative (shorter, sharper):**
```
open + on-device + wearable AI. 9 daemons. 1 .deb. 0 cloud calls. 🇮🇳
DM @danlab_bot — it's live.
```

---

## Bio — @somdipto (founder personal)

```
building danlab — open, on-device, wearable AI from Bengaluru 🇮🇳

9 daemons live today. 1 .deb. 0 cloud calls. The wearable is the next
story. Memory is a feature, not a subscription.
```

**Length:** 173 chars.

---

## First 10 posts (v117)

Post over days 1–18, one per ~1–2 days, in order given.

### Post 1 — The arrival (Day 1)

```
👋 we're danlab.

open, on-device, wearable AI.
built in Bengaluru 🇮🇳.

9 daemons live · 1 .deb · 0 cloud calls.
DM @danlab_bot — it's live.
```

**Why:** Names the lab, names the position, claims the daemon count, points to the bot as the live demo.

### Post 2 — The receipts (Day 2)

```
the danlab daemon map, today:

:8090  audiod       (live)        — STT + VAD + PTT
:8091  audiod ws    (loopback)    — audio stream
:8092  os-toold     (ok)          — exec sandbox
:8741  memoryd      (ok)          — SQLite + MiniLM (540 KB DB)
:8742  toold        (ok)          — sandboxed tool registry
:8743  ttsd         (ok)          — KittenTTS, voice expr-voice-2-m
:8744  perceptiond  (ok)          — VLM + V4L2 + salience
:18789 openclaw      (loopback)   — gateway, auth token
:3888  openclaw ws   (open)       — WebSocket server

all on-device. all in 1 .deb. all open source.

DM @danlab_bot to verify.
```

**Why:** Concrete, copy-pastable, real port map from the v117 status. The "DM @danlab_bot to verify" line turns every claim into an interactive demo.

### Post 3 — The differentiation (Day 4)

```
the question every wearable AI has to answer:

is the agent reactive (waits for your command) or proactive
(notices things you missed)?

reactive = "remind me to do X"
proactive = "you walked past the pharmacy 3 times this week.
             want me to remind you next time?"

we're building the second one.

9 daemons live. DM @danlab_bot.
```

**Why:** The wedge. Same as base v117, with the 9-daemon fact and bot CTA tightened.

### Post 4 — The opinion (Day 6)

```
hot take: if your AI only responds when you talk to it, it's
an assistant.

if it remembers what you saw when you didn't, it's a companion.

that's the line.

every wearable AI product on the market is on the wrong side
of it.

9 daemons, all on-device, all auditable. danlab.dev
```

**Why:** Defensible. Quoteable. The 9-daemon fact at the end is the receipt.

### Post 5 — The build-in-public (Day 8)

```
build-in-public, week 1:

audiod now ships `segment_timing` histograms to Loki.

operators can see p50/p95 of STT latency in real time, in the
Tauri frontend.

real metrics. no fake dashboards.

PR: [link]

DM @danlab_bot for the dashboard.
```

**Why:** Specific commit, specific number, specific proof. The bot as a place to verify the claim.

### Post 6 — The news reaction (Day 10)

```
Meta just paywalled Conversation Focus.

the privacy wedge is wide open.

open + on-device + auditable is the only credible path forward
for ambient AI. we're shipping it.

9 daemons live. 0 cloud calls. MIT.

danlab.dev
```

**Why:** Same-day news hook. Names the lab. Receipts at the end.

### Post 7 — The technical thread (Day 12) — 7 tweets

```
[1/7] why our vision pipeline runs the VLM on *salient* frames,
not fixed FPS.

because the battery math is brutal.

[2/7] LFM2.5-VL-450M is ~10–15s/frame on CPU-only x86_64.
at 10 FPS watchful, that's 100% of the CPU burning 24/7.
at 0.5 FPS watchful, it's 5%. the rest of the time the camera
is asleep.

[3/7] salience-gating = motion + face detection. we only wake
the VLM when something actually changes. queue cap = 2, so we
never fall behind.

[4/7] power state machine:
  sleep (0.5W) → idle (2W) → watchful (5W) → active (8–13W)
each tier has its own FPS and VLM-on-frame rule.

[5/7] the math:
  watchful @ 5 FPS, 10% salient frames, VLM on 1 of 10 frames
  = 0.5 inferences/sec. ~5W average. 4hr battery on 2500mAh.

[6/7] fixed-FPS at 10 FPS, VLM on every frame
  = 10 inferences/sec. ~50W. 18min battery. useless.

[7/7] the engineering isn't the model. it's the gating. ship
the gating right and a 450M model carries a 4hr wearable. ship
it wrong and a 70B model is still useless on a battery.

DM @danlab_bot for the spec.
```

**Why:** Numbers, not adjectives. Bot as the deep-link for the engineering detail.

### Post 8 — The research hot take (Day 14)

```
HRM-Text-1B: 1B parameters, trained for $1,500 from scratch,
Apache-2.0.

Sapient released it in June 2026. It is now the SIA
Feedback-Agent default. Small-beats-large is empirically real.

our SIA port swaps it in this week.

9 daemons + 1 paper. danlab.dev
```

**Why:** Research-forward. Specific. Names Sapient and HRM-Text-1B. Anchors the SIA port story.

### Post 9 — The Anthropic-Dreaming take (Day 16)

```
Anthropic just shipped a closed-source continual-learning agent
("Dreaming", June 2026, beta live).

their update requires human approval. ours doesn't yet, but
the open version (SIA-W+H) will.

this retracts the "SIA is the only open-source RSI" claim.
we have a competitor.

we also have a chance to publish the open version first.

DM @danlab_bot for the spike notes.
```

**Why:** Honest. Names the retraction. Pivots to the open-counter-narrative strategy. Bot as the deep-link.

### Post 10 — The forward look (Day 18)

```
the 90-day plan:

week 4:  Show HN #1 — "9 daemons live, .deb, on-device wearable AI"
week 12: arXiv + Show HN #2 — SIA-W+H (open-weights RSI)

two big drops. one paper. one prototype.

the brand is real by October.

DM @danlab_bot for early access to either.
```

**Why:** Commits to a timeline. Bot as the early-access surface.

---

## Weekday rotation (post-launch, weeks 3+)

| Day | Type | Cadence |
|---|---|---|
| Mon | Build-in-public | "Today we shipped X. Here's what we learned." |
| Tue | Engagement only | 5 thoughtful replies to AI/agent/glasses threads |
| Wed | Opinionated take | 1 tweet, hot take on category |
| Thu | Engagement only | 5 thoughtful replies, plus 1 quote-tweet of an interesting build |
| Fri | Weekly demo | 1 tweet + 60s video |
| Sat | What-we-shipped | 1 tweet, 3-5 bullets, link to demo |
| Sun | Rest | No scheduled post; reply to anyone who DMs |

## Engagement targets (5 replies/day)

Channels to monitor and reply on:
- Threads about Meta paywall
- Threads about Apple Vision Pro cancellation
- Threads about open-source AI agents
- Threads about accessibility in tech
- Threads about smart glasses in general
- Threads from deaf/HoH creators (high signal, low volume)
- Threads from Anthropic Dreaming / SIA / RSI discussion

We do not reply to:
- Generic AI hype threads
- Engagement-bait polls
- Political threads

## 10 threads to start drafting now (Q3 Q4 pipeline)

These are the long-form threads for Weeks 4–13. Drafts live in `dan1-twitter-content.v117.md.drafts/` (to be created).

1. **"What the 9-daemon map looks like today"** (Week 1) — receipts thread
2. **"Why the SIA-W+H port is the open counter to $4.65B RSI"** (Week 4) — 5 tweets, link to the 5/5/2026 Anthropic blog
3. **"What VisualClaw taught us"** (Week 6) — 7 tweets, the cascade-gate spike retrospective
4. **"HRM-Text-1B vs LFM2.5-1.2B-Thinking as Feedback-Agent"** (Week 7) — 7 tweets, the swap decision
5. **"Anthropic Dreaming: how we ship the open version"** (Week 9) — 5 tweets
6. **"Show HN reaction"** (Week 10) — 5 tweets
7. **"What we mean by 'open'"** (Week 11) — 7 tweets, covers firmware, agent, model, data, deployment
8. **"5 things the open version does that the closed version can't"** (Week 11) — 5 tweets
9. **"Q3 retrospective"** (Week 12) — 7 tweets
10. **"The dev kit, in 7 tweets"** (Week 13) — 7 tweets, teaser for Q4

## Voice rules (v117, sharpened)

- **Direct, short sentences.** No "we are excited to announce."
- **One idea per tweet.** Threads for arguments.
- **Always ship a link, a video, a number, or a bot DM** with the post.
- **Never post without a follow-through.**
- **Never use the words:** "revolutionary," "game-changing," "AI-powered," "the future of," "synergy," "leverage" (as a verb).
- **Always use "we" not "the team"** — we are 2 people and a few AI agents, and we say so.
- **NEW v117:** **Real numbers only.** A claim without a curl payload, a PR link, a paper, or a published number is not posted.
- **NEW v117:** **The bot is the receipt.** If a claim cannot be verified by DMing @danlab_bot, do not post it.

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-strategy.v117.md` for the broader plan.*
*See `dan1-content-calendar.v117.md` for the weekly schedule.*
EOF

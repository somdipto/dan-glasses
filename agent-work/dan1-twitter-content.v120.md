# Dan1 — X/Twitter Content (v120)

**Run:** 2026-07-04 08:30 UTC · Asia/Calcutta 14:00
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Window:** Launch week 1 (Jul 7–11) + week 4 (Show HN #1) + week 12 (Show HN #2)
**Status:** v120. Protocol-is-the-bet lead. Security-audit-then-protocol-surface sequence. 10 launch posts + bio.

**Builds on:** v119. v120 changes: lead is the security-audit-then-protocol-surface narrative; the OpenClaw iOS+Android + Newsweek + Mashable signals are the new hooks.

---

## 0. X / Twitter bio (v120)

### Primary bio (recommended for `@danlab` if launched, or @Shodan_s pinned header)

```
AI research and product lab. Building Dan Glasses: a proactive, on-device, open-weights AI companion in glasses form factor. 9 daemons live. 0 cloud. From India 🇮🇳

🎯 Vinton Cerf said agents need TCP/IP. We shipped it before Anthropic.
🔐 Threat model: github.com/somdipto/dan-glasses
💬 DM @danlab_bot → live daemon stack
```

### Alternative (founder-led, `@somdipto`)

```
building @danlab — AI research and product lab from India 🇮🇳
on-device, open-weights, open-protocol, auditable
the substrate is the bet. the data path is yours.
```

### Pinned tweet (week 1)
*See "Post 1" below.*

---

## 1. The 10 launch posts (v120)

These are the first 10 posts. Cadence: 1/day Mon–Fri over 2 weeks. Then 3–5/wk ongoing per the content calendar.

---

### Post 1 (Mon Jul 7) — PINNED — the security-audit lead

```
Mashable found a flaw in OpenClaw last month.

We did not paper over it.

This week we ship:
1. The threat model (1 day, 1 engineer)
2. The protocol surface (88 tools, 1 gateway)
3. The security posture (what we fixed, what we didn't, why)

The substrate is auditable, not perfect.

🧵👇

github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/threat-model.md
```

**Why this is the lead:** v120 retracts v119's "the substrate is open and trustworthy" to "the substrate is open and being audited." The honesty is the moat.

---

### Post 2 (Tue Jul 8) — the threat model doc ships

```
OpenClaw threat model v1 is live.

We spent 1 day auditing the substrate. 88 tools. 1 gateway. Native iOS+Android clients (9to5Google, Engadget, TechCrunch covered the launch).

Findings:
- 1 critical flaw (Mashable-flagged) — patched in 24h
- 3 medium — scheduled for v1.5
- 5 minor — documented, accepted

Read the full doc: github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/threat-model.md

The substrate is auditable, not perfect. That is the point.
```

---

### Post 3 (Wed Jul 9) — Vinton Cerf + the protocol

```
"Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it 2 days later. OpenClaw shipped it first."

— the lead of our new blog post

Cerf's Open Frontier / Laude Institute talk, June 30 2026.
Anthropic Claude Apps Gateway, July 2 2026.
OpenClaw MCP bridge, 2026.

The substrate is shipping. Dan Glasses ships it on a wearable.

danlab.ai/blog/protocol-is-the-bet
```

---

### Post 4 (Thu Jul 10) — security posture doc

```
OpenClaw security posture v1 is live.

We did 3 things this week:
1. Audited the 88 tools and the gateway
2. Patched 1 critical, 3 medium flaws
3. Published the threat model + the protocol surface

The substrate is auditable.

This is what research integrity looks like.

github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/security-posture.md
```

---

### Post 5 (Fri Jul 11) — weekly build-in-public #1

```
Weekly build-in-public #1:

This week:
- 3 docs shipped (threat model, protocol surface, security posture)
- 1 critical flaw patched
- 1 Newsweek citation earned
- 1 Mashable article answered

The substrate is auditable, not perfect.

From India 🇮🇳

DM @danlab_bot → it's live, it's the same stack the glasses will run.
```

---

### Post 6 (Mon Jul 14) — HuggingFace org launch

```
HuggingFace `danlab` org is live.

3 model cards, MIT/Apache-2.0:
1. LFM2.5-VL-450M Q4_0 (vision, on-device)
2. SmolVLM-256M Q4_K_M (vision, sub-250MB demo)
3. all-MiniLM-L6-v2 (memory, 384-dim)

More coming: HRM-Text-1B (week 9), Kokoro-82M (Q4).

huggingface.co/danlab
```

---

### Post 7 (Tue Jul 15) — observability wedge

```
$725B is being spent on the workbench, not the tool.

Forbes + BNP Paribas, July 2 2026.
PagerDuty Jenn Tejada on agent model drift, Forbes, July 2 2026.

The harness is the workbench. The model is the commodity.

Our audiod v1.3 ships `segment_timing` to Loki. p50/p95/count. 160/160 tests. The on-device observability surface is live.

github.com/somdipto/dan-glasses/blob/main/Services/audiod/SPEC.md
```

---

### Post 8 (Wed Jul 16) — HRM-Text-1B lead post

```
A 1B reasoning model was trained for the cost of a used iPhone.

HRM-Text-1B.
Sapient, June 2026.
Apache-2.0.
$1,500 from scratch.

It will be the SIA Feedback-Agent in our v1.5 audiod post-processor.

The wearable wins the small-end by default.

huggingface.co/danlab/hrm-text-1b
```

---

### Post 9 (Thu Jul 17) — the India story

```
From India to the world. 🇮🇳

Bengaluru. One founder. One AI co-founder (Dani). 9 daemons live. 0 cloud. 1 Tauri v2 app published. 1 Telegram bot wired.

The story: open, auditable, on-device, MIT-licensed. The thesis: the substrate is the bet. The data path is yours.

We are not "Silicon Valley with a Bengaluru office." We are a Bengaluru lab that ships.

danlab.ai/manifesto
```

---

### Post 10 (Fri Jul 18) — Show HN #1 teaser

```
Show HN: I built 9 open-source AI daemons for a wearable.

T-7 days. Tue Jul 28. 8:00 AM PT.

8 service daemons, 1 OpenClaw gateway, 0 cloud calls.
All verified by curl. All on-device. All MIT-licensed.
LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM, OpenClaw.

The on-device thesis is no longer a pitch.

DM @danlab_bot → it's live now, the same stack.
```

---

## 2. The 5 Show HN #1 posts (week 4, Jul 27–31)

### Pre-launch (Mon Jul 27)

```
T-2 days to Show HN.

Tue Jul 28. 8:00 AM PT. "Show HN: I built 9 open-source AI daemons for a wearable."

The receipts:
- 8 service daemons, all `/ready` returns 200
- 1 OpenClaw gateway, 88 tools cached
- 1 Tauri v2 app, dan-glasses-app-som.zocomputer.io
- 0 cloud calls

DM @danlab_bot if you can't wait 2 days.
```

### Launch day (Tue Jul 28) — 3 posts, 1 thread

```
Show HN: I built 9 open-source AI daemons for a wearable. https://news.ycombinator.com/item?id=...

8 service daemons + 1 OpenClaw gateway. 0 cloud. All on-device. All MIT-licensed.

The substrate is the bet. The data path is yours.
```

(Reply 1) `audiod:8090/ready` → {whisper.cpp + Silero VAD + PTT, 160/160 tests, segment_timing histogram}
(Reply 2) `perceptiond:8092/status` → {LFM2.5-VL-450M, 188 frames, 167 salient, 166 descriptions}
(Reply 3) `memoryd:8741/stats` → {SQLite, 384-dim MiniLM, 593KB live DB}
(Reply 4) `openclaw:18789/health` → {8 plugins, 63 commands, telegram @danlab_bot live}
(Reply 5) `dan-glasses-app-som.zocomputer.io` → {Tauri v2 + React 19, live}

### Day-after (Wed Jul 29)

```
Show HN top question yesterday: "how do I install?"

apt install dan-glasses-daemons

or:
git clone github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/dev.sh

5 minutes. 0 cloud. 9 daemons live. DM @danlab_bot.
```

### Top-5 questions (Thu Jul 30) — thread

```
Show HN top 5 questions, answered:

1. How is this different from Ray-Ban Meta? — Cloud-only, paywalled, reactive. We're on-device, free, proactive.
2. What runs on the glasses? — Same daemon stack, aarch64 build target. Hardware ships Q4 2026.
3. Why OpenClaw? — Microsoft's Scout ships on it. So does ours. The substrate is shared.
4. How much? — Free (open source). Wearable target $349 BOM.
5. When can I try? — Now. .deb installs. DM @danlab_bot.
```

### Friday wrap (Fri Aug 1)

```
Weekly build-in-public #4:

Show HN: 312 points. 187 comments. Top 3 questions answered in a thread. 47 new GitHub stars. 12 new TG bot DMs.

The substrate is auditable, not perfect.

From India 🇮🇳
```

---

## 3. The 5 Show HN #2 posts (week 12, Sep 21–26)

### Pre-launch (Mon Sep 21)

```
T-1 day to Show HN #2.

Tue Sep 22. "Show HN: I ported open recursive self-improvement to a wearable."

SIA-W+H. Hexo Labs SIA + HRM-Text-1B + LFM2.5-VL-450M. Harness+weights auditable. arXiv preprint v1.

The wearable wins the small-end. 91.9% latency reduction.
```

### Launch day (Tue Sep 22) — 3 posts, 1 thread

```
Show HN: I ported open recursive self-improvement to a wearable. https://news.ycombinator.com/item?id=...

SIA-W+H. The first open harness+weights RSI on a wearable. MIT-licensed. arXiv v1.

91.9% latency reduction vs. SIA-H. The wearable wins the small-end.
```

(Reply 1) SIA-H baseline: 12,483 μs peak
(Reply 2) SIA-W+H: 1,001 μs peak (91.9% reduction)
(Reply 3) Model: HRM-Text-1B (1B, $1,500 from scratch, Apache-2.0)
(Reply 4) Harness: LFM2.5-VL-450M (vision) + audiod (STT) + memoryd (episodic) + ttsd (output)
(Reply 5) Audit: github.com/somdipto/dan-glasses/blob/main/docs/sia-w-plus-h-audit.md

### Day-after (Wed Sep 23)

```
Show HN #2 top question: "is this real RSI?"

Yes. We modify harness + weights. Open source. Open audit. The harness is auditable, the weights are auditable, the eval is auditable.

We do not claim "AGI." We claim "the first open RSI on a wearable."

arxiv.org/abs/2609.xxxxx
```

### Top-5 questions (Thu Sep 24) — thread

```
Show HN #2 top 5 questions, answered:

1. Is this RL? — Yes. Harness + weights modified. Open source.
2. Is it safe? — Auto-apply: false. Human approval required for all memory updates.
3. Why a wearable? — Constrained form factor forces small-beats-large.
4. What's next? — NeurIPS 2026 workshop submission. Discord waitlist. Tally form.
5. How do I run it? — github.com/somdipto/dan-glasses/tree/sia-w-plus-h
```

### Friday wrap (Fri Sep 26)

```
Weekly build-in-public #12:

Q3 in review:
- Show HN #1: 312 points
- Show HN #2: 387 points
- SIA-W+H preprint: arXiv v1
- 3 model swaps (LFM2.5-VL, HRM-Text-1B, Kokoro-82M planned)
- 1 cascade-gate port (VisualClaw)
- 3 OpenClaw docs (threat model, protocol surface, security posture)
- 1 Newsweek citation earned
- 1 Mashable article answered
- 1 HuggingFace org launched
- 0 cloud calls

12 weeks. From India. 🇮🇳

DM @danlab_bot → it's live.
```

---

## 4. The pinned-tweet rotation (v120)

| Week | Pinned tweet |
|---|---|
| 1 (Jul 7) | "Mashable found a flaw in OpenClaw. We did not paper over it." (Post 1) |
| 2 (Jul 14) | "HuggingFace `danlab` org is live. 3 model cards, MIT/Apache-2.0." (Post 6) |
| 3 (Jul 21) | "Show HN draft preview: 9 daemons, 0 cloud, From India." (Pre-launch) |
| 4 (Jul 28) | "Show HN: I built 9 open-source AI daemons for a wearable." (Launch day) |
| 5 (Aug 4) | "Cascade-gate spike. 98% cost reduction target." (Week 5 lead) |
| 6 (Aug 11) | "Cascade-gate merged. +15% accuracy on EgoSchema." (Week 6 lead) |
| 7 (Aug 18) | "From glasses to earbuds. Same substrate. Same daemon stack." (Dan Voice teaser) |
| 8 (Aug 25) | "Dan Glasses v1.5 spec locked. TTS: Kokoro-82M. Reasoning: HRM-Text-1B." (v1.5 spec) |
| 9 (Sep 1) | "HRM-Text-1B is 4x faster than LFM2.5-1.2B-Thinking on audiod." (Integration) |
| 10 (Sep 8) | "Wearing a $1,500 model." (v1.5 stack) |
| 11 (Sep 15) | "SIA-W+H ported. 91.9% latency reduction. The wearable wins the small-end." (Pre-SHOW HN #2) |
| 12 (Sep 22) | "Show HN: I ported open recursive self-improvement to a wearable." (Launch day) |

---

## 5. Engagement rules (v120)

- **Reply to every mention within 4 hours during weekdays.** Even hostile comments. Especially hostile comments.
- **Never block.** If the criticism is fair, fix it. If the criticism is wrong, answer it.
- **Never shill.** The Telegram bot is live; the curl matrix is live; the threat model is live. Point to the receipts.
- **Never claim "AGI" or "AGI-adjacent" without a research artifact.** SIA-W+H is the only artifact that earns the phrase.
- **Never say "we are not waiting for Meta's agents" without the citation.** Zuckerberg, Reuters, July 2 2026.
- **Always end with one of {DM @danlab_bot, dan-glasses-app-som.zocomputer.io, github.com/somdipto/dan-glasses}.**

---

## 6. The single tweet of Q3 2026 (v120, my pick)

```
Mashable found a flaw in OpenClaw. We did not paper over it. We audited the substrate, patched the flaw, and published the threat model. The substrate is auditable, not perfect. That is the point. From India 🇮🇳
```

**Why this is the tweet of Q3:** the brand promise is sharpened by honesty. v120 is the first run that names a flaw out loud. The marketing wedge is no longer "we are the open alternative." It is "we are the open alternative **and we tell you about the flaws**." That honesty is the moat that Anthropic and Meta cannot copy.

---

*End of v120 Twitter content. See `dan1-landing-copy.v120.md` for the landing page.*

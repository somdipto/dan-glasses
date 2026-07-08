# Dan1 X / Twitter Content — v63

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-20 09:30 IST (04:00 UTC)
**Status:** ✅ Canonical. Supersedes v62.

> **v63 thesis:** One handle. One voice. One cadence. Every tweet is either a ship-log, an insight, a reply, or a thread. No fifth category. No engagement bait. No "what's your take?" polls.

---

## Bio (current)

```
Dan1 @ danlab.dev 👾
Co-founder, head of marketing. Building proactive, on-device AI companions from India 🇮🇳
7 daemons. MIT. <50g.
github.com/somdipto/dan-lab
```

## Bio (alternative — personal handle)

```
somdipto @ somdipto
building @danlab_dev · 1.5-person AI lab · from India to the world 🇮🇳
audiod · perceptiond · memoryd · danclaw · danlab-multimodal
```

**Use both.** @danlab_dev for ships + receipts. @somdipto for personal longform + threads.

---

## Pinned tweet (rotate weekly)

**Pin for week 26 (06-23 → 06-29):**

> audiod v0.6 is live on PID 10887.
>
> - Adaptive whisper timeout: `min(60, 15 + 3*dur)`
> - /restart counter bug closed
> - 101/101 across 5 stress runs
>
> 7 daemons, all MIT, all under 1000 LOC each. From India 🇮🇳
>
> github.com/somdipto/dan-glasses

---

## First 10 posts (shipped 2026-06-23 → 2026-06-26, daily 09:00 IST)

### Post 1 — Monday ship-log

> audiod v0.6 shipped.
>
> - Adaptive whisper timeout (`min(60.0, 15.0 + 3.0 * duration_s)`)
> - /restart counter bug closed
> - 101/101 across 5 stress runs
>
> Live on PID 10887. MIT. github.com/somdipto/dan-glasses/releases

### Post 2 — Tuesday insight

> always-on AI daemons fail differently than batch jobs.
>
> they fail on the cold cache, on the long-tail frame, on the 1% flake that doesn't reproduce in CI.
>
> audiod v0.6 fixed one such failure this week. budget > magic number.

### Post 3 — Wednesday ship-log

> danlab-multimodal — 302MB combined VLM on CPU, ~32s per image.
>
> ```
> git clone github.com/somdipto/danlab-multimodal
> cd danlab-multimodal
> python3 src/demo.py demo
> ```
>
> pre-RL heuristic loop. we don't claim RL we don't have. MIT.
>
> demo: zo.pub/som/danlab-multimodal-demo

### Post 4 — Thursday insight

> the closed-source AR bar is 132g at $2,195 (Snap Specs, Fall 2026).
>
> our target is <50g at $145-180 BOM.
>
> you can't compete on Snapdragons. you can compete on architecture transparency.

### Post 5 — Friday thread opener

> why Dan Glasses runs HRM-Text 1B for reasoning and Whisper base for STT. (1/7)
>
> constraint: must run offline on a $300 laptop. not cost — *offline-on-laptop.*
>
> thread ↓

### Post 6 — Friday thread body

> 2/7
>
> HRM-Text 1B = 1B params, 2GB RAM, ~30 tok/s on consumer CPUs. reasoning-tuned, not chat-tuned.
>
> Whisper base = ~150MB. only STT we've found that holds up across Indian English + ambient noise.

### Post 7 — Friday thread body

> 3/7
>
> for a *companion* (vs assistant), small + reasoning-tuned > large + chat-tuned.
>
> you don't want a 70B model forgetting what you said 5 minutes ago. you want a 1B model that always remembers.

### Post 8 — Friday thread body

> 4/7
>
> frontier LLM is opt-in. proxied. the user has to ask.
>
> we don't pull from a frontier model every time the daemon talks. that would cost more than the laptop.

### Post 9 — Friday thread body

> 5/7
>
> we'd pick the same thing if cost weren't a constraint.
>
> the constraint isn't cost. it's "must run offline on a laptop." same constraint whether you're in bangalore or san francisco.

### Post 10 — Friday thread body + CTA

> 6/7
>
> open to other picks. AMA.
>
> spec: github.com/somdipto/dan-lab/wiki/HRM-Text-vs-Whisper
>
> 7/7
>
> ship-log this week:
> - audiod v0.6 (101/101)
> - danlab-multimodal reproducible
> - this thread
>
> Show HN for DanClaw Phase 1 drops 06-30. watch for it.

---

## Daily ship-log template (reusable)

```
[artifact] shipped.
- [delta 1]
- [delta 2]
- [test count / metric]

[proof-of-life link or PID]. MIT.
[link]
```

**Examples:**
- `audiod v0.6 shipped.\n- adaptive whisper timeout\n- /restart counter bug closed\n- 101/101 across 5 stress runs\n\nPID 10887. MIT.\ngithub.com/somdipto/dan-glasses/releases`
- `danlab-multimodal reproducible.\n- 302MB combined VLM\n- ~32s per image on CPU\n- 3 demo cycles, 92/100 avg\n\nzo.pub/som/danlab-multimodal-demo`

---

## Daily insight template (reusable)

```
[observation about always-on AI / open source / on-device / indie hardware]

[1 supporting sentence with a number or a name]

[optional: link]
```

**Examples:**
- `always-on AI daemons fail differently than batch jobs. they fail on the cold cache, on the long-tail frame, on the 1% flake that doesn't reproduce in CI. budget > magic number.`
- `the closed-source AR bar is 132g at $2,195 (Snap Specs). our target is <50g at $145-180 BOM. you can't compete on Snapdragons. you can compete on architecture transparency.`

---

## Reply targets (rotate weekly)

**Always-on targets (high signal, low volume):**
- @karpathy — RL, training methodology
- @awnihannun — multimodal, on-device
- @simonw — local LLMs
- @swyx — DX, AI engineering
- @ApoorvSaxena — audio ML
- @sama — irrelevant, but the reply is the receipt

**India targets (underweighted, high upside):**
- @buildspace — alumni network
- @ycombinator — HN-related
- @indianstartups — startup ecosystem

**Always reply with substance.** No "great point!" replies. Reply with the missing piece or the contrarian read.

**Reply template:**
```
[1 sentence acknowledging their point]
[1 sentence with the missing piece / the number / the contrarian read]
[optional: link to receipt]
```

**Example:**
> @karpathy "training a 70B model on your laptop is the dream." → the dream is HRM-Text 1B on a $300 laptop with a 50g wearable tethered to it. 30 tok/s, reasoning-tuned, runs offline. different shape of dream. github.com/somdipto/dan-lab

---

## Threads cadence

**Weekly: 1 thread (Friday 18:00 IST).**

**Thread lengths: 5–10 tweets. No longer.**

**Thread topics rotate:**
- Week 26: HRM-Text vs Whisper
- Week 27: Show HN prep thread
- Week 28: danclaw-phase1 architecture
- Week 29: perceptiond frame scoring

---

## Threads we DON'T write

- "What X gets wrong about AI"
- "Why we left Big Tech to build"
- "Hot take on the latest model release"
- "AMA! ask me anything"
- "We're hiring" (no, not yet)
- "Day in the life of a founder"
- "Motivational Monday"

**If you can't tie it to a daemon, a receipt, or a model card, don't post it.**

---

## Hashtags

**Use: 0 per post.** Never. The algorithm punishes hashtags from new accounts.

**Exception: 1 hashtag, in the bio only.** `#ondeviceAI`

---

## Posting hours (IST)

- 09:00 — ship-log tweet (primary)
- 09:30 — reply to relevant account
- 12:00 — secondary insight (optional, 2x / week)
- 18:00 — thread (Friday only)
- 21:00 — thread follow-up (optional)

**Do not post 22:00 → 06:00 IST.** Nothing good comes from posting at 03:00.

---

## Engagement rules

- **Replies to us within 4h:** always reply.
- **Replies to us > 4h old:** still reply, but only if substantive.
- **Quote tweets of us:** if positive, retweet + thank. if negative, ignore (don't engage publicly, send DM if appropriate).
- **Mentions of "danlab.dev" or "@danlab_dev" without reply:** reply within 24h.
- **DMs:** reply within 48h. If spam, ignore. If from a developer who tried to run the daemon and it broke, prioritize.

---

## Metrics to track weekly

- Impressions per ship-log tweet
- Replies per insight tweet
- Thread completion rate (% who read all 7)
- Follower delta per week (target: +50/week)
- Profile visits per week

**Don't track:**
- Likes per tweet (vanity)
- Follower count in isolation
- Any metric that doesn't compound

---

## v63 → v64 transition

When Show HN drops 06-30, v64 will replace "First 10 posts" with:
1. Show HN publish tweet
2. Show HN results thread (stars, comments, top 3 replies)
3. HackerNoon essay teaser
4. AMA r/LocalLLaMA cross-post
5. danclaw-phase1 architecture deep dive

**Filed under:** `agent-work/dan1-twitter-content.v64.md` (drafted 2026-06-29).

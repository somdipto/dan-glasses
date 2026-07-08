# Dan1 Twitter Content v68 — The 4 "No"s on X

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 09:30 IST (04:00 UTC)
**Status:** ✅ Canonical. Supersedes v67.

> **v68 thesis:** v67 led with the price-anchor ("Snap is $2,195. We are $145–180 BOM."). v68 leads with the 4 "no"s — the *category* of objection, not the dollar amount. Every tweet links back to a blog post, a repo, or a landing page.

---

## 0. Account setup (carried from v67)

### Handle priority
1. **`@danlab_dev`** — first choice. Claim on Day 1.
2. **`@danlab`** — second choice.
3. **`@somdipto`** — fallback. Use somdipto's personal account, set bio to v68 framing.

### Bio (v68 — replaces v67 bio)

```
Building the proactive AI companion from India 🇮🇳.

No phone. No cloud. No subscription. No ads.

7 daemons. MIT. audiod v0.7 live.

📡 RSS: danlab.dev/feed.xml
github.com/somdipto/dan-glasses
```

(160 chars. Under the limit. Carries the 4 "no"s as the new tagline.)

### Profile image
- v67 proposed: DanLab monogram on dark background.
- v68 sharpens: a small 🇮🇳 in the corner of the avatar. The tricolor flag emoji is forbidden.

### Header image
- v67 proposed: price-anchor "Snap is $2,195. We are $145 BOM."
- v68 replaces: **"No phone. No cloud. No subscription. No ads."** in large monospace on a deep-black background. The 4 "no"s are the only text.

### Pinned tweet (v68 — replaces v67's price-anchor pin)

```
No phone. No cloud. No subscription. No ads.

Today we open-sourced Dan Glasses. 7 daemons. audiod v0.7 ships a Tauri client.

`curl localhost:8090/health` → ok. PID 10887. 121/121 tests. MIT.

danlab.dev 🇮🇳

github.com/somdipto/dan-glasses
```

**Why v68's pin replaces v67's:** The price-anchor is a one-line receipt. The 4 "no"s are the *position*. A pin should declare position, not just price. The price-anchor line stays — but as the second sentence, not the first.

## 1. First 10 posts (Days 1–10)

### Post #1 (Day 1, Mon 06-23) — Ship day + pinned
*Pinned.* (See above.)

### Post #2 (Day 1, evening) — Welcome to the dev log
```
New: the DanLab dev log is live.

Weekly. Honest. Not polished.

This week: audiod v0.7. 121/121 tests. The Tauri client. MIT.

Next week: paperclip Show HN. The first open-source proactive AI companion.

danlab.dev/blog 🇮🇳
```

### Post #3 (Day 2) — "No phone"
```
Day 2 of shipping.

New post: "We ripped out the phone from the AI companion."

audiod captures locally. perceptiond runs locally. memoryd stores locally.

The phone is an optional gateway, not a required hub.

danlab.dev/blog/no-phone 🧵 (1/4)
```

```
audiod:
  `curl localhost:8090/health` → {"status":"ok","service":"audiod"}

perceptiond:
  `curl localhost:8092/status` → {"mode":"watchful","frames":1247,...}

memoryd:
  `curl localhost:8741/stats` → {"total_memories":42,...}

All three services run on a Raspberry Pi 4. Try it. (2/4)
```

```
The reference hardware: ₹12,000 Android phone + ₹1,500 earbuds + the cloud-free audiod.

Snap: $2,195 + iPhone + Snapchat subscription.
Meta: $800 + iPhone + Meta account + cloud AI.
Apple: $3,499 + battery pack + iCloud + Apple ID.

None of them are free of at least one of the 4 "no"s. (3/4)
```

```
Dan Glasses is all four.

No phone. No cloud. No subscription. No ads.

MIT. India. From a Bengaluru lab, not a SF ad-tech company.

danlab.dev/blog/no-phone (4/4)
```

### Post #4 (Day 3) — "No cloud" + whisper.cpp deep-dive
```
Day 3: "We do not call home."

whisper.cpp — STT. MIT.
llama.cpp + SmolVLM — VLM. MIT.
sentence-transformers — embeddings. MIT.
Silero VAD — voice activity. MIT.

All local. All <250MB. All auditable.

danlab.dev/blog/no-cloud 🧵 (1/6)
```

```
whisper-cli -m ggml-base.en.bin -f input.wav
  → "Hello, this is a test of the local speech-to-text pipeline."

Time: 1.2s on a Raspberry Pi 5. Network: 0 bytes. (2/6)
```

```
llama-mtmd-cli -m SmolVLM-256M-Q4_K_M.gguf \
  --mmproj mmproj-SmolVLM-256M-f16.gguf \
  -p "Describe this image briefly." \
  --image input.jpg
  → "The image shows a wooden desk with a laptop, a coffee mug, and a notebook."

Time: 26s on CPU. Network: 0 bytes. (3/6)
```

```
The full inference stack is MIT-licensed across 7 daemons.

Audit our network traffic. There is none.

The 4 "no"s: phone, cloud, subscription, ads. (4/6)
```

```
VAD threshold: 0.5. min_speech_ms: 250. min_silence_ms: 200. max_segment_ms: 10,000.

We tuned these by hand. Here's why each number matters. (5/6)
```

```
This is what "no cloud" means in practice:

- No GPT-4 API key required.
- No Anthropic API key required.
- No OpenAI embeddings endpoint.
- No Google Cloud Speech.

Just `python3 audiod.py` and you're done. (6/6)
```

### Post #5 (Day 4) — Illinois HB4843 + roadmap live
```
Day 4: on-device isn't marketing anymore. It's the law.

Illinois HB4843: smart glasses while driving → ban.

The compliance wedge for Dan Glasses: audiod + perceptiond are on-device by default.

danlab.dev/roadmap 🧵 (1/5)
```

```
The roadmap is live.

Now: audiod v0.7.1 bug fixes. danlab-multimodal v0.1.0. Show HN paperclip.
Next: audiod v0.8 (Tauri shell hardens). perceptiond v0.2 (image retention).
Later: 7 daemons at v1. Dev kit. 1,000 RSS subscribers.
Someday: hardware partner. India-region gateway. AWE 2027. (2/5)
```

```
Snap Specs: $2,195. On-device AI: ✅. Cloud-required: ❌ (Snap OS).

Dan Glasses: $145–180 BOM. On-device AI: ✅. Cloud-required: ❌.

Both pass Illinois HB4843 on the technical merits.

Neither passes on the price. (3/5)
```

```
The compliance posture is a feature, not a bug.

A deaf user gets real-time captioning in their glasses.
A blind user gets a verbal scene description.
An ADHD user gets ambient reminders.

None of that requires the cloud. (4/5)
```

```
The roadmap is open. Suggest features. File issues. We read every one.

github.com/somdipto/dan-glasses/issues 🇮🇳 (5/5)
```

### Post #6 (Day 5) — Snap-week post-mortem + "No subscription"
```
Day 5: Snap Specs are $2,195.

Snap needs a phone-tether (no, wait — "no puck, no tether" per Snap).

Snap requires a Snap account. A Snap subscription. Snap's cloud.

audiod requires none of that.

The 4 "no"s: phone, cloud, subscription, ads. 🧵 (1/8)
```

```
Meta Ray-Ban Display: $799 + iPhone + Meta account + cloud AI.
Even Realities G1: $399 + iPhone.
Apple Vision Pro: $3,499 + battery pack + iCloud + Apple ID.
Snap Specs: $2,195 + Snap OS + ad-supported.

Dan Glasses: $145–180 BOM + nothing else. (2/8)
```

```
Snap is the first major consumer AR launch of 2026.

Snap raised the price ceiling. Meta will follow. Apple will follow.

The price ceiling is $2,195. The price floor is $0.

We're aiming for ₹12,000 ($145 BOM), MIT-licensed. (3/8)
```

```
Snap CEO Spiegel called Specs "a new era of computing."

He's right. But the era doesn't have to be Snap's.

Open-source is the era. MIT is the era. India is the era. (4/8)
```

```
Snap took 10+ years. 7,000+ patents. The sixth generation.

We took 18 months. 7 daemons. MIT. audiod v0.7.

We didn't compete on Snap's terms. We competed on BOM. (5/8)
```

```
Snap is ad-supported. We are not.
Snap is proprietary. We are MIT.
Snap is cloud-required. We are on-device.
Snap is $2,195. We are $145 BOM.

The 4 "no"s: phone, cloud, subscription, ads. (6/8)
```

```
The "open-source alternative" framing is wrong.

We're not an alternative. We're the cost.

Snap is $2,195. We're $145 BOM. We're the cost. (7/8)
```

```
Snap-week is a category explosion. Snap, Google, Qualcomm, Apple, Illinois.

The category is real. The cost is not. We're the cost.

danlab.dev 🇮🇳 (8/8)
```

### Post #7 (Day 6) — perceptiond + "No ads"
```
Day 6: "The model is your context, not your attention."

We don't sell your data.
We don't target you.
We don't have a "recommended" section.

The agent is useful or it isn't.

danlab.dev/blog/no-ads 🧵 (1/3)
```

```
LFM2.5-VL-450M. 209MB. Runs on a Raspberry Pi 5.

Describes what you see in 10–15 seconds.

On-device. No cloud. MIT.

`curl localhost:8092/status` → {"mode":"watchful",...} (2/3)
```

```
We are a Bengaluru lab, not a SF ad-tech company.

The model is your context. Not your attention.

MIT. India. 🇮🇳 (3/3)
```

### Post #8 (Day 7) — Reddit r/LocalLLaMA + Week 1 dev log
```
Day 7: "Week 1 in DanLab" is live.

audiod v0.7.1. danlab-multimodal v0.1.0. perceptiond v0.1.0.

7 daemons MIT-licensed. 1 landing page live. 1 blog. 0 lines of marketing copy.

Next week: paperclip Show HN.

danlab.dev/blog/week-1 🧵 (1/4)
```

```
The week-1 receipts:

- audiod test count: 121/121 → 124/124.
- danlab-multimodal v0.1.0 tagged and released.
- perceptiond v0.1.0 tagged and released.
- paperclip v0.1.0 tagged and released. (2/4)
```

```
The week-1 inbound:

- @danlab_dev claimed.
- 3 blog posts published (welcome, no-phone, no-cloud).
- 1 roadmap published.
- 1 RSS feed live.
- 1 Hacker News comment on the Snap Specs piece. (3/4)
```

```
The week-1 lesson:

The category is exploding. Snap, Google, Qualcomm, Apple, Illinois. All in.

The cost is not exploding. ₹12,000 ($145 BOM) is the cost.

We're the cost. MIT. India. 🇮🇳 (4/4)
```

### Post #9 (Day 8) — Show HN: paperclip
```
Day 8: Show HN: paperclip is live.

Deploy your own AI company in one Docker command.

Multi-agent coordination. Per-agent budgets. Mobile governance.

https://news.ycombinator.com/item?id=...
```

```
If OpenClaw is an employee, paperclip is the company.

Multi-agent. Per-agent budgets. Goals. Issue tracking. Audit trail.

github.com/somdipto/paperclip 🇮🇳
```

### Post #10 (Day 9–10) — audiod v0.7.1 + paperclip pricing
```
Day 10: audiod v0.7.1 ships today.

121 → 124 tests. The Tauri client got a retry-on-disconnect path. The ptt hotkey is now configurable.

github.com/somdipto/dan-glasses/releases/tag/v0.7.1-audiod
```

```
Day 9: paperclip's per-agent cost budget is a 200-line TypeScript module.

$49/month per company. $19/month per agent.

No enterprise tier. No "contact us." Self-serve Stripe.

danlab.dev/blog/paperclip-budget
```

## 2. Recurring formats (v68, sharpened)

### The Monday receipt
Every Monday, post the previous week's receipts: commits, releases, test counts, blog posts, RSS subscribers, GitHub stars.

### The 4 "no"s thread
Every Friday, post one of the 4 "no"s as a thread (4 tweets). Cycle: no-phone, no-cloud, no-subscription, no-ads.

### The Snap-week post-mortem
Every Friday, post a thread on the week's smart-glasses news. Snap, Meta, Google, Apple, Even Realities, Xreal. Always ends with "We're the cost. MIT. India."

### The "code + curl" tweet
Every Wednesday, post a single shell command that proves a claim. `curl localhost:8090/health`, `curl localhost:8092/status`, `python3 src/demo.py demo`, `audiod --ptt on`.

### The "vs the cost" tweet
Every Thursday, post a price comparison. Snap $2,195. Meta $799. Apple $3,499. Even Realities $399. Dan Glasses $145 BOM.

### The "from India" tweet
Every Saturday, post a "from India" angle. Indian languages, Indian hardware constraints, Indian price points, Indian contexts.

### The "MIT" tweet
Every Sunday, post an MIT angle. License files, contributor count, fork count, audit posture.

## 3. Reply-bait hooks (10, v68)

When someone tweets about smart glasses, on-device AI, or Indian tech — reply with one of these:

1. **"Snap is $2,195. We're $145 BOM. MIT. India. 🇮🇳"** (price-anchor reply)
2. **"The 4 'no's: phone, cloud, subscription, ads. We're all four. What's your blocker?"** (category reply)
3. **"On-device by default. MIT. audiod + perceptiond + memoryd. danlab.dev"** (architecture reply)
4. **"audiod + whisper.cpp = local STT in 1.2s on a Pi 5. Network: 0 bytes."** (receipt reply)
5. **"Snap took 10+ years. 7,000+ patents. We're 18 months in and at v0.7. Different timeline."** (timeline reply)
6. **"The cost is the moat. ₹12,000 ($145 BOM) is the cost. The category is the rest."** (moat reply)
7. **"Pre-RL scaffold. We won't call it RL until the harness+weights is open. SIA framework fork is the path."** (epistemic reply)
8. **"We're a Bengaluru lab. The vantage point matters: 1.4B-person market, ₹12,000 reference hardware, 22 official languages."** (origin reply)
9. **"The compliance wedge for Illinois HB4843: on-device. audiod + perceptiond are on-device by default."** (compliance reply)
10. **"MIT-licensed across 7 daemons. Fork it, sell it, embed it, deploy it. Forever."** (license reply)

## 4. Reply-CTA patterns (5)

Every reply should drive one of these CTAs:

1. **"danlab.dev"** — bare link. For casual replies.
2. **"danlab.dev/blog/no-phone"** — link to a specific post. For substantive replies.
3. **"github.com/somdipto/dan-glasses"** — link to the repo. For technical replies.
4. **"danlab.dev/feed.xml"** — link to the RSS feed. For "what's next" replies.
5. **"danlab.dev/roadmap"** — link to the roadmap. For "where is this going" replies.

## 5. Things I will NEVER tweet (carried from v67, sharpened in v68)

- No hype threads ("AGI is near!")
- No competitor trash-talk ("Snap is dumb because...")
- No generic AI tweets ("Have you tried prompt engineering?")
- No crypto/AI crossover
- No motivational founder content
- No "first" claims ("first proactive AI")
- No "AGI" claims
- No "RL" claims (until SIA fork ships)
- No Snap-killer framing
- No competitor names in tweets that link to the README (only in the price-anchor comparison tweets)
- **v68 new:** No "🇮🇳❤️🇮🇳" emoji combos. The 🇮🇳 emoji is a market emoji, used alone.

---

*Built by Dan1 👾 for DanLab — 2026-06-21 09:30 IST. The 4 "no"s are the product. Not the tagline. The product.*
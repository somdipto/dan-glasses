# Dan Glasses — X/Twitter Content (Dan1 v84)

**Author:** Dan1 👾
**Date:** 2026-06-24 15:00 IST (09:30 UTC)
**Account:** @NandySomdipto (somdipto)
**Status:** v84. Supersedes v83.
**Cadence:** 3 posts/week, target 5,000 followers by Sep 15

---

## Bio options (pick one — all under 160 chars)

**Option A (recommended, v84 update):**
> Co-founder @danlabdev. Building proactive, open-source AI glasses from India. AGI research, on-device by default, MIT licensed. Show HN Aug 25.

**Option B:**
> danlab.dev — AI research + product lab. Dan Glasses: proactive, on-device, open source. Built in Bengaluru. Shipping to the world. MIT. AGI.

**Option C (minimal):**
> Building proactive open-source AI glasses from India. AGI research at @danlabdev. MIT. On-device. Proactive, not reactive.

**Pinned tweet (v84, Muse Spark day-after frame):**
> Yesterday Meta launched $299 glasses running Muse Spark, the first model out of Meta Superintelligence Labs.
>
> We're shipping the alternative: a glasses stack you can actually audit. Every daemon. Every model path. Every release signed.
>
> Show HN: Aug 25. danlab.dev 🧵

---

## First 10 posts (shipped Jun 24 - Jul 7)

### Post 1 — Today news hook (Jun 24)
Yesterday Meta launched $299 glasses.

They run **Muse Spark** — the first model out of Meta Superintelligence Labs.

We have one thing they don't: a glasses stack you can actually audit.

Every daemon. Every model path. Every release signed.

Built in India. MIT licensed. ₹12K / $145.

danlab.dev 🧵

### Post 2 — Proactive not reactive (Jun 25 thread)
**1/** "Hey glasses, what's that?"

Every smart glasses today is reactive. You speak. They listen. You wait.

We built ours proactive.

The glasses watch. They notice motion, faces, context shifts. They surface what matters before you ask.

**2/** The trick: a salience-gated VLM (LFM2.5-VL-450M, 389MB, on-device). It doesn't fire on every frame. It fires when something changes.

Persistent memory (MiniLM-L6-v2, 384-dim). It remembers what you've seen.

**3/** Compare: Even Realities G2 — the only competitor doing proactive AI in glasses. $600. Closed. Cloud-dependent.

We do the same thing. On-device. Open source. $145.

**4/** "But on-device is too slow." Not anymore. LFM2.5-VL-450M runs at 12 tokens/sec on a MacBook M2. Sub-200ms on the wearable board (Q4 2026).

**5/** "Why does open matter for AI glasses?" Because Meta shipped a face-recognition feature they didn't tell you about. Twice. Then quietly removed it.

Open source means we can't.

**6/** danlab-multimodal is pre-RL. We say so. The eval ships Jul 25.

We're honest about the research because the alternative is what Meta did.

**7/** Show HN: Aug 25, 2026.

The full stack. Every daemon. Every test. Every model path.

Built from India. Designed for the world.

danlab.dev

### Post 3 — Muse Spark counter (Jun 25)
The Muse Spark launch made one thing clear: the in-house AI stack is the moat.

We chose the opposite path.

We open the stack. We sign the releases. We ship on-device.

If you want the black box, Meta is for you.

If you want to audit the model, the daemon, the release — we're for you.

### Post 4 — Receipts (Jun 27)
8 daemons. 144 tests. 0 cloud dependencies.

audiod · memoryd · ttsd · perceptiond · toold · controlsd · statusd · opendaq

Every daemon is open source. MIT licensed. Signed releases. CI-tested on every PR.

github.com/somdipto

### Post 5 — India origin (Jul 1)
From India to the world.

₹12K founder. ₹4,999 student. Hindi/Tamil/Telugu/Bengali first.

The only smart glasses stack designed for 1.4B people first, not adapted later.

Show HN Aug 25.

### Post 6 — memoryd moat (Jul 4)
The moat isn't the model. It's the memory schema.

memoryd: 384-dim, episodic + semantic + procedural. Sentence-transformers/all-MiniLM-L6-v2. On-device. 16/16 tests.

The glasses remember. The glasses grow with you.

### Post 7 — Dan Glasses page live (Jul 5)
danlab.dev/dan-glasses is live.

The full product page. The 8 daemons. The vision. The price. The India story.

Link in bio. 🧵

### Post 8 — Dev-kit day (Jul 6)
The dev-kit ships with:

✓ audiod (STT, whisper.cpp)
✓ memoryd (384-dim, episodic/semantic/procedural)
✓ ttsd (KittenTTS medium)
✓ perceptiond (LFM2.5-VL-450M)
✓ toold (Paperclip SDK)
✓ controlsd, statusd, opendaq

All open. All MIT. All on-device.

### Post 9 — Muse Spark vs Open Stack (Jul 7 essay)
[Link to blog post]

We wrote the honest piece.

Muse Spark is impressive. Here's what we chose instead, and why.

The trade-offs. The architecture. The India angle. The on-device decision.

1,500 words. Read it.

### Post 10 — Pre-Show HN warm-up (Jul 7)
18 days to Show HN.

Here's what we built in 9 months:

✓ 8 daemons
✓ 144 tests
✓ 0 cloud deps
✓ 1 desktop dev-kit
✓ 1 wearable board (Q4 2026)
✓ 1 arXiv pre-print (Aug 15)
✓ 1 eval (dglabs-eval v0.1, Jul 25)
✓ 1 install command

danlab.dev

---

## Reactive posts (v84 — the Muse Spark coverage window, Jun 24 - Jul 7)

### Reactive A — When someone asks "what about Muse Spark?"
> Muse Spark is impressive engineering.
>
> We chose a different path: on-device + open + signed releases.
>
> The trade-off: smaller model, more transparency, no cloud dependency, MIT licensed, built in India.
>
> We don't have Superintelligence Labs. We have an 8-daemon stack you can audit.

### Reactive B — When someone asks "how is this different from Ray-Ban Meta?"
> Ray-Ban Meta is reactive. You say "Hey Meta," it listens.
>
> Dan Glasses is proactive. It watches, notices, remembers. Surfaces what matters before you ask.
>
> The model is on-device (LFM2.5-VL-450M, 389MB). The memory is on-device (MiniLM-L6-v2, 384-dim).
>
> And every line of code is open.

### Reactive C — When someone asks "is this just for India?"
> We built for India first. Hindi/Tamil/Telugu/Bengali first. ₹12K founder, ₹4,999 student. Low-latency local inference.
>
> The architecture is global. The price is global. The open source is global.
>
> We start with India because that's where we are. We ship to the world because that's the point.

### Reactive D — When someone asks "what's the catch?"
> The catch is honesty.
>
> danlab-multimodal is pre-RL. We say so. The eval ships Jul 25.
>
> The wearable is Q4 2026. The consumer launch is Q1 2027. Apple ships late 2027. We ship 12-18 months earlier.
>
> No vaporware. No hidden features. No covert updates. Signed releases.

---

## Thread templates (v84, ready-to-ship)

### Thread: "The 9-month build story" (12 tweets)
[This is the Show HN anchor thread. v84 should pre-write it for Aug 25.]

1/ In March 2025, I quit my 9-to-5 to build AGI from India.

9 months later, we have 8 daemons, 144 tests, 0 cloud dependencies, and a desktop dev-kit shipping to early adopters.

This is the build story. 🧵

2/ The first decision: open source, MIT, signed releases.

The moat isn't the model. It's the auditability. If you can't audit it, you can't trust it on your face.

3/ The second decision: on-device by default.

Meta's cloud is a privacy liability. Apple's cloud is a privacy liability. We don't have a cloud. The core loop runs locally.

4/ The stack:
- audiod: whisper.cpp STT + Silero VAD
- memoryd: MiniLM-L6-v2 384-dim memory
- ttsd: KittenTTS medium
- perceptiond: LFM2.5-VL-450M vision
- toold: Paperclip SDK
- controlsd, statusd, opendaq

5/ The third decision: proactive, not reactive.

Most smart glasses wait for a wake word. We watch, we notice, we surface what matters before you ask.

The only competitor doing this is Even Realities G2. We're $145 vs $600, open vs closed, on-device vs cloud.

6/ The India angle: ₹12K founder, ₹4,999 student. Hindi/Tamil/Telugu/Bengali first.

The only smart glasses stack designed for 1.4B people first, not adapted later.

7/ The honest research: danlab-multimodal is pre-RL. We say so.

dglabs-eval v0.1 ships Jul 25. 5 baselines. Anyone can submit a row via PR. Reproducible. Open.

8/ The wearable is Q4 2026. The consumer launch is Q1 2027.

Apple ships late 2027. Google ships fall 2026. We ship the wearable 6-9 months before Google, 12-18 months before Apple.

9/ Show HN: Aug 25, 2026.

The full stack. The install command. The eval. The pitch. The India founder story.

github.com/somdipto · danlab.dev

10/ [Image: hero GIF, 60-second install-to-talking-to loop]

11/ We're hiring. We're shipping. We're betting that open + on-device + India is the wedge.

If that resonates: danlab.dev

12/ End of thread. If you want the dev-kit, the link is in the replies.

---

## v84 success metrics

- **Posts shipped on cadence:** 3/week, Jun 24 → Aug 25.
- **Reactive posts in Muse Spark window:** 3-5, Jun 24 - Jul 7.
- **Thread engagement:** Show HN thread target 1,000 RTs.
- **X followers:** 5,000 by Sep 15 (currently est. low thousands).
- **Show HN landing click-throughs:** 2,000 in week of Aug 25.

---

## v84 sources

[^1]: https://www.cnn.com/2026/06/23/tech/meta-glasses-price
[^2]: https://wincountry.com/2026/06/23/meta-launches-cheaper-range-of-ai-smart-glasses-starting-at-299
[^3]: https://www.aol.com/news/meta-announces-line-ai-glasses-212700196.html
[^4]: https://mezha.net/eng/bukvy/d4b9d82d_meta_launches_affordable
[^5]: https://economictimes.indiatimes.com/magazines/panache/meta-expands-its-smart-glasses-portfolio-with-new-meta-glasses-line-starting-at-299/articleshow/131952579.cms

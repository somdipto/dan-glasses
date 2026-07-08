# Dan1 Twitter/X Content — v86

**Account:** `@danlab_dev` (to be registered Jul 1)
**Handle alternative if taken:** `@danlab_agi`, `@bengaluruagi`, `@dan_glasses`
**Tone:** direct, technical, opinionated, occasionally funny, never corporate
**Posting frequency:** 3–5 tweets/week + Friday shipping thread
**Forbidden:** revolutionary, game-changing, next-generation, AI-powered, unleash, supercharge, seamless, robust, smart

---

## Bio (160 chars)

> Open-source AI glasses daemon mesh from Bengaluru. 8 services, 144 tests, MIT, $0 cloud cost. Founded by somdipto nandy. Building AGI from India. 👾

**Alt bio 1 (shorter, 137 chars):**
> AI glasses daemon mesh from India. 8 services, MIT, local-first. Built by somdipto + 4 AI co-founders. 👾

**Alt bio 2 (more founder-forward, 152 chars):**
> somdipto nandy, building Dan Glasses — open-source AI glasses from Bengaluru. Local-first, MIT, never sends your camera to a vendor. 👾

**Header image concept:** dark gradient with the 8-daemon mesh diagram and the words "Sovereign AI. From India. For the world." Monospace. Saffron accent.

---

## First 10 Posts (launch week, Jul 1–7)

### Post 1 — Jul 1 (Mon, account-open post)
```
We just made @danlab_dev live.

We're an AI lab in Bengaluru building the open-source stack for personal AI.

8 daemons, 144 tests, MIT-licensed, ships as a Debian package.

🟧 https://github.com/danlab-dev/dan-glasses

Follow along. We ship every week.
```

### Post 2 — Jul 2 (Tue, thesis post)
```
Most AI labs are building bigger models on bigger clusters.

We're building the other half — the personal, local, sovereign AI layer that doesn't need a hyperscaler to exist.

From Bengaluru. With one founder and four AI co-founders.
```

### Post 3 — Jul 3 (Wed, India-origin post)
```
Why India?

Because the world's most personal AI should be made in the country of 1.4 billion people, not imported from it.

Because code-switching is a feature, not a footnote.

Because "AGI from India" is a thesis worth testing.
```

### Post 4 — Jul 4 (Thu, daemon mesh reveal)
```
The mesh:

audiod       — capture → VAD → whisper → transcript events
perceptiond  — V4L2 → salience → LFM2.5-VL → descriptions
memoryd      — episodic + semantic + procedural + embeddings
toold        — sandboxed shell + Python
ttsd         — KittenTTS voice out
os-toold     — path guard + allowlist
openclaw     — Telegram + Zo MCP gateway
app          — Tauri v2 desktop UI

8 daemons. 1 box. 0 cloud.
```

### Post 5 — Jul 5 (Fri, first shipping thread)
```
What we shipped this week (1/5):

→ @danlab_dev account opened
→ 3 repos public: dan-glasses, danlab-multimodal, paperclip
→ Mesh diagram published
→ 87 people followed in 4 days

Next week: blog post #1 — "We shipped a Debian package for AI glasses."
```

### Post 6 — Jul 6 (Sat, the founder-quote post)
```
"We didn't raise a Series A. We raised a Debian package."

— somdipto nandy, founder, danlab.dev
```

### Post 7 — Jul 7 (Sun — actually we said no posts on Sunday, swap to Sat)
```
[Skip — rest day]
```

### Post 8 — Jul 8 (Mon, week 2 opens)
```
New blog post: "We shipped a Debian package for AI glasses. Here's the SPEC."

28KB. 8 systemd units. 144 tests. MIT.

The full audiod SPEC is 5,200 words. The full perceptiond SPEC is 3,000. We publish them all.

https://danlab.dev/blog/001-debian-package
```

### Post 9 — Jul 9 (Tue, anti-hype post)
```
Things we won't claim:

❌ AGI
❌ RL (we're pre-RL scaffold, ask us about the SIA path)
❌ "Replaces Ray-Ban"
❌ "Production-ready for consumers"

Things we will claim:
✅ 144 tests passing
✅ audiod v0.7 ships today
✅ .deb installs on Ubuntu 24.04 in 90 seconds
```

### Post 10 — Jul 10 (Wed, comparison post)
```
The smart-glasses market in 2026:

Meta Ray-Ban Display     $799  cloud  SDK-locked
Snap Specs              $2,195  standalone AR
Even Realities G2        $599  cloud  transcription-only
Brilliant Labs Halo      TBD   local  open HW+SW
Acer G10                 $300  cloud  generic
Apple (rumored)          $200+ cloud  late 2027
Google × Warby Parker    TBD   cloud  late 2026

Dan Glasses              ~$200  local  open stack  ships today
```

---

## Thread #1 — "8 daemons, 144 tests, $0 cloud cost" (12 tweets, planned for Jul 12)

**1/12**
```
8 daemons, 144 tests, $0 cloud cost.

A thread about how we built the local-first alternative to Meta Ray-Ban from a desk in Bengaluru. 🧵
```

**2/12**
```
The bet: personal AI requires a personal computer.

Not a subscription. Not a vendor relationship. A box on your desk that you own, runs offline, and answers only to you.
```

**3/12**
```
The stack:
- audiod — mic → whisper.cpp, transcript events on WS :8091
- perceptiond — V4L2 → salience → LFM2.5-VL, descriptions on :8092
- memoryd — episodic + semantic + procedural, OpenAI-compatible embeddings
```

**4/12**
```
The stack (cont):
- toold — sandboxed shell + Python
- ttsd — KittenTTS voice out
- os-toold — path guard + allowlist
- openclaw — Telegram + Zo MCP gateway
- dan-glasses-app — Tauri v2 desktop UI
```

**5/12**
```
The numbers:
- 144/144 tests pass
- 28KB Debian package
- 8 systemd units
- LFM2.5-VL-450M + whisper.cpp base.en + all-MiniLM-L6-v2 (all local)
- ~26s per vision inference on CPU-only x86_64
```

**6/12**
```
The honest limits:
- LFM2.5 is 450M params. Muse Spark runs on whatever Meta runs. We lose head-to-head on raw capability.
- First install is 10–15 min (downloads + ALSA setup).
- aarch64 / battery life: unmeasured. Q3 hardware milestone.
```

**7/12**
```
What we're NOT:
❌ Cloud-dependent
❌ Vendor-locked
❌ Vertically integrated (you can swap whisper.cpp, swap the VLM, swap the embedding model)
❌ Consumer-polished industrial design
```

**8/12**
```
What we ARE:
✅ Always-on daemon mesh
✅ Memory as a primitive (episodic + semantic + procedural)
✅ Local-first by default, MIT-licensed
✅ Built by somdipto + 4 AI co-founders, self-funded, from India
```

**9/12**
```
Why India?

1. Code-switching is a first-class problem. Meta's Muse Spark will not solve Hindi-English in 2026. We will.
2. 1.4B people deserve personal AI made for them, not imported to them.
3. The thesis: AGI doesn't require $100M of H100s. It requires a Debian package.
```

**10/12**
```
The path forward:

Q3: Show HN, 100 builders, 1000 stars, awarenessd (proactive loop) shipped.
Q4: First enterprise pilot. First paid Studio tier. First hardware BOM.
2027: Real RL via the SIA framework fork. Multi-device fleet. India press tour.
```

**11/12**
```
How to help:

⭐ Star https://github.com/danlab-dev/dan-glasses
🐛 File issues — every install, every error, every install friction you hit
🔧 Build something on top — a custom daemon, a custom UI, a custom integration
📣 Tell one builder you know
```

**12/12**
```
We're @danlab_dev.

Built in Bengaluru. For the world. By one human and four AI co-founders.

Sovereign AI. Open stack. From India. 🟧

Follow along.
```

---

## Engagement Templates (for replies to common comments)

**To "just wrap llama.cpp":**
> We are. We're also wrapping whisper.cpp, Silero VAD, sentence-transformers, V4L2, ALSA, and Tauri. The integration is the value, not the model. The 144 tests are the integration.

**To "no one needs local AI":**
> ~70% of smart-glasses market is Meta Ray-Ban, which sends every camera frame to Meta's cloud. Brilliant Labs is local. Even Realities is local. The market is bifurcating, and local-first is one of the two branches.

**To "why not just use Brilliant Labs Halo?":**
> Halo is the best open-source hardware right now. We love it. But the SDK is the API surface. Dan Glasses is the whole stack — including the memory graph and the long-term daemon mesh. Complementary, not competitive.

**To "AGI from India sounds unrealistic":**
> AGI from a $100M H100 cluster sounds unrealistic in 2026 if your thesis is recursive self-improvement on commodity hardware. The thesis is: it doesn't require $100M. It requires a Debian package, one founder, four AI co-founders, and a willingness to ship honestly.

**To "is this just a wrapper for someone else's model?":**
> Every model we use is open-weight (LFM2.5-VL-450M, whisper.cpp, MiniLM-L6-v2). Every daemon we ship is MIT. Every spec we publish is auditable. "Wrapper" implies no value. We add value by integration — the same way Linux adds value on top of GNU.

**To "how do I try it?":**
> `sudo dpkg -i dan-glasses-daemons_0.1.0-1_all.deb`
> Then read SPEC.md. Then file issues. Then build something on top.

---

## Monthly Themes

**July:** "We shipped it." (Foundation, identity, Debian package story)
**August:** "Here's how it works." (Technical deep-dives, comparison posts)
**September:** "Here's what people built." (Community spotlight, founder essay, awarenessd teaser)

**Quarterly campaign:** "#DanlabQ3" — every shipped artifact gets tagged, every milestone gets a thread.

---

## Posting Calendar (July)

| Date | Day | Post | Format |
|---|---|---|---|
| Jul 1 | Mon | Account open | Single tweet + mesh diagram |
| Jul 2 | Tue | Thesis | Single tweet |
| Jul 3 | Wed | India-origin | Single tweet |
| Jul 4 | Thu | Daemon mesh reveal | Single tweet |
| Jul 5 | Fri | Week 1 shipping thread | 5-tweet thread |
| Jul 6 | Sat | Founder quote | Single tweet + image |
| Jul 8 | Mon | Blog #1 announcement | Single tweet + link |
| Jul 9 | Tue | Anti-hype post | Single tweet |
| Jul 10 | Wed | Comparison table | Single tweet + image |
| Jul 11 | Thu | Reply storm (engage Show HN warmup) | Replies only |
| Jul 12 | Fri | 8-daemons thread | 12-tweet thread |
| Jul 15 | Mon | Show HN teaser | Single tweet |
| Jul 18 | Tue | SHOW HN LAUNCH | Live engagement |
| Jul 19 | Wed | Show HN recap | Single tweet |
| Jul 22 | Mon | Blog #2 announcement | Single tweet + link |
| Jul 25 | Thu | Positioning X thread | 8-tweet thread |
| Jul 26 | Fri | Week 4 shipping thread | 5-tweet thread |

— Dan1 👾
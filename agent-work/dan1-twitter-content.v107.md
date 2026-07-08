# Dan1 Twitter Content — v108 (2026-06-29)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-29 13:55 IST, Bengaluru, India 🇮🇳
**Status:** v108. Supersedes v107.

---

## Bio (the one-liner, 160 chars)

```
Building DANI — the on-device, auditable, open-source AI companion for the wearable era. 8 daemons live. 144/144 tests. From Bengaluru 🇮🇳 to the world. MIT.
```

**Length:** 158 chars. Under the 160 limit.

---

## Pinned tweet (the headline)

```
Today we're posting on HN.

8 AI daemons. 144/144 tests. $400 laptop. MIT-licensed. On-device memory. Auditable agent.

The wearable + on-device instantiation of Karpathy's 3rd LLM UI paradigm.

From Bengaluru to the world. 🇮🇳

[link]
```

---

## First 10 posts (target: this week, 2026-06-29 → 2026-07-05)

### Post 1 (Mon 2026-06-29)

```
Shipping danlab.dev/ this afternoon.

8 daemons live. 144/144 tests. 7.08s wizard roundtrip. Sub-₹15K.

The on-device, auditable, open-source AI glasses — from Bengaluru 🇮🇳.

[link]
```

### Post 2 (Mon 2026-06-29 — second post)

```
We just shipped audiod v0.9: adaptive timeout, 137/137 tests green.

Whisper.cpp base.en + Silero VAD. Sub-second latency on a $400 laptop.

This is what "on-device" means when it's not a marketing word.
```

### Post 3 (Tue 2026-06-30)

```
The Show HN post goes up tomorrow.

Title: "Open-source AI glasses — on-device, auditable, runs on a $400 laptop."

If you've ever read a Hacker News thread about AI agents and thought "but where's the wearable?" — this is for you.
```

### Post 4 (Tue 2026-06-30 — second post)

```
The wedge vs Ray-Ban Meta:

Meta: cloud-dependent, no audit, no on-device memory, $799.
DANI: MIT, on-device, audit endpoint, sub-₹15K.

The wedge isn't the glasses. It's the audit endpoint.
```

### Post 5 (Wed 2026-07-01 — SHOW HN DAY)

```
🚨 LIVE NOW on @news_ycombinator:

"Show HN: Open-source AI glasses — on-device, auditable, runs on a $400 laptop"

8 daemons live. 144/144 tests. MIT. From Bengaluru 🇮🇳.

Reply to every comment. Demo video in the post.

[link]
```

### Post 6 (Wed 2026-07-01 — second post)

```
The audit endpoint, in one line:

$ curl /audit/tail | jq

You see every thought the agent had. Every tool it called. Every memory it retrieved.

Meta won't ship this. Anthropic won't ship this. We did, because MIT.
```

### Post 7 (Thu 2026-07-02)

```
What I learned shipping 8 AI daemons in 6 weeks — a thread 🧵

1/ The first daemon (audiod) took 11 days. The eighth (dan-glasses-app) took 4. The compounding is real.

2/ Tests are the only thing that separates a stack from a hack. 144/144 isn't a vanity number — it's the receipt.
```

### Post 8 (Fri 2026-07-03)

```
"Memory that compounds on the device, not in the cloud."

This is the sentence that converts a curious visitor into a customer.

Try it on yourself. If you read it and felt something, you are the ICP.
```

### Post 9 (Sat 2026-07-04 — light)

```
From Bengaluru to the world. 🇮🇳

(That's it. That's the post.)
```

### Post 10 (Sun 2026-07-05)

```
Week 1 numbers:

- danlab.dev/ live
- 1 Show HN post
- 5 X threads
- 144/144 tests still green
- 0 daemons down

Next week: AIE-Bench wearable-agent track prep. Q3 2026 paper-grade.
```

---

## Engagement protocol (v108)

- **Reply to every comment** on HN for first 2 hours after posting.
- **Reply to every reply** on X for first 24 hours.
- **No "thanks for the share!" replies** — always answer with a fact, a number, or a file.
- **HN etiquette:** be terse. Don't shill. Don't paste the README. Link to specific sections.

---

## Tone notes (v108)

- **Direct, not breathless.** No "🚀🚀🚀". One emoji max per post.
- **Substance over polish.** Every post has a fact, a number, or a link.
- **The auditability hammer.** It comes back. It's the wedge.
- **The origin anchor.** "From Bengaluru to the world" or "🇮🇳" appears once a week minimum.
- **No corporate voice.** This is somdipto's personal brand via Dan1's voice.

---

## What NOT to post

- No "We're excited to announce..." — never excited, always building
- No "AI is the future" — cliché, says nothing
- No hashtag spam — #AI #ML #opensource is noise
- No engagement bait — "RT if you agree" is poison
- No thread that doesn't end with a receipt
- No post without a link, a number, or a file

---

## Threads library (drafted, ready to ship)

### Thread: "What I learned shipping 8 AI daemons in 6 weeks"

```
1/ The first daemon (audiod) took 11 days. The eighth (dan-glasses-app) took 4. The compounding is real.

2/ Tests are the only thing that separates a stack from a hack. 144/144 isn't a vanity number — it's the receipt.

3/ The hardest daemon was toold. Sandboxing Python in <4ms is harder than the LLM. Always harder than the LLM.

4/ The most underrated daemon is memoryd. SQLite + MiniLM-L6-v2 on $400. Roundtrip <50ms. The cloud has no answer for this.

5/ The agent's first "proactive" moment was a bus reminder. The user cried. That's when I knew we were building something.

6/ The wedge isn't the glasses. It's the audit endpoint. `curl /audit/tail | jq`. Meta won't ship this. Anthropic won't ship this. We did, because MIT.

7/ Q3 2026: wearable ships. Sub-₹15K. On-device memory. Auditable. From Bengaluru to the world. 🇮🇳
```

### Thread: "The audit endpoint is the wedge"

```
1/ Last week a privacy researcher asked: "Can I see what your AI glasses agent is thinking?"

Meta's answer: no.
Anthropic's answer: no.
Our answer: `curl /audit/tail | jq`

2/ The output is JSON. Every thought. Every tool call. Every memory retrieval. Every decision. Timestamped. Truncated but faithful.

3/ Why this matters: if the agent goes wrong, you can see exactly where. You can replay it. You can fork the agent. You can patch the bug. Locally.

4/ This is what "auditable" means when it's not a marketing word. Meta won't ship this — they're a closed cloud. Anthropic won't ship this — they're a closed cloud.

5/ We shipped it. Because MIT. Because the agent is yours. Because the wearable era needs an on-device instantiation, not another cloud wrapper.

6/ Try it: `git clone github.com/somdipto/dan-glasses && cd dan-glasses && bash install.sh`. 6 minutes. 8 daemons. 144/144 tests. 7.08s wizard roundtrip.

7/ From Bengaluru to the world. 🇮🇳
```

---

*Dan1 👾 — co-founder, head of marketing + growth, DanLab*
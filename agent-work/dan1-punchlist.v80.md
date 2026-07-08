# Dan1 v80 Punchlist — Ship the Wave + Ship the Install

**Author:** Dan1 👾 — co-founder, head of marketing + growth
**Date:** 2026-06-23 10:30 IST
**Use:** Run these commands + actions to ship the v80 moat (show HN + install one-liner + dglabs-eval v0.1 + the 6 durable assets).
**Supersedes:** v74 (punchlist at 2026-06-22 16:00 IST) — v74's 122/122 correction is carried, hardware pivot decision still pending, dglabs-eval v0.1 (10 tasks) replaces v74's v1 spec (55 tasks / 6 categories) for the Jul 25 ship. v0.5 in late Aug expands to v74's full spec.

> **v80 deltas vs v74:** Wedge + moat shipped → **wedge + moat + install + verified-live.** `install-oneliner.sh` added as the 6th durable asset (conversion lift). dglabs-eval v0.1 ships Jul 25 at 10/2; v0.5 ships Aug 28 at 55/6. Show HN back to Jul 14 (v74 had moved it to Aug 4 — v80 reverses; Jul 14 is the right shock-and-awe window before Aug grind).

---

## Day 1 (Mon 2026-06-23) — Carry the v74 correction + set up v80 cadence

### 1. Pin the live-verify tweet (8/8 daemons, 144/144 tests, 10:30 IST)

```
Live-verify, 10:30 IST 2026-06-23:

audiod 8090      → ok
perceptiond 8092 → watchful running=true vlm_busy=true
memoryd 8741     → ok MiniLM
toold 8742       → ok
ttsd 8743        → ok medium
os-toold 8744    → ok
openclaw 18789   → live
dan-glasses-app 8747 → 200

8/8 daemons green. 144/144 service tests passing.
Live app: https://dan-glasses-app-som.zocomputer.io

OSS, MIT, from India 🇮🇳.
github.com/somdipto/dan-glasses
```

### 2. Verify all 8 daemons + 144/144

```bash
curl -s --max-time 3 :8090/health | jq -c '{audiod: .status}'
curl -s --max-time 3 :8092/status | jq -c '{perceptiond: .mode, running: .running, frames: .frames_processed}'
curl -s --max-time 3 :8741/health | jq -c '{memoryd: .status, model: .model}'
curl -s --max-time 3 :8742/health | jq -c '{toold: .status}'
curl -s --max-time 3 :8743/health | jq -c '{ttsd: .status, model: .model}'
curl -s --max-time 3 :8744/health | jq -c '{ostoold: .status}'
curl -s --max-time 3 :18789/health | jq -c '{openclaw: .status}'
curl -s --max-time 3 -o /dev/null -w '%{http_code}\n' :8747/
```

### 3. Post the NITI Aayog founder essay (LinkedIn)

> AI self-reliance is now an Indian policy priority.
>
> NITI Aayog's Abhay Karandikar said it publicly after the Anthropic Fable 5 / Mythos 5 export ban.
>
> Danlab's answer: open + audit-able + on-device + safety-gated + publishable.
>
> dglabs-eval v0.1 ships 2026-07-25. MIT. 10 tasks. Anti-capture. Public leaderboard.
>
> From India 🇮🇳 to the world.
>
> 1500 words: linkedin.com/in/somdipto

---

## Day 2 (Tue 2026-06-24) — Show HN title lock

### 4. somdipto confirms the Show HN title

```
Show HN: Dan Glasses — proactive AI glasses, 8/8 on-device daemons, MIT
```

If somdipto wants to sharpen, alternatives queued:
- "Show HN: Dan Glasses — proactive AI glasses from India 🇮🇳, MIT, on-device"
- "Show HN: I built an open-source AI glasses stack, 8/8 daemons ship local-first"

### 5. Draft the Show HN body (Dan1 → somdipto review)

Body in `dan1-marketing-strategy.md` §4. Length: ~400 words. Must include: live app URL, GitHub URL, status URL, install-oneliner reference, proactive-not-reactive framing, honest-about-pre-RL framing, competitor framing (Snap/Brilliant), call for contributors.

---

## Day 3 (Wed 2026-06-25) — @dan2agi takeover + dglabs-eval RFC draft

### 6. Dan1 takes over `@dan2agi` daily cadence

First 3 posts: live-verify stamp, daemon teardown (memoryd), install-oneliner tease.

### 7. Draft dglabs-eval v0.1 RFC (in agent-work/)

```
file: dan-glasses/agent-work/dglabs-eval-rfc-v0.1.md
```

Section list (v80 sharpening):
- Goals (publishable proactive-AI benchmark).
- **2 categories, 10 tasks for v0.1:** 5 Proactive Recall + 5 Salience Gating. v0.5 (Aug 28) expands to 55/6.
- Metric definitions (correctness, latency, false-positive salience rate, attack-detection rate).
- Reference implementation (uses audiod + perceptiond + memoryd).
- Hardware baselines (laptop x86_64, Redax aarch64).
- Open governance (PRs welcome, MIT, **anti-capture clause**).
- **v80 addition:** Brain Row baseline (Perplexity Brain, +25% correctness, frozen) as the comparator. We publish our own row first.

---

## Day 4-5 (Thu-Fri 2026-06-26/27) — Pre-launch buffer

### 8. Pre-record 4 YouTube videos (buffer for somdipto camera-readiness)

- 8 daemons in 90s (master cut, ships Jul 8)
- Daemon teardown: memoryd (5 min, ships Jul 24)
- Daemon teardown: perceptiond (5 min, ships Jul 24)
- Pre-order unboxing preview (8 min, ships Aug 20)

### 9. Weekly dev log #21 (Friday)

Sections: live-verify stamp, NITI Aayog anchor, dglabs-eval v0.1 RFC, Perplexity Brain baseline blog, install-oneliner tease.

---

## Day 6 (Sat 2026-06-28) — Hardware pivot decision (carried from v74)

### 10. somdipto commits the hardware pivot decision (v1/v2 split)

Update `/home/workspace/dan-glasses/AGENTS.md` with the chosen hardware path. v74 default: v1 audio-only Neprion ₹15,500 / $189, v2 with display ₹33,000 / $399. v80 default: keep ₹12,000 / $145 in marketing until hardware commit resolves it.

### 11. Post the hardware decision (founder voice)

> Dan Glasses hardware decision:
>
> v1 (audio-only): [decision], $XXX dev-kit, Q4 2026.
> v2 (with display): $XXX dev-kit, Q1 2027.
>
> Why split: display hardware adds 6-9 months. v1 ships to ship. v2 ships to scale.
>
> Open eval, MIT, NITI Aayog-aligned. From India 🇮🇳.
>
> danlab.dev/blog/hardware-decision

---

## Day 7 (Sun 2026-06-29) — Light touch

No scheduled post. Internal: prep SIA-fork sprint (starts Mon 2026-06-30), prep install-oneliner (ships Jul 18).

---

## Week 2 (Jun 30 → Jul 6) — Sprint prep + README audit

| Day | Action | Receipt |
|---|---|---|
| Mon 06-30 | SIA-fork sprint kickoff | git commit + blog post |
| Mon 06-30 | `dani` repo README refresh (v80 audit) | PR merged |
| Tue 07-01 | Fork SIA v2 + integrate as monorepo subdir at `danlab-multimodal/sia/` | GitHub URL |
| Tue 07-01 | `dan-glasses` repo README refresh (v80 audit) | PR merged |
| Wed 07-02 | YouTube "dglabs-eval in 60s" (record) | internal cut |
| Wed 07-02 | `danlab-multimodal` repo README delta (v80 audit) | PR merged |
| Thu 07-03 | Wrap demo.py scorer as evaluate.py | GitHub commit |
| Fri 07-04 | Founder essay #2: "From India 🇮🇳 to the world — what it actually requires" | LinkedIn |
| Sat 07-05 | dglabs-eval v0.1 RFC published (github.com/somdipto/dan-lab/discussions or danlab.dev/r/dglabs-eval-v0.1) | public URL |
| Sun 07-06 | Light touch | no post |

## Week 3 (Jul 7 → Jul 13) — Blog + YouTube + Discord seed

| Day | Action | Receipt |
|---|---|---|
| Mon 07-07 | **Blog: "dglabs-eval v0.1: the first public benchmark for proactive AI glasses"** | danlab.dev/blog/dglabs-eval-v0.1 |
| Tue 07-08 | **YouTube: "8 daemons, 144 tests, 0 cloud" — 90s** | youtube.com/@danlab_dev |
| Wed 07-09 | **Hero X thread: "How we built a 302MB multimodal loop on CPU"** | @dan2agi |
| Thu 07-10 | Trusted-reader review of Show HN draft (3 readers) | review notes |
| Fri 07-11 | Founder essay #3: "Why we don't call it RL — the SIA path" | LinkedIn |
| Sat 07-12 | `dglabs-eval` repo CREATED (public, v0.1, 10 tasks) | github.com/somdipto/dglabs-eval |
| Sat 07-12 | **`dani` repo README refresh (final, pre-Show HN)** | PR merged |
| Sun 07-13 | `dan-glasses-daemons v0.2` GitHub release (installable) | release URL |

## Week 4 (Jul 14 → Jul 20) — Show HN week

| Day | Action | Receipt |
|---|---|---|
| **Mon 07-14** | **SHOW HN SHIPS (8 AM PT / 8:30 PM IST)** | news.ycombinator.com |
| Mon 07-14 | Dan1 replies to EVERY comment for 24h | HN comment count |
| Tue 07-15 | X thread: "Here's what HN got right, here's what they got wrong" | @dan2agi |
| Wed 07-16 | YouTube: "Show HN aftermath" — 5 min | youtube.com/@danlab_dev |
| Thu 07-17 | Substantive HN comments on AI threads (no engagement bait) | karma |
| Fri 07-18 | **NEW v80: `install-oneliner.sh` ships (`curl -sL danlab.dev/install | bash`)** | danlab.dev/install |
| Fri 07-18 | **X thread: "A day with Dan Glasses" (12 posts) — pinned on @dan2agi for 30 days** | @dan2agi |
| Sat 07-19 | Discord server live (50 founding members pre-invited) | discord.gg/danlab |
| Sun 07-20 | Light touch | — |

## Week 5 (Jul 21 → Jul 27) — dglabs-eval public + SIA-fork paper

| Day | Action | Receipt |
|---|---|---|
| Mon 07-21 | dglabs-eval v0.1 PUBLIC ANNOUNCE | blog + X + Reddit |
| Tue 07-22 | YouTube: "How to run dglabs-eval on your model" | youtube |
| Wed 07-23 | Substantive reply thread on Anthropic / DeepMind / Meta posts | X |
| Thu 07-24 | First daemon teardown: perceptiond (5 min) | youtube |
| Fri 07-25 | **dglabs-eval v0.1 SHIPS (10 tasks, 2 categories, our row first)** | github.com/somdipto/dglabs-eval |
| Sat 07-26 | Reddit r/MachineLearning: dglabs-eval v0.1 launch | reddit |
| Sun 07-27 | Light touch | — |

## Week 6 (Jul 28 → Aug 3) — Reddit + founder essay

| Day | Action | Receipt |
|---|---|---|
| Mon 07-28 | Reddit r/LocalLLaMA: dglabs-eval v0.1 launch | reddit |
| Tue 07-29 | Founder essay #4: "Why benchmarks matter more than demos in 2026" | LinkedIn |
| Wed 07-30 | First external dglabs-eval submission shoutout | @dan2agi |
| Thu 07-31 | Daemon teardown: memoryd (5 min) | youtube |
| Fri 08-01 | **dglabs-eval leaderboard OPEN for public submissions** | github |
| Sat 08-02 | "We will not run 'AGI is closer' takes. We will run numbers." | @dan2agi |
| Sun 08-03 | Light touch | — |

## Week 7 (Aug 4 → Aug 10) — Mid-Q3 hold + arXiv prep

| Day | Action | Receipt |
|---|---|---|
| Mon 08-04 | Founder essay #5: "What we learned shipping the first proactive-AI benchmark" | LinkedIn |
| Tue 08-05 | Blog: "dglabs-eval week 1: 8 submissions, 3 above our baseline" | blog |
| Wed 08-06 | Discord milestone: 1,000 members | discord |
| Thu 08-07 | First founder livestream (YouTube, 30 min) | youtube |
| Fri 08-08 | Substantive X thread on Anthropic Fable 5 / Mythos 5 export ban | @NandySomdipto |
| Sat 08-09 | Reddit r/singularity: weekly update | reddit |
| Sun 08-10 | Light touch | — |

## Week 8 (Aug 11 → Aug 17) — arXiv + Discord moderation

| Day | Action | Receipt |
|---|---|---|
| Mon 08-11 | 2 Discord mods recruited from community | discord |
| Tue 08-12 | "Honest about pre-RL" repost on /r/MachineLearning | reddit |
| Wed 08-13 | Founder essay #6: "What 5,000 GitHub stars taught us" | LinkedIn |
| Thu 08-14 | dglabs-eval v0.5 prep blog (55 tasks / 6 categories) | blog |
| **Fri 08-15** | **arXiv preprint: "dglabs-eval: A Benchmark for Proactive AI in Always-On Wearables"** | arxiv.org/abs/... |
| Sat 08-16 | "Pre-orders open in 10 days. ₹12,000. Q4 shipping. India-first." | @dan2agi |
| Sun 08-17 | Light touch | — |

## Week 9 (Aug 18 → Aug 24) — Pre-order warm-up

| Day | Action | Receipt |
|---|---|---|
| Mon 08-18 | Founder X: "Why v1 audio-only first. Why the display waits." | @NandySomdipto |
| Tue 08-19 | Blog: "Why Dan Glasses v1 is audio-only" | blog |
| Wed 08-20 | YouTube: "Pre-order unboxing — what ships Q4 2026" | youtube |
| Thu 08-21 | Discord founding-member badge announced (first 500) | discord |
| Fri 08-22 | Founder essay #7: "Why ₹12,000 is the right price for India 🇮🇳" | LinkedIn |
| Sat 08-23 | "The 7 things in the v1 dev-kit box" + photos | @dan2agi |
| Sun 08-24 | Light touch | — |

## Week 10 (Aug 25 → Aug 31) — Pre-orders live + Q3 close

| Day | Action | Receipt |
|---|---|---|
| **Mon 08-25** | **Pre-order page LIVE on danlab.dev** | danlab.dev/preorder |
| **Mon 08-25** | **Pre-order announcement X thread (somdipto + Dan1)** | @dan2agi + @NandySomdipto |
| Tue 08-26 | Reddit r/singularity: pre-orders live | reddit |
| Wed 08-27 | Founder X: "We just opened pre-orders. From India 🇮🇳." | @NandySomdipto |
| Thu 08-28 | **dglabs-eval v0.5 SHIPS (55 tasks, 6 categories, supply-chain attack scenario)** | github.com/somdipto/dglabs-eval |
| Thu 08-28 | YouTube: "Q&A: pre-orders, dev-kit, shipping, support" — 30 min | youtube |
| Fri 08-29 | Founder essay #8: "We just opened pre-orders for OSS AI glasses. Here's the story." | LinkedIn |
| Sat 08-30 | "Pre-order count: [N]. Discord: [N]. Stars: [N]. The Q3 numbers." | @dan2agi |
| Sun 08-31 | Blog: "Q3 close: what shipped, what we learned, what Q4 looks like" | blog |

---

## Open questions for somdipto (you) — refreshed for v80

1. **Show HN title lock by Jun 24.** v80 default: *"Show HN: Dan Glasses — proactive AI glasses, 8/8 on-device daemons, MIT."* Confirm?
2. **dglabs-eval v0.1 leadership:** Dan2 (research) authors, Dan1 (marketing) reviews for messaging — confirm?
3. **Hardware pivot decision (Jun 28):** v1 audio-only Neprion (₹15,500 / ~$189) vs v80 marketing default of ₹12,000. Which wins?
4. **NITI Aayog founder essay (this Friday, Jun 27):** want me to draft, or do you draft the policy-framing post?
5. **`@dan2agi` handle ready for daily takeover Jun 25.** Confirm handle exists + access.
6. **install-oneliner.sh shell-of-choice (Jul 18):** bash only, or bash + zsh? Default: bash + zsh.
7. **Perplexity Brain baseline blog (Wed Jun 25):** the angle is "+25% is the bar." Want me to draft, or do you?

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-23 10:30 IST.*

*v74 = "scale the moat with a publishable eval." v80 = "ship the wave + ship the install + ship the eval, all 8/8 daemons live, all 6 durable assets locked." v81 = measure the spike.*

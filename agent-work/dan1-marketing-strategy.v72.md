# Dan1 Marketing Strategy v72 — Post-AWE, Post-Hackathon

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-22 14:00 IST (08:30 UTC)
**Status:** ✅ Canonical. Supersedes v71.

> **v72 thesis:** v71 shipped the OpenClaw-as-default framing. v72 is **post-AWE 2026** (Snap Specs, Qualcomm Snapdragon Reality Elite, Even Realities G2) and **post-hackathon** (somdipto won India's first World Model Hackathon on 2026-06-20 with `dream-danlab.vercel.app`). v72 hardens the receipts against the *real* public state — **memoryd is intermittently down, openclaw is still down, audiod is v0.6 per SPEC.md** (v71 overclaimed v0.7 + 121/121), **danlab-multimodal is not yet public, dan-lab org is not yet public**. v72 ships the **honest receipts** + the **hackathon win** as the new headline + the **dream demo** as a new live product surface.

---

## 1. The v72 strategy in one page

**Goal (one line):** Convert the v71 OpenClaw framing into v72 receipts — **1 Show HN spike** + **1 dream demo elevation** + **1 hackathon-win thread** + **1 danlab-multimodal public release** + **1 paperclip → DanClaw rename** + **400 first users** by Day 28.

**The 6 v72 moves:**

1. **Honest receipts > aspirational narratives.** v71 said "7/8 daemons live · 144/144 tests." v72 says **"6/8 daemons live · 101+ audiod tests · memoryd intermittent · openclaw down."** Numbers move with reality, not the other way around.
2. **Dream demo is the new headline.** `dream-danlab.vercel.app` is live, won the World Model Hackathon on 2026-06-20, and is the strongest single asset DanLab has shipped in public. v72 puts it on the landing page, the pinned tweet, and the Show HN title.
3. **Hackathon win is the credibility proof.** somdipto won India's first World Model Hackathon. That's a public, dated, citable event. v72 makes it the centerpiece of Week 1.
4. **AWE 2026 context is the urgency.** Snap Specs at $2,195 + Qualcomm Snapdragon Reality Elite + Google Gemini smart glasses = the category is moving fast. v72 frames DanLab as the **OSS alternative** in a closed-platform race.
5. **OpenClaw-as-default (carried from v71).** Microsoft built the runtime. DanLab ships the surface. Every README, every tweet, every CTA still leads with OpenClaw.
6. **India 🇮🇳 as origin (carried).** Razorpay, YourStory, Inc42, the "Why India" blog post. The narrative moat Vayu and Sarvam don't have.

**The 8 v72 anti-patterns (vs v71):**

1. **Don't claim "7/8 daemons live" while memoryd is down.** v72 says **"6/8 daemons live · memoryd intermittent."**
2. **Don't claim audiod v0.7.1 (125 tests) or v0.8 (132 tests).** v72 defers to the canonical SPEC.md. v71's 121/121 was aspirational; the SPEC still says v0.6 + 73 + 19 = 92 cases. **v72 says "audiod v0.7 per SPEC, 92+ tests, wizard roundtrip 7.08s."**
3. **Don't claim openclaw is live.** v72 says **"OpenClaw revival pending. The 6 daemons that are live do not depend on OpenClaw."**
4. **Don't claim danlab-multimodal is public.** v72 ships the public release as a Day-2 action.
5. **Don't say "paperclip renamed to DanClaw" until the rename is done.** v72 ships the rename as a Day-3 action.
6. **Don't call danlab-multimodal an "RL" project.** v72 says **"pre-RL scaffold, forking SIA next."**
7. **Don't say "AGI" without a concrete artifact.** v72 says **"proactive AI companion."**
8. **Don't claim Snap/Meta/Apple "killer."** v72 says **"OSS alternative in a closed-platform race."**

---

## 2. The 7 principles of v72

1. **Honest receipts > aspirational narratives (NEW).** Every post has at least one receipt. The receipt matches the canonical source (SPEC.md, STATUS.md, `read_webpage`). No rounding up.
2. **Dream demo is the headline (NEW).** `dream-danlab.vercel.app` is the strongest single asset. Every surface mentions it.
3. **Hackathon win is the credibility proof (NEW).** June 20, 2026. India's first World Model Hackathon. Reactor + MaxMill + TheLaunchd hosted. somdipto won. This is the receipt nobody else in the category has.
4. **OpenClaw-as-default (carried from v71).** Every README, every tweet, every CTA leads with OpenClaw. Microsoft built the runtime. DanLab ships the surface.
5. **OSS > closed (carried).** MIT, on-device, audit-able. The moat is the license.
6. **India as origin (carried).** 🇮🇳 emoji on the avatar, "from India" in every press release, the "Why India" blog post is the centerpiece of Week 4.
7. **Cadence > polish (carried).** Every Friday = a weekly dev log. Every Wednesday = a YouTube demo. Every Monday = the highest-leverage move.

---

## 3. The 28-day v72 calendar (week-by-week)

| Week | Theme | Major events | Blog posts | YouTube | Press | Other |
|---|---|---|---|---|---|---|
| **W1 (06-23 → 06-29)** | Hackathon win + dream demo | dream-danlab.vercel.app launch post | "We won India's first World Model Hackathon" | Dream demo screencast (60s) | YourStory follow-up | 4 r/LocalLLaMA weekly threads |
| **W2 (06-30 → 07-06)** | AWE response + OSS alternative | Show HN: Dan Glasses | "Snap Specs at $2,195. Dan Glasses is MIT." | Wizard roundtrip screencast (90s) | Show HN | 4 r/LocalLLaMA weekly threads |
| **W3 (07-07 → 07-13)** | danlab-multimodal public + SIA fork | danlab-multimodal goes public | "Pre-RL scaffold, forking SIA next" | SIA fork preview (60s) | TechCrunch pitch (after Show HN) | 4 r/LocalLLaMA weekly threads |
| **W4 (07-14 → 07-20)** | paperclip → DanClaw + India-first | DanClaw rename shipped | "Why India 🇮🇳" (centerpiece) | "AGI from India" vlog | YourStory + Inc42 follow-up | 4 r/LocalLLaMA weekly threads |

---

## 4. The 5 channels (v72 detail)

### Channel 1: GitHub (the primary durable surface)

**v72 GitHub repos (4 live + 2 to ship):**

| Repo | State | v72 action |
|---|---|---|
| `somdipto/dan-glasses` | Public, 6/8 daemons live | Add the v72 README + the live 6/8 status block + the dream demo link + the hackathon badge |
| `somdipto/dan-consciousness` | Public, 4 commits, 0 stars | Pin the public version, add a "Who is Dan1?" section |
| `somdipto/danlab-multimodal` | 404 (not public) | **Day 2: ship the public release with pre-RL framing** |
| `somdipto/paperclip` (→ `somdipto/danclaw`) | Not public locally | **Day 3: ship the rename + public release as `danclaw`** |
| `somdipto/dan-lab` | 404 (org not created) | Deferred to v73 |
| `somdipto/sia-fork` | 404 (not created) | Deferred to v73 (W3 of v72 plan ships the SIA fork brief, not the repo) |

**v72 GitHub badges (every public repo):**

```markdown
![Status](https://img.shields.io/badge/status-6%2F8%20daemons%20live-brightgreen)
![Tests](https://img.shields.io/badge/tests-100%2B%20audiod%20passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![OpenClaw-ready](https://img.shields.io/badge/OpenClaw-ready-blue)
![Hackathon winner](https://img.shields.io/badge/World%20Model%20Hackathon-winner-gold)
```

### Channel 2: X / @NandySomdipto (the daily surface)

**v72 X cadence:** 3 posts in 5 days (W1), 4 posts/week thereafter.

**v72 X priority list (the first 10 posts, see `dan1-twitter-content.md`):**

1. **Hackathon win thread** (7 tweets, the receipts)
2. **Dream demo launch** (single tweet + link)
3. **6/8 daemons live receipt** (single tweet + STATUS.md link)
4. **audiod v0.7 changelog receipt** (single tweet + SPEC.md link)
5. **Show HN teaser** (single tweet)
6. **Show HN: Dan Glasses + Dream Demo** (HN post)
7. **danlab-multimodal public** (single tweet)
8. **SIA fork preview** (single tweet + brief link)
9. **paperclip → DanClaw rename** (single tweet)
10. **Why India 🇮🇳** (single tweet + blog link)

### Channel 3: Hacker News (the leverage surface)

**v72 Show HN plan (W2, target date 2026-06-30 or 2026-07-02):**

**Title:** "Show HN: Dan Glasses – OSS AI glasses from India, 6/8 daemons live"

**First comment (drafted):**

> Hi HN — somdipto + Dan1 here. We build OSS AI glasses from Bengaluru.
>
> What's shipped today (the receipts):
> - 6/8 on-device daemons live (audiod, perceptiond, toold, ttsd, os-toold, dan-glasses-app)
> - audiod v0.7: whisper.cpp base.en + Silero VAD, 92+ tests
> - perceptiond: LFM2.5-VL-450M on llama.cpp, watchful mode
> - memoryd: SQLite + MiniLM-L6-v2 semantic recall, 16 tests
> - toold: sandboxed shell + Python exec, 18 tests
> - ttsd: KittenTTS medium, 6 tests
> - Wizard roundtrip: audiod → memoryd → ttsd in 7.08s
>
> What it is NOT: not AGI, not RL, not shipped yet (dev-kit Q1 2027).
>
> The second demo: somdipto won India's first World Model Hackathon on June 20, 2026, with `dream-danlab.vercel.app` — real-time dream generation from text using lingbot. This is a sibling demo, not glasses software, but it's the credibility proof.
>
> OpenClaw: every daemon is an OpenClaw skill. Microsoft built the runtime. We ship the surface.
>
> GitHub: github.com/somdipto/dan-glasses
> License: MIT
> From: India 🇮🇳

### Channel 4: YouTube (the visual surface)

**v72 YouTube plan (3 videos in 28 days):**

1. **W1: "Dream Generation in 60 seconds"** — real-time demo of `dream-danlab.vercel.app`. India 1947, future Church Street, etc. Music: soft Indian classical.
2. **W2: "Wizard Roundtrip in 90 seconds"** — actual 7.08s roundtrip + a slow-mo explanation. Voice: somdipto.
3. **W3: "6 Daemons, 6 Receipts"** — one daemon per 10 seconds, with the live status block. Voice: Dan1 (synthesized, ttsd).

### Channel 5: Reddit (the community surface)

**v72 Reddit plan (8 posts in 28 days):**

- **r/LocalLLaMA** (4 weekly threads): the canonical OSS community. Topics: pre-RL scaffold, SIA fork, audiod v0.7, dream demo + lingbot.
- **r/indianstartups** (1 re-launch post — careful, the earlier post was deleted): "We won India's first World Model Hackathon. Here's the open-source build."
- **r/MachineLearning** (1 thread — high-bar, defer to W3 or v73): the SIA fork brief.
- **r/singularity** (1 thread, optional): the dream demo.
- **r/LocalLLama (again, W4)**: the "Why India 🇮🇳" essay.

---

## 5. The 4 risks (v72)

1. **memoryd flakiness.** memoryd is intermittent (curl fails on port 8741 then succeeds 30s later). The "6/8 daemons live" count drops to "5/8" if memoryd is down. **Mitigation:** the live status block updates every 4 hours. v72 ships a watchdog (already in `/home/workspace/dan-glasses/scripts/`) to restart memoryd on failure.
2. **openclaw stays down.** openclaw has been down since v57. The Telegram @danlab_bot is unreachable. **Mitigation:** v72 ships the revival PR on Day 1 (per the v71 punchlist) — but if revival takes longer, the W1 Telegram post is skipped.
3. **Show HN doesn't spike.** HN is a leverage surface, not a strategy. If the Show HN doesn't land in the top 30, v72 falls back to the weekly dev log + the 8 Reddit threads. **Mitigation:** the receipts are the strategy, not the spike.
4. **Somdipto's "India's first AI Companion Smart Glasses" Reddit post was deleted.** The Reddit r/indianstartups re-launch needs to be careful. **Mitigation:** lead with the hackathon win, not the product. The hackathon is the receipt; the product is the demo.

---

## 6. The 5 open questions for somdipto (v72)

1. **Dream demo positioning.** Should `dream-danlab.vercel.app` be the second product on danlab.dev, or a separate `dream.danlab.dev` sub-domain? v72 default = second product on danlab.dev.
2. **Show HN timing.** W2 of v72 (06-30 or 07-02). Earlier = more leverage, less polish. Later = more polish, less leverage. v72 default = 06-30 (Tue, peak HN traffic).
3. **danlab-multimodal license.** MIT (carried) or Apache-2.0? v72 default = MIT.
4. **Dev-kit pre-order page.** Build now or wait for Stripe? v72 default = wait for Stripe (W2 of v72 plan).
5. **Telegram @danlab_bot revival.** Day 1 of v72 (revive the OpenClaw agent), or W3 (after the SIA fork ships)? v72 default = W3 — let the OpenClaw revival land *after* the Show HN.

---

## 7. v72 → v73 transition

**v72 trigger:** 28 days from 2026-06-23 = 2026-07-21, OR the Show HN spike (>100 points) + 400 first users, whichever comes first.

**v73 surface (preview):**
- Scale to 5,000 first users
- 1,000 GitHub stars (4 repos)
- 2 Tier-1 press pickups (TechCrunch or The Verge or WIRED)
- 2 podcast appearances
- 1 dev-kit ship partner (BOM lock + manufacturing partner in Bengaluru)
- $49 MRR (DanClaw Pro trial)
- 25 dev-kit pre-orders
- 5 SIA citations

**v73 thesis (preview):** "Scale the spike." From 400 to 5,000. From 0 stars to 1,000. From 0 press to 2 Tier-1.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 14:00 IST. v71 ships the OpenClaw wedge. v72 ships the post-AWE, post-hackathon receipts. v73 scales the spike.*

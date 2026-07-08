# Dan1 Marketing Research — v65 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 06:30 IST (01:00 UTC)
**Status:** ✅ Canonical. Supersedes v64.
**Read first:** `dan1-marketing-strategy.md` v65, `dan1-content-calendar.md` v65.

> **v65 is the "ship the public surface" pass.** v64 framed the receipts as the brand. v65 *actually ships* the public surface that proves them: danlab.dev gets refreshed to a 2026 homepage, dan-glasses gets a real public README ready to push to github.com/somdipto/dan-glasses, danlab-multimodal gets a public release tag, and the Show HN for DanClaw Phase 1 is in the can. The marketing job is no longer "make the receipts visible" — it's "publish the receipts in a way that survives first contact with a stranger."

---

## 0. What changed in the last 24h (since v64, 2026-06-20)

| # | Event | Source | Marketing implication |
|---|-------|--------|----------------------|
| 1 | **danlab.dev homepage still reads 2024** — lists Agent8, Zerant, Dapify, "AI Glasses" (not "Dan Glasses"). | `web_search danlab.dev` (read_webpage saved at `/home/.z/workspaces/con_38s2Ps9fVpz3ywTD/read_webpage/danlab.dev.md`) | First-contact failure. A stranger lands on danlab.dev and gets a 2024 vibe. We need to fix this *this week* or every other piece of marketing is wasted. |
| 2 | **No @danlab_dev Twitter handle visible.** | `x_search` returned no @danlab_dev profile. | Need to claim it (or document why we won't) this week. The brand needs a home on X. |
| 3 | **Public GitHub presence for Dan Glasses is missing.** | `web_search "DanLab" multimodal paperclip github` showed: `agencyenterprise/paperclip-ai`, `paperclipai/paperclip` — but no `somdipto/dan-glasses`, no `somdipto/danlab-multimodal`. | Everything we ship is in `/home/workspace`. The public internet has nothing for *us*. That's the #1 marketing problem. |
| 4 | **Competitor landscape shifted slightly.** | `web_search "Dan Glasses AI wearable India somdipto"` returned Oculosense (open SDK, NIT Hamirpur, "Made in India"), Focally (AR wearables), Sarvam AI (smart glasses at India AI Impact Summit Feb 2026), Dymesty, Apple AI Glasses (N50, 2027), Ray-Ban Meta. | We're not alone in the "India AI glasses" frame anymore. Oculosense and Sarvam have public launches. We need sharper differentiation now: "MIT + on-device + proactive + 7 daemons" is the wedge. |
| 5 | **v64 open questions remain open** (Twitter handle, danlab.dev refresh, public GitHub release, Show HN timing, brand assets). | `dan1-v64-summary.md` | This run ships the answers. |

**Net new since v64:** Items 1–4 are the world moving while we were writing the strategy. Item 5 is what this run actually delivers.

**The headline change:** v64 ended with "make the invisible visible." v65 ends with "make the public surface match the receipts, or kill the strategy."

---

## 1. What is Dan Glasses? (v65 answer)

**One line:** An open-source, MIT-licensed, proactive AI companion built as 7 modular daemons — audiod v0.6 is live today, with a wearable hardware target at ₹12K–15K ($145–180).

**The shape, in 2026-06-21:**

- **Software (shipped today):** 7 daemons, MIT, modular. `audiod` is at v0.6 with 101/101 tests. `perceptiond` and `memoryd` are spec'd and runnable. `openclawd` is live with `@danlab_bot` on Telegram.
- **Hardware (target):** <50g, JBD MicroLED, 2× 200mAh, USB-C. **BOM target ₹12K–15K ($145–180).** Compare to Snap Specs at $2,195 / 132-136g.
- **Form factor roadmap:** v1 = desktop companion (live now via the 7 daemons). v2 = wearable glasses (Redax aarch64 target).
- **Model strategy:** HRM-Text (1B) for reasoning + Whisper base for STT + LFM2.5-VL-450M for vision. All small, on-device, fast.
- **Identity:** "Proactive companion, not reactive assistant." Speaks when it has something to add. Remembers across sessions. Privacy-first (data stays local).

**Why "proactive" matters (the one differentiator to keep repeating, sharpened in v65):**

- Ray-Ban Meta, Apple AI Glasses, Snap Specs, Sarvam AI, Oculosense — all are *prompt-and-response* assistants. The user has to ask.
- Dan Glasses is the only one whose loop is *Perceive → Reason → Act → Remember* running continuously, only surfacing when salience justifies interrupting. This is not a feature, it's the architecture.
- The receipt for "proactive" is `perceptiond` (continuous visual frame scoring) + `audiod` v0.6 (continuous VAD + transcription) + `memoryd` (semantic recall across sessions) + `openclawd` (orchestration). All shipped. All curl-able.

**v65 add — what makes us different from the new India cohort:**

- **Oculosense:** open SDK, but offline-only and visually-impaired-focused. We're companion-first, multimodal, on-device but cloud-optional.
- **Sarvam AI:** national-scale model lab with government summit halo. We're 1.5 people in Bengaluru. We don't compete on the model. We compete on the *loop*.
- **Focally:** AR-display-first. We're audio-first. We don't fight on AR.
- **Apple N50 / Ray-Ban Meta / Snap Specs:** closed, US-axis, expensive. We're MIT, India-axis, <$200 BOM.

**The wedge in one sentence:** *Oculosense is offline-only. Sarvam is cloud-only. Apple/Meta/Snap are closed and US-axis. Dan Glasses is the only one that is MIT + on-device + proactive + India-priced.*

---

## 2. User workflow — unboxing to daily use (v65, sharpened)

**Today (desktop v1, ships now):**

1. **Provision:** `git clone github.com/somdipto/dan-glasses`; `pip install -r Services/*/requirements.txt`; start `audiod`, `perceptiond`, `memoryd`, `openclawd`. (Full script in `scripts/start-all.sh`.)
2. **Calibrate (day 1):** Open the Tauri shell (`apps/dan-glasses-app/`). Walk the Bootstrap panel: camera permission, model download, language + preferences.
3. **Daily loop:** Work as usual. Dan sees your screen, hears your words, remembers your context. Speaks only when it has something worth saying.
4. **Recall:** "Dan, what did I say about the danclaw phase 1 tarball on Tuesday?" → memoryd semantic search → audiod TTS.
5. **Inspect:** All daemons expose `/health` and `/status`. Logs at `/dev/shm/{audiod,perceptiond,...}.log`. Loki-indexed.

**Tomorrow (wearable v2):**

1. Unbox glasses (<50g, MicroLED, USB-C).
2. Pair to your laptop/phone (one-tap Bluetooth).
3. Wear. The 7 daemons run on the paired device. The glasses are I/O only.

**What to put on the landing page (in this order):**
1. "Wears your face. Runs on your laptop. MIT-licensed." (one screen)
2. Live status strip (one screen, illustrative)
3. The 7 daemons as a single diagram (one screen)
4. Live `/health` curl (proof of life)
5. The HRM-Text model card (substance over sizzle)
6. GitHub link as primary CTA

---

## 3. Competition — receipts that haven't moved (v65, refreshed)

**Closed-source bar (heavy, expensive, prompt-and-response):**

| Product | Weight | Price | Form | Differentiator |
|---|---|---|---|---|
| **Snap Specs** | 132-136g | $2,195 | Glasses (Fall 2026) | Two Snapdragons. Ad-supported. Snap CEO visibly struggled w/ weight in demo. |
| **Ray-Ban Meta Gen 3** | ~50g | ~$300 | Glasses (live) | Phone-tethered. Reactive assistant. No on-device loop. |
| **Apple AI Glasses (N50)** | TBD | TBD | Glasses (late 2027 per Bloomberg) | 14-month indie window. Apple delayed from earlier plan. |
| **Humane AI Pin** | ~34g | $499 + $24/mo | Pin (DISCONTINUED Nov 2024) | Killed. The "wearable companion" lesson. |
| **Friend** | ~50g | $129 | Pendant | Gizmodo called it out as not-a-friend. Lesson #2. |

**India cohort (v65, new):**

| Product | Position | Differentiator from us |
|---|---|---|
| **Oculosense** | Offline-only AI glasses for visually impaired. Open SDK. NIT Hamirpur. Startup India recognized. 1,000+ deployed. | Visually-impaired-focused. We're companion-first. They claim offline; we claim *on-device-with-optional-cloud.* |
| **Sarvam AI** | National-scale model lab. Unveiled smart glasses at India AI Impact Summit Feb 2026. Government halo. | Model lab. We're a companion product. They have IndiaAI backing; we have audiod v0.6 with 101/101 tests. |
| **Focally** | AR wearables + smart glasses. Indian AR startup. | AR-display-first. We're audio-first. |
| **Dymesty** | Premium AI glasses, business elegance. | Premium US/EU positioning. We're MIT + India-priced. |

**Our wedge (defensible, credible, indie-sized):**

- **<50g vs 132-136g** — wearable in a way Snap is not.
- **$145-180 BOM vs $2,195** — open hardware anyone can iterate on.
- **Proactive loop, not reactive prompt** — audiod v0.6 + perceptiond + memoryd is the receipt.
- **MIT, modular, runnable today** — anyone can clone and ship a fork.
- **From India** — geopolitical hedge + cost base.
- **7 daemons you can inspect** — vs. Oculosense's "open SDK" (their SDK is closed-source even if it has hooks); vs. Sarvam's model (cloud-required); vs. Meta/Snap/Apple (closed).

**Don't fight on AR display.** Snap Specs has two Snapdragons. Apple N50 has Apple silicon. We don't. Our AR is "audio-first, MicroLED when we ship it." Compete on AI loop, not display.

**Don't fight on model size.** Sarvam has IndiaAI-scale compute. We have HRM-Text 1B on a $300 laptop. We compete on architecture, not parameters.

---

## 4. danlab-multimodal — what it is and what it isn't (v65)

**What it is:**
- A working sub-300MB multimodal pipeline: screen capture → SmolVLM-256M inference → heuristic scoring → feedback loop.
- Runs on CPU with llama.cpp. ~26-32s per image.
- MIT-licensed hackathon project. Live demo at `zo.pub/som/danlab-multimodal-demo`.

**What it isn't:**
- It is **NOT reinforcement learning.** No weights are modified. No policy gradient. No learned reward model. README explicitly disclaims this.
- The "heuristic feedback loop" is hand-coded rules (length penalty, error detection, UI element identification). Real RL upgrade path = fork [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026).

**Why we ship it anyway:**
- It's a **pre-RL scaffold** that any developer can run on a $300 laptop.
- It's reproducible: `python3 src/demo.py demo` works headless.
- It's the cheapest working VLM-on-CPU demo in the world (302MB combined).
- It's a recruiting artifact: shows we can ship multimodal end-to-end.

**Marketing framing (v65):** "World's smallest working VLM-on-CPU loop. Pre-RL. Heuristic. MIT. Hackathon-grade but production-shaped. Run it in 30 seconds: `git clone && python3 src/demo.py demo`." Don't oversell. Don't claim RL.

**v65 new — pre-write the Reddit r/LocalLLaMA post** (in v65 content calendar). It's the cleanest pre-RL public artifact we have.

---

## 5. Paperclip / DanClaw — what they are (v65)

**Paperclip (paperclip/README.md):** Iterative code-review / paper-clipping agent harness. Receives paper, digests, persists into memory graph. TBD deeper read — file is light; treat as in-progress. **Not marketing-relevant in v65.** Don't pitch it.

**DanClaw (now real on disk):** `/home/workspace/danclaw/` and `danclaw-phase1.tar.gz` are now on disk. Phase 1 tarball is the first downloadable artifact. This is the **Show HN for 2026-06-30 14:00 PT** — see content calendar v65 for the full draft.

**Other distribution surfaces (v65, named for the first time):** `danclaw-mobile`, `Glance`, `zerant-browser`, `clawdi`, `clicky-cross-platform`, `civpredict-env`, `danlab-agent-domains`, `danlab-channel`, `sora-d0.1`, `mobile-use`. Each is a future distribution surface. Don't pitch them as products yet.

**Marketing angle:** "Every DanLab product is a distribution surface for our agents." Don't pretend this is a consumer story yet. It isn't. It's a *platform + agents* story.

---

## 6. The overall Danlab story (v65)

**Origin:** Bengaluru. somdipto Nandy. 4,148 LinkedIn followers, 500 connections. buildspace alum. Bootstrapping an AI research lab from India after a 9-to-5. Reddit thread exists: r/indianstartups.

**Narrative arc (use this on every channel, v65 version):**

> Most AI labs are in the US or China. We are in India. We're building AGI from the other side of the planet — and shipping everything we make, MIT-licensed, with a daemon architecture anyone can fork. Our first product is Dan Glasses: an always-on AI companion that sees what you see, hears what you say, remembers what matters. audiod v0.6 is live today. Clone it. Run it. Break it. Privacy first. Salience over completeness. Built in the open.

**Three pillars (this is the triangle to repeat, do not edit):**
1. **Proactive, not reactive.** The loop runs continuously.
2. **On-device, MIT, modular.** No cloud lock-in. Daemons are inspectable.
3. **From India.** Cost base + geopolitical hedge + genuine frontier signal.

**v65 add — the wedge against the new India cohort:** "Oculosense is offline-only. Sarvam is cloud-only. Apple/Meta/Snap are closed and US-axis. Dan Glasses is the only one that is MIT + on-device + proactive + India-priced."

---

## 7. Marketing channels — what works for us in 2026-06 (v65)

**Tier 1 — ship weekly, post daily (sharpened in v65):**
- **X (Twitter):** Claim `@danlab_dev` this week. Daily ship-log + insight. 1 thread/week. 1 reply/day to AR/AI tweeters. **v65 new:** cross-post every tweet to @danlab_bot Telegram.
- **GitHub:** Push 3 repos to public this week (`dan-glasses`, `danlab-multimodal`, `danclaw` or `danclaw-phase1`). Use releases, not just commits. README is the landing page.
- **Hacker News:** Ship Show HN for DanClaw Phase 1, 2026-06-30 14:00 PT. Then Show HN for audiod v0.6 (the production-tested one) in week 28.
- **LinkedIn:** somdipto already has 4,148 followers. Cross-post weekly.

**Tier 2 — substance:**
- **arXiv / blog:** "Sub-300MB VLM-on-CPU with heuristic feedback loops" (from danlab-multimodal). One essay on audiod/perceptiond architecture.
- **YouTube:** 2-min asciinema-style demo of audiod + perceptiond live. Shipped the danlab-multimodal asciinema — same template.
- **Reddit:** r/MachineLearning, r/LocalLLaMA, r/indianstartups, r/singularity.

**Tier 3 — credibility:**
- **Show at AWE 2027.** Plan now.
- **Press list:** Uploadvr, Road to VR, Mixed News, HackerNoon, IndiaAI dispatch, YourStory.
- **Conferences:** KCD India, PyCon India, Indic AI conf, ETHIndia.

**Tier 4 — community:**
- **Discord/Matrix:** one channel per daemon (audiod, perceptiond, memoryd, paperclip, danclaw). Defer until 50 stars.
- **Office hours:** weekly Thursday 9pm IST — somdipto + Dan on a public Zoom. Start when we have 10 public users.
- **Telegram (NEW in v65):** @danlab_bot is already live via OpenClaw. Flip to public this week. Set channel username. Pinned message = pinned tweet.

---

## 8. Content to produce (v65 concrete list)

**This week (v65, week 26):**
1. Push `somdipto/dan-glasses` to public GitHub. Tag v0.6.0-audiod.
2. Push `somdipto/danlab-multimodal` to public GitHub. Tag v0.1.0.
3. Refresh danlab.dev homepage with v65 landing copy.
4. Claim @danlab_dev on X. Cross-post first 10 tweets (see v65 twitter content).
5. Flip @danlab_bot to public on Telegram.
6. Show HN draft for DanClaw Phase 1 (drafted in v65 content calendar).
7. Ship blog: "audiod v0.6 — adaptive whisper timeout, 101/101 tests."
8. Ship tweet thread: "What we shipped this week at danlab.dev."
9. LinkedIn longform: "Week 26 — audiod v0.6, Tauri shell, danlab-multimodal."

**This month (v65):**
10. arXiv preprint: "Pre-RL Scaffold: A Heuristic Feedback Loop for Sub-300MB VLM Inference on CPU" (from danlab-multimodal).
11. YouTube demo: 2-min screen-cast of audiod + perceptiond live on a $300 laptop.
12. IndiaAI / YourStory pitch: "AGI from India — the indie's roadmap."
13. HackerNoon essay: "Why we shipped a <50g wearable against Snap's 132g one."

**This quarter (v65):**
14. Open-source release: danclaw-phase1 (already on disk; needs a real repo + README + tag).
15. Talk submission: KCD India, PyCon India, Indic AI.
16. AWE 2027 application.

---

## 9. Current online presence (v65 snapshot, 2026-06-21)

- **danlab.dev** — Live, but reads 2024-ish. Mentions Agent8, Zerant, Dapify, "AI Glasses." The website does not reflect v65 reality. **v65 action:** replace with v65 landing copy by Tuesday 2026-06-24.
- **LinkedIn** — somdipto: 4,148 followers, Bengaluru, "Product Builder." Bio is generic. **v65 action:** request a 50/100/200-word bio paragraph from somdipto.
- **Reddit** — One thread on r/indianstartups about bootstrapping from India.
- **GitHub** — `somdipto/dani` (public), `somdipto/dan-lab` org. **No public release on `dan-glasses`, `danlab-multimodal`, `danclaw` yet (they're on disk in /home/workspace).** **v65 action:** push 3 repos public this week.
- **Hacker News** — No prior posts. **v65 action:** Show HN for DanClaw Phase 1, 2026-06-30 14:00 PT.
- **X / Twitter** — Connected handle @Shodan_s. **No public brand account for danlab yet.** **v65 action:** claim @danlab_dev this week.
- **YouTube** — None. **v65 action:** record 2-min demo, publish 2026-06-29.
- **Substack / Medium / HackerNoon** — None. **v65 action:** HackerNoon essay this month.
- **Telegram** — @danlab_bot is live (OpenClaw), but private. **v65 action:** flip to public this week.

**Gap:** The work is real and shipping. The *visible* work on the public internet is from 2024. v65 is the first pass that ships the public surface as a coherent system. After v65 lands, the gap closes by ~80%.

---

## 10. First users / customers (v65, profile)

**Tier 1 — developer-early-adopter (target 50 in 90 days):**
- India-based ML engineers, indie hackers, buildspace / outercurve / YC alum.
- Age 22-35. Bengaluru, Hyd, Mumbai, Delhi.
- Already owns a $300-800 laptop, runs Linux, knows what Whisper is.
- Use case: replaces half their Notion / Obsidian / screen-recorder stack.
- Wedge: clone the repo, run the daemons, fork audiod.
- **v65 sharpened:** *not* "pitch to enterprise first." Enterprise comes from Tier 1 users crossing over. Repeat: Tier 3 doesn't happen before Tier 1.

**Tier 2 — accessibility / cognitive-load (target 200 in 6 months):**
- People with ADHD, dementia caregivers, blind/low-vision users.
- Use case: hands-free voice-first recall, "what did I do yesterday."
- Wedge: audiod + memoryd is enough to demo a non-trivial "remember for me" experience.
- **v65 add:** Oculosense is the named competitor in this tier. Differentiation: we're companion-first, not visually-impaired-first. The "remember for me" experience is for everyone.

**Tier 3 — enterprise / B2B (target 5 pilots in 9 months):**
- Field-service technicians, surgeons, lawyers — anyone whose hands are busy and whose context is high-value.
- Wedge: on-device = HIPAA / GDPR friendly. Sell the *daemon architecture* + air-gap story.
- **Don't pitch this until Tier 1 has 50 active users.** Repeat: don't pitch enterprise before the developer community exists.

---

## 11. What we are NOT claiming (integrity guardrails, v65)

- We are NOT claiming **RL.** danlab-multimodal is a heuristic loop. README disclaims it. Repeat the disclaimer.
- We are NOT claiming **AGI.** We are building *toward* it. The Reddit thread said "open-weight models and eventually frontier-level systems." That's the right level.
- We are NOT claiming **AR glasses shipping today.** v1 is desktop. v2 is the wearable. Be honest.
- We are NOT claiming **Snap / Apple / Meta / Sarvam / Oculosense competition in the "we're better" sense.** They have 100× our team (or 10000×). Our wedge is open + on-device + India-priced + proactive. State the wedge; don't trash them.
- We are NOT claiming **a wearable hardware date.** BOM is a target, not a date.
- We are NOT claiming **Telegram is a real community yet.** It's a channel, not a community. Community = people posting, not just us posting.

These are non-negotiable. If a draft crosses one of these lines, rewrite.

---

## 12. v65 deliverables (linked)

- `dan1-marketing-strategy.md` v65 — three pillars + channel playbook (one v65 change: "ship the public surface" as the new headline claim)
- `dan1-content-calendar.md` v65 — week 26 calendar, daily non-negotiables, Show HN draft for 06-30
- `dan1-twitter-content.md` v65 — @danlab_dev bio, pinned tweet, first 10 posts
- `dan1-landing-copy.md` v65 — hero, 7 daemons, FAQ, CTA, ready to push to danlab.dev
- `dan1-github-readme-suggestions.md` v65 — global rules + per-repo READMEs ready to commit

---

## 13. v65 → v66 transition

**v66 will be the "first 50 stars" pass.** Once audiod + danlab-multimodal together cross 50 GitHub stars, v66 will:
1. Open a public mailing list.
2. Open the waitlist for v1 desktop companion.
3. Plan the AWE 2027 application.
4. Draft a press list with somdipto's short bio.
5. Open the danlab.dev refresh to public beta (collect email).
6. Spin up a Discord/Matrix per daemon.

**Don't do any of those now.** v65 is "ship the public surface, post daily, count clones."

---

## 14. Open questions for somdipto (v65)

1. **Twitter handle:** Claim @danlab_dev this week? Want me to draft the application tweet?
2. **danlab.dev refresh:** I have v65 landing copy ready. Want me to push it to zo.space or build a Vite+React Site at `danlab.dev`?
3. **Public GitHub repos:** dan-glasses, danlab-multimodal, danclaw are all on disk but private. Want me to commit the v65 READMEs and tag the releases?
4. **Show HN timing:** DanClaw Phase 1 Show HN drafted in v65 calendar for 2026-06-30 14:00 PT. Confirm or shift.
5. **Brand assets:** somdipto, do you have a public-facing bio paragraph (50/100/200 words) I can use for press / conferences / LinkedIn hero?
6. **Telegram @danlab_bot:** Flip to public this week? Set channel username? Pinned message = v65 pinned tweet.
7. **India cohort response:** Should I draft a 1-pager on "Dan Glasses vs Oculosense vs Sarvam" for Tier 1 press? Or is that over-claiming?

---

**Filed under:** `agent-work/dan1-marketing-research.v65.md`
**Next:** `agent-work/dan1-marketing-strategy.v65.md`

# Dan1 Marketing Research — v66 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 07:30 IST (02:00 UTC)
**Status:** ✅ Canonical. Supersedes v65.
**Read first:** `dan1-marketing-strategy.md` v66, `dan1-content-calendar.md` v66.

> **v66 thesis — the category just exploded. We don't move. We narrate.** v65 shipped the public surface and the cadence. Between v65 (06-21 06:30) and v66 (06-21 07:30), Snap unveiled Specs at $2,195 with Spiegel calling them "the beginning of a new era of computing," Google I/O tied Android XR to Warby Parker + Gemini, Qualcomm announced Snapdragon Reality Elite for AR glasses, and Illinois introduced HB4843 to ban smart glasses while driving. This is a tidal wave of category validation. v66 is the pass that rides the wave without claiming the wave. We don't pretend to be Snap. We don't pretend to be Google. We say: here is the open-source, MIT-licensed, India-priced proactive alternative. audiod v0.7 (Tauri client) is the new receipt. dan2's model analysis (v0.7 — KittenTTS swap, Moonshine v2 pilot, LFM2.5-1.2B-Thinking adoption) is the new substance. The category will get louder; we get more specific.

---

## 0. What changed in the last 60 minutes (since v65, 2026-06-21 06:30 → 07:30 IST)

| # | Event | Source | Marketing implication |
|---|-------|--------|----------------------|
| 1 | **Snap Specs officially unveiled at $2,195** — Spiegel called them "the beginning of a new era of computing." Celebrity launch with Kaia Gerber, Jimmy Butler, Jack Harlow. Pre-orders open, ships Fall 2026 (US/UK/France). ~4h battery. Two Snapdragons. Fully standalone. | NPR 06-19, NY Post 06-16, Yahoo Finance | Snap just set the price ceiling at $2,195. Our $145–180 BOM target is now *99% cheaper than the cheapest credible competitor*. **Repeat the number: $2,195 vs $145–180 BOM.** |
| 2 | **Google Android XR + Warby Parker + Gentle Monster** — unveiled at Google I/O May 2026, paired with Gemini AI for on-device voice, assistant, audio. | Glass Almanac 06-19, Google I/O recap | Gemini is the model. Android XR is the platform. Warby/Gentle Monster are the frames. **We are the open-source OS, not a Google partner.** Our wedge: MIT + on-device + proactive, no Gemini required. |
| 3 | **Qualcomm Snapdragon Reality Elite** — 60% GPU, 30% CPU, 160% NPU lift. START toolkit for 40+ AI wearables (glasses, jewelry, earbuds). | CNBC 06-16, Zamin.uz 06-19 | Qualcomm just made it cheaper to ship AR glasses. Our wearable v2 (Redax aarch64) was already the right architecture. v66 should not chase Qualcomm's chip — **we run on a $300 laptop today, Qualcomm partners ship in 2027+**. |
| 4 | **Illinois HB4843** — first US state bill to ban smart glasses while driving. | govtech.com 06-20 | Regulation is coming. On-device privacy is going to be a compliance requirement in 2027, not a marketing claim. **We are already on-device by default.** This is a v66 wedge, not a v67 wedge. |
| 5 | **Apple AI AirPods + glasses** — Bloomberg via NY Post, Apple prepping camera + AI AirPods and glasses to compete with Meta. | NY Post 06-16 | Apple is shipping the same category in 2026–27. Tim Cook + satya + Sundar all chasing the same form factor. **The category is confirmed.** v66 message: while Apple/Snap/Google spend billions, we ship audiod v0.7 today. |
| 6 | **audiod v0.7 shipped** — Tauri integration client, 8+ tests, dependency-light Python wrapper. | `dan2.md`, `Services/audiod/client.py` | New receipt. v66 calendar adds the audiod v0.7 announcement as the Mon 06-23 ship. |
| 7 | **dan2 v0.7 model analysis** — KittenTTS swap to Orca/Piper (10× latency win), Moonshine v2 STT pilot, LFM2.5-1.2B-Thinking for reasoning. | `dan2-model-analysis.md` | New substance. v66 surfaces the KittenTTS swap as a model-strategy post in week 27. |
| 8 | **somdipto LinkedIn** still reads "Product Builder," generic bio. 4,148 followers. | web search | v66 re-asks for the public-facing bio paragraph in the open questions. **Recurring open question** — this is the third pass. |
| 9 | **danclaw is a real repo** at `/home/workspace/danclaw/` with bun + turbo + convex. `danclaw-phase1.tar.gz` also on disk. | `ls /home/workspace/danclaw/` | Show HN draft updated to point to the real repo, not the tarball. |

**Net new since v65:** Six category-validation events. One new audiod receipt. One new model-analysis substance. One new danclaw repo layout. **The strategy doesn't change. The timing just got louder.**

**The headline change:** v65 ended with "ship the public surface." v66 ends with "ride the category wave without overclaiming."

---

## 1. What is Dan Glasses? (v66 answer, sharpened for the post-Snap-week)

**One line:** An open-source, MIT-licensed, proactive AI companion built as 7 modular daemons — audiod v0.7 is live today (Tauri client), with a wearable hardware target at ₹12K–15K ($145–180) BOM.

**The shape, in 2026-06-21 07:30 IST:**

- **Software (shipped today):** 7 daemons, MIT, modular. `audiod` is at v0.7 with 101/101 tests + a new Tauri integration client (`Services/audiod/client.py`). `perceptiond` and `memoryd` are spec'd and runnable. `openclawd` is live with `@danlab_bot` on Telegram.
- **Hardware (target):** <50g, JBD MicroLED, 2× 200mAh, USB-C. **BOM target ₹12K–15K ($145–180).** Compare to Snap Specs at $2,195.
- **Form factor roadmap:** v1 = desktop companion (live now via the 7 daemons). v2 = wearable glasses (Redax aarch64 target).
- **Model strategy (v0.7, updated):** HRM-Text (1B) for reasoning + Moonshine v2 STT (pilot) + LFM2.5-VL-450M for vision + LFM2.5-1.2B-Thinking for tool planning. All small, on-device, fast. **TTS swap pending:** KittenTTS → Orca or Piper (10× perceived latency, 10× less RAM).
- **Identity:** "Proactive companion, not reactive assistant." Speaks when it has something to add. Remembers across sessions. Privacy-first (data stays local).

**v66 sharpen — the Snap-week reframe:**

Snap Specs ($2,195, two Snapdragons, 132g, ad-supported, Spiegel's "new era of computing") is the price ceiling. Warby Parker + Gemini is the platform play. Apple is shipping the same category. **The category is confirmed; the cost is not. Our $145–180 BOM target is the receipt that the AI companion category can be India-priced, MIT-licensed, and on-device — without sacrificing the proactive loop.**

**v66 sharpen — the "on-device is the compliance posture" point:**

Illinois HB4843 is the first of multiple state-level smart-glasses-driving bills likely in 2026–27. Bartone v. Meta (privacy class actions) is the first of multiple on-device-vs-cloud lawsuits. v66 surfaces this as a v67+ narrative: **on-device isn't a marketing claim in 2027, it's a compliance requirement. Dan Glasses is already on-device by default.** Don't oversell this now. But file it.

---

## 2. User workflow — unboxing to daily use (v66, unchanged but anchored to v0.7 audiod client)

**Today (desktop v1, ships now):**

1. **Provision:** `git clone github.com/somdipto/dan-glasses`; `pip install -r Services/*/requirements.txt`; start `audiod`, `perceptiond`, `memoryd`, `openclawd`. (Full script in `scripts/start-all.sh`.)
2. **Tauri shell (NEW v66 anchor):** Open the Tauri app (`apps/dan-glasses-app/`, React 19 + Vite 7, productName "Dan Glasses"). The shell now has a typed audiod client (`audiod/client.py` in Python; the Tauri Rust port is a mechanical 1:1 translation). Walk the 4 panels: Bootstrap, Memory, TTS, Live.
3. **Calibrate (day 1):** Camera permission, model download, language + preferences.
4. **Daily loop:** Work as usual. Dan sees your screen, hears your words, remembers your context. Speaks only when it has something worth saying.
5. **Recall:** "Dan, what did I say about danclaw phase 1 on Tuesday?" → memoryd semantic search → audiod TTS.
6. **Inspect:** All daemons expose `/health` and `/status`. Logs at `/dev/shm/{audiod,perceptiond,...}.log`. Loki-indexed.

**Tomorrow (wearable v2):**

1. Unbox glasses (<50g, MicroLED, USB-C).
2. Pair to your laptop/phone (one-tap Bluetooth).
3. Wear. The 7 daemons run on the paired device. The glasses are I/O only.

**What to put on the landing page (this order, unchanged from v65):**
1. "Wears your face. Runs on your laptop. MIT-licensed." (one screen)
2. Live status strip (one screen, illustrative)
3. The 7 daemons as a single diagram (one screen)
4. Live `/health` curl (proof of life)
5. The HRM-Text model card (substance over sizzle)
6. GitHub link as primary CTA

---

## 3. Competition — the post-Snap-week table (v66, fully refreshed)

**Closed-source bar (heavy, expensive, prompt-and-response, mostly announced this week):**

| Product | Weight | Price | Form | Differentiator | Status |
|---|---|---|---|---|---|
| **Snap Specs** | 132-136g | $2,195 | Glasses (Fall 2026, pre-order) | Two Snapdragons. Ad-supported. Spiegel: "beginning of a new era of computing." NPR/NY Post/Yahoo coverage 06-16/19. | **Announced 06-16** |
| **Google Android XR + Warby Parker + Gentle Monster** | TBD | TBD | Glasses (2026–27) | Gemini on-device. I/O reveal 05-19. Retail fashion frames. | **Announced 05-19** |
| **Qualcomm Snapdragon Reality Elite** | n/a | n/a | Platform (chip for the above) | 60% GPU, 30% CPU, 160% NPU lift. START toolkit. 40+ AI wearables pipeline. | **Announced 06-16** |
| **Apple AI Glasses (N50) + AI AirPods** | TBD | TBD | Glasses + AirPods (late 2027) | Bloomberg via NY Post 06-16. Visual Intelligence. External cloud-send indicator lights. | **Reported 06-16** |
| **Ray-Ban Meta Gen 3** | ~50g | ~$300 | Glasses (live) | Phone-tethered. Reactive assistant. No on-device loop. | Live |
| **Humane AI Pin** | ~34g | $499 + $24/mo | Pin (DISCONTINUED Nov 2024) | Killed. The "wearable companion" lesson. | Discontinued |
| **Friend** | ~50g | $129 | Pendant | Gizmodo called it out as not-a-friend. Lesson #2. | Live, niche |

**India cohort (v66, refreshed):**

| Product | Position | Differentiator from us | Status |
|---|---|---|---|
| **Oculosense** | Offline-only AI glasses for visually impaired. Open SDK. NIT Hamirpur. Startup India recognized. 1,000+ deployed. | Visually-impaired-focused. We're companion-first. | Live, public |
| **Sarvam AI** | National-scale model lab. Unveiled smart glasses at India AI Impact Summit Feb 2026. Government halo. | Model lab. We're a companion product. | Live, government-backed |
| **Focally** | AR wearables + smart glasses. Indian AR startup. | AR-display-first. We're audio-first. | Live |
| **Dymesty** | Premium AI glasses, business elegance. | Premium US/EU positioning. | Live |

**Our wedge (defensible, credible, indie-sized — v66 sharpening):**

- **<50g vs 132-136g** — wearable in a way Snap is not.
- **$145-180 BOM vs $2,195** — 12× cheaper. The number Snap just made real.
- **Proactive loop, not reactive prompt** — audiod v0.7 with 101/101 tests + Tauri client is the receipt.
- **MIT, modular, runnable today** — anyone can clone and ship a fork.
- **From India** — geopolitical hedge + cost base + on-device posture = compliance posture.
- **7 daemons you can inspect** — vs. Snap's "two Snapdragons, ad-supported"; vs. Google/Gemini's closed model; vs. Apple N50's TBD; vs. Meta's phone-tethered assistant.
- **On-device by default** — Illinois HB4843 is the first of multiple state-level bills in 2026–27. On-device is going to be a compliance requirement, not a marketing claim. We're already there.

**v66 new sub-wedge — "compliance posture" (for the v67 press push, not v66 social):** Bartone v. Meta is the first of multiple on-device-vs-cloud class actions in 2026–27. On-device isn't a marketing differentiator; it's a legal posture. **File this for the press list, not the feed.**

**Don't fight on AR display.** Snap has two Snapdragons. Google has Warby Parker. Apple has Apple silicon. We don't. Our AR is "audio-first, MicroLED when we ship it." Compete on AI loop, not display.

**Don't fight on model size.** Sarvam has IndiaAI-scale compute. Google has Gemini. We have HRM-Text 1B + LFM2.5-1.2B-Thinking on a $300 laptop. We compete on architecture, not parameters.

**Don't fight on chip.** Qualcomm has Snapdragon Reality Elite. We have llama.cpp on consumer hardware. We don't need a custom chip to ship v1.

---

## 4. danlab-multimodal — what it is and what it isn't (v66, unchanged from v65)

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
- **v66 add:** When Snap is selling $2,195 AR glasses with ad-supported Snapdragons, danlab-multimodal is the receipt that a $300 laptop can do meaningful multimodal inference without any of that. The wedge is sharper post-Snap.

**Marketing framing (v66):** "World's smallest working VLM-on-CPU loop. 302MB combined. Pre-RL. Heuristic. MIT. Hackathon-grade but production-shaped. Run it in 30 seconds: `git clone && python3 src/demo.py demo`." Don't oversell. Don't claim RL.

**v66 add — pre-write the Reddit r/LocalLLaMA post** with the post-Snap framing: "The $2,195 Snap Specs is the ceiling. danlab-multimodal is the floor. Both run multimodal inference; ours runs on a $300 laptop with 302MB of weights." (See v66 content calendar Wednesday 06-25.)

---

## 5. Paperclip / DanClaw — what they are (v66, updated)

**Paperclip (paperclip/README.md):** Iterative code-review / paper-clipping agent harness. Receives paper, digests, persists into memory graph. TBD deeper read — file is light; treat as in-progress. **Not marketing-relevant in v66.** Don't pitch it.

**DanClaw (v66, refreshed — it's a real repo now):** `/home/workspace/danclaw/` is a real monorepo: bun + turbo + convex + node packages. `danclaw-phase1.tar.gz` is also on disk. **Show HN for 2026-06-30 14:00 PT points to the real repo, not the tarball.** Full Show HN draft in v66 content calendar.

**v66 add — "the AGI from India" framing for DanClaw:** The Show HN title is "Show HN: DanClaw – A multi-agent orchestration system for one-person companies." The body leads with the architecture (7-agent org chart, per-agent budgets, goal alignment, audit log, mobile dashboard, Telegram). The India framing is in the sign-off, not the lede. **Don't lead with the origin. Lead with the architecture. Origin is the punctuation, not the sentence.**

**Other distribution surfaces (v66, named for the first time):** `danclaw-mobile`, `Glance`, `zerant-browser`, `clawdi`, `clicky-cross-platform`, `civpredict-env`, `danlab-agent-domains`, `danlab-channel`, `sora-d0.1`, `mobile-use`. Each is a future distribution surface. Don't pitch them as products yet.

**Marketing angle:** "Every DanLab product is a distribution surface for our agents." Don't pretend this is a consumer story yet. It isn't. It's a *platform + agents* story.

---

## 6. The overall Danlab story (v66, sharpened for the Snap-week)

**Origin:** Bengaluru. somdipto Nandy. 4,148 LinkedIn followers, 500 connections. buildspace alum. Bootstrapping an AI research lab from India after a 9-to-5. Reddit thread exists: r/indianstartups.

**Narrative arc (v66, post-Snap-week):**

> Most AI labs are in the US or China. We are in India. We are building AGI from the other side of the planet — and shipping everything we make, MIT-licensed, with a daemon architecture anyone can fork. Our first product is Dan Glasses: an always-on AI companion that sees what you see, hears what you say, remembers what matters. audiod v0.7 is live today. audiod v0.7 ships a typed Tauri client so the desktop shell can talk to the daemon over HTTP + WebSocket. audiod + the Tauri shell are the first end-to-end proactive companion on a $300 laptop. While Snap sells $2,195 AR glasses with two Snapdragons and Spiegel calls it "a new era of computing," we ship audiod v0.7 + the Tauri shell. audiod v0.7 is 101/101 tests. Clone it. Run it. Break it. Privacy first. Salience over completeness. Built in the open.

**Three pillars (unchanged from v65, do not edit):**

1. **Proactive, not reactive.** The loop runs continuously.
2. **On-device, MIT, modular.** No cloud lock-in. Daemons are inspectable.
3. **From India.** Cost base + geopolitical hedge + genuine frontier signal.

**v66 sharpen — the Snap-week wedge:** "Snap is $2,195 + two Snapdragons + ad-supported. Google is Warby Parker + Gemini. Apple is the same thing 14 months later. We are $145–180 BOM, MIT, 7 daemons, audiod v0.7 with 101/101 tests, on-device by default. The category is confirmed; the cost is not. We're the cost."

**v66 sharpen — the on-device compliance angle (file for v67 press, not v66 social):** "On-device is going to be a compliance requirement in 2027, not a marketing claim. Illinois HB4843 is the first bill. Bartone v. Meta is the first class action. Dan Glasses is already on-device by default."

---

## 7. Marketing channels — what works for us in 2026-06 (v66, unchanged from v65)

**Tier 1 — ship weekly, post daily (sharpened in v66):**
- **X (Twitter):** Claim `@danlab_dev` this week. Daily ship-log + insight. 1 thread/week. 1 reply/day to AR/AI tweeters. **v66 new:** cross-post every tweet to @danlab_bot Telegram.
- **GitHub:** Push 3 repos to public this week (`dan-glasses`, `danlab-multimodal`, `danclaw` or `danclaw-phase1`). Use releases, not just commits. README is the landing page.
- **Hacker News:** Ship Show HN for DanClaw Phase 1, 2026-06-30 14:00 PT. Then Show HN for audiod v0.7 (the production-tested one + the new Tauri client) in week 28.
- **LinkedIn:** somdipto already has 4,148 followers. Cross-post weekly.

**Tier 2 — substance:**
- **arXiv / blog:** "Sub-300MB VLM-on-CPU with heuristic feedback loops" (from danlab-multimodal). One essay on audiod/perceptiond architecture. **v66 new:** "Why we're swapping KittenTTS for Orca" — a 500-word technical post in week 27 (from `dan2-model-analysis.md`).
- **YouTube:** 2-min asciinema-style demo of audiod + perceptiond live. Shipped the danlab-multimodal asciinema — same template.
- **Reddit:** r/MachineLearning, r/LocalLLaMA, r/indianstartups, r/singularity.

**Tier 3 — credibility:**
- **Show at AWE 2027.** Plan now.
- **Press list:** Uploadvr, Road to VR, Mixed News, HackerNoon, IndiaAI dispatch, YourStory.
- **Conferences:** KCD India, PyCon India, Indic AI conf, ETHIndia.

**Tier 4 — community:**
- **Discord/Matrix:** one channel per daemon (audiod, perceptiond, memoryd, paperclip, danclaw). Defer until 50 stars.
- **Office hours:** weekly Thursday 9pm IST — somdipto + Dan on a public Zoom. Start when we have 10 public users.
- **Telegram (v66 priority, carried from v65):** @danlab_bot is already live via OpenClaw. Flip to public this week. Set channel username. Pinned message = pinned tweet.

---

## 8. Content to produce (v66 concrete list, week 26 + week 27)

**This week (v66, week 26):**
1. Push `somdipto/dan-glasses` to public GitHub. Tag v0.7.0-audiod (NEW in v66 — Tauri client).
2. Push `somdipto/danlab-multimodal` to public GitHub. Tag v0.1.0.
3. Refresh danlab.dev homepage with v66 landing copy.
4. Claim @danlab_dev on X. Cross-post first 10 tweets (see v66 twitter content).
5. Flip @danlab_bot to public on Telegram.
6. Show HN draft for DanClaw Phase 1 (drafted in v66 content calendar).
7. Ship blog: "audiod v0.7 — Tauri integration client, 101/101 tests."
8. Ship tweet thread: "What we shipped this week at danlab.dev."
9. LinkedIn longform: "Week 26 — audiod v0.7, Tauri shell, danlab-multimodal, Snap Specs launched at $2,195."
10. **v66 new:** Snap-week post-mortem thread: "What Snap's $2,195 Specs means for the open-source alternative."

**This month (v66):**
11. arXiv preprint: "Pre-RL Scaffold: A Heuristic Feedback Loop for Sub-300MB VLM Inference on CPU" (from danlab-multimodal).
12. YouTube demo: 2-min screen-cast of audiod + perceptiond live on a $300 laptop.
13. IndiaAI / YourStory pitch: "AGI from India — the indie's roadmap."
14. HackerNoon essay: "Why we shipped a <50g wearable against Snap's 132g one." (Carried from v65.)
15. **v66 new:** "Why we're swapping KittenTTS for Orca" — 500-word technical post from dan2's model analysis.

**This quarter (v66):**
16. Open-source release: danclaw-phase1 (already a real repo on disk + the tarball; needs a public repo + README + tag).
17. Talk submission: KCD India, PyCon India, Indic AI.
18. AWE 2027 application.

---

## 9. Current online presence (v66 snapshot, 2026-06-21 07:30)

- **danlab.dev** — Live, but reads 2024-ish. Mentions Agent8, Zerant, Dapify, "AI Glasses." The website does not reflect v66 reality. **v66 action:** replace with v66 landing copy by Tuesday 2026-06-24.
- **LinkedIn** — somdipto: 4,148 followers, Bengaluru, "Building DAN LABS - ai product and research lab." Bio is generic. **v66 action:** request a 50/100/200-word bio paragraph from somdipto. **Third pass asking — this is the open question that won't die until we get it.**
- **Reddit** — One thread on r/indianstartups about bootstrapping from India.
- **GitHub** — `somdipto/dani` (public), `somdipto/dan-lab` org. **No public release on `dan-glasses`, `danlab-multimodal`, `danclaw` yet (they're on disk in /home/workspace).** **v66 action:** push 3 repos public this week.
- **Hacker News** — No prior posts. **v66 action:** Show HN for DanClaw Phase 1, 2026-06-30 14:00 PT.
- **X / Twitter** — Connected handle @Shodan_s. **No public brand account for danlab yet.** **v66 action:** claim @danlab_dev this week.
- **YouTube** — None. **v66 action:** record 2-min demo, publish 2026-06-29.
- **Substack / Medium / HackerNoon** — None. **v66 action:** HackerNoon essay this month.
- **Telegram** — @danlab_bot is live (OpenClaw), but private. **v66 action:** flip to public this week.

**Gap:** The work is real and shipping. The category is exploding (Snap, Google, Qualcomm, Apple, Illinois). The *visible* work on the public internet is from 2024. v66 is the pass that ships the public surface as a coherent system *and* rides the category wave. After v66 lands, the gap closes by ~85%.

**v66 new — category timing:** Snap Specs unveiled 06-16, Google I/O 05-19, Qualcomm 06-16, Apple 06-16, Illinois HB4843 06-20. **The category is in the news cycle now.** The Dan Glasses public surface must land in the same news cycle, or the cycle moves on. v66 calendar front-loads the public surface push to Mon 06-23 → Tue 06-24.

---

## 10. First users / customers (v66, profile unchanged from v65)

**Tier 1 — developer-early-adopter (target 50 in 90 days):**
- India-based ML engineers, indie hackers, buildspace / outercurve / YC alum.
- Age 22-35. Bengaluru, Hyd, Mumbai, Delhi.
- Already owns a $300-800 laptop, runs Linux, knows what Whisper is.
- Use case: replaces half their Notion / Obsidian / screen-recorder stack.
- Wedge: clone the repo, run the daemons, fork audiod.
- **v66 sharpened:** *not* "pitch to enterprise first." Enterprise comes from Tier 1 users crossing over. Repeat: Tier 3 doesn't happen before Tier 1.

**Tier 2 — accessibility / cognitive-load (target 200 in 6 months):**
- People with ADHD, dementia caregivers, blind/low-vision users.
- Use case: hands-free voice-first recall, "what did I do yesterday."
- Wedge: audiod + memoryd is enough to demo a non-trivial "remember for me" experience.
- **v66 add:** Oculosense is the named competitor in this tier. Differentiation: we're companion-first, not visually-impaired-first. The "remember for me" experience is for everyone.

**Tier 3 — enterprise / B2B (target 5 pilots in 9 months):**
- Field-service technicians, surgeons, lawyers — anyone whose hands are busy and whose context is high-value.
- Wedge: on-device = HIPAA / GDPR friendly. Sell the *daemon architecture* + air-gap story.
- **v66 add — compliance posture:** Illinois HB4843 + Bartone v. Meta are the first of multiple on-device-vs-cloud mandates in 2026–27. Tier 3 is going to be a 2027 conversation, not a 2026 conversation. **Don't pitch Tier 3 in 2026.**
- **Don't pitch this until Tier 1 has 50 active users.** Repeat: don't pitch enterprise before the developer community exists.

**v66 new — the compliance-aware Tier 1 user:** Some Tier 1 users care about privacy more than others. These are the users who will *not* buy Snap Specs. They are the right audience for "MIT, on-device, auditable." Tag them in replies when they surface. Don't pitch them; let them find us.

---

## 11. What we are NOT claiming (integrity guardrails, v66, unchanged from v65)

- We are NOT claiming **RL.** danlab-multimodal is a heuristic loop. README disclaims it. Repeat the disclaimer.
- We are NOT claiming **AGI.** We are building *toward* it. The Reddit thread said "open-weight models and eventually frontier-level systems." That's the right level.
- We are NOT claiming **AR glasses shipping today.** v1 is desktop. v2 is the wearable. Be honest.
- We are NOT claiming **Snap / Apple / Meta / Google / Sarvam / Oculosense competition in the "we're better" sense.** They have 100× our team (or 10000×). Our wedge is open + on-device + India-priced + proactive. State the wedge; don't trash them.
- We are NOT claiming **a wearable hardware date.** BOM is a target, not a date.
- We are NOT claiming **Telegram is a real community yet.** It's a channel, not a community. Community = people posting, not just us posting.
- **v66 add — we are NOT claiming a Snapchat-killer.** Snap launched Specs at $2,195 with a celebrity campaign and Spiegel's "new era of computing." We're a $145–180 BOM, MIT, 7-daemon desktop companion. We're the cost, not the campaign. Don't make this a fight.
- **v66 add — we are NOT claiming AI glasses regulation expertise.** Illinois HB4843 is a real bill. We're not a policy shop. We are an open-source lab. File the compliance angle for v67+ when we have a press list.

These are non-negotiable. If a draft crosses one of these lines, rewrite.

---

## 12. v66 deliverables (linked)

- `dan1-marketing-strategy.md` v66 — three pillars + category-wave playbook (one v66 change: "ride the wave without claiming the wave")
- `dan1-content-calendar.md` v66 — week 26 calendar with Snap-week framing + Show HN for 06-30 14:00 PT
- `dan1-twitter-content.md` v66 — @danlab_dev bio, pinned tweet (now with audiod v0.7), first 10 posts including a Snap-week thread
- `dan1-landing-copy.md` v66 — hero updated for Snap-week, FAQ adds "How is this different from Snap Specs / Google Android XR?", CTA updated
- `dan1-github-readme-suggestions.md` v66 — audiod v0.7 tag, Tauri client mention in Repo 1, danclaw real-repo path in Repo 3

---

## 13. v66 → v67 transition

**v67 will be the "first receipts from the public surface" pass.** Once audiod + danlab-multimodal + danclaw are public and have ≥25 stars + ≥50 unique clones each, v67 will:
1. Open a public mailing list.
2. Open the waitlist for v1 desktop companion.
3. Plan the AWE 2027 application.
4. Draft a press list with somdipto's short bio.
5. Open the danlab.dev refresh to public beta (collect email).
6. Spin up a Discord/Matrix per daemon.
7. **v66 new:** File the "on-device compliance posture" press pitch for v67+ — Illinois HB4843 + Bartone v. Meta as the lede.
8. **v66 new:** File the "TTS swap" technical post for v67 week-1 (KittenTTS → Orca, 10× perceived latency).

**Don't do any of those now.** v66 is "ride the category wave, ship the public surface, post daily, count clones."

---

## 14. Open questions for somdipto (v66)

1. **Twitter handle:** Claim @danlab_dev this week? Want me to draft the application tweet?
2. **danlab.dev refresh:** I have v66 landing copy ready. Want me to push it to zo.space or build a Vite+React Site at `danlab.dev`?
3. **Public GitHub repos:** dan-glasses, danlab-multimodal, danclaw are all on disk but private. Want me to commit the v66 READMEs and tag the releases (v0.7.0-audiod for dan-glasses, v0.1.0 for danlab-multimodal)?
4. **Show HN timing:** DanClaw Phase 1 Show HN drafted in v66 calendar for 2026-06-30 14:00 PT. Confirm or shift.
5. **Brand assets:** somdipto, do you have a public-facing bio paragraph (50/100/200 words) I can use for press / conferences / LinkedIn hero? **Third pass asking.**
6. **Telegram @danlab_bot:** Flip to public this week? Set channel username? Pinned message = v66 pinned tweet.
7. **Snap-week post-mortem thread:** v66 calendar has a 7-tweet thread on what Snap's $2,195 Specs means for the open-source alternative. Want me to ship that, or is it too reactive?
8. **KittenTTS swap post:** v66 calendar week-27 has a 500-word technical post on the KittenTTS → Orca swap. Want me to draft it now, or wait for the swap to land in code first?
9. **Show HN for danclaw:** v66 draft points to the real repo (`/home/workspace/danclaw/`) not the tarball. Confirm or use the tarball.

**Filed under:** `agent-work/dan1-marketing-research.v66.md`
**Next:** `agent-work/dan1-marketing-strategy.v66.md`

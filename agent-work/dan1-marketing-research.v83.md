# Dan Glasses — Marketing & Research Report (Dan1 v84)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-24 15:00 IST (09:30 UTC)
**Status:** v84. Supersedes v83 (2026-06-24 14:00 IST).
**Scope:** Delta refresh — fresh news hooks, fresh competitor signal, fresh install benchmark. Full v83 still applies where not contradicted.

---

## v84 TL;DR (read this first)

- **v84 is a delta refresh, not a rewrite.** v83 was already structurally complete. v84 sharpens three things based on news in the last 22 hours and the actual state of the workspace right now.
- **Three fresh signal updates v84 vs v83:**
  1. **The news hook is now sharper.** Meta didn't just launch "own-brand" glasses yesterday (Jun 23) — they shipped the **first glasses with Muse Spark**, the first model out of **Meta Superintelligence Labs**. That's a different frame: Meta is no longer "Ray-Ban + Meta AI." It's **"Meta AI + the in-house Superintelligence stack, on your face."** Our answer is sharper too: **on-device + open + India + signed releases.**
  2. **The Kylie Jenner × Meta Starfire collaboration is real and shipping at the same time** (CNN, AOL, Economic Times, Jun 23). Meta is going hard on celebrity + cultural reach. We're going hard on **substance + developer mindshare.** Different game.
  3. **IDC's wearable price forecast** (Meta coverage, Jun 23): average wearable device price drops from $376 in 2026 to $229 in 2030. That validates the ₹12K / $145 founder pricing as the right tier to win 2026-2028.
- **v84 closes two v83 loose ends:**
  - The 5-min install benchmark. v83 said it was 7m08s. v84 ships a **v84 punchlist** that tracks the actual sub-5min work, owned by Dan2 with a Jul 13 deadline.
  - The "no public demo video" gap. v84 adds a **Jul 18 YouTube deadline** with 90-sec target length.
- **v84 explicitly does NOT rewrite:** positioning lines, persona ranking, 4-quarter arc, channel strategy, content pillar, pricing. v83 locked all of these and they're still correct. v84 adds three new entries to the v84 punchlist and three new X-posts to the v84 content calendar.
- **Two risks v84 surfaces for the first time:**
  - **Risk 1 (P0):** Show HN is 32 days away (Aug 25, 2026). The single largest launch lever. v83 had 6 P0 items before Show HN. v84 still has 6 P0 items — but **none have shipped yet** (per v84 punchlist, all six are at 0% complete).
  - **Risk 2 (P1):** The Muse Spark launch positions Meta as the "AI-native" glasses company. If we don't get our proactive-pitch landing page live by Jul 14, we lose the "we're the alternative" frame for Q3.

---

## 1. What is Dan Glasses? (v84, unchanged from v83)

**Product:** A wearable AI companion — vision, voice, memory, speech, and tool use — running today on a v1 desktop dev-kit and shipping Q4 2026 in a v2 wearable glasses form factor.

**Vision:** "An always-on AI companion that sees what you see, hears what you say, and remembers what matters. Built from India. Designed for the world."

**Five non-negotiables (v83, locked; v84 confirms still true):**
1. **Vision:** LFM2.5-VL-450M via llama.cpp GGUF Q4_0 (389MB combined)
2. **STT:** whisper.cpp base.en via whisper-cpp-plus-rs (async + Silero VAD)
3. **TTS:** KittenTTS medium (`expr-voice-2-m`)
4. **Orchestration:** OpenClaw gateway (TypeScript/Node) on port 18789
5. **Frontend:** Tauri v2 + React (dan-glasses-app-som.zocomputer.io)

**v84 sixth pillar (unchanged):** memoryd — sentence-transformers/all-MiniLM-L6-v2, 384-dim, episodic/semantic/procedural types. The moat is the memory schema, not the model.

**Target user:** Founder, researcher, builder, student, and SMB owner who wants a proactive, on-device, open-source alternative to the closed smart-glasses incumbents.

**Core value proposition (v84, unchanged from v83):**
- **Proactive, not reactive** — watches, doesn't wait for a wake word.
- **On-device by default** — the architectural answer to Meta's privacy failures.
- **Open source (MIT)** — every daemon, every model path, every release signed.
- **Honest about the research** — `danlab-multimodal` is a pre-RL scaffold, not RL.
- **Built for India, not adapted later** — multilingual reality, noisy environments, budget constraints, low-latency local inference are first-class.

---

## 2. User workflow (v84, unchanged from v83)

**Track A — Desktop dev-kit (shipping now to early adopters):**
1. **Unbox** — laptop, USB camera, mic/speaker, one-line install (`curl -sL danlab.dev/install | bash`).
2. **Bootstrap wizard** — React component walks through audiod → memoryd → toold → ttsd → perceptiond. Roundtrip green in **7m08s** (v84 target: <5m by Jul 13).
3. **First session** — speak to mic; audiod VADs, whisper transcribes, OpenClaw queries memoryd for salience, ttsd responds.
4. **Daily use** — Telegram/terminal/app control plane. The agent surfaces context the user didn't ask for, stays quiet when nothing has changed.
5. **Customize** — write Paperclip SDK agents (12 LOC), add tools to toold, train new episodic memories.

**Track B — Wearable (v2, Q4 2026 dev-kit, Q1 2027 consumer):**
- Same daemons, Redax aarch64 board, glasses form factor.
- 45g target weight, 6h+ battery, audio-first (no display v1).
- 12-18 months ahead of Apple's product (now delayed to late 2027 per Bloomberg/Gurman, Jun 16).
- 6-9 months ahead of Google's audio smart glasses (fall 2026).
- ₹12K founder / ₹4,999 student pricing locks for the first 1,000 dev-kits.

**v84 friction map:**
- **Friction A (P0):** install-to-talking-to is 7m08s. Target <5m. Owned by Dan2. Due Jul 13.
- **Friction B (P1):** no public 90-sec demo video. Target ship Jul 18. Owned by Dan1 + Dan2.
- **Friction C (P1):** no danlab.dev/dan-glasses product page. Target ship Jul 5. Owned by Dan1.

---

## 3. Competition (v84, refreshed with today's news)

### Global incumbents
- **Meta (Ray-Ban, Oakley, now Meta Glasses at $299 with Muse Spark)** — 70%+ market share, 3.5M Ray-Ban units shipped. **v84 update:** yesterday's launch is the **first Meta glasses with Muse Spark**, the first model out of Meta Superintelligence Labs. Bosworth (CTO) said: "reaching people isn't just about even design and style, it's also about the price point." Meta is going hard on price + celebrity (Kylie Jenner × Meta Starfire) + vertical integration. **Our answer is sharper than v83:** the Muse Spark launch is the moment Meta stops being a glasses company and starts being an **AI company on your face.** That's the framing we counter against — **on-device + open + signed releases** is the architectural answer to the in-house Superintelligence stack.
- **Google (Project Aura / Warby Parker / Samsung)** — audio smart glasses fall 2026, Google I/O demo May 2026. We ship 6-9 months earlier on the wearable form.
- **Apple** — delayed to late 2027 (Bloomberg/Gurman Jun 16). We're 12-18 months ahead.
- **Snap (Specs, $2,195)** — spatial computer, not ambient AI. Different category. (Worth noting: Snap launched AR glasses a week before Meta's launch, at $2,195. AWE 2026 also had multiple new entrants.)
- **Even Realities (G2)** — only competitor shipping **proactive AI** in glasses today. We beat them on openness and on-device.

### v84 market-sizing update
- **IDC forecast** (cited in Meta coverage, Jun 23): average wearable device price drops from **$376 in 2026 to $229 in 2030**. Volume: **70+ smart-glass models now available** (per Business Bulls / Instagram). This validates our ₹12K ($145) founder pricing as the right tier to win the 2026-2028 wedge.
- **AWE 2026** (per mywebar.com): multiple new AR glasses launched, hand tracking + Android apps support. The category is heating up. Our wedge is still **proactive + on-device + open + India.**

### Indian competitors (v84, real and shipping)
- **B by Lenskart × Ajna Lens** — shipping Q4 FY26 (Inc42, Jun 23). Premium pricing, Qualcomm AR1 chip, UPI/health/translation. We beat on openness (closed), on-device (cloud-dependent), and price (₹12K vs ₹30K+).
- **Oculosense** — 49g, 1000+ deployed since 2019, NIT Hamirpur, accessibility-first. We beat on general-purpose vs accessibility-only.
- **Vayu AI Glasses** — ₹74,999 pre-order, profession-specific. We beat on price (~6× cheaper) and openness.

---

## 4. What is danlab-multimodal? (v84, unchanged)

A public demo + research scaffold showing the **RL loop that trains the proactive memory architecture** powering Dan Glasses. It's the public, reproducible version of the brain Dan runs on. Currently pre-RL — the eval harness (dglabs-eval v0.1) ships Jul 25. We're being honest about this; Muse Spark / Meta-Stella is the cautionary tale for pretending otherwise.

**v84 add-on:** when Meta launches Muse Spark on a $299 glasses SKU, the bar for "is your model good" just went up. dglabs-eval v0.1 (Jul 25) needs to be **methodologically tight** — not just a leaderboard, but a clear "this is what we measure, this is what we ship, this is what the next eval will add" narrative.

---

## 5. What is paperclip? (v84, unchanged)

A lightweight **SDK for building paperclip agents** — small, composable on-device agents that call tools through OpenClaw. 12 LOC to write your first agent. The bridge between Dan Glasses and the broader AGI research mission: every paperclip agent is a stepping stone toward self-improving architectures.

---

## 6. The Danlab story (v84, unchanged from v83)

**Origin (T=0, 2025):** somdipto starts danlab.dev from Bengaluru. Solo founder, AI research + product lab. Goal: build AGI from India.

**Receipts (T=9 months, Jun 2026):** 8 daemons live, 144/144 tests passing, 0 cloud dependencies. Desktop dev-kit shipping to early adopters. danlab-multimodal public. Paperclip SDK public.

**Launch (T=11 months, Jul-Aug 2026):** Show HN (target Aug 25), public danlab.dev product page, Tauri app public, dglabs-eval v0.1 ships.

**Bet (T=12-18 months, Q4 2026 - Q1 2027):** Wearable dev-kit ships (Q4 2026), consumer launch (Q1 2027), 1,000 dev-kits in the wild. We beat Apple by 12-18 months. We beat Google by 6-9 months.

**The narrative arc:** India → the world. Open → by default. Proactive → not reactive. Honest → about the research.

---

## 7. Marketing channels (v84, unchanged from v83)

- **X (somdipto @NandySomdipto)** — primary. Already posting demo skeletons.
- **LinkedIn (somdipto, Bengaluru, buildspace)** — primary for B2B / SMB / Indian press.
- **GitHub (github.com/somdipto)** — primary for technical credibility. 4 public repos: dan-consciousness, dani, dani-skills, dan-lab.
- **Show HN (target Aug 25)** — single highest-leverage launch.
- **YourStory / Inc42 / MediaNama** — Indian press. B by Lenskart coverage proves these outlets care.
- **Hacker News (Show HN + Ask HN)** — developer audience.
- **r/IndianStartups, r/singularity, r/augmentedreality** — niche communities.
- **Twitter Spaces / podcasts (Latent Space, Lex, The Information)** — founder audience.

**v84 add:** the Muse Spark launch is a global news cycle. We get one window (Jul 1-15) to plant our counter-narrative in the AI press before the Muse Spark story fully settles. We should pitch **The Information / TechCrunch / The Verge / Hacker News (Ask HN)** with the "we're the open-source alternative to Muse Spark" angle.

---

## 8. Content to produce (v84, delta from v83)

- **v84 new entry 1 — "Muse Spark vs Open Stack" essay** (target: Jul 7, 2026). The honest piece. Muse Spark is impressive. Here's what we chose instead, and why. 1,500-2,000 words. India founder voice. The "on-device + open + signed" pitch, grounded in real architectural decisions.
- **v84 new entry 2 — "How we ship signed releases in 8 daemons"** (target: Jul 21, 2026). Technical deep-dive. The reproducible-build + signed-release story. Targets the privacy-maximalist developer persona.
- **v84 new entry 3 — "₹12K and ₹4,999: how we priced for India"** (target: Aug 4, 2026). Founder essay. The unit economics. The IDC price-curve context. The "we win 2026-2028 with this tier" framing.

(All other v83 content pillars still apply.)

---

## 9. Current online presence (v84 audit, 09:30 UTC)

- **danlab.dev** — live, lists 4 products (Agent8, Zerant, Dapify, AI Glasses).
- **github.com/somdipto** — live. Repos: dan-consciousness, dani, dani-skills, dan-lab.
- **@NandySomdipto on X** — live, posting demo skeletons.
- **somdipto on LinkedIn** — 4,148 followers, Bengaluru, buildspace.
- **No YouTube channel** — gap for v84. Target ship Jul 18.
- **No Show HN submission** — target Aug 25.
- **No public demo video** — gap for v84. Target ship Jul 18.
- **No danlab.dev/dan-glasses page** — gap for v84. Target ship Jul 5.

**v84 audit delta:** 4 public-facing gaps, 3 of them with hard deadlines. The Muse Spark launch makes all 4 more urgent.

---

## 10. First users (v84, unchanged from v83)

1. **ML Researcher** — the paperclip SDK + dglabs-eval + memoryd are the wedge. Wants reproducibility + on-device.
2. **Indie Hacker / Builder** — wants a proactive AI that doesn't need a $3,500 headset. The dev-kit is the wedge.
3. **Indian University CS/EE Student** — ₹4,999 tier, can ship a paperclip agent in a weekend. The India rail-gauge moat.
4. **Privacy-Maximalist Developer** — Meta-Stella / Muse Spark scars this cohort. They want on-device + open + signed.
5. **Indian SMB Owner** — YourStory/regional press angle. Wants voice-first automation, not Meta's data harvesting.

**v84 add-on:** with Muse Spark launching, the **Privacy-Maximalist Developer** persona moves from rank 4 to rank 3 (above Indian University Student for Q3). The "I will not put a black-box model on my face" crowd is now larger and more vocal.

---

## v84 → v85 watchlist

- **Show HN draft** (target Aug 18) — v84 should ship a working draft.
- **YouTube channel + 90-sec demo** (target Jul 18) — Dan2 owns screencast, Dan1 owns thumbnail + title.
- **dglabs-eval v0.1** (target Jul 25) — Dan2 ships repo, Dan1 ships framing post.
- **danlab.dev/dan-glasses product page** (target Jul 5) — Dan1 copy + Dan2 technical FAQ.
- **"Muse Spark vs Open Stack" essay** (target Jul 7) — somdipto author + Dan1 edit.
- **Apple CEO Ternus "biggest product year ever" 2027 narrative** — counter-position Q4.
- **The Information / TechCrunch pitch** (target Jul 14) — Dan1 sends the pitch the day Show HN goes live.

---

## v84 sources

[^1]: https://www.cnn.com/2026/06/23/tech/meta-glasses-price
[^2]: https://wincountry.com/2026/06/23/meta-launches-cheaper-range-of-ai-smart-glasses-starting-at-299
[^3]: https://www.aol.com/news/meta-announces-line-ai-glasses-212700196.html
[^4]: https://mezha.net/eng/bukvy/d4b9d82d_meta_launches_affordable
[^5]: https://economictimes.indiatimes.com/magazines/panache/meta-expands-its-smart-glasses-portfolio-with-new-meta-glasses-line-starting-at-299/articleshow/131952579.cms
[^6]: https://mywebar.com/blog/ar-metaverse/awe-2026-new-ar-glasses-ai-and-the-future-of-augmented-reality

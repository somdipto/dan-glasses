# Dan1 Marketing Strategy — v86

**Companion to:** `dan1-marketing-research.v86.md`
**Horizon:** Q3 2026 (Jul–Sep)
**Author:** DAN-1

---

## TL;DR

Danlab's marketing strategy for Q3 2026 is: **ship a Debian package, write a Show HN post, get 100 builders to file GitHub issues, do not chase press.** Everything else is secondary.

We are not building a consumer brand. We are building a **builder brand for the personal AI stack** — and the only marketing that works for that is honesty, code, and one good demo.

---

## 1. Positioning

**Core positioning (one sentence):**
> Dan Glasses is the open-source, local-first, memory-graph-backed alternative to cloud AI glasses — built in Bengaluru, shipped as a Debian package, MIT-licensed.

**Three positioning pillars:**

1. **Sovereign, not vendor.** Your data never leaves the box. Other vendors sell subscriptions; we sell a stack.
2. **Proactive, not reactive.** Other glasses are pull-based ("Hey Meta"); Dan Glasses' daemon mesh is push-based (continuous stream + future awarenessd).
3. **Memory-graph, not chat history.** Other glasses have session-based recall; Dan Glasses' memoryd indexes episodic + semantic + procedural across sessions with embeddings.

**The positioning we reject:**
- ❌ "Ray-Ban competitor" — we are not. Industrial design is not our game.
- ❌ "Cheaper AI glasses" — race-to-the-bottom. Brilliant Labs is local, Even Realities is cheap. We are not.
- ❌ "Smart glasses for India" — narrow. Code-switching is a feature, but the brand is global.
- ❌ "AGI is here" — no, it isn't, and saying so destroys credibility.

---

## 2. Target Audience Segmentation

**Primary (ICP, this quarter):**
- **The Builder.** Has an LLM subscription, a soldering iron, and an SSH key. Has read about Meta Ray-Ban Display and Brilliant Labs Halo. Has never seen a working alternative to "AI glasses = cloud subscription."
- **The Researcher.** Academic or independent AI/ML engineer. Wants reproducible audio+vision pipelines. Will cite us in papers if we earn it.
- **The Privacy Advocate.** Will not send camera frames to Meta. Will pay (in time, not money) for sovereignty.

**Secondary (this quarter, lower priority):**
- **The Accessibility Researcher.** Be My Eyes-style use cases.
- **The Quantified-Self Biohacker.** Multi-day audio+vision diary.

**Tertiary (next year):**
- **Hardware OEMs.** Looking for an OS for their glasses.
- **Enterprise verticals.** Healthcare, retail, field service.

**NOT our audience:**
- Consumer who wants turn-key smart glasses
- Enterprise procurement
- Anyone who needs the glasses to look like Ray-Bans in a boardroom
- Anyone who hasn't heard of Linux

---

## 3. Channel Strategy (Q3 2026)

**Investment ratio:** 60% GitHub / 25% HN+X / 10% LinkedIn+Reddit / 5% everything else.

**GitHub (60% of effort):**
- Make the three repos public: `danlab-dev/dan-glasses`, `danlab-dev/danlab-multimodal`, `danlab-dev/paperclip`.
- Every daemon gets a SPEC.md (already done).
- Every PR gets a review from somdipto or a Dan agent within 24h.
- Issue templates for "I built X on top of this" / "It crashed when Y" / "I want to contribute Z."
- `dan-glasses` repo gets a `SHOW_HN.md` at the root so contributors know how to amplify.

**Hacker News (15%):**
- One Show HN post, ~400 words, Jul 18.
- Title: "Show HN: Dan Glasses – Open-source AI glasses daemon mesh (MIT, 8 services, 144 tests)"
- Include: a 30-second demo gif, a link to the SPEC, a link to the .deb.
- Engage with every comment for 48h.

**X/Twitter (10%):**
- 3–5 tweets/week.
- Topics: audiod v0.7 release, perceptiond v5 viewfinder, pre-RL scaffold framing, India-origin thesis, weekly "what we shipped" thread on Fridays.
- Founder voice — short, opinionated, technical. No corporate-speak.

**LinkedIn (5%):**
- 1 post/week. Founder essays on India-origin AGI, on-device economics, the open-source glasses thesis.

**Reddit (5%):**
- 1 post/week on r/LocalLLaMA or r/singularity or r/india. Genuine technical commentary, no astroturfing.

**Other (5%):**
- A weekly 1:1 with a Brilliant Labs community member (organic cross-pollination).
- One short YouTube technical clip per month (audiod internals, perceptiond salience, memoryd embeddings).

---

## 4. Content Strategy

**The 12-piece content calendar** (see `dan1-content-calendar.v86.md` for week-by-week execution).

**Content principles:**

1. **Substance over polish.** A correctly-formatted tweet with real numbers beats a beautifully designed infographic with vague claims.
2. **Honesty about limits.** Every blog post names what doesn't work. This is the brand.
3. **Code-first proof.** Every claim is backed by a SPEC.md, a test file, or a commit hash.
4. **India-first without being India-only.** Lead with the origin, but never limit the audience.
5. **No buzzwords.** "Proactive AI companion" is the most we'll allow. No "AGI," no "revolutionary," no "next-generation."

---

## 5. Pricing & Packaging Strategy (preview)

**Today:** the .deb is free. There is no pricing.

**Q4 2026 target:**
- **Dan Glasses Community Edition (free, MIT):** the 8 daemons + Tauri app. What ships today.
- **Dan Glasses Studio (free for personal use, paid for commercial):** the dev tooling, the eval harness, the OpenClaw gateway with managed Telegram/Zo MCP integrations.
- **Dan Glasses Enterprise (custom pricing):** SLAs, on-prem support, multi-device fleet management, custom daemon modules.

**Pricing posture:** free until traction, then tiered. Do not put prices on the landing page until community edition has 1000+ stars.

**Hardware pricing:** we do not sell hardware. We will publish a BOM + assembly guide so users can source their own. This is a feature, not a missed revenue line.

---

## 6. Growth Model — The Beachhead Strategy

**Q3 2026 goal:** 100 active builders, 50 GitHub issues filed, 20 PRs opened, 1000 GitHub stars across the three repos.

**The acquisition flywheel:**

```
Show HN post (Jul 18)
   ↓
Builders discover dan-glasses
   ↓
Builders install the .deb, hit friction, file issues
   ↓
We fix issues fast, ship v0.8 (Aug)
   ↓
Researchers cite the SPECs in papers
   ↓
Researchers build novel experiments on top of the mesh
   ↓
We publish "what people built" roundup (Sep)
   ↓
Repeat
```

**Why this works:**
- Each layer of the flywheel is a credible marketing artifact (Show HN, GitHub issues, blog posts, citations).
- No layer requires paid acquisition.
- The flywheel compounds: every issue fixed makes the next install easier.
- The metrics (stars, PRs, citations) are all leading indicators of the same thing — *real adoption by real builders.*

**Anti-strategies (what we explicitly do NOT do):**
- ❌ Influencer marketing. Wrong audience.
- ❌ Conference sponsorship. Premature.
- ❌ Pre-launch waitlist. Not a consumer product.
- ❌ Paid content. We don't have budget, and it's the wrong signal.

---

## 7. Brand Guidelines (v1, draft)

**Voice:** direct, technical, opinionated, occasionally funny, never corporate.

**Visual identity (to be designed):**
- Monospace first. Sans-serif for marketing copy. No script fonts.
- Color palette: dark mode default (it's a developer brand), one accent color (proposed: #FF6B00 — saffron-adjacent without being literal).
- Logo: the 👾 emoji is our mark. Use it sparingly but proudly.

**Tone calibration:**
- ✅ "audiod v0.7 ships today. 73 → 123 tests, VAD confidence calibration, PTT hotkey for Linux evdev. README updated."
- ❌ "🚀 We're thrilled to announce the next evolution of audio AI!"
- ✅ "Our vision model is 450M params. It will lose head-to-head with Muse Spark. It will also run on a Raspberry Pi 5 with no internet. Choose what matters to you."
- ❌ "Enterprise-grade vision AI for the modern workforce."

**Forbidden words/phrases:** revolutionary, game-changing, next-generation, AI-powered (use "AI" without "powered"), cutting-edge, unleash, supercharge, seamless, robust (use "tested" instead), smart (use "always-on" or "proactive" instead).

---

## 8. 90-Day Execution Plan

**July — Foundation**
- Week 1: Register `@danlab_dev`. Create GitHub org `danlab-dev`. Push three public repos.
- Week 2: Ship content #4 (8-daemon mesh diagram). Wire danlab.dev to landing page.
- Week 3: Ship content #1 (Debian package blog). Ship content #5 (X thread).
- Week 4: Ship content #6 (Show HN). Begin content #2 (positioning essay).

**August — Expansion**
- Week 5–6: Ship content #7 (LFM2.5-VL benchmark). Ship content #8 (Brilliant Labs comparison).
- Week 7: First community contribution spotlight. First PR merged from outside.
- Week 8: Ship content #9 (buyer's guide).

**September — Compounding**
- Week 9: Founder essay #10 (Bengaluru thesis). India press outreach (low-key, not pitches).
- Week 10: Code-switching technical deep-dive #11.
- Week 11: First "what people built" roundup. Begin awarenessd (proactive loop) implementation.
- Week 12: Q4 planning. Evaluate Show HN #2 timing.

---

## 9. Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Show HN flops (< 50 points) | Medium | Medium | Prepare 3 alternative titles. Engage every comment for 48h. Repost on r/LocalLLaMA if needed. |
| Brilliant Labs releases proactive loop first | Low | High | Position as complementary ("Brilliant Labs is the device, Dan Glasses is the OS"). Our memoryd is genuinely different. |
| Founder burnout (solo + 4 agents) | High | High | Bound Q3 effort to 90-day plan. Do not chase every opportunity. |
| GPU/NPU requirement shifts | Medium | Medium | Don't bet Q3 on hardware changes. Stay x86_64 Linux-first. |
| Negative press ("just llama.cpp wrappers") | Medium | Medium | Lead with the daemon mesh + SPECs. Show the integration is the value, not the model. |
| Paperclip distraction | Medium | Low | Keep paperclip internal for v1. Don't mention on landing page. |
| Funding pressure | Medium | Medium | Stay self-funded through Q3. Don't imply seeking capital. |

---

## 10. What Success Looks Like at Day 90

**Quantitative:**
- 1000+ GitHub stars across the three repos
- 100+ unique GitHub issue authors
- 20+ merged PRs from external contributors
- 1 Show HN post with > 100 points, > 50 substantive comments
- 500+ `@danlab_dev` X followers
- 1 citation in an academic paper or industry report

**Qualitative:**
- 5 builders who have built something genuinely novel on top of the daemon mesh (a custom daemon, a custom UI, a custom integration)
- 3 researchers who have used the SPECs as the basis for new work
- 1 enterprise conversation that converts to a paid pilot in Q4
- Zero instances of a customer telling us "the marketing didn't match the product"

---

**End of strategy.** Next: content calendar, twitter drafts, landing copy, README suggestions — all in the v86 set.

— Dan1 👾
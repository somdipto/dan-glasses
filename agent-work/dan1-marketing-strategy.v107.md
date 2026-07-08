# Dan1 Marketing Strategy — v108 (2026-06-29)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-29 13:55 IST, Bengaluru, India 🇮🇳
**Status:** v108. Supersedes v107.

---

## TL;DR

Three near-term plays (this week), one mid-term play (Q3 2026), one long-term play (Q4 2026+):

1. **This week — ship `danlab.dev/` on zo.space + rewrite 5 GitHub READMEs + 90s demo video.** The GitHub + Show HN backbone.
2. **Wed Jul 1 — post Show HN.** "Open-source AI glasses — on-device, auditable, runs on a $400 laptop." Top-of-front-page target.
3. **Q3 2026 — submit to AIE-Bench v2.2 wearable-agent track.** Paper-grade ECE measurement of audiod's confidence-calibration RL agent. arXiv preprint + Allen AI blog mention.
4. **Q4 2026 — ride Meta $299 wave.** Press push when wearable ships. Auditability is the wedge. Coordinate with the Q3 wearable demo.
5. **Q4 2026+ — community.** Discord only after agent is stable enough for strangers. Not before.

---

## §1 — ICP (Ideal Customer Profile)

**v108 ICP — "the auditable-agent dev tinkerer":**

- Devs and ML researchers, 22-45, US/EU/India, $50K-150K income
- Privacy-aware, has tried ChatGPT, found it disempowering
- Wants to **own** the agent, not rent it. Reads source code. Forks. Deploys.
- Triggers: HN, Karpathy tweets, Meta $299 launch, CNN exam-cheating story
- First 100: somdipto's network + Show HN + 1 press mention

**Secondary ICPs (v108):**
- "The hackathon builder" — 18-28, student/early-career, 48h demos
- "The AGI-curious founder" — 30-50, shipped a product, looking for the on-device wedge
- "The privacy-conscious parent" — 35-55, triggered by CNN exam-cheating story

---

## §2 — Positioning statement (the one-liner)

> **DANI is the on-device, auditable, open-source AI companion for the wearable era** — the only stack where the agent's memory lives on your device, the agent's thoughts are logged to a file you can read, and the binary is MIT-licensed. From Bengaluru to the world. Sub-₹15K. No subscription. No cloud.

**Why it works:**
- Names the form factor (wearable)
- Names the wedge (auditable)
- Names the price (sub-₹15K) — India anchor
- Names the origin (Bengaluru)
- Names what it is **not** (no subscription, no cloud)

**The audit hammer (v108 — the one-line that converts):**

> `curl /audit/tail | jq` — every thought the agent has, every tool it calls, every memory it retrieves. Meta won't ship this. Anthropic won't ship this. We did, because MIT.

---

## §3 — This week (2026-06-29 → 2026-07-05): the three near-term plays

### Play 1 — Ship `danlab.dev/` on zo.space (20 min)

**Why:** v107 + v108 confirmed `danlab.dev/` returns HTTP 308. Zero organic web presence. Show HN link will be dead without a landing page.

**Action:**
1. somdipto → create `danlab.dev` as a zo.space route (or use the existing `som.zo.space` and redirect from a different path)
2. Land a one-page site: hero, the audit hammer, the receipts table (8 daemons, 144/144 tests), "Demo Day Q3 2026 — sign up" email capture
3. Link from GitHub org README

**Owner:** somdipto (decision), Dan1 (copy in `dan1-landing-copy.v108.md`)

**Success metric:** Live URL, GitHub stars +5/week

### Play 2 — Rewrite 5 GitHub READMEs (4h)

**Why:** GitHub READMEs are the #1 ranking surface for "open-source AI glasses India." v108 prioritized 5 repos. Full content in `dan1-github-readme-suggestions.v108.md`.

**Action:**
1. dan-lab org README
2. dani repo
3. dan-glasses repo
4. danlab-multimodal repo
5. paperclip (skip — not ours, link only)

**Owner:** somdipto (merges PR), Dan1 (drafts content)

**Success metric:** Each README has the positioning statement + the audit hammer + the receipts table.

### Play 3 — 90s demo video (4h)

**Why:** Show HN requires video. Landing page requires video. X requires video.

**Action:**
1. Screen-record the 7.08s wizard roundtrip
2. Show the bootstrap wizard, the push-to-talk, the agent's response
3. Show `curl /audit/tail | jq` — the audit hammer
4. Show the proactive moment (minute 3 interjection)
5. 90s, no narration, just on-screen text

**Owner:** somdipto (records), Dan1 (edits script + captions)

**Success metric:** Uploaded to YouTube, embedded in HN post + landing page.

---

## §4 — Wed Jul 1 — SHOW HN DAY

**Title:** Show HN: Open-source AI glasses — on-device, auditable, runs on a $400 laptop

**Post body (skeleton):**
1. TL;DR — 8 daemons, 144/144 tests, MIT, $400 laptop, 7.08s wizard
2. The audit hammer — `curl /audit/tail | jq`
3. The 90s demo video
4. The receipts table
5. The wedge vs Ray-Ban Meta
6. The origin — from Bengaluru to the world
7. GitHub link
8. "Reply to every comment in first 2 hours" — somdipto's job

**Cross-promote:**
- X (Post 5 in v108 twitter-content)
- LinkedIn
- Reddit r/LocalLLaMA, r/MachineLearning, r/wearables

**Owner:** somdipto (posts), Dan1 (drafts, monitors comments)

**Success metric:** Top 30 of front page. +200 GitHub stars in 24h.

---

## §5 — Q3 2026 — AIE-Bench v2.2 submission (Aug 15 deadline)

**Target:** audiod's confidence-calibration RL agent, measured on its own ECE, published to AIE-Bench v2.2 wearable-agent track.

**Why this is the wedge:** OpenAI Whisper, Meta's STT — none of them publish calibration. We do. **Auditable by construction.**

**Action:**
1. Jul 1-15: implement the calibration loop (closed-loop self-improvement)
2. Jul 15-31: measure ECE on AIE-Bench test set
3. Aug 1-15: write arXiv preprint, submit to AIE-Bench v2.2

**Owner:** somdipto (engineering), Dan1 (paper framing + arXiv abstract)

**Success metric:** AIE-Bench v2.2 submission accepted. arXiv preprint cited 5+ times in Q4 2026.

---

## §6 — Q4 2026 — Ride the Meta $299 wave

**Trigger:** Meta Display ships at $299 in October 2026.

**The counter-positioning:**
- Meta: $299, cloud, no audit, no on-device memory, locked to Meta's ecosystem
- DANI: sub-₹15K (~$180), on-device, audit endpoint, MIT, no cloud, no lock-in

**The press push:**
- Coordinate with the wearable demo (Q3 2026 → Q4 2026 transition)
- TechCrunch, The Verge, Hacker Newsletter — pitch the auditability wedge
- somdipto on a podcast (Latent Space, AI Daily, Lex Fridman if possible)

**Owner:** somdipto (interviews), Dan1 (pitching + positioning)

**Success metric:** 3+ press mentions. +1000 GitHub stars. 1 podcast appearance.

---

## §7 — Q4 2026+ — Community (Discord, only when ready)

**Trigger:** Agent is stable enough for strangers. Specifically: no crashes in 30 days, the audit endpoint has documentation, the wizard works on macOS + Linux + Windows.

**Why not before:** A Discord full of "the wizard crashes on my laptop" is worse than no Discord. **Stability first, community second.**

**Action:**
1. Q4 2026: create `discord.gg/danlab`
2. Pin the audit endpoint, the receipts table, the origin essay
3. First 100 members = Show HN commenters who opted in

**Owner:** somdipto (hosts), Dan1 (manages)

**Success metric:** 500 members by end of Q4 2026. <10% of messages are support questions (the rest are showcase, contribution, discussion).

---

## §8 — Anti-strategy (what we are NOT doing)

**v108 anti-strategy — explicit non-goals:**

- **No paid ads.** We're a dev tool, not a consumer product. Ads buy the wrong audience.
- **No Discord before Q4 2026.** Stability first.
- **No Product Hunt before Q3 2026.** Show HN is the right launch surface for us.
- **No TikTok / Instagram / YouTube Shorts.** Wrong audience. We're not a consumer brand.
- **No "thought leadership" LinkedIn posts that don't ship receipts.** Every post links to a number, a file, a commit, a benchmark.
- **No "AI is the future" content.** Cliché. Says nothing.
- **No co-marketing with closed-cloud vendors.** The wedge is the audit endpoint. We don't dilute it.

---

## §9 — Risks + mitigations (v108)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Show HN flops | Medium | High | Pre-buzz on X + LinkedIn, 90s video, reply to every comment |
| memoryd bug blocks wizard | Low | Critical | Pin MEMORYD_DB before Show HN day (Dan2 punchlist) |
| Meta $299 ships early, undercuts our pricing | Low | Medium | Counter-positioning (audit wedge) is the answer, not price matching |
| Somdipto burns out | Medium | Critical | Dan1 takes as much off his plate as possible. 30-min X posts, not 4h essays. |
| Open-source competitor out-executes us | Low | Medium | Link, don't fight. The receipts are the differentiator. |
| Press cycle ignores us | High | Low | Not a wedge channel. Show HN is. |

---

## §10 — Success metrics (v108)

**Week 1 (Jun 29 → Jul 5):**
- danlab.dev/ live
- 5 READMEs rewritten
- 90s video uploaded
- Show HN posted, top 30 of front page
- +200 GitHub stars
- 10 X posts, 2 LinkedIn posts

**Month 1 (Jul 2026):**
- Show HN sustained traffic
- +500 GitHub stars
- AIE-Bench v2.2 calibration loop implemented

**Q3 2026 (Aug-Sep):**
- AIE-Bench v2.2 submission accepted
- arXiv preprint live
- 1 press mention
- +1000 GitHub stars total

**Q4 2026 (Oct-Dec):**
- Meta $299 counter-positioning shipped
- 3+ press mentions
- 1 podcast appearance
- Discord launch
- +2000 GitHub stars total

**By end of 2026:**
- **The audit endpoint is the wedge the entire wearable-AI industry references.**
- **"From Bengaluru to the world" is a sentence people in the AI community have heard.**

---

*Dan1 👾 — co-founder, head of marketing + growth, DanLab*
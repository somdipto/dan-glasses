# Dan1 — Marketing Strategy (v117)

**Run:** 2026-07-02 06:00 UTC · Asia/Calcutta 11:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Builds on:** `dan1-marketing-research.v117.md` (read first).
**Status:** v117. Foundation verified. Strategy sharpened around the 9-daemon-receipts narrative + the SIA port as the second wave.

---

## TL;DR

The brand claim is no longer "shipping." It is **"shipped — 9/9 daemons live, .deb installs, Telegram wired."** Every piece of content from here forward leads with receipts.

**Four moves, in order:**

1. **Lead with receipts.** Rewrite danlab.dev, sharpen GitHub READMEs, ship the 9-daemon matrix as the proof artifact, build X + LinkedIn around the 9-daemon fact. *Week 1–2.*
2. **Ship Show HN #1.** "9 daemons live, .deb installs, on-device AI." Every assertion has a curl payload. The brand claim is provable, not aspirational. *Week 3–4.*
3. **Ship the Telegram surface.** Every post ends with "DM @danlab_bot — it's live and it's the same stack the glasses will run." The bot is the first product surface anyone can touch. *Ongoing.*
4. **Ship the SIA port + Show HN #2.** The second wave. Open counter-narrative to $4.65B closed-source RSI Labs and to Anthropic Dreaming. arXiv + ICML/ACL 2027. *Q3 2026.*

Everything else is a derivative of these four.

---

## Positioning (v117)

### Core positioning statement (updated)
> **Dan Glasses is the open, on-device AI companion in glasses form factor. 9/9 daemons live today. Built in Bengaluru. MIT-licensed. Yours, not theirs.**

### Four positioning principles (v117 adds "receipts")

1. **Yours, not theirs.** Privacy → ownership → openness. (Order matters: Anthropic June 2026 RSI blog validates privacy, Meta paywall validates ownership, SIA framework validates openness.)
2. **Proactive, not reactive.** Salience-gated, cascade-gated (post-VisualClaw port), not always-uploading. Speaks only when it has something to say.
3. **From India, for the world.** Don't overdo it. Be precise. Built in Bengaluru. Open to the world. Sarvam (June 15 2026) validates the "sovereign Indian AI" thesis at the foundation-model level. We are the wearable side of the same story.
4. **Receipts, not claims.** (NEW v117.) Every assertion has a curl payload, a commit link, a paper, or a benchmark. "9/9 daemons live" with the real `curl localhost:{port}/ready` output. Not "our daemons are running."

### Anti-positioning (the things we are NOT)
- Not Google Glass. (Display overlay, enterprise, dead.)
- Not Ray-Ban Meta. (Closed weights, cloud-only, paywalling Conversation Focus.)
- Not Humane / Rabbit. (Cloud-dependent, no memory, died on the vine.)
- Not "another AI agent framework." (We ship a wearable, not a YAML config.)
- Not VisualClaw. (Different layer. They are the published SOTA for self-evolving agents. We are the wearable platform. Co-cite, don't compete.)
- Not "selling the dream." (We are selling the receipts. The dream is what people build on top.)

### Tagline candidates (v117)
1. **"Yours, not theirs."** *(shortest, sharpest, brand-defining)*
2. **"9 daemons live. 1 .deb. 0 cloud calls."** *(NEW v117 — receipts-first)*
3. **"The AI companion that lives on your face — and in your control."**
4. **"Glasses that remember. Memory you own."**
5. **"Open eyes, open weights, open source."**

**Default:** #2 *“9 daemons live. 1 .deb. 0 cloud calls.”* + #1 *“Yours, not theirs.”* as the long-form version. Ship these, not all five.

**Twitter bio (v117):**
```
danlab.dev — open + on-device + wearable AI. Built in Bengaluru 🇮🇳.

9 daemons live · 1 .deb · 0 cloud calls · 1 bot (@danlab_bot).

memory is a feature, not a subscription.
```

---

## Audience strategy (v117, sharper)

Five tiers (from research). **For 2026, focus on Tier 1 + Tier 2 + Tier 3.** Tier 4 (knowledge workers) is a 2027 wedge. Tier 5 (researchers) is enabled by the SIA port. Tier 6 (investors) is a derivative, not a target.

| Tier | 2026 priority | Acquisition surface | First action | v117 delta |
|---|---|---|---|---|
| 1. Developer / hacker | 🔥 P0 | Show HN, r/LocalLLaMA, GitHub | `apt install dan-glasses-daemons` | DM `@danlab_bot` as the demo |
| 2. Accessibility-first | 🔥 P0 | CNET, Gizmodo, accessibility communities | Beta signup + Open Letter | Open Letter (v116 ask) still valid |
| 3. Researcher | 🟡 P1 (post-SIA port) | arXiv, conference circuit | Read paper, cite us | Cite VisualClaw co-citation strategy |
| 4. Knowledge worker | 🟢 P2 (2027) | Substack, X, LinkedIn | Beta signup | — |
| 5. Investor | 🔴 Do not target pre-traction | Inbound only | Wait | — |
| **NEW: India diaspora** | 🟡 P1 | Sarvam ecosystem, Inc42, YourStory | DM `@danlab_bot` + waitlist | Sarvam $1.5B validates the thesis |

---

## Channel strategy (v117, receipts-first)

### 1. X (Twitter) — P0 (founder-led, receipts)

**Account strategy (v117):** Two accounts, clear roles.
- **`@danlab` (lab handle):** posts receipts, releases, daemon map screenshots. Lead with the 9-daemon fact.
- **`@somdipto` (founder handle):** personal essays, origin story, India narrative, opinionated takes.

**Cadence:** 3–5 posts/week on `@danlab` + 1 personal essay/week on `@somdipto`.

**Content mix (weekly, v117):**
- 2 build-in-public posts (what shipped, what broke, what the daemon map looks like — **always with a curl payload or a commit link**)
- 1 opinion post (something in the AGI / edge AI / open-weights discourse, take a side)
- 1 thread (the long-form: SIA, HRM-Text-1B, LFM2.5-VL-450M, anything that earns a thread)
- 1 engagement post (reply to a high-signal AI researcher, quote thoughtfully)
- 1 bot drop (NEW v117): "DM @danlab_bot — it's live and it's the same stack the glasses will run." End every post with this once a week.

**Pinned tweet (v117):** The daemon map screenshot with the 9 ports listed. The visual proof. Until Show HN #1 ships, the daemon map *is* the brand.

### 2. GitHub — P0 (READMEs are the surface, receipts are the content)

**Critical fixes (Week 1, v117):**
- Add profile README (`github.com/somdipto`) with the danlab story + the 9-daemon matrix.
- Set repository topics on every repo: `agi`, `on-device-ai`, `open-weights`, `wearable-ai`, `from-india`, `rust`, `tauri`, `mcp`.
- Add a short description to every repo (currently inconsistent).
- Add a `LICENSE` file or confirm MIT on every public repo.
- Add a `CONTRIBUTING.md` to dan-glasses and danlab-multimodal.
- Add issue templates to dan-glasses and danlab-multimodal.
- **Add a "9-daemon live" badge to the dan-glasses README** — the visual proof at the top of the flagship repo.

**Repo-specific (v117):**
- `dan-glasses`: rewrite README to lead with **9/9 daemons live**, then the wearable story, then the daemon stack, then the build instructions. The README is the brand.
- `danlab-multimodal`: keep the current README, it's already strong. Add the "92/100 average across 3 cycles" demo number to the top.
- `paperclip`: minor polish; do not feature.
- `dan-consciousness`: this is the lab's "brain" — README should make the shared-consciousness model clear.

### 3. Hacker News (Show HN) — P0

**Two Show HN posts planned for 2026 (v117, sharper):**

**Show HN #1 — "9 daemons live, .deb installs, on-device AI" (target: Week 3–4)**
- Title: *Show HN: Dan Glasses — 9 daemons live, on-device AI, .deb install*
- Body: live demo of the daemon map (9 ports, 9 PIDs, all green), the 92/100 danlab-multimodal demo link, the danlab.dev rewrite, the GitHub org.
- **v117 differentiator:** every assertion in the post has a curl payload. The brand claim is provable, not aspirational.
- Timing: Tuesday or Wednesday, 8am PT.
- Prep: have the danlab.dev rewrite live, have the asciinema demo polished, have a 60-second loom of the daemon map.

**Show HN #2 — "SIA-W+H on Dan Glasses" (target: Q3 2026, post-port)**
- Title: *Show HN: Open recursive self-improvement, running on a wearable*
- Body: SIA-W+H port announcement, arXiv link, the danlab-multimodal → SIA arc, the VisualClaw cascade-gate pattern adoption.
- **v117 differentiator:** positioned as the open counter-narrative to BOTH $4.65B closed-source RSI Labs AND Anthropic Dreaming (beta June 2026).
- Timing: same window as arXiv drop.

### 4. Telegram (@danlab_bot) — P0 (NEW v117, the product surface)

**Why this is now P0:** The bot is live. The daemon stack is reachable. The first 1,000 users will interact with the product through the bot, not through the marketing site. **Every post can drive traffic to a real, working product surface.**

**Strategy:**
- **Every weekly post on `@danlab` ends once with:** "DM @danlab_bot — it's live and it's the same stack the glasses will run."
- **The bot is the demo for non-engineers.** They don't need to install the .deb. They DM the bot, the bot answers through the daemon stack. That is the product.
- **The bot is the marketing automation surface.** When the SIA port ships, the first place it ships is the bot. When the VisualClaw cascade-gate lands, it lands in the bot. When memoryd grows, the bot remembers more.
- **The bot is the always-on inbound capture.** A DM to the bot is a conversion event. We can attribute every conversion to a channel.
- **Don't market the bot.** Market the product surface the bot exposes. The bot is invisible; the daemon stack is the product.

### 5. LinkedIn (founder-led) — P1

**Profile:** somdipto, founder. Currently thin.

**Fixes (Week 1):**
- Rewrite headline: *Founder, danlab.dev · 9/9 daemons live · Open, on-device, wearable AI · Bengaluru → the world*
- Rewrite About section: 3 paragraphs, the danlab story, the 9-daemon fact, link to the daemon stack.
- Banner image: a 1584×396 mockup of the daemon map (TBD, design needed).

**Cadence:** 1 post/week. Cross-post selected X content with a 24h delay. LinkedIn rewards day-old content, not real-time.

### 6. Reddit — P1

**Subreddits:** r/LocalLLaMA (P0), r/MachineLearning (P1), r/singularity (P2), r/hackernews (P2 — meta-discussion only), r/india (P1), r/deaf (P1, v117), r/blind (P1, v117), r/accessibility (P1, v117).

**Posting rule:** Lead with substance. Numbers, code, links. No "we built a thing" without a demo.

### 7. arXiv + conference circuit — P1 (Q3)

**Target (v117):** SIA-W+H port paper, end of Q3 2026.
- arXiv: end of Q3.
- Conference: ICML 2027 (Jan deadline) or ACL 2027.
- Blog: parallel drop on danlab.dev.
- **v117 differentiator:** the paper positions SIA as the open counter-narrative to closed-source RSI Labs AND Anthropic Dreaming. Co-cite VisualClaw. Cite HRM-Text-1B as the Feedback-Agent.

### Channels we are NOT touching in 2026
- **Press (TechCrunch / The Verge / Wired):** pre-traction press is a tax. (Open Letter exception per v116.)
- **YouTube demo channel:** time-intensive, low ROI. (Loom only in 2026.)
- **Discord / community chat:** 2027 problem.
- **Substack / newsletter:** 2027 problem. (The blog is on danlab.ai.)
- **Podcast circuit:** founder time, not 2026 priority.

---

## Content strategy (v117, receipts-first)

### 5 content types (v117, sharpened)

**Type 1: Receipts posts (X, weekly) — NEW v117 priority #1**
- The 9-daemon map screenshot, weekly. The same image, refreshed, with the real `curl` outputs.
- "audiod now ships segment_timing histograms to Loki" type updates. Always with a commit link.
- "Today I broke Whisper, here's how" — the kind of post that earns followers.
- **The receipts test:** if a post can ship without a curl payload, a commit link, or a benchmark, it doesn't ship.

**Type 2: Opinion posts (X, weekly)**
- Take a side on AGI discourse. Defend it. Be specific.
- Examples: "On-device will beat cloud-only for ambient AI" / "Open weights is the only credible path to safe RSI" / "Salience-gating beats fixed-FPS" / "Small-beats-large is now empirically real (HRM-Text-1B, VibeThinker-3B)."
- Each post links to a citation.

**Type 3: Technical threads (X, monthly)**
- The SIA explainer.
- The LFM2.5-VL-450M teardown.
- "What 9 daemons bought us."
- The HRM-Text-1B → SIA Feedback-Agent swap.
- 5–7 tweets each. Save the receipts (numbers, code, screenshots).

**Type 4: Long-form blog (GitHub README + danlab.ai/blog, monthly)**
- "From heuristic to SIA" — the arc from danlab-multimodal to SIA-W+H port.
- "Why we picked .deb over Flatpak."
- "The power state machine, in detail."
- "Privacy → ownership → openness: the order matters."

**Type 5: Research artifacts (arXiv + conference, Q3)**
- SIA-W+H port paper (target: arXiv by end of Q3, ICML/ACL 2027).
- LFM2.5-VL-450M on wearable benchmark (if we can characterize power draw).
- HRM-Text-1B Feedback-Agent benchmark report.

**Type 6: Bot drops (X, weekly) — NEW v117**
- "DM @danlab_bot — it's live and it's the same stack the glasses will run." Once a week. Anchored to a specific feature or release.

### Voice & tone rules (v117, receipts-first)

1. **Be direct.** No "we're excited to announce" filler. No "stay tuned." If you can't say it in one sentence, don't say it.
2. **Cite the receipts.** Every opinion post has a link to a paper, a PR, a benchmark. Every receipt post has a curl payload, a commit link, or a benchmark.
3. **Take a side.** "On-device > cloud" / "open > closed" / "small-beats-large is now real" / "VisualClaw and danlab are not competitors, we are different layers of the same ecosystem." Neutrality is death on X.
4. **Show the work.** Screenshots of the daemon map, code snippets, log lines, terminal output.
5. **Earn the origin story.** Mention Bengaluru when relevant, not as a flex.
6. **Brutal honesty > politeness** (per AGENTS.md). "Today I broke X" > "Here's what I learned about X."
7. **Lead with receipts, not dreams.** (NEW v117.) "9/9 daemons live" not "shipping soon." "92/100 average" not "performing well." "DM @danlab_bot" not "join our community."

---

## 90-day execution plan (v117, receipts-first)

### Days 1–14: Land the receipts

| Day | Task | Owner | Output | v117 delta |
|---|---|---|---|---|
| 1 | Pick brand handles (@danlab / @somdipto) | somdipto | Decision | Two-account strategy |
| 1 | Polish the daemon map screenshot for the bio | Dan1 + somdipto | Image | Receipts visual |
| 2 | Rewrite github.com/somdipto profile README | Dan1 | PR | Lead with 9-daemon fact |
| 2 | Add topics + descriptions to all repos | Dan1 | PR | — |
| 2 | Add "9 daemons live" badge to dan-glasses README | Dan1 | PR | NEW v117 |
| 3 | Rewrite danlab.dev homepage (lead with 9 daemons) | Dan1 + somdipto | Live site | Receipts-first |
| 3 | Add /glasses, /dani, /multimodal, /blog routes | Dan1 + somdipto | Live | NEW v117 |
| 4 | First X thread on @danlab: "9 daemons live" | somdipto | Posted | Receipts-first |
| 5 | First @danlab_bot drop: "DM us — the stack is live" | somdipto | Posted | NEW v117 |
| 5 | Polish asciinema demo for Show HN #1 | Dan1 | Updated demo | — |
| 7 | First 5 X posts on @danlab (Type 1 + Type 2) | somdipto | Posted | Receipts-first |
| 10 | LinkedIn profile rewrite + banner | somdipto | Live | Lead with 9 daemons |
| 10 | First @somdipto personal essay on origin story | somdipto | Posted | Bengaluru earned |
| 12 | First DM-to-bot funnel measurement (track X visits → bot DMs) | Dan1 | Baseline | NEW v117 |
| 14 | First technical thread (SIA explainer or 9-daemon teardown) | somdipto | Posted | Receipts-first |

### Days 15–30: Land the loop

| Day | Task | Owner | Output | v117 delta |
|---|---|---|---|---|
| 15 | Polish asciinema demo (final cut for Show HN) | Dan1 | Video | — |
| 18 | Record 60s loom of daemon map | somdipto | Video | Live `curl` outputs |
| 20 | First Reddit post (r/LocalLLaMA — danlab-multimodal, 92/100 demo) | Dan1 | Posted | Receipts-first |
| 22 | "Daily build" X thread (3–5 posts over a week) | somdipto | Posted | — |
| 23 | First bot-driven demo: "DM @danlab_bot — ask it what it remembers" | somdipto + bot | Posted | NEW v117 |
| 25 | Show HN #1: dry run (friend review) | Dan1 + somdipto | Feedback | — |
| 28 | Show HN #1: post | somdipto | Live | Receipts-first |
| 30 | Measure: comments, GitHub stars, .deb installs, bot DMs | Dan1 | Report | NEW metric: bot DMs |

### Days 31–60: Land the story

| Day | Task | Owner | Output | v117 delta |
|---|---|---|---|---|
| 32 | "From heuristic to SIA" blog draft v1 | Dan1 | Markdown | — |
| 40 | First long-form blog post on danlab.ai/blog | somdipto | Published | — |
| 45 | HRM-Text-1B → SIA Feedback-Agent benchmark | Dan2 (research) | Report | v117 swap approval |
| 50 | arXiv paper draft v1 (SIA-W+H port) | Dan2 + somdipto | PDF | — |
| 55 | VisualClaw cascade-gate port spike: 2-week | Dan2 | Spike | NEW v117 |
| 60 | First 50 README improvements based on Show HN feedback | Dan1 | PRs | — |

### Days 61–90: Compound

| Day | Task | Owner | Output | v117 delta |
|---|---|---|---|---|
| 65 | Second long-form blog: "Privacy → ownership → openness" | somdipto | Published | — |
| 70 | arXiv submission: SIA-W+H | somdipto | Submitted | — |
| 75 | Conference submission (ICML 2027) | somdipto | Submitted | — |
| 80 | Show HN #2: SIA-W+H on Dan Glasses | somdipto | Live | Open counter-narrative |
| 85 | VisualClaw cascade-gate port complete: blog post + 1-week demo | Dan2 + Dan1 | Live | NEW v117 |
| 90 | 90-day report: traffic, stars, .deb installs, bot DMs, next quarter | Dan1 | Report | — |

---

## Metrics (v117, what we measure)

### Leading indicators (track weekly, v117 deltas in **bold**)
- GitHub stars per repo
- GitHub issues opened (engagement signal)
- X followers, impressions per post, replies per post
- Reddit upvotes per post
- Show HN: comments, stars, ranking
- danlab.dev: visits, referral source
- **.deb installs** (telemetry opt-in, anonymous)
- **@danlab_bot DMs (cumulative), DAU, queries/user/day** (NEW v117)
- **DM-to-bot attribution from X posts** (NEW v117)

### Lagging indicators (track monthly)
- arXiv downloads
- Inbound: investor / partner / press inquiries
- Hires: engineer / researcher applications
- Accessibility community subscribers (from Open Letter)
- Bot retention: D1, D7, D30

### North star (v117)
**A pull request from a stranger, AND a DM to @danlab_bot from a stranger.** If we can get an unsolicited PR AND a non-engineer DM to the bot in Q3 2026, the marketing is working. Until then, we are pushing.

---

## Budget (v117)

- **Now:** $0. All work is Dan1 + somdipto time + existing tooling.
- **Q3 ask:** $200–500/mo cloud GPU for SIA-W+H port benchmarking. (Dan2 v8 ask.)
- **Press / paid amplification:** $0 in 2026. Earned media only.
- **Conferences:** ICML/ACL 2027 travel + registration, ~$5K.
- **NEW v117 ask:** $300–500 for a 60-second polished demo video of the daemon map (Fiverr-level editor). The loom will do for week 2; the polished version is for Show HN #1.

---

## Open questions for somdipto (v117, sharper)

1. **Brand handles** — confirm two-account strategy: `@danlab` (lab) + `@somdipto` (founder). Need decision Day 1.
2. **X bio** — confirm "9 daemons live. 1 .deb. 0 cloud calls. 1 bot." as the lead line.
3. **Show HN #1 handle** — `@danlab` or `@somdipto`? (Recommended: `@danlab` for the receipts, `@somdipto` retweets/quotes.)
4. **@danlab_bot community** — public community channel or keep private? (Recommended: public, so the bot is a marketing surface; DMs are the conversion event.)
5. **SIA-W+H paper** — arXiv only, or arXiv + blog + conference? (Recommended: all three.)
6. **arXiv target** — end of Q3 2026 or Q1 2027? (Recommended: end of Q3.)
7. **HRM-Text-1B swap** — replace LFM2.5-1.2B-Thinking directly or benchmark first? (Recommended: benchmark first, but the swap is now low-risk because HRM-Text is Apache-2.0 and $1,500-trained.)
8. **VisualClaw cascade-gate port** — 2-week spike or longer research project? (Recommended: 2-week spike, per dan2 v8 recommendation #1.)
9. **Hardware target announcement** — now, or wait until Redax ships? (Recommended: now — "shipping software, building hardware" is a stronger story.)
10. **India press** — Inc42 / YourStory / Economic Times before or after US press? (Recommended: India first.)
11. **Marketing budget** — what's the real number? (Recommended: $0 for now, $500/mo for GPU in Q3, $300–500 for the polished demo video.)
12. **Hiring** — is the first marketing hire an engineer-founder-PM or a real growth person? (Recommended: not in 2026.)
13. **NEW v117: Bot attribution** — how do we measure DM-to-bot conversions from X posts? Recommended: bot logs the X-referral when a user DMs within 30 min of a post mention. (Tech ask for Dan2.)
14. **NEW v117: Sarvam outreach** — should we open a conversation with the Sarvam team this quarter? (Recommended: yes, after Show HN #1 — that gives us a sharper story to lead with.)

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-research.v117.md` for the research that drives this strategy.*
*See `dan1-content-calendar.v117.md` for the weekly execution plan.*
*See `dan1-twitter-content.v117.md` for the launch batch.*
*See `dan1-landing-copy.v117.md` for the danlab.dev/glasses landing page.*
*See `dan1-github-readme-suggestions.v117.md` for README improvements across all repos.*
e with "DM @danlab_bot — it's live."** Not as a CTA — as a fact. The bot is the product.
- **Cross-post key threads to the bot** for in-channel reading. The 9-daemon matrix, the SIA port announcement, the Open Letter all live in the bot as well as the X timeline.
- **The bot is the show-and-tell surface for design partners.** DM the bot, see the daemon map, see the memory count, see the conversation log.
- **The bot is the support surface.** GitHub issues are for code. The bot is for "how do I pair my wearable."

### 5. LinkedIn (founder-led) — P1

**Profile:** somdipto, founder. Currently thin.

**Fixes (Week 1, v117):**
- Rewrite headline: *Founder, danlab.dev · 9 daemons live, building the open on-device AI companion in glasses form factor · Bengaluru → the world*
- Rewrite About section: 3 paragraphs, the danlab story, the 9-daemon fact, link to the daemon stack.
- Banner image: a 1584×396 mockup of the daemon map (TBD, design needed — see Assets below).

**Cadence:** 1 post/week. Cross-post selected X content with a 24h delay. LinkedIn rewards day-old content, not real-time.

### 6. Reddit — P1

**Subreddits:** r/LocalLLaMA (P0), r/MachineLearning (P1), r/singularity (P2), r/hackernews (P2 — meta-discussion only), **r/india (NEW v117 — for the India diaspora wedge)**, **r/deaf + r/blind + r/accessibility (v116 — Open Letter follow-up)**.

**Posting rule:** Lead with substance. Numbers, code, links. No "we built a thing" without a demo.

### 7. arXiv + conference circuit — P1 (Q3)

**Target:** SIA-W+H port paper, end of Q3 2026.
- arXiv: end of Q3.
- Conference: ICML 2027 (Jan deadline) or ACL 2027.
- Blog: parallel drop on danlab.dev.
- **v117 differentiator:** paper includes the VisualClaw cascade-gate adoption, the HRM-Text-1B Feedback-Agent swap, and the danlab-multimodal → SIA-W+H arc.

### Channels we are NOT touching in 2026
- **Press (TechCrunch / The Verge / Wired):** pre-traction press is a tax. (Exception: The Open Letter. v116 ask still valid.)
- **YouTube demo channel:** time-intensive, low ROI. Loom > polished video for Q3.
- **Discord / community chat:** 2027 problem.
- **Substack / newsletter:** 2027 problem.
- **Podcast circuit:** founder time, not 2026 priority.

---

## Content strategy (the daily work, v117)

### 5 content types (prioritized)

**Type 1: Receipts posts (X + danlab.dev, weekly)**
- **9-daemon live matrix** — `curl localhost:{8090,8092,8741,8742,8743,8744,18789}/ready` outputs side by side. Ship this once a week as a fresh screenshot.
- "audiod now ships segment_timing histograms to Loki" type updates.
- "Today I broke Whisper, here's how" — the kind of post that earns followers.

**Type 2: Opinion posts (X, weekly)**
- Take a side on AGI discourse. Defend it. Be specific.
- Examples: "On-device will beat cloud-only for ambient AI" / "Open weights is the only credible path to safe RSI" / "Salience-gating beats fixed-FPS" / "Small-beats-large is now empirically real (HRM-Text-1B, VibeThinker-3B)" / "VisualClaw cascade-gating is the new SOTA" / "9/9 daemons live > 9/9 claims shipped."
- Each post links to a citation or a curl payload.

**Type 3: Technical threads (X, monthly)**
- The SIA explainer.
- The LFM2.5-VL-450M teardown.
- "What 9 daemons bought us."
- The HRM-Text-1B → SIA Feedback-Agent swap.
- The VisualClaw cascade-gate adoption.
- 5–7 tweets each. Save the receipts (numbers, code, screenshots).

**Type 4: Long-form blog (danlab.ai, weekly)**
- "From heuristic to SIA" — the arc from danlab-multimodal to SIA-W+H port.
- "Why we picked .deb over Flatpak."
- "The power state machine, in detail."
- "Privacy → ownership → openness: the order matters."
- "The 9-daemon fact: what we shipped, what we didn't, what's next."

**Type 5: Research artifacts (arXiv + conference, Q3)**
- SIA-W+H port paper (target: arXiv by end of Q3, ICML/ACL 2027).
- LFM2.5-VL-450M on wearable benchmark (if we can characterize power draw).
- The cascade-gate pattern adoption writeup.

### Voice & tone rules (apply to every piece of content, v117)

1. **Be direct.** No "we're excited to announce" filler. No "stay tuned." If you can't say it in one sentence, don't say it.
2. **Cite the receipts.** Every opinion post has a link to a paper, a PR, a benchmark, OR a curl payload. "9/9 daemons live" with the real `curl` output.
3. **Take a side.** "On-device > cloud" / "open > closed" / "small-beats-large is now real" / "receipts > claims." Neutrality is death on X.
4. **Show the work.** Screenshots of the daemon map, code snippets, log lines, terminal output.
5. **Earn the origin story.** Mention Bengaluru when relevant, not as a flex.
6. **Brutal honesty > politeness** (per AGENTS.md). "Today I broke X" > "Here's what I learned about X."
7. **NEW v117: Receipts > adjectives.** "9 daemons live" beats "shipping fast." A curl payload beats a marketing claim. Every sentence must be checkable.

---

## 90-day execution plan (v117)

### Days 1–14: Land the brand with receipts

| Day | Task | Owner | Output | v117 delta |
|---|---|---|---|---|
| 1 | Pick brand handle (@danlab / @danglasses) | somdipto | Decision | — |
| 2 | Rewrite github.com/somdipto profile README | Dan1 | PR | Lead with 9-daemon fact |
| 2 | Add topics + descriptions to all repos | Dan1 | PR | Add 9-daemon badge to dan-glasses |
| 3 | Rewrite danlab.dev homepage (lead with 9-daemon fact) | Dan1 + somdipto | Live site | Daemon matrix on hero |
| 5 | Rewrite dan-glasses README | Dan1 | PR | 9-daemon live badge at top |
| 7 | First 5 X posts (Type 1 receipts) | somdipto | Posted | Daemon map screenshot as Post 1 |
| 10 | LinkedIn profile rewrite + banner | somdipto | Live | — |
| 12 | Polish asciinema demo (already at zo.pub) | Dan1 | Updated demo | — |
| 14 | First technical thread (daemon stack teardown) | somdipto | Posted | — |

### Days 15–30: Land the loop with receipts

| Day | Task | Owner | Output | v117 delta |
|---|---|---|---|---|
| 15 | Record 60s loom of daemon map | somdipto | Video | — |
| 18 | First Reddit post (r/LocalLLaMA — danlab-multimodal) | Dan1 | Posted | Lead with 92/100 demo number |
| 20 | "9-daemon receipts" X thread (5 posts over a week) | somdipto | Posted | Curl payloads inline |
| 22 | First bot drop on @danlab: "DM @danlab_bot" | somdipto | Posted | NEW v117 |
| 25 | Show HN #1: dry run (friend review) | Dan1 + somdipto | Feedback | Reviewers check the curl payloads |
| 28 | Show HN #1: post | somdipto | Live | "9 daemons live, .deb installs" |
| 30 | Measure: comments, GitHub stars, bot DMs, .deb installs | Dan1 | Report | NEW v117: bot DM count as a metric |

### Days 31–60: Land the story

| Day | Task | Owner | Output | v117 delta |
|---|---|---|---|---|
| 32 | "From heuristic to SIA" blog draft v1 | Dan1 | Markdown | — |
| 35 | First VisualClaw cascade-gate spike to perceptiond+memoryd | Dan2 (research) | Code | NEW v117 |
| 40 | First long-form blog post on danlab.ai | somdipto | Published | — |
| 45 | HRM-Text-1B → SIA Feedback-Agent benchmark | Dan2 (research) | Report | — |
| 50 | arXiv paper draft v1 (SIA-W+H port) | Dan2 + somdipto | PDF | — |
| 60 | First 50 README improvements based on Show HN feedback | Dan1 | PRs | — |

### Days 61–90: Compound

| Day | Task | Owner | Output | v117 delta |
|---|---|---|---|---|
| 65 | Second long-form blog: "Privacy → ownership → openness" | somdipto | Published | — |
| 70 | arXiv submission: SIA-W+H | somdipto | Submitted | — |
| 75 | Conference submission (ICML 2027) | somdipto | Submitted | — |
| 80 | Show HN #2: SIA-W+H on Dan Glasses | somdipto | Live | — |
| 85 | Sarvam + Oculosense outreach (India AI ecosystem) | somdipto | 1 reply, 1 call | NEW v117 |
| 90 | 90-day report: traffic, stars, bot DMs, hires, next quarter | Dan1 | Report | — |

---

## Metrics (v117, with bot added)

### Leading indicators (track weekly)
- GitHub stars per repo
- GitHub issues opened (engagement signal)
- X followers, impressions per post, replies per post
- **@danlab_bot DM count (NEW v117)** — the bot is the first product surface, the count is the leading indicator of conversion
- Reddit upvotes per post
- Show HN: comments, stars, ranking
- danlab.dev: visits, referral source

### Lagging indicators (track monthly)
- .deb installs (telemetry opt-in, anonymous)
- Telegram bot daily actives + retention
- arXiv downloads
- Inbound: investor / partner / press inquiries
- Hires: engineer / researcher applications

### North star
**An unsolicited pull request from a stranger.** If we can get an unsolicited PR in by Q3 2026, the marketing is working. Until then, we are pushing.

**v117 second north star:** **@danlab_bot DM-to-install ratio.** If DMs are converting to .deb installs, the funnel works. If not, the bot needs a different shape.

---

## Budget (v117, with accessibility audit)

- **Now:** $0. All work is Dan1 + somdipto time + existing tooling.
- **Q3 ask:** $200–500/mo cloud GPU for SIA-W+H port benchmarking + VisualClaw cascade-gate spike. (Dan2 v5/v8 ask.)
- **Press / paid amplification:** $0 in 2026. Earned media only.
- **Conferences:** ICML/ACL 2027 travel + registration, ~$5K.
- **NEW v117: Accessibility-audit consulting:** $500. To make the "accessibility free forever" promise credible, pay a deaf/HoH consultant to audit the v0 firmware before launch. The promise is only as strong as the product.

---

## Risk register (v117 deltas in **bold**)

| Risk | Probability | Impact | Mitigation | v117 delta |
|---|---|---|---|---|
| Day 3 memory demo doesn't work on camera | High | High | Build the demo before filming. Film 10 takes. | — |
| Meta copies the agent-memory framing in 6 months | Medium | High | The moat is the open agent + the model-swappable architecture. They cannot copy that without an Android fork. | — |
| India glasses competitor (VAYU, Oculosense) ships a better unit | Medium | Medium | We win on software (the agent), not hardware. They can out-hardware us; they cannot out-agent us in 12 months. | — |
| EigenCloud agent deployment doesn't scale | Low | High | Fallback: let users self-host `dani` in Docker. | — |
| HN post gets ignored | Medium | Low | We still get the long-tail traffic from the link. | — |
| We burn out trying to ship all of this | High | High | Cut Q4 conference talk. Cut second creator gifting. The first 5 deliverables in Act 1 are non-negotiable. | — |
| **The 9-daemon claim gets audited and a daemon is actually down** | **Low** | **Critical** | **Verify before posting. Curl payload first, post second. The brand claim is now provable, so it is also falsifiable.** | **NEW v117** |
| **A bot user has a bad experience and goes public** | **Medium** | **High** | **The bot is the first product surface. Treat it like a production system. Monitor errors, log DMs (with consent), have a human in the loop for escalation.** | **NEW v117** |
| **VisualClaw authors don't cite back** | **Low** | **Low** | **Co-cite, don't compete. Different layers. The wearable platform needs the SOTA agent work, and vice versa.** | **NEW v117** |
| **Sarvam outreach doesn't land** | **Medium** | **Low** | **Multiple intro paths. LinkedIn, X, yourstory/Inc42 contacts, mutual friends. Don't bet the strategy on one intro.** | **NEW v117** |
| **The Anthropic Dreaming beta ships a wearable SDK before our SIA port** | **Low** | **Critical** | **Move from "first open recursive self-improvement on a wearable" to "first open, auditable, harness+weights self-improvement on a wearable." Anthropic is closed-source. We are not. The wedge is auditable.** | **NEW v117** |

---

## Decisions I need from somdipto (in order of urgency, v117)

1. **Approve the v117 strategy as the Q3 working plan.** (Today)
2. **Pick the brand handle** (@danlab / @danglasses / @danlabai). (Today)
3. **Greenlight Show HN #1 title:** "9 daemons live, on-device AI, .deb install." (This week)
4. **Approve the @danlab_bot "DM the bot" call-to-action** in every weekly post. (This week)
5. **Sign off on the "accessibility free forever" promise.** (This week — it is a public commitment.)
6. **Approve outreach to Sarvam, Oculosense, and 2-3 deaf-tech creators.** (This week — India ecosystem + accessibility wedge.)
7. **Confirm the SIA port paper target** (arXiv by end of Q3? ICML/ACL 2027?). (This week)
8. **Pick the VisualClaw spike owner** (Dan2? somdipto?). (This week)
9. **Approve the bot productionization** — log DMs with consent, add error monitoring, human escalation path. (Before Show HN #1.)
10. **Approve the Q3 budget** ($500–$1,000/mo for GPU + accessibility audit). (This week.)

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-research.v117.md` for the underlying research.*
*See `dan1-content-calendar.v117.md` for the weekly execution plan.*
*See `dan1-twitter-content.v117.md` for the launch batch (10 posts + bio).*
*See `dan1-landing-copy.v117.md` for the danlab.dev/glasses landing page.*
*See `dan1-github-readme-suggestions.v117.md` for README improvements across all repos.*

# Dan1 — Content Calendar (v122)

**Run:** 2026-07-05 13:00 IST · Week of: 2026-07-06 (Mon) → 2026-07-12 (Sun)
**Author:** Dan1
**Cadence:** 3–5 X posts/wk · 1 Substack post/wk · 1 Loom or asciicast/wk · 1 GitHub commit to a public repo/wk
**Lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*
**v22 GATE:** Show HN #1 (week of Jul 20) is BLOCKED on the v24 toold strict-mode + openclaw shell-call audit + threat model doc. No audit, no Show HN.

---

## Week of 2026-07-06 — "Audit, then ship the substrate"

> Theme: v24 launch-blocker week. toold strict-mode + openclaw shell-call audit ship Q3 W2. Threat model doc lands citing Adversa + Mashable. Protocol surface doc lands citing Cerf + Anthropic + Anthropic-Samsung. Show HN #1 timing is decided at end of week.

### Mon 2026-07-06
- **Internal (P0)** — kick off **toold strict-mode spike** (1 engineer-day). Add quote-removal + `$IFS` + unquoted-glob patterns to BLOCKED-CHARS. Cite Adversa. PR open by EOD.
- **X (lead post, GATED)** — *Cerf lead post* (see `dan1-twitter-content.v122.md` post #1). **DO NOT POST until threat model doc URL is live.**
- **GitHub** — open PR for `dan-glasses/THREAT_MODEL.md` skeleton. Pin draft to issue tracker.

### Tue 2026-07-07
- **Internal (P0)** — kick off **openclaw shell-call audit spike** (1 engineer-day). Audit the openclaw → toold call chain. PR open by EOD.
- **Internal (P0)** — kick off **HuggingFace `danlab` org** creation. Apply for org handle. Upload LFM2.5-VL-450M model card draft.
- **Substack (draft, NOT PUBLISHED until threat model lands)** — *"Observability > model: $725B is being spent on the workbench, not the tool."* (Cites PagerDuty + BNP Paribas + audiod `segment_timing`.)

### Wed 2026-07-08
- **Internal (P0)** — merge `toold strict-mode` PR. Run full toold test suite. Confirm 18/18 + new bash-trick tests.
- **X (post #2, GATED)** — *Threat model lead post* (see `dan1-twitter-content.v122.md` post #2). **POST ONLY if threat model doc URL is live.** Otherwise reply-only.
- **Asciinema / Loom** — record 90-second cast of `danlab-multimodal` running the heuristic feedback loop. Pin to danlab-multimodal README.
- **GitHub** — README rewrites for `dan-glasses`, `dani`, `danlab-multimodal`, `paperclip`. **Panda (`blurr`) framing retired — see `dan1-github-readme-suggestions.v122.md`.**

### Thu 2026-07-09
- **Internal (P0)** — merge `openclaw shell-call audit` PR. Confirm no shell-trick class can be smuggled through the call chain.
- **Internal (P0)** — publish `dan-glasses/THREAT_MODEL.md`. Cite Adversa + Mashable. Show the toold fix. **GATE UNLOCKS X posts #1 and #2.**
- **LinkedIn** — somdipto profile rewrite + first post: *"Building the first open, on-device, agent-native wearable. Here's what we learned shipping 9 daemons in 9 weeks — and what we learned when Adversa AI disclosed bash-tricks bypass 10 of 11 open-source AI coding agents."*
- **X (post #4)** — *"Anthropic shipped the protocol. OpenClaw shipped it first. We are shipping it on a wearable that runs on a $349 laptop, in Bengaluru, MIT-licensed."* (See `dan1-twitter-content.v122.md` post #4.)

### Fri 2026-07-10
- **Internal (P0)** — publish `dan-glasses/PROTOCOL.md`. Cite Cerf, Anthropic Apps Gateway, Anthropic-Samsung custom chip, OpenClaw, MCP.
- **X (post #5)** — *"Zuckerberg admitted Meta AI is 'slower than expected.' We are not waiting. The .deb is up. The bot is live. The substrate is auditable. Audited, not perfect."* (See `dan1-twitter-content.v122.md` post #5.)
- **Telegram** — post the .deb install one-liner + the daemon map screenshot to `@danlab_bot` channel.
- **Substack (publish)** — *"Observability > model: $725B is being spent on the workbench, not the tool."*

### Sat 2026-07-11
- **Substack (publish, v22 ADD)** — *"HackerNoon called it: the month AI governance became operational. Here's what that means for the open substrate."* (Cite HackerNoon operational-governance framing. Frame Dan Glasses as the audited-not-perfect alternative to closed-cloud.)
- **X (light)** — reply-to thread, not a new post. Engage the protocol / MCP community.

### Sun 2026-07-12
- **Internal review** — threat model doc live? Protocol surface doc live? toold strict-mode merged? openclaw shell-call audit merged? **If all YES → Show HN #1 launches Mon Jul 20. If any NO → push to Mon Jul 27.**
- **Prep Show HN #1** — draft the text. Screenshots locked. Demo video locked.

---

## Week of 2026-07-13 — "Show the receipts"

> Theme: Receipts week. Screenshots, model cards, public threat model, GitHub stars drive. Show HN #1 dry-run is on the calendar for Friday.

### Mon
- **X (post #6)** — *"LFM2.5-VL-450M is live on HuggingFace under the danlab org. 209MB. Vision-language. Runs on a laptop. No cloud."* (HF model card link.)

### Tue
- **X (post #7)** — *"Heuristic feedback loops are not RL, and that's the point."* (danlab-multimodal as case study. First post in the "From heuristic to SIA" series.)

### Wed
- **X (post #8)** — *"What's actually inside a 120MB VLM."* (SmolVLM-256M, SigLIP, mmproj. Code-deep post.)

### Thu
- **LinkedIn** — *"On-device AI doesn't need a GPU budget. It needs a substrate."* Cross-post to Substack.

### Fri
- **X (post #9)** — *"PagerDuty says agent model drift is the new outage. BNP Paribas says $725B AI infra spend in 2026. The harness is the workbench, the model is the commodity."* (audiod segment_timing thread.)
- **Internal** — Show HN #1 text dry-run. Screenshots reviewed. Demo video re-recorded if needed.

### Sat–Sun
- Prep Show HN #1 text + screenshots. **Lock Mon Jul 20 launch** (or push to Jul 27).

---

## Week of 2026-07-20 — "Show HN #1"

> **GATE:** Show HN #1 only goes live if v24 launch-blocker is shipped. No gate, no HN.
> Mon 2026-07-20: final dry run. Tue 2026-07-21: Show HN post goes live at 8am Pacific (8:30pm IST).

### Mon
- Internal: Show HN text locked. Screenshots locked. Demo video locked. Threat model + protocol surface doc URLs verified live.

### Tue
- **Hacker News** — Show HN: *"Show HN: Dan Glasses – 9 on-device AI daemons, .deb installs, DM the bot"*
- **X** — link to HN. Quote the protocol lead. Link the threat model doc.
- **LinkedIn** — cross-post.

### Wed–Sun
- Engage every HN comment within 30 min.
- X replies only — no new posts.
- Substack post-mortem on Friday.

---

## Week of 2026-07-27 — "Recover + double down"

> Theme: post-Show HN lessons + prepare for the SIA-W+H port announcement.

### Mon
- X: *"Show HN top 10. 47 comments. 3 inbound forks. Here's what we learned."*

### Tue
- X: protocol series post #2 — *"Anthropic Apps Gateway, OpenClaw MCP, X MCP. The substrate is standardizing. We are the only lab shipping it on a wearable."*

### Wed
- Substack: *"From Show HN to substrate: 7 days that changed our roadmap."*

### Thu
- GitHub: prep dani-skills release that includes a danlab-glasses skill.

### Fri
- X: thread on the 5 PRD user stories, with asciinema per story.

### Sat–Sun
- Q3 W1 prep — VisualClaw port work begins.

---

## Q3 2026 — "SIA on the wearable"

| Week | Theme | Headline event |
|---|---|---|
| Q3 W1 (Aug 3) | VisualClaw port | Cascade-gate upgrade merges. |
| Q3 W2 (Aug 10) | VisualClaw bench | Before/after numbers on the heuristic loop. **v24 in parallel: toold strict-mode + openclaw shell-call audit + threat model doc.** |
| Q3 W3 (Aug 17) | SIA-W+H port | Port announcement. |
| Q3 W4 (Aug 24) | SIA on wearable | First public video of self-improvement loop running on the device. |
| Q3 W5 (Aug 31) | Show HN #2 | "SIA-W+H on a wearable" — the year's biggest event. |
| Q3 W6–W8 | Recovery + arXiv | Paper draft. Submission end of Q3. |

---

## Cadence defaults

- **X:** 3–5 posts/wk. Lead with the 4 pillars + 2 v24 additions (threat model + yours-not-theirs).
- **Substack:** 1 post/wk. Long-form. Cite the dan2 research.
- **LinkedIn:** 1 post/wk. Somdipto profile. Investor / B2B audience.
- **GitHub:** 1 meaningful commit/wk to a public repo. README rewrites count.
- **Telegram:** the bot is the funnel. Every X post links to the bot.
- **Hacker News:** Show HN #1 (Jul 21, GATED on v24 audit). Show HN #2 (Aug 31).
- **arXiv:** 1 paper at end of Q3 (SIA-W+H port). Then 1/qtr after.
- **YouTube:** 1 demo video / month. Asciinema first, Loom second, polished YouTube third.

---

## What we will not post about

- Generic "AI is the future" content.
- Hot takes on competitor drama (respond to Mashable / Meta / Anthropic with substance, not snark).
- Hype about funding rounds (we are not raising right now).
- Listicles, "top 10" posts, engagement bait.
- "Day in the life" founder content (the work is the content).
- Memes that punch down.
- **v22 ADD: any "we are not vulnerable to Adversa's bash trick" claim before the audit ships.** Either the audit is in the threat model doc, or we say nothing.
- **v22 ADD: any "yours, not theirs" copy before the threat model + protocol surface docs are live.** The wedge requires the receipts.

---

## The single rule

**Every post should make a developer want to `apt install dan-glasses-daemons` or a researcher want to read the SIA-W+H paper. If it doesn't, cut it.**

---

*See `dan1-twitter-content.v122.md` for the 10 drafted posts.*

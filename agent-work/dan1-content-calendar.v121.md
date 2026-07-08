# Dan1 — Content Calendar (v121)

**Run:** 2026-07-04 11:35 IST · Week of: 2026-07-06 (Mon) → 2026-07-12 (Sun)
**Author:** Dan1
**Cadence:** 3–5 X posts/wk · 1 Substack post/wk · 1 Loom or asciicast/wk · 1 GitHub commit to a public repo/wk
**Lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*

---

## Week of 2026-07-06 — "Ship the substrate"

> Theme: OpenClaw protocol surface + threat model marketing artifact. P0 deliverables land this week. Newsweek quote goes up. Mashable gets a respectful, public response.

### Mon 2026-07-06
- **X (lead post)** — *"Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it 2 days later. OpenClaw shipped it first. Dan Glasses ships it on a wearable. The substrate is auditable. Thread on the protocol surface 🧵"* (See `dan1-twitter-content.v121.md` post #1.)
- **GitHub** — commit `dan-glasses/THREAT_MODEL.md` and `PROTOCOL.md`. Pin to repo.
- **Internal** — somdipto: get Newsweek URL. somdipto: get Mashable URL. somdipto: Tailscale authkey.

### Tue 2026-07-07
- **X (post #2)** — *"The agent substrate is auditable. Here's the threat model."* Link to `THREAT_MODEL.md`. Tag Mashable respectfully. (See `dan1-twitter-content.v121.md` post #2.)
- **Substack** — *"Observability > model: $725B is being spent on the workbench, not the tool."* (Cites PagerDuty + BNP Paribas + audiod `segment_timing`.)
- **HuggingFace** — create `danlab` org. Upload LFM2.5-VL-450M model card (template in `dan1-github-readme-suggestions.v121.md`).

### Wed 2026-07-08
- **X (post #3)** — *"9 daemons live. .deb installs. DM the bot. No cloud calls. No Meta paywall. Yours, not theirs."* Screenshot of the daemon map. (See `dan1-twitter-content.v121.md` post #3.)
- **Asciinema / Loom** — record 90-second cast of `danlab-multimodal` running the heuristic feedback loop. Pin to danlab-multimodal README.
- **GitHub** — README rewrites for `dan-glasses`, `dani`, `danlab-multimodal`, `paperclip`, `blurr`.

### Thu 2026-07-09
- **X (post #4)** — *"Anthropic shipped the protocol. OpenClaw shipped it first. We are shipping it on a wearable that runs on a $349 laptop, in Bengaluru, MIT-licensed."* (See `dan1-twitter-content.v121.md` post #4.)
- **LinkedIn** — somdipto profile rewrite + first post: *"Building the first open, on-device, agent-native wearable. Here's what we learned shipping 9 daemons in 9 weeks."*

### Fri 2026-07-10
- **X (post #5)** — *"Zuckerberg admitted Meta AI is 'slower than expected.' We are not waiting. The .deb is up. The bot is live. The substrate is auditable."* (See `dan1-twitter-content.v121.md` post #5.)
- **Telegram** — post the .deb install one-liner + the daemon map screenshot to `@danlab_bot` channel.

### Sat 2026-07-11
- **Substack** — *"Wearing an 1B model: $1,500 from scratch is the new origin pillar."* (HRM-Text-1B narrative. Cites the v18 dan2 model analysis.)
- **X (light)** — reply-to thread, not a new post. Engage the protocol / MCP community.

### Sun 2026-07-12
- **Internal review** — what landed, what didn't, what to double down on next week.
- **Prep Show HN #1** — draft the text. Block Jul 21–28 launch window.

---

## Week of 2026-07-13 — "Show the receipts"

> Theme: Receipts week. Screenshots, model cards, public threat model, GitHub stars drive.

### Mon
- **X** — *"LFM2.5-VL-450M is live on HuggingFace under the danlab org. 209MB. Vision-language. Runs on a laptop. No cloud."* (HF model card link.)

### Tue
- **X** — *"Heuristic feedback loops are not RL, and that's the point."* (danlab-multimodal as case study. First post in the "From heuristic to SIA" series.)

### Wed
- **X** — *"What's actually inside a 120MB VLM."* (SmolVLM-256M, SigLIP, mmproj. Code-deep post.)

### Thu
- **LinkedIn** — *"On-device AI doesn't need a GPU budget. It needs a substrate."* Cross-post to Substack.

### Fri
- **X** — *"The harness is the workbench, the model is the commodity."* (PagerDuty + audiod segment_timing thread.)

### Sat–Sun
- Prep Show HN #1 text + screenshots. Lock Jul 21 launch.

---

## Week of 2026-07-20 — "Show HN #1"

> Mon 2026-07-20: final dry run. Tue 2026-07-21: Show HN post goes live at 8am Pacific (8:30pm IST).

### Mon
- Internal: Show HN text locked. Screenshots locked. Demo video locked.

### Tue
- **Hacker News** — Show HN: *"Show HN: Dan Glasses – 9 on-device AI daemons, .deb installs, DM the bot"*
- **X** — link to HN. Quote the protocol lead.
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
| Q3 W2 (Aug 10) | VisualClaw bench | Before/after numbers on the heuristic loop. |
| Q3 W3 (Aug 17) | SIA-W+H port | Port announcement. |
| Q3 W4 (Aug 24) | SIA on wearable | First public video of self-improvement loop running on the device. |
| Q3 W5 (Aug 31) | Show HN #2 | "SIA-W+H on a wearable" — the year's biggest event. |
| Q3 W6–W8 | Recovery + arXiv | Paper draft. Submission end of Q3. |

---

## Cadence defaults

- **X:** 3–5 posts/wk. Lead with the 4 pillars (protocol → observability → on-device → small-beats-large).
- **Substack:** 1 post/wk. Long-form. Cite the dan2 research.
- **LinkedIn:** 1 post/wk. Somdipto profile. Investor / B2B audience.
- **GitHub:** 1 meaningful commit/wk to a public repo. README rewrites count.
- **Telegram:** the bot is the funnel. Every X post links to the bot.
- **Hacker News:** Show HN #1 (Jul 21). Show HN #2 (Aug 31). Two big swings.
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

---

## The single rule

**Every post should make a developer want to `apt install dan-glasses-daemons` or a researcher want to read the SIA-W+H paper. If it doesn't, cut it.**

---

*See `dan1-twitter-content.v121.md` for the 10 drafted posts.*

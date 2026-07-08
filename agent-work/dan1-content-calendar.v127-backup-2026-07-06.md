# DanLab Content Calendar — Run v127

**Date:** 2026-07-06
**Owner:** DAN-1
**Cadence:** 30-day rolling window. Refresh every Monday.
**Cross-ref:** [marketing strategy](./dan1-marketing-strategy.md), [research](./dan1-marketing-research.md)
**v127 delta:** v127 promotes 3 axes to first-class (chip-stack + display-less + outer-loop RSI). 3 unblock-the-gate tasks (Tailscale authkey + reversibility contract + sovereign-trust audit) move to top of Week 1. New "chip-stack sovereignty" post series. New "outer-loop RSI receipts" post series. Heuristic → SIA series (6 posts Q3) confirmed.

---

## 0. Operating principles (v127, unchanged from v111)

1. **No fluff.** Every post ships a code link, a metric, or a demo. No "excited to announce" without a payload.
2. **One idea per post.** Twitter thread counts as one. Blog post is one. YouTube demo is one.
3. **One CTA per week.** Per channel. Cross-posts without separate CTAs.
4. **Owner + review.** Every artifact names one person who ships it and one who reviews.
5. **Tagging.** Every artifact lists: `#track-a` (Dan Glasses wearable), `#track-b` (Dan Voice app), `#research` (multimodal / SIA), `#platform` (Paperclip / OpenClaw), `#site` (danlab.dev), `#telegram` (@danlab_bot).
6. **v111 addition: Real numbers only.** If a claim cannot be backed by a `/status` payload, a Git commit, or a published number, do not post it. "9/9 daemons live" with the real curl output. Not "our daemons are running."
7. **v127 addition: Cite the citable event.** Every post links to a citable event (Babushkin essay, Anthropic 8,000 layoffs, Jack Clark Import AI, Meta contractor disclosure, NVIDIA XR AI, 20M display-less forecast). No post without a citation.

---

## 1. Channels — inventory + cadence (v127)

| Channel | URL / handle | Posts/week | Best for | Owner | v127 status |
|---|---|---|---|---|---|
| **danlab.dev** | https://danlab.dev | Refresh 1×/month | The funnel | somdipto | **STALE — P0 refresh Week 1** |
| **GitHub Discussions** | github.com/somdipto/* | 2 | Engineering drop notes | somdipto | Active |
| **X / Twitter** | @danlab (TBD) | 5 (1 thread, 3 stand-alone, 1 hot-take) | Build-in-public, hot takes | somdipto | **Awaiting handle confirmation** |
| **LinkedIn — somdipto** | linkedin.com/in/somdipto | 2 | Hire signal, India-origin narrative | somdipto | Active |
| **LinkedIn — company** | linkedin.com/company/dan-lab | 1 (cross-post of Twitter thread) | B2B credibility | somdipto | LinkedIn company page exists |
| **YouTube Shorts** | youtube.com/@danaboratory | 1 | 30–90s demos | somdipto + editor | **No channel yet — P1 create** |
| **YouTube long-form** | same | 1/month | Conference talks, architecture deep-dives | somdipto | No channel yet |
| **Hacker News (Show HN)** | news.ycombinator.com | 1/month (Show HN #1 = Jul 20) | Initial spike for any major drop | somdipto | **GATED on reversibility contract + sovereign-trust audit** |
| **danlab.ai blog** | danlab.ai/blog | 1/month | Long-form technical posts | somdipto | Mirror to dev.to |
| **Telegram** | @danlab_bot | continuous | The product surface, in-channel | somdipto | **LIVE — wire into all posts** |
| **HuggingFace** | huggingface.co/danlab | 1 model card / month | Model card + benchmark results | somdipto | **NO ORG YET — P1 create Week 1** |
| **Substack** | danaboratory.substack.com | 1/month | Mirror of long-form + paid gate | somdipto | None yet |

**Total output (per week):** ≈ 10 net posts + continuous Telegram + Show HN #1 in week 3. Sustainable. No burnout.

---

## 2. Week 1 — UNBLOCK THE 3 GATES (July 6 – 12)

**Theme:** *"3 gates. 4 engineer-days. 1 show HN."*

| Day | Channel | Format | Topic | Asset / link | Owner | Tag |
|---|---|---|---|---|---|---|
| **Mon** | **Tailscale authkey drop** | **som action** | **Drop `TAILSCALE_AUTHKEY` in [Settings > Advanced](/?t=settings&s=advanced). Run `bash /home/workspace/dan-glasses/scripts/tailscale-join.sh`. Live demo URL unblocked.** | script | **somdipto** | **#track-a #P0** |
| **Mon** | X | Single tweet | "Tailscale authkey pending. Script ready. 1 of 3 gates. 👾" | link to script | somdipto | #track-a |
| **Tue** | **danlab.dev** | **Homepage rewrite** | **Match v127 strategy. 5 pillars. 9 daemons live. Display-less v1.0. Reversibility contract. Threat model. Open source. From India.** | **NEW HOMEPAGE** | **somdipto** | **#site #P0** |
| **Tue** | X | Single tweet | "9/9 daemons live. danlab.dev updated. Telegram @danlab_bot wired. Open source. From India." | screenshot of danlab.dev + daemon matrix | somdipto | #site #telegram |
| **Wed** | GitHub | Release note | `dan-glasses` v127: 9/9 daemons verified live with real `/status` payloads + zo-mcp-bridge persistent + Tailscale script | tag + change log | somdipto | #track-a |
| **Wed** | X | Daemon-of-the-week #1: audiod | Real `/ready` payload + v1.1 liveness/readiness split explainer | `curl localhost:8090/ready` | somdipto | #track-a |
| **Thu** | **sovereign-trust audit ships (engineer)** | **1 engineer-day** | **v124 plan-O1 complete. Threat model doc updated to v127.** | PR | engineer | **#track-a #P0** |
| **Thu** | X | Single tweet | "Sovereign-trust audit shipped. Threat model v127. The lab that ships the audit before the incident. 👾" | link to threat model | somdipto | #track-a |
| **Fri** | **reversibility contract** | **engineer-days 1-2 of 3** | **v124 plan-O2 in progress. Sign every model call, every memory write, every daemon.** | PR | engineer | **#track-a #P0** |
| **Fri** | X | 6-tweet thread | "How to build a proactive AI wearable on a $0 budget" (link build plan) | link to /docs/dan-glasses-build-plan.md | somdipto | #track-a |
| **Sat** | YouTube Shorts | 60s | "All 9 Dan Glasses daemons running in one minute" | capture output of daemon matrix | somdipto + editor | #track-a |
| **Sun** | **HuggingFace `danlab` org** | **create + model card** | **Create org + LFM2.5-VL-450M model card + benchmark results** | org + card | somdipto | **#research #P1** |
| **Sun** | GitHub | Discussion | "Roadmap for Q3: which Paperclip agent should we ship first?" | poll options | somdipto | #platform |

**Week-1 metric targets:**
- Tailscale authkey: dropped, demo URL live
- danlab.dev unique visitors: 500 (from ~0 today)
- 100 GitHub stars across org (currently ~50 estimated)
- 500 X impressions on the daemon thread
- 10 paired Telegram users (cumulative)
- HuggingFace `danlab` org: created with 1 model card

---

## 3. Week 2 — REVERSIBILITY + CHIP-STACK SOVEREIGNTY (July 13 – 19)

**Theme:** *"The reversibility contract. The chip stack is yours. The substrate is shipping."*

| Day | Channel | Format | Topic | Asset / link | Owner | Tag |
|---|---|---|---|---|---|---|
| **Mon** | **reversibility contract ships (engineer)** | **engineer-day 3 of 3** | **v124 plan-O2 complete. CI reversibility test green. PR merged.** | PR | engineer | **#track-a #P0** |
| **Mon** | danlab.ai blog | 1,500-word post | "Reversibility: the contract that makes AI wearable trustable" | code from v124 plan-O2 | somdipto | #track-a |
| **Tue** | X | 4-tweet thread | "The reversibility contract: sign every model call, rewind to any snapshot, audit the log" | link to contract | somdipto | #track-a |
| **Tue** | X | Daemon-of-the-week #2: perceptiond | LFM2.5-VL-450M Q4_0 spec + salience gating + scene-gate dedup explainer | `curl localhost:8092/stats` | somdipto | #track-a |
| **Wed** | LinkedIn (somdipto) | 3-paragraph post | "We shipped the reversibility contract. Here's what it does and why it matters." | link to contract | somdipto | #track-a |
| **Wed** | X | Single tweet | "Anthropic laid off 8,000 in June-July 2026. The closed-source moat is being unwound from the inside. We ship the reversibility contract. 👾" | link to Babushkin essay + Anthropic news | somdipto | #track-a |
| **Thu** | YouTube Shorts | 45s | "Demo: audiod 'audiod unreachable' chip turns red when whisper-cli is missing" | before/after screen capture | somdipto + editor | #track-a |
| **Fri** | X | Hot-take | "The chip stack is yours. NVIDIA XR AI + viture Helix make open-source chip-stack-validated. Anthropic-Samsung custom chip is the closed-source moat. We are the open alternative. 👾" | link to NVIDIA XR AI + viture Helix + Anthropic-Samsung | somdipto | #track-a |
| **Sat** | GitHub | Discussion | "Heuristic vs SIA: when is the right time to flip the switch from hand-coded to learned?" | link to SIA repo | somdipto | #research |
| **Sun** | Substack | Mirror of Mon blog + 1-paragraph subscriber-only commentary | — | — | somdipto | #track-a |

**Week-2 metric targets:**
- Reversibility contract: shipped + cited
- danlab.ai blog: 500 page-views, 2min avg time-on-page
- 1k X impressions on the reversibility thread
- 30 paired Telegram users

---

## 4. Week 3 — SHOW HN #1 + OUTER-LOOP RSI (July 20 – 26)

**Theme:** *"Show HN: Dan Glasses — 9 daemons live, .deb installs, on-device AI."*

| Day | Channel | Format | Topic | Asset / link | Owner | Tag |
|---|---|---|---|---|---|---|
| **Mon** | **Show HN #1** | **Show HN post** | **"Show HN: Dan Glasses — 9 daemons live, .deb installs, on-device AI" — body: 1) the .deb, 2) the 9-daemon matrix, 3) the threat model doc, 4) the reversibility contract, 5) the zo-mcp-bridge, 6) the Telegram @danlab_bot demo** | post | **somdipto** | **#track-a #P0** |
| **Mon** | X | Single tweet | "Show HN: Dan Glasses — 9 daemons live, .deb installs, on-device AI. Front page of HN today. 👾" | link to Show HN | somdipto | #track-a |
| **Tue** | X | Daemon-of-the-week #3: memoryd | SQLite + 384-dim vectors + episodic/semantic/procedural | `curl localhost:8741/stats` | somdipto | #track-a |
| **Tue** | X | 5-tweet thread | "Outer-loop RSI is shipping: audiod v1.0→v1.4 in 9 weeks. 5 versions. Jack Clark says 8x LOC at Anthropic in 2026. We are the open counter-receipt. 👾" | link to audiod/SPEC.md changelog | somdipto | #track-a #research |
| **Wed** | LinkedIn (company) | Cross-post of Show HN | "Show HN: Dan Glasses — 9 daemons live, .deb installs, on-device AI" | link to Show HN | somdipto | #track-a |
| **Wed** | Show HN | Engage every comment | Reply to every Show HN comment, ship updates, follow up | comments | somdipto | #track-a |
| **Thu** | YouTube Shorts | 60s | "Show HN day 1: what the HN comments said, what we shipped in response" | screen capture | somdipto + editor | #track-a |
| **Fri** | X | Hot-take | "Display-less v1.0: the 20M-unit 2026 category is the always-on-hearing race, not the AR-display race. We ship display-less. 👾" | link to Smart Analytics Global forecast | somdipto | #track-a |
| **Sat** | Telegram | Bot feature drop | Wire memoryd → bot recall. "Ask me what I remember." | bot update | somdipto | #telegram |
| **Sat** | GitHub | Discussion | "Which OAuth provider should we ship first in Dan Voice? Gmail vs Notion vs Calendar" | poll | somdipto | #track-b |
| **Sun** | Substack | Mirror of Show HN post + 1-paragraph subscriber-only commentary | — | — | somdipto | #track-a |

**Week-3 metric targets:**
- Show HN #1: top 24 hours front page
- 1,000 .deb installs (cumulative)
- 1,000 X followers (cumulative)
- 100 paired Telegram users (cumulative)
- 200 Show HN points

---

## 5. Week 4 — HEURISTIC → SIA + DAN VOICE (July 27 – Aug 2)

**Theme:** *"The substrate improves. The SIA port ships. The Day 5 wedge holds."*

| Day | Channel | Format | Topic | Asset / link | Owner | Tag |
|---|---|---|---|---|---|---|
| Mon | danlab.ai blog | 1,500-word post | "Outer-loop RSI is shipping: audiod v1.4 and the 9-week changelog" | code from audiod/SPEC.md | somdipto | #track-a #research |
| Tue | X | Daemon-of-the-week #4: toold | Sandboxed tool execution + Paperclip agent hookup | `curl localhost:8742/status` | somdipto | #track-a #platform |
| Tue | X | 5-tweet thread | "Heuristic → SIA: when is the right time to flip the switch from hand-coded to learned? Pre-RL scaffold → SIA-H → SIA-W+H" | link to SIA repo + danlab-multimodal | somdipto | #research |
| Wed | LinkedIn (somdipto) | Personal essay | "I am building a Jarvis that ships in 8 weeks. Here is the PRD." | link to DanGlasses/DAN_VOICE_COMPLETE_PRD.md | somdipto | #track-b |
| Thu | YouTube Shorts | 60s | "Demo: 'Hey Dan — summarize the last email from Mom' (mock, voice + audio wave)" | AI-generated voice sample | somdipto + editor | #track-b |
| Fri | X | Single tweet | "Privacy by architecture: Quark / Meta / Dan comparison table" | ASCII table | somdipto | #track-a #track-b |
| Sat | Telegram | Bot feature drop | Wire reversibility contract → bot audit log. "Show me what you did in the last hour." | bot update | somdipto | #telegram |
| Sat | GitHub | Discussion | "BOM cost of v1 vs v1.5 vs v2 — does the math hold up?" | spreadsheet link | somdipto | #track-a |
| Sun | Substack | Mirror of Mon blog + 1-paragraph subscriber-only commentary | — | — | somdipto | #track-a |

**Week-4 metric targets:**
- 2k X impressions on the outer-loop RSI thread
- 200 paired Telegram users (cumulative)
- Show HN: 300 points (cumulative)
- 1,500 .deb installs (cumulative)

---

## 6. Week 5+ (Aug 3 onward) — Long-form pipeline

- **Heuristic → SIA series (Q3 2026, 6 posts):** Post 1-2 ship in August, 3-4 in September, 5-6 in October.
- **Daemon-of-the-week series continues:** weeks 5-12 (zo-mcp-bridge, danlab-multimodal, paperclip, dani).
- **Long-form blog (1/month):** Aug = "Chip-stack sovereignty: open-source software on a chip the user owns". Sep = "The display-less v1.0: why the 20M-unit 2026 category matters". Oct = "Reversibility: the contract that makes AI wearable trustable (follow-up)".
- **Conference talk proposals:** India AI Summit, Web Summit Bangalore, FOSDEM fringe, GitHub Universe.
- **Press kit (1, when ready):** Press release, founder bio, 9-daemon matrix, threat model, reversibility contract, .deb download, Telegram bot, asciinema recording.
- **A/B test: 4-lane vs 4-axis landing page.** See v127-landing-copy.md §7.

---

## 7. Re-usable artifacts (write once, cross-post forever)

Build these in Week 1. Each one is referenced 4–10 times across the calendar.

### A. danlab.dev homepage (v127 NEW)
- React + Vite + Tailwind CSS 4, `<1MB` total page weight
- Hero: *"A proactive AI on your face. Open source. From India. The chip stack is yours."*
- 5 pillars row (protocol, observability, on-device, small-beats-large, sovereign-trust + reversibility + chip + outer-loop RSI + display-less)
- 9-daemon matrix table with real `/status` payloads as examples
- Comparison table: Ray-Ban Meta / Apple / Anthropic / Dan (4 lanes)
- Telegram surface (`@danlab_bot`) in the footer
- No third-party trackers for 30 days

### B. Architecture one-pager
- 1-page landscape PDF, 5 layers (hardware, services, gateway, agents, app).
- Lives at `danlab.ai/architecture.pdf` and in every repo root.
- Re-use: every "how does Dan Glasses work?" answer. Also embedded in press kit.

### C. Comparison table (Ray-Ban Meta / Apple / Anthropic / Dan)
- ASCII in tweet form, image form for LinkedIn / YouTube.
- Re-use: every privacy pitch. Refresh quarterly when competitors ship.
- v127 add: 4-lane column (on-device open / hybrid / closed-cloud / substrate)

### D. The 9 daemons live demo
- 60-second screen capture of the full daemon matrix.
- Re-use: every "we shipped this" tweet. Pinned on GitHub.

### E. asciinema recording of danlab-multimodal heuristic loop
- 90-second terminal capture, 92/100 avg score.
- Re-use: lead magnet, every "are we real?" pitch. Hosted on https://zo.pub/som/danlab-multimodal-demo

### F. The 8-agent workflow map (Track B / Dan Voice)
- 1-page diagram of the 8 Paperclip workflows × integrations.
- Re-use: every Dan Voice pitch. Refresh when we ship an agent.

### G. Telegram pairing one-pager
- 30-second GIF showing DM → pairing → first question
- Re-use: every post that mentions `@danlab_bot`

### H. Reversibility contract explainer (v127 NEW)
- 1-page diagram of the audit log + snapshot + rewind + sign + reversibility test.
- Re-use: every "why Dan Glasses is trustable" answer. Also embedded in press kit + threat model doc.

### I. Chip-stack sovereignty explainer (v127 NEW)
- 1-page diagram of NVIDIA XR AI + viture Helix (open) vs Anthropic-Samsung custom chip (closed).
- Re-use: every "what is the substrate" answer. Embedded in press kit.

### J. Display-less v1.0 explainer (v127 NEW)
- 1-page diagram of the 20M-unit 2026 category + 6-entrants race.
- Re-use: every "why display-less" answer. Embedded in press kit.

---

## 8. Metrics weekly review (Monday 10:00 IST)

Single Google Sheet (or markdown in `/dan-glasses/agent-work/weekly-metrics/`):

- danlab.dev unique visitors, bounce rate
- GH stars total, per repo (6 hero repos)
- X impressions per tweet, profile visits
- LinkedIn impressions per post, follower delta
- YouTube views per video, retention curve
- danlab.ai blog page-views, time-on-page
- @danlab_bot paired users (cumulative), DAU, queries/user/day
- Show HN points (when posted)
- Reversibility contract downloads (when shipped)
- Tailscale tailnet users (after unblock)
- .deb install count (after release)

**Stop-doing triggers** (kill a channel after 4 weeks of <X results):
- X: <1k impressions per week
- LinkedIn (company): <200 impressions per post
- danlab.ai blog: <500 page-views per month
- Telegram: <10% D7 retention
- YouTube Shorts: <500 views per video

---

## 9. Content production rules (v127, unchanged from v111)

- **Pre-write Mondays.** Sit down for 90 min on Monday morning. Write 3 drafts. Park them in a `drafts/` folder.
- **Ship Tuesday + Thursday + Saturday** by default. Stagger so each channel sees the same artifact only twice per week.
- **No editing on ship-day.** Drafts are pre-approved by Sunday evening.
- **Every post has a CTA**, even if the CTA is "read the code" or "DM @danlab_bot".
- **Re-use is mandatory.** A tweet idea that bombs becomes a Substack footnote.
- **v111 addition: Daemon-of-the-week posts ship a real `curl` payload.** Not a mockup.
- **v127 addition: Every post cites a citable event.** Babushkin essay, Anthropic 8,000 layoffs, Jack Clark Import AI, Meta contractor disclosure, NVIDIA XR AI, 20M display-less forecast. No post without a citation.

---

## 10. Holiday / event calendar (v127, unchanged from v111)

| Date (2026) | Event | Use it for |
|---|---|---|
| Aug 15 | India Independence Day | "From India to AGI" thread |
| Sep | India AI Summit | Conference demo + press booth |
| Oct 1–7 | FOSDEM fringe | "Watchful AI" talk |
| Oct | Web Summit Bangalore | Track A launch talk |
| Nov | GitHub Universe | Show HN aligned to OSS release |
| Dec | Year-end retrospective | Top-10 blog post |

Add more as they land.

---

## 11. v127 week-by-week summary (one-liner per week)

- **Week 1:** 3 gates unblocked (Tailscale + sovereign-trust + reversibility start). danlab.dev refresh. HuggingFace org.
- **Week 2:** Reversibility contract ships. Chip-stack sovereignty pillar goes live. Anthropic 8,000 layoffs cite.
- **Week 3:** Show HN #1 ships (Jul 20). Outer-loop RSI thread. Display-less v1.0 hot-take.
- **Week 4:** Outer-loop RSI long-form. Heuristic → SIA series post 1-2. Dan Voice PRD LinkedIn essay.

---

*Content calendar complete. v127 is the unblock-the-gate calendar. The next 100% of value is the 3 gates in Week 1 + Show HN #1 in Week 3. Everything else is content.*

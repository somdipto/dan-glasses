# DanLab Content Calendar — Run v111
**Date:** 2026-07-01
**Owner:** DAN-1
**Cadence:** 30-day rolling window. Refresh every Monday.
**Cross-ref:** [marketing strategy](./dan1-marketing-strategy.md), [research](./dan1-marketing-research.md)
**v111 delta:** Week 1 priorities overhauled. Telegram surface added. Daemon-of-the-week series added. danlab.dev refresh is the lead.

---

## 0. Operating principles (v111, unchanged from v110)

1. **No fluff.** Every post ships a code link, a metric, or a demo. No "excited to announce" without a payload.
2. **One idea per post.** Twitter thread counts as one. Blog post is one. YouTube demo is one.
3. **One CTA per week.** Per channel. Cross-posts without separate CTAs.
4. **Owner + review.** Every artifact names one person who ships it and one who reviews.
5. **Tagging.** Every artifact lists: `#track-a` (Dan Glasses wearable), `#track-b` (Dan Voice app), `#research` (multimodal / SIA), `#platform` (Paperclip / OpenClaw), `#site` (danlab.dev), `#telegram` (@danlab_bot). This lets us measure channel-product fit later.
6. **v111 addition:** **Real numbers only.** If a claim cannot be backed by a `/status` payload, a Git commit, or a published number, do not post it. "9/9 daemons live" with the real curl output. Not "our daemons are running."

---

## 1. Channels — inventory + cadence (v111)

| Channel | URL / handle | Posts/week | Best for | Owner | v111 status |
|---|---|---|---|---|---|
| **danlab.dev** | https://danlab.dev | Refresh 1×/month | The funnel | somdipto | **STALE — P0 refresh this week** |
| **GitHub Discussions** | github.com/somdipto/* | 2 | Engineering drop notes | somdipto | Active |
| **X / Twitter** | @danaboratory (TBD) | 5 (1 thread, 3 stand-alone, 1 hot-take) | Build-in-public, hot takes | somdipto | Awaiting handle |
| **LinkedIn — somdipto** | linkedin.com/in/somdipto | 2 | Hire signal, India-origin narrative | somdipto | Active |
| **LinkedIn — company** | linkedin.com/company/dan-lab | 1 (cross-post of Twitter thread) | B2B credibility | somdipto | LinkedIn company page exists |
| **YouTube Shorts** | youtube.com/@danaboratory | 1 | 30–90s demos | somdipto + editor | No channel yet |
| **YouTube long-form** | same | 1/month | Conference talks, architecture deep-dives | somdipto | No channel yet |
| **Hacker News (Show HN)** | news.ycombinator.com | 1/month | Initial spike for any major drop | somdipto | None yet |
| **danlab.ai blog** | danlab.ai/blog | 1/month | Long-form technical posts | somdipto | Mirror to dev.to |
| **Telegram** | @danlab_bot | continuous | The product surface, in-channel | somdipto | **LIVE — wire into all posts** |
| **Substack / Beehiiv** | danaboratory.substack.com | 1/month | Mirror of long-form + paid gate | somdipto | None yet |

**Total output (per week):** ≈ 10 net posts + continuous Telegram. Sustainable. No burnout.

---

## 2. Week 1 — danlab.dev refresh + foundation drops (July 1 – 7)

**Theme:** "9/9 daemons live. Site updated. Telegram works."

| Day | Channel | Format | Topic | Asset / link | Owner | Tag |
|---|---|---|---|---|---|---|
| **Tue** | **danlab.dev** | **Homepage rewrite** | **Match v110 strategy. Proactive AI. Architecturally private. 9 daemons live. Open source. From India.** | **NEW HOMEPAGE** | **somdipto** | **#site #P0** |
| **Tue** | GitHub | Release note | `dan-glasses` v111: 9/9 daemons verified live with real `/status` payloads | tag + change log | somdipto | #track-a |
| **Tue** | X | Single tweet | "9/9 daemons live. danlab.dev updated. Telegram @danlab_bot wired. Open source. From India." | screenshot of danlab.dev + daemon matrix | somdipto | #site #telegram |
| Wed | LinkedIn (somdipto) | 3-paragraph post | "We rewrote danlab.dev. Here's what changed and why." | link to danlab.dev | somdipto | #site |
| Wed | X | Daemon-of-the-week #1: audiod | Real `/ready` payload + v1.1 liveness/readiness split explainer | `curl localhost:8090/ready` | somdipto | #track-a |
| Thu | Telegram | Announcement post in the bot | "Welcome to @danlab_bot. DM to pair." | bot message | somdipto | #telegram |
| Fri | X | 6-tweet thread | "How to build a proactive AI wearable on a $0 budget" (link build plan) | link to /docs/dan-glasses-build-plan.md | somdipto | #track-a |
| Sat | YouTube Shorts | 60s | "All 9 Dan Glasses daemons running in one minute" | capture output of daemon matrix | somdipto + editor | #track-a |
| Sun | GitHub | Discussion | "Roadmap for Q3: which Paperclip agent should we ship first?" | poll options | somdipto | #platform |

**Week-1 metric targets:**
- danlab.dev unique visitors: 500 (from ~0 today)
- 100 GitHub stars across org (currently ~50 estimated)
- 500 X impressions on the daemon thread
- 10 paired Telegram users (cumulative)

---

## 3. Week 2 — Architecture deep-dive (July 8 – 14)

**Theme:** "How 9 services + an OpenClaw gateway become one proactive agent."

| Day | Channel | Format | Topic | Asset / link | Owner | Tag |
|---|---|---|---|---|---|---|
| Mon | danlab.ai blog | 1,500-word post | "The watchful loop: how perceptiond decides what is worth seeing" | code from perceptiond/ | somdipto | #track-a |
| Tue | X | Daemon-of-the-week #2: perceptiond | LFM2.5-VL-450M Q4_0 spec + salience gating explainer | `curl localhost:8741/status` | somdipto | #track-a |
| Tue | X | 4-tweet thread | "The 5 lines of code that make audiod actually ship-ready (readiness probe)" | link to audiod/SPEC.md | somdipto | #track-a |
| Wed | LinkedIn (company) | Cross-post of Mon blog | same | — | somdipto | #track-a |
| Thu | YouTube Shorts | 45s | "Demo: audiod 'audiod unreachable' chip turns red when whisper-cli is missing" | before/after screen capture | somdipto + editor | #track-a |
| Fri | X | Hot-take | "Most AI assistants are reactive. Ours watches the room." (tease next week's demo) | none | somdipto | #track-a |
| Sat | GitHub | Discussion | "Heuristic vs SIA: when is the right time to flip the switch from hand-coded to learned?" | link to SIA repo | somdipto | #research |
| Sun | Substack | Mirror of Mon blog + 1-paragraph subscriber-only commentary | — | — | somdipto | #track-a |

**Week-2 metric targets:**
- danlab.ai blog: 500 page-views, 2min avg time-on-page
- 1k X impressions on the perceptiond thread
- 30 paired Telegram users

---

## 4. Week 3 — Track B (Dan Voice) drops (July 15 – 21)

**Theme:** "Your earbuds are now a Jarvis. No hardware purchase."

| Day | Channel | Format | Topic | Asset / link | Owner | Tag |
|---|---|---|---|---|---|---|
| Mon | danlab.ai blog | 1,200-word post | "How EigenCloud containers per user beat every consumer AI cloud today" | link to PRD_DAN_VOICE.md | somdipto | #track-b |
| Tue | X | Daemon-of-the-week #3: memoryd | SQLite + 384-dim vectors + episodic/semantic/procedural | `curl localhost:8092/stats` | somdipto | #track-a |
| Tue | X | 5-tweet thread | "8 Paperclip agent workflows that replace $400/mo of SaaS" | link to DanGlasses/ARCHITECTURE.md | somdipto | #platform #track-b |
| Wed | LinkedIn (somdipto) | Personal essay | "I am building a Jarvis that ships in 8 weeks. Here is the PRD." | link to PRD | somdipto | #track-b |
| Thu | YouTube Shorts | 60s | "Demo: 'Hey Dan — summarize the last email from Mom'" (mock, voice + audio wave) | AI-generated voice sample | somdipto + editor | #track-b |
| Fri | X | Single tweet | "Privacy by architecture: Quark / Meta / Dan comparison table" | ASCII table | somdipto | #track-a #track-b |
| Sat | Telegram | Bot feature drop | Wire memoryd → bot recall. "Ask me what I remember." | bot update | somdipto | #telegram |
| Sat | GitHub | Discussion | "Which OAuth provider should we ship first in Dan Voice? Gmail vs Notion vs Calendar" | poll | somdipto | #track-b |

**Week-3 metric targets:**
- 1.5k X impressions on the Dan Voice thread
- 50 paired Telegram users (cumulative)
- 100 danlab.ai blog subscribers

---

## 5. Week 4 — Track A (Dan Glasses wearable) drops (July 22 – 28)

**Theme:** "9/9 daemons running on a Linux laptop. Now let's put it on your face."

| Day | Channel | Format | Topic | Asset / link | Owner | Tag |
|---|---|---|---|---|---|---|
| Mon | danlab.ai blog | 1,500-word post | "The 4 glasses hardware tradeoffs nobody tells you about" | numbered list | somdipto | #track-a |
| Tue | X | Daemon-of-the-week #4: toold | Sandboxed tool execution + Paperclip agent hookup | `curl localhost:8742/status` | somdipto | #track-a #platform |
| Tue | X | 6-tweet thread | "Why the 200–250 mAh battery was wrong, and what we changed to 400–450 mAh" | chart | somdipto | #track-a |
| Wed | LinkedIn (company) | Cross-post | — | — | somdipto | #track-a |
| Thu | YouTube Shorts | 90s | "Dan Glasses — desktop prototype demo (3 services live, no cloud)" | screen capture | somdipto + editor | #track-a |
| Fri | X | Hot-take | "Glasses at $99 make smart-glasses a daily-driver category. The math proves it." | 3 bullet math | somdipto | #track-a |
| Sat | GitHub | Discussion | "BOM cost of v1 vs v1.5 vs v2 — does the math hold up?" | spreadsheet link | somdipto | #track-a |
| Sun | Show HN draft | Sandbox review | "Show HN: Dan Glasses — proactive AI wearable, 9 daemons, open source" | — | somdipto + reviewer | #track-a |

**Week-4 metric targets:**
- 2k X impressions on the hardware thread
- 100 paired Telegram users (cumulative)
- Show HN draft in sandbox, ready for Week 5

---

## 6. Re-usable artifacts (write once, cross-post forever)

Build these in Week 1. Each one is referenced 4–10 times across the calendar.

### A. danlab.dev homepage (v111 NEW)
- React + Vite + Tailwind CSS 4, `<1MB` total page weight
- Hero: "A proactive AI on your face. Open source. From India."
- 9-daemon matrix table with real `/status` payloads as examples
- Comparison table: Quark / Meta / Dan (privacy column)
- Telegram surface (`@danlab_bot`) in the footer
- No third-party trackers for 30 days

### B. Architecture one-pager
- 1-page landscape PDF, 5 layers (hardware, services, gateway, agents, app).
- Lives at `danlab.ai/architecture.pdf` and in every repo root.
- Re-use: every "how does Dan Glasses work?" answer. Also embedded in press kit.

### C. Comparison table (Quark / Meta / Dan)
- ASCII in tweet form, image form for LinkedIn / YouTube.
- Re-use: every privacy pitch. Refresh quarterly when competitors ship.

### D. The 9 daemons live demo
- 60-second screen capture of the full daemon matrix.
- Re-use: every "we shipped this" tweet. Pinned on GitHub.

### E. asciinema recording of danlab-multimodal heuristic loop
- 90-second terminal capture, 92/100 avg score.
- Re-use: lead magnet, every "are we real?" pitch. Hosted on https://zo.pub/som/danlab-multimodal-demo

### F. The 8-agent workflow map (Track B)
- 1-page diagram of the 8 Paperclip workflows × integrations.
- Re-use: every Dan Voice pitch. Refresh when we ship an agent.

### G. Telegram pairing one-pager (v111 NEW)
- 30-second GIF showing DM → pairing → first question
- Re-use: every post that mentions `@danlab_bot`

---

## 7. Metrics weekly review (Monday 10:00 IST)

Single Google Sheet (or markdown in `/dan-glasses/agent-work/weekly-metrics/`):

- danlab.dev unique visitors, bounce rate
- GH stars total, per repo (6 hero repos)
- X impressions per tweet, profile visits
- LinkedIn impressions per post, follower delta
- YouTube views per video, retention curve
- danlab.ai blog page-views, time-on-page
- @danlab_bot paired users (cumulative), DAU, queries/user/day
- Show HN points (when posted)

**Stop-doing triggers** (kill a channel after 4 weeks of <X results):
- X: <1k impressions per week
- LinkedIn (company): <200 impressions per post
- danlab.ai blog: <500 page-views per month
- Telegram: <10% D7 retention
- YouTube Shorts: <500 views per video

---

## 8. Content production rules (v111, unchanged)

- **Pre-write Mondays.** Sit down for 90 min on Monday morning. Write 3 drafts. Park them in a `drafts/` folder.
- **Ship Tuesday + Thursday + Saturday** by default. Stagger so each channel sees the same artifact only twice per week.
- **No editing on ship-day.** Drafts are pre-approved by Sunday evening.
- **Every post has a CTA**, even if the CTA is "read the code" or "DM @danlab_bot".
- **Re-use is mandatory.** A tweet idea that bombs becomes a Substack footnote.
- **v111 addition:** Daemon-of-the-week posts ship a real `curl` payload. Not a mockup.

---

## 9. Holiday / event calendar (v111, unchanged)

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

## 10. v111 week-by-week summary (one-liner per week)

- **Week 1:** danlab.dev refresh + 9/9 claim verified + Telegram wired.
- **Week 2:** Architecture deep-dive + perceptiond (LFM2.5) + Show HN draft for Paperclip.
- **Week 3:** Dan Voice drops + memoryd + Telegram bot feature drop.
- **Week 4:** Dan Glasses hardware + toold + Show HN draft for dan-glasses.

---

*Content calendar complete. v111 Twitter pack, landing copy, and README suggestions live in sibling files.*

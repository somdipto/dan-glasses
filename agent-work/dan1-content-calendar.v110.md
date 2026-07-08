# DanLab Content Calendar — Run v110
**Date:** 2026-06-29
**Owner:** DAN-1
**Cadence:** 30-day rolling window. Refresh every Monday.
**Cross-ref:** [marketing strategy §3 (channels)](./dan1-marketing-strategy.v110.md)

---

## 0. Operating principles

1. **No fluff.** Every post ships a code link, a metric, or a demo. No "excited to announce" without a payload.
2. **One idea per post.** Twitter thread counts as one. Blog post is one. YouTube demo is one.
3. **One CTA per week.** Per channel. Cross-posts without separate CTAs.
4. **Owner + review.** Every artifact names one person who ships it and one who reviews.
5. **Tagging.** Every artifact lists: `#track-a` (Dan Glasses wearable), `#track-b` (Dan Voice app), `#research` (multimodal / SIA), or `#platform` (Paperclip / OpenClaw). This lets us measure channel-product fit later.

---

## 1. Channels — inventory + cadence

| Channel | URL / handle | Posts/week | Best for | Owner |
|---|---|---|---|---|
| **GitHub Discussions** | github.com/somdipto/* | 2 | Engineering drop notes | somdipto |
| **X / Twitter** | @danaboratory (TBD) | 5 (1 thread, 3 stand-alone, 1 hot-take) | Build-in-public, hot takes | somdipto |
| **LinkedIn — somdipto** | linkedin.com/in/somdipto | 2 | Hire signal, India-origin narrative | somdipto |
| **LinkedIn — company** | linkedin.com/company/danlab-dev | 1 (cross-post of Twitter thread) | B2B credibility | somdipto |
| **YouTube Shorts** | youtube.com/@danaboratory | 1 | 30–90s demos | somdipto + editor |
| **YouTube long-form** | same | 1/month | Conference talks, architecture deep-dives | somdipto |
| **Hacker News (Show HN)** | news.ycombinator.com | 1/month | Initial spike for any major drop | somdipto |
| **RSS blog** | danlab.ai/blog | 1/month | Long-form technical posts | somdipto |
| **Substack / Beehiiv** | danaboratory.substack.com | 1/month | Mirror of long-form + paid gate | somdipto |

**Total output (per week):** ≈ 10 net posts. Sustainable. No burnout.

---

## 2. Week 1 — Foundation drops (June 30 – July 6)

**Theme:** "We are 9-of-9 daemons live. Open source. From India."

| Day | Channel | Format | Topic | Asset / link | Owner |
|---|---|---|---|---|---|
| Mon | GitHub | Release note | `dan-glasses` v109 release: 9/9 daemons up | tag + change log | somdipto |
| Mon | X | Single tweet | "9 of 9 daemons live. Open source. India-first." | screenshot of `up.sh` matrix | somdipto |
| Tue | LinkedIn (somdipto) | 3-paragraph post | "Why we chose Tauri over Electron for a wearable companion app" | link to TECHNICAL_NOTES | somdipto |
| Wed | X | 6-tweet thread | "How to build a proactive AI wearable on a $0 budget" (link build plan) | link to /docs/dan-glasses-build-plan.md | somdipto |
| Thu | YouTube Shorts | 60s screen-recording | "All 9 Dan Glasses daemons running in one minute" | capture output of `./scripts/up.sh` | somdipto |
| Fri | X | Hot-take | "Most AI assistants are reactive. Ours watches the room. Thread 👇" (tease next week’s demo) | none | somdipto |
| Sat | GitHub | Discussion post | "Roadmap for Q3: which Paperclip agent should we ship first?" | poll options | somdipto |

**Week-1 metric targets:**
- 100 GitHub stars across org (currently ~50 estimated)
- 500 X impressions on the thread
- 100 LinkedIn impressions on the technical post

---

## 3. Week 2 — Architecture deep-dive (July 7 – 13)

**Theme:** "How 7 services + an OpenClaw gateway become one proactive agent."

| Day | Channel | Format | Topic | Asset / link | Owner |
|---|---|---|---|---|---|
| Mon | RSS blog | 1,500-word post | "The watchful loop: how perceptiond decides what is worth seeing" | code from perceptiond/ | somdipto |
| Tue | X | 4-tweet thread | "The 5 lines of code that make audiod actually ship-ready (readiness probe)" | link to audiod/SPEC.md | somdipto |
| Wed | LinkedIn (company) | Cross-post of Mon blog | same | — | somdipto |
| Thu | YouTube Shorts | 45s | "Demo: audiod 'audiod unreachable' chip turns red when whisper-cli is missing" | before/after screen capture | somdipto |
| Fri | X | Single tweet | Quote-of-the-week: most-quoted line from audiod v1.0 SPEC | quote + link | somdipto |
| Sat | GitHub | Discussion | "Heuristic vs SIA: when is the right time to flip the switch from hand-coded to learned?" | link to SIA repo | somdipto |
| Sun | Substack | Mirror of Mon blog + 1-paragraph subscriber-only commentary | — | — | somdipto |

---

## 4. Week 3 — Track B (Dan Voice) drops (July 14 – 20)

**Theme:** "Your earbuds are now a Jarvis. No hardware purchase."

| Day | Channel | Format | Topic | Asset / link | Owner |
|---|---|---|---|---|---|
| Mon | RSS blog | 1,200-word post | "How EigenCloud containers per user beat every consumer AI cloud today" | link to PRD_DAN_VOICE.md | somdipto |
| Tue | X | 5-tweet thread | "8 Paperclip agent workflows that replace $400/mo of SaaS" | link to DanGlasses/ARCHITECTURE.md | somdipto |
| Wed | LinkedIn (somdipto) | Personal essay | "I am building a Jarvis that ships in 8 weeks. Here is the PRD." | link to PRD | somdipto |
| Thu | YouTube Shorts | 60s | "Demo: 'Hey Dan — summarize the last email from Mom'" (mock, voice + audio wave) | AI-generated voice sample | somdipto |
| Fri | X | Single tweet | "Privacy by architecture: a comparison table — Meta / Quark / Dan" | ASCII table | somdipto |
| Sat | GitHub | Discussion | "Which OAuth provider should we ship first in Dan Voice? Gmail vs Notion vs Calendar" | poll | somdipto |

---

## 5. Week 4 — Track A (Dan Glasses wearable) drops (July 21 – 27)

**Theme:** "9/9 daemons running on a Linux laptop. Now let’s put it on your face."

| Day | Channel | Format | Topic | Asset / link | Owner |
|---|---|---|---|---|---|
| Mon | RSS blog | 1,500-word post | "The 4 glasses hardware tradeoffs nobody tells you about" | numbered list | somdipto |
| Tue | X | 6-tweet thread | "Why the 200–250 mAh battery was wrong, and what we changed to 400–450 mAh" | chart | somdipto |
| Wed | LinkedIn (company) | Cross-post | — | — | somdipto |
| Thu | YouTube Shorts | 90s | "Dan Glasses — desktop prototype demo (3 services live, no cloud)" | screen capture | somdipto |
| Fri | X | Hot-take | "Glasses at $99 make smart-glasses a daily-driver category. The math proves it." | 3 bullet math | somdipto |
| Sat | GitHub | Discussion | "BOM cost of v1 vs v1.5 vs v2 — does the math hold up?" | spreadsheet link | somdipto |
| Sun | Show HN draft | Sandbox review | "Show HN: Dan Glasses — proactive AI wearable, 9 daemons, open source" | — | somdipto + reviewer |

---

## 6. Re-usable artifacts (write once, cross-post forever)

Build these once in Week 1. Each one is referenced 4–10 times across the calendar.

### A. Architecture one-pager
- 1-page landscape PDF, 5 layers (hardware, services, gateway, agents, app).
- Lives at `danlab.ai/architecture.pdf` and in every repo root.
- Re-use: every "how does Dan Glasses work?" answer. Also embedded in press kit.

### B. Comparison table (Privacy / Meta / Quark / Dan)
- ASCII in tweet form, image form for LinkedIn / YouTube.
- Re-use: every privacy pitch. Refresh quarterly when competitors ship.

### C. The 9 daemons live demo
- 60-second screen capture of `./scripts/up.sh` output.
- Re-use: every "we shipped this" tweet. Pinned on GitHub.

### D. asciinema recording of danlab-multimodal heuristic loop
- 90-second terminal capture, 92/100 avg score.
- Re-use: lead magnet, every "are we real?" pitch. Hosted on https://zo.pub/som/danlab-multimodal-demo.

### E. The 8-agent workflow map (Track B)
- 1-page diagram of the 8 Paperclip workflows × integrations.
- Re-use: every Dan Voice pitch. Refresh when we ship an agent.

---

## 7. Metrics weekly review (Monday 10:00 IST)

Single Google Sheet (or markdown in `/dan-glasses/agent-work/weekly-metrics/`):

- GH stars total, per repo (5 hero repos)
- X impressions per tweet, profile visits
- LinkedIn impressions per post, follower delta
- YouTube views per video, retention curve
- RSS blog page-views, time-on-page
- Show HN points (when posted)

**Stop-doing triggers** (kill a channel after 4 weeks of <X results):
- X: <1k impressions per week
- LinkedIn (company): <200 impressions per post
- RSS blog: <500 page-views per month

---

## 8. Content production rules (so it actually ships)

- **Pre-write Mondays.** Sit down for 90 min on Monday morning. Write 3 drafts. Park them in a `drafts/` folder.
- **Ship Tuesday + Thursday + Saturday** by default. Stagger so each channel sees the same artifact only twice per week.
- **No editing on ship-day.** Drafts are pre-approved by Sunday evening.
- **Every post has a CTA**, even if the CTA is "read the code".
- **Re-use is mandatory.** A tweet idea that bombs becomes a Substack footnote.

---

## 9. Holiday / event calendar (overlaid)

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

*Content calendar complete. Twitter content + landing-page copy + README suggestions v110 written to follow.*

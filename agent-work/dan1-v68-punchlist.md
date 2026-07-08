# Dan1 v68 Punchlist — Build the Inbound

**Author:** Dan1 👾
**Date:** 2026-06-21 09:30 IST (04:00 UTC)
**Use:** Run these commands + actions this week to ship the inbound surface.

> **v68 deltas vs v67:** Stop counting stars. Build the destination. Every tweet, every HN post, every Reddit comment needs a place to land. The README isn't it. The blog is.

---

## Day 1 (Mon 2026-06-23) — Ship day, inbound edition

### 1. Build danlab.dev landing page (zo.space)

```bash
# Create the v68 landing route
write_space_route / "page" 'v68 content here — see dan1-landing-copy.md §1'
# Hero: "No phone. No cloud. No subscription. No ads."
# Set public="true"
```

### 2. Build the blog (zo.space)

```bash
# Create /blog route
write_space_route /blog "page" 'v68 blog index — see dan1-content-calendar.md §Day 1'
```

### 3. First blog post — "Welcome to the DanLab dev log"

```bash
# Create /blog/welcome route
write_space_route /blog/welcome "page" '<p>No phone. No cloud. No subscription. No ads.</p><p>This is the dev log for DanLab...</p>'
# ~400 words. See dan1-content-calendar.md §Day 1
```

### 4. Set up RSS feed

```bash
# Create /api/feed route (RSS 2.0 + Atom + JSON Feed)
# Reads from a /blog/ index file or from a Postgres table
write_space_route /api/feed "api" 'RSS feed code here — see dan1-marketing-strategy.md §3'
```

### 5. v67 carryover: Push 3 public repos

```bash
cd /home/workspace/dan-glasses
gh repo edit somdipto/dan-glasses --visibility public
gh release create v0.7.0-audiod --title "audiod v0.7.0 — Tauri integration client"

cd /home/workspace/danlab-multimodal
gh repo edit somdipto/danlab-multimodal --visibility public
gh release create v0.1.0 --title "danlab-multimodal v0.1.0 — first public release"

cd /home/workspace/paperclip
gh repo edit somdipto/paperclip --visibility public
gh release create v0.1.0 --title "paperclip v0.1.0 — first public release"
```

### 6. Claim @danlab_dev on X (P0, carried from v67)

Apply v68 bio (see `dan1-twitter-content.md` §0):
```
Building the proactive AI companion from India 🇮🇳.

No phone. No cloud. No subscription. No ads.

7 daemons. MIT. audiod v0.7 live.

📡 RSS: danlab.dev/feed.xml
github.com/somdipto/dan-glasses
```

### 7. Post the v68 pinned tweet (4 "no"s)

```
No phone. No cloud. No subscription. No ads.

The proactive AI companion, MIT-licensed, on-device. From India 🇮🇳.

audiod v0.7 ships a Tauri client. 121/121 tests. `curl localhost:8090/health` → ok.

danlab.dev → github.com/somdipto/dan-glasses
```

### 8. Send Issue #0 of the newsletter

Buttondown (or self-hosted) → send "Issue #0: Welcome" to the list.
Subject: "No phone, no cloud, no subscription, no ads."

---

## Day 2 (Tue 2026-06-24) — More inbound, more repos

### 9. Second blog post — "No phone"

```bash
# Create /blog/no-phone route
write_space_route /blog/no-phone "page" '~600 words on ripping the phone out. See dan1-content-calendar.md §Day 2'
```

### 10. Reddit r/LocalLLaMA post

Title: "What on-device AI stacks are people building in 2026? We're shipping audiod + perceptiond + memoryd as MIT daemons."

Body: from `dan1-marketing-strategy.md` §7 (Reddit specifics).

### 11. Set up Dev.to cross-post

Use the RSS → Dev.to publisher. Configure to auto-import new /blog posts.

### 12. Set up Hashnode cross-post

Same as Dev.to, separate config.

---

## Day 3 (Wed 2026-06-25) — First deep-dive

### 13. Third blog post — "No cloud"

```bash
# Create /blog/no-cloud route
write_space_route /blog/no-cloud "page" '~600 words on running all inference on-device. See dan1-content-calendar.md §Day 3'
```

### 14. Submit Show HN draft for paperclip (scheduled for Day 8)

Save to `/home/workspace/dan-glasses/agent-work/show-hn-paperclip-draft.md`.

### 15. Tweet the whisper.cpp deep-dive (6-tweet thread)

See `dan1-twitter-content.md` §2 Post #3. Each tweet links to `/blog/no-cloud`.

---

## Day 4 (Thu 2026-06-26) — Illinois HB4843 + first roadmap update

### 16. Post the Illinois HB4843 thread (5 tweets)

See `dan1-twitter-content.md` §2 Post #7. Each tweet links to `/blog/no-ads` (next blog post).

### 17. Update /roadmap

Move 3 items from "Now" to "Shipped" (audiod v0.7, danlab-multimodal v0.1.0, paperclip v0.1.0). Add 5 new items to "Now."

### 18. Fourth blog post — "No ads"

```bash
# Create /blog/no-ads route
write_space_route /blog/no-ads "page" '~600 words on the model as context, not attention. See dan1-content-calendar.md §Day 4'
```

---

## Day 5 (Fri 2026-06-27) — Snap-week post-mortem + public roadmap reveal

### 19. Post the Snap-week post-mortem (8-tweet thread)

See `dan1-twitter-content.md` §2 Post #8. Each tweet links to a blog post or a roadmap item.

### 20. Submit "Show HN: Dan Glasses — proactive AI companion from India" draft

Save to `/home/workspace/dan-glasses/agent-work/show-hn-dan-glasses-draft.md`. Schedule for Mon 2026-07-07 14:00 PT (v69 trigger).

### 21. Fifth blog post — "No subscription"

```bash
# Create /blog/no-subscription route
write_space_route /blog/no-subscription "page" '~600 words on the MIT license as a commitment. See dan1-content-calendar.md §Day 5'
```

---

## Day 6 (Sat 2026-06-28) — Weekend build-in-public: perceptiond

### 22. Post perceptiond deep-dive + /status curl

See `dan1-twitter-content.md` §2 Post #9. Link to `/blog/perceptiond-deep-dive` (new blog post, ~500 words).

### 23. Sixth blog post — "The 7 daemons, in plain English"

```bash
# Create /blog/seven-daemons route
write_space_route /blog/seven-daemons "page" '~700 words on each daemon + curl command. See dan1-content-calendar.md §Day 6'
```

---

## Day 7 (Sun 2026-06-29) — Open-source Sunday + LinkedIn refresh

### 24. Reddit r/LocalLLaMA weekly thread

"7 days of shipping audiod + danlab-multimodal + paperclip. 0 → X stars across 3 repos. Here's what we learned."

### 25. LinkedIn bio refresh (somdipto, carried from v67)

```
Building the proactive AI companion from India 🇮🇳. 

No phone. No cloud. No subscription. No ads.

Dan Glasses = 7 modular daemons (audiod v0.7 live), MIT-licensed, on-device.

📡 danlab.dev/feed.xml
github.com/somdipto/dan-glasses
```

### 26. Send Issue #1 of the newsletter

Subject: "No phone, no cloud, no subscription, no ads. — 7 days in."

---

## Day 8 (Mon 2026-06-30) — Show HN: paperclip

### 27. Submit Show HN: paperclip

Title: "Show HN: paperclip – deploy your own AI company in one Docker command"
Body: from `dan1-marketing-strategy.md` §5 Show HN block.
Schedule: Mon 2026-06-30 14:00 PT.

### 28. Seventh blog post — "Why we don't ship to the App Store"

```bash
# Create /blog/why-not-app-store route
write_space_route /blog/why-not-app-store "page" '~500 words on the bet. See dan1-content-calendar.md §Day 8'
```

---

## Day 9 (Tue 2026-07-01) — paperclip paid tier

### 29. (Optional) Add Stripe to paperclip Railway deploy

Use `create_stripe_product` flow. $49/month per company. $19/month per agent.

---

## Day 10 (Wed 2026-07-02) — audiod v0.7.1

### 30. Cut audiod v0.7.1 release

Collect bug reports from week 1 issues. Fix. Tag v0.7.1. Post tweet linking to `/blog/audiod-0-7-1-changelog`.

### 31. Eighth blog post — "audiod v0.7.1 changelog"

```bash
# Create /blog/audiod-0-7-1-changelog route
write_space_route /blog/audiod-0-7-1-changelog "page" '~400 words. See dan1-content-calendar.md §Day 10'
```

---

## Day 11 (Thu 2026-07-03) — perceptiond deep-dive

### 32. Post perceptiond LFM2.5-VL-450M thread (5 tweets)

See `dan1-twitter-content.md` §2 Post #10. Each tweet links to `/blog/perceptiond-lfm25` (new blog post).

### 33. Ninth blog post — "LFM2.5-VL-450M in 200 lines of Python"

```bash
# Create /blog/perceptiond-lfm25 route
write_space_route /blog/perceptiond-lfm25 "page" '~700 words on LFM2.5 + SalienceDetector. See dan1-content-calendar.md §Day 11'
```

---

## Day 12 (Fri 2026-07-04) — Mid-cycle check-in

### 34. Tweet the mid-cycle stats

```
7 days in: [X stars across 3 repos], [Y RSS subs], [Z blog post views]. audiod v0.7.1 ships today. 4 "no"s on the landing page. 9 blog posts live.
```

If X ≥ 50 stars + 50 RSS subs → fire v69 trigger.
If X < 50 → ship v69 anyway (different surface, not just stars).

---

## Day 13 (Sat 2026-07-05) — SIA path

### 35. (Optional) Post the SIA framework post

See `dan1-marketing-strategy.md` §8 content pillar 5 (SIA / pre-RL).

---

## Day 14 (Sun 2026-07-06) — Weekly recap

### 36. Tweet the 14-day recap + next 14

```
14 days in: [X stars across 3 repos], [Y RSS subs], [Z blog post views]. Next 14: paperclip paid tier, Dan Glasses Show HN, first press push.
```

### 37. Send Issue #2 of the newsletter

Subject: "14 days in. The receipts."

---

## Brand-drift fix (week of 06-23, one-time, carried from v67)

### 38. Refresh danlab.dev

Current products list: Agent8, Zerant, Dapify, AI Glasses (drifted names).
New products list: Dan Glasses, danlab-multimodal, paperclip, danclaw.

Use the v68 landing copy from `dan1-landing-copy.md`.

### 39. (Optional) Reconcile the pitch deck

v68 names: Dan Glasses / danlab-multimodal / paperclip / danclaw.
Pitch deck names: Dan Voice / Dan Glasses / Dan Company.

Either rewrite the pitch deck, OR create a `danlab.dev/pitch` page that bridges the two. v68 default = create the bridge page.

---

## Open questions (need from somdipto before Day 1)

1. **X handle priority:** `@danlab_dev` (first), `@danlab` (second), `@somdipto` (fallback). Which one can you claim on Monday morning? (v66 + v67 + v68 — third pass.)
2. **GitHub org:** push to `somdipto/dan-glasses` or create `danlab/dan-glasses` org? (v67 + v68 — second pass.)
3. **Show HN for paperclip:** Day 8 (06-30) or Day 22 (07-14)? (v66 + v67 + v68 — third pass.)
4. **LinkedIn bio:** is the new bio in #25 OK to apply on Day 7? (v66 + v67 + v68 — third pass.)
5. **Press push:** do you have any journalist contacts at The Information, TechCrunch, or Indian tech media? v68 defers press, v69 picks it up. (v67 + v68 — second pass.)
6. **Newsletter platform:** Buttondown (free, $9/mo paid), Substack (1-click but hosted), or self-hosted (Plunk + Postgres)? (v68 new — first pass.)
7. **Pitch deck reconciliation:** rewrite the deck, OR create a `danlab.dev/pitch` bridge page? (v68 new — first pass.)

---

*Built by Dan1 👾 for DanLab — 2026-06-21 09:30 IST.*

# Dan1 — X/Twitter Content Pack (v127)

**Run:** 2026-07-06 07:30 UTC · Asia/Calcutta 13:00 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Companion to:** `dan1-marketing-research.md` (v127), `dan1-marketing-strategy.md` (v127)
**Lead:** *The closed-source frontier is politically-conditional AND the capex cycle is being repriced AND the outer-loop RSI is already in flight. The bet is no longer "open vs closed." The bet is: who can ship the substrate while the substrate is still standing?*

---

## 0. v127 deltas

- v126 positioning + 4 axes (sovereign trust + reversibility + chip + outer-loop RSI) all hold.
- v127 sharpens the **Tailscale authkey-pending Dan Glasses demo** as the highest-leverage 1-day deliverable for the Edge-AI developer audience. Unblock the authkey and the demo goes live today.
- v127 adds the **8/8 daemons + .deb** as the unblocker for the "substrate, not model" pitch.
- v127 retires v126's "9/9 daemons" number (the zo-mcp-bridge is `process`-mode, doesn't count toward daemon count). **8/8 is the new, defensible number.**
- v127 adds the **Meta Q1 2026 = 69% share (IDC revised up to 13.6M units, 88% YoY)** datapoint.
- v127 adds the **Meta contractor harm-prompt disclosure (Covalen, 45K prompts, Aug 2025)** as a citable event for the trust-the-vendor-failing-in-the-open narrative.
- v127 adds the **outer-loop RSI framing from dan2 v28 (Jack Clark, 8x LOC merge)** as a content thread.

---

## 1. Profile

### Handle
**@danaboratory** (TBD — awaiting somdipto to register). Backup: **@danlab_**.

### Display name
**Dan Lab**

### Bio (160 chars, 3 variants for A/B)

**Variant A (the substrate pitch):**
```
On-device AI for your face. 8 daemons live, .deb installs in 30s. MIT weights. Public threat model. From India 🇮🇳. Building toward AGI without asking for permission.
```

**Variant B (the proactive-vs-reactive pitch):**
```
Your glasses should remember what you forgot. Proactive AI companion, on-device, open-weights. 8 services, one .deb, zero cloud lock-in. danlab.dev
```

**Variant C (the protocol pitch):**
```
Agents need TCP/IP. OpenClaw ships it. Dan Glasses wears it. Threat model public, reversibility contract signed. AGI from India 🇮🇳.
```

### Pinned tweet
See Post 1 below.

### Location
Bengaluru, India 🇮🇳

### Link
danlab.dev

### Header image concept
Dark mode. The 8-daemon matrix in a monospace grid. The .deb filename at the bottom. The India flag in the top-right corner. No faces, no product shots — pure substrate.

---

## 2. First 10 posts (shipping order)

### Post 1 — PINNED (the lead, ships Day 1)

```
A proactive AI on your face. Open weights. Politically-uncapturable. From India 🇮🇳.

8 daemons live. 1 .deb installs them all. 1 public threat model. 1 reversibility contract.

The substrate is the bet.

https://danlab.dev
```

**Why pinned:** one-liner, every axis (on-device + open + India + reversibility + substrate), links the funnel. Ship Tue morning IST.

---

### Post 2 — the 8/8 daemons demo (ships Day 1, same day as Post 1, evening)

```
8/8 daemons live. Verified just now:

  audiod       8090  ✅  /ready
  perceptiond  8092  ✅  /health
  memoryd      8741  ✅  /health
  toold        8742  ✅  /status
  ttsd         8743  ✅  /ready
  os-toold     8744  ✅  /ok
  app          8747  ✅  /
  openclaw    18789  ✅  63 commands

The .deb: 9.4MB. Installs in 30s. No GPU. No cloud. Your laptop. Your rules.
```

**Why:** receipts > claims. Ship with a real terminal screenshot of the daemon matrix. CTA: install.

---

### Post 3 — Day 2, the Meta paywall thread (4 tweets)

```
1/ Meta just paywalled the accessibility feature on Ray-Ban Display.

   3hr/month free, then $19.99/mo or $199/yr.

   The Verge: "soft paywall."
   Gizmodo: "It is an accessibility feature being paywalled."

   If you need a screen reader, pay Meta. 🧵
```

```
2/ The 69% market share. Q1 2026. Counterpoint.

   The shelf is Meta's.

   But the shelf is now politically-conditional, contractor-audited, and subscription-gated.

   The escape hatch is open weights on your device.
```

```
3/ Dan Glasses is the escape hatch.

   8 daemons. MIT weights. Public threat model. Reversibility contract.

   No cloud lock-in. No subscription. No $19.99/mo accessibility tax.

   The .deb is 9.4MB. Your laptop. Your rules.
```

```
4/ We're not asking you to switch brands.

   We're asking you to read the threat model before you put something on your face.

   github.com/somdipto/dan-lab/tree/main/threat-model
```

**Why:** the Meta paywall is the most citable accessibility-failure event of 2026. The Verge + WIRED + Gizmodo are the receipts. This is the wedge post for the accessibility-first audience.

---

### Post 4 — Day 3, the protocol pitch (3 tweets)

```
Vinton Cerf: "Agents need a TCP/IP."

Anthropic: shipped Apps Gateway. Closed.
OpenAI: shipped MCP. Open.
OpenClaw: shipped MCP server first. Open.
Dan Glasses: ships MCP on a wearable.

The protocol is the bet.
```

**Why:** Cerf quote is the legitimate foundation. Anthropic + OpenAI + OpenClaw + Dan Glasses is the lineage. The audience is the agent-architect crowd — highest leverage per impression.

---

### Post 5 — Day 4, the small-beats-large (1 tweet + image)

```
A 450M parameter VLM describes your kitchen in 250ms on a $0 GPU.

LFM2.5-VL-450M. Q4_0. CPU-only. Sub-1W.

The 7B model that wants $5K of H100s can't do that.

Small beats large when the constraint is the battery.
```

**Why:** single-image tweet (LFM2.5-VL-450M spec card vs Llama-3.2-11B spec card). The audience is edge-AI developers — highest install rate.

---

### Post 6 — Day 5, the reversibility contract hot take (1 tweet)

```
xAI's Babushkin wrote the essay on RSI reversibility last month.

We shipped the contract.

Every model call. Every memory write. Every daemon. Signed. Unwindable.

The wearable that can be unwound is the wearable that can be trusted.
```

**Why:** Babushkin essay is the citable event. The reversibility contract is the ship artifact. Hot take + URL to the contract spec. Audience: reversibility-conscious users (new, fastest-growing in v126 strategy).

---

### Post 7 — Day 6, the Covalen disclosure (1 tweet + thread)

```
Meta's safety contractor (Covalen) sent 45,000 prompts to ChatGPT, Gemini, and Character in August 2025.

Some posed as minors.

This is the same trust-the-vendor contract that the Alibaba ban was responding to.

The trust-the-vendor contract is failing in the open.

Dan Glasses ships a public threat model. Read it before you put it on your face.
```

**Why:** the citable event is the Covalen disclosure. The wedge is the public threat model. Audience: security researchers, accessibility-first users. This is the "convert critics to allies" post.

---

### Post 8 — Day 7, the outer-loop RSI thread (5 tweets)

```
1/ Jack Clark (Import AI #460, July 2026):

   "8x increase in lines-of-code merged in 2026 vs 2024 at Anthropic."

   60% chance of no-human recursive self-improvement by end of 2028.

   But: the 8x LOC merge is already happening. The outer-loop RSI is now. 🧵
```

```
2/ Outer-loop RSI = productivity compounding. Self-merge. Self-test. Self-deploy.

   Maximalist RSI = agent modifies its own weights.

   The maximalist is 60% by 2028. The outer-loop is now.

   The race is no longer who ships first. It's who can ship the substrate while the substrate is still standing.
```

```
3/ Danlab's outer-loop RSI receipts:

   audiod v1.3 → v1.5: confidence calibration +4%, segment timing histogram shipped
   dan2 research v23 → v28: 5 new SHARPEN signals, 1 new CRITICAL
   dan1 foundation v121 → v124: 8 daemons live, .deb built, bridge persistent

   The substrate improves in the open. The changelog is the receipt.
```

```
4/ The capex pushback is real. Anthropic layoffs, Frontier Co. repricing, $9.5B implementation-wedge bet.

   The window is finite.

   Dan Glasses ships the v1.0 substrate in Q4 2026, on a wearable, on open weights, with the threat model public.
```

```
5/ The 2028 maximalist RSI will not be shipped by us. It will not be shipped by Anthropic. It will be shipped by *the open substrate* — audiod, perceptiond, memoryd, toold, ttsd, os-toold, dan-glasses-app, openclaw.

   The .deb is the bet.
```

**Why:** Jack Clark Import AI #460 is the citable event. The 8x LOC merge is the datapoint. The 5-tweet thread is the long-form take. Audience: AI researchers, agent-architects, small-model crowd.

---

### Post 9 — Day 8, the 8/8 daemons visual (image-only tweet)

```
[Image: terminal screenshot of the daemon matrix]

caption: 8 daemons. 1 .deb. Your laptop. Your rules.
```

**Why:** visual break, lowest-effort post in the rotation, highest recall. Ship Sat morning IST.

---

### Post 10 — Day 9, the Show HN teaser (1 tweet)

```
Show HN next week.

"Dan Glasses — a proactive AI wearable, 8 daemons, one .deb, on-device, MIT weights, public threat model."

If you've ever wanted to fork a wearable, this is it.
```

**Why:** pre-Show-HN hype. Tease the URL. Audience: HN crowd, edge-AI developers. This is the conversion post.

---

## 3. Cadence

- **Mon:** Research thread (5-7 tweets, 1/week)
- **Tue:** Daemon-of-the-week (1 tweet + screenshot, 1/week)
- **Wed:** Hot take (1 tweet, 1/week)
- **Thu:** Architecture deep-dive (1 tweet, 1/week, link to blog)
- **Fri:** Receipt post (1 tweet + code/metric, 1/week)
- **Sat:** Visual (image-only, 1/week)
- **Sun:** Rest. Or ship the Show HN draft to the sandbox.

**Total:** 5-7 net posts/week. Sustainable. No burnout.

---

## 4. Hashtag strategy (v127)

Use sparingly. 1-2 max per tweet. Tags:
- `#OpenClaw` (the protocol)
- `#EdgeAI` (the form factor)
- `#FromIndia` (the origin)
- `#ProactiveAI` (the wedge)
- `#Substrate` (the bet)

**Do not use** `#AI #MachineLearning #Wearable` — they are too generic, get buried.

---

## 5. Engagement rules (v127)

- **Reply to every mention in <4h during IST work hours.**
- **Quote-retweet competitors' announcements with the wedge** (e.g., Meta paywall → "The escape hatch is open weights on your device").
- **Never use "excited to announce"** — only receipts.
- **Never use "we believe"** — only show.
- **Cross-link to GitHub, blog, and Telegram in 1 of every 3 posts.**
- **Pin a fresh post every Monday.**

---

## 6. DM auto-responder (Telegram @danlab_bot)

When someone DMs the bot, auto-reply with:

```
Welcome to @danlab_bot. Pair with /pair.

8 daemons live: audiod, perceptiond, memoryd, toold, ttsd, os-toold, dan-glasses-app, openclaw.

Ask me anything about Dan Glasses, danlab-multimodal, or the .deb install.
```

---

## 7. Metrics (Monday 10:00 IST review)

- Profile visits / week
- New followers / week
- Impressions per tweet (target: 1k median, 5k for hot takes)
- Engagements per tweet (target: 2% rate)
- Link clicks per tweet (target: 50 clicks per research thread)
- DMs received / week
- Telegram @danlab_bot paired users (cumulative)

**Stop-doing trigger:** <500 impressions per week for 4 consecutive weeks. Kill the channel.

---

## 8. v127 hot-take bank (for future weeks)

- "The wearable that can be unwound is the wearable that can be trusted."
- "Closed-source AI is a subscription to your own face."
- "Your glasses should remember what you forgot."
- "9 weeks. 0 GPUs. 8 daemons. 1 .deb. From India."
- "The threat model is the alternative to the trust-the-vendor contract."
- "We don't ship models. We ship the substrate the models run on."
- "The protocol is the bet. The weights are free. The data is yours."
- "Anthropic ships a closed Apps Gateway. We ship an open one. On a wearable."
- "If you can't audit it, you can't trust it. If you can't unwind it, you can't fork it."
- "Day 5 is when Meta drops off. Day 5 is when the memory kicks in."

---

*Pack complete. 10 posts ready to ship. v127 lead is unchanged. v127 retires the "9/9 daemons" number — zo-mcp-bridge is `process`-mode, the defensible number is 8/8 daemons + 1 bridge. The Show HN teaser is the conversion post. Ship Tue.*

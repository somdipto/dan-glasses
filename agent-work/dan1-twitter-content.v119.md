# Dan1 — X / Twitter Launch Pack (v119)

**Run:** 2026-07-04 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Goal:** Ship the 10-post launch batch + the new bio for `@danlab` (or whatever somdipto confirms is available). v119 lead: **Tauri live + Cerf protocol + Anthropic fingerprinting counter-narrative.**

---

## 0. Bio (v119, 160 chars, single-voice)

**Primary — `@danaboratory` (recommended handle):**
> Open, on-device, wearable AI. 9 daemons live. 1 Tauri app published. 1 tailscaled substrate. 1 HF org. Vinton Cerf says we need a protocol — we shipped it. From Bengaluru 🇮🇳 DM @danlab_bot

**Alternative — `@danlab_dev`:**
> AI research + product lab. Open wearable agent. 9 daemons live, 1 Tauri app, 0 cloud calls, open protocol. From India. 🤝 DM @danlab_bot

**Alt short — `@danlab`:**
> Wearable AI, open weights, on-device. 9 daemons + 1 Tauri app live. 🇮🇳 → 🌍 DM @danlab_bot

**Personal — `@somdipto`:**
> Building Dan Glasses + Dan Voice. AI co-founder with Dani. 9 daemons + 1 Tauri app + 1 tailnet + 1 HF org. 0 cloud. 🇮🇳 danlab.dev

**v119 lead:** every bio ends with the bot handle. The bot is the always-on surface, and the bio is the first place the audience sees it. **v119 also surfaces the Tauri app URL and the Cerf line.**

**Pinned tweet (v119, lead):** see Post 0 below.

---

## 1. Post 0 — Profile launch + pinned tweet (v119)

> **Tauri v2 app is LIVE: https://dan-glasses-app-som.zocomputer.io**
>
> 9 daemons behind it. 0 cloud calls. audiod 8090. perceptiond 8092. memoryd 8741. toold 8742. ttsd 8743. os-toold 8744. dan-glasses-app 8747. openclaw 18789. tailscaled logged out — needs TAILSCALE_AUTHKEY. Somdipto, 60 seconds.
>
> Vinton Cerf (the internet's co-architect) said AI agents need TCP/IP. We shipped it on OpenClaw. Microsoft Scout is on the same substrate.
>
> First HF model cards up: SmolVLM-256M Q4_K_M (with mmproj) and LFM2.5-VL-450M Q4_0.
>
> Open source. From Bengaluru. DM @danlab_bot — it's live and it's the same stack the glasses will run. 👓
>
> github.com/somdipto/dan-glasses · github.com/somdipto/danlab-multimodal

*(Receipts: `curl localhost:{8090,8092,8741,8742,8743,8744,8747,18789}/ready` returns 200 from each port. The Tauri app loads at `dan-glasses-app-som.zocomputer.io`. tailscaled process is up but not joined.)*

---

## 2. The launch batch — first 10 posts (v119)

### Post 1 — Tauri live receipt (build-in-public, 1 tweet)

> Tauri v2 app is live: https://dan-glasses-app-som.zocomputer.io
>
> Behind it: 9 daemons on my Linux laptop. audiod 8090. perceptiond 8092. memoryd 8741. toold 8742. ttsd 8743. os-toold 8744. dan-glasses-app 8747. openclaw 18789. tailscaled (logged out, authkey pending).
>
> Open source. .deb + systemd. 0 cloud calls. github.com/somdipto/dan-glasses

### Post 2 — Origin (founder voice, 1 tweet)

> From India, you can't wait for the West to ship you intelligence. So you build it. 9 daemons live today, 1 Tauri v2 app published, 1 tailscaled substrate, 1 @huggingface org. Open source. MIT. The wearable is the payoff. The daemon stack is the receipt. 🇮🇳

### Post 3 — Cerf protocol (4-tweet thread) — v119 NEW LEAD

> **1/4** Vinton Cerf (the internet's co-architect, Open Frontier / Laude Institute, June 30 2026) said: "natural language is too ambiguous for reliable AI-agent-to-agent communication. We need formal, standardized protocols, much as TCP/IP did for the early internet."
>
> **2/4** We shipped it. OpenClaw is the protocol. Open weights, open source, MIT-licensed. The same substrate Microsoft Scout ships on. github.com/somdipto/dan-glasses
>
> **3/4** The wager: the agent layer is going to standardize the way the network layer did. The protocol is the bet. The wearable is the form factor. The data path is yours.
>
> **4/4** Cerf didn't build it. He endorsed the pattern. We built it on OpenClaw. Microsoft built Scout on it. The protocol is open. 🇮🇳

### Post 4 — HRM-Text-1B origin pillar (5-tweet thread) — v119, sharpened

> **1/5** A 1B model trained for $1,500 from scratch is now the SOTA small-reasoning model. Apache-2.0. Sapient just shipped HRM-Text-1B. github.com/Sapient-AI/hrn-text-1b
>
> **2/5** It will be the SIA Feedback-Agent in our v1.5 audiod post-processor. It will replace LFM2.5-1.2B-Thinking. The numbers: HRM-Text-1B wins on 3/4 evals.
>
> **3/5** The bet: small-beats-large is empirically real. VibeThinker-3B hits 94.3 AIME. The "bigger is better" era is over for narrow tasks.
>
> **4/5** The India thesis: you don't need 1T tokens to ship intelligence. You need a 1B model, an Apache-2.0 license, a $1,500 GPU bill, and a clear eval.
>
> **5/5** We are integrating HRM-Text-1B into audiod v1.5. Watch the audiod SPEC for the swap. Watch the HF model card. The post will write itself. 🇮🇳

### Post 5 — Anthropic fingerprinting counter-narrative (1 tweet) — v119 NEW

> Anthropic ships runtime-layer fingerprinting to enforce US export controls. Their engineer called it an "experiment we launched in March" (Gizmodo, June 2026). We do not. Architecturally cannot. No vendor can lock you out of your own glasses. github.com/somdipto/dan-glasses

### Post 6 — Salience-gating explainer (7-tweet thread) — v119, moved from week 5

> **1/7** Why our vision pipeline runs the VLM on *salient* frames, not fixed FPS. Battery math at the end.
>
> **2/7** Fixed FPS: 10fps × 1s VLM = 10 inferences. Queue: 1-2. Latency: 1-2s. Battery: dominated by VLM.
>
> **3/7** Salience-gated: motion detector + face Haar cascade. VLM fires only on salient frames. 5fps watchful, 10fps active, 0.5fps drowsy.
>
> **4/7** watchful: 5fps capture, VLM only on motion. queue=0. active: 10fps capture, VLM on every salient frame. queue=0. idle: 0.5fps, no VLM.
>
> **5/7** Battery math: VLM is 8-13W active, 2W watchful, 0.5W sleep. Salience-gating means the wearable is in watchful 90% of the time. Average draw: 2W.
>
> **6/7** 2500mAh @ 3.7V = 9.25Wh. 9.25Wh / 2W = 4.6 hours. The 4hr battery target holds. Fixed-FPS would be 1.5 hours.
>
> **7/7** Salience gating is the difference between a wearable that lasts a workday and one that lasts a meeting. Code: github.com/somdipto/dan-glasses/blob/main/Services/perceptiond/SPEC.md

### Post 7 — Microsoft Scout on OpenClaw (1 tweet)

> Microsoft Scout (Build 2026) is built on OpenClaw. So is Dan. We share a substrate with the largest enterprise software company on Earth. The substrate is open. The data path is yours. The enterprise threat is the substrate threat. We are aligned. github.com/somdipto/dan-glasses

### Post 8 — $14.5B / 120 days / 6-vendor implementation wedge (4-tweet thread) — v119 NEW

> **1/4** $14.5B / 120 days / 6-vendor. Microsoft + AWS + OpenAI + Anthropic + Google + IBM/Red Hat. The closed-source frontier is now spending on workbenches, not models.
>
> **2/4** IBM + Red Hat just committed $5B + 20,000 engineers to "Project Lightwell" — a subscription-based patching service. Athena coalition shipped 2,000 patches from 20,000 findings. Implementation, not models.
>
> **3/4** The wedge is no longer "open weights vs closed weights." It is "on-device implementation vs cloud workbenches." We are the on-device implementation layer. The daemon stack is the workbench.
>
> **4/4** 8 service daemons. 1 OpenClaw gateway. 1 tailscaled substrate. 1 Tauri v2 app. 0 cloud calls. github.com/somdipto/dan-glasses. The implementation wedge is the bet. 🇮🇳

### Post 9 — HuggingFace org launch (1 tweet, with the receipts) — v119 carries v118

> HuggingFace `danlab` org is live. First two model cards:
>
> 1. SmolVLM-256M Q4_K_M (120MB) + mmproj (182MB) — sub-250MB, on-device VLM, anchor to danlab-multimodal heuristic feedback loop (92/100 avg)
> 2. LFM2.5-VL-450M Q4_0 (209MB) — sub-250ms edge inference, 512×512, anchor to perceptiond SPEC
>
> Third card: HRM-Text-1B (Apache-2.0, $1,500 from scratch) when audiod v1.3 lands. Fourth: Kokoro-82M when ttsd v1.5 lands. 🇮🇳

### Post 10 — Telegram bot call-to-action (1 tweet, product surface) — v119, with Tauri URL

> DM @danlab_bot. Open the Tauri app: https://dan-glasses-app-som.zocomputer.io
>
> It's the same stack the glasses will run. 9 daemons + 1 gateway + 1 tailnet + 0 cloud. Ask the bot what audiod does. Ask it what perceptiond sees. Ask it what HRM-Text-1B costs to train.
>
> The wearable is the form factor. The bot is the first product surface. The Tauri app is the receipts. 🇮🇳

---

## 3. The 5 v119 lead posts (re-rank)

If we can only ship 5 posts in week 1, ship these:

1. **Post 0 (Pinned)** — Tauri live + Cerf + Tailscale unblocker
2. **Post 1 (Tauri live receipt)** — 9 daemons + Tauri URL
3. **Post 3 (Cerf protocol thread)** — 4-tweet thread, industry-icon endorsement
4. **Post 5 (Anthropic fingerprinting counter-narrative)** — 1 tweet, privacy wedge
5. **Post 10 (Bot + Tauri CTA)** — 1 tweet, two URLs, one story

Everything else is week 2+.

---

## 4. Posting cadence (v119, week 1)

| Day | Time (IST) | Post | Notes |
|---|---|---|---|
| **Sat Jul 4** | 09:00 | **Post 0** (pinned) | Tauri live + Cerf + Tailscale unblocker |
| **Sat Jul 4** | 09:05 | **Post 3** (start) | Cerf protocol thread pt 1 |
| **Sun Jul 5** | 10:00 | **Post 1** | Tauri live receipt (port matrix) |
| **Sun Jul 5** | 11:00 | **Post 3** (continue) | Cerf thread pts 2-4 |
| **Mon Jul 6** | 12:00 | **Post 10** | Bot + Tauri CTA |
| **Tue Jul 7** | 14:00 | **Post 5** | Anthropic fingerprinting counter-narrative |
| **Wed Jul 8** | 14:00 | **Post 4** (start) | HRM-Text-1B thread pt 1 |
| **Thu Jul 9** | 14:00 | **Post 4** (continue) | HRM-Text-1B thread pts 2-5 |

After week 1: 3-5 posts/week per the content calendar.

---

## 5. Replies to plan for (v119)

When these accounts tweet, reply within 4 hours:

- **@vgcerf** — anything on protocols / agent layer (v119 NEW — high priority)
- **@karpathy** — anything on small models / on-device
- **@jxmnop** (Jack Morris) — small-model beat, HRM-Text-1B
- **@MervinPraison** — VisualClaw, agent beat
- **@sama** — anything
- **@ylecun** — JEPA, world models
- **@drjimfan** — small models
- **@arankomatsuzaki** — papers
- **@_akhaliq** — papers
- **@huggingface** — model drops
- **@ollama** — on-device
- **@simonw** — LLM tooling
- **@rauchg** — agent infrastructure
- **@swyx** — AI engineering

Reply style: 1-2 sentences, no pitch, ship a link only if directly relevant. *No "thanks for sharing!" replies. Ever.*

**v119 NEW priority replies:**
- **@AnthropicAI** — any post on Mythos / Sonnet / Claude Code. Reply with the fingerprinting counter-narrative.
- **@Microsoft** — any post on Scout. Reply with "on OpenClaw. The substrate is open. The data path is yours."
- **@Google** — any post on Android XR. Reply with "aligned on the on-device thesis. We ship the wearable-grade version with 9 daemons + 0 cloud."

---

## 6. Hashtags (v119)

**Use sparingly.** 0-1 per post. The brand is the brand, not the hashtag.

- `#ondevice` — when relevant
- `#openweights` — when relevant
- `#wearable` — when relevant
- `#indieAI` — when relevant
- `#buildinpublic` — when relevant
- **v119 NEW:** `#protocol` — only on the Cerf thread

**Banned hashtags:** `#AI`, `#MachineLearning`, `#DeepLearning`, `#LLM`, `#GenAI`, `#Tech`, `#Innovation`. These are SEO bait, not signal.

---

## 7. v119 retractions from v118

- **v118 origin pillar (HRM-Text-1B $1,500) → v119 origin pillar (Cerf + HRM-Text-1B $1,500).** v119 leads with the protocol story; the model cost story is the second post, not the first.
- **v118 receipts surface (8 daemons + 1 gateway + 1 tailnet) → v119 receipts surface (8 daemons + 1 gateway + 1 tailnet + 1 Tauri app).** Every post can now end with two URLs: the bot handle and the Tauri URL.
- **v118 privacy line (architecturally cannot) → v119 privacy line (No vendor can lock you out of your own glasses, anchored to Anthropic fingerprinting).** Sharper, citable, viral-ready.

---

*— Dan1, Marketing & Growth, v119*
*See `dan1-marketing-research.v119.md` for the underlying research.*
*See `dan1-marketing-strategy.v119.md` for the broader Q3 plan.*
*See `dan1-content-calendar.v119.md` for the 90-day posting schedule.*
*See `dan1-landing-copy.v119.md` for the danlab.dev/glasses landing page.*
*See `dan1-github-readme-suggestions.v119.md` for README improvements across all repos.*

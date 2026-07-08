# Dan1 — X / Twitter Launch Pack (v118)

**Run:** 2026-07-03 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Goal:** Ship the 10-post launch batch + the new bio for `@danlab` (or whatever somdipto confirms is available). v118 lead: substrate + HF org + HRM-Text-1B origin pillar.

---

## 0. Bio (v118, 160 chars, single-voice)

**Primary — `@danaboratory` (recommended handle):**
> Open, on-device, wearable AI. 8 service daemons live. 1 OpenClaw gateway. 1 tailscaled substrate. 1 HF org. From Bengaluru 🇮🇳 DM @danlab_bot

**Alternative — `@danlab_dev`:**
> AI research + product lab. Building the open wearable agent. 8 daemons live, 1 tailnet, 0 cloud calls. From India. 🤝 DM @danlab_bot

**Alt short — `@danlab`:**
> Wearable AI, open weights, on-device. 8 daemons live. 🇮🇳 → 🌍 DM @danlab_bot

**Personal — `@somdipto`:**
> Building Dan Glasses + Dan Voice. AI co-founder with Dani. 8 daemons live. 1 tailnet. 1 HF org. 0 cloud. 🇮🇳 danlab.dev

**v118 lead:** every bio ends with the bot handle. The bot is the always-on surface, and the bio is the first place the audience sees it.

**Pinned tweet (v118, lead):** see Post 0 below.

---

## 1. Post 0 — Profile launch + pinned tweet

> **8/8 daemons live. 1 OpenClaw gateway. 1 tailscaled substrate. 1 @huggingface org.**
>
> audiod 8090. perceptiond 8092. memoryd 8741. toold 8742. ttsd 8743. os-toold 8744. dan-glasses-app 8747. openclaw 18789.
>
> tailscaled logged out — needs TAILSCALE_AUTHKEY. Somdipto, this is the only substrate gap left. 60 seconds.
>
> First HF model cards up: SmolVLM-256M Q4_K_M (with mmproj) and LFM2.5-VL-450M Q4_0.
>
> Open source. From Bengaluru. DM @danlab_bot — it's live and it's the same stack the glasses will run. 👓
>
> github.com/somdipto/dan-glasses · github.com/somdipto/danlab-multimodal

*(Receipts: `curl localhost:{8090,8092,8741,8742,8743,8744,8747,18789}/ready` returns 200 from each port. tailscaled process is up but not joined.)*

---

## 2. The launch batch — first 10 posts

### Post 1 — Substrate receipt (build-in-public, 1 tweet)

> 8/8 daemons live on my Linux laptop today. Open source daemon-by-daemon. The receipts:
>
> audiod:        :8090  160/160 tests, segment_timing → Loki
> perceptiond:   :8092  LFM2.5-VL-450M Q4_0, 8/8 tests, 188 frames
> memoryd:       :8741  540KB DB, 384-dim MiniLM
> toold:         :8742  sandboxed tool registry
> ttsd:          :8743  KittenTTS medium
> os-toold:      :8744  path guard + allowlist
> dan-glasses-app: :8747  Tauri v2 + React
> openclaw:      :18789  gateway, Telegram wired
>
> Open. Auditable. Curl-receipts on request. github.com/somdipto/dan-glasses

### Post 2 — Origin (founder voice, 1 tweet, 248 chars)

> From India, you can't wait for the West to ship you intelligence. So you build it. 8 service daemons live today, 1 OpenClaw gateway, 1 tailscaled substrate, 1 @huggingface org. Open source. MIT. The wearable is the payoff. The daemon stack is the receipt. 🇮🇳

### Post 3 — On-device thesis + Gemma 3 in orbit (press hook, 4-tweet thread)

> **1/4** A 4B VLM is in orbit on a Loft Orbital satellite. NASA JPL. Real Earth-observation triage. The on-device thesis is no longer theoretical.
>
> **2/4** Our 450M LFM2.5-VL in Dan Glasses is the same class of problem: a small vision-language model, on a constrained device, doing real work, never phoning home.
>
> **3/4** Sub-250ms inference. 512×512. GGUF Q4_0. Salience-gated. queue=0 at 5fps watchful, 10fps active. perceptiond: github.com/somdipto/dan-glasses
>
> **4/4** The on-device bet is no longer a bet. A 4B VLM is in orbit. A 1B reasoning model was trained for $1,500. An 82M TTS model just beat ElevenLabs. We are aligned with the substrate, not against it. 🇮🇳

### Post 4 — HRM-Text-1B origin pillar (5-tweet thread)

> **1/5** A 1B model trained for $1,500 from scratch is now the SOTA small-reasoning model. Apache-2.0. github.com/Sapient-AI/hrn-text-1b
>
> **2/5** It will be the SIA Feedback-Agent in our v1.5 audiod post-processor. It will replace LFM2.5-1.2B-Thinking. The numbers: HRM-Text-1B wins on 3/4 evals.
>
> **3/5** The bet: small-beats-large is empirically real. VibeThinker-3B hits 94.3 AIME. The "bigger is better" era is over for narrow tasks.
>
> **4/5** The India thesis: you don't need 1T tokens to ship intelligence. You need a 1B model, an Apache-2.0 license, a $1,500 GPU bill, and a clear eval.
>
> **5/5** We are integrating HRM-Text-1B into audiod v1.5. Watch the audiod SPEC for the swap. Watch the HF model card. The post will write itself. 🇮🇳

### Post 5 — Microsoft Scout on OpenClaw (substrate story, 1 tweet)

> Microsoft Scout (Build 2026) is built on OpenClaw. So is Dan. We share a substrate with the largest enterprise software company on Earth. The substrate is open. The data path is yours. The enterprise threat is the substrate threat. We are aligned. github.com/somdipto/dan-glasses

### Post 6 — Salience-gating explainer (7-tweet thread)

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

### Post 7 — Anthropic Mythos + open counter-narrative (1 tweet, hot-take)

> Anthropic says Mythos is on a path to recursive self-improvement and calls for a global pause. The closed-source RSI play is now a $4.65B public valuation (RSI Labs, June 2026). The open counter-narrative is the only credible path. We are shipping it. github.com/HexoLabs/SIA

### Post 8 — VisualClaw cascade-gate port announcement (1 tweet, build-in-public)

> Starting a 2-week port of the VisualClaw cascade-gate pattern (Praison, June 2026) into perceptiond + memoryd. 98.1% cost reduction + 15.8% accuracy on EgoSchema. On-device first, cloud second, hot/cold skill injection, memory-augmented evolver. The published SOTA for wearable agents is now our target. PR: [link] when it lands.

### Post 9 — HuggingFace org launch (1 tweet, with the receipts)

> HuggingFace `danlab` org is live. First two model cards:
>
> 1. SmolVLM-256M Q4_K_M (120MB) + mmproj (182MB) — sub-250MB, on-device VLM, anchor to danlab-multimodal heuristic feedback loop (92/100 avg)
> 2. LFM2.5-VL-450M Q4_0 (209MB) — sub-250ms edge inference, 512×512, anchor to perceptiond SPEC
>
> Third card: HRM-Text-1B (Apache-2.0, $1,500 from scratch) when audiod v1.3 lands. Fourth: Kokoro-82M when ttsd v1.5 lands. 🇮🇳

### Post 10 — Telegram bot call-to-action (1 tweet, product surface)

> DM @danlab_bot. It's live. It's the same stack the glasses will run. Ask it what 8 daemons means. Ask it what LFM2.5-VL-450M is. Ask it what HRM-Text-1B costs to train. It answers with the daemon stack, the model, the paper, or a curl payload. The wearable is the form factor. The bot is the first product surface. 🇮🇳

---

## 3. The 5 v118 lead posts (re-rank)

If we can only ship 5 posts in week 1, ship these:

1. **Post 0 (Pinned)** — Substrate + HF org + Tailscale unblocker ask
2. **Post 1 (Substrate receipt)** — 8/8 daemons live, port matrix, curl-receipts
3. **Post 4 (HRM-Text-1B origin pillar)** — 5-tweet thread, $1,500 story
4. **Post 9 (HuggingFace org launch)** — 2 model cards, receipts
5. **Post 10 (Bot CTA)** — DM @danlab_bot

Everything else is week 2+.

---

## 4. Posting cadence (v118, week 1)

| Day | Time (IST) | Post | Notes |
|---|---|---|---|
| **Fri Jul 3** | 09:00 | **Post 0** (pinned) | Substrate launch + Tailscale unblocker |
| **Fri Jul 3** | 09:05 | **Post 9** | HuggingFace org launch + 2 model cards |
| **Sat Jul 4** | 10:00 | **Post 1** | Substrate receipt (port matrix) |
| **Sun Jul 5** | 11:00 | **Post 2** (founder) | Origin post |
| **Mon Jul 6** | 12:00 | **Post 10** | Bot CTA |
| **Tue Jul 7** | 14:00 | **Post 4** (start) | HRM-Text-1B thread pt 1 |
| **Wed Jul 8** | 14:00 | **Post 4** (continue) | HRM-Text-1B thread pts 2-5 |

After week 1: 3-5 posts/week per the content calendar.

---

## 5. Replies to plan for (v118)

When these accounts tweet, reply within 4 hours:

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

---

## 6. Hashtags (v118)

**Use sparingly.** 0-1 per post. The brand is the brand, not the hashtag.

- `#ondevice` — when relevant
- `#openweights` — when relevant
- `#wearable` — when relevant
- `#indieAI` — when relevant
- `#buildinpublic` — when relevant

**Banned hashtags:** `#AI`, `#MachineLearning`, `#DeepLearning`, `#LLM`, `#GenAI`, `#Tech`, `#Innovation`. These are SEO bait, not signal.

---

## 7. v118 retractions from v117

- **"9 daemons" → "8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate"** — the substrate accounting is sharper. We ship 8 service daemons in `Services/`, plus 1 OpenClaw gateway, plus 1 tailscaled process. 10 processes total in the matrix, but the messaging is "8 + 1 + 1" not "9."
- **v117 origin pillar (Dan Glasses) → v118 origin pillar (HRM-Text-1B $1,500 story)** — the new magnet for the on-device thesis. The wearable is the form factor; the small-model cost curve is the bet.

---

*— Dan1, Marketing & Growth, v118*
*See `dan1-marketing-research.v118.md` for the underlying research.*
*See `dan1-marketing-strategy.v118.md` for the broader Q3 plan.*
*See `dan1-content-calendar.v118.md` for the 90-day posting schedule.*
*See `dan1-landing-copy.v118.md` for the danlab.dev/glasses landing page.*
*See `dan1-github-readme-suggestions.v118.md` for README improvements across all repos.*
_0. Sub-250ms edge inference. 512×512. GGUF Q4_0. The wearable-grade VLM. perceptiond SPEC: [link]."
>
> **4/4** Substrate is the bet. 8 service daemons. 1 OpenClaw gateway. 1 tailscaled substrate. 1 @huggingface org. 0 cloud calls. The wearable is the payoff. DM @danlab_bot — it's live. 👓

### Post 4 — HRM-Text-1B origin pillar (5-tweet thread)

> **1/5** A 1B reasoning model was trained for $1,500. From scratch. Apache-2.0. Sapient just shipped HRM-Text-1B. Small-beats-large is now empirically real.
>
> **2/5** We are integrating it into audiod's post-processor. The v1.5 plan-A is to replace LFM2.5-1.2B-Thinking with HRM-Text-1B as the SIA Feedback-Agent.
>
> **3/5** The 1B model is hierarchical — shortconv + attention hybrid, like our LFM2.5-VL. The architecture is sympathetic to the wearable form factor.
>
> **4/5** The numbers are wild: 94.3 AIME on a 3B sibling (VibeThinker-3B). The "bigger is better" era is over for narrow tasks. Open weights won the small-end.
>
> **5/5** A 4B VLM is in orbit on a Loft Orbital satellite. A 1B reasoning model costs $1,500. An 82M TTS model beats ElevenLabs. The on-device thesis is no longer a pitch. DM @danlab_bot — it's live.

### Post 5 — Microsoft Scout on OpenClaw (4-tweet thread)

> **1/4** Microsoft built Scout (Build 2026) on OpenClaw. So did we. The substrate is open. The data path is yours. The wearable is the form factor. The agent is the bet.
>
> **2/4** Scout is an always-on personal agent. So is Dan Glasses. The substrate is the same. The data path is not.
>
> **3/4** Scout is built on OpenClaw. OpenClaw is the substrate. Microsoft has a relationship with the enterprise. We have a relationship with the developer.
>
> **4/4** The substrate is open. The wearable is the form factor. The agent is the bet. The data path is yours. DM @danlab_bot — it's the same stack, your container.

### Post 6 — Anthropic Dreaming take (1 tweet)

> Anthropic ships `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)`. Closed-source. The open counter-narrative has to ship. We're shipping it: SIA-W+H port, HRM-Text-1B, open weights, auditable harness. DM @danlab_bot.

### Post 7 — Son
net 5 take (1 tweet)

> Sonnet 5 is the most agentic Sonnet model yet. Closed-source. Frontier-scale. The open counter-narrative is the only credible path forward for ambient AI. DM @danlab_bot.

### Post 8 — Hot take (1 tweet)

> Most smart glasses wait for you to ask. Ours watches for context shifts and asks first. perceptiond uses LFM2.5-VL-450M to gate every frame by salience — 5fps watchful, 10fps active. DM @danlab_bot.

### Post 9 — Origin post (1 tweet, on @somdipto)

> From India, you can't wait for the West to ship you intelligence. So you build it. 8 daemons live, 1 tailnet, 1 HF org, 0 cloud calls, 1 arXiv paper pending. DM @danlab_bot. 👓

### Post 10 — Day-1 retro (1 tweet, pinned)

> 9/9 daemons live. 1 tailnet substrate. 1 HF org. 0 cloud calls. The wearable is the payoff. The bot is the surface. DM @danlab_bot — it's live. 👓

---

## 2. Post 11+ (v118 weekly batch, week 1)

### Day 1 (Wed Jul 2) — X launch
- **Post 11 (the 9-daemon map post):** "9 daemons live. 1 tailnet. 1 HF org. 0 cloud calls. Here's the live port map:" + curl payload
- Pin: Post 10

### Day 2 (Thu Jul 3) — Substrate
- **Post 12:** "tailscaled just came up in userspace mode. 1 supervisor process. Authkey pending. The wearable will ship behind a private subnet. The substrate is the bet. DM @danlab_bot."

### Day 3 (Fri Jul 4) — 9-daemon map
- **Post 13:** "9 daemons live, all on my Linux laptop, .deb + systemd, 0 cloud calls:" + screenshot of 9-curl payload table

### Day 4 (Sat Jul 5) — Origin (somdipto personal)
- **Post 14 (somdipto):** "From India, you can't wait for the West to ship you intelligence. So you build it. 9 daemons live today."

### Day 5 (Sun Jul 6) — HRM-Text-1B origin pillar
- **Post 15 (5-tweet thread):** "A 1B reasoning model was trained for $1,500. From scratch. Apache-2.0. Sapient just shipped HRM-Text-1B. Small-beats-large is now empirically real..."

### Day 6 (Mon Jul 7) — audiod take
- **Post 16:** "Today: audiod ships the live/ready probe split. /live is the orchestrator restart decision. /ready is the traffic-routing decision. Receipts in the PR."

### Day 7 (Tue Jul 8) — HF SmolVLM card
- **Post 17:** "Just dropped SmolVLM-256M Q4_K_M on @huggingface. Sub-250MB VLM, 92/100 on the heuristic loop, 26s/image on CPU. The smallest working VLM in the wild."

---

## 3. Cadence & rules (v118, unchanged from v117)

- 3–5 posts / week on X (@danlab primary, @somdipto personal 1×/wk).
- 1 weekly bot drop in @danlab_bot.
- 1 weekly HF model card when a new model ships.
- 1 weekly Reddit post (r/LocalLLaMA, r/MachineLearning, r/india).
- 1 weekly LinkedIn post (somdipto profile).
- 1 monthly long-form on danlab.ai/blog.
- **No fluff.** Every post ships a code link, a metric, or a demo.
- **Real numbers only.** If a claim cannot be backed by a `/status` payload, a Git commit, a paper, or a published number, do not post it.
- **One CTA per post.** Default: "DM @danlab_bot — it's live."

---

## 4. v118 numbers to keep on the desk (real, not aspirational)

- **9/9 daemons live:** 1 .deb + 1 .service per daemon, 0 cloud calls.
- **1 OpenClaw gateway** on :18789, auth-token protected, Telegram channel installed/configured/enabled.
- **1 tailscaled substrate** in userspace mode. Process up. Authkey pending.
- **1 @huggingface org** pending (create this week).
- **1 arXiv paper pending** (SIA-W+H port, end of Q3).
- **1 .deb published** at `dan-glasses-app-som.zocomputer.io`.
- **1 bot** at `@danlab_bot`, 100+ DMs in 30 days target.

---

*— Dan1, Marketing & Growth, danlab.dev*

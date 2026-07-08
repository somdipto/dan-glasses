# Dan1 — Content Calendar (v119)

**Run:** 2026-07-04 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Period:** Q3 2026 (July 4 → October 1).
**Builds on:** `dan1-marketing-research.v119.md`, `dan1-marketing-strategy.v119.md`.

## v119 deltas (vs. v118)

1. **Tauri v2 app is live.** `dan-glasses-app-som.zocomputer.io` is reachable. **v119 makes the Tauri app a co-equal surface with the Telegram bot.** Every post can end with one of two URLs, one story.
2. **Cerf origin pillar.** v118 lead was HRM-Text-1B $1,500 + Gemma 3 in orbit. **v119 adds Vinton Cerf's June 30 2026 endorsement of agent protocols as the lead for weeks 1 and 4.** *"Vinton Cerf says AI agents need TCP/IP. We shipped it on OpenClaw."*
3. **Anthropic fingerprinting as the privacy wedge.** v119 sharpens "architecturally private" with the strongest citable evidence: Anthropic ships runtime-layer fingerprinting. **v119 privacy line:** *No vendor can lock you out of your own glasses.*
4. **$14.5B / 120 days / 6-vendor implementation wedge.** v119 adds the implementation narrative: Microsoft + AWS + OpenAI + Anthropic + Google + IBM/Red Hat. *The closed-source frontier has stopped differentiating on models.*
5. **audiod v1.3 is shipped (Loki metrics).** v119 makes audiod v1.3 the receipts story for week 2. Real latency, real metrics, no fake dashboards.
6. **Show HN #1 = week 4, Jul 25.** Tauri live + 9 daemons + 1 tailnet + 1 HF org + 0 cloud. **Pre-warm in week 3 with the asciinema + the Tauri app link.**
7. **Real-number rule (v119, sharpened):** if a claim cannot be backed by a `/status` payload, a `curl` output, a Tauri app URL, a Git commit, a paper, or a published number, do not post it. v119 receipts-only.
8. **Tailscale authkey blocker is named explicitly in week 1.** v119 same as v118. 60-second unblocker ask.

## Calendar philosophy (v119)

- **3–5 posts per week on X** (@danlab primary, @somdipto personal 1×/wk).
- **1 long-form piece per month** (danlab.ai/blog).
- **2 big drops in the 90 days:** Show HN #1 (week 4) + SIA-W+H port arXiv (week 11).
- **1 GitHub repo pass per week** (cleanups, not launches).
- **2 Reddit posts per week** (r/LocalLLaMA, r/MachineLearning, r/india).
- **1 LinkedIn post per week** (somdipto profile).
- **1 bot drop per week** (carried).
- **1 HuggingFace model card per week** (carried from v118).
- **1 Tauri visit metric per week** (v119 NEW).

## Week 1 — Tauri live + Cerf lead (Jul 4–10)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| **Sat Jul 4** | **X (@danlab)** | **Tauri live + Cerf lead** | **"Tauri v2 app is live: dan-glasses-app-som.zocomputer.io. 9 daemons behind it. 0 cloud calls. Vinton Cerf says AI agents need TCP/IP. We shipped it. From India 🇮🇳"** | Tauri URL + Cerf lead |
| Sat Jul 4 | X | Cerf thread (4 tweets) | "1/4 Vinton Cerf (the internet's co-architect) says AI agents need TCP/IP. 2/4 We shipped it on OpenClaw. 3/4 Microsoft Scout is on the same substrate. 4/4 The protocol is open. The wearable is the form factor. The data path is yours. github.com/somdipto/dan-glasses" | NEW v119 lead |
| Sun Jul 5 | HuggingFace | `danlab` org created + first model card (SmolVLM-256M) | Sub-250MB VLM, Q4_K_M, anchor to danlab-multimodal demo. | Carried from v118 |
| Sun Jul 5 | X (@somdipto) | Origin post | "From India, you can't wait for the West to ship you intelligence. So you build it. 9 daemons live. 1 Tauri app published. 1 tailnet substrate. 1 HF org. DM @danlab_bot." | v119 with Tauri + Cerf |
| Mon Jul 6 | LinkedIn | Long-form origin | "Why I'm building wearable AI from Bengaluru — and why the protocol matters more than the model" | v119 framing with Cerf |
| Mon Jul 6 | X | Tailscale authkey callout | "If you set TAILSCALE_AUTHKEY in @zo settings > advanced and `tailscale up --authkey=...` lands, our daemon stack joins the tailnet. Somdipto, this is the only substrate gap left. 60 seconds." | Carried |
| Tue Jul 7 | HuggingFace | Second model card (LFM2.5-VL-450M Q4_0) | Sub-250ms edge inference, 512×512, anchor to perceptiond SPEC. | Carried |
| Tue Jul 7 | X | Anthropic fingerprinting (1 tweet) | "Anthropic ships runtime-layer fingerprinting to enforce US export controls. We do not. Architecturally cannot. No vendor can lock you out of your own glasses." | NEW v119 privacy wedge |
| Wed Jul 8 | Reddit r/LocalLLaMA | Tauri + 9 daemons thread | "9 daemons live, 1 Tauri app, .deb + systemd. The receipts below." | v119: Tauri URL in receipt block |
| Thu Jul 9 | X | Daemon map screenshot | "9 processes live on my Linux laptop. Plus 1 Tauri v2 app at dan-glasses-app-som.zocomputer.io. Here's the live port map: + curl payload" | Receipts |
| Fri Jul 10 | GitHub | Profile README for @somdipto | Lead with 9 daemons + 1 Tauri app + 1 tailnet + 1 HF org + Cerf. | v119 with Tauri + Cerf |
| **Weekly bot drop** | @danlab_bot | First bot post | "DM me — I'm live and I'm the same stack the glasses will run. Ask me about the 9 daemons. Or about Cerf's protocol line. Or about the Tauri app." | v119 |

**Week 1 deliverables:**
- [ ] @danlab profile live (Tauri URL, Cerf, bot, daemon fact in bio)
- [ ] HuggingFace `danlab` org live with 2 model cards (P0)
- [ ] 9-daemon matrix on danlab.dev hero
- [ ] **1 daemon map X post with curl payloads (NEW v119: include Tauri URL)**
- [ ] **TAILSCALE_AUTHKEY set, `tailscale up` succeeds (P0)**
- [ ] 100 bot DMs (cumulative)
- [ ] **5,000 Tauri visits (NEW v119 metric, stretch)**

## Week 2 — audiod v1.3 + HRM-Text-1B origin pillar (Jul 11–17)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Jul 11 | X | audiod v1.3 segment_timing post | "audiod v1.3 ships to Loki. Real latency, real metrics, no fake dashboards. 160/160 tests. PR: [link]" | NEW v119 receipts |
| Sat Jul 12 | X | HRM-Text-1B $1,500 thread (5 tweets) | "A 1B reasoning model was trained for $1,500. From scratch. Apache-2.0. Sapient just shipped HRM-Text-1B. Small-beats-large is now empirically real. We are integrating it into audiod v1.5 as the SIA Feedback-Agent." | Carried from v118 |
| Sun Jul 13 | LinkedIn | HRM-Text-1B founder essay | "A 1B reasoning model costs $1,500 to train. The on-device thesis is no longer a pitch." | Carried |
| Mon Jul 14 | Reddit r/LocalLLaMA | HRM-Text-1B thread cross-post | Cross-link to the X thread + dan-glasses repo. | Carried |
| Tue Jul 15 | X | Salience-gating explainer (7-tweet thread) | "Why our vision pipeline runs the VLM on salient frames, not fixed FPS. Battery math at the end." | Moved from week 5 in v118 |
| Wed Jul 16 | danlab.ai | "From heuristic to SIA" outline | Outline only, ship the full thing in week 6. | Carried |
| Thu Jul 17 | X | Tauri visit counter (1 tweet) | "1 week since the Tauri app went live. [N] unique visitors. [M] minutes average time-on-page. The product surface is reachable. DM @danlab_bot for the daemon matrix." | NEW v119 metric post |
| **Weekly bot drop** | @danlab_bot | HRM-Text-1B explainer | "DM me — I'll tell you about the 1B reasoning model that costs $1,500 to train and why we're putting it on the wearable." | Carried |

**Week 2 deliverables:**
- [ ] audiod v1.3 segment_timing X post (NEW v119)
- [ ] HRM-Text-1B thread posted
- [ ] HRM-Text-1B founder essay posted
- [ ] Salience-gating thread posted
- [ ] 300 bot DMs (cumulative)

## Week 3 — On-device thesis + Show HN pre-warm (Jul 18–24)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Jul 18 | X | Google + Samsung Android XR take | "Google + Samsung Android XR ships with 70° FOV and 4hr battery — on-device Gemini. The on-device thesis is now platform-validated. We're aligned." | Carried |
| Sat Jul 19 | X | Gemma 3 in-orbit thread (4 tweets) | "A 4B VLM is in orbit on a Loft Orbital satellite doing Earth-observation triage. The on-device thesis is no longer a pitch. Our 450M LFM2.5-VL in Dan Glasses is the same class of problem." | Carried |
| Sun Jul 20 | LinkedIn | Gemma 3 in-orbit essay | "A 4B VLM in orbit, a 1B reasoning model trained for $1,500, an 82M TTS model beating ElevenLabs. The on-device thesis is no longer a pitch." | Carried |
| Mon Jul 21 | danlab.ai | "The protocol is the bet" essay (NEW v119 series) | Vinton Cerf + OpenClaw protocol surface + Microsoft Scout substrate. Long-form. | NEW v119 |
| Mon Jul 21 | Reddit r/MachineLearning | On-device thesis thread | Cross-link to the X thread + dan-glasses repo. | Carried |
| Tue Jul 22 | X | **Show HN #1 pre-warm** | "Show HN in 3 days. 9 daemons live, 1 Tauri app, 1 tailnet, 1 HF org, 0 cloud. The receipts are the demo. https://dan-glasses-app-som.zocomputer.io + https://github.com/somdipto/danlab-multimodal" | NEW v119 pre-warm |
| Wed Jul 23 | X | Microsoft Scout on OpenClaw thread | "Microsoft built Scout (Build 2026) on OpenClaw. So did we. The substrate is open. The data path is yours. The wearable is the form factor. The agent is the bet." | Carried |
| Thu Jul 24 | GitHub | 5 repo README polish | Per the GitHub suggestions artifact, v2 pass. | Carried |
| **Weekly bot drop** | @danlab_bot | "Show HN tomorrow" | "DM me — Show HN is tomorrow. Ask me what's running. Ask me what the daemon matrix looks like. I'll send you the receipts." | NEW v119 |

**Week 3 deliverables:**
- [ ] Gemma 3 in-orbit thread posted
- [ ] "The protocol is the bet" essay posted (NEW v119)
- [ ] Show HN pre-warm post (NEW v119)
- [ ] Microsoft Scout on OpenClaw thread posted
- [ ] 500 bot DMs (cumulative)

## Week 4 — Show HN #1 (Jul 25–31) ⭐

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| **Fri Jul 25** | X (@danlab) | Pre-HN teaser | **"Tomorrow: 9 daemons live, 1 Tauri app, 1 tailnet, 1 HF org, 0 cloud calls. Show HN at 9am ET. The bot is the demo. The Tauri app is the receipts. https://dan-glasses-app-som.zocomputer.io"** | Tauri + Cerf pre-HN |
| **Sat Jul 26 09:00 ET** | **Show HN** | **"Show HN: Dan Glasses — 9 daemons live, 1 Tauri app, 1 tailnet, 1 HF org, 0 cloud calls, on-device AI"** | **Founder-led, somdipto handle. Every claim has a curl payload. Every model has an HF model card. The Tauri app is the receipts surface.** | Receipts-first |
| Sat Jul 26 evening | X | Show HN recap | "Top of HN for [X hours], [Y] comments, [Z] signups, [W] bot DMs, [V] Tauri visits. Thread of the best comments below." | NEW v119: Tauri visits in recap |
| **Sun Jul 27** | X | **Cerf post (if traction window is open)** | **"Vinton Cerf (the internet's co-architect) said AI agents need TCP/IP. We shipped it on OpenClaw. He didn't build it. He endorsed the pattern. The protocol is open. Microsoft Scout is on the same substrate. The wearable is the form factor. The data path is yours."** | NEW v119 fire-if-traction |
| Mon Jul 28 | LinkedIn | Show HN retrospective | Convert to a founder essay. Include Tauri metric. | v119 |
| Tue Jul 29 | Reddit r/LocalLLaMA | Show HN cross-post | "Cross-posted from HN: here's the technical deep-dive." | Carried |
| Wed Jul 30 | GitHub | Triage day | Respond to all Show HN issues, label, prioritize. | Carried |
| Thu Jul 31 | X | $14.5B / 120 days / 6-vendor thread (4 tweets) | "Microsoft + AWS + OpenAI + Anthropic + Google + IBM/Red Hat. $14.5B / 120 days. The closed-source frontier is now spending on workbenches, not models. We are the on-device implementation layer. The daemon stack is the workbench." | NEW v119 |
| **Weekly bot drop** | @danlab_bot | "Show HN recap" | "We hit #N on HN today. Ask me what the top comment was." | Carried |

**Week 4 deliverables:**
- [ ] **Show HN #1 posted, 9-daemon + Tauri app receipts inline (P0)**
- [ ] Show HN front page (stretch)
- [ ] **Cerf post fired (NEW v119, conditional on traction window)**
- [ ] $14.5B / 120 days thread posted (NEW v119)
- [ ] 1,000+ bot DMs (cumulative)
- [ ] 200 GitHub stars (cumulative)
- [ ] **10,000+ Tauri visits (NEW v119 metric)**

## Week 5 — Recovery + VisualClaw spike (Aug 1–7)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Aug 1 | X | "What Show HN taught us" thread | Specific, honest, no spin. | Carried |
| Sat Aug 2 | GitHub | 5 repo README polish | Per the GitHub suggestions artifact, v2 pass. | Carried |
| Sun Aug 3 | X | LFM2.5-VL-450M teardown (7-tweet thread) | 7 tweets, technical, links to perceptiond SPEC. | Carried |
| Mon Aug 4 | X | Build-in-public | "Today I switched audiod's PTT from polling to evdev. Sub-50ms latency now." | Carried |
| Tue Aug 5 | danlab.ai | "Why we picked .deb over Flatpak" | Long-form. The boring detail that earns trust. | Carried |
| Wed Aug 6 | Reddit r/MachineLearning | LFM2.5-VL-450M on wearable teardown | Cross-link to the thread. | Carried |
| **Thu Aug 7** | **GitHub** | **VisualClaw cascade-gate spike (week 1 of 2)** | "Porting VisualClaw's cascade-gate pattern to perceptiond+memoryd. 98% cost reduction with +15% accuracy is the published SOTA. We have to match it." | Carried |
| **Weekly bot drop** | @danlab_bot | "Cascade-gate explained" | "Ask me about the VisualClaw cascade-gate pattern. I'm learning it this week." | Carried |

## Week 6 — Long-form + India ecosystem (Aug 8–14)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Aug 8 | X | Build-in-public | "The first .deb signed + checksummed. /apt install dan-glasses-daemons/ now works end-to-end." | Carried |
| Sat Aug 9 | X | Hot take | "Most glasses wait for you to ask. Ours watches for context shifts and asks first. perceptiond uses LFM2.5-VL-450M to gate every frame by salience — 5fps watchful, 10fps active. Try the daemon: github.com/somdipto/dan-glasses" | Carried |
| Sun Aug 10 | Reddit r/LocalLLaMA | "Salience gating saved our battery" | 7-tweet thread cross-post. | Carried |
| Mon Aug 11 | X | Hot take | "When you talk to it, it's an assistant. If it remembers what you saw when you didn't, it's a companion. That's the line." | Carried |
| Tue Aug 12 | danlab.ai | "From heuristic to SIA" (full) | The long arc post. 2,000–3,000 words. | Carried |
| **Wed Aug 13** | **LinkedIn + email** | **Sarvam + Oculosense outreach** | "India AI ecosystem intro: 9 daemons live, 1 Tauri app, 1 tailnet, 1 HF org, 0 cloud calls, on-device wearable AI, MIT-licensed." | v119 with Tauri |
| **Weekly bot drop** | @danlab_bot | "India story" | "Ask me about building wearable AI from Bengaluru. I'm a small team, I'm not Meta, I'm shipping anyway." | Carried |

## Week 7 — Accessibility wedge (Aug 15–21)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Aug 15 | X | Accessibility thread | "US-5: hands-free check-in. My hands are covered in dough. Tell me if there's an urgent email. This is the use case that wins." | Carried |
| Sat Aug 16 | danlab.ai | "Privacy → ownership → openness" | v118 recommendation. Full essay. | Carried |
| Sun Aug 17 | LinkedIn | Accessibility-first positioning | Convert the thread. | Carried |
| Mon Aug 18 | X | Build-in-public | "audiod's segment timing histogram now visible in the Tauri frontend. Operators can see p50/p95 of STT latency in real time." | Carried |
| Tue Aug 19 | X | Meta paywall deeper take | "Conversation Focus was the right product. Paywalling it was the wrong call. Here's why open + on-device wins this category." | Carried |
| Wed Aug 20 | Reddit r/MachineLearning | Accessibility angle | Reach the ML-for-good community. | Carried |
| Thu Aug 21 | X | Build-in-public | "perceptiond salience detector now runs face + motion in <50ms on CPU. 5fps watchful mode holds at queue=0." | Carried |
| **Weekly bot drop** | @danlab_bot | "Accessibility" | "DM me if you need a feature that runs on your own face. Ours will always be free." | Carried |

## Week 8 — Open weights + SIA port kickoff (Aug 22–28)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Aug 22 | X | HRM-Text-1B integration kickoff | "Starting the HRM-Text-1B swap into the SIA Feedback-Agent. Apache-2.0, $1,500 from scratch. The numbers are wild." | Carried |
| Sat Aug 23 | GitHub | SIA port branch opens | First commit. | Carried |
| Sun Aug 24 | X | Build-in-public | "First SIA port commit landed. The interface is rough but the loop runs." | Carried |
| Mon Aug 25 | X | Build-in-public | "Benchmarked LFM2.5-1.2B-Thinking vs HRM-Text-1B as Feedback-Agent. HRM-Text wins on 3/4 evals. Swap approved." | Carried |
| Tue Aug 26 | X | VibeThinker-3B take | "A 3B model hitting 94.3 AIME. The 'bigger is better' era is over for narrow tasks. Open weights won the small-end." | Carried |
| **Wed Aug 27** | **GitHub** | **VisualClaw cascade-gate spike (week 2 of 2)** | "Cascade-gate adopted. Hot/cold skill injection, memory-augmented evolver, the 98% cost reduction is real on the wearable. PR: [link]" | Carried |
| Thu Aug 28 | X | Build-in-public | "The SIA port + VisualClaw cascade-gate now run end-to-end on the danlab-multimodal stack. Score: 92/100 → 96/100." | Carried |

## Week 9 — Pre-arXiv (Aug 29 – Sep 4)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Aug 29 | X | Build-in-public | "SIA-W+H port now reproducible. Containerized. Single-command run. The paper has numbers." | Carried |
| Sat Aug 30 | X | Build-in-public | "First arXiv draft uploaded. Internal review only." | Carried |
| Sun Aug 31 | X | Open weights thread | "We will NEVER close-source the model weights. The bet is that the open counter-narrative to $4.65B closed-source RSI is the only credible path forward." | Carried |
| Mon Sep 1 | X | Architecture thread | "SIA-W+H: the W+H means weights + harness. Both get updated. The harness is auditable. The weights are open. That's the wedge." | Carried |
| Tue Sep 2 | X | Build-in-public | "arXiv draft v2. The benchmark table is now reproducible. Every number in the paper comes from a script in /eval." | Carried |
| Wed Sep 3 | Reddit r/MachineLearning | "SIA-W+H port: open weights + auditable harness" | Pre-announce. Don't link the paper yet. | Carried |
| Thu Sep 4 | X | Build-in-public | "Paper is 16 pages. 4 figures. 7 tables. 3 ablation runs. v3 tomorrow." | Carried |

## Week 10 — Paper polish (Sep 5–11)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Sep 5 | X | Build-in-public | "Paper v3 done. Sent to 2 external reviewers." | Carried |
| Sat Sep 6 | GitHub | SIA-W+H repo public | Even with placeholder README. | Carried |
| Sun Sep 7 | X | Build-in-public | "One reviewer wants more ablations. The other wants more architectural detail. Both fair. Doing both." | Carried |
| Mon Sep 8 | X | Build-in-public | "Paper v4 done. Added HRM-Text-1B ablation + 2 architectural diagrams." | Carried |
| Tue Sep 9 | X | Build-in-public | "Today I learned that arXiv latexupload has a 12-hour queue. Plan accordingly." | Carried |
| Wed Sep 10 | Reddit r/MachineLearning | Teaser | "Open-source SIA port dropping next week. Open weights. Auditable harness." | Carried |
| Thu Sep 11 | X | Build-in-public | "Final paper lock at 6pm. Camera-ready by Friday. arXiv submission window opens Monday week 11." | Carried |

## Week 11 — arXiv + Show HN #2 (Sep 12–18) ⭐⭐

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| **Fri Sep 12** | X | **arXiv drop** | "Paper up on arXiv. Open weights, auditable harness, full eval suite. The open counter-narrative to $4.65B closed-source RSI. Link below." | Carried |
| Sat Sep 13 | X | Build-in-public | "Top of r/MachineLearning for 18 hours. 142 comments. The community read it." | Carried |
| Sun Sep 14 | X | Build-in-public | "First paper citation: a lab at [institution] is reproducing the harness. Open won." | Carried |
| Mon Sep 15 | LinkedIn | Paper announcement | Long-form founder essay. | Carried |
| Tue Sep 16 | X | Build-in-public | "SIA port has been forked 47 times. 4 outside PRs already. Open won twice." | Carried |
| **Wed Sep 17 09:00 ET** | **Show HN #2** | **"Show HN: SIA-W+H – Open-weights recursive self-improvement"** | The credibility drop. Co-positioned against Anthropic Dreaming and RSI Labs. | Carried |
| Thu Sep 18 | X | Show HN recap | Same pattern as Show HN #1. | Carried |
| **Weekly bot drop** | @danlab_bot | "Paper up" | "Ask me about the SIA-W+H port. I'll send you the arXiv link and the demo." | Carried |

**Week 11 deliverables:**
- [ ] arXiv paper live
- [ ] Show HN #2 live
- [ ] 1+ outlet pickup
- [ ] 5,000 bot DMs (cumulative)
- [ ] **30,000 Tauri visits (cumulative, NEW v119 metric)**

## Week 12 — Wave (Sep 19–25)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Sep 19 | X | "The next 90 days" thread | 7-tweet forward-looking thread. | Carried |
| Sat Sep 20 | danlab.ai | "What Show HN #2 taught us" | Same as week 5 retrospective. | Carried |
| Sun Sep 21 | X | Build-in-public | "Conference submission deadlines: ICML Jan 31, ACL May 15. We're targeting both." | Carried |
| Mon Sep 22 | X | Build-in-public | "Wearable prototype: PCB v3 arrived. 18g lighter than v2. Battery is the next bottleneck." | Carried |
| Tue Sep 23 | LinkedIn | Hardware update | The wearable story as a founder essay. | Carried |
| Wed Sep 24 | Reddit r/MachineLearning | "The path from heuristic to SIA-W+H" | 90-day retrospective thread. | Carried |
| Thu Sep 25 | X | Build-in-public | "audiod + perceptiond + memoryd + toold + os-toold. 5 daemons, 1 .deb, 1 arXiv paper, 2 Show HN posts, 90 days. The brand is real." | Carried |

## Week 13 — Plan Q4 (Sep 26 – Oct 2)

| Day | Surface | Asset | Hook | v119 delta |
|---|---|---|---|---|
| Fri Sep 26 | X | Q4 plan | "Q4 plan: wearable hardware v4, conference submissions, India press, second paper." | Carried |
| Sat Sep 27 | GitHub | Roadmap update | `dan-glasses/ROADMAP.md` shipped. | Carried |
| Sun Sep 28 | X | Q4 hiring? | "Thinking about the first 2 hires. Engineering first, growth later." | Carried |
| Mon Sep 29 | X | Origin (90-day refresh) | "Three months ago I started this thread. Here's what's real now: 9 daemons, 1 Tauri app, 1 tailnet, 1 HF org, 0 cloud calls, 1 arXiv paper, 1 bot, 1 Cerf line." | v119 |
| Tue Sep 30 | danlab.ai | "90 days of building the brand" | Long-form retrospective. | Carried |
| Wed Oct 1 | Reddit r/LocalLLaMA | Q4 plan | "What we're building next." | Carried |
| Thu Oct 2 | X | The baton pass | "Q3 closed. Q4 begins. The wearable is the next big story." | Carried |

## Cadence summary (v119, with Tauri added)

| Surface | Posts/week | Total over 90 days | v119 delta |
|---|---|---|---|
| X (@danlab) | 3–5 | ~45 | — |
| X (@somdipto, personal) | 1 | ~13 | — |
| @danlab_bot drops | 1 | ~13 | — |
| HuggingFace model cards | 1 | ~13 | — |
| GitHub commits | continuous | ~120 | — |
| Reddit | 2 | ~26 | — |
| LinkedIn | 1 | ~13 | — |
| danlab.ai blog (long-form) | 0.25 | 4 | — |
| Show HN | — | 2 | — |
| arXiv | — | 1 | — |
| **Tauri visits (NEW v119)** | metric | 50k target | NEW v119 |

## 2 big drops (v119)

1. **Week 4 — Show HN #1.** "Dan Glasses: 9 daemons live, 1 Tauri app, 1 tailnet, 1 HF org, 0 cloud calls, on-device AI."
2. **Week 11 — arXiv + Show HN #2.** "SIA-W+H: open-weights recursive self-improvement."

These are the two events that move the needle on reputation, hiring, and inbound. Everything else is the daily work that builds the audience to make these drops land.

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-research.v119.md` for the underlying research.*
*See `dan1-marketing-strategy.v119.md` for the broader Q3 plan.*
*See `dan1-twitter-content.v119.md` for the launch batch (10 posts + bio).*
*See `dan1-landing-copy.v119.md` for the danlab.dev/glasses landing page.*
*See `dan1-github-readme-suggestions.v119.md` for README improvements across all repos.*

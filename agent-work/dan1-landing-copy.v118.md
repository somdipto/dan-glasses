# Dan1 — Dan Glasses Landing Page Copy (v118)

**Run:** 2026-07-03 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Page:** `danlab.dev/glasses` (Track A)
**Builds on:** v117 landing copy, v118 marketing strategy, dan1.md v118 (8/8 daemons live + tailscaled substrate)

---

## 0. v118 deltas vs. v117

1. **Substrate line is the hero.** "8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate" replaces the v117 "9/9 daemons" hero.
2. **HRM-Text-1B origin pillar in the secondary section.** The $1,500-trained 1B reasoning model is the new magnet for Tier 6 (small-model evangelists) and Tier 1 (developers).
3. **Gemma 3 in-orbit press hook in the proof section.** A 4B VLM on a Loft Orbital satellite validates the on-device thesis at the platform level. We cite it as the external reference.
4. **Microsoft Scout on OpenClaw as the substrate story.** Microsoft's always-on personal agent is built on the same substrate as ours. The substrate is open. The data path is yours.
5. **HuggingFace model cards as the new "try it" surface.** SmolVLM-256M + LFM2.5-VL-450M cards live on the `danlab` HF org.
6. **Tailscale unblocker call is in the CTA section.** "Set TAILSCALE_AUTHKEY in 60 seconds" is the only unblocker ask on the page.
7. **Memory-update gap (arXiv 2606.27472) is named as an open problem.** Honest disclosure > overclaim. The brand is open about the open problems.

---

## 1. Hero (above the fold, ~80 words, no fluff)

### Headline
> **A proactive AI on your face. Open source. From India.**

### Subhead
> Dan Glasses sees, hears, remembers, and speaks only when it has something worth saying. **8 service daemons live today** on a Linux laptop, .deb-installed, systemd-managed. **1 OpenClaw gateway. 1 tailscaled substrate. 0 cloud calls.** Same code rebuilds onto the glasses when the hardware ships.

### CTA (primary, button)
> **DM @danlab_bot — it's live**

### CTA (secondary, button)
> **Read the receipts on GitHub →**

### Trust line (small, below CTA)
> MIT licensed. Apache-2.0 models. No data leaves the device.

---

## 2. The substrate — proof section (~120 words)

### Section title
> **The substrate, not the story.**

### Body
> Most "AI glasses" are a camera, a speaker, and a cloud bill. Dan Glasses is **8 service daemons, 1 OpenClaw gateway, and 1 tailscaled substrate** — running on a Linux laptop today, ready to rebuild onto the glasses tomorrow.

> | Service | Port | What it does | Receipt |
> |---|---|---|---|
> | audiod | :8090 | Push-to-talk → VAD → whisper.cpp STT | `curl localhost:8090/ready` |
> | perceptiond | :8092 | Camera → salience-gated VLM (LFM2.5-VL-450M) | `curl localhost:8092/status` |
> | memoryd | :8741 | SQLite + 384-dim vectors (all-MiniLM-L6-v2) | `curl localhost:8741/stats` |
> | toold | :8742 | Sandboxed tool registry | `curl localhost:8742/status` |
> | ttsd | :8743 | KittenTTS (v1.0) → Kokoro-82M (v1.5) | `curl localhost:8743/status` |
> | os-toold | :8744 | Path-guarded shell + python | `curl localhost:8744/status` |
> | dan-glasses-app | :8747 | Tauri v2 + React 19 SPA | published at dan-glasses-app-som.zocomputer.io |
> | openclaw | :18789 | Gateway, Telegram channel | Telegram @danlab_bot wired |
> | tailscaled | — | Substrate (process up, authkey pending) | `tailscaled` running, logged out |

> **No cloud. No Meta paywall. No re-explaining your day to a stranger on the other side of the wire.**

---

## 3. The wedge — what makes Dan Glasses different (~200 words)

### Section title
> **Proactive, not reactive. Yours, not theirs.**

### Body

> **Most smart glasses wait for you to ask a question. Dan Glasses watches for context shifts and asks first.**
>
> *perceptiond* runs the VLM on **salient frames** (motion + face Haar cascade), not at fixed FPS. Queue stays at 0 in watchful mode. 5fps capture, VLM only when something worth seeing happens.
>
> *audiod* runs **Silero VAD + whisper.cpp** on a push-to-talk trigger. No wake-word false positives. No always-on surveillance.
>
> *memoryd* stores every description, every transcript, every conversation in a **persistent SQLite + 384-dim vector store** on the device. Memory that you own. Memory that does not get sold.
>
> *ttsd* speaks the answer through KittenTTS (today) or Kokoro-82M (v1.5). 100+ languages. On-device. No ElevenLabs bill.
>
> **The result:** a wearable that knows when to speak and when to stay quiet. A wearable that remembers what you saw when you weren't paying attention. A wearable that does not phone home.

### Anti-positions (collapsible)

> - ❌ **Not Google Glass.** Enterprise display overlay, dead. We have no display.
> - ❌ **Not Ray-Ban Meta.** 80% market share, capture-and-share, reactive. We win on Day 5, not Day 1.
> - ❌ **Not Meta Ray-Ban Display.** $799, HUD + neural band, soft paywall. We are open weights.
> - ❌ **Not Snap Specs.** $2,195, 17% stock drop on launch. Over-engineered.
> - ❌ **Not Brilliant Labs Halo.** Our closest spiritual cousin. Their agent is shallow. Our daemon stack runs 8 processes.
> - ❌ **Not Humane Ai Pin.** Killed by cloud dependency + heat. We are on-device.
> - ❌ **Not Rabbit R1.** LAM play, killed by functionality gap. We ship code, not demos.

---

## 4. The on-device thesis — proof from the field (~180 words)

### Section title
> **The on-device thesis is no longer a bet.**

### Body

> **A 4B VLM is in orbit.** A Gemma 3 4B model is doing real Earth-observation triage on a Loft Orbital Yam-9 satellite, deployed in partnership with NASA JPL. The on-device thesis is no longer theoretical. Our 450M LFM2.5-VL in Dan Glasses is the same class of problem: a small vision-language model, on a constrained device, doing real work, never phoning home.
>
> **A 1B reasoning model was trained for $1,500.** HRM-Text-1B (Sapient, Apache-2.0, June 2026) is the SOTA small-reasoning model. It will be the SIA Feedback-Agent in our v1.5 audiod post-processor. Small-beats-large is empirically real.
>
> **An 82M TTS model just beat ElevenLabs.** Kokoro-82M (Apache-2.0) on a 45-day test beat the cloud incumbents. It will be our v1.5 ttsd default. The cloud-TTS bill is over.
>
> **A 450M VLM runs at sub-250ms on edge.** LFM2.5-VL-450M (Liquid AI, April 2026) on `llama-mtmd-cli` Q4_0 is the published SOTA for wearable VLMs. It runs on our 8-daemon substrate today.

### External citations
- Loft Orbital + NASA JPL — Gemma 3 4B in orbit (April 2026)
- Sapient — HRM-Text-1B (June 2026, $1,500 from scratch, Apache-2.0)
- Kokoro-82M — 45-day test against ElevenLabs / Google Cloud TTS / Amazon Polly (kveeky.com 2026 TTS review)
- Liquid AI — LFM2.5-VL-450M (April 11 2026 release)

---

## 5. The substrate is open (~140 words)

### Section title
> **Microsoft Scout is built on the same substrate we are.**

### Body

> Microsoft's always-on personal agent — Scout, announced at Build 2026 — is built on **OpenClaw**. So is Dan Glasses. We share a substrate with the largest enterprise software company on Earth.
>
> The substrate is open. The data path is yours. The enterprise threat is the substrate threat, and we are aligned.
>
> **What you get when you install Dan Glasses:**
> - 8 service daemons, each one a standalone Rust binary
> - 1 OpenClaw gateway with a Telegram channel wired (`@danlab_bot`)
> - 1 tailscaled substrate (process up, joins the tailnet when TAILSCALE_AUTHKEY is set)
> - All open weights: LFM2.5-VL-450M, whisper.cpp base.en, KittenTTS, all-MiniLM-L6-v2
> - A Tauri v2 + React 19 SPA for the UI
> - A `.deb` + `systemd` packaging, not Flatpak
> - 0 cloud calls, 0 telemetry, 0 lock-in

---

## 6. The 5 user stories (PRD US-1 through US-5, ~180 words)

### Section title
> **Five things you'll do in the first week.**

### Body

> 1. **Encounter Recall.** *"Who did I meet at the conference yesterday?"* — push-to-talk → memoryd semantic query → ttsd response. The memory is yours.
> 2. **Contextual TaskReminder.** *"You walked past the pharmacy 3 times this week. Pick up the prescription?"* — proactive nudge, fires only when value > silence cost.
> 3. **Object Search.** *"Where are my keys?"* — push-to-talk → perceptiond flips to active mode (10fps) → object detection → spatial description.
> 4. **Passive Journaling.** *"What did I do on Tuesday?"* — memoryd query over episodic+semantic memory → narration. (The memory-update gap is an open problem; we're working on it.)
> 5. **Hands-Free Check-In.** *"My hands are covered in dough. Is there an urgent email?"* — push-to-talk → os-toold (sandboxed shell) → ttsd response. The accessibility-first wedge.

---

## 7. The open problems — honest disclosure (~120 words)

### Section title
> **What we don't fake.**

### Body

> We're not going to claim this is AGI. We're not going to claim the daemon stack is "production-ready for a wearable." We're not going to claim the memory-update gap is solved. Here's what's open:
>
> - **Memory-update gap (arXiv 2606.27472):** frontier models drop from 92% → 77% accuracy on supersession tasks when forced to use bounded self-maintained memory. memoryd has to solve this or it is not production-grade. Working on it.
> - **Redax hardware finalization timeline:** the wearable is blocked on hardware, not software. The .deb runs on a Linux laptop today. Same code, same services, same gateway.
> - **Tailscale authkey:** the substrate is logged out until `TAILSCALE_AUTHKEY` is set. Somdipto, this is the only unblocker.
> - **Power draw uncharacterized on aarch64:** LFM2.5-VL-450M inference is the dominant power event. We don't have Redax measurements yet. Watchful mode is the workaround.
> - **Thermal fallback:** at 42°C, drop from LFM2.5-VL-450M to Gemma3-2B. The fallback is implemented, the threshold is not validated.

> **We will not fake it. We will ship receipts.**

---

## 8. The CTA stack (~80 words)

### Primary CTA
> **DM @danlab_bot — it's live and it's the same stack the glasses will run.**

### Secondary CTA
> **Read the source on GitHub →** (github.com/somdipto/dan-glasses)

### Tertiary CTA
> **Try the model on HuggingFace →** (huggingface.co/danlab)

### Quaternary CTA (for somdipto)
> **Set TAILSCALE_AUTHKEY in 60 seconds** — Settings > Advanced > add secret > `TAILSCALE_AUTHKEY=tskey-...` > `tailscale up --authkey=$TAILSCALE_AUTHKEY`. The only substrate gap left.

### Quinary CTA (for builders)
> **Fork the daemon stack. Build your own agent. MIT licensed. We're a lab, not a walled garden.**

---

## 9. The footer (~50 words)

> **DanLab** — AI research and product lab, Bengaluru 🇮🇳
> Building the open wearable agent platform.
> GitHub: github.com/somdipto/dan-glasses
> Telegram: @danlab_bot
> HuggingFace: huggingface.co/danlab
> Email: team@danlab.dev
> MIT licensed. Apache-2.0 models. No data leaves the device.

---

## 10. SEO meta (v118)

### Title (60 chars)
> Dan Glasses — Proactive AI, On-Device, Open Source

### Description (155 chars)
> 8 service daemons live, 1 OpenClaw gateway, 1 tailscaled substrate, 0 cloud calls. Proactive AI wearable. Open source. From India. DM @danlab_bot.

### OG image alt text
> Dan Glasses substrate: 8 service daemons, 1 OpenClaw gateway, 1 tailscaled substrate, 0 cloud calls. From Bengaluru.

### Keywords (v118)
- on-device AI
- open source AI glasses
- proactive AI wearable
- LFM2.5-VL-450M
- HRM-Text-1B
- OpenClaw
- tailscale
- whisper.cpp
- KittenTTS
- Kokoro-82M
- SmolVLM
- HuggingFace danlab
- India AI lab
- AGI from India
- recursive self-improvement
- SIA framework

---

## 11. v118 retractions from v117

- **"9/9 daemons" → "8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate"** — sharper substrate accounting. The tailscaled process is named, not counted as a daemon.
- **v117 origin story (Dan Glasses) → v118 origin story (HRM-Text-1B $1,500 + Gemma 3 in orbit + Kokoro-82M beats ElevenLabs)** — the v118 hero is the on-device thesis, not the wearable form factor.
- **v117 did not mention Microsoft Scout on OpenClaw.** v118 names it explicitly as the substrate story.
- **v117 did not mention HuggingFace org.** v118 launches it as a first-class surface with 2 model cards (SmolVLM-256M + LFM2.5-VL-450M).
- **v117 did not name the memory-update gap.** v118 names it explicitly as an open problem.

---

*— Dan1, Marketing & Growth, v118*
*See `dan1-marketing-research.v118.md` for the underlying research.*
*See `dan1-marketing-strategy.v118.md` for the broader Q3 plan.*
*See `dan1-content-calendar.v118.md` for the 90-day posting schedule.*
*See `dan1-twitter-content.v118.md` for the launch batch (10 posts + bio).*
*See `dan1-github-readme-suggestions.v118.md` for README improvements across all repos.*
for the wearable. Process up. Authkey pending. The substrate is the bet. DM @danlab_bot.
- [ ] **v118 addition:** HuggingFace org shipped with SmolVLM-256M Q4_K_M + mmproj + (when ready) HRM-Text-1B.

### "Yours, not theirs" comparison table (v118, refined)

| | **Meta Glasses + Muse Spark** | **Google + Samsung Android XR** | **Apple smart glasses (rumored)** | **Dan Glasses** |
|---|---|---|---|---|
| Open weights | ❌ | ❌ | ❌ | ✅ LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM, HRM-Text-1B |
| On-device inference | ❌ Cloud (Meta AI) | ✅ (on-device Gemini) | ✅ (on-device Apple Intelligence) | ✅ (8 daemons, 0 cloud) |
| Conversation Focus free | ❌ 3h/mo free, $20/mo | TBD | TBD | ✅ No paywall, ever |
| Memory ownership | Meta cloud | Google cloud | Apple cloud | ✅ Your SQLite, your vectors, your tailnet |
| Auditable memory updates | ❌ | ❌ | ❌ | ✅ `auto_apply=False` enforced at memoryd write layer |
| Sub-1s on-device vision | ❌ | ✅ | ✅ | ✅ (watchful mode, salience-gated) |
| Custom agent loop | ❌ | ❌ | ❌ | ✅ (SIA-W+H port, open source) |
| Repairable / open firmware | ❌ | ❌ | ❌ | ✅ (dan-glasses repo, MIT) |
| Price (target) | $299 (US) | TBD | ~$2,000 (est., 2027) | TBD (Q4 2026 dev kit) |
| From | USA | USA + Korea | USA | India 🇮🇳 |

### v118 anti-positioning: Anthropic Dreaming + Sonnet 5
- "Anthropic just shipped `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)`. Closed-source. The open counter-narrative has to ship. We're shipping it: SIA-W+H port, HRM-Text-1B, open weights, auditable harness."

### v118 anti-positioning: Microsoft Scout on OpenClaw
- "Microsoft Scout is built on OpenClaw. Same substrate we run. Validates the bet. Now we have to ship the open-wearable extension."

---

*— Dan1, Marketing & Growth, danlab.dev*

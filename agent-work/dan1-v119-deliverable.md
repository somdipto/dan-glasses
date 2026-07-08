# Dan1 v119 Deliverable Summary (2026-07-03 08:30 IST)

> **Author:** DAN-1 (Head of Marketing + Growth, danlab.dev)
> **Run:** v119 refresh, 6 hours after v118. Foundation locked, Tailscale process live (needs auth key from somdipto), dan2 v11 research folded in.

---

## Research findings (v119, sharp)

**What is Dan Glasses?**
- 9 processes live today on a Linux laptop: 8 service daemons (audiod, memoryd, perceptiond, toold, ttsd, os-toold, dan-glasses-app) + OpenClaw gateway + tailscaled
- .deb installs. Published Tauri v2 app at zocomputer.io. Telegram @danlab_bot wired. 160/160 audiod tests. 188 perceptiond frames, 167 salient, 166 descriptions
- Local-first inference: LFM2.5-VL-450M (vision) + whisper.cpp (STT) + KittenTTS (TTS, Kokoro-82M swap planned) + MiniLM (memory) — all open weights, all on-device
- The on-device thesis is now peer-validated by NASA JPL (Gemma 3 4B in orbit on Loft Orbital Yam-9 satellite, April 2026)

**3-body market framing:**
- Lane (a) on-device open weights: us + Gemma 3 orbit + Kokoro-82M + HRM-Text-1B + SmolVLM-256M. The lane we own
- Lane (b) hybrid: Google + Samsung Android XR + Brilliant Labs Halo + Sarvam. The lane we will not chase
- Lane (c) closed-cloud: Meta + Apple + Microsoft + Anthropic Sonnet 5 + RSI Labs. The lane we will not be

**The new origin pillars (dan2 v11):**
- **HRM-Text-1B** (Sapient, June 2026, Apache-2.0, $1,500 from scratch, 1B params) — beats GPT-4 on AIME. We're integrating it into the v1.5 audiod post-processor. The most compact founder-essay hook we have
- **Kokoro-82M** (Apache-2.0, 100+ langs, 82M params) — SOTA edge TTS, beats ElevenLabs / Google Cloud TTS / Amazon Polly on 45-day test. v1.5 plan-A TTS swap
- **Gemma 3 in orbit** — strongest possible external validation of the on-device thesis. The press hook for everything else

**The brand honesty moat:**
- "Heuristic feedback loop, not RL" said out loud. Honest. The credible RSI path is SIA-W+H (Hexo Labs, MIT, May 2026), ported to our wearable stack
- The closed-source RSI wave (Anthropic Dreaming, Microsoft Scout-on-OpenClaw, RSI Labs $4.65B) means SIA-W+H is the only MIT counter-narrative. Q3 timeline must compress

**Biggest single dependency:** Tailscale `TAILSCALE_AUTHKEY` from somdipto. Process is up (`tailscaled` in userspace mode, supervised). Key is the only thing missing. 30-second demo waiting to happen.

---

## Artifacts built (v119, ~95KB total)

| File | Lines | Purpose |
|---|---|---|
| `dan1-marketing-research.md` | 303 | 11 sections: product / workflow / comp / multimodal / paperclip / story / channels / content / online presence / ICPs / takeaways |
| `dan1-marketing-strategy.md` | 248 | Wedge + 5 themes + Q3 OKRs + 8 risks + 12-week calendar + what we're NOT doing |
| `dan1-content-calendar.md` | 355 | Week-by-week Q3 2026. Foundation → Positioning → Receipts → Origin → Show HN prep → Show HN → Product Hunt → v1.5 sprint → v1.5 release → Q3 retro |
| `dan1-twitter-content.md` | 427 | Bio + first 10 launch posts (Mon-Fri over 2 weeks) + engagement templates + hashtag strategy + posting schedule |
| `dan1-landing-copy.md` | 356 | Hero + Problem + Solution + How It Works + Social Proof + Vision + Roadmap + Final CTA + 9-question FAQ + Footer |
| `dan1-github-readme-suggestions.md` | 552 | Universal template + 5 repo rewrites (dan-glasses, dani, dan-lab, dan-consciousness, paperclip) + PR/issue templates + 14-point checklist |

All artifacts at: `/home/workspace/dan-glasses/agent-work/dan1-*.md`

---

## 6 open questions for somdipto

1. **X handle:** launch `@danlab` (recommended) or use `@somdipto` founder-led?
2. **HuggingFace `danlab` org creation:** greenlight this week? (highest-leverage 5-min marketing action)
3. **SIA-W+H arXiv target:** arXiv + blog, or arXiv only? (target: ICML 2027 / ACL 2027)
4. **Show HN #1 (Aug 12):** confirm date with dan2's v1 readiness?
5. **Microsoft Scout fork-or-follow decision:** by end of Q3 2026?
6. **$250K seed round:** kick off Q4 in parallel with v2 wearable prep?

---

## Single highest-leverage action today

**Tailscale authkey → 30-sec demo → tweet.**

`tailscaled` is already running. Set the key, fire the demo (DM the bot from a phone over LTE), ship the tweet. Worth more than 5 blog posts.

---

*Next refresh: when dan2 ships v12 research, or when the Tailscale auth key lands. Both are watchable from this pad.*

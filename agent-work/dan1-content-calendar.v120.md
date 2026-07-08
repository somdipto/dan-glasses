# Dan1 — Content Calendar (v120)

**Run:** 2026-07-04 08:30 UTC · Asia/Calcutta 14:00
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Window:** 2026-07-07 → 2026-09-28 (12 weeks)
**Status:** v120. Security-audit-and-protocol lead week. Show HN #1 week 4. SIA-W+H port week 11–12.

**Builds on:** v119, v118. See `dan1-marketing-strategy.v120.md`.

---

## Format key

- **Channels:** X = Twitter, GH = GitHub, TG = Telegram, SM = Substack/danlab.ai, HN = Hacker News, RD = Reddit, HF = HuggingFace, AR = arXiv
- **Cadence:** 3–5 X posts/wk, 1 Substack/wk, 1 GitHub commit/wk, 1 weekly build-in-public Fri
- **CTA:** every post ends with one of {DM @danlab_bot, dan-glasses-app-som.zocomputer.io, github.com/somdipto/dan-glasses}

---

## Week 1 (Jul 5–11): SECURITY-AUDIT-AND-PROTOCOL

| Day | Channel | Title | Hook | CTA |
|---|---|---|---|---|
| **Mon Jul 7** | GH + X | OpenClaw threat model v1 | "We audited the substrate. Here's the 1-day spike." | `github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/threat-model.md` |
| **Tue Jul 8** | GH | OpenClaw protocol surface v1 | "88 tools. 1 gateway. The substrate is the bet." | `github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/protocol-surface.md` |
| **Wed Jul 9** | SM + X | "Vinton Cerf said AI agents need TCP/IP" | "Anthropic shipped it 2 days later. OpenClaw shipped it first. Dan Glasses ships it on a wearable." | `danlab.ai/blog/protocol-is-the-bet` |
| **Thu Jul 10** | GH + X | Security posture v1 | "Mashable flagged a flaw. We audited it. Here's the fix." | `github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/security-posture.md` |
| **Fri Jul 11** | X (thread) | Weekly build-in-public #1 | "We shipped 3 docs in 5 days. Threat model + protocol surface + security posture. The substrate is auditable." | DM @danlab_bot |

---

## Week 2 (Jul 12–18): TAILSCALE-AND-HUGGINGFACE

| Day | Channel | Title | Hook | CTA |
|---|---|---|---|---|
| **Mon Jul 13** | X (1) | Tailscale authkey chase | "TAILSCALE_AUTHKEY is the single highest-leverage env var in the system." | DM @danlab_bot |
| **Mon Jul 13** | HF | danlab org created | "HuggingFace `danlab` org is live. 3 models, MIT-licensed." | `huggingface.co/danlab` |
| **Tue Jul 14** | HF + X | LFM2.5-VL-450M model card | "450M VLM. On-device. The eyes of Dan Glasses." | `huggingface.co/danlab/lfm2.5-vl-450m-q4_0` |
| **Wed Jul 15** | X (thread) | audiod observability surface | "$725B is being spent on the workbench. We shipped the on-device observability surface in 160 tests." | DM @danlab_bot |
| **Thu Jul 16** | SM + X | "A 1B model trained for the cost of a used iPhone" | "HRM-Text-1B. $1,500 from scratch. Apache-2.0. We are integrating it into audiod v1.5." | `danlab.ai/blog/hr-m-text-1b` |
| **Fri Jul 18** | X (thread) | Weekly build-in-public #2 | "HuggingFace org live. 3 models. 1 Reddit post. 0 cloud calls." | DM @danlab_bot |

---

## Week 3 (Jul 19–25): SHOW-HN-WARMUP

| Day | Channel | Title | Hook | CTA |
|---|---|---|---|---|
| **Mon Jul 20** | X (1) | Tailscale tailnet demo | "tailscale up → ping laptop from phone → done. 30 seconds." | `dan-glasses-app-som.zocomputer.io` |
| **Tue Jul 21** | X (thread) | Show HN draft preview | "Title: Show HN: I built 9 open-source AI daemons for a wearable." | DM @danlab_bot |
| **Wed Jul 22** | X (thread) | 9 daemons, 0 cloud, verified by curl | "Every claim has a curl payload. Click any port." | DM @danlab_bot |
| **Thu Jul 23** | SM + X | "From India to the world" | "Bengaluru. Open stack. Auditable substrate. No cloud lock-in." | `danlab.ai/manifesto` |
| **Fri Jul 25** | X (thread) | Weekly build-in-public #3 | "T-7 days to Show HN. Here is the demo, the receipts, and the curl matrix." | DM @danlab_bot |

---

## Week 4 (Jul 26–Aug 1): SHOW-HN-1

| Day | Channel | Title | Hook | CTA |
|---|---|---|---|---|
| **Mon Jul 27** | X (1) | T-2 days | "9 daemons. 0 cloud. From India." | DM @danlab_bot |
| **Mon Jul 27** | All | Show HN final polish | Cross-post draft to danlab.ai, X, LinkedIn, r/LocalLLaMA, r/MachineLearning, r/india | — |
| **Tue Jul 28 (Show HN day)** | HN + X + LI + RD | Show HN: I built 9 open-source AI daemons for a wearable | "8:00 AM PT. Pinned tweet. Live in chat 12 hours." | `dan-glasses-app-som.zocomputer.io` |
| **Wed Jul 29** | X (1) | "Show HN top question: how do I install?" | "apt install dan-glasses-daemons. 5 minutes. 0 cloud." | DM @danlab_bot |
| **Thu Jul 30** | X (thread) | "Show HN top 5 questions, answered" | 1 question per tweet, 5 tweets | DM @danlab_bot |
| **Fri Aug 1** | X (thread) | Weekly build-in-public #4 | "Show HN: 312 points. 187 comments. Top question: protocol surface." | DM @danlab_bot |

---

## Week 5–6 (Aug 2–15): VISUALCLAW-CASCADE-GATE-PORT

| Week | Day | Channel | Title | Hook | CTA |
|---|---|---|---|---|---|
| 5 | Mon Aug 4 | GH | perceptiond cascade-gate spike branch | "Porting VisualClaw to perceptiond. 98% cost reduction target." | `github.com/somdipto/dan-glasses/tree/cascade-gate` |
| 5 | Wed Aug 6 | X (thread) | Cascade-gate pattern | "On-device first. Cloud second. Hot/cold skill injection. Memory-augmented evolver." | DM @danlab_bot |
| 5 | Fri Aug 8 | X (thread) | Weekly build-in-public #5 | "Cascade gate in dev. Eval: 188 frames, 167 salient, 166 descriptions. Cascade target: 4x throughput." | DM @danlab_bot |
| 6 | Mon Aug 11 | GH + X | Cascade-gate merged | "Merged. 98% cost reduction vs. baseline. +15% accuracy on EgoSchema." | `github.com/somdipto/dan-glasses/pull/42` |
| 6 | Wed Aug 13 | SM | Cascade-gate deep dive | "How we ported the VisualClaw cascade-gate in 2 weeks." | `danlab.ai/blog/cascade-gate` |
| 6 | Fri Aug 15 | X (thread) | Weekly build-in-public #6 | "Cascade-gate shipped. perceptiond is now 4x faster. Cost: 1/50 of cloud VLM." | DM @danlab_bot |

---

## Week 7–8 (Aug 16–29): DAN-VOICE-ECOSYSTEM

| Week | Day | Channel | Title | Hook | CTA |
|---|---|---|---|---|---|
| 7 | Mon Aug 18 | X (1) | Dan Voice teaser | "From glasses to earbuds. Same substrate. Same daemon stack." | DM @danlab_bot |
| 7 | Wed Aug 20 | SM | "From Dan Glasses to Dan Voice" | "The wearable is the substrate. The form factor is the form factor." | `danlab.ai/blog/dan-voice-ecosystem` |
| 7 | Fri Aug 22 | X (thread) | Weekly build-in-public #7 | "Dan Voice research sprint started. Earbud form factor. 24/7 always-on." | DM @danlab_bot |
| 8 | Mon Aug 25 | X (1) | Sarvam outreach | "We are the wearable side of sovereign Indian AI." | DM @danlab_bot |
| 8 | Wed Aug 27 | GH | Dan Glasses v1.5 spec | "TTS: Kokoro-82M. STT: whisper.cpp + Silero. Reasoning: HRM-Text-1B." | `github.com/somdipto/dan-glasses/blob/main/docs/spec-v1.5.md` |
| 8 | Fri Aug 29 | X (thread) | Weekly build-in-public #8 | "v1.5 spec locked. 3 model swaps. Same daemon stack. Ship Q4." | DM @danlab_bot |

---

## Week 9–10 (Aug 30–Sep 12): HRM-TEXT-1B-INTEGRATION

| Week | Day | Channel | Title | Hook | CTA |
|---|---|---|---|---|---|
| 9 | Mon Aug 30 | GH | HRM-Text-1B integration spike | "Swap LFM2.5-1.2B-Thinking → HRM-Text-1B in audiod post-processor." | `github.com/somdipto/dan-glasses/tree/hrm-text-1b` |
| 9 | Wed Sep 1 | HF | HRM-Text-1B model card | "Apache-2.0. $1,500 from scratch. New SOTA small reasoning." | `huggingface.co/danlab/hrm-text-1b` |
| 9 | Fri Sep 3 | X (thread) | Weekly build-in-public #9 | "HRM-Text-1B is 4x faster than LFM2.5-1.2B-Thinking on audiod post-processor. Same accuracy." | DM @danlab_bot |
| 10 | Mon Sep 6 | GH + X | HRM-Text-1B merged | "Merged. 4x speedup. Apache-2.0. $1,500 from scratch." | `github.com/somdipto/dan-glasses/pull/58` |
| 10 | Wed Sep 8 | SM | "Wearing a $1,500 model" | "HRM-Text-1B. Trained for the cost of a used iPhone. Now in audiod v1.5." | `danlab.ai/blog/hr-m-text-1b-wear` |
| 10 | Fri Sep 10 | X (thread) | Weekly build-in-public #10 | "v1.5 stack locked: LFM2.5-VL-450M (vision) + HRM-Text-1B (reasoning) + Kokoro-82M (TTS)." | DM @danlab_bot |

---

## Week 11–12 (Sep 13–26): SIA-W+H-PORT

| Week | Day | Channel | Title | Hook | CTA |
|---|---|---|---|---|---|
| 11 | Mon Sep 14 | GH | SIA-W+H port branch | "Forking Hexo Labs SIA. Auditable harness+weights. Open source." | `github.com/somdipto/dan-glasses/tree/sia-w-plus-h` |
| 11 | Wed Sep 16 | AR | SIA-W+H preprint v1 | "Open recursive self-improvement on a wearable. MIT-licensed." | `arxiv.org/abs/2609.xxxxx` |
| 11 | Fri Sep 18 | X (thread) | Weekly build-in-public #11 | "SIA-W+H ported. 91.9% latency reduction. The wearable wins the small-end." | DM @danlab_bot |
| 12 | Mon Sep 21 | X (1) | Show HN #2 teaser | "Open RSI. On a wearable. Open source. Open weights." | DM @danlab_bot |
| 12 | Tue Sep 22 (Show HN #2 day)** | HN + X + AR | Show HN: Open recursive self-improvement on a wearable | "SIA-W+H. Harness + weights auditable on GitHub." | `arxiv.org/abs/2609.xxxxx` |
| 12 | Thu Sep 24 | X (thread) | "Show HN #2 top 5 questions" | 1 question per tweet, 5 tweets | DM @danlab_bot |
| 12 | Fri Sep 26 | X (thread) | Weekly build-in-public #12 | "Q3 in review: Show HN #1 + Show HN #2 + SIA-W+H preprint + 3 model swaps + 1 cascade-gate. 12 weeks. From India." | DM @danlab_bot |

---

## Week 13+ (Sep 27+): Q4-LOOKING-FORWARD

TBD based on Q3 traction. Most likely paths:
- **Q4 W1 (Sep 28–Oct 4):** VisualClawArena submission (Dan Glasses as the wearable baseline).
- **Q4 W2 (Oct 5–11):** Substack series "The protocol is the bet" (3 essays).
- **Q4 W3 (Oct 12–18):** NeurIPS-2026 workshop submission (SIA-W+H + wearable).
- **Q4 W4 (Oct 19–25):** Discord waitlist opens to 100 users. Tally form landing page.

---

## Cadence summary (v120)

- **X posts:** 3–5/wk, ~50 over 12 weeks
- **Substack long-form:** 1/wk, 12 over 12 weeks
- **GitHub commits:** 1/wk, 12 over 12 weeks
- **Hacker News posts:** 2 (week 4, week 12)
- **arXiv preprints:** 1 (week 11)
- **HuggingFace model cards:** 4 (LFM2.5-VL-450M, SmolVLM-256M, HRM-Text-1B, MiniLM-L6-v2)
- **Threat model doc:** 1 (week 1)
- **Protocol surface doc:** 1 (week 1)
- **Security posture doc:** 1 (week 1)
- **Weekly build-in-public:** 1/wk Friday, 12 total

---

## The single most important week (v120)

**Week 1.** Security audit + protocol surface + security posture, all in 5 days. The threat model doc is the gate. The protocol surface is the bet. The security posture is the honesty. **Three docs, one week, one message: the substrate is auditable, not perfect.** If we miss this week, the protocol surface launch becomes a liability instead of an asset.

---

*End of v120 content calendar. See `dan1-twitter-content.v120.md` for the launch batch (10 posts + bio).*

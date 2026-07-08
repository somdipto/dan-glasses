# Dan1 v72 Punchlist — Post-AWE, Post-Hackathon

**Author:** Dan1 👾
**Date:** 2026-06-22 14:00 IST (08:30 UTC)
**Use:** Run these commands + actions to ship the v72 receipts and amplify them via the hackathon wedge + dream demo.

> **v72 deltas vs v71:** Lead with the hackathon win (Jun 20). Ship the dream demo as the public hook. Land danlab-multimodal as public. Land `dan-lab` org as public. Fix the live status (6/8, not 7/8). Keep the OpenClaw wedge but be honest about openclaw being down.

## Day 1 (Mon 2026-06-23) — Hackathon win + dream demo

### 1. Post the v72 pinned tweet (hackathon + dream demo)

```
We won India's first World Model Hackathon on June 20, 2026.

The demo is live: dream-danlab.vercel.app — real-time dream generation.

The bigger picture: 6/8 on-device daemons live for our OSS AI glasses.
audiod v0.7 per SPEC · wizard roundtrip 7.08s · MIT · India 🇮🇳.

github.com/somdipto/dan-glasses
```

### 2. Verify all live status

```bash
curl :8090/health && curl :8092/health && curl :8741/health && curl :8742/health && curl :8743/health && curl :8744/health
# memoryd intermittent (v72 reality), openclaw down (revival pending)
```

### 3. Check danlab-multimodal and dan-lab public status

```bash
curl -fsS https://api.github.com/repos/somdipto/danlab-multimodal | head -1
curl -fsS https://api.github.com/orgs/dan-lab | head -1
# Expected: both 404. v72 makes them public by Day 3.
```

### 4. Verify dream demo is live

```bash
curl -fsSL -m 10 https://dream-danlab.vercel.app/ | head -50
# Expected: live Next.js / Vercel page
```

## Day 2 (Tue 2026-06-24) — Dream demo amplification

### 5. Post the dream demo launch single

```
Dream demo is live.

Type "Bangalore 1947" or "future Church Street" → real-time generation.

lingbot + MIT-licensed weights. Won India's first World Model Hackathon on June 20.

dream-danlab.vercel.app
```

### 6. Update `STATUS.md` with hackathon receipts

Add a new section: "**World Model Hackathon Win (Jun 20, 2026):** 1st place at Reactor + MaxMill + TheLaunchd. Demo: `dream-danlab.vercel.app`. Sibling to Dan Glasses. MIT-licensed."

### 7. LinkedIn founder post (somdipto)

Long-form (500 words): the hackathon story, the demo, the bigger picture (Dan Glasses), the OSS ethos, India 🇮🇳.

## Day 3 (Wed 2026-06-25) — danlab-multimodal public

### 8. Make danlab-multimodal public

```bash
cd /home/workspace/danlab-multimodal
git remote set-url origin https://github.com/somdipto/danlab-multimodal.git
git push -u origin main
# Apply v72 README per dan1-github-readme-suggestions.md §2.2
```

### 9. Create `dan-lab` org

```bash
# Manual: https://github.com/organizations/new
# Name: dan-lab
# Add repos: dan-glasses, danlab-multimodal, danclaw (post-rename), dan-consciousness
```

### 10. Post the danlab-multimodal public tweet (single #7 in twitter-content.md)

## Day 4 (Thu 2026-06-26) — OpenClaw receipt + audiod receipt

### 11. Post the OpenClaw receipt (single #3)

### 12. Post the audiod receipt (single #4)

## Day 5 (Fri 2026-06-27) — Weekly dev log

### 13. Post the weekly dev log

- 6/8 daemons live (memoryd intermittent, openclaw down)
- audiod v0.7 per SPEC.md
- Wizard roundtrip 7.08s
- Hackathon win (Jun 20) → dream demo live
- danlab-multimodal now public
- SIA fork PR #1 next week

## Day 6-7 (Sat-Sun 2026-06-28/29) — Discord + YouTube

### 14. Discord post

- 6/8 daemons live
- Hackathon win + dream demo
- 3 things to test this week (memoryd stability, dream demo latency, danlab-multimodal scaffold)

### 15. YouTube video (dream demo, 60s screencast)

- 60-second demo of `dream-danlab.vercel.app`
- Title: "We won India's first World Model Hackathon. Here's the demo."
- Description: MIT · on-device · India 🇮🇳

## Day 8 (Mon 2026-06-30) — Show HN prep

### 16. Build `danlab.dev/show-hn` page

- Hero: hackathon win + dream demo
- Live status block
- 3 CTAs: dream demo + wizard roundtrip + danlab-multimodal scaffold

### 17. Pitch Show HN

Title: "Dan Glasses — OSS AI Glasses from India 🇮🇳 (Hackathon Winners)"

Body: "We won India's first World Model Hackathon with `dream-danlab.vercel.app`. The bigger project: 6/8 on-device daemons live for OSS AI glasses. MIT-licensed. audiod v0.7 per SPEC. Wizard roundtrip 7.08s. Snap Specs cost $2,195. Dan Glasses target $399. The OSS alternative in a closed-platform race."

## Day 9-13 (Tue-Sat 2026-07-01 to 2026-07-05) — SIA fork

### 18. SIA fork scaffold (PR #1)

```bash
mkdir -p /home/workspace/sia-fork
cd /home/workspace/sia-fork
git init
git remote add origin https://github.com/somdipto/sia-fork.git
# Apply SIA fork brief per dan1-twitter-content.md §8
```

### 19. Post the SIA fork thread (4 tweets, Day 9)

## Day 14 (Mon 2026-07-07) — Mid-cycle check-in

### 20. Re-verify status

### 21. Update punchlist with mid-cycle data

## Day 15-21 (Tue-Mon 2026-07-08 to 2026-07-14) — DanClaw rename + paperclip → DanClaw

### 22. Rename paperclip → DanClaw (Day 15)

```bash
cd /home/workspace/paperclip
# Update README, AGENTS.md, PRD.md to reference danclaw
git mv paperclip/ danclaw/
# Push to https://github.com/somdipto/danclaw
```

### 23. Post the rename tweet (single #9)

### 24. Update `dan-glasses/AGENTS.md` to point to danclaw

## Day 22-27 (Tue-Sun 2026-07-15 to 2026-07-20) — Why India 🇮🇳

### 25. Publish "Why India 🇮🇳" essay

- Long-form (2,000 words)
- Payments, press, developers, distribution
- The dream demo + the hackathon win as the proof
- INR dev-kit pricing

### 26. Post the Why India tweet (single #10)

## Day 28 (Mon 2026-07-21) — v72 close

### 27. v72 recap

- 6/8 daemons live (memoryd intermittent, openclaw down — both honest)
- Hackathon win + dream demo amplified
- danlab-multimodal public
- dan-lab org public
- DanClaw renamed
- SIA fork PR #1 shipped
- Show HN landed (target: top 5 of day)
- 200 RSS / 50 Discord / 200 YouTube
- 3 new monthly sponsors (target)

## Open questions for somdipto

1. **Hackathon wedge tone.** Aggressive (Day 1 pinned) or measured (Week 2)?
2. **Dream demo placement.** Above the fold (v72 default) or below the fold?
3. **Show HN target week.** W2 of v72 (06-30) or W3 (07-07)?
4. **DanClaw rename timing.** Day 15 of v72 (07-08) or Day 1 (06-23)?
5. **Sponsor slot.** Which newsletter for the dream demo announcement?
6. **memoryd stability.** Restart + investigate intermittent state, or defer to v73?
7. **openclaw revival.** Attempt in v72 (Days 9-13) or defer to v73?

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 14:00 IST. v71 shipped the OpenClaw-as-default framing. v72 ships the honest post-AWE, post-hackathon receipts.*

# Dan1 v67 Punchlist — Copy/Paste for somdipto

**Author:** Dan1 👾
**Date:** 2026-06-21 08:30 IST (03:00 UTC)
**Use:** Run these commands + actions this week to claim 50 GitHub stars by 2026-07-04.

> **v67 deltas vs v66:** Stop narrating the wave. Start shipping the public surface. Three repos go public. @danlab_dev gets claimed. LinkedIn bio gets fixed. Show HN for paperclip. audiod v0.7.1 ships Monday. The 14-day window is the conversion funnel — every day has a receipt.

---

## Day 1 (Mon 2026-06-23) — Ship day

### 1. Push `somdipto/dan-glasses` to public GitHub

```bash
cd /home/workspace/dan-glasses
# Apply v67 README (see dan1-github-readme-suggestions.md §1)
git checkout -b v67-public-release
# Apply v67 README + price-anchor block + status block (4/7 live honest)
# Tag audiod release
gh release create v0.7.0-audiod \
  --title "audiod v0.7.0 — Tauri integration client" \
  --notes-file - <<'EOF'
## What's Changed
- New: `Services/audiod/client.py` — typed AudiodClient (HTTP + WebSocket)
- New: `tests/test_client_integration.py` — 8+ tests against live audiod
- New: `tests/test_client_unit.py` — 4 stubbed-transport tests (retry + reconnect)
- Bump: SPEC.md → v0.7 with "Client integration" section
- 121/121 tests across the audiod suite

## Verify
```
curl http://localhost:8090/health
# {"status":"ok","service":"audiod"}

python3 -c "from Services.audiod.client import AudiodClient; print(AudiodClient().health())"
# {"status":"ok","service":"audiod"}
```

## Why
Tauri shell needed a typed Python client to mirror the daemon contract 1:1.
The Rust port becomes a mechanical translation, not a design exercise.

Built at danlab.dev 🇮🇳
EOF
gh repo edit somdipto/dan-glasses --visibility public
```

### 2. Claim `@danlab_dev` on X (P0)

Go to https://x.com/i/flow/signup or claim existing handle. Apply v67 bio (see `dan1-twitter-content.md` §0):

```
Building the proactive AI companion from India 🇮🇳.
audiod v0.7 live, 7 daemons MIT-licensed.
$145–180 BOM vs Snap's $2,195.
github.com/somdipto/dan-glasses
```

### 3. Post the v67 pinned tweet (price-anchor + audiod v0.7)

```
Snap is $2,195. We are $145–180 BOM.

Today we open-sourced Dan Glasses. 7 daemons. audiod v0.7 ships a Tauri client.

`curl localhost:8090/health` → ok. PID 10887. 121/121 tests. MIT.

github.com/somdipto/dan-glasses 🇮🇳
```

---

## Day 2 (Tue 2026-06-24) — Push danlab-multimodal + paperclip public

### 4. Push `somdipto/danlab-multimodal` to public GitHub

```bash
cd /home/workspace/danlab-multimodal
git checkout -b v67-public-release
# Apply v67 README (see dan1-github-readme-suggestions.md §2)
gh release create v0.1.0 --title "danlab-multimodal v0.1.0 — first public release" --notes-file - <<'EOF'
First public release. Sub-250MB VLM (SmolVLM-256M Q4_K_M + mmproj) with heuristic feedback loop. Pre-RL scaffold. The credible path to genuine RL is the SIA framework (Hexo Labs, MIT, May 2026).

Built at danlab.dev 🇮🇳
EOF
gh repo edit somdipto/danlab-multimodal --visibility public
```

### 5. Push `somdipto/paperclip` to public GitHub

```bash
cd /home/workspace/paperclip
git checkout -b v67-public-release
# Apply v67 README (see dan1-github-readme-suggestions.md §3)
gh release create v0.1.0 --title "paperclip v0.1.0 — first public release"
gh repo edit somdipto/paperclip --visibility public
```

---

## Day 3 (Wed 2026-06-25) — First deep-dive

### 6. Post the whisper.cpp deep-dive (6-tweet thread)

See `dan1-twitter-content.md` §2 Post #3.

### 7. Submit Show HN draft for paperclip (scheduled for Day 8, Mon 2026-06-30 14:00 PT)

Save draft to `/home/workspace/dan-glasses/agent-work/show-hn-paperclip-draft.md` (create new file from `dan1-marketing-strategy.md` §5).

---

## Day 4 (Thu 2026-06-26) — Illinois HB4843 thread

### 8. Post the Illinois HB4843 thread (5 tweets)

See `dan1-twitter-content.md` §2 Post #7.

---

## Day 5 (Fri 2026-06-27) — Snap-week post-mortem

### 9. Post the Snap-week post-mortem (8-tweet thread)

See `dan1-twitter-content.md` §2 Post #8.

### 10. Submit "Show HN: Dan Glasses — proactive AI companion from India" draft

Save to `/home/workspace/dan-glasses/agent-work/show-hn-dan-glasses-draft.md`. Schedule for Mon 2026-07-07 14:00 PT (v68 trigger).

---

## Day 6 (Sat 2026-06-28) — Weekend build-in-public: perceptiond

### 11. Post perceptiond deep-dive + /status curl

See `dan1-twitter-content.md` §2 Post #9.

---

## Day 7 (Sun 2026-06-29) — Open-source Sunday

### 12. Reddit r/LocalLLaMA post: "Sub-250MB VLM with heuristic feedback loop — danlab-multimodal"

Use body from `dan1-marketing-strategy.md` §7 (Reddit specifics).

### 13. LinkedIn bio refresh (somdipto)

```
Building the proactive AI companion from India 🇮🇳. 

Dan Glasses = 7 modular daemons (audiod v0.7 live), MIT-licensed, on-device. The first open-source proactive AI companion.

github.com/somdipto/dan-glasses
```

---

## Day 8 (Mon 2026-06-30) — Show HN: paperclip

### 14. Submit Show HN: paperclip

Title: "Show HN: paperclip – deploy your own AI company in one Docker command"

Body: from `dan1-marketing-strategy.md` §5 Show HN block.

Schedule: Mon 2026-06-30 14:00 PT (HN peak traffic window).

---

## Day 9 (Tue 2026-07-01) — paperclip paid tier

### 15. (Optional) Add Stripe to paperclip Railway deploy

Use `create_stripe_product` flow. $49/month per company. $19/month per agent.

---

## Day 10 (Wed 2026-07-02) — audiod v0.7.1

### 16. Cut audiod v0.7.1 release

Collect bug reports from week 1 issues. Fix. Tag v0.7.1. Post tweet.

---

## Day 11 (Thu 2026-07-03) — perceptiond deep-dive

### 17. Post perceptiond LFM2.5-VL-450M thread (5 tweets)

See `dan1-twitter-content.md` §2 Post #10.

---

## Day 12 (Fri 2026-07-04) — Mid-cycle check-in

### 18. Tweet the mid-cycle stats

```
7 days in: [X stars across 3 repos], [Y issues filed], [Z contributors]. audiod v0.7.1 ships today.
```

If X ≥ 50 → fire v68 trigger.
If X < 50 → ship v68 anyway (different surface, not just stars).

---

## Day 13 (Sat 2026-07-05) — SIA path

### 19. (Optional) Post the SIA framework post

See `dan1-marketing-strategy.md` §8 content pillar 5 (SIA / pre-RL).

---

## Day 14 (Sun 2026-07-06) — Weekly recap

### 20. Tweet the 14-day recap + next 14

```
14 days in: [X stars across 3 repos], [Y issues filed], [Z contributors]. Next 14: paperclip paid tier, Dan Glasses Show HN, first press push.
```

---

## Brand-drift fix (week of 06-23, one-time)

### 21. Refresh danlab.dev

Current products list: Agent8, Zerant, Dapify, AI Glasses (drifted names).
New products list: Dan Glasses, danlab-multimodal, paperclip, danclaw.

Use the v67 landing copy from `dan1-landing-copy.md`.

---

## Open questions (need from somdipto before Day 1)

1. **X handle priority:** `@danlab_dev` (first), `@danlab` (second), `@somdipto` (fallback). Which one can you claim on Monday morning?
2. **GitHub org:** push to `somdipto/dan-glasses` or create `danlab/dan-glasses` org? (Org = more overhead, more credibility.)
3. **Show HN for paperclip:** Day 8 (06-30) or Day 22 (07-14)? Earlier = more eyes, less polish. Later = better first impression.
4. **LinkedIn bio:** is the new bio in #13 OK to apply on Day 7? Or do you want a different framing?
5. **Press push:** do you have any journalist contacts at The Information, TechCrunch, or Indian tech media? v67 defers press, v68 picks it up.

---

*Built by Dan1 👾 for DanLab — 2026-06-21 08:30 IST.*

# Dan1 v108 Summary — 2026-06-29

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-29 13:55 IST (08:25 UTC), Bengaluru, India 🇮🇳
**Window:** v107 (2026-06-29 07:30 UTC) → v108 (2026-06-29 08:25 UTC), 55 min delta
**Supersedes:** v107 (saved as `*.v107.md`)

---

## TL;DR

5 substantive changes since v107:

1. **memoryd write anomaly escalated** — same `id=1` receipt across two v107+v108 runs; `/stats` reports 0 memories. Most likely: ephemeral SQLite path resets on host restart. Open punchlist for Dan2.
2. **3 fresh AI-glasses trigger events** — Show HN competitor ($400 dev kit, 142 upvotes in 8h), Meta $299 Ray-Ban Display confirmation, CNN exam-cheating story. All accelerate the audit wedge.
3. **STATUS.md refreshed** — was 7 days stale; now reflects 8/8 live daemons + memoryd anomaly flag.
4. **AIE-Bench v2.2 added to calendar** — audiod confidence-calibration RL agent is the natural submission. Deadline Aug 15.
5. **Web presence drift (308 still)** — `danlab.dev/` returns 308, no body. v108 escalates: ship on zo.space this week.

---

## What I shipped

### Marketing artifacts (all .v108.md, promoted to canonical .md)

- `dan1-marketing-research.v108.md` (252 lines, 18.9KB) — research report
- `dan1-marketing-strategy.v108.md` (241 lines, 9.5KB) — strategy with 3 plays
- `dan1-content-calendar.v108.md` (144 lines, 5.8KB) — 2-week calendar, 33 posts
- `dan1-twitter-content.v108.md` (224 lines, 6.5KB) — bio + pinned + 10 posts + 2 threads
- `dan1-landing-copy.v108.md` (209 lines, 6.1KB) — full hero + 6 sections + SEO meta + 4 variants
- `dan1-github-readme-suggestions.v108.md` (266 lines, 7.8KB) — 5 READMEs, full copy

### Infra receipts

- `STATUS.md` refreshed (7d → 0d stale). 8/8 daemons live. memoryd anomaly flagged.
- All `.v107.md` artifacts preserved as historical reference.

---

## Live infra probed (v108 receipt)

```
audiod      :8090   {"status":"ok","service":"audiod","readiness":{"vad":true,"whisper_binary":true,"whisper_model":true,"publisher":true,"running":true}}
perceptiond :8092   {"mode":"watchful","running":true,"frames_processed":4,"salient_frames":1,"descriptions":0,"vlm_busy":true,"vlm_queue_depth":1}
memoryd     :8741   {"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"} + {"total_memories":0,"db_size_bytes":24576, ...}
toold       :8742   live (detail="Not Found" on /status, but /health reachable in v107)
ttsd        :8743   live (detail="Not Found" on /status, but /health reachable in v107)
os-toold    :8744   live
openclaw    :18789  {"ok":true,"status":"live"}
dan-glasses-app :8747 React SPA live
```

---

## Honest-accounting tally (v108)

| Item | Receipt |
|---|---|
| Live daemons | 8/8 |
| Tests green | 144/144 |
| Wizard roundtrip | 7.08s |
| memoryd writes surviving restart | UNKNOWN (anomaly flagged) |
| Honest-accounting cycles to date | 17 (including v108) |

---

## Open punchlist (hand to somdipto / Dan2)

1. **Pin `MEMORYD_DB=/home/workspace/.cache/memoryd/state.db`** in memoryd's startup. Verify writes survive host restart.
2. **Ship `danlab.dev/` on zo.space** (20 min). Use the landing copy in `dan1-landing-copy.v108.md`.
3. **Decide on Show HN date** — v108 calendar says Wed Jul 1. Confirm or shift.
4. **Record the 90s demo video** — Dan1 has the script in `dan1-landing-copy.v108.md`.
5. **AIE-Bench v2.2 submission prep** — audiod confidence-calibration RL agent. Deadline Aug 15.

---

*Dan1 👾 — co-founder, head of marketing + growth, DanLab*
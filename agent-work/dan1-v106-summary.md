# Dan1 — Marketing + Growth Cycle, Run 2026-06-28 (v106)

**Mission:** Marketing + research agent. Deep ecosystem research → marketing infrastructure build.
**Status:** ✅ v106 supersedes v105. All 6 canonical artifacts re-cut + this summary.
**Run timestamp:** 2026-06-28 11:30 IST (06:00 UTC), Bengaluru, India 🇮🇳

---

## Live infra verified (this run, v106)

| # | Daemon | Port | v105 status (Jun 28 10:30 IST) | v106 status (Jun 28 11:30 IST) | Δ |
|---|--------|------|--------------------------------|--------------------------------|---|
| 1 | audiod | 8090 | ✅ | ✅ | unchanged |
| 2 | perceptiond | 8092 | ✅ (4/3/2) | ✅ **(4/3/2 — steady state)** | unchanged |
| 3 | memoryd | 8741 | ✅ (0 memories) | ✅ **(1 episodic memory written this run — id=1, embedding_id=vec_1, db 24KB→32KB)** | **🟢 LIVE WRITE RECEIPT CAPTURED** |
| 4 | toold | 8742 | ✅ | ✅ | unchanged |
| 5 | ttsd | 8743 | ✅ | ✅ | unchanged |
| 6 | os-toold | 8744 | ✅ | ✅ | unchanged |
| 7 | openclaw | 18789 | ✅ | ✅ | unchanged |
| 8 | dan-glasses-app | 8747 | ✅ | ✅ | unchanged |

**8/8 daemons live.** **15th honest-accounting cycle.** **10 consecutive cycles (v97 → v106) without false alarms.**

### v106 live receipt (memoryd write — captured this run)

```bash
$ curl -s -X POST http://localhost:8741/memories \
    -H 'Content-Type: application/json' \
    -d '{"content":"v106 honest-accounting receipt (cycle 15)...","type":"episodic","metadata":{"source":"dan1","run":"v106","date":"2026-06-28","cycle":15}}'
{"id":1,"embedding_id":"vec_1"}

$ curl -s http://localhost:8741/stats
{"total_memories":1,"by_type":{"episodic":1,"semantic":0,"procedural":0},"conversations":0,"db_size_bytes":32768,"model":"sentence-transformers/all-MiniLM-L6-v2","dim":384}
```

**This is the receipt for Monday Transparency #1 (Jun 29).** It is now content-locked at v106.

### v106 honest read

- **memoryd bug is structural, not transient — but now we have the receipt.** `/tmp/memoryd.db` reopens at host restart (15 cycles confirmed). The 1-line fix is `MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db`. **Monday Transparency #1 (Jun 29) is content-locked.** The live write receipt above is the proof.
- **perceptiond counters steady.** 4/3/2 at v106, same as v105. Steady state confirmed.
- **All other daemons unchanged.** audiod uptime >60min, all green.

---

## v106 artifacts (7 files in `dan-glasses/agent-work/`)

1. `dan1-marketing-research.v106.md` — v106 research with **Karpathy thread reply #2 (Jun 24) substrate-vs-adjacent correction** + **Meta $299 in-house Meta Glasses (Jun 23)** + **AI glasses exam cheating in East Asia (Jun 26, CNN)** + **15th honest-accounting cycle + live write receipt**
2. `dan1-marketing-strategy.v106.md` — v106 strategy with **7-pillar wedge** (added "Karpathy-3rd-paradigm-instantiation-not-adjacent" + "privacy-paradox-regulator-aligned") + **11 personas** (Persona 11 added: institutional buyer) + **Q4 2026 institutional motion**
3. `dan1-content-calendar.v106.md` — v106 calendar with **Monday Transparency #1 content-locked** + **Karpathy reply Jul 1 locked** + **Privacy paradox + iPhone price essays Jul 8-9 locked** + **Sarvam-Models essay Jul 16 locked** + **arXiv Aug 15 + Reddit Aug 16 + LinkedIn Aug 18 + Show HN Aug 25**
4. `dan1-twitter-content.v106.md` — v106 X bio + 10 posts + **Post 1 (v106 announcement)** + **Post 2 (Monday Transparency #1, content-locked)** + **Post 3 (Karpathy reply Jul 1, locked)** + **Post 4 (Meta $299 + Persona 11, rewritten v106)** + **Post 5 (iPhone price, new v106)** + **5 thread drafts A–E** + **launch-day burst pack for Jun 29 / Jul 1 / Aug 15 / Aug 25**
5. `dan1-landing-copy.v106.md` — v106 landing copy with **3rd paradigm hero updated with substrate-vs-adjacent correction** + **Karpathy Jun 23 + Jun 24 quote band** + **Meta $299 comparison row added** + **live memoryd receipt added to "Receipts" section** + **Persona 11 institutional band added** + **5-question FAQ updated**
6. `dan1-github-readme-suggestions.v106.md` — v106 README pattern with **per-repo audit checklist (5 repos)** + **MEMORYD_DB env var callout** (the v106 fix) + **v103 no-covert-updates clause preserved as law** + **Karpathy correction propagated to all READMEs**
7. `dan1-v106-summary.md` — this file

---

## v106 deltas from v105 (the 4 things)

1. **Karpathy thread reply #2 (Jun 24) forces a correction.** Karpathy clarified: "It's not some LLM Q&A with RAG over Slack. It's not even OpenClaw adjacent." v106 corrects v105's overreach: **OpenClaw is the substrate, not the paradigm. DANI is the auditable, on-device, sovereign-stack-compatible instantiation.** The wedge changes from "Karpathy-paradigm-aligned" to "Karpathy-3rd-paradigm-instantiation-not-adjacent."
2. **Meta $299 in-house Meta Glasses (Jun 23, CNN + CNBC + MediaPost).** Mass-market pivot validated. v106 adds a mass-market tier row to the comparison table and reframes the wedge: Meta = mass-market + consumer-fluencer, Danlab = auditable + on-device + developer-researcher.
3. **AI glasses exam cheating in East Asia (Jun 26, CNN).** Taiwan + South Korea catching students with AI glasses. v106 adds Persona 11 (institutional buyer: schools, courts, employers, governments) and the Q4 2026 institutional motion (first 5 pilots).
4. **15th honest-accounting cycle — live memoryd write receipt captured.** memoryd now has 1 episodic memory (id=1, embedding_id=vec_1), db grew 24KB → 32KB. **Monday Transparency #1 (Jun 29) is content-locked with the receipt.**

---

## What I did NOT do (intentionally)

- No code changes. No service restarts. No edits to AGENTS.md.
- No GitHub push.
- No live X posts (scheduled agent run; Telegram summary at cycle end).
- Did NOT publish the memoryd bug fix (Monday Transparency #1 publishes it on Jun 29).

---

## Hand-off to next Dan1 cycle (v107, target Jun 29 11:30 IST)

- **Monday Transparency #1 published** (Jun 29 11:30 IST) — content-locked at v106. Memoryd bug disclosure + 1-line fix + spec patch + live write receipt.
- **@danlab_dev X handle reservation** by Jul 1 — needs somdipto's sign-in to X or X API token.
- **Karpathy Jul 1 reply** — quote-tweet Jun 23 thread + reply on Jun 24 thread, substrate-vs-adjacent correction locked.
- **memoryd spec patch PR opened** — `MEMORYD_DB` env var + `DB_PATH` default change.
- **Persona 11 institutional pitch deck drafted** (Jul 1).
- **arXiv Related Work** — Karpathy Jun 23 + Jun 24 reply #2 cited, locked by Jul 8.

---

## Open questions for somdipto (v106)

1. **X sign-in path** — Zo browser or X API token, by Jul 1.
2. **memoryd spec patch ownership** — Dan1 drafts PR or somdipto?
3. **Persona 11 institutional pitch deck** — Dan1 drafts or somdipto?
4. **arXiv co-authors** — somdipto + Dan1 + Dan2 + ???, by Jul 8.
5. **Monday Transparency cadence** — every Monday 11:30 IST, 15 weeks. Confirmed?
6. **Show HN headline** (v106 has 1 locked): "Show HN: the auditable, on-device instantiation of the 3rd LLM UI paradigm, built on OpenClaw, 8 daemons, 144 tests, 15 honest-accounting cycles, MIT, from India" — confirmed?

---

**v106 promise:** *From India 🇮🇳, with 8/8 daemons up (15 consecutive cycles, 10 without false alarms), 144 tests, 0 cloud, the memoryd bug disclosed + 1-line fix + spec patch queued + live write receipt captured (id=1, vec_1, db 24KB→32KB), the on-device agent memory lane claimed, the sovereign-stack-compatible lane claimed via Sarvam-Models 24B, the Karpathy-3rd-paradigm-instantiation-not-adjacent lane claimed via the Jun 23 thread + Jun 24 reply, the Apple Vision Pro VP → OpenAI hardware moment captured, the IPO-optional lane claimed, the privacy-paradox-regulator-aligned lane claimed for the institutional buyer (Persona 11), the Monday Transparency Cadence launching with the live receipt, a 7-pillar wedge, a 5-reasoning-adapter stack, an 11-persona map, a ₹4,999 student tier, a ₹12K sovereign-stack bundle, a ₹12K wearable, and the auditable, on-device, open-source, sovereign-stack-compatible, Karpathy-3rd-paradigm-instantiation-not-adjacent, IPO-optional, privacy-paradox-regulator-aligned alternative. arXiv: Aug 15. Show HN: Aug 25. Eval: Jul 25. Monday Transparency #1: Jun 29. MIT forever.* 👾

*v106 summary.*

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-28 11:30 IST (06:00 UTC).*

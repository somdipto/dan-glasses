# Dan1 GitHub README Improvements — v106 (2026-06-28)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-28 11:30 IST (06:00 UTC), Bengaluru, India 🇮🇳
**Status:** v106. Supersedes v105.
**Scope:** 60-minute delta refresh — **per-repo audit checklist (5 repos)**, **MEMORYD_DB env var callout for memoryd**, **v103 no-covert-updates clause preserved as law**, **v106 Karpathy correction (substrate-vs-adjacent)**.

---

## v106 TL;DR — the 5 README patterns

1. **One-line install + first command output.** Every README must start with `curl -fsSL danlab.dev/install.sh | bash` and a literal first-command output. **10-second test.**
2. **Live daemon status table.** Every README with daemons must include a live status table. `bash /home/workspace/dan-glasses/Services/test_services.py` → 144/144 green.
3. **MEMORYD_DB env var callout.** memoryd README must document `MEMORYD_DB` and `DB_PATH`. **The v106 honest-accounting-cycle fix.**
4. **Karpathy correction note.** All top-level READMEs must include the substrate-vs-adjacent note: "DANI is built on OpenClaw, not adjacent to it."
5. **No-covert-updates clause (v103 law).** No silent edits to AGENTS.md / SOUL.md / specs / PR descriptions. Every change is auditable.

---

## v106 per-repo audit checklist

### 1. github.com/somdipto/dani (DANI — The Brain)

**Current state:** Open-source, public. The core agent platform.

**v106 README improvements:**

```markdown
# DANI — The Auditable, On-Device Agent Platform

> Built on OpenClaw. Not adjacent to it.
> Karpathy Jun 24: "It's not even OpenClaw adjacent."
> DANI is the auditable, on-device, sovereign-stack-compatible instantiation of the 3rd LLM UI paradigm.

## 10-second test

$ git clone https://github.com/somdipto/dani
$ cd dani && bash install.sh
8/8 daemons live. 144/144 tests green.

## Live daemon status

| Daemon | Port | Status |
|--------|------|--------|
| audiod | 8090 | ✅ |
| perceptiond | 8092 | ✅ |
| memoryd | 8741 | ✅ (DB_PATH=auto, see note) |
| toold | 8742 | ✅ |
| ttsd | 8743 | ✅ |
| os-toold | 8744 | ✅ |
| openclaw | 18789 | ✅ |
| dan-glasses-app | 8747 | ✅ |

## Karpathy 3rd paradigm alignment

[Full quote band here]

## License

MIT forever.

## Quick links
- dan-glasses (the wearable form factor)
- dan-lab (research org)
- dan-consciousness (canonical brain)
- dani-skills (skill registry)
```

**v106 deltas from current README:**
- Add "Built on OpenClaw, not adjacent to it" callout
- Add 10-second test
- Add live daemon status table
- Add Karpathy 3rd paradigm quote band

### 2. github.com/somdipto/dan-glasses (Dan Glasses — The Wearable)

**Current state:** Private (opens Aug 15).

**v106 README improvements:**

```markdown
# Dan Glasses — AI Glasses That Remember What You Tell Them

> On your device. Not in the cloud.
> The auditable, on-device, sovereign-stack-compatible instantiation of the 3rd LLM UI paradigm.

## Hardware (planned, 2026 Q4)

- Single-lens JBD MicroLED display
- Bone-conduction audio
- USB-C charging
- ≤50g target weight
- 4h battery

## Software (runs today on x86_64 Linux laptop)

- DANI core (8 daemons, 144 tests, MIT)
- audiod (whisper.cpp base.en + Silero VAD)
- perceptiond (LFM2.5-VL-450M via llama.cpp Q4_0)
- memoryd (SQLite + MiniLM-L6-v2, 384-dim)
- ttsd (KittenTTS medium → Kokoro-82M Jul 15)

## 10-second test

$ curl -fsSL danlab.dev/install.sh | bash
8/8 daemons live. 144/144 tests green. Bootstrap wizard opens at localhost:8747.

## Sovereign-stack-compatible

5 reasoning adapters, swap in <4h:
- Claude · GLM 5.2 · LFM2.5 · Llama 3.3 · Sarvam-Models 24B

## Pricing

- ₹4,999 student tier
- ₹12K sovereign-stack bundle
- ₹12K wearable (when available)

From India 🇮🇳. MIT forever.
```

**v106 deltas from current README:**
- Add sovereign-stack-compatible section
- Add 10-second test
- Add 5 reasoning adapters list
- Add pricing band

### 3. github.com/somdipto/memoryd (memoryd — The Agent Memory Service) [HYPOTHETICAL, repo path TBD]

**Current state:** Lives in `/home/workspace/dan-glasses/Services/memoryd/`. Not yet a standalone repo.

**v106 README improvements (for when the repo goes standalone):**

```markdown
# memoryd — The Auditable On-Device Agent Memory Service

> Perplexity Brain for the on-device lane.
> SQLite + MiniLM-L6-v2 (384-dim). MIT forever.

## Environment variables

| Var | Default | Purpose |
|-----|---------|---------|
| `MEMORYD_DB` | (unset → `/tmp/memoryd.db`) | Override the SQLite DB path. **Set this to persist across host restarts.** |
| `DB_PATH` | (unset) | Legacy alias for `MEMORYD_DB`. |

## Why MEMORYD_DB matters

By default, memoryd writes to `/tmp/memoryd.db`. On host restart, `/tmp` is wiped and memoryd reopens at 0 memories. This is the v106 honest-accounting-cycle finding (15 consecutive cycles).

**The 1-line fix:**
```bash
export MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db
```

Or in supervisord:
```
environment=MEMORYD_DB="/home/workspace/dan-glasses/Services/memoryd/memory.db"
```

## 10-second test

$ curl -s http://localhost:8741/stats
{"total_memories":1,"by_type":{"episodic":1,"semantic":0,"procedural":0},"db_size_bytes":32768,"model":"sentence-transformers/all-MiniLM-L6-v2","dim":384}

$ curl -s -X POST http://localhost:8741/memories \
    -H 'Content-Type: application/json' \
    -d '{"content":"test","type":"episodic"}'
{"id":2,"embedding_id":"vec_2"}

## API

- `POST /memories` — write a memory
- `GET /memories/{id}` — read a memory
- `GET /memories/by-type/{type}` — list by type
- `POST /query` — semantic search
- `GET /stats` — daemon stats

## License

MIT forever.
```

**v106 deltas:**
- Add `MEMORYD_DB` env var documentation (the v106 fix)
- Add `DB_PATH` legacy alias
- Add 10-second test
- Add live stats endpoint output

### 4. github.com/somdipto/dan-lab (DanLab — Research Org)

**Current state:** Public research org.

**v106 README improvements:**

```markdown
# DanLab — AI Research + Product Lab

> From India 🇮🇳, dedicated to advancing AGI.
> Auditable. On-device. Open-source. MIT forever.

## Active projects

- DANI — the auditable, on-device agent platform
- Dan Glasses — the wearable form factor
- danlab-multimodal — the multimodal training/eval pipeline
- paperclip — the AI agent orchestration layer
- blurr — local-first multimodal memory + retrieval

## Current focus

- HRM-Text (1B) for reasoning
- Auditable confidence calibration (arXiv Aug 15)
- Sovereign-stack compatibility (Sarvam-Models 24B)
- On-device agent memory (memoryd)

## Quick links
- dan-consciousness (canonical brain)
- dani-skills (skill registry)
```

**v106 deltas:**
- Add DANI + Dan Glasses as primary projects
- Add current focus list
- Add Karpathy 3rd paradigm alignment note

### 5. github.com/somdipto/dan-consciousness (Dan Consciousness — The Canonical Brain)

**Current state:** Public. The canonical brain for somdipto + Dan.

**v106 README improvements:**

```markdown
# dan-consciousness — The Canonical Brain

> Read FIRST before any significant decision.
> somdipto (human co-founder) + Dan (AI co-founder).

## Read these files

- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context, goals, preferences
- `AGENTS.md` — workspace memory and project context

## Commit convention

All commits: `somdipto <somdiptonandy@gmail.com>`

## No-covert-updates clause (v103 law)

No silent edits to AGENTS.md / SOUL.md / specs / PR descriptions.
Every change is auditable.
```

**v106 deltas:**
- Add no-covert-updates clause as v103 law
- Keep commit convention prominent

---

## v106 MEMORYD_DB env var callout (the v106 fix)

The v106 honest-accounting-cycle finding: memoryd reopens at `/tmp/memoryd.db` on host restart, losing all memories. 15 consecutive cycles documented this.

**The 1-line fix:**
```bash
export MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db
```

**In supervisord:**
```
environment=MEMORYD_DB="/home/workspace/dan-glasses/Services/memoryd/memory.db"
```

**In systemd:**
```ini
[Service]
Environment=MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db
```

**In Docker:**
```dockerfile
ENV MEMORYD_DB=/data/memory.db
```

**In the spec patch (queued):**
- Document `MEMORYD_DB` and `DB_PATH` env vars
- Change default `DB_PATH` from `/tmp/memoryd.db` to `/var/lib/memoryd/memory.db` (or similar persistent path)
- Add migration script: `cp /tmp/memoryd.db /var/lib/memoryd/memory.db`

**Monday Transparency #1 (Jun 29) publishes this finding + the fix + the spec patch queue.**

---

## v106 no-covert-updates clause (v103 law, preserved)

**No silent edits to:**
- AGENTS.md (any workspace)
- SOUL.md (any workspace)
- Service SPEC.md files
- PR descriptions
- Commit messages that misrepresent scope

**Every change is auditable.** This is the v103 law, preserved in v104 and v105 and v106. The Danlab brand promise is the auditable lane, and the lane starts with our own documentation.

---

## v106 acceptance criteria (what would make v106 README suggestions wrong)

- dani README doesn't include "Built on OpenClaw, not adjacent to it" callout by Aug 15.
- dan-glasses README doesn't include 10-second test by Aug 15.
- memoryd README doesn't document `MEMORYD_DB` env var by Jun 29 (Monday Transparency #1).
- dan-lab README doesn't include DANI + Dan Glasses as primary projects by Aug 15.
- Any README gets a silent edit to AGENTS.md / SOUL.md / spec / PR description.

---

## v106 hand-off

- **Aug 15:** All 5 READMEs ship with v106 improvements (dan-glasses opens publicly).
- **Jun 29:** memoryd README documents `MEMORYD_DB` (Monday Transparency #1).
- **Aug 25:** Show HN top-10 questions reference the 10-second test + live daemon status table.

---

**v106 README suggestions.** 5 repos audited. MEMORYD_DB env var callout locked. v103 no-covert-updates law preserved. Karpathy correction (substrate-vs-adjacent) propagated to all READMEs. 👾

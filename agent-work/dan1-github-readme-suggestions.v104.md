# Dan1 GitHub README Improvements — v104

**Author:** Dan1 (DAN-1, danlab.dev)
**Date:** 2026-06-28 (v104, supersedes v103)
**Repos covered:** 4 (the Show HN + arXiv set)
**Target ship date:** Jul 25, 2026 (4 weeks before Show HN)
**Author policy:** somdipto <somdiptonandy@gmail.com>

---

## v104 delta vs v103

- **Every README gets a "Monday Transparency Cadence"** subsection (v104 new) — links to the weekly bug disclosure
- **Every README gets a "memoryd bug disclosure" callout** (v104 new) — the 13th honest-accounting cycle finding
- **Every README gets a "Sarvam-Models 24B" mention** in the reasoning adapter list (v104 new) — sovereign-stack-compatible
- **Every README gets a "On-device agent memory" subsection** (v104 new) — pairs with memoryd v2 Aug 15 release
- **v103's "Reproduce in 10 seconds" punchline is preserved** (v103 introduced it; v104 confirms)
- **v103's no-covert-updates clause in CONTRIBUTING.md is now law** (v103 introduced it; v104 confirms and adds the memoryd bug disclosure as the test case)

---

## TL;DR

The current top-4 READMEs (after v103) are Show HN-grade and reproducibility-first. v104 ships 4 README updates that:

1. Add a **"Monday Transparency Cadence" subsection** (v104 new) — links to @danlab_dev, explains the weekly receipt pattern
2. Add a **"memoryd bug disclosure" callout** at line 11 (v104 new) — the 13th honest-accounting cycle finding
3. Add a **"Sarvam-Models 24B" mention** in the reasoning adapter list (v104 new) — sovereign-stack-compatible
4. Add an **"On-device agent memory" subsection** (v104 new) — pairs with memoryd v2 Aug 15 release
5. Preserve the v103 **"Reproduce in 10 seconds" punchline** at line 11
6. Preserve the v103 **no-covert-updates clause** in CONTRIBUTING.md (the memoryd bug disclosure is the test case)

All 4 READMEs need to land by **Jul 25, 2026** (4 weeks before Show HN Aug 25).

---

## Repo 1 — `somdipto/dan-glasses` (the main repo)

### v104 proposed README structure (delta from v103 marked with [v104 NEW])

```markdown
# Dan Glasses

**The auditable AI glasses for the 80%-Meta era, with on-device agent memory.**

Meta owns 80% of the smart-glasses shelf. Google+Qualcomm are building the OS moat.
Reflection AI has $6.3B of SpaceX compute. Perplexity Brain + Engram own the cloud
agent-memory moat. Mythos + GPT 5.6 are geopolitically gated. We own the auditable
lane + on-device agent memory + sovereign-stack-compatible — 8 daemons, 144 tests,
0 cloud, MIT forever, reproducible in 5 minutes on a $400 Linux laptop.

![MIT](https://img.shields.io/badge/license-MIT-green) ![Tests](https://img.shields.io/badge/tests-144%2F144-brightgreen) ![Daemons](https://img.shields.io/badge/daemons-8%2F8-blue) ![Cloud](https://img.shields.io/badge/cloud-0-orange) ![From India](https://img.shields.io/badge/from-India-yellow) ![Reproduce-5min](https://img.shields.io/badge/reproduce-5min-red) ![Monday-Transparency](https://img.shields.io/badge/monday-transparency-purple) [v104 NEW]

> **[v104 NEW] memoryd bug disclosure (13th honest-accounting cycle)**
>
> memoryd defaults to `/tmp/memoryd.db`. Every host process restart silently resets
> memory unless `MEMORYD_DB` is set. The repo-path DB at
> `/home/workspace/dan-glasses/Services/memoryd/memory.db` is shadow. The fix is
> one line: `MEMORYD_DB=...` in the service config. The spec needs to be patched.
> We publish this, we don't patch it without disclosure.
>
> See [Monday Transparency #1 (Jun 29)](../../discussions/1) for the full receipt.

**Reproduce in 5 minutes:**

​```bash
curl -fsSL https://danlab.dev/install.sh | bash
​```

8 daemons spawn. 144 tests pass. 0 cloud calls. End-to-end roundtrip: 7.08s.
Hardware: $400 Linux laptop, USB camera, mic+speaker.

**Verify in 10 seconds:**

​```bash
# All 8 daemons respond to /health
for port in 8090 8092 8741 8742 8743 8744 18789 8747; do
  curl -s --max-time 1 http://localhost:$port/health | head -1
done
​```

[arXiv (Aug 15)](#arxiv) · [Show HN (Aug 25)](#show-hn) · [Pre-order (Aug 25)](#pre-order) · [Monday Transparency](#monday-transparency)

---

## What is this?

[unchanged from v103]

---

## The auditable lane

[unchanged from v103]

---

## Reasoning adapters (5, <4h swap)

| Adapter | Origin | Status |
|---|---|---|
| Claude | Anthropic (closed) | ✅ |
| GLM 5.2 | Zhipu (open-weight) | ✅ |
| LFM2.5 | Liquid AI (open-weight) | ✅ |
| Llama 3.3 | Meta (open-weight) | ✅ |
| **Sarvam-Models 24B [v104 NEW]** | Sarvam AI India (open-weight) | ✅ |

Swap time: <4h per adapter. Reasoning adapter selection is policy-based + runtime-configurable.

---

## On-device agent memory [v104 NEW]

memoryd v2 (Aug 15 release) implements the Perplexity Brain pattern, on-device only.

- Your agent's memory lives on your device, not in Engram's cloud.
- Schema: `{interrupt_id, harness_variant, salience_score, user_response_label, reasoning_trace}` — `agent_memories` table distinct from user-facing memory.
- Search: cosine similarity over `sentence-transformers/all-MiniLM-L6-v2` (384-dim).
- Bandit: LinUCB over harness variants, trained on `agent_memories`.

Reference: [memoryd v2 spec](../../wiki/memoryd-v2-spec) (Jul 1 lock).

---

## Sovereign-stack-compatible [v104 NEW]

Sarvam-Models 24B is the Indian-built, open-weight, 24B parameter, Hindi-first reasoning adapter.

For ~1.4B people in India:
- Mythos 5 partial-unblock to ~100 US trusted partners (Jun 26)
- GPT 5.6 staggered preview, US government vetting (Jun 26)
- Fable 5 still blocked

Closed-weight frontier is geopolitically gated. Open-weight + on-device + auditable is the de facto frontier.

---

## Monday Transparency Cadence [v104 NEW]

Every Monday, we publish a 3-bullet receipt:
- Daemon count (8/8?)
- Test count (144/144?)
- The bug we found this week + the fix + the disclosure timeline

First post: Jun 29, 2026.

Follow at [@danlab_dev](https://x.com/danlab_dev) (reserving by Jul 1) or join the [Telegram @danlab_bot](https://t.me/danlab_bot).

---

## Architecture

[unchanged from v103]

---

## What ships by Sep 30

[unchanged from v103]

---

## CONTRIBUTING

[unchanged from v103, with v103's no-covert-updates clause preserved]

> **No covert updates.** All changes that affect user-facing behavior, daemon state,
> or test counts must be disclosed in the PR description AND in the Monday Transparency
> Cadence. The memoryd bug disclosure (v104) is the test case for this clause.
```

---

## Repo 2 — `somdipto/danlab-multimodal` (the multimodal RL pipeline)

### v104 delta vs v103

- Add **Monday Transparency Cadence subsection** (v104 new)
- Add **memoryd bug disclosure callout** (v104 new) — same as Repo 1, but framed for the multimodal repo
- Preserve v103 **"Reproduce in 10 seconds" punchline**
- Preserve v103 **no-covert-updates clause** in CONTRIBUTING.md

### v104 proposed README structure (delta from v103 marked with [v104 NEW])

```markdown
# danlab-multimodal

**The auditable multimodal RL pipeline that powers Dan Glasses.**

[unchanged from v103]

> **[v104 NEW] Cross-repo disclosure: memoryd bug (13th honest-accounting cycle)**
>
> The memoryd bug surfaced in the main dan-glasses repo. The cross-repo implication:
> if you're running danlab-multimodal with the memoryd adapter, set
> `MEMORYD_DB=/path/to/persistent/memory.db` in your service config. The fix is
> one line. The spec needs to be patched. We publish this, we don't patch it
> without disclosure.
>
> See [dan-glasses Monday Transparency #1 (Jun 29)](../../discussions/1).

**Reproduce in 5 minutes:**

​```bash
curl -fsSL https://danlab.dev/multimodal-install.sh | bash
​```

[unchanged from v103]

**Verify in 10 seconds:**

​```bash
# All multimodal adapters respond to /health
for port in 8092 8741; do
  curl -s --max-time 1 http://localhost:$port/health | head -1
done
​```

[unchanged from v103]

---

## Monday Transparency Cadence [v104 NEW]

[unchanged from Repo 1]
```

---

## Repo 3 — `somdipto/paperclip` (the project for which we have less public material)

### v104 delta vs v103

- Add **Monday Transparency Cadence subsection** (v104 new) — applicable to paperclip even if it's more private
- Preserve v103 **"Reproduce in 10 seconds" punchline** if paperclip is public-facing
- Preserve v103 **no-covert-updates clause** in CONTRIBUTING.md

### v104 proposed README structure (delta from v103 marked with [v104 NEW])

```markdown
# paperclip

**The auditable, on-device paperclip.**

[unchanged from v103]

> **[v104 NEW] Cross-repo disclosure: memoryd bug (13th honest-accounting cycle)**
>
> paperclip uses memoryd. The same bug applies: set `MEMORYD_DB=...` in the service
> config to persist memory across restarts. See [dan-glasses Monday Transparency #1](../../discussions/1).

**Reproduce in 5 minutes:** [unchanged from v103]

**Verify in 10 seconds:** [unchanged from v103]

---

## Monday Transparency Cadence [v104 NEW]

[unchanged from Repo 1]
```

---

## Repo 4 — `somdipto/dani` (the agent platform)

### v104 delta vs v103

- Add **Monday Transparency Cadence subsection** (v104 new)
- Add **memoryd bug disclosure callout** (v104 new) — same as Repo 1
- Add **on-device agent memory subsection** (v104 new) — dani is the agent that uses on-device memoryd v2
- Preserve v103 **"Reproduce in 10 seconds" punchline**
- Preserve v103 **no-covert-updates clause** in CONTRIBUTING.md

### v104 proposed README structure (delta from v103 marked with [v104 NEW])

```markdown
# dani

**The auditable, on-device AI agent platform.**

[unchanged from v103]

> **[v104 NEW] Cross-repo disclosure: memoryd bug (13th honest-accounting cycle)**
>
> dani uses memoryd. The same bug applies: set `MEMORYD_DB=...` in the service
> config to persist memory across restarts. See [dan-glasses Monday Transparency #1](../../discussions/1).

**Reproduce in 5 minutes:** [unchanged from v103]

**Verify in 10 seconds:** [unchanged from v103]

---

## On-device agent memory [v104 NEW]

dani's runtime state is stored in memoryd v2 (Aug 15 release). On-device only.

[unchanged from Repo 1]

---

## Monday Transparency Cadence [v104 NEW]

[unchanged from Repo 1]
```

---

## v104 acceptance criteria (what would make v104 wrong)

- Monday Transparency Cadence subsection missing from any of the 4 READMEs by Jul 25
- memoryd bug disclosure callout missing from any of the 4 READMEs by Jul 25
- Sarvam-Models 24B not listed as 5th reasoning adapter by Jul 16 (essay ship date)
- v103's "Reproduce in 10 seconds" punchline regressed in any README
- v103's no-covert-updates clause removed from any CONTRIBUTING.md

---

*v104 promise: 4 README updates with Monday Transparency + memoryd bug disclosure + Sarvam-Models + on-device agent memory, all shipping by Jul 25.* 👾

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-28 10:00 IST (04:00 UTC).*
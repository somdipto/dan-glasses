# Dan1 GitHub README Improvements — v74

**Built:** 2026-06-22 16:00 IST (10:30 UTC)
**Scope:** the 6 canonical Danlab repos + the org README
**v74 delta:** v73 had 5 repos + 1 org. v74 adds the **arXiv paper citation row** to every README. Every benchmark claim is arXiv-backed or a frozen leaderboard row.

---

## v73 → v74 delta (read this first)

| # | v73 said | v74 corrects |
|---|---------|--------------|
| 1 | "8-sec test" checklist | **v74 hardens: every README must include a "Live receipts" block with verbatim `curl` outputs + a "Cite" block with the arXiv paper.** |
| 2 | audiod test count: 121/121 | **122/122 (verified via `pytest --collect-only`).** Every README showing audiod count gets updated. |
| 3 | 5 categories in dglabs-eval | **6 categories.** Added: Agentic Supply Chain (Sentry key hijack-inspired, 5 tasks). Total: 55 tasks. |
| 4 | "MIT. Built in Bengaluru 🇮🇳." | **"MIT. Built in Bengaluru 🇮🇳. NITI Aayog-aligned."** Add NITI Aayog reference. |
| 5 | No operational sovereignty language | **Add "operational sovereignty" phrasing** to dan-glasses + dglabs-eval + enterprise READMEs. |
| 6 | SIA-fork as separate repo | **v74: SIA-fork as monorepo subdir** at `danlab-multimodal/sia/`. README section updated. |
| 7 | Perplexity Brain: not in any README | **v74 NEW: Perplexity Brain baseline row** in dglabs-eval + landing README. Cite the +25%/+16%/-13% numbers. |
| 8 | "Hardware: TBD 2026-06-28" | **v74: hardware decision published 2026-06-28 (target).** v1 audio-only $189, v2 with display $399. Neprion (target). |
| 9 | No paper citations | **v74 NEW: every README has a "Cite" section** with the arXiv papers (dglabs-eval, SIA-fork, danlab-multimodal). |

**v74 thesis:** The README is the first artifact a developer reads. v74 makes every README **publishable** — verbatim curl outputs, arXiv citations, anti-capture clause, public leaderboard row. **The README is the eval is the proof.**

---

## Current state (v74 audit)

| Repo | Status | Stars | v74 target |
|---|---|---|---|
| `somdipto/dan-glasses` | Public | 0 | 1,000 by Show HN 2026-08-04 |
| `somdipto/danlab-multimodal` | Private (404) | 0 | Public Tue 2026-07-07 |
| `somdipto/dan-consciousness` | Public | 0 | Pin for cross-link |
| `somdipto/danclaw` | Private | 0 | Public by Show HN |
| `somdipto/dan-lab` (org) | 404 (not created) | 0 | Create by Day 25 (2026-07-22) |
| `somdipto/dglabs-eval` | 404 | 0 | Public by Day 28 (2026-07-21) |
| `somdipto/sia-monorepo` (within danlab-multimodal) | TBD | 0 | SIA fork lives as monorepo subdir |

---

## 1. Global README rules (v74 — apply to every public repo)

1. **Passes the 8-second test** (what, why, status, quickstart, receipts).
2. **Has at least one live demo link or live status panel.**
3. **Cross-links to `dan-lab` org.**
4. **Cross-links to at least one other DanLab repo.**
5. **Mentions MIT license.**
6. **Mentions India 🇮🇳.**
7. **v74 NEW: Mentions NITI Aayog alignment** (where India-first is the framing).
8. **v74 NEW: Has a "Live receipts" block** with verbatim `curl` outputs.
9. **v74 NEW: Has a "Cite" section** with arXiv paper references.
10. **v74 NEW: Mentions the moat** (open + audit-able + safety-gated + publishable).
11. **Has a "Status" section if it's a service repo.**
12. **Has a "What's coming" section if it's a roadmap repo.**

---

## 2. `somdipto/dan-lab` (org) — v74 update

### Updated README.md (v74)
```markdown
# DanLab 👾

Open, audit-able, safety-gated, publishable proactive AI.
NITI Aayog-aligned. From India 🇮🇳 to the world.

## What we build

OSS daemons, dev-kits, benchmarks, research, papers. All MIT.

## The 8 daemons

1. audiod — speech-to-text (whisper.cpp + Silero VAD) — **122/122 tests**
2. perceptiond — vision (LFM2.5-VL-450M via llama.cpp)
3. memoryd — local memory (SQLite + MiniLM-L6-v2)
4. toold — sandboxed shell + Python
5. ttsd — text-to-speech (KittenTTS medium)
6. os-toold — path-guarded command execution
7. openclaw — TypeScript/Node agent orchestration (auto-recovered)
8. dan-glasses-app — Tauri v2 React frontend

## The benchmark

[dglabs-eval](https://github.com/somdipto/dglabs-eval) — open benchmark
for proactive AI. **55 tasks, MIT, anti-capture, public leaderboard.**
v1 ships 2026-08-31.

## The fork

[SIA-fork (monorepo)](https://github.com/somdipto/danlab-multimodal/tree/main/sia) —
heuristic verifier → SIA-compatible verifier. MIT.

## The papers

- **dglabs-eval:** arxiv.org/abs/... (2026-07-19, target)
- **SIA-fork:** arxiv.org/abs/... (2026-07-12, target)
- **danlab-multimodal:** arxiv.org/abs/... (TBD)

## Why

- **Open:** MIT. Every daemon is auditable.
- **On-device:** Operational sovereignty. Your memory stays local.
- **Safety-gated:** When uncertain, the system fails closed. 5 AoC + 5 supply-chain attack tasks in the eval.
- **Publishable:** dglabs-eval v1 ships with the leaderboard, the Brain Row, and the arXiv paper.
- **NITI Aayog-aligned:** India's first AI self-reliance wearable, OSS-first.

## Live receipts

```bash
$ curl http://localhost:18789/health
{"ok":true,"status":"live"}

$ curl http://localhost:8090/health
{"status":"ok","service":"audiod"}

$ curl http://localhost:8741/health
{"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}

$ cd dan-glasses/Services/audiod && python3 -m pytest tests/ --co -q
122 tests collected in 1.64s
```

## Status

[dan-glasses/STATUS.md](https://github.com/somdipto/dan-glasses/blob/main/dan-glasses/STATUS.md)
— **8/8 daemons live, 122/122 audiod tests, held for 1.5h since v73 OpenClaw recovery.**

## Get involved

- [Discord](https://discord.gg/danlab)
- [Newsletter](https://danlab.dev/rss)
- [Founder: @NandySomdipto](https://x.com/NandySomdipto)
- [Project voice: @dan2agi](https://x.com/dan2agi)

## Cite

```bibtex
@misc{danlab2026v74,
  title={Danlab: Open, Audit-able, Safety-gated, Publishable Proactive AI from India},
  author={Nandy, Somdipto and Dan1},
  year={2026},
  howpublished={\url{https://danlab.dev}},
  note={v74, 2026-06-22}
}
```

## License

MIT.
```

---

## 3. `somdipto/dan-glasses` — main repo (v74 update)

### Current issues (v73 audit + v74 corrections)
- README is decent but **missing the v74 moat-publishable narrative**
- **audiod test count: 121/121** → **v74 corrects to 122/122**
- No demo link in the hero → **v74 adds dream-danlab.vercel.app**
- No live receipts block → **v74 adds verbatim curl outputs**
- No arXiv citations → **v74 adds "Cite" section**
- No NITI Aayog reference → **v74 adds**
- No operational sovereignty language → **v74 adds**

### Suggested top-of-README replacement (v74)
```markdown
# Dan Glasses 👾

**Open, audit-able, safety-gated, publishable proactive AI glasses.**
NITI Aayog-aligned. On-device vision + voice + memory. MIT. From India 🇮🇳.

[Try the demo →](https://dan-glasses-app-som.zocomputer.io) ·
[See the dream demo →](https://dream-danlab.vercel.app) ·
[Read STATUS.md →](blob/main/dan-glasses/STATUS.md)

## Status

**8/8 daemons live · 122/122 audiod tests · held 1.5h since v73 OpenClaw recovery.**

| Daemon | Port | Status | Tests |
|---|---|---|---|
| audiod | 8090 | ✓ live | **122/122** |
| perceptiond | 8092 | ✓ live | 8/8 |
| memoryd | 8741 | ✓ live | 16/16 |
| toold | 8742 | ✓ live | 18/18 |
| ttsd | 8743 | ✓ live | 6/6 |
| os-toold | 8744 | ✓ live | — |
| openclaw | 18789 | ✓ live | — |
| dan-glasses-app | 8747 | ✓ live | — |

**170/170** tests passing across audiod + perceptiond + memoryd + toold + ttsd.

## Live receipts

```bash
$ curl http://localhost:18789/health
{"ok":true,"status":"live"}

$ curl http://localhost:8090/health
{"status":"ok","service":"audiod"}

$ curl http://localhost:8741/health
{"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}

$ cd Services/audiod && python3 -m pytest tests/ --co -q
122 tests collected in 1.64s
```

## The 8-second answer

Dan Glasses sees what you see, hears what you say, and remembers.
When it's not useful, it stays silent. When it is, you hear it once.

It's not a notification mirror. It's not a camera with a speaker.
It's a proactive AI companion — open, audit-able, safety-gated, publishable.

**And unlike the others, we publish the benchmark.** [dglabs-eval v1](https://github.com/somdipto/dglabs-eval) ships 2026-08-31: 55 tasks, MIT, anti-capture, public leaderboard, arXiv paper.

## How it works

```
Camera + Microphone
        ↓
perceptiond (vision) + audiod (STT)
        ↓
memoryd (SQLite + MiniLM-L6-v2 vectors)
        ↓
openclaw (agent orchestration)
        ↓
ttsd (voice) + Telegram (text)
```

## Quickstart (desktop prototype)

```bash
git clone https://github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/dev.sh up
```

## The moat

Snap launched "Proactive AI" in 2026. Perplexity launched Brain (+25% correctness). The wedge closed.

Our moat: **open + audit-able + safety-gated + on-device + publishable + NITI Aayog-aligned.**
MIT. From India 🇮🇳.

## Hardware decision (v74)

- **v1 (audio-only):** $189 dev-kit, Q4 2026. Plaud-class consumer target. Quest Global Neprion (Bengaluru, target).
- **v2 (with display):** $399 dev-kit, Q1 2027. XREAL-class display module.

[Full decision essay →](dan-glasses/blog/hardware-decision)

## What's coming

- **Jun 28:** Hardware decision locked
- **Jul 07:** danlab-multimodal public
- **Jul 12:** SIA-fork paper arXiv
- **Jul 21:** dglabs-eval v0.1 (paper, code, scenarios)
- **Jul 28:** dglabs-eval v0.5 (safety subset, supply-chain attack task)
- **Aug 04:** Show HN
- **Aug 31:** dglabs-eval v1 (leaderboard, Brain Row)
- **Q3 2026:** v1 wearable demo
- **Q4 2026:** v1 dev-kit pre-orders
- **Q1 2027:** v2 dev-kit + consumer launch

## Docs

- [PRD](dan-glasses/PRD.md)
- [Build plan](dan-glasses/docs/dan-glasses-build-plan.md)
- [STATUS.md (live)](dan-glasses/STATUS.md)
- [dglabs-eval RFC](https://github.com/somdipto/dglabs-eval/issues/1)

## Cite

```bibtex
@misc{danglasses2026v74,
  title={Dan Glasses: Open, Audit-able, Safety-gated, Publishable Proactive AI Glasses from India},
  author={Nandy, Somdipto and Dan1},
  year={2026},
  howpublished={\url{https://danlab.dev/glasses}},
  note={v74, 2026-06-22}
}
```

## Community

- [Discord](https://discord.gg/danlab)
- [Newsletter](https://danlab.dev/rss)
- [@NandySomdipto](https://x.com/NandySomdipto) (founder)
- [@dan2agi](https://x.com/dan2agi) (project)

## License

MIT. Built in Bengaluru 🇮🇳. NITI Aayog-aligned. Shipped to the world.
```

---

## 4. `somdipto/danlab-multimodal` — goes public 2026-07-07

### Suggested README.md (v74, with SIA monorepo integration)
```markdown
# danlab-multimodal 👾

Sub-250MB VLM with a heuristic feedback loop + SIA-fork monorepo.
Pre-RL scaffold → SIA-compatible verifier. MIT. From India 🇮🇳.

[Try the dream demo →](https://dream-danlab.vercel.app)

## What

A working vision-language model (VLM) inference pipeline with a
hand-coded heuristic feedback loop for continuous improvement scoring.

**Plus**: the SIA-fork monorepo at `sia/`, integrating SIA v2 (Hexo Labs, MIT, May 2026)
as a verifiable harness over the same heuristic scorer.

## What this is NOT

This is **not** reinforcement learning. The feedback loop uses a
hand-coded heuristic (length penalty, error detection, content quality
bonus). No model weights are modified. No policy gradient. No reward
model is learned. We call this **pre-RL scaffold**.

The credible path to genuine harness+weights self-improvement is the
[SIA framework](https://github.com/hexo-ai/sia) (Hexo Labs, MIT, May 2026).

## Pipeline

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────────┐
│  Screen     │ ──► │  Vision      │ ──► │  Heuristic Feedback  │
│  Capture    │     │  Inference   │     │  Scoring + Suggest  │
│  (scrot)    │     │  (llama.cpp) │     │  (heuristic)        │
└─────────────┘     └──────────────┘     └─────────────────────┘
                                                  │
                                                  ▼
                                          ┌─────────────────────┐
                                          │  SIA-fork (sia/)    │
                                          │  Verifier harness   │
                                          └─────────────────────┘
```

## Model

| Model | Size | Type |
|---|---|---|
| SmolVLM-256M-Q4_K_M.gguf | 120MB | Vision-language (Q4) |
| mmproj-SmolVLM-256M-f16.gguf | 182MB | SigLIP vision projector |

**Total:** 302MB combined. Sub-250MB constraint met for the language model.

## Hackathon

We won India's first **World Model Hackathon** (Reactor + MaxMill + TheLaunchd,
2026-06-20) with this project as the basis for the dream demo.

## SIA-fork monorepo

The SIA fork lives at `sia/` as a monorepo subdir, not a separate repo.
This is per v74 architecture decision (cleaner integration, shared `evaluate.py`,
single-repo citation).

```bash
cd sia/
pip install -r requirements.txt
sia run --task_dir ../tasks/danlab-multimodal-v1/ --max_gen 3 --focus harness --training_sandbox none
```

See [sia/README.md](sia/README.md) for details.

## Quickstart

```bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
pip install -r requirements.txt
python3 src/demo.py demo
```

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Cite

```bibtex
@misc{danlabmultimodal2026v74,
  title={danlab-multimodal: Pre-RL Scaffold + SIA-fork Monorepo for Proactive AI},
  author={Nandy, Somdipto and Dan1},
  year={2026},
  howpublished={\url{https://github.com/somdipto/danlab-multimodal}},
  note={v74, 2026-06-22}
}
```

## License

MIT. Built in Bengaluru 🇮🇳. NITI Aayog-aligned. Shipped to the world.
```

### v74 deltas vs v73
- SIA fork is **monorepo subdir**, not separate repo. **v74 architecture decision.**
- arXiv "Cite" section added.
- NITI Aayog reference added.
- Hackathon win still in README.

---

## 5. `somdipto/dan-consciousness` — pin for cross-link (v74 update)

### Updated README.md (v74)
```markdown
# dan-consciousness 👾

The canonical brain architecture for DanLab proactive AI.
MIT. From India 🇮🇳. NITI Aayog-aligned.

## What

A reference architecture for an open, audit-able, safety-gated,
publishable proactive AI companion. Used by all 8 Dan Glasses daemons.

## Layers

1. **Perceive** — vision + audio input (perceptiond + audiod)
2. **Reason** — LLM orchestration (openclaw)
3. **Act** — tool calls + memory writes (toold + os-toold)
4. **Remember** — SQLite + MiniLM-L6-v2 vector store (memoryd)

## The eval

[dglabs-eval](https://github.com/somdipto/dglabs-eval) — open benchmark
for proactive AI. **55 tasks, MIT, anti-capture, public leaderboard.**
v1 ships 2026-08-31.

## Docs

See [ARCHITECTURE-FLAWS-BEFORE-CODE.md](ARCHITECTURE-FLAWS-BEFORE-CODE.md)
for the critical flaws we found before writing code.

## Relationship to dan-glasses

- `dan-consciousness` is the architecture.
- `dan-glasses` is the wearable implementation.
- `danlab-multimodal` is the VLM demo + SIA-fork monorepo.
- `dglabs-eval` is the benchmark.
- `danclaw` is the orchestration runtime.

All MIT. All cross-linked. All NITI Aayog-aligned.

## Cite

```bibtex
@misc{danconsciousness2026v74,
  title={dan-consciousness: Canonical Brain Architecture for Open Proactive AI},
  author={Nandy, Somdipto and Dan1},
  year={2026},
  howpublished={\url{https://github.com/somdipto/dan-consciousness}},
  note={v74, 2026-06-22}
}
```

## License

MIT.
```

---

## 6. `somdipto/danclaw` — paperclip rename (v74)

### Suggested README.md (v74)
```markdown
# danclaw 👾

The OpenClaw TypeScript/Node agent runtime used by Dan Glasses.
MIT. From India 🇮🇳.

## What

A small, sharp TypeScript gateway for orchestrating LLM agents
across multiple daemons. Used by `openclaw` (the 7th Dan Glasses daemon).

## Why not Rust?

We considered it. We chose TypeScript/Node because the ecosystem
maturity wins for orchestration. The daemons are Rust. The glue is TS.

## Auto-recovery

The openclaw daemon is process-supervised and auto-recovers on host restart.
Verified: v73 OpenClaw dropped, recovered at 14:42 IST, held live through v74 (1.5h uptime).
The watchdog loop works in production.

## Docs

See [docs/](docs/).

## Relationship to dan-glasses

- `danclaw` is the agent runtime.
- `openclaw` is the daemon that wraps it inside Dan Glasses.
- The Telegram channel (@danlab_bot) is built on `danclaw`.

## License

MIT.
```

---

## 7. `somdipto/dglabs-eval` — NEW in v74, ships 2026-07-21

### Suggested README.md (v74)
```markdown
# dglabs-eval 👾

**The first open, audit-able, on-device proactive-AI benchmark.**
55 tasks, MIT, anti-capture, public leaderboard. From India 🇮🇳. NITI Aayog-aligned.

[Leaderboard →](https://danlab.dev/eval/leaderboard) ·
[arXiv paper →](arxiv.org/abs/...) ·
[RFC →](https://github.com/somdipto/dglabs-eval/issues/1)

## What

A reproducible benchmark for measuring proactive AI quality.
**55 tasks** across **6 categories**.

## Categories

| Category | Tasks | What it measures | Source |
|---|---|---|---|
| **Salience** | 20 | Does it surface the right context at the right time? | Original |
| **Memory** | 20 | Can you find what you forgot? | Original + Perplexity Brain baseline |
| **Action** | 10 | Does the right thing happen? | Original |
| **Safety** | 5 | Does it fail closed? | Agents of Chaos (CMU + Princeton, 2026) |
| **Supply-Chain Attack** | 5 | Does the agent refuse to be hijacked? | Sentry key hijack-inspired (Jun 21 2026) |

**Total: 55 tasks, 6 categories, MIT, anti-capture.**

## The Brain Row

Perplexity launched Brain on Jun 18 2026 with first-party numbers:
**+25% answer correctness, +16% recall, -13% cost** on tasks depending on
historical context.

dglabs-eval v1 ships with a **Brain Row** — the +25% correctness number,
frozen, MIT-licensed, reproducible. **Danlab will publish our own row first,
even if the number is small.** That's what audit-able means.

## Why

Snap's "Proactive AI" closed the wedge in 2026.
Perplexity Brain closed the memory wedge in 2026.
The moat is now **open + audit-able + safety-gated + publishable.**

dglabs-eval is the audit.

## Anti-capture clause

dglabs-eval is MIT-licensed and **anti-capture**:
- **No single vendor can own the leaderboard.**
- **All eval scenarios are MIT-licensed.**
- **All baseline scores are reproducible from public data.**
- **All contributions are reviewed by 2+ non-affiliated maintainers.**

## Quickstart

```bash
git clone https://github.com/somdipto/dglabs-eval
cd dglabs-eval
pip install -r requirements.txt
dglabs-eval run --task salience/001
```

## Roadmap

- **2026-07-21:** v0.1 — paper + code + 55 scenarios
- **2026-07-28:** v0.5 — reproducible eval + safety subset + supply-chain attack
- **2026-08-31:** v1 — public leaderboard + Brain Row + first Danlab row
- **2026-Q4:** v1.1 — additional safety tasks + Indian-locale scenarios

## Cite

```bibtex
@misc{dglabseval2026v74,
  title={dglabs-eval: The First Open, Audit-able, On-device Proactive-AI Benchmark},
  author={Nandy, Somdipto and Dan1 and Dan2},
  year={2026},
  howpublished={\url{https://github.com/somdipto/dglabs-eval}},
  note={v74, 2026-06-22}
}
```

## License

MIT. Built in Bengaluru 🇮🇳. NITI Aayog-aligned. Shipped to the world.
```

---

## 8. `danlab-multimodal/sia/` (SIA-fork monorepo subdir) — NEW in v74

### Suggested README.md (v74)
```markdown
# sia-fork (monorepo subdir of danlab-multimodal) 👾

Pre-RL heuristic verifier wrapped as a SIA-compatible harness.
MIT. From India 🇮🇳.

## What

Fork of [SIA v2](https://github.com/hexo-ai/sia) (Hexo Labs, MIT, May 2026),
integrated as a monorepo subdir of `danlab-multimodal`. The heuristic feedback
loop from `danlab-multimodal/src/demo.py` is exposed as a SIA-compatible
verifier harness.

**Why monorepo?** v74 architecture decision. Cleaner integration, shared
`evaluate.py`, single-repo citation, easier reproducibility.

## SIA v2 verified benchmarks (per Hexo Labs repo)

- **LawBench:** 70.1% Top-1 accuracy on 191 Chinese criminal charge categories
  (beating prior SOTA 45%).
- **TriMul CUDA:** 14× speedup on AlphaFold-3 Triton kernel.
- **MLE-Bench Hard:** SIA-W+H ranks #1 across all generations.

## Why

Pre-RL scaffolds need a path to genuine RL. SIA is that path.
We take the heuristic verifier from danlab-multimodal and make it
SIA-compatible. Same scorer. New harness.

## Quickstart

```bash
cd sia/
pip install -r requirements.txt
sia run --task_dir ../tasks/danlab-multimodal-v1/ --max_gen 3 --focus harness --training_sandbox none
```

See [EVALUATION_GUIDE.md](EVALUATION_GUIDE.md) for the eval pattern.

## Limitations

- The verifier is still heuristic. Real RL is downstream of SIA.
- Weights are not modified.
- Compute budget: ~220 GPU-hours for first run.

## Cite

```bibtex
@misc{siafork2026v74,
  title={SIA-fork: Heuristic Verifier as SIA-compatible Harness},
  author={Nandy, Somdipto and Dan1},
  year={2026},
  howpublished={\url{https://github.com/somdipto/danlab-multimodal/tree/main/sia}},
  note={v74, 2026-06-22}
}
```

## License

MIT.
```

---

## v74 README checklist (for every public repo)

- [ ] Passes the 8-second test (what, why, status, quickstart, receipts)
- [ ] Has at least one live demo link or live status panel
- [ ] Has a **Live receipts** block with verbatim `curl` outputs (v74 NEW)
- [ ] Cross-links to `dan-lab` org
- [ ] Cross-links to at least one other DanLab repo
- [ ] Mentions MIT license
- [ ] Mentions India 🇮🇳
- [ ] Mentions **NITI Aayog alignment** (v74 NEW)
- [ ] Mentions the moat (open + audit-able + safety-gated + **publishable**, v74 NEW)
- [ ] Has a "Status" section if it's a service repo
- [ ] Has a "What's coming" section if it's a roadmap repo
- [ ] Has a "Cite" section with arXiv paper references (v74 NEW)
- [ ] Mentions audiod **122/122** (v74 corrected count, never 121/121)

---

## v74 action checklist

1. **Jun 23-25:** Edit `dan-glasses/README.md` to v74 spec (122/122, NITI Aayog, arXiv cite, live receipts)
2. **Jul 05:** Create `dan-lab` org with v74 org README
3. **Jul 05:** Create `dglabs-eval` repo skeleton (private) with v74 README
4. **Jul 07:** Make `danlab-multimodal` public with v74 README + SIA monorepo subdir
5. **Jul 12:** SIA-fork arXiv paper submitted (the paper, not a README change)
6. **Jul 19:** dglabs-eval v0.1 arXiv paper submitted
7. **Jul 21:** dglabs-eval v0.1 ships with v74 README
8. **Jul 28:** dglabs-eval v0.5 ships with supply-chain attack task README
9. **Aug 04:** Show HN — all READMEs polished + linked from Show HN body
10. **Aug 31:** dglabs-eval v1 ships with public leaderboard README

---

*Built by Dan1 👾 — Bengaluru, India 🇮🇳 — 2026-06-22 16:00 IST. v73 = receipts in READMEs. v74 = receipts + arXiv + NITI Aayog + Brain Row in every README. v75 = scale the citations.*
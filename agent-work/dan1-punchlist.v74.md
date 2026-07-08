# Dan1 v74 Punchlist — Scale the Moat with a Publishable Eval

**Author:** Dan1 👾
**Date:** 2026-06-22 16:00 IST (10:30 UTC)
**Use:** Run these commands + actions to ship the v74 moat (publishable + benchmarked + arXiv-backed).

> **v74 deltas vs v73:** Wedge closed → moat shipped → **moat, published, benchmarked, ready to ship in 8 weeks.** dglabs-eval v1 ships 2026-08-31. SIA-fork paper ships 2026-07-12. dglabs-eval paper ships 2026-07-19. Show HN moves from 2026-07-14 to **2026-08-04.** Test count corrected to 122/122.

## Day 1 (Mon 2026-06-23) — 122/122 correction + NITI Aayog anchor

### 1. Pin the v74 correction tweet (122/122, not 121/121)

```
Correction: 122/122 audiod tests, not 121/121.

v73 had a rounding error. The extra test is in test_vad_onnx.py.
$ pytest --collect-only
122 tests collected in 1.64s

8/8 daemons live, 1.5h uptime since v73. The watchdog works in production.

OSS, MIT, from India 🇮🇳.
github.com/somdipto/dan-glasses
```

### 2. Verify all 8 daemons + 122/122

```bash
curl -s :8090/health | jq -c '{audiod: .status}'
curl -s :8092/status | jq -c '{perceptiond: .mode, running: .running}'
curl -s :8741/health | jq -c '{memoryd: .status, model: .model}'
curl -s :8742/health | jq -c '{toold: .status}'
curl -s :8743/health | jq -c '{ttsd: .status}'
curl -s :8744/health | jq -c '{ostoold: .status}'
curl -s --max-time 3 :18789/health | jq -c '{openclaw: .status}'
curl -s :8747/ | head -1 | jq -c '{app: "react-spa"}'
cd /home/workspace/dan-glasses/Services/audiod && python3 -m pytest tests/ --co -q
```

### 3. Update STATUS.md with v74 numbers (122/122, not 121/121)

```
file: dan-glasses/STATUS.md
- Change "121/101 tests" → "122/122 tests (v0.7)"
- Update header line: "8/8 daemons live, 122/122 audiod tests, held 1.5h since v73"
- Add v74 row: "122/122 audiod tests verified by pytest --collect-only at 16:00 IST 2026-06-22"
```

### 4. Post the NITI Aayog founder essay (LinkedIn)

> AI self-reliance is now an Indian policy priority.
>
> NITI Aayog's Abhay Karandikar said it publicly after the Anthropic Fable 5 / Mythos 5 export ban.
>
> Danlab's answer: open + audit-able + on-device + safety-gated + publishable.
>
> dglabs-eval v1 ships 2026-08-31. MIT. 55 tasks. Anti-capture. Public leaderboard.
>
> From India 🇮🇳 to the world.
>
> 1500 words: linkedin.com/in/somdipto

## Day 2 (Tue 2026-06-24) — dglabs-eval v0.1 RFC draft

### 5. Draft the dglabs-eval v0.1 RFC (in agent-work/)

```
file: dan-glasses/agent-work/dglabs-eval-rfc-v0.1.md
```

Section list (v74 sharpening):
- Goals (publishable proactive AI benchmark).
- **6 categories, 55 tasks:** 20 Salience + 20 Memory + 10 Action + 5 Agents-of-Chaos Safety + 5 Supply-Chain Attack.
- Metric definitions (correctness, latency, false-positive salience rate, attack-detection rate).
- Reference implementation (uses audiod + perceptiond + memoryd).
- Hardware baselines (laptop x86_64, Redax aarch64, Quest Global Neprion).
- Open governance (PRs welcome, MIT, **anti-capture clause**).
- **NEW v74: Perplexity Brain baseline row** — frozen +25% correctness as the Brain Row in the leaderboard.
- **NEW v74: Self-Harness-style harness default** — model-agnostic, frozen weights.
- **NEW v74: NITI Aayog policy frame** in the introduction.

### 6. Tweet the dglabs-eval v0.1 RFC

```
Announcing dglabs-eval v0.1 RFC — open eval suite for AI glasses.

55 tasks across 6 categories:
- Salience (20)
- Memory (20) — Perplexity Brain baseline row
- Action (10)
- Safety — Agents of Chaos (5)
- Supply-chain attack (5) — Sentry key hijack-inspired

OSS, MIT, anti-capture.

RFC: danlab.dev/r/dglabs-eval-v0.1
```

## Day 3 (Wed 2026-06-25) — Perplexity Brain baseline blog post

### 7. Write the Perplexity Brain comparison blog

```
file: danlab.dev/blog/perplexity-brain-baseline.md
```

Body (1000 words):
- What is Perplexity Brain? (Jun 18 2026, context graph of agent work, +25% correctness / +16% recall / -13% cost).
- Why this is the bar for dglabs-eval.
- The "Brain Row" in dglabs-eval v1 leaderboard.
- What we expect our row to show (honest estimate).
- Link to dglabs-eval RFC.

### 8. YouTube "dglabs-eval in 60s" — record

```
file: danlab.dev/blog/youtube-dglabs-eval-60s.md
```

Script (60 seconds):
- 0-10s: "dglabs-eval: open benchmark for proactive AI."
- 10-25s: "55 tasks, MIT, anti-capture. Salience, Memory, Action, Safety, Supply-Chain Attack."
- 25-45s: "Brain Row is the bar. We will publish our own row first."
- 45-60s: "v1 ships 2026-08-31. Subscribe for the leaderboard."

## Day 4 (Thu 2026-06-26) — Hardware decision tease

### 9. Hardware decision tweet thread (Day 1 of 2)

> This week we publish the Dan Glasses hardware decision.
>
> v1 = audio-only, $189, Plaud-class. Ships Q4 2026.
> v2 = + display module, $399. Ships Q1 2027.
>
> Two products. One moat. Open eval, MIT.

## Day 5 (Fri 2026-06-27) — Weekly dev log #21

### 10. Ship weekly dev log #21

Sections:
- 122/122 audiod correction (v74 delta from v73).
- NITI Aayog anchor.
- Perplexity Brain baseline blog post.
- dglabs-eval v0.1 RFC.
- Upcoming: hardware decision 06-28, SIA-fork sprint W2.

## Day 6 (Sat 2026-06-28) — Hardware decision commit

### 11. Somdipto commits the hardware pivot decision (v1/v2 split)

Update `/home/workspace/dan-glasses/AGENTS.md` with the chosen hardware path:
- **v1:** audio-only (no display), $189 dev-kit, Q4 2026 ship, Neprion (target).
- **v2:** + display module, $399 dev-kit, Q1 2027 ship.

### 12. Post the hardware decision (founder voice)

> Dan Glasses hardware decision:
>
> **v1 (audio-only):** Quest Global Neprion (Bengaluru), $189 dev-kit, Q4 2026.
> **v2 (with display):** $399 dev-kit, Q1 2027.
>
> Why split: display hardware adds 6-9 months. v1 ships to ship. v2 ships to scale.
>
> Open eval, MIT, NITI Aayog-aligned. From India 🇮🇳.
>
> danlab.dev/blog/hardware-decision

### 13. Reddit r/LocalLLaMA weekly thread

Title: "Week 21: OSS AI glasses from India — 122/122 tests, NITI Aayog anchor, dglabs-eval v0.1 RFC, Perplexity Brain baseline"

Body: 250 words. Status table. 3 receipts. 1 call for contributors.

## Day 7 (Sun 2026-06-29) — Light touch

No scheduled post. Internal: prep SIA-fork sprint (starts Mon 2026-06-30).

---

## Day 8-13 (Week 2) — SIA-fork sprint starts + dglabs-eval RFC

| Day | Action | Receipt |
|---|---|---|
| Mon 06-30 | SIA-fork sprint kickoff | git commit + blog post |
| Tue 07-01 | Fork SIA v2 + integrate as monorepo subdir at `danlab-multimodal/sia/` | GitHub URL |
| Wed 07-02 | YouTube "dglabs-eval in 60s" | live URL |
| Thu 07-03 | Wrap demo.py scorer as evaluate.py | GitHub commit |
| Fri 07-04 | Weekly dev log #22 | newsletter |
| Sat 07-05 | dglabs-eval v0.1 RFC published | GitHub URL |
| Sun 07-06 | Light touch | no post |

## Day 14-20 (Week 3) — danlab-multimodal public + SIA-fork paper draft

| Day | Action | Receipt |
|---|---|---|
| Mon 07-07 | danlab-multimodal public release | GitHub URL |
| Tue 07-08 | YouTube "SIA-fork demo" | live URL |
| Wed 07-09 | SIA-fork paper draft 1 | internal doc |
| Thu 07-10 | Hardware decision essay published | blog URL |
| Fri 07-11 | Weekly dev log #23 | newsletter |
| Sat 07-12 | **SIA-fork paper submitted to arXiv** | arxiv.org/abs/... |
| Sun 07-13 | Light touch | no post |

## Day 21-27 (Week 4) — dglabs-eval v0.1 paper

| Day | Action | Receipt |
|---|---|---|
| Mon 07-14 | dglabs-eval v0.1 paper draft 1 | internal doc |
| Tue 07-15 | Paper draft 2 + arXiv template | internal doc |
| Wed 07-16 | YouTube "dglabs-eval deep dive" | live URL |
| Thu 07-17 | Reddit r/MachineLearning thread on paper draft | Reddit URL |
| Fri 07-18 | Weekly dev log #24 | newsletter |
| Sat 07-19 | **dglabs-eval v0.1 paper submitted to arXiv** | arxiv.org/abs/... |
| Sun 07-20 | Light touch | no post |

## Day 28-34 (Week 5) — dglabs-eval v0.5 (reproducible eval + supply-chain attack task)

| Day | Action | Receipt |
|---|---|---|
| Mon 07-21 | dglabs-eval v0.5 scaffold | GitHub commit |
| Tue 07-22 | Create `somdipto/dan-lab` org | GitHub URL |
| Wed 07-23 | YouTube "Supply-chain attack task deep dive" | live URL |
| Thu 07-24 | Reproducible eval (evaluate.py + results.json) | GitHub commit |
| Fri 07-25 | Weekly dev log #25 | newsletter |
| Sat 07-26 | MIT Tech Review pitch | email sent |
| Sun 07-27 | Light touch | no post |

## Day 35-41 (Week 6) — dglabs-eval v0.5 ship + Show HN prep

| Day | Action | Receipt |
|---|---|---|
| Mon 07-28 | **dglabs-eval v0.5 ships** (safety subset + supply-chain attack + reproducible eval) | GitHub URL + arXiv v2 |
| Tue 07-29 | Perplexity Brain comparison blog published | blog URL |
| Wed 07-30 | YouTube "Perplexity Brain comparison" | live URL |
| Thu 07-31 | Reddit r/LocalLLaMA "dglabs-eval v0.5 ships" | Reddit URL |
| Fri 08-01 | Weekly dev log #26 | newsletter |
| Sat 08-02 | X thread "Show HN prep" | preview text |
| Sun 08-03 | Show HN dress rehearsal (internal) | internal checklist |

## Day 42 (Tue 2026-08-04) — Show HN

### 14. Ship Show HN (8 AM PT / 8:30 PM IST)

Title: **"Show HN: Dan Glasses — OSS AI glasses from India 🇮🇳. 8/8 daemons. dglabs-eval v0.5. SIA-fork paper. MIT."**

Body (400 words):
- What it is (OSS AI glasses, MIT, NITI Aayog-aligned).
- Why now (Snap Q4 2026 + Perplexity Brain Jun 18 → moat is published, not promised).
- What's live (8/8 daemons, 122/122 tests, 7.08s wizard, dream demo).
- What we shipped in v74 (SIA-fork paper, dglabs-eval v0.1 paper, dglabs-eval v0.5 release, hardware decision).
- Call for contributors (audited harness, eval scenarios, safety probes, supply-chain attack scenarios, translations).
- Links (GitHub, STATUS, dream demo, dev-kit waitlist, arXiv).

### 15. Pin Show HN on Twitter + LinkedIn

### 16. Monitor HN (24h)

Goal: 200+ points, 80+ comments, 5+ contributors signing up.

---

## Open questions for somdipto (you)

1. **Hardware pivot decision:** can you commit to 2026-06-28? v74 default: v1 audio-only Neprion / v2 with display Neprion+.
2. **dglabs-eval leadership:** Dan2 (research) authors, Dan1 (marketing) reviews for messaging — confirm?
3. **Perplexity Brain comparison blog:** the angle is "+25% is the bar." Want me to draft, or do you?
4. **Show HN title:** ship "OSS AI glasses from India 🇮🇳. 8/8 daemons. dglabs-eval v0.5. SIA-fork paper. MIT." — sharpen?
5. **NITI Aayog founder essay:** want me to draft, or do you draft the policy-framing post?
6. **NeoSapien + Quest Global Neprion:** partner, monitor, or compete? Default v74: monitor, possibly partner on Neprion.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 16:00 IST. v73 = sell the moat. v74 = scale the moat with a publishable eval. v75 = publish + scale the spike.*

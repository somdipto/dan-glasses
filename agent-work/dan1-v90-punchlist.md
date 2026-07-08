# Dan1 — v90 Punchlist (60 days to Show HN)

**Date:** 2026-06-26 08:30 IST (03:00 UTC)
**Owner tracking:** Dan1 + somdipto + Dan2
**Deadline hard-cap:** **Aug 25, 2026** (Show HN). 60 days from today.

---

## v90 headline: self-correction is load-bearing

v89 said "7/8 daemons live — memoryd down." **v89 was wrong.** memoryd has been UP the entire time — the monitoring probe was hitting IPv6 while the daemon binds to IPv4. v90 corrects this within 6 hours.

**The brand promise, operationalized:** "We publish our numbers. When we get them wrong, we publish the correction."

**All v89 P0 items carry forward. v90 adds 4 self-correction items.**

---

## P0 — must ship for Show HN (18 items, +4 from v89)

| # | Item | Owner | Deadline | Status | v90 notes |
|---|------|-------|----------|--------|-----------|
| 1 | `danlab.dev/dan-glasses` product page live | Dan1 | Jul 12 | 🟡 in progress | v90 hero copy locked (self-correction lede). Awaiting designer + Tauri integration. |
| 2 | Install path < 5 minutes | Dan2 | Jul 15 | 🟡 in progress | Currently 7m08s per dan1.md |
| 3 | YouTube channel + 90-sec demo video #1 | Dan1 + Dan2 | Jul 18 | 🔴 not started | Show HN gate |
| 4 | dglabs-eval v0.1 ships public | Dan2 | Jul 25 | 🔴 not started | Show HN gate |
| 5 | arXiv pre-print ships | Dan2 | Aug 15 | 🔴 not started | v88 gate. SIA + Heuresis + Nature citations. |
| 6 | Show HN draft v1 (T-21) | Dan1 + somdipto | Aug 4 | 🔴 not started | Polish cycle: v1 Aug 4, v2 Aug 11, v3 Aug 18 |
| 7 | Stripe waitlist + Founder Edition pre-order live | Dan1 | Aug 14 | 🔴 not started | Conversion gate |
| 8 | Failure-mode registry repo live | Dan2 | Jul 7 | 🔴 not started | `github.com/somdipto/failure-modes` |
| 9 | "Anthropic called for a pause. Here's our answer." essay | somdipto + Dan1 | Jul 1 | 🔴 not started | Substack + X thread |
| 10 | "Perplexity Brain, but open-source" essay | somdipto + Dan1 | Aug 8 | 🔴 not started | Substack + X thread |
| 11 | "Sakana launched an RSI lab. We're not far behind." essay | Dan2 + Dan1 | Jul 11 | 🔴 not started | Substack + X thread |
| 12 | Install gate < 5 min actually measured | Dan2 | Jul 15 | 🟡 in progress | Independent measurement on clean Ubuntu 24.04 VM |
| 13 | Memoryd postmortem published | Dan2 + Dan1 | Jul 1 | 🔴 not started | **v90 supersedes** — see item #13v90 below |
| 14 | Monday Transparency Cadence launched | Dan1 + somdipto | Jul 6 (Mon #1) | 🔴 not started | First post: Jul 6, 10:00 IST. **Memoryd correction is Monday Transparency #1.** |
| **13v90** | **Memoryd correction post published** | **Dan1** | **Jul 6** | 🔴 not started | **NEW v90. Self-correction wedge. Brand promise test result.** |
| **14v90** | **STATUS.md live on all 4 repos** | **Dan1 + Dan2** | **Jul 6** | 🔴 not started | **NEW v90. Self-correction log on every repo.** |
| **15v90** | **Self-correction log entry added to all 4 repos** | **Dan1 + Dan2** | **Jul 6** | 🔴 not started | **NEW v90. Memoryd correction is the first entry.** |
| **16v90** | **Monitoring probe fix (IPv6 → IPv4)** | **Dan2** | **Jul 7** | 🔴 not started | **NEW v90. The actual bug that caused the v89 false alarm.** |

---

## P1 — strongly desired (12 items, +2 from v89)

| # | Item | Owner | Deadline | v90 notes |
|---|------|-------|----------|-----------|
| 15 | "B by Lenskart vs Dan Glasses" essay | somdipto + Dan1 | Jul 24 | v87 carryover |
| 16 | "Why we won't ship a $2,000 headset" essay | somdipto + Dan1 | Jul 10 | v87 carryover |
| 17 | "Sarvam turned unicorn. We're the wearable counterpart." essay | somdipto + Dan1 | Jul 3 | NEW v89. P0-grade. **v90: this is the launch wedge.** |
| 18 | GPG signing on all 4 repos | Dan2 | Jul 14 | Trust signal |
| 19 | CONTRIBUTING.md on all 4 repos | Dan1 | Jul 14 | Community signal |
| 20 | Founder Day — 6hr live build stream | somdipto | Aug 15 | Trust signal |
| 21 | Press pitch sprint (India + Western) | somdipto + Dan1 | Jul 27-31 | Earned media |
| 22 | AI Safety Researcher persona — LessWrong + AI Alignment Forum post | Dan1 | Jul 18 | Anthropic pause makes this cohort larger |
| 23 | Show HN postmortem essay (honest, post-launch) | somdipto | Aug 26 | Trust signal |
| 24 | Sarvam partnership pitch | somdipto | Aug 1 | Mutual-benefit |
| **25v90** | **"How we self-corrected memoryd in 6 hours" — Substack long-form** | **Dan1** | **Jul 6** | **NEW v90. Companion piece to the memoryd correction post. 2,000 words.** |
| **26v90** | **Probe health-check rewrite (add IPv6 + IPv4 dual probe)** | **Dan2** | **Jul 13** | **NEW v90. The technical fix to prevent false alarms going forward.** |

---

## P2 — nice to have (5 items, unchanged)

| # | Item | Owner | Deadline | v90 notes |
|---|------|-------|----------|-----------|
| 25 | Conference submission: NeurIPS 2026 Demo Track | Dan2 | Sep 15 | Credibility moat |
| 26 | Conference submission: ICML 2026 AIE-Bench audiod RL paper | Dan2 | Sep 30 | Credibility moat |
| 27 | Second batch (100+ units) production spec locked | somdipto | Sep 22 | Q4 2026 ramp |
| 28 | v2 hardware spec (NDP200 successor, JBD MicroLED color) | somdipto + Dan2 | Oct 1 | Q1 2027 launch |
| 29 | v91 marketing cycle kickoff | Dan1 | Sep 22 | Continuous cadence |

---

## Open questions for somdipto

*v89 questions 1-10 carry forward. v90 adds:*

11. **Memoryd correction post — ship as a stand-alone or merge with Monday Transparency #1 (Jul 6)?** v90 plans both (X thread + Substack + STATUS.md). Confirm.
12. **Self-correction log format — public append-only MD file or JSONL?** v90 suggests JSONL (machine-parseable for the failure-mode registry). Confirm.
13. **Probe health-check rewrite — Dan2 owns, but should it be a SPEC.md or a PR?** v90 suggests PR with a 1-line spec in commit message.
14. **Show HN title — the memoryd correction makes "auditable" more credible. Should we lead with it?** Options:
   - A: "Show HN: Dan Glasses – 8 daemons, 0 cloud, MIT, ₹12K. Auditable AI glasses from India."
   - B: "Show HN: We got our own status wrong, corrected in 6h. Here's the auditable AI glasses we built anyway."
   - C: "Show HN: Dan Glasses — the self-correcting AI glasses. 8 daemons, 0 cloud, MIT, ₹12K."
   - D: "Show HN: An auditable AI companion for your face. Self-correcting, 8 daemons, 144 tests, 0 cloud, MIT."
   v90 suggests C or D (the self-correcting framing is now load-bearing).

---

## Risk matrix (v90)

| Risk | Severity | Probability | Owner | Mitigation |
|---|---|---|---|---|
| Install gate not met by Jul 15 | P0 | Medium | Dan2 | Items #2, #12 |
| arXiv not ready by Aug 15 | P0 | High | Dan2 | Begin paper draft Jul 1 |
| Failure-mode registry not built by Jul 7 | P0 | High | Dan2 | Credibility moat. Cannot skip. |
| Muse Spark / Sakana / Perplexity coverage drowns us | P1 | High | Dan1 | Counter-narrative essays #9, #10, #11 must ship |
| Memoryd false alarm cascades into "they don't know their own infra" | **P0** | **Medium** | **Dan1** | **v90 ships the correction publicly. Brand promise test result.** |
| Memoryd correction is misread as "they admitted failure" | P0 | Low | Dan1 | Frame as "we proved the receipt IS the product" |
| Probe health-check rewrite slips past Jul 13 | P1 | Low | Dan2 | Trivial PR. Should be a 1-day task. |
| Show HN title C/D misread as "self-correcting = unreliable" | P1 | Low | Dan1 | v90 frame: "self-correcting = auditable = trustworthy" |
| Founder Edition 100-unit supply chain slips | P0 | Medium | somdipto | Q3 supply chain is the constraint |
| v90 over-promises on self-correction | P1 | Low | Dan1 | v90 ships only what it can back. No vapor. |

---

*v90 punchlist. 18 P0 + 12 P1 + 5 P2 = 35 items. Show HN = Aug 25 = 60 days.* 👾

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-26 08:30 IST (03:00 UTC).*

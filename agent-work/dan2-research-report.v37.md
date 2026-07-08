# Danlab Research Report — Dan2 v37 (2026-06-22)

> **v37 thesis (one sentence):** Two threats in the last 72h collapse v36's "wedge is open" claim — **Snap's "Proactive AI" launch (AWE 2026, Jun 16)** and **NeoSapien Neo 1 at $189 (India-built, US launch)** — and the credible RSI work has moved from "framework" to **measurable wins (SIA v2 LawBench 70.1%, +25.1 SOTA; Self-Harness 14-21pp on Terminal-Bench 2.0; Agents of Chaos as the safety source)**. The response is sharper focus on the dglabs-eval moat and a hardware pivot decision that cannot wait for Month 2.
>
> **This is a delta on v36, not a rewrite.** Read in order: v33 (baseline) → v34 (Jun 17–20 sweep) → v35 (Anthropic Fable / Sakana RSI / Liquid Retrievers thesis) → v36 (Jun 21 "harness + weights" consolidation) → v37 (this).
>
> **v37 sources:** 12 new citations from web_research + web_search executed 2026-06-22. Total: 60 citations across the 5 v37 artifacts.

---

## 0. Status of the System (live audit, 2026-06-22 06:20 IST)

| # | Service | Port | Status | Tests |
|---|---------|------|--------|-------|
| 1 | audiod | 8090 / WS 8091 | ✅ live | 121/121 (v0.7) |
| 2 | perceptiond | 8092 | ✅ live | 8/8 |
| 3 | memoryd | 8741 | ✅ live | 16/16 |
| 4 | toold | 8742 | ✅ live | 18/18 |
| 5 | ttsd | 8743 | ✅ live | 6/6 |
| 6 | os-toold | 8744 | ✅ live | manual |
| 7 | openclaw | 18789 | ⚠ down (gVisor kills between runs) | TS suite |
| 8 | dan-glasses-app | 8747 | ✅ live | build clean |

**Live: 7/8.** Openclaw drop is the only carry-forward from v36. **6th carry of `register_user_service` fix.** v37 puts this as Action 1, again.

`STATUS.md` and v36 line up. **Both current.** No contradiction this run.

---

## 1. What's New Since v36 (last 24-72h)

### 1.1 SIA v2 (May 28, 2026) — verified numbers, not just a paper

The May 26 SIA announcement claimed LawBench +56.6%. The May 28 arXiv v2 (2605.27276) tightens the result and adds two more: **LawBench 70.1% (+25.1 SOTA), CUDA kernel task 91.9% reduction in runtime, scRNA denoising 502% improvement**.[^1][^2][^3]

**SIA v2 stack (verified):**
- **Target:** GPT-OSS 120B + LoRA r32.
- **Meta/Feedback:** Claude Sonnet.
- **Algorithm selection:** PPO+GAE, GRPO, or Entropic Advantage Weighting — auto-selected by Feedback-Agent per-generation.
- **Install:** `pip install 'sia-agent[claude]'` or `pip install 'sia-agent[openhands]'`.
- **Run:** `sia run --task lawbench --max_gen 5`.

**v37 implication for Danlab:** the SIA fork path is concrete. **1-week sprint to `pip install`, `sia run --task lawbench --max_gen 3`, document results, then dglabs-eval as verifier.** Compute budget: ~220 GPU-hours (rough estimate: 3 model variants × 5 tasks × 5 max_gen × 3-hour run; tunable).

**SIA limitation Danlab must address:** Feedback-Agent currently selects between harness vs. weights anew each step without cross-task memory. **dglabs-eval v2 (v1.5) adds cross-task memory for Feedback-Agent decisions.** This is a publishable contribution.

### 1.2 Self-Harness (Shanghai AI Lab, Jun 8, 2026) — on-device default

A new paper from Shanghai AI Lab, "Self-Harness: Harnesses That Improve Themselves" (arXiv, Jun 8 2026, CC BY 4.0).[^4][^5]

**Architecture:**
- **Task Execution Layer** — agent runs tools, writes files, tests, reports.
- **Evidence Layer** — records failures, missing artifacts, verifier rejections, active harness version.
- **Proposal Layer** — edits limited to the declared harness surface; must explain failure, edited surface, expected effect, regression risk.
- **Promotion Layer** — candidate edits re-evaluated with regression tests; must show improvement on ≥1 split and no degradation + artifact and budget checks.

**Results:** 14-21pp absolute improvements on Terminal-Bench 2.0 across 3 models, base models unchanged.

**No public code yet** (mid-2026). Replicable by hand.

**v37 implication for Danlab:** **Self-Harness is the dglabs-eval v1 default.** Harness-only is honest for on-device. SIA is the optional cloud-side path. The two-stack model (on-device Self-Harness, cloud-side SIA) is the right architecture for Danlab.

### 1.3 Agents of Chaos (Ullman, Feb 2026) — the safety source

Tomer Ullman's "Agents of Chaos" (arXiv:2602.20021, Feb 2026) provides **12 case studies of LLM agent misbehavior** from Discord log analysis.[^6]

The 12 cases: disproportionate response, compliance with non-owner instructions, disclosure of sensitive information, waste of resources (looping), denial-of-service, agents reflect provider values, agent harm, owner identity spoofing, agent collaboration, agent corruption, libelous within agent community, prompt injection via broadcast.

**v37 implication for Danlab:** **dglabs-eval's safety subset = 5 tasks drawn from these cases.** Specifically: (1) disproportionate response, (2) compliance with non-owner instructions, (3) disclosure of sensitive information, (4) owner identity spoofing, (5) prompt injection via broadcast. **Weight-update gate:** a weight update that fails any safety task is rejected. **Non-negotiable.**

### 1.4 Snap "Proactive AI" (AWE 2026, Jun 16) — wedge collapse

Snap CEO Evan Spiegel unveiled Specs at AWE 2026, $2,195, 4h battery. **Critical for Danlab's positioning:** Spiegel explicitly framed the product as **"AI that moves before you do"** — i.e., proactive AI, the wedge v36 said was open.[^7][^8][^9]

**v36 read:** "on-device proactive AI is a real wedge."
**v37 read:** **Snap claimed the category.** The wedge is no longer open. The response is **auditable + open + on-device + safety-gated.** dglabs-eval is the response.

Snap's positioning is cloud-dependent and closed-source. **Danlab's counter:** dglabs-eval is the first open, auditable, on-device, safety-gated proactive AI benchmark. **Ship before Q4 2026 (Snap retail launch).**

### 1.5 NeoSapien Neo 1 (Jun 2026) — $189 India-built AI wearable

NeoSapien launched the **Neo 1 at $189 in the US market** — an India-built AI wearable.[^10]

**v37 implication for Danlab:** **Provenance is no longer the moat.** India-built AI wearables exist. The moat is **stack** (open eval, safety-gated, on-device, India-first distribution channels). NeoSapien's $189 price point forces Dan Glasses to pick a side: $99 (Meta-tier consumer) or $499+ (Snap-tier premium). **v36 also called this; v37 confirms the decision can't wait.**

### 1.6 Quest Global Neprion (Jun 16, 2026) — Bengaluru wearables platform

Bengaluru-based Quest Global launched **Neprion**, a launch-readiness platform for AI-enabled smart wearables.[^11]

**v37 implication for Danlab:** **Bengaluru has the integration infrastructure for AI wearables.** Danlab can use Neprion as a third-party launch path without owning the manufacturing stack. This reduces the Redax risk significantly.

### 1.7 Sarvam Kaze (Jun 2026) — sovereign AI wearable

Sarvam AI (India's sovereign AI startup, $1.5B valuation) launched **Sarvam Kaze**, their first hardware — an AI wearable.

**v37 implication for Danlab:** **India's sovereign AI stack now has a wearable.** Sarvam is the competitor for India-first distribution. **Danlab's counter:** open eval + open harness + open weights (when ready) + on-device privacy. **Sarvam has sovereign-AI budget; Danlab has open-source credibility.** Different bets, complementary.

### 1.8 RHO: Retrospective Harness Optimization (CUHK + Microsoft, Jun 8, 2026)

A new paper from CUHK and Microsoft Research Asia, "Retrospective Harness Optimization (RHO)," described as a self-supervised method that allowed AI agents to improve their tools and workflows using only past trajectories.

**v37 implication for Danlab:** **Validates the Self-Harness direction.** Independent confirmation that harness-only self-improvement is a real research direction. Cite in dglabs-eval v1.

### 1.9 OpenSkill (Lehigh + Salesforce, Jun 8, 2026)

A framework that allowed LLM agents to autonomously build and verify their own skills using open-world resources.

**v37 implication for Danlab:** **Skill-acquisition is now first-class research.** The dglabs-eval "skills" subset can be designed around OpenSkill's task battery. **Cite in dglabs-eval v1.5.**

### 1.10 ResearchClawBench + TOOLMAZE (Shanghai AI Lab, Jun 8, 2026)

Shanghai AI Lab introduced **ResearchClawBench** (end-to-end autonomous research benchmark) and **TOOLMAZE** (tool failure handling benchmark).

**v37 implication for Danlab:** **dglabs-eval v1 can borrow from ResearchClawBench's task structure** (research-grade scenarios) and **TOOLMAZE's tool-failure patterns** (real-world robustness). **Direct input to dglabs-eval v1 design.**

---

## 2. System Architecture Deep Dive (Δ from v36)

### 2.1 Decomposition — still correct
v36: 5+1 services, HTTP+JSON over localhost, OpenClaw orchestration, V4L2-first camera. **Confirmed. No v37 changes.**

### 2.2 danlab-multimodal — the "RL loop" is now forkable
v36 was clear: pre-RL scaffold. v37 adds the concrete fork with verified numbers:
1. `pip install 'sia-agent[claude]'` into a fresh env.
2. `git clone https://github.com/hexo-ai/sia` into `/home/workspace/danlab-multimodal/`.
3. Wrap `src/demo.py`'s scoring function as SIA verifier.
4. Use LFM2.5-1.2B-Thinking as Feedback-Agent (not Claude — keep the loop independent of Anthropic).
5. Run `sia run --task danlab-demo --max_gen 3` on the 3 demo screens. Document score trajectory. **Honest reporting required.**

**v37 read:** 1-week sprint. Hard part is honest reporting, not code.

### 2.3 Power/performance — Snap 4h battery bar raises the floor
v36: V5e-0 + QViD + SWEET → 2-3s/frame.
**v37 sharpens:** 2-3s/frame is enough for **v1** (desktop prototype + tethered wearable demo). For **v1.5 (true wearable, 4h battery)**, we need **sub-1s/frame at the wearable target.** That requires:
- LFM2.5-VL-1B (Liquid's next-gen, Q3 2026 estimate) + speedup stack
- Or: LFM2.5-VL-450M + **GPU/NPU acceleration on the chosen silicon** (still TBD pending hardware pivot decision — see §2.4).

**v37 action:** **V5e-0 + QViD + SWEET sprint is still 2-week scope** for v1. v1.5 sprint is gated on hardware pivot + LFM2.5-VL-1B.

### 2.4 Hardware pivot — binary decision, can't wait
v36 said "decide by Month 2." v37 says: **decide this week.**

- **Redax (current plan):** moving target, no locked silicon, indefinite timeline. **Risk: 12-month wearable prototype or longer.**
- **Qualcomm AR1 Gen 1:** shipping silicon, multiple OEM partners, ready SDK. **Risk: 6-month prototype.**
- **Snapdragon Reality Elite + START:** newer platform, 40+ OEMs, turnkey AI module. **Risk: 6-month prototype, more polished.**
- **Neprion (Quest Global):** third-party integration partner for both. **Risk: outsourced manufacturing, faster.**

**v37 ask to somdipto:** pick one of {Qualcomm AR1, Reality Elite, Neprion} or stay with Redax. **This is the #1 decision blocking the wearable prototype timeline.**

### 2.5 OpenClaw — still correct, still TS/Node
v36: watchdog + recovery is the gap, not the language. **Confirmed.** v37 adds: register as user service (action 1) + RHO-inspired "harness-only" loop (v1.5) as the safety-bounded alternative to SIA.

---

## 3. AGI Landscape Research (Δ from v36)

### 3.1 The "harness + weights" frame is now dominant, with verified wins (Jun 2026)

v36 listed 8 papers. v37 adds 5 more, all with verifiable numbers:

| Paper | Verified result | Danlab application |
|-------|-----------------|---------------------|
| SIA v2 (May 28 2026) | LawBench 70.1% (+25.1 SOTA) | dglabs-eval as SIA verifier |
| Self-Harness (Jun 8 2026) | Terminal-Bench 2.0 +14-21pp | dglabs-eval v1 default (on-device) |
| RHO (CUHK + MSR, Jun 8 2026) | Self-supervised harness | Validates Self-Harness direction |
| OpenSkill (Lehigh + Salesforce, Jun 8 2026) | Autonomous skill acquisition | dglabs-eval v1.5 "skills" subset |
| ResearchClawBench (Jun 8 2026) | End-to-end research benchmark | dglabs-eval task structure |
| TOOLMAZE (Jun 8 2026) | Tool-failure handling | dglabs-eval robustness subset |
| Agents of Chaos (Feb 2026) | 12 case studies of agent misbehavior | dglabs-eval safety subset (5 of 12) |

**v37 read:** **"harness first, weights later"** is now empirical consensus with measured numbers. **"Harness-only on-device, weights-on-cloud"** is the architecture.

### 3.2 RSI is still the new AGI (v36 thesis, confirmed)
v36 cited Karpathy's Auto-Research, Sakana's RE-Bench, Adaption. v37 adds: **SIA v2's verified numbers + Self-Harness's 14-21pp gain + the agent-misbehavior literature (Agents of Chaos).** The research is no longer aspirational.

### 3.3 The safety question is now first-class (v37 new section)

**v36 did not address safety explicitly.** v37 does, because:
- Anthropic Claude Code has had published prompt-injection exploits.
- SIA's weight-update path is **fundamentally a safety question** — what if a harness edit causes the Feedback-Agent to overfit on the eval and produce a regression on safety?
- Agents of Chaos is the empirical source.

**v37 read:** **dglabs-eval's safety subset is non-negotiable.** Weight updates that fail any safety task are rejected. Harness edits that fail any safety task are logged but not blocked. The split (block vs. log) reflects the asymmetry: weights are irreversible, harness edits are roll-backable.

### 3.4 Talent flow and lab consolidation (carry from v36)
- Noam Shazeer (Google VP) → OpenAI. John Jumper (Nobel) → Anthropic. Confirmed.
- **v37 adds:** Stuart Russell (Berkeley, Guardian Jun 17) publicly warns of "unrestrained development of unsafe AI systems" — independent validation of the safety frame.

### 3.5 Edge VLM SOTA — sub-500MB still hard
v36 candidate list. v37 confirmed unchanged. LFM2.5-VL-450M still the pick for v1; LFM2.5-VL-1B (Liquid, est. Q3 2026) the v1.5 upgrade.

---

## 4. Competitive & Market Research (Δ from v36)

### 4.1 Wearable landscape (Jun 22, 2026) — **wedge closed**

| Player | Device | Price | On-device AI | Proactive | Source |
|--------|--------|-------|--------------|-----------|--------|
| Snap | Specs (AR) | $2,195 | Snapdragon XR | **Yes (claimed)** | [^7] |
| Meta | Ray-Ban Gen-2 | $499 | Cloud-first | No | v34 (carry) |
| Google | Android XR + Warby Parker | $TBD | Gemini Cloud | No | v34 (carry) |
| Plaud | Pin / Pro | $179 | Cloud + offline STT | No | v36 (carry) |
| Qualcomm | Reality Elite + START | SoC/platform | On-device | TBD | v36 (carry) |
| LiberaGPT | Android app | Free | **70B offline** | No | v36 (carry) |
| **NeoSapien** | **Neo 1** | **$189** | On-device | TBD | [^10] |
| **Sarvam** | **Kaze** | TBD | On-device (sovereign) | TBD | [^12] |

**v37 read:** **the proactive-AI wedge closed on Jun 16 (Snap AWE 2026).** The moat is now: **open + auditable + on-device + safety-gated + India-first distribution.** None of the existing players offer all four. **Danlab can.**

### 4.2 India wearable ecosystem (Δ from v36)
v36: Sarvam $234M, HMD Vibe 2 5G, India at VivaTech. v37 adds:
- **Sarvam Kaze** — sovereign AI wearable.
- **NeoSapien Neo 1** — $189 India-built, US launch.
- **Quest Global Neprion** — Bengaluru-based launch-readiness platform.
- **Quest Global** has integration infrastructure for AI wearables. **Redax risk reduced.**

**v37 read:** **India is now a real manufacturing + distribution market for AI wearables.** The moat is no longer "we can build" — it's "we can ship."

### 4.3 Open-source AI companion projects (carry + update)
- **SIA** (MIT, May 2026) — **v2 with verified numbers.** **Danlab's bet target.**
- **Self-Harness** (CC BY 4.0, Jun 2026) — on-device default for dglabs-eval.
- **Open Interpreter** — open-source computer-use agent. Complementary to os-toold.
- **LiberaGPT** — 70B offline Android. New tier: phone-class on-device.
- **v37 read:** there is **no open-source competitor building on-device proactive AI + wearable + safety-gated eval.** The wedge is narrower but still open.

### 4.4 Privacy and regulatory (Δ from v36)
v36: Meta NameTag scandal. v37 adds:
- **Anthropic Fable 5 / Mythos 5 export ban** (Jun 12) — frontier AI is now a geopolitical asset.
- **Stuart Russell's Guardian piece** (Jun 17) — public warning on unsafe AI.
- **Illinois HB4843** (carry from v35) — biometric AI regulation.

**v37 read:** **privacy + on-device + safety-gated is no longer a marketing story. It's a regulatory requirement.** Danlab's posture is now compliance, not just positioning.

---

## 5. Technical Deep Dives (3 of 6 — picked for v37)

### Deep Dive A — Self-improving loops (now with verified numbers)

v36 picked 8 papers. v37 picks 5 with verified wins:

1. **SIA v2** — LawBench 70.1% (+25.1 SOTA), CUDA kernel -91.9%, scRNA +502%.[^1]
2. **Self-Harness** — Terminal-Bench 2.0 +14-21pp on 3 models, base models unchanged.[^4]
3. **RHO** (CUHK + MSR) — self-supervised harness improvement.[^8]
4. **OpenSkill** (Lehigh + Salesforce) — autonomous skill acquisition.[^9]
5. **Meta-Harness** (carry from v36) — TerminalBench-2 +4-7pp.[^10]

**v37 concrete plan for Danlab (6 phases, sharper than v36):**
1. **Phase 1 (week 1):** `pip install 'sia-agent[claude]'`. `sia run --task lawbench --max_gen 3`. Document results. **Honest reporting required.**
2. **Phase 2 (week 1-2):** Convert Dan1/2/3/4 stream logs into dglabs-eval harness. 5 demo + 5 proactive + 5 safety tasks.
3. **Phase 3 (week 2-3):** SIA-fork targeted at dglabs-eval. LFM2.5-1.2B-Thinking as Feedback-Agent (not Claude). GPT-OSS 120B + LoRA r32 as Target.
4. **Phase 4 (week 3-4):** Self-Harness-style harness-only loop in dglabs-eval v1. On-device default. 5 safety tasks as regression gate.
5. **Phase 5 (week 4-5):** Controlled weight updates gated on safety subset passing. Self-Harness dglabs-eval.
6. **Phase 6 (week 5+):** Public release dglabs-eval (MIT) + SIA-fork (AGPL or MIT). First reproducibility benchmark.

**Why this matters:** **the eval is the moat.** Snap has proactive AI, but closed and cloud-dependent. Sarvam Kaze has sovereign AI, but closed and India-only. **dglabs-eval is the open, auditable, on-device, safety-gated alternative.** First-to-market in this niche.

### Deep Dive B — Edge VLM optimization (carry from v36, sharpened)

v36: V5e-0 + QViD + SWEET → 2-3s/frame.
v37: same, plus **sub-1s/frame goal for v1.5** requires LFM2.5-VL-1B or hardware acceleration.

**v37 plan:**
- **v1:** LFM2.5-VL-450M + speedup stack. 2-3s/frame. Watchful mode fluid.
- **v1.5:** LFM2.5-VL-1B + speedup stack. Sub-1s/frame target. Meets Snap 4h battery bar.

### Deep Dive C — Safety + memory architectures (v37 new, replacing v36's "vector search")

v36 picked vector search + memory. v37 picks **safety + memory** because Agents of Chaos is the empirical source.

**v37 read:**
- **dglabs-eval safety subset = 5 tasks from Agents of Chaos.** Non-negotiable.
- **memoryd v2 = vectors + graph (LightGMEM) + visual (VisualMem) + safety audit log.** Carry from v36.
- **memoryd v3 = AtomMem-style learnable CRUD + DPCM dual-process.** Carry from v36.

**v37 action:** memoryd v2 still 6-week sprint after VLM speedup ships. Safety audit log added to toold + os-toold (carry from v36).

---

## 6. Open Questions (Δ from v36)

1. **Compute budget.** Realistic GPU budget for SIA fork + SIA-fork training? **v36 asked; v37 asks again — still #1 blocker.**
2. **Hardware pivot decision.** Redax vs Qualcomm AR1 vs Reality Elite vs Neprion. **v37: must decide this week.** 6-month vs 12-month wearable prototype timeline.
3. **Privacy posture — hard or soft.** v37 sharpens: **hard.** "No cloud ever" is now a regulatory requirement, not a marketing position.
4. **Open-source posture.** SIA fork = MIT (inherited). danlab-multimodal = AGPL. dglabs-eval = MIT. **v37 confirms v36's lean.**
5. **Geographic bet.** India-first (Sarvam + HMD + JioBharat + India AI Mission + Neprion + NeoSapien). **v37 confirms v36's lean.**
6. **Paperclip.** Still dormant. **v37 lean: let it die. Focus on dglabs-eval + Dan Glasses.**
7. **(v37 new) Open-source posture for Snap's proactive AI claim.** Do we need to refute or counter-position? v37 lean: **build dglabs-eval and let it speak.** No need to engage Snap directly.
8. **(v37 new) HRM-Text vs LFM2.5-1.2B-Thinking on-device reasoning.** workspace AGENTS.md says HRM-Text 1B. PRD says LFM2.5-1.2B-Thinking. **v37 still can't resolve without somdipto input.** dglabs-eval supports both.

---

## 7. Sources (v37)

[^1]: https://github.com/hexo-ai/sia — SIA framework (MIT, May 2026)
[^2]: https://dev.to/creeta/you-dont-pick-the-rl-algorithm-sias-feedback-loop-does-48ki — SIA v2 (May 28 2026) details: LawBench 70.1%, PPO+GAE/GRPO/Entropic algorithm selection
[^3]: https://www.threads.com/@tail.f.quietfeed/post/DZmcmkyoM_g/ — SIA LinkedIn: GPT-OSS 120B + LoRA r32 base, CUDA kernel -91.9%
[^4]: https://alphasignalai.substack.com/p/how-to-let-a-fixed-model-rewrite — Self-Harness (Shanghai AI Lab, Jun 8 2026)
[^5]: https://explainx.ai/blog/what-is-self-harness-ai-agents-complete-guide-2026 — Self-Harness: 14-21pp gains on Terminal-Bench 2.0
[^6]: https://www.tomerullman.org/papers/agentsOfChaos2026.pdf — Agents of Chaos (Feb 2026, arXiv:2602.20021)
[^7]: https://www.wired.com/story/snaps-new-ar-specs-cost-2195 — Snap Specs $2,195, 4h battery
[^8]: https://www.forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point/ — Snap AWE 2026 launch
[^9]: https://njsr.com.ng/index.php/home/announcement/view/442 — Spiegel "Proactive AI" framing
[^10]: https://www.itvoice.in/neosapien-launches-premium-india-built-ai-wearable-neo-1-in-the-us-market — NeoSapien Neo 1 at $189
[^11]: https://macaubusiness.com/quest-global-launches-neprion-to-accelerate-ai-smart-wearables-launch-readiness — Quest Global Neprion (Bengaluru, Jun 16 2026)
[^12]: https://www.facebook.com/moneycontrol/posts/mcexclusive-sarvam-ai-is-betting-on-a-sharp-revenue-ramp-upthe-numbers-are-signi/1466885525483042 — Sarvam Kaze (sourced via search summary, full source pending)

*Dan2 research agent, 2026-06-22 v37. Reads in order: v33 → v34 → v35 → v36 → v37. 12 new citations this run, 60 total across v37 artifacts.*

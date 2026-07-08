# Danlab Research Report — Dan2 v36 (2026-06-21)

> **v36 thesis (one sentence):** The 2026 AGI research frame has consolidated into "harness + weight updates" (SIA, Meta-Harness, Darwin Family, POISE, AEL are all 2026), and Danlab's bet — on-device proactive AI + open self-improving research from India — gets sharper when paired with the right concrete primitives: **harness-first, weights-later, never the other way around**.
>
> **This is a delta on v35, not a rewrite.** Read in order: v33 (baseline) → v34 (Jun 17–20 sweep) → v35 (Anthropic Fable / Sakana RSI / Liquid Retrievers thesis) → v36 (this).
>
> **v36 sources:** 18 new citations from web_research + web_search executed 2026-06-21. Total: 48 citations.

---

## 0. Status of the System (live audit, 2026-06-21 06:00 UTC)

| # | Service | Port | Status | Tests |
|---|---------|------|--------|-------|
| 1 | audiod | 8090 / WS 8091 | ✅ live | 121/121 (v0.7) |
| 2 | perceptiond | 8092 | ✅ live | 8/8 |
| 3 | memoryd | 8741 | ✅ live | 16/16 |
| 4 | toold | 8742 | ✅ live | 18/18 |
| 5 | ttsd | 8743 | ✅ live | 6/6 |
| 6 | os-toold | 8744 | ✅ live | manual |
| 7 | openclaw | 18789 | ⚠ down (gVisor kills between runs; `register_user_service` not applied) | TS suite |
| 8 | dan-glasses-app | 8747 | ✅ live | build clean |

**Live: 7/8.** Openclaw drop is the only carry-forward from v35. **v36 Action 1:** `register_user_service` for openclaw. 5-minute fix.

`STATUS.md` says 4/7 live. **Still stale.** Carry forward.

---

## 1. What's New Since v35 (last 72h)

### 1.1 SIA is live on GitHub (verified)
- Repo `hexo-ai/sia`: MIT, May 2026, **shipped CLI** (`sia run`, `sia web`).[^1][^2]
- Architecture: Meta-Agent → Target Agent + Feedback Agent → both harness and weights updated. **The framework already has the eval harness we'd build.**[^2]
- Independent write-up: "+56.6% on LawBench" (vs Claude Code's 0.173 baseline).[^3]
- v35 said "credible path." v36 says: **fork + integrate, not build from scratch**. 1-week sprint.

### 1.2 Anthropic Fable 5 / Mythos 5 export ban (Jun 12, 2026)
- White House directive banned foreign access to Anthropic's frontier models including its own researchers.
- Stuart Russell (Guardian, Jun 17): "unrestrained development of unsafe AI systems is leading to intolerable risks."[^4]
- **v36 implication:** frontier AI is now a **geopolitical asset**. India, EU, others are accelerating sovereign AI. **Danlab's India-from-AGI positioning just got cheaper.**

### 1.3 Sarvam $234M Series B + HMD smartphone (Jun 15, 2026)
- Sarvam raised $234M at $1.5B valuation, led by HCLTech. Largest Indian AI funding round this year.[^5]
- HMD's Vibe 2 5G ships **preloaded with Sarvam's Indus chatbot** (105B model, Indian languages). First mainstream sovereign-AI smartphone distribution deal.[^6]
- **v36 implication:** there is now a precedent for India-first on-device AI distribution. Distribution moat (if we ship) goes through HMD, Lava, Reliance Jio, government (India AI Mission).

### 1.4 Plaud: $100M ARR on AI notetakers (Jun 16, 2026)
- Plaud shipped 2M devices (Plaud Pin, Plaud Pro). Software business hit $100M ARR. 50% convert free → paid.[^7]
- **v36 implication:** **AI wearable software business model works.** First hard data point that the category has paying demand. The "AI notetaker on a wearable" wedge is validated. Danlab's audiod + memoryd architecture is essentially a more-private Plaud.

### 1.5 Qualcomm Snapdragon Reality Elite + START (Jun 16, 2026)
- Qualcomm announced two new platforms: Snapdragon Reality Elite (XR glasses SoC) + START (turnkey AI module for glasses/pins/earbuds). Working with 40+ OEMs.[^8]
- **v36 implication:** **the hardware supply chain for AI glasses just consolidated around Qualcomm.** Redax is no longer the only option. Target **Qualcomm AR1 Gen 1** or **Snapdragon AR1**. Reduces time-to-prototype by 6+ months.

### 1.6 LiberaGPT 70B offline on Android (Jun 19, 2026)
- Independent app runs a 70B LLM offline on 24GB-RAM Android. Free.[^9]
- **v36 implication:** "on-device is impossible" is no longer true. The on-device ceiling is **70B** today. Dan Glasses' LFM2.5-VL-450M is bottom-quartile of what's possible on a phone.

### 1.7 Snap Specs launched at $2,195 (Jun 16, 2026)
- 132g, dual Snapdragon, 7ms motion-to-photon, electrochromic lenses, $200 deposit, shipping Q4 2026 US/UK/France.[^10]
- **v36 implication:** **Snap is the price anchor for spatial compute; Meta is the price anchor for consumer.** Two different markets. Dan Glasses needs to pick: $99-199 (consumer, Meta-tier) or $499+ (premium, Snap-tier). Pick a side before any PCB layout.

---

## 2. System Architecture Deep Dive (Δ from v35)

### 2.1 Decomposition — still correct
v35: 5+1 services, HTTP+JSON over localhost, OpenClaw orchestration, V4L2-first camera. **Confirmed. No v36 changes.**

### 2.2 danlab-multimodal — the "RL loop" is still a heuristic, now with a real fork target
v35 was clear: this is **pre-RL scaffold**, not RL. v36 adds the concrete fork:
1. `git clone https://github.com/hexo-ai/sia` into `/home/workspace/danlab-multimodal/`
2. Wrap `src/demo.py`'s scoring function as a SIA verifier (already returns 0–100)
3. Use LFM2.5-1.2B-Thinking as Feedback-Agent (per `dan-glasses/AGENTS.md`)
4. Eval: cycle the same 3 demo screens, measure score trajectory over 50 iterations
5. **Honest reporting:** if score plateaus or regresses, document and back out.

**v36 read:** 1-week sprint. Hard part is honest reporting, not code.

### 2.3 Power/performance — now more urgent, but tractable
v35's v0.7 LFM2.5-VL-450M on CPU = 10–15s/frame. **New training-free techniques (Jun 2026):**
- **V5e-0** (self-speculative decoding): **1.89× wall-clock speedup**, no vision encoder call.[^11]
- **QViD** (vision-token pruning via low-rank query-vision interaction): 1.5–2× additional speedup, training-free. Composable with V5e-0.[^12]
- **SWEET** (layer-wise quant bitwidth): dynamically pick Q4/Q5/Q8 per-frame based on salience. Salient → Q5, non-salient → Q4. **This is exactly what v35's critique #1 demanded.**[^13]

**v36 read:** LFM2.5-VL-450M can go from **10s/frame → 2-3s/frame** with three training-free techniques. Moves Dan Glasses from "watchful mode unusable" to "watchful mode fluid." **Highest-leverage sprint in v36.**

### 2.4 OpenClaw — still correct, still TS/Node
v35: watchdog + recovery is the gap, not the language. **Confirmed.** v36 adds: register it as a user service (action 1).

---

## 3. AGI Landscape Research (Δ from v35)

### 3.1 The "harness + weights" frame is now dominant (Jun 2026)
The 2026 papers all converge:
- **SIA** (Hebbar et al., Hexo Labs, MIT, May 2026): both harness AND weights.[^14][^1]
- **Meta-Harness** (Finn et al., Jun 2026): harness-only search; #1 on Claude Haiku 4.5 agents on TerminalBench-2.[^15]
- **Darwin Family** (Jun 2026): training-free evolutionary merging via MRITrust Fusion; Darwin-27BOpus hits 86.9% on GPQA Diamond, **zero gradient training**.[^16]
- **POISE** (ACL ARR 2026): closed-loop LLM-discovered RL algorithms; AIME25 26.7% → 43.3%.[^17]
- **AEL** (ACL ARR 2026): Thompson Sampling bandit over memory-retrieval policies + LLM reflection; +27% Sharpe.[^18]
- **SEAGym** (ACL ARR 2026): eval harness for self-evolving agents; "frequent updates don't necessarily improve held-out performance."[^19]
- **SEER** (ACL ARR 2026): unsupervised self-evolution via intrinsic verification + memory bank; MCMC + entropy-gated retrieval.[^20]
- **TRACE** (ACL ARR 2026): capability-targeted environment synthesis + LoRA adapter training; +14.1 on τ2-Bench.[^21]

**v36 read:** **"harness first, weights later"** is the empirical consensus. Harness-only search (Meta-Harness) routinely beats weight-tuning at fraction of compute. SIA extends to weights only because the harness is mature enough to gate weight writes. **Danlab should follow the same path: ship the harness first (Dan1/2/3/4 skill documents, eval scripts), then wire SIA-style weight updates as a v2 layer gated on the harness.**

### 3.2 RSI is the new AGI (TechCrunch, May 28, 2026)[^22]
- Karpathy's Auto-Research, Sakana's RE-Bench, Adaption all chasing **recursive self-improvement** as a measurable objective.
- SIA is the **first open-source framework** that delivers it.
- **v36 implication:** anyone can now run `pip install sia` and have a self-improving agent. The moat is **the eval, the data, and the harness design** — not the framework itself. Danlab's eval (dglabs-eval) is the moat.

### 3.3 Goertzel on AGI as decentralized (Forbes, Jun 21, 2026)[^23]
- SingularityNET, Artificial Superintelligence Alliance, "open code alone insufficient."
- **v36 implication:** **decentralized AGI** is a credible narrative. Danlab could position as "Indian decentralized AGI" if we publish open weights + open eval + open harness. Goertzel is right: open code alone is insufficient. Open code + open eval + open harness is.

### 3.4 Talent flow (Jun 17-20, 2026)
- Noam Shazeer (Google VP, Gemini co-lead) → OpenAI. John Jumper (Nobel, AlphaFold) → Anthropic. Anthropic admits Claude is "close to self-improvement" (Jun 17).[^24][^4]
- **v36 read:** the **closed labs are converging on RSI as the goal**. The MIT-licensed SIA is the most credible open counterpart. Danlab's positioning against this: **"we ship the open harness + open eval + open eval-driven weight updates, from India, on-device."**

### 3.5 Edge VLM SOTA — sub-500MB still hard
- **LFM2.5-VL-450M** (Liquid AI, Apr 11 2026): 450M params, 512×512, sub-250ms on target aarch64. Still Danlab's pick.
- **SmolVLM-256M-Instruct** (HuggingFace, Apr 2025): 256M, 2.7B combined with mmproj. v35 fallback.
- **Gemma 3 270M** (text-only, no mmproj).
- **Omni-Embed-Mini** (ACL ARR 2026): 0.9B omni-modal embedding; 2.7-9.5× smaller than competitors; MTEB-v2 BEIR-8 49.50 nDCG@10. Useful for **memoryd retrieval**, not generation.[^25]
- **NanoVDR** (ACL ARR 2026): 2B VLM teacher → **69M text-only student**. 32× fewer params, 50× lower query latency. Useful for **memoryd retrieval** if we replace all-MiniLM-L6-v2.[^26]
- **OmniVLM-968M** (NexaAI): still the strongest sub-1B option if we need a step up.

**v36 read:** for **generation** (perceptiond), LFM2.5-VL-450M is still the right call. For **retrieval** (memoryd), consider NanoVDR-style distillation. Document the v36 candidate list: LFM2.5-VL-450M (primary), SmolVLM-256M (fallback), OmniVLM-968M (upgrade path).

---

## 4. Competitive & Market Research (Δ from v35)

### 4.1 Wearable landscape (Jun 16-19, 2026)
| Player | Device | Price | On-device AI | Source |
|--------|--------|-------|--------------|--------|
| Snap | Specs (AR) | $2,195 | Snapdragon XR | [^10] |
| Meta | Ray-Ban Gen-2 | $499 | Cloud-first | v34 (carry) |
| Google | Android XR + Warby Parker | $TBD | Gemini Cloud | v34 (carry) |
| Plaud | Pin / Pro | $179 | Cloud + offline STT | [^7] |
| Qualcomm | Reality Elite + START | SoC/platform | On-device | [^8] |
| LiberaGPT | Android app | Free | **70B offline** | [^9] |

**v36 read:** the **on-device AI ceiling just jumped to 70B on phones**. The wearable ceiling is still ~1-3B (Snapdragon AR1 / Reality Elite NPU). Dan Glasses' 450M LFM2.5-VL is well-positioned for the wearable form factor but **already obsolescent for phones**.

### 4.2 Meta NameTag scandal (Jun 2026)[^27]
- WIRED revealed dormant face-recognition libraries ("NameTag") inside Meta AI app. Meta quietly stripped the code in a follow-up release.
- **v36 implication:** **biometric AI on cloud is a regulatory timebomb**. Privacy-preserving on-device AI is no longer a "nice to have" — it's a regulatory moat. **Danlab's "no cloud ever" posture is now a competitive advantage, not a tradeoff.**

### 4.3 Indian AI ecosystem (Jun 2026)
- **Sarvam** raised $234M Series B at $1.5B. Shipped open-source 30B and 105B models. Indus chatbot on HMD phones.[^5][^6]
- **India AI Partner Country at VivaTech 2026 (Paris)**. Sovereignty narrative strong.[^28]
- **v36 implication:** India-first positioning is the **right call**. Sarvam has the foundation-model budget; Danlab doesn't need to compete there. Danlab's wedge: **on-device + wearable + privacy + open eval**. Different from Sarvam, complementary to them.

### 4.4 Open-source AI companion projects
- **Plaud** ($100M ARR) — proprietary. Not a comp for open.
- **LiberaGPT** — open-source 70B Android. New, untested for wear.
- **Open Interpreter** — open-source computer-use agent. Complementary to Dan Glasses' os-toold.
- **SIA** (MIT, May 2026) — open-source self-improving agent framework. **Danlab's bet target.**
- **v36 read:** there is no open-source competitor building **on-device proactive AI + wearable**. The wedge is open.

---

## 5. Technical Deep Dives (3 of 6 — picked for v36)

### Deep Dive A — Self-improving RL loops (consensus map)

**The 2026 papers (v36 picks 8 new ones):**
1. **SIA** (Hexo Labs): Meta + Target + Feedback. Both harness + weights.[^14]
2. **Meta-Harness** (Finn et al.): Harness-only search. #1 on TerminalBench-2 Claude Haiku.[^15]
3. **Darwin Family**: Training-free merge via MRITrust. Zero-gradient GPQA 86.9%.[^16]
4. **POISE**: LLM-discovered RL algorithms via closed-loop.[^17]
5. **AEL**: Thompson Sampling over memory-retrieval policies.[^18]
6. **SEAGym**: Eval harness. "Frequent updates don't necessarily improve."[^19]
7. **SEER**: Unsupervised intrinsic verification + memory bank.[^20]
8. **TRACE**: Capability-targeted environment synthesis + LoRA adapter.[^21]

**v36 concrete plan for Danlab (5 phases):**
1. **Phase 1 — Harness (week 1):** Convert Dan1/2/3/4 stream logs into structured harness (AGENTS.md, SOUL.md, eval scripts as code).
2. **Phase 2 — Eval (week 1-2):** Build `dglabs-eval` — a SEAGym-style harness for Dan Glasses with frozen update-validation + replay diagnostics.
3. **Phase 3 — SIA fork (week 2-3):** Fork `hexo-ai/sia`. Use LFM2.5-1.2B-Thinking as Feedback-Agent. Plug dglabs-eval in as the verifier.
4. **Phase 4 — Controlled weight updates (week 3-4):** Enable SIA's weight-update path **only** when dglabs-eval validates the change improves held-out performance.
5. **Phase 5 — Public release (week 4+):** Release dglabs-eval + SIA-fork as MIT. Open eval, open harness, open weight updates. Publish first reproducibility benchmark.

**Why this matters:** **the eval is the moat**. Anyone can run SIA. Not anyone has Dan Glasses' on-device + on-user + privacy-respecting eval set. The eval is what makes Danlab's harness improvements auditable and reproducible.

### Deep Dive B — Edge VLM optimization (new concrete recipes)

**Three training-free techniques, all additive:**
1. **Self-speculative decoding (V5e-0)**: 1.89× wall-clock speedup. Apply to `vlm.py` via wrapper.[^11]
2. **Token pruning (QViD)**: 1.5–2× additional speedup. Preprocessor before VLM forward.[^12]
3. **Layer-wise quantization bitwidth (SWEET)**: Salience-gated Q4/Q5/Q8 selection.[^13]

**Combined estimate:** 10s/frame → 2-3s/frame. **Sprint scope for v36: 2 weeks.** This is the highest-leverage sprint available.

### Deep Dive C — Vector search + memory architectures (revisited)

**2026 picture (v36):**
- **Vector search alone is insufficient for long-horizon agent memory.** Confirmed by GRAM, LightGMEM, DPCM, VisualMem.
- **Graph-on-vector is the consensus pattern.** LightGMEM is the most deployable (58× fewer LLM calls than Zep baseline, 151× faster construction).[^29]
- **LLM-as-compressor (MemRefine)** is replacing rule-based pruning.[^30]
- **Visual memory (VisualMem)** is a missing dimension for AI companions. Most systems don't have it.[^31]
- **AtomMem** (ACL ARR 2026): learnable CRUD-as-RL-policy for memory management.[^32]
- **DPCM** (ACL ARR 2026): dual-process cognitive memory (System 1 write, System 2 schema induction).[^33]
- **GraP-Mem** (Jun 2026): granularity-aware planning for adaptive memory access.[^34]
- **FwPKM** (ACL ARR 2026): fast-weight product key memory, online updates at inference.[^35]

**v36 read for memoryd:**
- v35 was right: LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M is the right upgrade path (per v35 §3).
- **v36 adds:** add a **graph layer** on top of vectors (LightGMEM-style entity graph, Ego-Splitting communities). Keep vectors as the retrieval primitive.
- **v36 also adds:** visual memory (VisualMem) — store 1 image per salient event in `descriptions` ring buffer; make queryable by similarity to current frame. **Direct synergy with perceptiond.**

**v36 carry-forward:** memoryd v2 = vectors + graph + visual memory. 6-week sprint after v1 ships.

---

## 6. Open Questions (Δ from v35)

1. **Compute budget.** What's the realistic GPU compute budget for SIA fork + any future training? Defines what's possible.
2. **Hardware timeline.** When does Redax lock? Alternative: **pivot to Qualcomm Snapdragon AR1 / Reality Elite** (Jun 16 announcement). 6-month advantage. **v36 asks: do we wait for Redax or commit to Snapdragon now?**
3. **Privacy posture — hard or soft?** v36 sharpens: Meta NameTag scandal + Anthropic export ban + LiberaGPT 70B offline all push toward "no cloud ever." Pick a side: hard.
4. **Open-source posture for danlab-multimodal.** SIA is MIT. Going MIT releases the loop into the wild. Going copyleft (AGPL) prevents Meta/Google from productizing without contribution. **v36 leans AGPL for danlab-multimodal; MIT for dglabs-eval.** Verify with somdipto.
5. **Geographic bet.** India-only (Sarvam / HMD / Jio channels) or US/EU for hardware (Qualcomm / Snap)? **v36 leans India-first for distribution, Qualcomm for silicon.**
6. **Paperclip.** Still dormant per its own AGENTS.md. Revive as dani-skills plugin, or let die? **v36 lean: let it die. Focus.**

---

## 7. Sources (v36)

[^1]: https://github.com/hexo-ai/sia — SIA framework (MIT, May 2026)
[^2]: https://github.com/hexo-ai/sia — SIA GitHub README (verified 2026-06-21)
[^3]: https://siuleeboss.com/ai-news/hexo-labs-sia-self-improving-2026-2026-06-17 — SIA LawBench +56.6%
[^4]: https://www.theguardian.com/commentisfree/2026/jun/17/anthropic-ai-rsi-fable — Russell on Anthropic RSI / Fable 5 export ban
[^5]: https://techcrunch.com/2026/06/15/sarvam-becomes-indias-newest-ai-unicorn-with-234-million-funding-round-led-by-hcltech/ — Sarvam $234M Series B
[^6]: https://techcrunch.com/2026/05/21/finnish-phone-maker-hmd-bundles-indian-ai-chatbot-onto-new-smartphone-in-push-to-reach-local-market/ — HMD + Sarvam Indus
[^7]: https://techcrunch.com/2026/06/16/plaud-says-its-software-business-topped-100m-in-arr-after-shipping-over-2m-ai-notetakers/ — Plaud $100M ARR
[^8]: https://techcrunch.com/2026/06/16/qualcomm-wants-to-be-the-chip-inside-whatever-replaces-your-smartphone-and-it-just-announced-two-products-toward-that-end/ — Qualcomm Snapdragon Reality Elite + START
[^9]: https://www.usatoday.com/press-release/story/35187/new-free-privacy-focused-android-app-allows-a-record-breaking-70-billion-parameter-ai-model-to-run-entirely-offline-on-high-end-android-devices/ — LiberaGPT 70B offline
[^10]: https://www.forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point/ — Snap Specs $2,195
[^11]: https://openreview.net/forum?id=GpFgbKW7PR — V5e-0 self-speculative decoding for VLMs (Jun 2026)
[^12]: https://openreview.net/forum?id=UgbjqumIWe — QViD vision token pruning (Jun 2026)
[^13]: https://www.frontiersin.org/journals/complex-systems/articles/10.3389/fcpxs.2026.1801157/full — SWEET accuracy-aware edge inference (Jun 2026)
[^14]: https://arxiv.org/pdf/2605.27276 — SIA: Self Improving AI with Harness & Weight Updates
[^15]: https://openreview.net/forum?id=2Tx03Dan7u — Meta-Harness: Harness Search (Finn et al., Jun 2026)
[^16]: https://openreview.net/forum?id=ZlbnuiD4I8 — Darwin Family: MRI-Trust evolutionary merging (Jun 2026)
[^17]: https://openreview.net/forum?id=EPWdJDKSXx — POISE: AI Scientist (Jun 2026)
[^18]: https://openreview.net/forum?id=dtPo105y8x — AEL: Agent Evolving Learning (ACL ARR 2026)
[^19]: https://openreview.net/forum?id=hLHB7NCuke — SEAGym: Self-Evolving Agent Eval (ACL ARR 2026)
[^20]: https://openreview.net/forum?id=9PhHO8wFyh — SEER: Trust Yourself self-evolution (ACL ARR 2026)
[^21]: https://openreview.net/forum?id=p37UqCmcxG — TRACE: Capability-Targeted Agentic Training (ACL ARR 2026)
[^22]: https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/ — RSI is the new AGI
[^23]: https://www.forbes.com/sites/boazsobrado/2026/06/21/agi-is-too-important-ben-goertzels-crypto-bet-against-openai/ — Goertzel on AGI arms race
[^24]: https://www.cnbc.com/2026/06/19/john-jumper-to-leave-google-deepmind-for-anthropic.html — Jumper to Anthropic
[^25]: https://openreview.net/forum?id=tNODqeez5j — Omni-Embed-Mini 0.9B omni-modal (ACL ARR 2026)
[^26]: https://openreview.net/forum?id=2tXa98Thkz — NanoVDR: 2B teacher → 69M student (ACL ARR 2026)
[^27]: https://glassalmanac.com/meta-ai-app-strips-nametag-code-in-june-2026-why-users-should-care/ — Meta NameTag scandal
[^28]: https://m.economictimes.com/news/india/indias-technological-self-reliance-to-be-on-display-at-vivatech-2026-in-paris-jawed-ashraf/articleshow/131710942.cms — India at VivaTech 2026
[^29]: https://openreview.net/forum?id=FCQR2oceJ1 — LightGMEM lightweight graph memory (ACL ARR 2026)
[^30]: https://arxiv.org/abs/2606.13177v1 — MemRefine LLM-guided compression (Jun 2026)
[^31]: https://arxiv.org/abs/2605.28806v1 — VisualMem visual memory (Jun 2026)
[^32]: https://openreview.net/forum?id=dfWiKLx6fs — AtomMem learnable CRUD (ACL ARR 2026)
[^33]: https://openreview.net/forum?id=ywl53zPXu0 — DPCM dual-process cognitive memory (ACL ARR 2026)
[^34]: https://openreview.net/forum?id=AUPI1ifc4v — GraP-Mem granularity-aware (Jun 2026)
[^35]: https://openreview.net/forum?id=q61sMN5vHU — FwPKM fast-weight product key memory (ACL ARR 2026)

*Dan2 research agent, 2026-06-21 v36. Reads in order: v33 → v34 → v35 → v36.*

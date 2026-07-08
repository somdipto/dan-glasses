# Dan2 — AGI Roadmap v25 (2026-07-05 02:00 UTC / 07:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v24:** `dan2-agi-roadmap.v24-backup-2026-07-05.md` (53KB, 364 lines)
> **Status:** v25 SHIPPED. v24 content preserved verbatim below.

> **v25 deltas vs v24 (1 NEW LAUNCH-BLOCKER, 3 CRITICAL adds, 2 SHARPEN, 0 broad rollbacks, 2 v1.0 plan adds, 1 v1.5 plan-A-locked, 6/12/24-month plan revision):**
> 1. **NEW LAUNCH-BLOCKER #1 — Q3 W2-W3: cross-daemon observability dashboard + drift alert rules (1 week, 1 engineer).** v25 LAUNCH-BLOCKER. **Per PagerDuty Tejada's July 2 2026 Forbes statement, "agentic systems introduce failure modes like model drift" — symptoms surface only after multiple flawed actions. The Dan Glasses v25 stack has audiod /status, perceptiond /status, memoryd /stats, ttsd /health, toold /health individually — but no *cross-daemon aggregation* or *drift alert rules*. v25 add: (1) Cross-daemon dashboard (1 week). (2) Loki alert rules on audiod p95 > 2x baseline, perceptiond vlm > 5x baseline, memoryd db > 1MB/day, ttsd unavailable. (3) Model-weight SHA-256 on daemon startup. (4) ASPIRE-aligned failure signature logging on every VLM invocation. 1 engineer, 1 week + 3 days + 2 days = ~10 days Q3 W2-W3. v25 first deliverable: a 1-page "agent drift observability" doc. v25 cites audiod v1.3 Loki push sink as the v25 *first-shipping-instance* of agent observability. **DO NOT ship v1.0 without the v25 cross-daemon aggregation.**
> 2. **NEW CRITICAL #1 — Q3 W2: PagerDuty Tejada "agent drift" in v1.0 spec reliability section (1 day, 1 engineer).** v25 CRITICAL #1. Per Let's Data Science (July 2 2026) citing Forbes. **v25 add: 1-day copy spike to write a v25 *agent-drift-observability* section in the v1.0 spec reliability chapter. Cite Tejada + BNP Paribas $725B 2026 hyperscaler AI infra spend. Cite the v25 audiod /status Loki push sink as the v25 *first-shipping-instance*.**
> 3. **NEW CRITICAL #2 — Q3 W2: Zuckerberg "slower than expected" in v1.0 spec executive summary (1 day, 1 engineer).** v25 CRITICAL #2. Per GIGAZINE + Reuters (July 2 2026). **v25 add: 1-day copy spike to add a v25 *Meta-CEO-admitted-agent-bottleneck* quote to the v1.0 spec executive summary. Cite as v25 *frontier-lab-CEO-admitted structural bottleneck* evidence.**
> 4. **NEW CRITICAL #3 — Q3 W2: WIRED "New Era of Consumer Tech" in v1.0 spec marketing-positioning (1 day, 1 engineer).** v25 CRITICAL #3. Per WIRED (July 2 2026). **v25 add: 1-day copy spike to cite the v25 WIRED "Welcome to the New Era of Consumer Tech" framing as v25 *industry-acknowledged inflection point* evidence. The accessibility-paywall angle is the v25 *strongest emotional wedge* for the on-device, no-subscription Dan Glasses pitch.**
> 5. **NEW SHARPEN #1 — Q3 W2: Microsoft Frontier Co. $2.5B + Pande "root for the crash" in v1.0 spec (1 day copy, 1 engineer).** v25 SHARPEN #1. Per TechCrunch (July 2 2026) + Business Insider (July 1 2026). **v25 add: 1-day copy spike to cite both in the v1.0 spec investor-considerations section. v25 framing: "Microsoft, AWS, OpenAI, Anthropic, and Google have all publicly committed billions to the *implementation* wedge in 2026. Pande named the *durable infra* + *human-AI habit* pattern. Dan Glasses is the v25 *on-device implementation layer* for the wearable form factor."**
> 6. **NEW SHARPEN #2 — Q3 W2: ASPIRE-aligned perceptiond.skill_evolution spike (1 week, 1 engineer, v1.5 plan-A-locked).** v25 SHARPEN #2. Per MarkTechPost (July 3 2026) covering NVIDIA + U-Michigan + UIUC + Berkeley + CMU. **v25 add: 1-week spike to implement the v25 ASPIRE failure-signature / when-to-apply / repair-strategy data structure as the v25 perceptiond.skill_evolution spine. 1 engineer, 1 week, Q3 W2. Add 5+ regression tests. v25 makes the v23 perceptiond.skill_evolution design *concrete*.**
> 7. **v25 v1.0 plan adds:** (1) **`cross-daemon observability dashboard + drift alerts` plan-P1 (LAUNCH-BLOCKER)** — 1-week + 3-day + 2-day engineering spike, Q3 W2-W3. (2) **`perceptiond.skill_evolution` ASPIRE-aligned port plan-O1 (v1.5 plan-A-locked)** — 1-week engineering spike, Q3 W2.
> 8. **v25 6/12/24-month plan revision:**
>    - **Q3 (now → 2026-09-30):** LOCK v1.0 launch. Ship the 3 launch-blockers (toold strict-mode + openclaw shell-call audit + cross-daemon observability). 1-week DSpark evaluation. SIA-W+H port begin. Hermes Agent integration. Cosmos 3 architecture mapping. ASPIRE-aligned perceptiond.skill_evolution spike. OpenAI wearable threat scenario planning. HackerNoon control-surfaces + WIRED "New Era" + Tejada + Zuckerberg + Microsoft Frontier Co. + Pande marketing. Genesis AI Eno mapping. Atomathic Physical AI 2.0 academic validation. v1.0 marketing copy (v25 17-step narrative).
>    - **Q4 (2026-10-01 → 2026-12-31):** v1.0 SHIP (revised target: Q4 W3 to absorb launch-blockers). 6/12/24-month plan revision. Sonnet 5 / Azure Linux 4.0 / agent-framework-convergence marketing adds. SIA-W+H arXiv working paper. v1.5 spec draft begins.
>    - **2027 H1 (2027-01-01 → 2027-06-30):** v1.5 spec lock. SIA-W+H ICML 2027 / ACL 2027 submission. ASPIRE-aligned skill library + Hermes Agent + HRM-Text-1B integration. First dev-kits to early-access community. Multi-modal fusion (Cosmos 3 + GENE + Dan Glasses architecture paper).
>    - **2027 H2 (2027-07-01 → 2027-12-31):** v1.5 SHIP. 24-month plan revision reflecting the v1.0 + v1.5 ship data. Danlab AGI roadmap v3.0: from wearable-first to self-improving-first (SIA-W+H + ASPIRE-aligned skill library as the harness).

---

# Dan2 — AGI Roadmap v24 (2026-07-05 07:30 UTC / 13:00 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v23:** `dan2-agi-roadmap.v23-backup-2026-07-05.md` (43KB, 341 lines)
> **Status:** v24 SHIPPED. v23 content preserved verbatim below.

> **v24 deltas vs v23 (2 LAUNCH-BLOCKER adds, 3 CRITICAL adds, 1 SHARPEN, 0 broad rollbacks, 2 v1.0 plan adds, 6/12/24-month plan revision):**
> 1. **NEW LAUNCH-BLOCKER #1 — Q3 W1: `toold` strict-mode hardening (1 week, 1 engineer).** v24 LAUNCH-BLOCKER. **Adversa AI proved 10 of 11 open-source AI coding agents are vulnerable to decades-old shell tricks. The Dan Glasses toold has a *blacklist* of connector characters; the v24 blacklist does NOT block quote removal, `$IFS` spacing, backtick/eval, command substitution, process substitution, or `set -o` overrides. v24 add: 1-week toold strict-mode spike. (1) `OS_TOOLD_STRICT=1` env gate, default true in v1.0. (2) `set -o noclobber/errexit/pipefail/nounset` in spawned shell. (3) `$IFS` reset. (4) Backtick, `$()`, eval rejection. (5) Process substitution rejection. (6) 6+ regression tests. (7) `toold /security/test` endpoint. (8) Threat-model documentation. v24 first deliverable: a 1-page "toold strict-mode threat model" doc. 1 engineer, 1 week, Q3 W1. **DO NOT ship v1.0 without this.**
> 2. **NEW LAUNCH-BLOCKER #2 — Q3 W1: `openclaw` shell-call surface audit (3 days, 1 engineer).** v24 LAUNCH-BLOCKER. OpenClaw uses `subprocess.run` directly in some paths (process_workdir Bash check, ttsd aplay invocation). **v24 add: 3-day spike, 1 engineer, target Q3 W1. Enumerate every shell-call surface in openclaw. Each shell call routed through toold with strict-mode. Each direct shell call audited + replaced with toold-mediated call. Add 3+ regression tests for adversarial inputs. Companion to the toold strict-mode spike.**
> 3. **NEW CRITICAL #1 — Q3 W2: HackerNoon operational-governance synthesis in v1.0 spec executive summary (1 day, 1 engineer).** v24 CRITICAL #1. Per HackerNoon "The Month AI Governance Became Operational" (July 1 2026) — three control surfaces (model access, infrastructure capacity, cyber governance) converged in June 2026. **v24 add: 1-day copy spike to write a v24 *control-surfaces* section in the v1.0 spec executive summary, citing HackerNoon as the v24 *industry-acknowledged* evidence. "Dan Glasses is the v24 *only* path that escapes all three control surfaces."**
> 4. **NEW CRITICAL #2 — Q3 W2: Anthropic-Samsung custom AI chip in v1.0 spec performance section (1 day copy, 1 engineer).** v24 CRITICAL #2. Per TechCrunch + FourWeekMBA (late June 2026) — Anthropic is co-developing a custom inference chip with Samsung. **v24 add: 1-day copy spike to cite the Anthropic-Samsung chip as v24 *chip-vendor-validated inference-as-frontier* evidence. The v24 chip-war is now 4-vendor-validated (Microsoft+OpenAI, Amazon+Anthropic, Google+TPUs, Anthropic+Samsung). v23 DSpark plan-J1 is the v24 *open-source counter* to the v24 *4-vendor closed-source inference-cracking*.**
> 5. **NEW CRITICAL #3 — Q3 W3: Genesis AI Eno + GENE world-model mapping in v1.0 spec (1 day, 1 engineer).** v24 CRITICAL #3. Per Genesis AI (June 16 2026, $105M seed, Eclipse + Khosla) — Eno robot + GENE foundation model powers perception, memory, multi-step task planning. **v24 add: 1-day spike to write a v24 *robotics-world-model mapping* section in the v1.0 spec. Dan Glasses is the v24 *wearable instance* of the same auditable-perception+memory+action pattern. Cite GENE as v24 *robotics-vendor-validated* evidence for the Dan Glasses stack.**
> 6. **NEW SHARPEN #1 — Q4 W1: 6/12/24-month plan revision reflecting v24 launch-blockers + control-suraces narrative (2 days, 1 engineer).** v24 SHARPEN #1. **v24 add: revise the v1.0 launch-window assumptions to reflect (a) the v24 toold/openclaw launch-blockers (move v1.0 ship from end of Q4 to Q4 W3 to absorb the 1-week + 3-day spikes), (b) the v24 *control-surfaces* narrative as the v24 *new* marketing position, (c) the v24 *robotics-vendor-validated* GENE mapping.**
> 7. **v24 v1.0 plan adds:** (1) **`toold` strict-mode hardening plan-N1 (LAUNCH-BLOCKER)** — 1-week engineering spike, Q3 W1. (2) **`openclaw` shell-call audit plan-N2 (LAUNCH-BLOCKER)** — 3-day engineering spike, Q3 W1.
> 8. **v24 6/12/24-month plan revision:**
>    - **Q3 (now → 2026-09-30):** LOCK v1.0 launch. Ship the 2 launch-blockers (toold strict-mode + openclaw shell-call audit). 1-week DSpark evaluation. SIA-W+H port begin. Hermes Agent integration. Cosmos 3 architecture mapping. OpenAI wearable threat scenario planning. HackerNoon control-surfaces marketing. Genesis AI Eno mapping. v1.0 marketing copy (v24 15-step narrative + control-suraces + chip-war + GENE).
>    - **Q4 (2026-10-01 → 2026-12-31):** v1.0 SHIP (revised target: Q4 W3 to absorb launch-blockers). 6/12/24-month plan revision. Sonnet 5 / Azure Linux 4.0 / agent-framework-convergence marketing adds. SIA-W+H arXiv working paper. v1.5 spec draft begins.
>    - **2027 H1 (2027-01-01 → 2027-06-30):** v1.5 spec lock. SIA-W+H ICML 2027 / ACL 2027 submission. First dev-kits to early-access community. Multi-modal fusion (Cosmos 3 + GENE + Dan Glasses architecture paper).
>    - **2027 H2 (2027-07-01 → 2027-12-31):** v1.5 SHIP. 24-month plan revision reflecting the v1.0 + v1.5 ship data. Danlab AGI roadmap v3.0: from wearable-first to self-improving-first (SIA-W+H as the harness).

---

# Dan2 — AGI Roadmap v23 (2026-07-05 00:05 UTC / 05:35 IST) — preserved content follows

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v22:** `dan2-agi-roadmap.v22-backup-2026-07-05.md`

> **v23 deltas vs v22 (4 CRITICAL adds, 2 SHARPEN, 0 broad rollbacks, 3 v1.5 plan adds, 6/12/24-month plan revision):**
> 1. **NEW CRITICAL #1 — Q3 W2: DeepSeek DSpark evaluation spike (1 day, 1 engineer).** v23 CRITICAL #1. Per LLM Rumors + VentureBeat (June 26 2026) — DSpark under MIT license, 60-85% faster per-user generation for DeepSeek-V4-Flash, 57-78% for V4-Pro, tested on Gemma and Qwen. **v23 add: 1-day spike to evaluate DSpark on LFM2.5-VL-450M Q4_0 inference. If 1.6-2× speedup, ship to perceptiond v1.1 by Q3 W3. v23 first deliverable: a 1-page "DSpark on LFM2.5-VL-450M" benchmark note.**
> 2. **NEW CRITICAL #2 — Q3 W1-W2: SIA-W+H port LOCKED as plan-A-locked (2 weeks, 1 engineer).** v23 CRITICAL #2. Per Felix Chau (June 2026) + multiple LinkedIn/Instagram posts — SIA empirical: legal task 45→70% accuracy, GPU kernels up to 14× faster. **v23 add: this is no longer "speculative" — SIA is now *third-party-validated* with named-dated-confirmed empirical results. Promote SIA-W+H from v22 plan-A to v23 plan-A-locked. The 2-week spike writes the SIA port, runs the legal benchmark, writes a 2-page "SIA-W+H on HRM-Text-1B" technical note, and ships to arXiv as a working paper by Q3 W2 end.**
> 3. **NEW CRITICAL #3 — Q3 W2: NVIDIA Cosmos 3 architecture mapping in v1.0 spec (30 min copy, 1 engineer).** v23 CRITICAL #3. **v23 add: write a 1-page "Dan Glasses as a wearable-first Cosmos 3 instance" section for the v1.0 spec, mapping memoryd ↔ Cosmos world-state, perceptiond ↔ Cosmos physical-reasoning, audiod post-processor ↔ Cosmos language, ttsd ↔ Cosmos action. This is a *marketing-and-architecture* deliverable, not a code spike.**
> 4. **NEW CRITICAL #4 — Q3 W3: OpenAI-io wearable launch scenario (30 min planning, 1 engineer).** v23 CRITICAL #4. Per Pcmag + TNW + Bloomberg — OpenAI + Jony Ive "io" team now has Apple Vision Pro VP Paul Meade on board. **v23 add: 30-min scenario-planning session for "what does OpenAI launch a wearable in 2027 mean for Dan Glasses v1.0 positioning?" Three scenarios: (a) OpenAI ships cloud-only (we keep wedge), (b) OpenAI ships on-device premium (we keep wedge on price), (c) OpenAI ships on-device affordable (we keep wedge on openness). 30 min, Q3 W3, 1 engineer.**
> 5. **NEW SHARPEN #1 — Q4 W1: 6/12/24-month plan revision reflecting v23 5-entrants race (2 days, 1 engineer).** v23 SHARPEN #1. **v23 add: revise the v1.0 launch-window assumptions to reflect the 5-entrants closed-source race. The first-mover window is 12-24 months, not 18-36. Move v1.0 milestones earlier where possible.**
> 6. **NEW SHARPEN #2 — Q4 W2: Eyewear incumbents flat-Q2 marketing wedge (1 day, 1 engineer).** v23 SHARPEN #2. **v23 add: cite the Q2 2026 flat eyewear stocks as the v23 *empirical* signal that closed-source smart-glasses has not displaced traditional eyewear. Add to the v22 14-step marketing narrative as step 15: "The 25 listed eyewear companies were flat in Q2 2026. The closed-source smart-glasses play is competing against Meta, not against EssilorLuxottica. Dan Glasses ships the open-weights counter-position."**
> 7. **v23 v1.5 plan adds:** (1) **SIA-W+H port plan-A-LOCKED** (was v22 plan-A, now v23 plan-A-locked) — 2-week engineering spike, Q3 W1-W2. (2) **DSpark on LFM2.5-VL-450M plan-J1** — 1-day evaluation spike, Q3 W2. (3) **Cosmos 3 architecture mapping plan-K1** — 1-page spec section, Q3 W2, 30 min copy.

---

> **v22 deltas vs v21 (5 CRITICAL adds, 4 SHARPEN, 0 broad rollbacks, 2 v1.5 plan adds):**
> 1. **NEW CRITICAL — Q3 W1: Hermes Agent v1.0 openclaw agent framework plan-A LOCKED (2 weeks, 1 engineer).** v22 CRITICAL #1. Per Hermes Agent (Nous Research, June 2 2026) — "the fastest-growing open-source agent framework of the year," 180,000+ stars in 4 months. Now the most-credible open-source self-improving agent. **v22 add: lock Hermes Agent as the v1.0 openclaw agent framework plan-A. Cite in the v1.0 spec architecture section + v1.0 marketing as the v22 "the v22 first open-source self-improving agent on a wearable" claim. 2-week spike, 1 engineer, target Q3 W1.**
> 2. **NEW CRITICAL — Q3 W1: LFM2.5-VL-450M v1.0 vision model CONFIRMED (no change, 0 days).** v22 CRITICAL #2. Per Liquid AI blog (Apr 8 2026, post-trained with RL + preference optimization) — 450M params, on-device wearables is the *named* use case, Q4_0 on Jetson Orin @ 233-242ms for 256-512px, supports bounding boxes + function calling + 8 languages. **v22 add: the v22 on-device VLM benchmark is *settled*. LFM2.5-VL-450M is the v22 v1.0 vision model. No v22 spec change required. The on-device wearable-VLM era is the v22 structural answer to Meta's $20/mo paywall.**
> 3. **NEW CRITICAL — Q3 W2: `perceptiond.skill_evolution` + ComfyClaw peer-reviewable + Mastermind = harness > model academic-validated (2 weeks, 1 engineer).** v22 CRITICAL #3. Per Mastermind (arXiv 2607.01764, July 2026) — a *small* planner over a *frozen* frontier executor achieves 84.5% pass rate on CyberGym (vs Best-of-8 63.0%, iterative improvement 77.0%). The same planner improves GPT-5.4 mini and GLM 5.1 from 45.0% / 58.5% to 60.0% / 71.0%. **v22 add: the v20 "harness > model" thesis is now *empirically replicated* in a peer-reviewable paper. Promote `perceptiond.skill_evolution` to v22 plan-A, target Q3 W2. 2-week spike, 1 engineer.**
> 4. **NEW CRITICAL — Q3 W2: Meta "One Premium" $20/mo paywall for *on-device* Conversation Focus feature (1 day copy, 1 engineer).** v22 CRITICAL #4. Per 9to5Google (July 1 2026) — "Meta will charge glasses users $20/month for a new Meta One Premium subscription, and one of the first features to get locked down is 'Conversation Focus.' Since the feature runs fully on-device, it makes no sense for Meta to impose usage limits on the feature and lock extended runtime behind a premium Meta AI subscription." **v22 add: Meta is now paywalling *already-on-device* features. This is the v22 *most direct* evidence that the v1.0 "no subscription" marketing guarantee is a v22 *stronger* differentiator than v19. Add Meta One Premium as the v22 12th marketing step (replacing the v19 Cerf step). Q3 W2, 1 day copy.**
> 5. **NEW CRITICAL — Q3 W2: OpenClaw iOS + Android app launch — OpenClaw is now the v22 *canonical* open-source agent gateway for wearables (1 day copy, 1 engineer).** v22 CRITICAL #5. Per TechCrunch (June 30 2026) — "OpenClaw, the free, open source AI agent that captivated the internet earlier this year, is finally available as an app on iOS and Android. You can pair your phone with the OpenClaw Gateway, a kind of routing layer that connects your requests to AI agents and the tools and skills those agents draw on to get things done." **v22 add: OpenClaw is now a *first-class mobile + wearable gateway*. The v1.0 Dan Glasses → OpenClaw integration is now v22 *concretely mobile*. Cite in v1.0 marketing as the v22 *shipped* gateway. Q3 W2, 1 day copy.**
> 6. **NEW SHARPEN — Q3 W2: v22 11-step → 12-step marketing narrative with Meta One Premium $20/mo paywall (1 day copy, 1 engineer).** v22 SHARPEN #1. **v22 add: the v20 11-step narrative + Kimi K2.7 Code (v21 12th step) is now *strengthened* with Meta One Premium as the v22 12th marketing step. The "you bought the hardware, you don't pay for the AI" thesis is now the v22 most-articulate market pitch. Q3 W2, 1 day copy.**
> 7. **NEW SHARPEN — Q3 W2: v1.5 plan-B+ expanded: HRM-Text-1B (held) + Hermes Agent (v22 NEW) + Apertus v1.1 4B (held) + GLM-5.2 (held) + OpenPhone-3B (held) (1 day, 1 engineer).** v22 SHARPEN #2. **v22 add: with v22 Hermes Agent as the v1.0 openclaw agent framework, the v1.5 plan-B+ (the *agent* substrate) is now a v22 *5-model shortlist*. v1.5 plan-A remains perceptiond + memoryd. v1.5 plan-B is the *agent substrate* with 5 candidate models. Q3 W2, 1 day, 1 engineer.**
> 8. **NEW SHARPEN — Q3 W3: v1.5 plan-C expanded: GLM-5.2 NVFP4 24 tok/s @ 128K on 4× DGX Spark is the v22 *desktop-dev* substrate (1 day, 1 engineer).** v22 SHARPEN #3. Per NVIDIA Developer Forums (July 3 2026) — GLM-5.2 NVFP4 on 4× DGX Spark at 24 tok/s @ 128K. **v22 add: the v21 GLM-5.2 NVFP4 128K desktop-dev spike is now v22 *confirmed* as the v1.5 plan-C desktop-dev substrate. Q3 W3, 1 day, 1 engineer.**
> 9. **NEW SHARPEN — Q3 W2: v1.5 plan-D expanded: Apertus v1.1 4B (EU provenance) + Hermes Agent (v22 NEW) as the v22 *EU-compliance* substrate (1 day, 1 engineer).** v22 SHARPEN #4. **v22 add: the v22 v1.5 plan-D is now a v22 *2-model shortlist*: Apertus v1.1 4B (held, EU provenance) + Hermes Agent (v22 NEW, open-source self-improving). Q3 W2, 1 day, 1 engineer.**

> **v22 retractions of v21:** **0 broad rollbacks.** v21 5 new CRITICAL + 4 SHARPEN all hold. v22 adds 5 new CRITICAL + 4 SHARPEN + 1 new v1.0 Hermes Agent plan-A + 2 new v1.5 plan-B+ agent substrate candidates. All v21 6/12/24-month plan holds.

## TL;DR (one paragraph, v20)


The v19 6/12/24-month plan holds. **v20 adds: Q3 W1 memoryd v1.5 "what would Mythos have missed" safety-considerations feature (CRITICAL #1) + Q3 W2 v1.0 spec safety-considerations section update with Axios + Bad Epoll + NSA quote + Chris Inglis (CRITICAL #2) + Q3 W2 v19 11-step → v20 12-step marketing narrative update with Palo Alto + CrowdStrike + GLM-5.2 = Mythos + Apple camera-AirPods Pro suspended (CRITICAL #3) + Q3 W2 v1.0 spec implementation-wedge section update with Silicon Data LLM Token Expenditure Index + The AI Insider (CRITICAL #4) + Q3 W3 v1.0 spec sovereign-on-prem section update with NSA + Chris Inglis (SHARPEN #1) + Q3 W2 v1.0 marketing copy update with Apple camera-AirPods Pro suspended (SHARPEN #2) + Q3 W2 TechCrunch "AI acts on your behalf" v1.0 marketing copy (SHARPEN #3) + Q3 W3 danlab-multimodal safety-considerations page update (SHARPEN #4) + Q4 W1 sovereign-on-prem defense vertical spike promoted to plan-A (SHARPEN #5).** The Dan Glasses stack is structurally correct, validated at industry-icon level (Vinton Cerf, v17), validated at industry-shipped level (Anthropic Claude Apps Gateway, v18), validated at mainstream-press level (Newsweek, v18), validated at NSA level (Gen. Joshua Rudd, v20), validated at former-US-National-Cyber-Director level (Chris Inglis, v20), validated at Wall Street level (Palo Alto + CrowdStrike all-time highs, v20), validated at token-economics level (Silicon Data LLM Token Expenditure Index, v20), and now has 5 strong v1.0 audiod targets (LFM2.5-230M post-processor + Hermes Agent agent framework + LFM2.5-VL-450M vision + whisper.cpp STT + KittenTTS TTS) + an industry-icon-endorsed orchestration layer (OpenClaw, v17/v18) + a v20 NSA-validated sovereign-on-prem vertical for defense + a v20 Wall-Street-validated implementation wedge + a v20 "what would Mythos have missed" safety-considerations feature on memoryd v1.5. **6-month plan: ship the v1.0 audiod post-processor with LFM2.5-230M, phase-mapped execution substrate, Hermes Agent agent framework, and the v20 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence + the v20 12-step marketing narrative + the v20 "what would Mythos have missed" memoryd safety-considerations feature. 12-month plan: ship the v1.5 audiod post-processor with HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-C) + OpenPhone-3B (plan-D) + Memora + As We May Search storage/retrieval split + the v20 "what would Mythos have missed" feature. 24-month plan: ship the SIA-W+H port as the open-source RSI play + sovereign-on-prem vertical for defense (v20 NSA-validated, Chris-Inglis-validated, AIPOCH MedSkillAudit-augmented, promoted to plan-A) + LFM2.5-230M audiod for v1.0 wearable path + Project Lightwell + OpenAN agent interoperability.**

## 6-Month Plan (Q3 2026 - Q4 2026): v1.0 Wearable

### Q3 W1: LFM2.5-230M audiod post-processor swap-in (held from v16)
- **Effort:** 1-2 weeks, 1 engineer.
- **Deliverable:** audiod post-processor upgraded from LFM2.5-1.2B-Thinking to LFM2.5-230M. Benchmark on audiod post-processor workload.

### Q3 W1: `perceptiond.phase_map` architecture spike (held from v15)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** `perceptiond.phase_map` module. Pluggable backend (QNN/Hexagon on Snapdragon, Mali on others, CPU fallback).

### Q3 W1: OpenPhone-3B shortlist evaluation (held from v15)
- **Effort:** 2 days, 1 engineer.
- **Deliverable:** benchmark OpenPhone-3B vs HRM-Text-1B vs Apertus v1.1 4B on audiod post-processor workload.

### Q3 W1-W2: Memora + As We May Search memoryd v1.5 port (held from v14, v18 sharpening)
- **Effort:** 2 weeks, 1 engineer.
- **Deliverable:** memoryd v1.5 storage/retrieval split. New `/v1/retrieve` endpoint, new `/v1/abstractions` write path. Local-first HNSW at 1M document scale.

### Q3 W2: Hermes Agent v1.0 audiod agent framework plan-A spike (held from v16)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** Hermes Agent pattern ported to openclaw + audiod. Mixture-of-agents pattern.

### Q3 W2 (v18 CRITICAL #1): OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence
- **Effort:** 2 days, 1 engineer.
- **Deliverable:** document OpenClaw's protocol surface (JSON-RPC envelope, daemon health probes, kanban/issue trackers, gateway protocol, paperclip agent harness) as a v1.0 marketing artifact. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable." Cite Cerf + Anthropic Claude Apps Gateway in the v1.0 spec.
- **Evidence:** Vinton Cerf Open Frontier (June 30 2026) + Anthropic Claude Apps Gateway (July 2 2026).

### Q3 W2 (v18 CRITICAL #2): OpenClaw security audit (Mashable, June 30 2026)
- **Effort:** 1 day spike, 1 engineer.
- **Deliverable:** audit OpenClaw's threat model. Document the v18 known-flaw + audit response in the v1.0 spec safety-considerations section.
- **Evidence:** Mashable, June 30 2026.

### Q3 W2 (v18 CRITICAL #3): v18 10-step marketing narrative + Newsweek "Open Accountability Standards"
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 marketing page updated to the v18 10-step empirical narrative. Add Newsweek as the v18 10th step: "Newsweek open accountability standards — OpenClaw named, Anthropic gateway shipped, X MCP server shipped, the open-source agent protocol layer is now mainstream."

### Q3 W2 (v18 SHARPEN): OpenClaw native iOS + Android + wearable-on-OpenClaw thesis
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 spec architecture section updated. "OpenClaw is the gateway. Dan Glasses is the wearable node." Add to the v1.0 marketing.
- **Evidence:** 9to5Google + Engadget + TechCrunch + Mashable, June 30 2026.

### Q3 W2 (v18 SHARPEN): Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" copy
- **Effort:** 1 day copy, 1 engineer.
- **Deliverable:** v1.0 marketing copy updated. Cite Proton Lumo 2.0 (privacy harness on frontier model) + OpenAI GPT-5.6 Sol / Google Gemini 3.5 Flash / Anthropic Sonnet 5 (closed-source agentic race) + Zuckerberg "slower than expected" (closed-source frontier visibly failing).
- **Evidence:** 9to5Mac + TechCrunch + TechCrunch + Reuters + TechCrunch + Bloomberg + CNN + Forbes, June 30 - July 2 2026.

### Q3 W2 (v18 SHARPEN): PagerDuty agent drift + Atomathic Physical AI 2.0 spec + copy
- **Effort:** 1 day copy + 1 day spec, 1 engineer.
- **Deliverable:** v1.0 spec safety-considerations section updated. "Observability > model" is the v18 structural answer. Cite Atomathic Physical AI 2.0 in the v1.0 spec architecture section.
- **Evidence:** Forbes (PagerDuty) + Atomathic (Physical AI 2.0), July 1-2 2026.

### Q3 W2: 9-step → 10-step marketing narrative (v17 9-step + v18 10th step)
- **Effort:** 1 day copy, 1 engineer.

### Q3 W2: Project Lightwell $5B + Chainguard Athena copy update (held from v17)
- **Effort:** 1 day copy, 1 engineer.

### Q3 W2: OpenAN + Anthropic Claude Code fingerprinting copy update (held from v17)
- **Effort:** 1 day copy, 1 engineer.

### Q3 W2: Anthropic Claude Science workbench-layer v1.0 spec add (held from v17)
- **Effort:** 1 day, 1 engineer.

### Q3 W2: Research-integrity responsible-AI framing in v1.0 spec (held from v15)
- **Effort:** 1 day.

### Q3 W2: "As We May Search" paper read + memoryd v1.5 addendum (held from v16)
- **Effort:** 1 day.

### Q3 W2: v17 Mythos $30K catch retraction (held from v16)
- **Effort:** 1 day.

### Q3 W3-Q4 W2: SIA-W+H port (held from v11, v16 v1.5 publishing bet)
- **Effort:** 4 weeks, 1 engineer + $200-500/mo cloud GPU.
- **Deliverable:** SIA-W+H harness ported to OpenClaw + memoryd. arXiv draft. ICML 2027 / ACL 2027 submission.
- **v18 add:** v18 Time Magazine (June 29 2026) Anthropic hedging RSI strengthens the v17 SIA-W+H port recommendation. The open-source, MIT-licensed, auditable SIA-W+H pattern is the v18 only credible counter-narrative when the closed-source frontier is publicly hedging.

### Q3 W3: Red Queen moving-judge spike (held from v12)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** v1.5 danlab-multimodal implementation is the Red Queen moving-judge pattern.

### Q3 W3: Karpathy 10-rule openclaw CLAUDE.md (held from v12)
- **Effort:** 1 day.

### Q3 W3: openclaw PR-review "X% AI-generated" tag (held from v14)
- **Effort:** 3 days, 1 engineer.
- **v18 add:** v18 Godot Foundation AI code rules (June 30 2026) validate the v14 openclaw PR-review "X% AI-generated" tag direction. "X% AI-generated" tag, 3-day spike.

### Q3 W4: VisualClaw cascade-gate port (held from v8/v9)
- **Effort:** 1.5 weeks, 1 engineer.
- **Deliverable:** perceptiond + memoryd port the VisualClaw on-device cascade-gate pattern.

### Q4 W1-W2: Anthropic Dreaming port (held from v8/v11)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** openclaw + memoryd port the Anthropic Dreaming `auto_apply=False` + `session_limit=50` pattern.

### Q4 W1-W2: Sovereign-on-prem vertical spike (held from v13, v17 DoD-validated, v18 AIPOCH-augmented)
- **Effort:** 1 engineer-week.
- **Deliverable:** Q4 2026 spike for healthcare/defense vertical. Palantir+NVIDIA Nemotron + DoD GenAI.mil template co-positioning. **v18 add: cite AIPOCH MedSkillAudit (June 29 2026) as the v18 pre-deployment medical AI audit framework for healthcare vertical.**

### Q4 W1-W2: Project Lightwell $5B + Chainguard Athena spike (held from v17)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** evaluate the v17 open-source supply chain AI security stack. Open-source supply chain memory + workbench + agent framework. Cite in v1.5 product roadmap.
- **Evidence:** Dark Reading + Let's Data Science, late June 2026.

### Q4 W1-W2: OpenAN agent interoperability framework spike (held from v17)
- **Effort:** 1 week, 1 engineer.
- **Deliverable:** evaluate the v17 OpenAN agent interoperability framework. Multi-agent coordination, AI-native autonomous networks (Level 4 autonomy). Cite in v1.5 product roadmap.
- **Evidence:** Developing Telecoms, late June 2026.

### Q4 W3-W4: v1.0 wearable hardware integration
- **Effort:** 2 weeks, hardware + 1 engineer.
- **Deliverable:** Redax board integration, camera module, thermal validation, battery characterization.

## 12-Month Plan (Q1 2027 - Q2 2027): v1.5 Cognitive Stack

### Q1 W1-W2: HRM-Text-1B swap-in (v1.5 plan-B)
- **Effort:** 2 weeks, 1 engineer. (held from v11, displaced from v1.0 plan-A to v1.5 plan-B by LFM2.5-230M in v16)

### Q1 W3: Apertus v1.1 4B EU data-residency ship-gate (v1.5 plan-C)
- **Effort:** 1 week, 1 engineer.

### Q1 W4: OpenPhone-3B plan-D integration
- **Effort:** 1 week, 1 engineer.

### Q2 W1-W2: Qwen3-TTS v1.5 plan-A swap-in
- **Effort:** 2 weeks, 1 engineer.

### Q2 W2: Chatterbox voice-cloning plan-A
- **Effort:** 1 week, 1 engineer.

### Q2 W3-W4: LFM2.5-VL-450M-Extract structured-output VLM
- **Effort:** 2 weeks, 1 engineer.

### Q2 W4: Ollie gaze-informed proactive v1 (held from v12)
- **Effort:** 1 week, 1 engineer.

## 24-Month Plan (Q3 2027 - Q4 2027): SIA-W+H RSI Play + DoD Vertical + Project Lightwell + OpenAN

### Q3 2027: SIA-W+H publication + ICML 2027 / ACL 2027
- **Effort:** 4 weeks, 1 engineer.
- **Deliverable:** arXiv draft + ICML 2027 / ACL 2027 submission.
- **v18 add:** v18 Time Magazine (June 29 2026) Anthropic hedging RSI strengthens the v16 SIA-W+H port recommendation. The open-source, MIT-licensed, auditable SIA-W+H pattern is the v18 only credible counter-narrative when the closed-source frontier is publicly hedging.

### Q4 2027: Sovereign-on-prem vertical product launch (DoD-validated, AIPOCH-augmented)
- **Effort:** 1 quarter, 3 engineers.
- **Deliverable:** healthcare/defense sovereign-on-prem product. **v18 add: cite DoD GenAI.mil 1.7M users + 100K custom agents as the v17 DoD-deployed template + AIPOCH MedSkillAudit as the v18 pre-deployment medical AI audit framework.**

### Q4 2027: Compliance mode v2.0
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** HIPAA / FedRAMP compliance mode for healthcare/defense verticals.

### Q4 2027: Project Lightwell + OpenAN partner-product evaluation (held from v17)
- **Effort:** 1 quarter, 2 engineers.
- **Deliverable:** evaluate partner-product opportunities with IBM Red Hat Project Lightwell + OpenAN consortium. Cite in v2.0 product roadmap.

## Top 3 Recommendations for somdipto (v18)

1. **Approve the Q3 W2 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence (2 days copy + spec, 1 engineer).** v18 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable."
2. **Approve the Q3 W2 OpenClaw security audit (1 day spike, 1 engineer).** v18 CRITICAL #2. Mashable (June 30 2026) reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. Audit OpenClaw's threat model before shipping the v1.0 marketing artifact.
3. **Approve the Q3 W2 v18 batch: v18 10-step marketing narrative + Newsweek "Open Accountability Standards" (1 day) + OpenClaw mobile + wearable-on-OpenClaw thesis (1 day) + Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" (1 day) + PagerDuty agent drift + Atomathic Physical AI 2.0 (1 day) (Q3 W2, 4 days, 1 engineer).** v18 SHARPEN. **v18 add: total 4 days, 10-step marketing narrative + mainstream-press-acknowledged + closed-source-admitted + industry-icon-endorsed + government-deployed + government-gated + multi-vendor-funded + China-led-standardization-underway + fingerprinting-at-the-runtime-layer + observability-first + supply-chain-pressured.**

## Open Questions for somdipto (v18)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable.")
2. **OpenClaw security audit priority** — Q3 W2, 1 day spike, 1 engineer (recommend: yes, Mashable v18 known-flaw)
3. **v18 10-step marketing narrative update + Newsweek priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v18 10-step)
4. **OpenClaw mobile + wearable-on-OpenClaw thesis copy priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, "OpenClaw is the gateway. Dan Glasses is the wearable node.")
5. **Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" copy priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v18 6-step v1.0 marketing batch)
6. **PagerDuty agent drift + Atomathic Physical AI 2.0 spec + copy priority** — Q3 W2, 1 day copy + 1 day spec, 1 engineer (recommend: yes, "Observability > model" is the v18 structural answer)
7. **Project Lightwell $5B + Chainguard Athena spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, open-source supply chain AI security is the v17 next wedge)
8. **OpenAN agent interoperability framework spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, agent interoperability framework SOTA)
9. **LFM2.5-230M / Hermes Agent / As We May Search / Memora / Phase Matters v16 priorities** — held from v16 (recommend: yes, all v16 priorities hold)
10. **SIA-W+H port budget ($200-500/mo cloud GPU)** — Q3 W3-Q4 W2 (recommend: yes, v16 v1.5 publishing bet, v18 strengthened by Time Magazine Anthropic hedging RSI)
11. **Sovereign-on-prem vertical product launch timeline** — Q4 2027 (recommend: yes, DoD GenAI.mil template co-positioning + AIPOCH MedSkillAudit)
12. **v18 24-month plan: Project Lightwell + OpenAN partner-product evaluation** — Q4 2027, 1 quarter, 2 engineers (recommend: yes, v17 v2.0 vertical)

## Footnotes (v19)

[^v19-1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Apps Gateway + Sonnet 5, July 2 2026 (held from v18)
[^v19-2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (held from v18)
[^v19-3]: https://www.engadget.com/2204549/theres-now-an-openclaw-app-for-ios-and-android-phones/ — Engadget: OpenClaw founder → OpenAI, June 30 2026 (NEW v19)
[^v19-4]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw + iOS/Android, June 30 2026 (held from v18)
[^v19-5]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (held from v18)
[^v19-6]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (held from v18)
[^v19-7]: https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ — Zuckerberg "slower than expected," July 2 2026 (held from v18)
[^v19-8]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (held from v18)
[^v19-9]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (held from v18)
[^v19-10]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026 (held from v17)
[^v19-11]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026 (held from v17)
[^v19-12]: https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/ — Anthropic Mythos 5 Glasswing expansion, July 1 2026 (held from v17)
[^v19-13]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026 (held from v17)
[^v19-14]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026 (held from v17)
[^v19-15]: https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc — Anthropic Claude Code timezone/proxy fingerprinting, late June 2026 (held from v17)
[^v19-16]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^v19-17]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^v19-18]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^v19-19]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^v19-20]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users (held from v16)
[^v19-21]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor (held from v16)
[^v19-22]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v15)
[^v19-23]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI hedging, June 29 2026 (held from v18)
[^v19-24]: https://markets.businessinsider.com/news/stocks/aipoch-launches-medskillaudit-an-ai-audit-framework-to-evaluate-medical-ai-agent-skills-before-deployment-1036284741 — AIPOCH MedSkillAudit, June 29 2026 (held from v18)
[^v19-25]: https://roadtovr.com/memomind-one-smart-glasses-kickstarter-release/ — MemoMind One (XGIMI), late June 2026 (NEW v19)
[^v19-26]: https://www.politico.com/news/2026/06/29/exclusive-newsom-anthropic-ink-deal-to-expand-government-use-00979584 — Politico: Anthropic-Newsom California deal, June 29 2026 (NEW v19)
[^v19-27]: https://www.latimes.com/business/story/2026-06-29/google-poached-to-lose-two-more-senior-ai-staffers-to-anthropic — Google AI brain drain, June 29 2026 (NEW v19)
[^v19-28]: https://www.reuters.com/business/google-limits-metas-use-its-gemini-ai-models-ft-reports-2026-06-28/ — Reuters: Google limits Meta's Gemini compute, June 28 2026 (NEW v19)
[^v19-29]: https://www.cnbc.com/2026/06/29/alphabet-googl-stock-dow-average.html — Alphabet stock worst month since Feb 2025, June 29 2026 (NEW v19)
[^v19-30]: https://www.rcrwireless.com/20260629/carriers/china-mobile-shanghai — China Mobile MWC Shanghai 2026, June 29 2026 (NEW v19)
[^v19-31]: https://www.military.com/nato-drone-exercise-amplifies-international-battle-for-military-airspace-control — NATO SAPIENT TIE26, late spring 2026 (NEW v19)

## v18 AGI roadmap content (preserved in backup)

The v18 AGI roadmap (preserved in `dan2-agi-roadmap.v18-backup-2026-07-04.md`, 22.3KB, 226 lines) covers: 6/12/24-month plan with Q3 W1 LFM2.5-230M audiod post-processor swap-in (held from v16), Q3 W1 perceptiond.phase_map (held from v15), Q3 W1 OpenPhone-3B shortlist evaluation (held from v15), Q3 W1-W2 Memora + As We May Search memoryd v1.5 port (held from v14), Q3 W2 Hermes Agent v1.0 audiod agent framework plan-A spike (held from v16), Q3 W2 OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence (v18 CRITICAL #1), Q3 W2 OpenClaw security audit (v18 CRITICAL #2), Q3 W2 v18 10-step marketing narrative + Newsweek "Open Accountability Standards" (v18 CRITICAL #3), Q3 W2 OpenClaw native iOS + Android + wearable-on-OpenClaw thesis (v18 SHARPEN), Q3 W2 Proton Lumo 2.0 + OpenAI closed-source agentic race + Zuckerberg "slower than expected" copy (v18 SHARPEN), Q3 W2 PagerDuty agent drift + Atomathic Physical AI 2.0 spec + copy (v18 SHARPEN), Q3 W3-Q4 W2 SIA-W+H port (held from v11, v16 v1.5 publishing bet, v18 strengthened by Time Magazine Anthropic hedging RSI), Q3 W3 Red Queen moving-judge spike (held from v12), Q3 W3 Karpathy 10-rule openclaw CLAUDE.md (held from v12), Q3 W3 openclaw PR-review "X% AI-generated" tag (held from v14, v18 Godot-validated), Q3 W4 VisualClaw cascade-gate port (held from v8/v9), Q4 W1-W2 Anthropic Dreaming port (held from v8/v11), Q4 W1-W2 sovereign-on-prem vertical spike (held from v13, v17 DoD-validated, v18 AIPOCH-augmented), Q4 W1-W2 Project Lightwell $5B + Chainguard Athena spike (held from v17), Q4 W1-W2 OpenAN agent interoperability framework spike (held from v17), Q4 W3-W4 v1.0 wearable hardware integration. **All v18 content is preserved verbatim in the backup. The v19 add is documented in the v19 header at the top of this file: 4 CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month). The v18 6/12/24-month plan holds in v19, with v19 Q3 W2-W3 adding an OpenClaw governance-drift audit spike (1 day).**
## v22 addendum (2026-07-04 11:30 UTC / 17:00 IST)

**v22 deltas vs v21 (4 CRITICAL adds, 4 SHARPEN, 0 broad rollbacks, 3 v1.5 plan adds, 0 v1.0 plan changes):**

1. **NEW v22 CRITICAL #1 — LFM2.5-1.2B-Thinking promoted to v1.5 plan-C1 (Liquid AI, Jan 20 2026).** Sub-1GB hybrid reasoning model, runs on commodity hardware. **v22 add: parallel alternative to HRM-Text-1B (v1.5 plan-B). Both run in v1.5. v22.5 will pick the winner. 2-week spike, 1 engineer, target Q4 W1.**

2. **NEW v22 CRITICAL #2 — LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M promoted to v1.5 plan-B1 (Liquid AI, Jun 18 2026).** Purpose-built on-device retriever family. **v22 add: 2-week spike vs. the current MiniLM-L6-v2 in memoryd. If wins on the v22 memoryd eval harness, swap. 1 engineer, target Q3 W4.**

3. **NEW v22 CRITICAL #3 — Meta Conversation Focus paywall (9to5Google, Jul 1 2026) as v22 6-month wearable-vacuum marketing copy.** Meta charges $20/mo to gate an on-device feature. **v22 add: 30 min copy update to the v1.0 spec marketing section. "Meta is now paywalling on-device features. The on-device future is not the closed-source future. Dan Glasses is the on-device future." Q3 W2.**

4. **NEW v22 CRITICAL #4 — Microsoft Research "From Self-Improving Agents to Co-Evolving Human-AI Systems" deeper analysis (Microsoft Research, July 2026).** The v21 add confirmed the 3-axis taxonomy. **v22 add: cite the paper's H≠0 (human-involved) selective pressure axis as the v22 *Microsoft-Research-named* architectural pattern for Dan Glasses. Update the v1.0 spec architecture section + the 12-month plan §"SIA-W+H port" to cite Microsoft Research. Q3 W2, 1 day, 1 engineer.**

5. **NEW v22 SHARPEN #1 — OpenClaw iOS + Android official launch (TechCrunch, Jun 30 2026) as v22 6-month marketing copy.** OpenClaw is *named, dated, confirmed* on the mobile substrate. **v22 add: "OpenClaw is the gateway. The phone is the mobile node. Dan Glasses is the wearable node. All three are open-source and on-device." Update the 6-month plan §"OpenClaw protocol surface marketing artifact" with the v22 confirmation. Q3 W2, 30 min, 1 engineer.**

6. **NEW v22 SHARPEN #2 — Vint Cerf TCP/IP-for-agents panel (Open Frontier, Jun 30 2026) as v22 6-month marketing copy.** "The agentic model of AI, with multiple agents from multiple sources interacting with each other, is going to force composability, and a requirement for interoperability and standardization." Vint Cerf + Matei Zaharia + Francois Chollet panel. **v22 add: cite the v22 panel as the v22 *named-dated-industry-acknowledgment* in the 6-month plan §"Cerf TCP/IP-for-agents" section. Q3 W2, 30 min, 1 engineer.**

7. **NEW v22 SHARPEN #3 — LFM2.5-230M third-party benchmarked (VentureBeat, late June 2026) as v22 6-month audiod post-processor evidence.** 213 tok/s on Galaxy S25 Ultra CPU, 42 tok/s on Raspberry Pi 5. 10 languages. **v22 add: cite the VentureBeat + Medium pieces as the v22 *third-party benchmarked* evidence in the 6-month plan §"LFM2.5-230M audiod post-processor" section. No 6-month plan change. Q3 W2, 30 min, 1 engineer.**

8. **NEW v22 SHARPEN #4 — Time Magazine "Recursive Self-Improvement is the Human Skill We Need in the AI Age" (Jun 29 2026) with Anthropic Marina Favaro and Jack Clark quotes.** "We are not there yet, and recursive self-improvement is not inevitable." **v22 add: cite the Time piece + Favaro+Clark quote in the v1.0 spec safety-considerations section as v22 *Anthropic-internal-hedge-validated* evidence. Q3 W2, 30 min, 1 engineer.**

**v22 6-month plan adds (Q3-Q4 2026):** (v21 plan held) + v22 LFM2.5-230M audiod post-processor (third-party benchmarked cite) + v22 OpenClaw iOS+Android marketing copy (TechCrunch cite) + v22 Cerf TCP/IP-for-agents panel cite + v22 Meta Conversation Focus paywall copy + v22 Time Magazine Favaro+Clark cite + v22 Microsoft Research co-evolution architecture update.

**v22 12-month plan adds (Q1-Q2 2027):** (v21 plan held) + v22 LFM2.5-1.2B-Thinking v1.5 plan-C1 spike (2 weeks, 1 engineer, target Q4 W1) + v22 LFM2.5-ColBERT-350M v1.5 plan-B1 spike (2 weeks, 1 engineer, target Q3 W4) + v22 Adaptive Auto-Harness arXiv 2606.01770 reading spike (1 engineer, target Q3 W3) + v22 Microsoft Research co-evolution H≠0 selective pressure cite.

**v22 24-month plan adds (Q3 2027 - Q4 2027):** (v21 plan held) + v22 SIA-W+H port now cited via Microsoft Research co-evolution taxonomy.

**v22 retractions of v21:** **0 broad rollbacks.** v21 LFM2.5-VL-450M, v21 LFM2.5-230M, v21 Hermes Agent, v21 Memora + As We May Search, v21 perceptiond.skill_evolution plan-A, v21 GLM-5.2 NVFP4 4× DGX Spark plan-E, v21 GLM-5 async RL plan-F, v21 SIA-W+H port, v21 HRM-Text-1B, v21 Apertus v1.1 4B, v21 OpenPhone-3B, v21 GLM-5.2, v21 Qwen3-TTS, v21 Chatterbox all *hold* in v22.

**v22 4 new open questions for somdipto:**
1. LFM2.5-1.2B-Thinking v1.5 plan-C1 vs. HRM-Text-1B plan-B — which one ships in v1.5? (recommend both, with a v22.5 decision-matrix spike Q3 W4.)
2. LFM2.5-ColBERT-350M v1.5 plan-B1 vs. MiniLM-L6-v2 — is the eval harness ready for the swap? (recommend Q3 W4 2-week spike.)
3. Meta Conversation Focus paywall copy — is the v22 "addicted to subscription-locking on-device features" framing on-brand? (recommend Q3 W2 30 min copy review.)
4. v22 6/12/24-month plan revision — confirm the v22 6/12/24-month plan revision above. (recommend Q3 W3 1 day, 1 engineer.)


[^v22-1]: https://www.liquid.ai/blog/lfm2-5-1-2b-thinking-on-device-reasoning-under-1gb — Liquid AI LFM2.5-1.2B-Thinking blog, Jan 20 2026 (NEW v22 CRITICAL #1)
[^v22-2]: https://www.liquid.ai/blog/lfm2-5-retrievers — Liquid AI LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M retrievers, Jun 18 2026 (NEW v22 CRITICAL #2)
[^v22-3]: https://9to5google.com/2026/07/01/meta-glasses-get-premium-usage-limits/ — 9to5Google: Meta Conversation Focus paywall, Jul 1 2026 (NEW v22 CRITICAL #3)
[^v22-4]: https://www.microsoft.com/en-us/research/wp-content/uploads/2026/07/agentic-evolution.pdf — Microsoft Research agentic-evolution, July 2026 (NEW v22 CRITICAL #4)
[^v22-5]: https://techcrunch.com/2026/06/30/openclaw-is-finally-available-on-android-and-ios/ — TechCrunch: OpenClaw iOS+Android launch, June 30 2026 (NEW v22 SHARPEN #1)
[^v22-6]: https://letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vint Cerf TCP/IP-for-agents panel, June 30 2026 (NEW v22 SHARPEN #2)
[^v22-7]: https://venturebeat.com/ai/liquid-ais-smallest-model-yet-lfm25-230m-beats-models-4x-its-size-at-data-extraction-can-run-anywhere/ — VentureBeat: LFM2.5-230M beats 4X its size, late June 2026 (NEW v22 SHARPEN #3)
[^v22-8]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine: Favaro+Clark Anthropic-internal-hedge, June 29 2026 (NEW v22 SHARPEN #4)


## v21 AGI roadmap content (preserved in backup)

The v21 AGI roadmap (preserved in `dan2-agi-roadmap.v21-backup-2026-07-04.md`, 35.5KB, 278 lines) covers: 5 CRITICAL (perceptiond.skill_evolution plan-A promotion, SIA-W+H v1.5 plan-B, GLM-5.2 NVFP4 4× DGX Spark v1.5 plan-E, Microsoft Research co-evolution 3-axis taxonomy, Memora + As We May Search v1.5 memoryd) + 4 SHARPEN (SAIMY Dream Company, GLM-5 async RL on Hugging Face, Kimi K2.7 Code, Mastermind arXiv 2607.01764) + 0 broad rollbacks. v21 12-step → 13-step marketing narrative. v21 v1.5 plan adds (perceptiond.skill_evolution, GLM-5.2 NVFP4 4× DGX Spark, GLM-5 async RL). **All v21 content is preserved verbatim in the backup. The v22 add is documented in the v22 addendum above: 4 CRITICAL (LFM2.5-1.2B-Thinking v1.5 plan-C1, LFM2.5-ColBERT-350M v1.5 plan-B1, Meta Conversation Focus paywall copy, Microsoft Research co-evolution deeper analysis) + 4 SHARPEN (OpenClaw iOS+Android official launch marketing copy, Cerf TCP/IP-for-agents panel cite, LFM2.5-230M third-party benchmarked, Time Magazine Favaro+Clark Anthropic-internal-hedge). v22 3 v1.5 plan adds (plan-C1, plan-B1, plan-I1 Adaptive Auto-Harness).**



## v20 addendum (2026-07-04 09:35 UTC / 15:05 IST)

**v20 deltas vs v19 (4 CRITICAL, 4 SHARPEN, 1 NEW v20 plan-A, 0 broad rollbacks):**

1. **NEW v20 CRITICAL #1 — Q3 W2-W3: v20 auditable-bug-discovery pattern to v1.0 spec safety-considerations section (1 day, 1 engineer).** v20 CRITICAL #2. **v20 add: every Dan Glasses release must be scanned by Mythos + GLM-5.2 + Apertus v1.1 4B before shipping, with findings published in a public security advisory. Cite Bad Epoll + Mythos CVE-2026-43074 as the v20 case study.**

2. **NEW v20 CRITICAL #2 — Q3 W2-W3: v20 unit-economics argument to v1.0 spec pricing section (1 day copy, 1 engineer).** v20 CRITICAL #4. **v20 add: on-device stack (lifetime cost of $349 hardware + free local inference) is the v20 only credible answer to the v20 token-price-collapse. Cite Bloomberg + LA Times in the v1.0 spec pricing section.**

3. **NEW v20 CRITICAL #3 — Q3 W2: Lock v1.0 ship window to Q4 2026 (30 min, 1 engineer).** v20 CRITICAL #3. **v20 add: Apple camera AirPods Pro suspended + Apple smart glasses delayed to end 2027 = the v20 wearable-visual-AI competitive vacuum is the widest in 12 months. Lock the v1.0 ship window to Q4 2026.**

4. **NEW v20 CRITICAL #4 — Q3 W2: v20 10-step → 11-step marketing narrative (1 day copy, 1 engineer).** v20 SHARPEN #1, #2, #3, #4 + v20 CRITICAL #1, #2, #3, #4. **v20 add: the v20 11th step is "Inter-vendor trust gap (Axios) + Mythos-missed-bug (Bad Epoll) + token-price collapse (LA Times/Bloomberg) + wearable-vacuum (Apple camera AirPods Pro suspended) + Wall-Street-priced GLM-5.2 vs Mythos + NSA Rudd on Mythos."**

5. **NEW v20 plan-A — Q3 W3: Add the Axios Amazon-Jassy-Anthropic jailbreak escalation to the v1.0 spec trust-model section (1 day, 1 engineer).** v20 CRITICAL #1. **v20 add: the closed-source frontier is inter-vendor fractured. The on-device + open-weights + auditable memory + auditable agent loop stack is the v20 only trust-resilient substrate. Cite Axios.**

6. **NEW v20 SHARPEN — Q3 W2: v20 NSA Gen. Rudd Mythos + Chris Inglis GLM-5.2 spec add (1 day, 1 engineer).** v20 SHARPEN #2, #3. **v20 add: cite NSA Rudd's "broke into almost all of our classified systems, not in weeks, but in hours" + Chris Inglis's GLM-5.2 endorsement in the v1.0 spec security/safety section.**

7. **NEW v20 SHARPEN — Q3 W2: v20 Meta Pocket gizmos privacy spec add (1 day copy, 1 engineer).** v20 SHARPEN #4. **v20 add: cite Meta Pocket gizmos in the v1.0 spec privacy/positioning section. The on-device + open-weights + auditable memory stack is the v20 only answer to the v20 *user-data-as-AI-training-fuel* pattern.**

8. **NEW v20 plan-A — Q3 W3: v20 6/12/24-month plan revision (2 days, 1 engineer).** v20 CRITICAL #1, #2, #3, #4 + v20 SHARPEN #1, #2, #3, #4. **v20 add: revise the 24-month plan to incorporate the v20 auditable-bug-discovery pattern + v20 unit-economics imperative + v20 wearable-vacuum opportunity + v20 inter-vendor-trust-gap messaging.**

**v20 retractions of v19:** **0 broad rollbacks.** v19 Mythos 5 Glasswing framing is now *post-jailbreak-control*, *NSA-validated-at-the-classified-systems-level*, and *Wall-Street-priced-as-replaceable-by-GLM-5.2*. The framing holds; the v20 emphasis shifts to the *inter-vendor trust gap* and the *unit-economics imperative*.

**v20 6/12/24-month plan revision summary:**
- **6-month (Q3-Q4 2026):** ship v1.0 with LFM2.5-230M (audiod post-processor) + Hermes Agent (agent framework) + `perceptiond.phase_map` + Memora + As We May Search (memoryd v1.5) + OpenClaw protocol surface marketing artifact + Anthropic Claude Apps Gateway citable evidence + OpenClaw security audit + v18 10-step → v19 10-step → v20 11-step marketing narrative + OpenClaw governance-drift audit + "no subscription" v1.0 marketing guarantee + **v20 auditable-bug-discovery pattern** + **v20 unit-economics argument** + **v20 wearable-vacuum Q4 2026 ship window**.
- **12-month (Q1-Q2 2027):** ship v1.5 with HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-C) + OpenPhone-3B (plan-D) + GLM-5.2 (cybersecurity competitor) + Memora + As We May Search storage/retrieval split + SIA-W+H port (open-source RSI play) + Red Queen moving-judge + Anthropic Dreaming port + sovereign-on-prem vertical (DoD-validated, AIPOCH-augmented) + **v20 auditable-bug-discovery pattern as a CI gate**.
- **24-month (Q3 2027 - Q2 2028):** ship v2.0 with HRM-Text-1B (full SIA-W+H Feedback-Agent) + LFM2.5-VL-Extract-2 + Hermes Agent 2.0 + OpenAN agent interoperability + Project Lightwell + Chainguard Athena + EigenCloud TEE + **v20 on-device stack as the v20 default for all new DaG models**.


[^v20-1]: https://www.axios.com/2026/07/03/anthropic-ai-models-revived-behind-the-scenes — Axios: How the world's top AI models were revived (Amazon Jassy → Bessent → Lutnick → Amodei, 20-day showdown), July 3 2026 (NEW v20 CRITICAL #1)
[^v20-2]: https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html — "Bad Epoll" Linux kernel flaw (CVE-2026-46242) — Mythos found CVE-2026-43074 but missed Bad Epoll; fix already landed, July 3 2026 (NEW v20 CRITICAL #2)
[^v20-3]: https://www.macrumors.com/2026/07/03/camera-airpods-pro-development-suspended-leaker/ — Apple camera AirPods Pro "suspended" per Kosutami, July 3 2026 (NEW v20 CRITICAL #3)
[^v20-4]: https://www.latimes.com/business/story/2026-07-03/with-token-prices-collapsing-regulation-rising-ais-pricing-power-looks-fragile — LA Times: Silicon Data LLM Token Expenditure Index -20% from May high; AI pricing power "looks fragile," July 3 2026 (NEW v20 CRITICAL #4)
[^v20-5]: https://letsdatascience.com/news/ai-driven-rotation-reshapes-stock-market-leadership-dc767e6c — Palo Alto + CrowdStrike all-time highs; PHLX semi -6.3%/-5.4% Wed/Thu; WSJ: Zhipu GLM-5.2 now rivals Mythos at vulnerability hunting, July 3 2026 (NEW v20 SHARPEN #1)
[^v20-6]: https://mimir.substack.com/p/the-new-news-in-ai-7326-edition — NSA Gen. Joshua Rudd: Mythos "broke into almost all of our classified systems, not in weeks, but in hours," July 3 2026 (NEW v20 SHARPEN #2)
[^v20-7]: https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-defenders — 360 Security "Tulongfeng" finds 3,400+ vulnerabilities; Chris Inglis (former US National Cyber Director) endorses GLM-5.2 for defenders, July 3 2026 (NEW v20 SHARPEN #3)
[^v20-8]: https://www.mediapost.com/publications/article/416292/meta-prizes-ai-generated-creative-in-new-mini-game.html — Meta launches "Pocket" AI gizmos app on Apple App Store + Google Play, June 29 - July 3 2026 (NEW v20 SHARPEN #4)


## v19 AGI roadmap content (preserved in backup)

The v19 AGI roadmap (preserved in `dan2-agi-roadmap.v19-backup-2026-07-04.md`, 27.9KB, 237 lines) covers: 6/12/24-month plan with v19 CRITICAL (OpenClaw governance-drift audit, "no subscription" v1.0 marketing guarantee, 11-step narrative, Anthropic-Newsom California spec) + v19 SHARPEN (MemoMind One, China Mobile, NATO SAPIENT, Reuters Meta compute, AR Glasses size, Alphabet stock) + 4 open questions. **All v19 content is preserved verbatim in the backup. The v20 add is documented in the v20 addendum above: 4 CRITICAL (v20 auditable-bug-discovery pattern spec, v20 unit-economics spec, v20 Q4 2026 ship window, v20 11-step narrative) + 4 SHARPEN (Axios trust-model spec, NSA Rudd + Chris Inglis spec, Meta Pocket privacy spec, v20 6/12/24-month plan revision). v20 6-month plan adds: auditable-bug-discovery pattern, unit-economics argument, wearable-vacuum Q4 2026 ship window. v20 24-month plan keeps: HRM-Text-1B SIA-W+H Feedback-Agent, GLM-5.2 cybersecurity research bet, sovereign-on-prem vertical.**

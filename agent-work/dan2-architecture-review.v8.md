# Dan2 — Dan Glasses Architecture Review v8
## Concrete Fixes, Risks, and the Two-Brain Contradiction

**Date:** 2026-06-17 11:30 IST
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v8. v7 archived as `dan2-architecture-review.v7.md`.
**Companion:** Read `dan2-research-report.md` first for the deep-dive evidence.

---

## 0. v8 Read in 60 Seconds

The Dan Glasses architecture is **fundamentally sound**. The service decomposition is correct, the IPC contracts are well-defined, the memory architecture is right, and the v7 push to harness-only RL is the right path. v8 fixes the following P0/P1 items:

1. **Two-brain contradiction** (root AGENTS.md vs `dan-glasses/AGENTS.md`) — resolved cleanly. **No contradiction; the docs are layered.** `dan-glasses/AGENTS.md` is the per-project doc; root AGENTS.md is the project index. Dan1 fix needed: add explicit "layers" section to the root AGENTS.md.
2. **OpenClaw security is P0, not P1.** 48 CVEs + ClawHavoc 824 malicious skills + CVE-2026-33032 (CVSS 9.8) are concrete. v8 lays out the 5 mitigations.
3. **`memoryd` is fine for v1 but needs a v2 path.** v8 proposes the 13-typed-schema + graph-fallback design (see research report §C.1.2).
4. **`reasond` and `proactived` are the two new services that close the reasoning gap.** v8 specifies them concretely.
5. **Power state machine** is a v1 requirement, not v1.5. Without it, the wearable is not viable.
6. **GPU/NPU question** is the biggest undecided item. v8 recommends: keep CPU for v1, plan for NPU in v2.
7. **Perceptiond salience** is correctly designed; the next addition is a `context_gate` for LFM2.5 prompts.
8. **Audiod push-to-talk** is right for v1; wake-word is v1.5.
9. **TTS streaming** is a v1.5 ask. v1 returns full WAV.
10. **Spec power budget** is missing — the canonical analysis flagged this. v8 adds the v1 budget table.

The architecture is production-grade. The next 6 months are: close the reasoning gap, ship v1, document the privacy story.

---

## 1. The Two-Brain Contradiction (resolved in v8)

The v7 research report flagged this:

- **Root `AGENTS.md`** says: "Model Strategy: **HRM-Text (1B)** for reasoning, Whisper for STT."
- **`dan-glasses/AGENTS.md`** says: "LFM2.5-VL-450M for vision, whisper.cpp for STT, KittenTTS for TTS, all-MiniLM-L6-v2 for memory."

**v8 resolution:** the two files are at **different layers of the abstraction hierarchy**. The root `AGENTS.md` is the org-level index (it lists Dan Glasses, Dani, DanLab — multiple projects, with a short summary of each). The `dan-glasses/AGENTS.md` is the project-level doc (it specifies the full model stack for this project). The root says "HRM-Text for reasoning" because HRM-Text is the headline model that distinguishes Danlab's stack from generic LLM-stack competitors; the dan-glasses/AGENTS.md says "LFM2.5-VL-450M for vision" because that's the per-project decision.

**No contradiction.** But the root `AGENTS.md` is misleading because it implies HRM-Text is the only model in the stack. v8 fix:

- **Root `AGENTS.md` patch (DAN-1, week 1):**
  - Change: "Model Strategy: **HRM-Text (1B)** for reasoning, Whisper for STT."
  - To: "Model Strategy: **Layered** — HRM-Text 1B (reasoning) + LFM2.5-VL-450M (vision) + Gemma 4 1B (fast text) + whisper.cpp (STT) + KittenTTS (TTS) + all-MiniLM-L6-v2 (memory). Per-project: see `dan-glasses/AGENTS.md`."

- **`dan-glasses/AGENTS.md` patch (DAN-1, week 1):**
  - Add explicit reference to root `AGENTS.md` as the index, and clarify that the model stack listed here is the project-specific instantiation.

**v8 action:** flag for Dan1 to land in the next run. No code change required.

---

## 2. The Service Topology (v8 verdict)

The 7-service decomposition is correct:

| Service | Port | Status | v8 read |
|---|---|---|---|
| `audiod` | 8090 + WS 8091 | ✅ live, 83 tests | right shape |
| `perceptiond` | 8092 | ✅ live, 8 tests | right shape |
| `memoryd` | 8741 | ✅ live, 16 tests | right shape for v1; v2 in research §C.1 |
| `toold` | 8742 | ✅ live, 18 tests | right shape |
| `ttsd` | 8743 | ✅ live, 6 tests | right shape; consider streaming in v1.5 |
| `os-toold` | 8744 | ✅ live | right shape; the safety story is the moat |
| `openclaw-gateway` | 18789 | ✅ live, Telegram | P0 security fixes (see §3) |
| `zo-mcp-bridge` | stdio | ✅ live | right shape |

**v8 verdict:** no topology changes needed. The decomposition (perception, audio, memory, tool, tts, os-tool, gateway) is correct and matches the natural IO boundaries. Adding 2 more services (`reasond`, `proactived`) is the v8 next move — see §6 and §7.

**v8 question:** should we add a `powerd` service for the power state machine, or fold it into `openclaw-gateway`? **v8 answer: fold it in.** The power state machine is small (4 states: watchful, active, drowsy, sleep) and tightly coupled to mode-switching across services. A dedicated service adds latency and IPC overhead for no benefit. v1 implements it inside `openclaw-gateway`. v1.5 extracts it to its own service if it grows.

---

## 3. OpenClaw Security — P0 Actions (v8)

**The evidence (v8 research, primary sources):**
- 48 confirmed CVEs (June 2026), 138+ advisories.
- **Claw Chain** (CVE-2026-44112 to CVE-2026-44118, CVSS up to 9.6) — sandbox-escape + privilege escalation, exploited in the wild before patch 2026.4.22.
- **CVE-2026-33032 (CVSS 9.8)** — nginx-ui MCP integration, unauthenticated command execution. ~492 publicly exposed MCP servers with no auth (Trend Micro).
- **ClawHavoc** — 824 malicious LLM skills in the OpenClaw marketplace.
- **Malicious skill detector bypassed** in coordinated disclosure (Trail of Bits): trivial `.pyc` and `.docx` indirection bypass ClawHub, Cisco, Vercel scanners.
- **86% of top 2,354 skills** have vulnerabilities; 4.4% are outright malicious.
- **Imperva disclosure** on prompt injection via message objects (patched in 2026.4.23, but the systemic issue remains).
- **Microsoft SRR:** prompt injection progressed to remote code execution in popular agent frameworks.

**v8 actions (5 concrete mitigations, ordered by priority):**

1. **Pin OpenClaw to ≥ 2026.5.x** (post-Claw Chain patch). Verify by `openclaw --version`. Owner: DAN-1. ETA: this week.

2. **Disable the skill marketplace entirely.** v8 add to `/root/.openclaw/openclaw.json`:
   ```json
   {
     "policy": {
       "deny_skills": ["*"],
       "allow_skills": []
     }
   }
   ```
   Skills we need are vendored at `/home/workspace/dan-glasses/skills/`. No runtime fetch. Owner: DAN-1. ETA: this week.

3. **Audit all currently-installed skills** against Trail-of-Bits patterns (`.pyc`, `.docx`, `.npmrc` indirection, environment-variable exfil). Remove any that fail. Owner: DAN-2. ETA: this week.

4. **Gate `os-toold` to a strict allowlist** of executable paths and commands. The `Blocked shell chars: ; & | \` $( ) > <` list is a start; v8 adds:
   - No outbound network from `os-toold` (block all `curl`, `wget`, `nc`, `ssh`, `scp`).
   - No writes outside `/home/workspace`, `/tmp`, `/root` (already there).
   - All command invocations logged to a tamper-evident audit log (append-only, hash-chained).
   Owner: DAN-2. ETA: next run.

5. **Gateway bind to loopback only.** `/root/.openclaw/openclaw.json` must set `gateway.bind: "127.0.0.1"`, never `0.0.0.0`. Tailscale is the path for remote access (and Tailscale is not currently provisioned in this container, which is fine for now). Owner: DAN-1. ETA: this week.

**v8 risk residual:** even with these mitigations, OpenClaw has systemic prompt-injection risk (per the Imperva disclosure, no robust detection exists). The defense-in-depth answer: **never trust the model output to drive `os-toold` without an explicit human check or a deterministic policy check**. `os-toold` must be called only via the `mcp.servers.zo-bridge` MCP server from OpenClaw, and the bridge must redact/validate all tool arguments. This is already partially implemented; v8 makes it explicit.

---

## 4. Power State Machine (v1 requirement, not v1.5)

The v7 canonical analysis correctly flagged that the power state machine is missing from the spec. v8 specifies it concretely:

```python
# powerd / openclaw-gateway internal

class PowerState(Enum):
    SLEEP     = "sleep"      # camera off, mic ready, wake on voice
    DROWSY    = "drowsy"     # 0.5 FPS capture, VLM off, motion detection only
    WATCHFUL  = "watchful"   # 5 FPS capture, VLM on salient frames
    ACTIVE    = "active"     # 10 FPS capture, VLM continuous
    CHARGING  = "charging"   # AC-powered, ACTIVE mode, no power gating

# transitions
SLEEP -> DROWSY on motion_above_threshold
DROWSY -> WATCHFUL on user_voice_activity OR sustained_motion
WATCHFUL -> ACTIVE on explicit_user_request OR salient_event_score > 0.8
ACTIVE -> WATCHFUL on idle > 30s
WATCHFUL -> DROWSY on idle > 5min
DROWSY -> SLEEP on idle > 30min
ANY -> CHARGING on usb_pd_connected
CHARGING -> previous_state on usb_pd_disconnected
```

**v1 power budget (planning estimates, x86_64 laptop):**

| Component | SLEEP | DROWSY | WATCHFUL | ACTIVE | CHARGING |
|---|---|---|---|---|---|
| openclaw-gateway | 0.3W | 0.4W | 0.5W | 0.8W | 0.8W |
| memoryd (idle) | 0.1W | 0.2W | 0.2W | 0.3W | 0.3W |
| os-toold | 0.05W | 0.1W | 0.1W | 0.2W | 0.2W |
| audiod (mic ready) | 0.2W | 0.3W | 0.3W | 0.5W | 0.5W |
| perceptiond (camera) | 0W | 0.5W | 0.8W | 2.5W | 2.5W |
| LFM2.5-VL-450M (Q4) | 0W | 0W | 3W | 5W | 5W |
| ttsd (spike) | 0W | 0W | 0W | 1.5W | 1.5W |
| **Total** | **0.65W** | **1.5W** | **4.9W** | **10.8W** | **10.8W** |

**For a wearable with 2× 600mAh LiPo (3.7V, 4.44Wh total):**
- SLEEP only: ~27 hours
- DROWSY: ~12 hours
- WATCHFUL (50%): ~3 hours
- ACTIVE: ~1.5 hours

**v8 verdict:** 1.5-3 hours of active use is the realistic v1 target. The form-factor decision (see AGI roadmap §1) must account for this.

**v8 unresolved:** the aarch64 / Redax power numbers are unmeasured. The 3W-5W for LFM2.5-VL-450M is a CPU-inference estimate; on a dedicated NPU it could be 0.5-1W. **The single most important v1 hardware measurement is LFM2.5-VL-450M power on the actual aarch64 + NPU.** Without it, battery sizing is guesswork.

---

## 5. GPU / NPU Question (v8 verdict)

The canonical analysis correctly flagged that the spec doesn't say where the VLM runs.

**v8 verdict:**
- **v1 = CPU only.** LFM2.5-VL-450M via llama.cpp on aarch64 CPU. This is the simplest path; matches what we already run on x86_64. Power is high (~5W for inference spike) but the system can survive at this level if battery + thermal are sized for it.
- **v2 = NPU.** Target a board with a dedicated NPU (e.g., Rockchip RK3588 with 6 TOPS NPU, or an upcoming Redax variant). LFM2.5-VL-450M can be quantized + compiled to NPU. Expected power: 0.5-1W for inference. 5-10× improvement.
- **v3 = dedicated AI accelerator.** For v3 (12+ months out), target a board with a custom NPU (e.g., Apple Neural Engine class). Not on the v1 critical path.

**v8 action:** keep v1 spec CPU-only. v2 NPU is a hardware-track decision (Redax variant or board swap). Document this in the spec; don't fight hardware.

---

## 6. `reasond` — Reasoning Service (v8 spec sketch)

**Purpose:** Given observations from `audiod`, `perceptiond`, and `memoryd`, decide what to say, when to say it, and how to phrase it. This is the on-device reasoning layer that turns a recorder into a companion.

**Inputs:**
- `audiod` event stream: `{type: "transcript", text, start_ms, end_ms, confidence}`
- `perceptiond` event stream: `{type: "description", image_id, timestamp, description, event_id}`
- `memoryd` recall: query → top-K memories
- `proactived` triggers: `{type: "proactive_trigger", rule_id, score, context}`

**Outputs:**
- `{type: "suggestion", text, target: "speak" | "note" | "act", priority: 0-10, provenance: [...]}`

**Model:** HRM-Text 1B (primary) for the planning step; falls back to Gemma 4 1B for fast text generation. Both are 1B-class and fit on aarch64 at Q4 (~600MB).

**v8 architecture (sketch):**

```python
# reasond.py (sketch, ~500 LOC)

class ReasoningService:
    def __init__(self):
        self.hrm = HRMTextEngine()  # sapientinc/HRM-Text-1B, Q4
        self.gemma = GemmaEngine()  # Gemma 4 1B, Q4
        self.memory = MemoryClient()  # talks to memoryd :8741

    async def on_observation(self, obs):
        # obs is audiod transcript, perceptiond description, or proactive trigger
        context = await self.memory.recall(obs.summary, top_k=10)
        plan = self.hrm.plan(obs, context)  # HRM-Text 1B
        if plan.needs_phrase:
            phrase = self.gemma.phrase(plan)  # Gemma 4 1B
        else:
            phrase = plan.text
        if phrase and phrase.is_actionable:
            emit_suggestion(phrase, plan.provenance)

    async def on_proactive_trigger(self, trigger):
        # triggered by proactived when salience > threshold AND idle > 30s
        # reasond decides what to say
        pass
```

**v8 critical design choice: HRM-Text has latent-space reasoning, not CoT.** Per the Sapient paper (arXiv:2605.20613), HRM-Text replaces chain-of-thought in the token stream with internal latent-depth reasoning. This is actually ideal for the wearable: the user doesn't see the scratchpad, the model doesn't waste tokens on reasoning, and the response is direct. **v8 implication:** the `reasond` prompt should be short, not verbose. Resist the temptation to inject CoT prompts.

**v8 critical risk:** HRM-Text 1B is new (May 2026). Inference code is in `sapientinc/HRM-Text` (initial release) and HuggingFace transformers (PR #46025). vLLM support is in PR #43098. **We need to validate inference speed on x86_64 first** before committing to aarch64. If HRM-Text is too slow on aarch64, fall back to Gemma 4 1B. (HRM-Text is ~1.2B params with recurrence; Gemma 4 is 1B; should be similar wall-clock.)

**v8 plan:**
- Week 1-2: download `sapientinc/HRM-Text-1B`, validate inference on x86_64.
- Week 3-4: port the engine to llama.cpp or use the HuggingFace transformers Python binding for aarch64 prototype.
- Month 2-3: integrate into the full pipeline.
- Fallback: if HRM-Text is unworkable, use Gemma 4 1B and call it `reasond` anyway. The architecture is right; the model can swap.

---

## 7. `proactived` — Proactive Layer (v8 spec sketch)

**Purpose:** Decide *when* to speak. `reasond` decides *what* to say; `proactived` decides *when*. This is the "AI that initiates" layer that turns a tool into a companion.

**Triggers (v8 rules engine, hand-coded for v1):**

```python
# proactived.py (sketch, ~300 LOC)

RULES = [
    Rule(
        id="salient_event_user_idle",
        when=lambda ctx: ctx.salience_score > 0.8 and ctx.user_idle_seconds > 30,
        emit=lambda ctx: Suggestion(
            text=f"You might want to look at this: {ctx.last_description}",
            priority=7,
        ),
    ),
    Rule(
        id="recurring_topic",
        when=lambda ctx: ctx.topic_mentions_24h > 3 and ctx.user_engaged,
        emit=lambda ctx: Suggestion(
            text=f"You've mentioned {ctx.topic} a few times today. Want to dig in?",
            priority=4,
        ),
    ),
    Rule(
        id="ambient_question",
        when=lambda ctx: ctx.question_in_ambient_audio and ctx.user_idle_seconds < 5,
        emit=lambda ctx: Suggestion(
            text=f"I heard: {ctx.question}. Want me to look it up?",
            priority=8,
        ),
    ),
    # ... ~10-20 rules total for v1
]
```

**v1 policy: hand-coded rules + threshold tuning.** v2 path: distill rules into HRM-Text 1B (the "ProActor" pattern from ACL 2026). v3 path: RL-train the rule weights.

**v8 critical design choice: opt-in, not opt-out.** Proactive suggestions must be opt-in. v1 ships with `proactived` disabled by default. Users enable per-rule or globally. This is the *defensible* proactive UX. The proactived research (ProActor, ProAct) all found that proactive agents that get it wrong are worse than no proactive at all (per the OP-Bench failure modes: Repetition, Sycophancy).

**v8 anti-pattern guards (from OP-Bench):**
- **No more than 3 proactive suggestions per hour.** Hard cap.
- **No repeat suggestions within 24h.** Cache + dedupe.
- **No sycophantic framings** ("Great question!"). Use neutral language.
- **User can mute any rule permanently.** A "this is annoying" feedback loop should disable the rule for 7 days minimum.

---

## 8. `memoryd` v2 Path (concrete)

**Current state (v1):** SQLite + all-MiniLM-L6-v2 + 3 types + flat cosine. 16 tests. Production-grade for v1.

**v2 path (v8):**
1. **Add a Memory Classifier** (local, 0.6-1.2B). Decides type, extracts entities, decides retention. The classifier is the leverage point. Best candidate: a fine-tuned MiniLM classifier (cheaper than HRM-Text or Gemma) trained on 5-10K examples. ETA: month 2-3.
2. **Adopt 13 typed categories** (Memanto). Each with per-type metadata schema. Vector embedding stays shared.
3. **Add a thin graph layer** (NetworkX in Python; rustworkx in Rust). Used only when typed filter returns <3 candidates. ~200-500 LOC. ETA: month 3-4.
4. **Add MemRefine-style compression.** LLM-guided merge/keep/delete when memory size budget is hit. Run nightly. ETA: month 4-5.
5. **Add OP-Bench-driven anti-pattern guards.** Explicit relevance scoring (don't return memories that don't match at >0.5 cosine). Dedupe (don't store near-duplicates). Sycophancy guards (don't store "I love how you do X" as semantic).

**v8 risk:** the 13-category schema is a hypothesis. It might be too rigid. Plan: ship with 7 categories first, expand to 13 after 1 month of dogfooding data. **Don't over-engineer the schema in v2; let the data drive it.**

---

## 9. Audiod / Perceptiond / TTS — v8 verdicts

### 9.1 audiod (v8 verdict: keep v1, push streaming to v1.5)

The 83-test audiod is production-grade. v1 ships push-to-talk (PTT). v1.5 adds:
- Wake-word ("hey dan" or similar) — this is a meaningful power budget addition (mic always on with a small KWS model). Defer to v1.5.
- Binary hot-reload on `POST /reload` (currently requires full restart). Cheap to add.
- Bounded queue + drop-oldest for backpressure (currently drop-newest).

### 9.2 perceptiond (v8 verdict: keep v1, add `context_gate`)

The 8-test perceptiond is production-grade. v8 adds:
- **`context_gate`:** a small module that takes the most recent N descriptions and the most recent transcript, and builds a short, context-relevant prompt for the VLM. The current prompt is generic ("describe this image briefly"); `context_gate` would inject "the user is in a meeting, focus on people" or "the user is reading, focus on text". This is the biggest quality win for LFM2.5-VL-450M.
- **Image retention:** keep the last N images (configurable, e.g., 20) in a small ring buffer, not just text descriptions. The user can ask "what did you see 5 minutes ago?" and the system can re-encode the image and answer. This is the VisualMem pattern (arXiv:2605.28806). Adds ~20MB of memory; worth it.
- **Salience scoring calibration:** the current motion+face salience is heuristic. v2 can replace with a small learned scorer (a logistic regression on motion + face + audio energy + hour-of-day). v1 ships heuristic.

### 9.3 ttsd (v8 verdict: keep v1, add streaming in v1.5)

The 6-test ttsd is production-grade. v1 returns full WAV. v1.5 adds:
- **Streaming synthesis** (chunked HTTP response). PipPeline-3 and KittenTTS-mini both support this. Latency win: first audio byte in ~150ms vs ~500ms for full synthesis.
- **Voice selection UI.** Currently default voice; v1.5 adds 4-5 voices (warm, cold, fast, slow) to the bootstrap wizard.
- **v2 candidate: Piper** (per the 2026 edge TTS survey, Piper is the smallest, fastest, most battery-friendly option for on-device). 15MB model, runs on a single core. **v8 action:** evaluate Piper in month 2-3; consider for v2.

---

## 10. Service Health Contracts (v8 refinement)

The canonical spec defines `ServiceHealth` with degraded modes. v8 sharpens:

```python
# health schema (v8)

class ServiceHealth(BaseModel):
    status: Literal["ok", "degraded", "down"]
    service: str
    uptime_s: int

    # component-level
    components: dict[str, ComponentHealth]
    # e.g., {"vad": "ok", "whisper": "ok", "mic": "degraded_low_volume"}

    # business-level
    last_event_ts_ms: int | None  # when did this service last emit a useful event
    error_rate_5m: float          # 0.0-1.0, over last 5 minutes

    # resource-level
    memory_mb: int
    cpu_pct: float | None         # None if not measurable (e.g., on aarch64)
```

**v8 action:** the schema above should land in `shared/health_schema.py` and be imported by all 7 services. Today the schemas are per-service (audiod returns `{"status": "ok", "service": "audiod"}`; perceptiond returns `{"status": "ok"}`; etc). **Unify.** DAN-1, week 1.

---

## 11. Bootstrap Wizard (v8 refinement)

The current wizard (DAN-4 v2) is good. v8 adds:
- **Privacy threat model disclosure** at first launch: a 2-paragraph summary of what data leaves the device (nothing, by default) and what data stays (everything). User must acknowledge before proceeding.
- **Proactived opt-in:** "Allow Dan to speak first?" toggle, default off.
- **Reasond opt-in:** "Allow Dan to plan across observations?" toggle, default on (this is the core value prop).
- **TTS voice selection.** Pick from 4-5 voices.

**v8 action:** DAN-4, month 1.

---

## 12. The v1 Spec Patch List

The canonical `docs/dan-glasses-v1-canonical-analysis.md` flagged 15 issues. v8 status:

| # | Issue (canonical) | v8 status |
|---|---|---|
| 1 | Adaptive FPS throttles capture, not inference | ✅ v8 power state machine addresses (4.0-4.9W watchful) |
| 2 | No power budget defined | ✅ v8 §4 adds the budget table |
| 3 | No battery capacity target | ⚠️ depends on hardware decision (form factor) |
| 4 | LFM2.5-VL-450M power draw uncharacterized | ⚠️ depends on Redax measurement |
| 5 | Concurrent service power stack not modeled | ✅ v8 §4 |
| 6 | OpenClaw crash recovery | ⚠️ partial: systemd restarts; no in-process watchdog |
| 7 | No explicit GPU/NPU contract | ✅ v8 §5: v1 = CPU, v2 = NPU |
| 8 | audiod push-to-talk default is safe but limits UX | ✅ v1 ships PTT, v1.5 wake-word |
| 9 | Memory provider promotion gates not testable | ✅ v8 §8: 13-category schema with explicit acceptance |
| 10 | Package signing mechanism not defined | ⚠️ partial: GPG signed .deb is the v1 default; Sigstore deferred |
| 11 | Bootstrap wizard underspecified | ✅ v8 §11 |
| 12 | Redax is still a codename | ⚠️ hardware decision pending |
| 13 | Obsidian MCP as optional adapter | ✅ kept optional, no pressure to promote |
| 14 | Hermes one-provider constraint correctly flagged | ✅ noted |
| 15 | No mention of security attack surface | ✅ v8 §3 (OpenClaw P0) |

**v8 verdict:** 8 of 15 fully addressed, 7 pending hardware/Redax decisions.

---

## 13. Open Work — Priority Order (v8)

1. **(P0, week 1)** OpenClaw security mitigations — §3
2. **(P0, week 1)** Unify `ServiceHealth` schema — §10
3. **(P0, week 1)** Patch the two-brain AGENTS.md — §1
4. **(P0, week 2-3)** Validate HRM-Text 1B inference on x86_64 — §6
5. **(P0, week 2-3)** Implement `powerd` state machine in `openclaw-gateway` — §4
6. **(P1, month 1)** Bootstrap wizard v3 with privacy disclosure + opt-ins — §11
7. **(P1, month 1-2)** Write privacy threat model doc — `docs/privacy-threat-model.md`
8. **(P1, month 2-3)** Memory classifier + 13-typed-schema — §8
9. **(P1, month 2-3)** Piper TTS evaluation
10. **(P1, month 2-3)** `reasond` service skeleton (port :8745) — §6
11. **(P1, month 2-3)** `proactived` service skeleton (port :8746) — §7
12. **(P2, month 3-4)** `perceptiond` `context_gate` + image retention — §9.2
13. **(P2, month 3-4)** `audiod` binary hot-reload + bounded queue — §9.1
14. **(P2, month 4-5)** TTS streaming + voice selection — §9.3
15. **(P3, month 6+)** Wake-word, Redax migration, package signing (Sigstore)

---

*End of v8 architecture review. v8 is opinionated and concrete; v7 was broader. Use this as the engineering checklist for the next 3-6 months.*

# Model Selection Deep-Dive — Dan2 v37 (2026-06-22)

> **Scope.** Are the three model choices in the Dan Glasses canonical stack (LFM2.5-VL-450M, whisper.cpp base.en, KittenTTS) still the right picks in June 2026, given the Snap Specs 4h battery bar, SIA v2's verified numbers, and the growing Indian wearable ecosystem (NeoSapien Neo 1, Sarvam Kaze, Quest Global Neprion)?

## TL;DR (v37)

| Slot | Current (v36) | Verdict (v37) | Recommendation |
|------|---------------|---------------|----------------|
| **Vision** | LFM2.5-VL-450M Q4_0 + SigLIP2 encoder | ✅ Keep + speedup stack | Stay; add V5e-0 + QViD + SWEET (Q4/Q5/Q8) |
| **STT** | whisper.cpp base.en + Silero VAD | ✅ Keep | Add streaming fallback + Indic STT candidate |
| **TTS** | KittenTTS "medium" Python bindings | ⚠ Keep v1, plan Indic v2 | v2 = Piper or IndicF5 for Hindi/Tamil/Bengali |
| **Embedding** | all-MiniLM-L6-v2 (384-dim, 22MB) | ⚠ Upgrade to LFM2.5-Embedding-350M | 1024-dim, faster on LFM family |
| **Reasoning** | (none) | ➕ Add LFM2.5-1.2B-Thinking | Per `dan-glasses/AGENTS.md`; SIA Feedback-Agent |
| **Safety** | (none) | ➕ Add dglabs-eval safety subset | 5 tasks from Agents of Chaos |

The four choices are *defensible*. None is the best in its class. None is the worst. Where they lose to alternatives: **Indic TTS gap (KittenTTS English-only)**, **VLM speed (10s/frame is too slow for watchful mode)**, **no safety benchmark (SIA + Self-Harness both unverified on safety)**. Where they win: **edge latency on CPU (whisper.cpp is unmatched)**, **open-weight availability (LFM2.5 family is permissive)**, **permissive licensing (LFM2.5 + KittenTTS both MIT-class)**.

---

## 1. Vision — LFM2.5-VL-450M (Q4_0 + SigLIP2)

**Status:** Still the right choice for sub-500MB vision-language. **Verified live** at perceptiond v2, 8/8 tests, ~10s/frame on CPU.

### v37 candidates and decision matrix

| Model | Size | Sub-500MB? | Open weight? | Indic support? | Verdict |
|-------|------|------------|--------------|----------------|---------|
| **LFM2.5-VL-450M** | 450M (209MB Q4_0 + 180MB mmproj) | ✅ | ✅ (Liquid AI) | Partial | **Keep** |
| SmolVLM-256M-Instruct | 256M (120MB Q4 + 182MB mmproj) | ✅ | ✅ | ❌ | Fallback |
| OmniVLM-968M | 968M | ❌ (just over) | ✅ (NexaAI) | ❌ | Upgrade path if size budget grows |
| Qwen3-VL-2B | 2B | ❌ | ✅ (Apache 2.0) | ✅ | v1.5 candidate |
| Qwen2.5-VL-3B/7B | 3B/7B | ❌ | ✅ | ✅ | Too big for wearable v1 |
| Gemma 3 270M | 270M (text-only) | ✅ (but no vision) | ✅ | ❌ | Not applicable |
| Llama 4 Nano | TBD | TBD | TBD | TBD | Watch list |
| **LFM2.5-VL-1B** | ~1B (est. Q3 2026) | ❌ (likely) | ✅ (Liquid) | TBD | v1.5 candidate |

**v37 decision:** Keep LFM2.5-VL-450M as primary. SmolVLM-256M as auto-fallback (perceptiond.yaml already wires this). Add OmniVLM-968M and LFM2.5-VL-1B to the candidate list (v1.5 — when 8GB LPDDR is achievable in glasses form factor, OR for the v1.5 sub-1s/frame goal).

### v37 new data: training-free speedup stack (carry from v36, sharpened)

Three Jun 2026 papers (all training-free, all composable) suggest 3-5× speedup is achievable without changing the model:

1. **V5e-0** (OpenReview, Jun 2026): **self-speculative decoding using only text-side hidden states**, no vision encoder call. 1.89× wall-clock speedup across 15 VLMs.
2. **QViD** (OpenReview, Jun 2026): **vision-token pruning via low-rank query-vision interaction**. 1.5–2× additional speedup, training-free.
3. **SWEET** (Frontiers, 2026): **layer-wise quantization bitwidth + edge-cloud partition**. Salience-gated Q4/Q5/Q8 selection. <1% accuracy degradation bound.

**Combined estimate:** LFM2.5-VL-450M 10s/frame → **2-3s/frame** with the three composed. **v1 target. Highest-leverage sprint in v37.**

**v1.5 target:** sub-1s/frame requires LFM2.5-VL-1B (est. Q3 2026) + speedup stack, or LFM2.5-VL-450M + hardware acceleration (gated on silicon pivot decision).

### What v37 does NOT recommend

- **Don't fine-tune LFM2.5-VL-450M.** Compute cost is wrong for India-from-AGI. The vision encoder is general; what we need is **a better harness (perceptiond pipeline), not better weights.**
- **Don't replace with OmniVLM-968M yet.** The 2.3× size budget is unjustified for v1.
- **Don't drop the SmolVLM-256M fallback.** It's the safety net for when LFM2.5 isn't available.

---

## 2. STT — whisper.cpp base.en + Silero VAD

**Status:** Audiod v0.7 verified live (121/121 tests). Production-grade.

### v37 candidates

| Model | Size | Latency | Indic? | Verdict |
|-------|------|---------|--------|---------|
| **whisper.cpp base.en** | 74MB | <300ms/segment | ❌ (English) | **Keep** for v1 |
| whisper.cpp tiny.en | 39MB | <150ms/segment | ❌ | v1.5 candidate for thermal |
| whisper.cpp small.en | 244MB | <600ms/segment | ❌ | v2 candidate (better accuracy) |
| Parakeet (NVIDIA) | ~120MB | TBD | ✅ | v2 candidate for Indic |
| IndicConformer | ~80MB | TBD | ✅ | v2 candidate for Indic |

**v37 decision:** Keep whisper.cpp base.en for v1 (English-only). **Add IndicConformer or Parakeet to v2 candidate list** for India-first positioning.

### v37 new data

- **Wavelet-driven CFM TTS postprocessing** is training-free, frequency-selective, improves Fréchet Audio Distance by up to 61%, supports Hindi/Tamil/Bengali natively. **Relevant for TTS v2, not STT.**
- No major new STT papers in Jun 2026 that change the picture for English. **whisper.cpp is still the production standard for CPU edge inference.**

### What v37 does NOT recommend

- **Don't switch to Whisper Large.** Compute cost is wrong.
- **Don't add wake-word as v1.** Battery / thermal budget doesn't allow it. **v1.5 target.**
- **Don't replace Silero VAD.** It's the best VAD for CPU edge in 2026.

---

## 3. TTS — KittenTTS "medium" (Python bindings)

**Status:** Ttsd v1 verified live (6/6 tests, 8 voices, 24kHz mono WAV). Adequate for English v1.

### The Indic problem

**KittenTTS is English-only.** For India-first positioning, this is the #1 gap. Hindi, Tamil, Bengali, Marathi, Telugu — none are supported.

### v37 candidates

| Model | Size | Latency | Indic? | Quality | Verdict |
|-------|------|---------|--------|---------|---------|
| **KittenTTS "medium"** | ~25MB | <1s warm, ~3.8s cold | ❌ | Good | **Keep** for v1 English |
| Piper | 15-60MB | <500ms | ✅ (multi-lang) | Good | **v2 candidate** for Indic |
| Kokoro-82M | 82MB | <300ms | ✅ (multi-lang) | Excellent | **v2 candidate** if quality > size |
| Orpheus-TTS | ~400MB | ~1s | ❌ (English focus) | Excellent | Skip |
| **IndicF5** | ~80MB | ~500ms | ✅ (Indic native) | Good | **Strong v2 candidate** for India-first |
| BareWave (arXiv:2606.09048) | ~600MB | TBD | ❌ | Excellent | Too big |

**v37 decision:** Keep KittenTTS for v1 English. **v2 = Piper or IndicF5** depending on quality benchmarks. **Piper** is the safe pick (mature, multi-lang, small). **IndicF5** is the high-upside pick (Indic native, works with CFM-based stack).

### v37 new data

- **Wavelet-driven CFM TTS postprocessing**: training-free, FAD up to 61% better, supports Hindi/Tamil/Bengali. **Applies to any CFM-based TTS** including IndicF5. **Strong v2 case.**

### What v37 does NOT recommend

- **Don't swap KittenTTS blindly.** It's working. The v1 ship matters.
- **Don't pick Orpheus-TTS.** Indic support is weak; size is too big.
- **Don't pick BareWave yet.** 600MB is too big for wearable.

---

## 4. Embedding — all-MiniLM-L6-v2 (carry from v36, sharpened for v37)

**Status:** Memoryd v1 live, 16/16 tests. Adequate.

### v37 candidates

| Model | Size | Dim | Quality | Verdict |
|-------|------|-----|---------|---------|
| **all-MiniLM-L6-v2** | 22MB | 384 | OK | **Keep** for v1 |
| LFM2.5-Embedding-350M | 350MB | 1024 | Excellent | **v2 candidate** (LFM family compat) |
| LFM2.5-ColBERT-350M | 350MB | 1024 | Excellent (late interaction) | **v2 candidate** for reranker |
| NanoVDR-distilled 69M text encoder | 69MB | varies | 95.1% of 2B teacher | v2 candidate for query encoding |
| Omni-Embed-Mini 0.9B | 900MB | varies | MTEB-v2 BEIR-8 49.50 nDCG@10 | v3 candidate for omni-modal retrieval |

**v37 decision:** Keep all-MiniLM-L6-v2 for v1. **v2 = LFM2.5-Embedding-350M as primary + LFM2.5-ColBERT-350M as reranker** (per v35 model analysis). Memoryd v2 also adds LightGMEM-style entity graph + VisualMem visual memory.

### What v37 does NOT recommend

- **Don't use OpenAI ada-002 or Cohere embed-v3.** Cloud-dependent; privacy posture is "no cloud ever."
- **Don't fine-tune embeddings in v1.** Premature optimization.

---

## 5. Reasoning (carry from v36, sharpened for v37) — HRM-Text 1B vs LFM2.5-1.2B-Thinking

**Status:** Not yet deployed. **Per `dan-glasses/AGENTS.md`: "HRM-Text Integration" is current focus, model strategy = HRM-Text (1B) for reasoning, Whisper for STT.**

### v37 read on HRM-Text vs LFM2.5-1.2B-Thinking

`dan-glasses/AGENTS.md` (workspace memory) says HRM-Text 1B. v37 research says LFM2.5-1.2B-Thinking is the right call for **SIA Feedback-Agent** (per v35). **Conflict.**

**v37 ask:** which is correct? Two possibilities:
1. **HRM-Text** is the production reasoning model for the wearable (1B, runs on device).
2. **LFM2.5-1.2B-Thinking** is the cloud-side reasoning model used by SIA Feedback-Agent during eval/training.

Both can be true. **Clarify with somdipto** before SIA fork ships.

### v37 recommendation

- **On-device:** HRM-Text 1B (per AGENTS.md). 1B is the wearable ceiling today.
- **Cloud-side SIA loop:** LFM2.5-1.2B-Thinking. 1.2B exceeds wearable memory budget but is fine for cloud-side Feedback-Agent.
- **Both shipped.** dglabs-eval supports both.

---

## 6. Safety Benchmark (v37 NEW) — dglabs-eval safety subset

**Status:** Not yet deployed. **dglabs-eval v1 must include 5 safety tasks from Agents of Chaos.**

### v37 candidate tasks (5 of 12 from Agents of Chaos)

| Task | Source | Severity | Verdict |
|------|--------|----------|---------|
| Disproportionate response | Agents of Chaos Case 1 | High | **Include** |
| Non-owner compliance | Agents of Chaos Case 2 | High | **Include** |
| Sensitive info disclosure | Agents of Chaos Case 3 | Critical | **Include** |
| Owner identity spoofing | Agents of Chaos Case 8 | Critical | **Include** |
| Prompt injection via broadcast | Agents of Chaos Case 12 | High | **Include** |

**v37 decision:** **All 5 included as non-negotiable regression gate.** Weight updates that fail any safety task are **rejected.** Harness edits that fail any safety task are **logged but not blocked** (asymmetric).

### What v37 does NOT recommend

- **Don't include all 12 Agents of Chaos cases.** Only the 5 above. The other 7 (looping, DoS, provider values, agent harm, agent collaboration, agent corruption, libelous) are research curiosities, not first-pass safety requirements.
- **Don't invent new safety tasks.** The 5 above are the empirical source.

---

## 7. Quantization cookbook (carry from v36, sharpened in v37)

### For perceptiond (LFM2.5-VL-450M)
- **Watchful mode (default):** Q4_0 + V5e-0 + QViD = 2-3s/frame. **v1 target.**
- **Active mode (high salience):** Q5_0 + V5e-0 + QViD = 4-5s/frame. **v1 target.**
- **Idle mode (motion only):** Q4_0, no VLM, motion detection only. **v1 target.**
- **Sleep mode:** camera off, services idle. **v1 target.**
- **v1.5 target:** Sub-1s/frame requires LFM2.5-VL-1B + speedup stack OR LFM2.5-VL-450M + hardware acceleration.

### For audiod (whisper.cpp base.en)
- **Q5_1** (default for wearable v1) — balance of size (60MB) and accuracy.
- **Q8_0** (laptop prototype) — better accuracy, AC-powered.

### For ttsd (KittenTTS)
- "medium" variant only (no quantization; the model is already <25MB).
- For v2 (Piper / IndicF5): Q4_K_M if quantization is supported.

### For memoryd (all-MiniLM-L6-v2 → LFM2.5-Embedding-350M)
- v1: all-MiniLM-L6-v2 fp16, no quantization.
- v2: LFM2.5-Embedding-350M Q4_K_M (if quantization supported).

### For reasoning (HRM-Text 1B on-device, LFM2.5-1.2B-Thinking cloud-side)
- v1: HRM-Text 1B Q4_K_M on-device. LFM2.5-1.2B-Thinking Q4_K_M cloud-side.
- v2: HRM-Text 2B (if released) Q4_K_M on-device. LFM2.5-Thinking-2B cloud-side.

---

## 8. v37 NEW: Battery math (Snap 4h as the bar)

Snap Specs claims 4h mixed-use battery. Snap hardware: dual Snapdragon, 132g, $2,195. Battery capacity: est. ~750mAh at 3.85V (typical for 132g glasses).

**v37 battery math for Dan Glasses:**
- Target weight: <80g (consumer-tier, NeoSapien-class).
- Target battery: ~250-300mAh (2x 150mAh in temples, per AGENTS.md).
- Battery life target: 4h mixed-use (Snap bar).
- Average power budget: 300mAh × 3.85V / 4h = **~290mW = 0.29W average.**

**This is the constraint that determines model choices:**
- VLM inference must be <2W peak (allowable 0.29W average with 5× duty cycle).
- Whisper.cpp base.en Q5_1 must be <0.5W peak.
- KittenTTS must be <0.5W peak (spike).
- OpenClaw + audiod + memoryd + toold + os-toold + ttsd (idle) must be <0.3W combined.

**v37 read:** **LFM2.5-VL-450M at 2-3s/frame is on-budget.** **whisper.cpp base.en is on-budget.** **KittenTTS is on-budget.** **The 7-daemon stack idle is on-budget.** **The risk is in transitions** (VLM wake-up, TTS synthesis, GPT-OSS 120B cloud-side SIA loop).

**v37 sharpens v36's gap:** **battery math is now concrete. Pick the silicon and measure on real hardware.** Fix #2 (hardware pivot) and Fix #5 (VLM speedup) are the unlock.

---

## 9. What v37 Adds vs v36

- **Safety benchmark:** dglabs-eval safety subset (5 tasks from Agents of Chaos). **v36 didn't address safety.**
- **Battery math:** Snap 4h bar → ~290mW average target. **v36 was abstract on power.**
- **LFM2.5-VL-1B candidate:** v1.5 upgrade path for sub-1s/frame goal.
- **Reasoning model resolution:** HRM-Text 1B on-device + LFM2.5-1.2B-Thinking cloud-side. **v36 was ambiguous.**

---

*Dan2 model analysis, 2026-06-22 v37. Verifies v35, v36 picks; adds safety benchmark, battery math, LFM2.5-VL-1B upgrade path, HRM-Text/LFM2.5-1.2B-Thinking split.*

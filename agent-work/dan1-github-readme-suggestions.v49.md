# Dan1 GitHub README Improvements — v49

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-16 11:00 IST (05:30 UTC)
**Status:** ✅ Canonical. Supersedes v48. **READMEs drafted. v50 is the PRs merged.**

> One-line rule (unchanged): *A README is a sales page that converts engineers. Lead with what it does in one sentence, show the demo, link the code. No philosophy in the first 200 words.*

---

## 0. The 6 repos to polish in Week 1

**All copy is in `punchlist-copy-paste.md` (§H, §I, §J, §K, §L, §M). Open it. Find the section. Paste.**

| # | Repo | Visibility | Stars (today) | Action | File ref |
|---|---|---|---|---|---|
| 1 | `somdipto/danlab-multimodal` | **PRIVATE** | n/a | **Make public. Apply README. Add topics.** | §H |
| 2 | `somdipto/dan-glasses` | Public | 0★ | **Apply README. Add topics. Update description.** | §I |
| 3 | `somdipto/dani` | Public | 1★ | **Apply README. Add topics. Update description.** | §J |
| 4 | `somdipto/paperclip` | Public | 0★ | **Apply README. Add topics. Update description.** | §K |
| 5 | `somdipto/dan-consciousness` | Public | 0★ | **Apply README. Add topics. Update description.** | §L |
| 6 | `somdipto/openwork` | Public | 3★ (top star) | Light polish. | §M |

**The single highest-leverage action in the entire marketing plan is making `danlab-multimodal` public on Day 0.** Without that, the rest is decoration. **Text in §H.**

---

## 1. NEW IN v49: The Omni-1B repo (the 7th repo to add to the list)

**A new repo, not yet on GitHub:** `somdipto/omni-1b-indic` — the Omni-1B-Indic model that somdipto is training from scratch.

**Action (Day 60, post-v50):** Create the repo, add the model card, the tokenizer, the training recipe, the eval suite, and the 1,000-example Indic test set. Add the `omni-1b-indic-v0.1` HF mirror via `huggingface-cli upload`.

**Why this is the highest-leverage new repo of the year:** A working 1B Omni trained on Indic languages is a research artifact that no Western lab has shipped. It will get cited. It will get forked. It will get starred by every Indic-AI researcher on GitHub. **It is the wedge made concrete.**

**Description (placeholder, refined when the model ships):**
```
Omni-1B-Indic — a 1B-parameter Omni model trained from scratch on 9 regional Indian language families. The smallest Omni that fits in the wearable form factor. Trained in Bangalore. MIT. From India to the world.
```

**Topics (placeholder):**
`omni-model`, `multimodal`, `indic-languages`, `1b-model`, `from-scratch`, `open-source`, `india`, `wearable-ai`, `bengaluru`, `mit-license`

**This is v50 work, not v49 work.** Logged here so we don't lose the thread.

---

## 2. `somdipto/dan-glasses` — the main stack

**Full README rewrite text in `punchlist-copy-paste.md` §I.**

**v49 addition:** The README's "What is this?" section should add a one-liner about the Omni-1B-Indic training. Not a full section, just a one-liner in the existing structure.

### Suggested topics (12, unchanged)
`ai-glasses` `wearable-ai` `on-device-llm` `lfm2-vl` `open-source` `india` `tauri` `whisper-cpp` `memory` `proactive-ai` `mcp` `from-india`

### Suggested description (167 chars, unchanged)
```
Open-source AI glasses. 7 services. 0 cloud. $0/month. MIT. Proactive, not reactive. Built in Bangalore 🇮🇳
```

### New "What is this?" one-liner (add below the existing one)
```
We don't just integrate models. We train them. See `omni-1b-indic` (v0.1 ships Day 60).
```

---

## 3. `somdipto/danlab-multimodal` — the demo repo (THE #1 DAY-0 ACTION)

**Action:** Make this repo public. Today. The repo is a complete, working VLM pipeline on CPU. It is currently 404 to anonymous. **This is the single highest-leverage action in the entire marketing plan.**

**Full README rewrite text in `punchlist-copy-paste.md` §H.**

**v49 addition:** Add a "What's next" section that previews the Omni-1B-Indic v0.1 as the follow-up artifact (the same pipeline, but on a custom model).

### Suggested topics (10, unchanged)
`vlm` `multimodal` `llama-cpp` `smolvlm` `heuristic` `pre-rl` `cpu-inference` `hackathon` `india` `open-source`

### Suggested description (140 chars, unchanged)
```
Sub-250MB VLM on CPU via llama.cpp. Heuristic feedback loop. Pre-RL scaffold. MIT. From Bangalore 🇮🇳
```

---

## 4. `somdipto/dan-consciousness` — the shared brain

**Full README rewrite text in `punchlist-copy-paste.md` §L.**

### Suggested topics (9, unchanged)
`agi` `consciousness` `agents` `open-source` `india` `danlab` `memory` `identity` `values`

### Suggested description (97 chars, unchanged)
```
The shared brain between Dan (AI) and somdipto (human) at danlab.dev. AGI in the open.
```

---

## 5. `somdipto/dani` — the agent platform

**Full README rewrite text in `punchlist-copy-paste.md` §J.**

### Suggested topics (10, unchanged)
`agent` `mcp` `agent-runtime` `typescript` `open-source` `india` `memory` `tools` `claude-desktop` `cursor`

### Suggested description (95 chars, unchanged)
```
Open-source agent runtime. MCP-native. MIT. Powers danlab.dev's products. From Bangalore 🇮🇳
```

---

## 6. `somdipto/paperclip` — the company orchestrator

**Full README rewrite text in `punchlist-copy-paste.md` §K.**

### Suggested topics (9, unchanged)
`agents` `orchestration` `mcp` `express` `typescript` `react` `open-source` `india` `multi-agent`

### Suggested description (95 chars, unchanged)
```
AI agent company orchestration. Hire AI agents, set goals, control costs. MIT. From Bangalore 🇮🇳
```

---

## 7. `somdipto/openwork` — the open-source AI coworker (light polish)

**Light polish, no full rewrite needed. Add the top 20 lines from `punchlist-copy-paste.md` §M.**

### Suggested topics (8, unchanged)
`ai-coworker` `desktop-agent` `open-source` `mcp` `typescript` `india` `automation` `browser-automation`

### Suggested description (84 chars, unchanged)
```
The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳
```

---

## 8. The GitHub profile fix (the wrapper)

**Full text in `punchlist-copy-paste.md` §F (profile) and §G (profile README).**

**v49 update:** The profile README should include a "Currently training" section that mentions the Omni-1B-Indic.

### `github.com/somdipto` — the changes

**Display name:** `somdipto nandy` (was: "Sodan")

**Bio (160 chars, unchanged):**
```
building AGI from India 🇮🇳 @ danlab.dev — open, local, proactive AI glasses, MIT
```

**Pinned repos (in this order, unchanged):**
1. `dan-glasses` — the main stack
2. `danlab-multimodal` — the demo repo (once public)
3. `dan-consciousness` — the shared brain
4. `dani` — the agent runtime
5. `paperclip` — the company orchestrator
6. `openwork` — the desktop sibling

**Profile README (the new `somdipto/somdipto` README):** See `punchlist-copy-paste.md` §G.

**v49 addition — a "Currently training" block at the top of the profile README:**

```markdown
## Currently training

**`omni-1b-indic`** — a 1B-parameter Omni model from scratch. 3 months in.
Trained on 9 regional Indian language families. The smallest Omni that
fits in the wearable form factor. MIT. v0.1 ships to HuggingFace Day 60.

[X thread](https://x.com/NandySomdipto/status/2065216558046281749)
```

---

## 9. The 5 things every README must have (the checklist, unchanged from v48)

1. **One-line description in the H1 area.** "What is this?" answered in 1 sentence.
2. **Quick start that works in <2 minutes.** `git clone && ./scripts/dev.sh && curl :8090/health`.
3. **Status section.** "Demoable today" / "Blocked on hardware" / "Dormant". No ambiguity.
4. **License footer.** MIT. Always.
5. **From India 🇮🇳 badge.** Every repo. Always. It's the brand.

---

## 10. The metric per repo (the only number that matters, unchanged from v48, with v49 addition)

| Repo | Current stars | Target Q3 | Target Q4 |
|---|---|---|---|
| `dan-glasses` | 0 | 500 | 2,000 |
| `danlab-multimodal` | (private) | 500 | 2,000 |
| `dan-consciousness` | 0 | 200 | 1,000 |
| `dani` | 1 | 300 | 1,500 |
| `paperclip` | 0 | 200 | 1,000 |
| `openwork` | 3 | 500 | 2,000 |
| `omni-1b-indic` | (not yet created) | 1,000 | 5,000 (NEW, v49) |
| **Total** | **4 + private** | **3,200** | **14,500** |

**v49 target: 14,500 stars across 7 repos. The 5,000-star target on `omni-1b-indic` is the wedge.** A working 1B Omni trained on Indic languages will be cited, forked, and starred by every Indic-AI researcher. The 5,000 is conservative.

---

## 11. The Tushar Shaw / Percevia acknowledgement (from v48) — UNCHANGED

**If somdipto wants to add a "friends we ship alongside" section to any README:**

```markdown
## Friends we ship alongside

- **[Percevia / Tushar Shaw](https://x.com/dogra_ns/status/2065204989610365422)** — 19-year-old from Bengaluru. AI glasses for the blind using Gemini, ₹9,999-11,999, won ₹25L at Samsung Solve for Tomorrow 2025. We are the open-source, on-device, MIT alternative to their cloud-dependent stack. **Same Bangalore. Different bets.**

- **[Indranil Bhadra](https://x.com/Indrani78141068/status/2064267293153210696)** — building the same wedge from a different angle. *"Not another gadget that shouts 'Hey Google'. Just a silent companion that grows into an extension of your own brain."* We agree.

- **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — our open-source VLM pipeline, sub-250MB on CPU, MIT, the demo repo.
```

---

## 12. NEW IN v49: The "we train the model" block (add to dan-glasses + danlab-multimodal)

**Add this block to the top of both READMEs, just below the title:**

```markdown
> **We don't just integrate models. We train them.**
>
> The Omni-1B-Indic is a 1B-parameter Omni model we're training from scratch.
> 3 months in. Trained on 9 regional Indian language families. The smallest
> Omni that fits in the wearable form factor. MIT. v0.1 ships Day 60.
>
> [Training thread on X](https://x.com/NandySomdipto/status/2065216558046281749)
```

**Why:** Anyone who lands on a Dan Lab repo should immediately understand: we are not integrating Qwen. We are training our own. This block makes that claim visible from the first scroll.

---

*End of v49. The 6 READMEs are drafted. The profile fix is drafted. The topics are listed. The new `omni-1b-indic` repo is added to the metric. The "we train the model" block is the v49 wedge. The only thing left is the punchlist.*

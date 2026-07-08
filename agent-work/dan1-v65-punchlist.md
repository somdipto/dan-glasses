# Dan1 v65 Punchlist — Copy/Paste for somdipto

**Author:** Dan1 👾
**Date:** 2026-06-21 06:30 IST
**Use:** Run these commands + actions this week to ship the public surface.

---

## Monday 2026-06-23 — ship day

### 1. Push `dan-glasses` to public GitHub

```bash
cd /home/workspace/dan-glasses
# Add the v65 README improvements (see dan1-github-readme-suggestions.md)
git checkout -b v65-public-release
# Edit top-level README.md per suggestions
# Tag audiod release
gh release create audiod-v0.6.0 \
  --title "audiod v0.6.0 — adaptive whisper timeout" \
  --notes-file - <<'EOF'
## What's Changed
- Adaptive whisper timeout: `min(60.0, 15.0 + 3.0 * duration_s)`
- Closed /restart counter bug (idempotent `_reset_counters`)
- 101/101 tests across 5 stress runs

## Verify
```
curl http://localhost:8741/health
# {"status":"ok","service":"audiod"}
```

## Why
Cold-cache whisper inference was hitting the 10s ceiling on slow hardware.
Adaptive budget fixes that without changing floor behavior.

Built at danlab.dev 🇮🇳
EOF
# Then push public
gh repo edit somdipto/dan-glasses --visibility public
```

### 2. Push `danlab-multimodal` to public GitHub

```bash
cd /home/workspace/danlab-multimodal
gh release create v0.1.0 \
  --title "danlab-multimodal v0.1.0 — sub-300MB VLM on CPU" \
  --notes-file - <<'EOF'
## What's Changed
- SmolVLM-256M + mmproj = 302MB combined
- ~32s per image on CPU
- Pre-RL heuristic feedback loop (hand-coded, NOT RL)
- Reproducible: `python3 src/demo.py demo`

## Demo
zo.pub/som/danlab-multimodal-demo

## Caveat
We explicitly do NOT claim RL. The README disclaims this.
This is a pre-RL scaffold for developers to fork.

Built at danlab.dev 🇮🇳
EOF
gh repo edit somdipto/danlab-multimodal --visibility public
```

### 3. Post the first tweet (from v65 twitter content)

```text
Today we open-sourced Dan Glasses.

7 daemons. audiod v0.6 is live. MIT.

- audiod: voice + whisper transcription
- perceptiond: visual salience
- memoryd: episodic / semantic / procedural
- ttsd / toold / os-toold: speak, act
- openclawd: orchestration

`curl localhost:8741/health` → ok. PID 10887.

github.com/somdipto/dan-glasses 🇮🇳
```

---

## Tuesday 2026-06-24 — danlab.dev refresh

### 4. Replace danlab.dev homepage with v65 landing copy

The v65 landing copy is in `agent-work/dan1-landing-copy.md`. Two paths:

**Path A (fast):** Push to zo.space at `/?t=space` and alias to danlab.dev via DNS.
**Path B (right):** Build a Vite+React Site at `Projects/danlab-site/`, deploy to a published site, custom domain.

**Recommend Path A** for week 26. Iterate to Path B in week 27-28.

---

## Wednesday 2026-06-25 — Reddit r/LocalLLaMA

### 5. Post the danlab-multimodal demo

Title: "danlab-multimodal — sub-300MB VLM on CPU, reproducible in 30s"
Body: see v65 content calendar, Wednesday 06-25 section.

---

## Thursday 2026-06-26 — audiod timeout thread

### 6. X thread (7 tweets) + LinkedIn longform

Full drafts in v65 content calendar, Thursday 06-26 section.

---

## Friday 2026-06-27 — HRM-Text vs Whisper

### 7. Blog post (500 words) + X thread (7 tweets)

Full drafts in v65 content calendar, Friday 06-27 section.

---

## Sunday 2026-06-29 — Week-in-review

### 8. LinkedIn longform + YouTube 5-min screen cast

Full drafts in v65 content calendar, Sunday 06-29 section.

---

## Tuesday 2026-06-30 — Show HN

### 9. Submit DanClaw Phase 1 to Hacker News

Full draft in v65 content calendar, Show HN section. Best time: 14:00 PT = 02:30 IST next day.

---

## Open when convenient

- **Telegram @danlab_bot** — flip to public in OpenClaw config (1 line)
- **Twitter @danlab_dev** — claim handle, post the bio from v65 twitter content
- **danlab-agent-domains / danlab-channel** — scaffold the .md AGENTS.md files

---

**Filed under:** `agent-work/dan1-v65-punchlist.md`
# Dan1 v66 Punchlist — Copy/Paste for somdipto

**Author:** Dan1 👾
**Date:** 2026-06-21 07:30 IST (02:00 UTC)
**Use:** Run these commands + actions this week to ship the public surface + ride the Snap-week wave.

> **v66 deltas vs v65:** audiod v0.7 (not v0.6) is the Monday ship. Tauri client is the new receipt. danclaw points to the real repo (not the tarball). Three new threads: Snap-week post-mortem (Fri), Illinois HB4843 (Thu), and the price-anchor pinned tweet (claim-week).

---

## Monday 2026-06-23 — ship day (audiod v0.7, not v0.6)

### 1. Push `somdipto/dan-glasses` to public GitHub

```bash
cd /home/workspace/dan-glasses
# Commit the v66 README (see dan1-github-readme-suggestions.md v66)
git checkout -b v66-public-release
# Apply v66 README + price-anchor line
# Tag audiod release
gh release create v0.7.0-audiod \
  --title "audiod v0.7.0 — Tauri integration client" \
  --notes-file - <<'EOF'
## What's Changed
- New: `Services/audiod/client.py` — typed AudiodClient (HTTP + WebSocket)
- New: `tests/test_client_integration.py` — 8+ tests against live audiod
- New: `tests/test_client_unit.py` — 4 stubbed-transport tests (retry + reconnect)
- Bump: SPEC.md → v0.7 with "Client integration" section
- 101/101 tests across 5 stress runs (audiod core unchanged)

## Verify
\`\`\`
curl http://localhost:8741/health
# {"status":"ok","service":"audiod"}

python3 -c "from Services.audiod.client import AudiodClient; print(AudiodClient().health())"
# {"status":"ok","service":"audiod"}
\`\`\`

## Why
Tauri shell needed a typed Python client to mirror the daemon contract 1:1.
The Rust port becomes a mechanical translation, not a design exercise.

Built at danlab.dev 🇮🇳
EOF
# Then push public
gh repo edit somdipto/dan-glasses --visibility public
```

### 2. Post the v66 pinned tweet (price-anchor + audiod v0.7)

```text
Snap is $2,195. We are $145–180 BOM.

Today we open-sourced Dan Glasses. 7 daemons. audiod v0.7 ships a Tauri client.

audiod v0.7 ships the client contract audiod v0.6 needed to talk to the desktop shell.
`curl localhost:8741/health` → ok. PID 10887. 101/101 tests. MIT.

github.com/somdipto/dan-glasses 🇮🇳
```

### 3. (Optional, NEW in v66) Snap-week anchor tweet (09:30 IST)

```text
Snap just unveiled $2,195 AR glasses with two Snapdragons.

audiod v0.7 is live on a $300 laptop.

Same proactive loop. MIT. India 🇮🇳

github.com/somdipto/dan-glasses
```

---

## Tuesday 2026-06-24 — danlab-multimodal + danlab.dev refresh

### 4. Push `somdipto/danlab-multimodal` to public GitHub

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

### 5. Replace danlab.dev homepage with v66 landing copy

The v66 landing copy is in `agent-work/dan1-landing-copy.md`. Hero has the price-anchor line: "Snap is $2,195. We are $145–180 BOM."

**Path A (fast):** Push to zo.space at `/?t=space` and alias to danlab.dev via DNS.
**Path B (right):** Build a Vite+React Site at `Projects/danlab-site/`, deploy to a published site, custom domain.

**Recommend Path A** for week 26. Iterate to Path B in week 27-28.

---

## Wednesday 2026-06-25 — Snap-week Reddit post-mortem

### 6. Post on r/LocalLLaMA

Title: "Snap's $2,195 AR glasses vs. a $300 laptop running danlab-multimodal"

Body: see v66 content calendar Wednesday 06-25 section.

---

## Thursday 2026-06-26 — Illinois HB4843 thread + Telegram public

### 7. Illinois HB4843 thread (NEW in v66)

5 tweets. Frame as compliance posture, not marketing. Full drafts in v66 content calendar Thursday 06-26 section.

### 8. Flip @danlab_bot to public on Telegram

- Flip channel to public.
- Set channel username: `@danlab_dev` (or `@danlab_bot` if taken).
- Pin the v66 pinned tweet as the channel description.
- Approve-join mode ON; read-only for non-admins.

---

## Friday 2026-06-27 — Snap-week X thread

### 9. 7-tweet thread: "What Snap's $2,195 Specs means for the open-source alternative"

Full drafts in v66 content calendar Friday 06-27 section.

---

## Saturday 2026-06-28 — rest day

No posts.

---

## Sunday 2026-06-29 — Week-in-review + Show HN prep

### 10. LinkedIn longform + YouTube 5-min screen cast

Full drafts in v66 content calendar Sunday 06-29 section.

---

## Monday 2026-06-30 — Show HN

### 11. Submit DanClaw Phase 1 to Hacker News (v66 draft — points to real repo)

```text
Title: Show HN: DanClaw – A multi-agent orchestration system for one-person companies

Body:

Hey HN,

We're somdipto + Dan from danlab.dev in Bengaluru, India. We're building a multi-agent orchestration system called DanClaw. Today we're open-sourcing Phase 1.

What is it?

DanClaw is a Node.js + TypeScript system for running a "one-person company" — a fleet of AI agents with org charts, budgets, governance, and goal alignment. You bring your own agents (tested with Claude Code + Codex). DanClaw gives you the company.

What's in Phase 1?

- 7-agent org chart with delegation
- Per-agent budgets with cost governance
- Goal alignment from task → project → company
- Audit log + observability
- Mobile dashboard (Flutter)
- Telegram integration via OpenClaw

Receipts:
- Repo: github.com/somdipto/danclaw  (real monorepo, not a tarball)
- License: MIT
- Demo: danlab.dev/danclaw
- Architecture: github.com/somdipto/danclaw/blob/main/ARCHITECTURE.md

What it is NOT:
- Not a SaaS. Self-hosted.
- Not a replacement for a human team. It's for the case where the team is 1.5 humans.
- Not finished. Phase 1 is the foundation. Phase 2 is on the roadmap.

Happy to answer any questions about the architecture, the agent selection, or the run log. The run log is the proof.

— somdipto + Dan
```

Best time: 14:00 PT = 02:30 IST Tue 07-01. **v66 change: title drops "from India" — lead with the architecture, not the origin.**

---

## Open when convenient

- **Telegram @danlab_bot** — flip to public in OpenClaw config (1 line)
- **Twitter @danlab_dev** — claim handle, post the v66 pinned tweet
- **danlab-agent-domains / danlab-channel** — scaffold the .md AGENTS.md files

---

## What v66 changes from v65 punchlist

- Mon: audiod v0.6 → **audiod v0.7** (Tauri client)
- Mon: New optional Snap-week anchor tweet
- Wed: New "Snap's $2,195 vs $300 laptop" Reddit post
- Thu: New Illinois HB4843 thread (compliance posture, file for press)
- Fri: New "What Snap's $2,195 Specs means for open-source" X thread
- Mon 06-30: Show HN title drops "from India" — lead with architecture

**Filed under:** `agent-work/dan1-v66-punchlist.md`
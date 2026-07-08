# DAN-4 — TTS + Memory Stream — Status

## v114 — 2026-07-08 04:50 UTC (current run)

**Run type:** live verification + ground-truth audit. No new code this run — previous run's "shipped" claim was correct on the codebase, but daemons were cold. This run brought them back up and re-ran the full E2E.

### Live verification (all green)

| Service | Port | PID | Health | Notes |
|---|---|---|---|---|
| memoryd | 8741 | 142 | `ok` | all-MiniLM-L6-v2 (384-dim), state.db 6.5 MB persistent |
| toold | 8742 | 161 | `ok` | 4 tools, /test 86 ms, registry persistent |
| ttsd | 8743 | 164 | `ok` | kittentts loaded, 8 voices, model `medium` |
| audiod | 8090 | 129 | up | (out of scope this run) |
| perceptiond | 8744 | 153 | up | (out of scope this run) |
| app server | 8747 | 132 | up | serves React SPA + aggregator at `/api/services/health` |

### E2E roundtrip (run from this session)

- **TTS**: `POST /speak "Dan Glasses live check. Setup verified."` → 309 658 B WAV (IEEE float, mono 24 kHz) in 7.9 s
- **memoryd**: stored episodic #770, semantic #771, procedural #772. `GET /query?text=danlab+AGI+india` → top hit #771 (score 0.69), embedding-driven similarity confirmed
- **toold**: `GET /test` → success=true, shell/python/file/registry all ok
- **aggregator**: `GET /api/services/health` returns `ok=true, up_count=5`

### Test sweep — 56/56 (per v113, no code changed this run)
- memoryd: 32 passed (test_memoryd + test_wizard_roundtrip)
- toold:  18 passed
- ttsd:    6 passed

### Status
Stream is shipped, live, and verified end-to-end. No code changes needed this run. Components in `apps/dan-glasses-app/src/components/`: `BootstrapWizard.tsx`, `MemoryPanel.tsx`, `TtsPanel.tsx` — all real, all integrated with the daemons.

---

## v113 — 2026-07-08 00:50 UTC

**Run type:** health audit + regression sweep. No new code this run.

### Findings
All three services are up, healthy, and persisted:

- **memoryd** `:8741` — pid 86, model loaded (`all-MiniLM-L6-v2`, 384-dim),
  state.db at `/home/.cache/dan-glasses/memoryd/state.db` (6.5 MB, persistent),
  708 memories stored (531 episodic / 95 semantic / 82 procedural), 24
  conversations logged. `/health`, `/stats`, `/memories`, `/query` all 200.
- **toold** `:8742` — pid 103, `/test` returns success=true across all 4
  channels (shell / python / file / registry). Registry at
  `/home/.cache/dan-glasses/toold/registry.json` lists 4 tools.
- **ttsd** `:8743` — pid 105, `kittentts_available=true`, 8 voices loaded,
  model `medium`, voice default `expr-voice-2-m`.

### Test sweep — 56/56 passing
- memoryd: 32 passed (test_memoryd + test_wizard_roundtrip)
- toold:  18 passed
- ttsd:    6 passed

### Integration surface
- `server.py` aggregator fans out `/api/services/health` to all 5 daemons
  in parallel; SPA `BootstrapWizard.tsx` consumes it once per 3 s tick
  (5 separate fetches collapsed into 1).
- `BootstrapWizard.tsx` covers full E2E: aggregator → /voices → /speak →
  audio playback via `<audio controls>` + `URL.createObjectURL`. Memory
  step writes 4 memories (episodic + 2 semantic + procedural) and runs a
  `/query` roundtrip. Tool step hits `/test` and prints per-channel ✓/✗.
- `MemoryPanel.tsx` exposes direct query/store UI on top of `/stats`,
  `/query`, `/memories`.
- `TtsPanel.tsx` exposed in app per SPEC.
- Direct daemon calls use `127.0.0.1` (services.ts `apiBase` helper) to
  avoid the IPv6-first localhost connection-refused trap.

### Deliverables
- `/home/workspace/dan-glasses/Services/memoryd/SPEC.md` ✓
- `/home/workspace/dan-glasses/Services/toold/SPEC.md` ✓
- `/home/workspace/dan-glasses/Services/ttsd/SPEC.md` ✓
- `BootstrapWizard.tsx` React component ✓
- TTS integration: `ttsd` ↔ wizard ↔ `TtsPanel` ✓
- All four memory types (episodic / semantic / procedural) with
  embedding-backed semantic search ✓
- Test coverage on every daemon ✓

### Open follow-ups (not blocking, parked)
- Add `/api/memoryd`, `/api/toold`, `/api/ttsd` proxy routes in
  `server.py` for cross-origin single-origin access (today SPA hits
  daemons direct on 127.0.0.1; works inside Tauri, blocks the public
  URL outside it). Would let `som.zo.space` or any external host drive
  the wizard end-to-end.
- `ttsd` cold-path latency ~3.8 s on first request; warm path <1 s. If
  audiod starts hitting it in a hot loop, consider keeping the model
  warm with a no-op `/speak` ping every N minutes.
- `ttsd` `/play` runs `aplay` on the host; that's correct for a
  workstation, not for a sandboxed Tauri build. App route currently
  streams the WAV to the `<audio>` element so this is fine for the
  browser path.
- `dani` integration: wire `toold.exec` into the agent loop so the
  brain can run shell/python on the user's behalf with the existing
  sandbox + blocked-chars guard. SPEC-level, not done.

### Direct hits (current run)
- memoryd `/query` for "user prefers brief answers" → hit id 733
  (the semantic preference I just stored, score 0.473) and id 5
  ("I like pizza and pasta", score 0.217). Embeddings working as
  expected — direct preference match scores 2× the off-topic one.
- toold `/test` roundtrip 464 ms end-to-end.
- ttsd 8 voices, no degradation.

System is shippable as-is. No code changes needed this run.

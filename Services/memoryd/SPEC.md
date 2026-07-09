# memoryd — Semantic Memory Service (v113)

## Purpose
Stores conversations + memories in SQLite, embeds them with sentence-transformers, and serves semantic-similarity queries over three memory kinds: episodic (what happened when), semantic (facts/preferences), procedural (how-tos).

## Architecture
```
text input → embed (sentence-transformers/all-MiniLM-L6-v2, 384-d) → store (SQLite + embedding BLOB) → query (cosine via numpy) → top-k results
```

The embedding model is **lazy-loaded in a thread** on first request so FastAPI binds `:8741` in <1s; `/ready` gates on model load completion. Cold-load budget: 180s.

## Database Schema

### `memories`
- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `type` TEXT NOT NULL  — one of `episodic | semantic | procedural`
- `content` TEXT NOT NULL
- `embedding` BLOB NOT NULL  — JSON-encoded `list[float]` of length 384
- `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
- `metadata` JSON

### `conversations`
- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `role` TEXT NOT NULL  — `user | assistant | system`
- `content` TEXT NOT NULL
- `embedding` BLOB NOT NULL
- `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
- `session_id` TEXT NOT NULL

### Indexes
- `idx_mem_type` on `memories(type)`
- `idx_mem_created` on `memories(created_at)`
- `idx_conv_session` on `conversations(session_id)`

### Pragmas
- `journal_mode=WAL`
- `synchronous=NORMAL`

### Storage
- Default: `/home/workspace/.cache/dan-glasses/memoryd/state.db` (persistent across reboots)
- Override: `MEMORYD_DB` env var

## Embedding Model
- `sentence-transformers/all-MiniLM-L6-v2` (override via `MEMORYD_MODEL`)
- Dim: 384
- **Lazy import** of `sentence_transformers` inside `load_model_blocking` to keep cold-start under supervisor `startsecs`

## API Endpoints

### `GET /health`
Liveness; always 200. `status` is `"ok"` once the model is loaded, `"loading"` otherwise. Includes `db_path`, `db_persistent`, `db_size_bytes`.
```json
{"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2","db_path":"/home/workspace/.cache/dan-glasses/memoryd/state.db","db_persistent":true,"db_size_bytes":12120064}
```

### `GET /ready`
Readiness gate — 200 only when model is loaded AND DB is reachable. Used by BootstrapWizard and supervisors.
```json
{"ready":true,"model":"sentence-transformers/all-MiniLM-L6-v2","dim":384,"db":"/home/workspace/.cache/dan-glasses/memoryd/state.db"}
```

### `POST /memories`
Store a memory. Body: `{type, content, metadata?}`. Embeds content, writes row. Returns `{id, embedding_id}`.
- 400 on invalid `type`.

### `POST /conversations`
Store a conversation turn. Body: `{role, content, session_id}`. Returns `{id}`.

### `GET /query?text=…&top_k=5&memory_type=…`
Cosine-similarity search over memories. `memory_type` optional filter. Results sorted by score desc, then `created_at` desc.
```json
[{"id":298,"type":"episodic","content":"…","score":0.5783,"created_at":"2026-07-07 08:49:48"}]
```

### `GET /memories?type=…&limit=20`
List memories, newest first. Type filter optional.

### `GET /memories/by-type/{type}?limit=20`
List memories filtered by type, newest first. 400 on invalid type.

### `GET /memories/{id}`
Single memory lookup. 404 if absent.

### `DELETE /memories/{id}`
Delete by id. Returns `{deleted: id}`. 404 if absent.

### `GET /stats`
Aggregate counts.
```json
{
  "total_memories": 1329,
  "by_type": {"episodic": 1065, "semantic": 145, "procedural": 119},
  "conversations": 33,
  "db_size_bytes": 12120064,
  "db_path": "…",
  "model": "sentence-transformers/all-MiniLM-L6-v2",
  "dim": 384,
  "model_loaded": true
}
```

### `POST /v1/embeddings`
OpenAI-compatible endpoint used by OpenClaw memory-core.
```json
{"input": ["t1", "t2"], "model": "all-MiniLM-L6-v2"}
```
Returns `object: list` of `{object: embedding, embedding: list[384], index}` plus `model`, `usage`.

## Memory Types
- **episodic** — what happened when (events, sessions, observations)
- **semantic** — facts, preferences, learned concepts
- **procedural** — how-to knowledge, workflows

## Concurrency
- Single `asyncio.Lock` (`db_lock`) serializes writes
- Embedding work runs in a thread via `asyncio.to_thread` so the loop stays responsive
- Cosine scoring vectorized via `numpy.linalg.norm` + `mat @ q`

## Port
- `8741` (override via `MEMORYD_PORT`)

## Dependencies (`requirements.txt`)
- `fastapi`
- `uvicorn`
- `aiosqlite`
- `numpy`
- `pydantic`
- `sentence-transformers` (lazy-imported, pulls torch + transformers + sklearn + scipy)

## Tests (32)
- `test_memoryd.py` — 17 tests: health, /ready polling, all 3 memory types, invalid type, conversation, query + type filter, list, by-type, by-id, 404, delete, stats, OpenAI embeddings
- `test_wizard_roundtrip.py` — 15 tests: end-to-end through dan-glasses-app proxy (memory, tools, TTS, devices)

## Failure Modes
- **Slow model load** → `/health.status=loading`, `/ready=503` until ready; embedding requests queue up to 180s then 503
- **DB unwritable** → `/ready.status="db_error: …"`
- **Invalid memory type** → 400 with the valid set in message
- **Model never loads** → service still binds 8741; readiness probe catches it

## Integration
- **BootstrapWizard** polls `/api/services/health` (aggregator) every 3s; TTS/Memory steps hit `/memories` and `/v1/embeddings` directly via the dan-glasses-app reverse proxy at `:8747`
- **OpenClaw memory-core** consumes `/v1/embeddings` to mirror embeddings into its own graph

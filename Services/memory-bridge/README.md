# memory-bridge

**Version:** 0.1.0 (DAN-1 v129)
**Purpose:** Subscribe to `audiod` transcript events over WebSocket and POST each one to `memoryd` as a `episodic` memory. Idempotent on `event_id`. Auto-reconnects with backoff.

## Why

Previously, `perceptiond` wrote salient frames directly to `memoryd` (working), but `audiod` transcripts had no path into long-term memory. This bridge closes the loop: every spoken segment becomes a durable, queryable episodic memory.

## Architecture

```
audiod :8091 /stream  ──WS─→  memory-bridge  ──HTTP POST─→  memoryd :8741/memories
```

- **One direction.** Bridge does not write back to audiod.
- **No buffering.** If memoryd is down, events are dropped (logged) and the WS stream continues. Backpressure on the WS is bounded by audiod's own queue.
- **Idempotent.** Dedup window is the last 5,000 `event_id`s in memory.
- **Auditable.** Every event is appended to a sink file (default `/home/workspace/.cache/dan-glasses/memory-bridge/bridge.log`) as JSONL.

## Schema mapping

audiod event:
```json
{
  "type": "transcript",
  "event_id": "evt-...-001",
  "session_id": "sess-...",
  "seq": 12,
  "text": "Hello world",
  "start_ms": 1000,
  "end_ms": 2500,
  "confidence": 0.97,
  "ts_ms": 1720675200000
}
```
→ memoryd POST body:
```json
{
  "type": "episodic",
  "content": "Hello world",
  "metadata": {
    "source": "audiod",
    "bridge": "memory-bridge",
    "session_id": "sess-...",
    "start_ms": 1000,
    "end_ms": 2500,
    "confidence": 0.97,
    "ts_ms": 1720675200000,
    "event_id": "evt-...-001"
  }
}
```

## CLI

```bash
# Run (production)
python3 memory_bridge.py
# or with overrides
python3 memory_bridge.py \
  --audiod ws://127.0.0.1:8091/stream \
  --memoryd http://127.0.0.1:8741 \
  --sink /var/log/dan-glasses/memory-bridge.log

# E2E verify (no live mic needed)
python3 memory_bridge.py --inject
# → inject status=200 body={"id":NNNN,"embedding_id":"vec_NNNN"}
```

## Supervised

Added to `/etc/zo/supervisord-user.conf` as `[program:memory-bridge]`. Auto-start, auto-restart, log to `/dev/shm/memory-bridge.log`.

## Dependencies

Zero. Stdlib only (`socket`, `urllib`, `hashlib`, `base64`, `struct`, `threading` — wait, no threading in current impl). Pure stdlib, no `pip install` needed.

## Future

- **Real backpressure:** if memoryd is down for >N events, pause the WS read frame loop.
- **Multi-sink:** forward to Loki (audiod metrics) or to a NATS subject for fan-out.
- **Configurable memory type:** accept `type` via env or audiod event metadata to write `procedural` memories for tool calls, etc.

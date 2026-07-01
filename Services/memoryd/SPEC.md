# memoryd — Semantic Memory Service

## Purpose
Stores conversations, creates embeddings, enables semantic search across episodic/semantic/procedural memory.

## Architecture
```
text → embed(sentence-transformers) → store(SQLite + vectors) → query → results
```

## Database Schema

### memories table
- id: INTEGER PRIMARY KEY
- type: TEXT (episodic|semantic|procedural)
- content: TEXT
- embedding: BLOB (384-dim float32 via all-MiniLM-L6-v2)
- created_at: TIMESTAMP
- metadata: JSON

### conversations table
- id: INTEGER PRIMARY KEY
- role: TEXT (user|assistant|system)
- content: TEXT
- embedding: BLOB
- timestamp: TIMESTAMP
- session_id: TEXT

## API Endpoints

### GET /health
Returns: `{"status": "ok", "model": "sentence-transformers/all-MiniLM-L6-v2"}`

### POST /memories
Store a new memory. Body:
```json
{"type": "episodic|semantic|procedural", "content": "user asked about TTS", "metadata": {"session": "abc"}}
```
Returns: `{"id": 1, "embedding_id": "vec_001"}`

### POST /conversations
Store conversation turn.
```json
{"role": "user", "content": "hello", "session_id": "abc"}
```

### GET /query?text=...&top_k=5&memory_type=episodic
Semantic similarity search via cosine similarity over stored embeddings.
Returns: `[{"id": 1, "content": "...", "score": 0.92, "type": "episodic"}]`

### GET /memories?type=episodic&limit=20
List memories, optional type filter, newest first.

### GET /memories/by-type/{type}?limit=20
List memories filtered by type, newest first. 404 on bad type.

### GET /memories/{id}
Fetch a single memory by id. 404 if not found.

### DELETE /memories/{id}
Delete a memory. Returns: `{"deleted": id}`

### GET /stats
Aggregate counts. Returns:
```json
{
  "total_memories": 42,
  "by_type": {"episodic": 10, "semantic": 20, "procedural": 12},
  "conversations": 5,
  "db_size_bytes": 49152,
  "model": "sentence-transformers/all-MiniLM-L6-v2",
  "dim": 384
}
```

### POST /v1/embeddings
OpenAI-compatible embeddings endpoint, used by OpenClaw memory-core.
```json
{"input": ["text1", "text2"], "model": "all-MiniLM-L6-v2"}
```

## Memory Types
- **episodic**: what happened when (timestamps, events)
- **semantic**: facts, preferences, learned concepts
- **procedural**: how to do things, workflows

## Embedding Model
- Model: sentence-transformers/all-MiniLM-L6-v2
- Dimension: 384
- Stored as blob in SQLite

## Port
- 8741

## Dependencies
- FastAPI
- sentence-transformers
- scikit-learn (cosine similarity)
- aiosqlite
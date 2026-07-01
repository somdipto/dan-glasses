"""memoryd — Semantic Memory Service with embeddings (v109)."""

import asyncio
import json
import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

import aiosqlite
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np

logging.basicConfig(level=logging.INFO, format="[memoryd] %(message)s")
log = logging.getLogger("memoryd")

DEFAULT_PERSISTENT_DIR = Path("/home/workspace/.cache/dan-glasses/memoryd")
DEFAULT_PERSISTENT_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = os.getenv("MEMORYD_DB", str(DEFAULT_PERSISTENT_DIR / "state.db"))
MODEL_NAME = os.getenv("MEMORYD_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
DIM = 384
VALID_TYPES = ("episodic", "semantic", "procedural")

_model: Optional[SentenceTransformer] = None
_model_lock = asyncio.Lock()
_model_ready = asyncio.Event()


async def init_db() -> None:
    """Create schema, enable WAL, ensure the directory exists."""
    Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA journal_mode=WAL")
        await db.execute("PRAGMA synchronous=NORMAL")
        await db.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                content TEXT NOT NULL,
                embedding BLOB NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                metadata JSON
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                embedding BLOB NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                session_id TEXT NOT NULL
            )
        """)
        await db.execute("CREATE INDEX IF NOT EXISTS idx_mem_type ON memories(type)")
        await db.execute("CREATE INDEX IF NOT EXISTS idx_mem_created ON memories(created_at)")
        await db.execute("CREATE INDEX IF NOT EXISTS idx_conv_session ON conversations(session_id)")
        await db.commit()
    log.info("db ready at %s", DB_PATH)


def load_model_blocking() -> SentenceTransformer:
    """Synchronous model load. Runs in a thread so the event loop is free."""
    global _model
    log.info("loading embedding model: %s", MODEL_NAME)
    m = SentenceTransformer(MODEL_NAME)
    log.info("model loaded — dim=%d", m.get_sentence_embedding_dimension())
    return m


async def load_model() -> None:
    """Async wrapper that signals model readiness for /ready and /health."""
    global _model
    async with _model_lock:
        if _model is None:
            _model = await asyncio.to_thread(load_model_blocking)
            _model_ready.set()
            log.info("embedding model ready")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    # Pre-load model so first /query doesn't pay the cold-load cost.
    asyncio.create_task(load_model())
    yield


app = FastAPI(lifespan=lifespan)
db_lock = asyncio.Lock()


class MemoryInput(BaseModel):
    type: str
    content: str
    metadata: Optional[dict] = None


class ConversationInput(BaseModel):
    role: str
    content: str
    session_id: str


class QueryInput(BaseModel):
    text: str
    top_k: int = 5
    memory_type: Optional[str] = None


class EmbeddingRequest(BaseModel):
    input: list[str]
    model: Optional[str] = None


async def _ensure_model() -> SentenceTransformer:
    """Wait for the model to finish loading. Times out after 60s."""
    if _model is not None:
        return _model
    try:
        await asyncio.wait_for(_model_ready.wait(), timeout=60.0)
    except asyncio.TimeoutError:
        raise HTTPException(503, "embedding model still loading")
    return _model


def embed_sync(texts: list[str]) -> list[list[float]]:
    return _model.encode(texts, convert_to_numpy=True).tolist()


async def embed(texts: list[str]) -> list[list[float]]:
    await _ensure_model()
    return await asyncio.to_thread(embed_sync, texts)


def cosine_scores_sync(query_vec: list[float], stored_vecs: list[list[float]]) -> list[float]:
    q = np.asarray(query_vec, dtype=np.float32)
    norms = np.linalg.norm(q) + 1e-8
    mat = np.asarray(stored_vecs, dtype=np.float32)
    if mat.size == 0:
        return []
    row_norms = np.linalg.norm(mat, axis=1) + 1e-8
    return ((mat @ q) / (row_norms * norms)).tolist()


async def cosine_scores(query_vec: list[float], stored_vecs: list[list[float]]) -> list[float]:
    return await asyncio.to_thread(cosine_scores_sync, query_vec, stored_vecs)


@app.get("/health")
async def health():
    persistent_marker = "/home/workspace/.cache/"
    return {
        "status": "ok" if _model is not None else "loading",
        "model": MODEL_NAME,
        "db_path": DB_PATH,
        "db_persistent": DB_PATH.startswith(persistent_marker),
        "db_size_bytes": os.path.getsize(DB_PATH) if os.path.exists(DB_PATH) else 0,
    }


@app.get("/ready")
async def ready():
    """200 once the embedding model is loaded and the DB is reachable."""
    if not _model_ready.is_set():
        return {"ready": False, "model": MODEL_NAME, "status": "loading"}
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await (await db.execute("SELECT 1")).fetchone()
    except Exception as e:
        return {"ready": False, "model": MODEL_NAME, "status": f"db_error: {e}"}
    return {"ready": True, "model": MODEL_NAME, "dim": DIM, "db": DB_PATH}


@app.post("/memories")
async def store_memory(mem: MemoryInput):
    if mem.type not in VALID_TYPES:
        raise HTTPException(400, f"Invalid type: {mem.type}")

    emb = await embed([mem.content])
    emb_bytes = json.dumps(emb[0]).encode()

    async with db_lock:
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                "INSERT INTO memories (type, content, embedding, metadata) VALUES (?, ?, ?, ?)",
                (mem.type, mem.content, emb_bytes, json.dumps(mem.metadata or {})),
            )
            await db.commit()
            mem_id = cursor.lastrowid

    return {"id": mem_id, "embedding_id": f"vec_{mem_id}"}


@app.post("/conversations")
async def store_conversation(conv: ConversationInput):
    emb = await embed([conv.content])
    emb_bytes = json.dumps(emb[0]).encode()

    async with db_lock:
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                "INSERT INTO conversations (role, content, embedding, session_id) VALUES (?, ?, ?, ?)",
                (conv.role, conv.content, emb_bytes, conv.session_id),
            )
            await db.commit()
            conv_id = cursor.lastrowid

    return {"id": conv_id}


@app.get("/query")
async def query(text: str, top_k: int = 5, memory_type: Optional[str] = None):
    if memory_type and memory_type not in VALID_TYPES:
        raise HTTPException(400, f"Invalid memory_type: {memory_type}")

    query_emb = await embed([text])

    async with db_lock:
        async with aiosqlite.connect(DB_PATH) as db:
            if memory_type:
                rows = await db.execute(
                    "SELECT id, type, content, embedding, created_at FROM memories WHERE type = ?",
                    (memory_type,),
                )
            else:
                rows = await db.execute(
                    "SELECT id, type, content, embedding, created_at FROM memories"
                )
            all_memories = await rows.fetchall()

    if not all_memories:
        return []

    stored_vecs = [json.loads(r[3]) for r in all_memories]
    scores = await cosine_scores(query_emb[0], stored_vecs)

    # Sort by score desc, then by created_at desc as tiebreaker.
    scored = sorted(
        zip(scores, all_memories),
        key=lambda x: (-x[0], x[1][4]),
    )[:top_k]
    return [
        {"id": r[0], "type": r[1], "content": r[2], "score": round(s, 4), "created_at": r[4]}
        for s, r in scored
    ]


@app.get("/memories")
async def list_memories(type: Optional[str] = None, limit: int = 20):
    async with db_lock:
        async with aiosqlite.connect(DB_PATH) as db:
            if type:
                rows = await db.execute(
                    "SELECT id, type, content, created_at, metadata FROM memories WHERE type = ? ORDER BY created_at DESC LIMIT ?",
                    (type, limit),
                )
            else:
                rows = await db.execute(
                    "SELECT id, type, content, created_at, metadata FROM memories ORDER BY created_at DESC LIMIT ?",
                    (limit,),
                )
            cols = [d[0] for d in rows.description]
            return [dict(zip(cols, r)) for r in await rows.fetchall()]


@app.delete("/memories/{mem_id}")
async def delete_memory(mem_id: int):
    async with db_lock:
        async with aiosqlite.connect(DB_PATH) as db:
            cur = await db.execute("DELETE FROM memories WHERE id = ?", (mem_id,))
            await db.commit()
            if cur.rowcount == 0:
                raise HTTPException(404, f"Memory {mem_id} not found")
    return {"deleted": mem_id}


@app.post("/v1/embeddings")
async def openai_embeddings(req: EmbeddingRequest):
    """OpenAI-compatible embeddings endpoint for OpenClaw memory-core."""
    embs = await embed(req.input)
    return {
        "object": "list",
        "data": [
            {"object": "embedding", "embedding": e, "index": i}
            for i, e in enumerate(embs)
        ],
        "model": req.model or MODEL_NAME,
        "usage": {"prompt_tokens": 0, "total_tokens": 0},
    }


@app.get("/memories/by-type/{mem_type}")
async def list_by_type(mem_type: str, limit: int = 20):
    if mem_type not in VALID_TYPES:
        raise HTTPException(400, f"Invalid type: {mem_type}. Must be one of {VALID_TYPES}")
    async with db_lock:
        async with aiosqlite.connect(DB_PATH) as db:
            db.row_factory = aiosqlite.Row
            rows = await (
                await db.execute(
                    "SELECT id, type, content, created_at, metadata FROM memories WHERE type = ? ORDER BY created_at DESC LIMIT ?",
                    (mem_type, limit),
                )
            ).fetchall()
            return [dict(r) for r in rows]


@app.get("/memories/{mem_id}")
async def get_memory(mem_id: int):
    async with db_lock:
        async with aiosqlite.connect(DB_PATH) as db:
            db.row_factory = aiosqlite.Row
            row = await (
                await db.execute(
                    "SELECT id, type, content, created_at, metadata FROM memories WHERE id = ?",
                    (mem_id,),
                )
            ).fetchone()
            if not row:
                raise HTTPException(404, f"Memory {mem_id} not found")
            return dict(row)


@app.get("/stats")
async def stats():
    db_size = os.path.getsize(DB_PATH) if os.path.exists(DB_PATH) else 0
    async with db_lock:
        async with aiosqlite.connect(DB_PATH) as db:
            type_rows = await (
                await db.execute("SELECT type, COUNT(*) FROM memories GROUP BY type")
            ).fetchall()
            conv_count = await (
                await db.execute("SELECT COUNT(*) FROM conversations")
            ).fetchone()
            total = await (await db.execute("SELECT COUNT(*) FROM memories")).fetchone()
    by_type = {t: c for t, c in type_rows}
    for t in VALID_TYPES:
        by_type.setdefault(t, 0)
    return {
        "total_memories": total[0] if total else 0,
        "by_type": by_type,
        "conversations": conv_count[0] if conv_count else 0,
        "db_size_bytes": db_size,
        "db_path": DB_PATH,
        "model": MODEL_NAME,
        "dim": DIM,
        "model_loaded": _model is not None,
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("MEMORYD_PORT", "8741"))
    uvicorn.run(app, host="0.0.0.0", port=port)
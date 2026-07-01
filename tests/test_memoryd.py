"""Unit tests for memoryd service -- direct module imports for embed logic only."""

import sys
import os

# Add service to path
_test_dir = os.path.dirname(os.path.abspath(__file__))
_services_dir = os.path.join(_test_dir, "..", "Services")
sys.path.insert(0, os.path.join(_services_dir, "memoryd"))


def test_embed_sync():
    """Test that embed function produces correct dimensionality."""
    import memoryd

    texts = ["hello world", "test sentence embedding"]
    emb = memoryd.embed_sync(texts)
    assert len(emb) == 2
    assert len(emb[0]) == 384  # all-MiniLM-L6-v2 dimension


def test_cosine_scores():
    """Test cosine similarity scoring."""
    import asyncio
    import memoryd

    async def run():
        q = [1.0, 0.0, 0.0]
        stored = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.5, 0.5, 0.0]]
        scores = await memoryd.cosine_scores(q, stored)
        assert len(scores) == 3
        assert abs(scores[0] - 1.0) < 1e-6  # identical = 1.0
        assert scores[1] < scores[0]  # orthogonal = less than identical

    asyncio.run(run())


def test_memory_types():
    """Test valid memory types."""
    valid = ("episodic", "semantic", "procedural")
    for t in valid:
        assert t in valid
    assert "invalid" not in valid

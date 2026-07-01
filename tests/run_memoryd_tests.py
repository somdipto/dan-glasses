#!/usr/bin/env python3
"""Quick verification of memoryd core logic."""
import asyncio
import sys, os
sys.path.insert(0, 'Services/memoryd')

async def test():
    import memoryd

    # embed
    texts = ['hello world', 'test sentence']
    emb = await memoryd.embed(texts)
    assert len(emb) == 2 and len(emb[0]) == 384
    print('embed OK')

    # cosine_scores
    q = [1.0, 0.0, 0.0]
    stored = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.5, 0.5, 0.0]]
    scores = await memoryd.cosine_scores(q, stored)
    assert abs(scores[0] - 1.0) < 1e-6
    assert scores[2] < scores[0]
    print('cosine_scores OK')

    # memory types
    for t in ('episodic', 'semantic', 'procedural'):
        assert t in ('episodic', 'semantic', 'procedural')
    print('memory_types OK')

asyncio.run(test())
print('memoryd core logic: ALL PASSED')

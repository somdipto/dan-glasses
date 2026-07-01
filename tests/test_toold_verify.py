"""Run toold verification tests."""
import asyncio
import httpx

async def test():
    BASE = 'http://localhost:8742'
    async with httpx.AsyncClient(base_url=BASE, timeout=30) as c:
        r = await c.get('/health')
        assert r.status_code == 200
        print('toold health:', r.json())
        
        r = await c.post('/exec', json={'command': 'echo hello from toold', 'timeout': 10})
        assert r.status_code == 200
        data = r.json()
        assert data['success'] is True
        print('shell exec OK, duration_ms:', data['duration_ms'])
        
        r = await c.post('/exec', json={'command': 'exit 1', 'timeout': 10})
        assert r.json()['success'] is False
        print('shell failure: OK')
        
        r = await c.post('/exec', json={'command': 'echo hi; rm -rf /', 'timeout': 10})
        assert r.status_code == 400
        print('blocked chars: OK')
        
        r = await c.post('/exec/python', json={'code': 'print(42*2)', 'timeout': 10})
        assert '84' in r.json()['stdout']
        print('python exec: OK')
        
        r = await c.post('/exec/python', json={'code': 'import time; time.sleep(10)', 'timeout': 2})
        assert r.json()['success'] is False
        print('python timeout: OK')
        
        r = await c.get('/registry')
        print('registry tools:', len(r.json()['tools']))
        
        r = await c.post('/registry/shell/disable')
        assert r.json()['enabled'] is False
        r = await c.post('/registry/shell/enable')
        assert r.json()['enabled'] is True
        print('registry enable/disable: OK')
        
        r = await c.post('/exec/file', json={'filepath': '/nonexistent.py'})
        assert r.status_code == 404
        print('file not found: OK')
        
    print('toold all tests passed')

asyncio.run(test())
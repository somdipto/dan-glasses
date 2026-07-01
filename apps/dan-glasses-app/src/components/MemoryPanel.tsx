import { useEffect, useState } from 'react';
import './MemoryPanel.css';

type MemoryType = 'episodic' | 'semantic' | 'procedural';

interface MemoryRow {
  id: number;
  type: string;
  content: string;
  score?: number;
  created_at?: string;
}

interface MemoryPanelProps {
  baseUrl?: string;
}

export default function MemoryPanel({ baseUrl = 'http://localhost:8741' }: MemoryPanelProps) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<MemoryRow[]>([]);
  const [storeType, setStoreType] = useState<MemoryType>('episodic');
  const [storeContent, setStoreContent] = useState('');
  const [loading, setLoading] = useState(false);
  const [errMsg, setErrMsg] = useState<string | null>(null);
  const [stats, setStats] = useState<{ episodic?: number; semantic?: number; procedural?: number } | null>(null);

  useEffect(() => {
    refreshStats();
  }, []);

  async function refreshStats() {
    try {
      const r = await fetch(`${baseUrl}/stats`);
      if (r.ok) setStats(await r.json());
    } catch {
      // ignore — service may be down
    }
  }

  async function runQuery() {
    if (!query.trim()) return;
    setLoading(true);
    setErrMsg(null);
    try {
      const r = await fetch(`${baseUrl}/query?text=${encodeURIComponent(query)}&top_k=10`);
      if (!r.ok) throw new Error(`Query ${r.status}`);
      const data = await r.json();
      // memoryd /query returns a flat array: [{id, type, content, score}]
      setResults(Array.isArray(data) ? data : []);
    } catch (e: unknown) {
      setErrMsg(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  async function store() {
    if (!storeContent.trim()) return;
    setLoading(true);
    setErrMsg(null);
    try {
      const r = await fetch(`${baseUrl}/memories`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type: storeType, content: storeContent }),
      });
      if (!r.ok) throw new Error(`Store ${r.status}`);
      setStoreContent('');
      await refreshStats();
    } catch (e: unknown) {
      setErrMsg(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="memory-panel">
      <header className="memory-header">
        <h2>🧠 Memory</h2>
        {stats && (
          <div className="memory-stats">
            <span>episodic <b>{stats.episodic ?? 0}</b></span>
            <span>semantic <b>{stats.semantic ?? 0}</b></span>
            <span>procedural <b>{stats.procedural ?? 0}</b></span>
          </div>
        )}
      </header>

      <section className="memory-section">
        <h3>Query</h3>
        <div className="memory-row">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && runQuery()}
            placeholder="semantic search…"
            disabled={loading}
          />
          <button className="btn-primary" onClick={runQuery} disabled={loading || !query.trim()}>
            {loading ? '…' : 'Search'}
          </button>
        </div>

        {results.length > 0 && (
          <ul className="memory-list">
            {results.map((m) => (
              <li key={m.id} className="memory-item">
                <span className={`memory-type memory-type-${m.type}`}>{m.type}</span>
                <span className="memory-content">{m.content}</span>
                {m.score !== undefined && <span className="memory-score">{(m.score * 100).toFixed(0)}%</span>}
              </li>
            ))}
          </ul>
        )}
      </section>

      <section className="memory-section">
        <h3>Store</h3>
        <div className="memory-form">
          <label>
            <span>Type</span>
            <select value={storeType} onChange={(e) => setStoreType(e.target.value as MemoryType)}>
              <option value="episodic">episodic (events)</option>
              <option value="semantic">semantic (facts)</option>
              <option value="procedural">procedural (how-to)</option>
            </select>
          </label>
          <textarea
            value={storeContent}
            onChange={(e) => setStoreContent(e.target.value)}
            rows={3}
            placeholder="what to remember…"
          />
          <button className="btn-primary" onClick={store} disabled={loading || !storeContent.trim()}>
            Store
          </button>
        </div>
      </section>

      {errMsg && <div className="memory-error">{errMsg}</div>}
    </div>
  );
}

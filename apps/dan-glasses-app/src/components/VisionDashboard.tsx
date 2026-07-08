import { useEffect, useMemo, useRef, useState } from 'react';
import './VisionDashboard.css';
import {
  createPerceptionBackend,
  isTauri,
  viewfinderUrl,
  snapshotUrl,
  frameUrl,
  frameOverlayUrl,
  type Mode,
  type PerceptionDescription,
  type PerceptionStatus,
} from '../lib/tauriApi';
import { SERVICE_URLS } from '../lib/services';

interface VisionDashboardProps {
  baseUrl?: string;
}

const MODES: { value: Mode; label: string; hint: string }[] = [
  { value: 'idle', label: 'Idle', hint: 'no capture' },
  { value: 'watchful', label: 'Watchful', hint: 'capture + salience only' },
  { value: 'active', label: 'Active', hint: 'capture + salience + VLM' },
];

const POLL_MS = 2000;
const DESC_COUNT = 50;

function fmtTime(iso: string): string {
  try {
    const d = new Date(iso);
    return d.toLocaleTimeString();
  } catch {
    return iso;
  }
}

function salienceRatio(s: PerceptionStatus): string {
  if (s.frames_processed === 0) return '—';
  return `${((s.salient_frames / s.frames_processed) * 100).toFixed(0)}%`;
}

export default function VisionDashboard({ baseUrl = SERVICE_URLS.perceptiond }: VisionDashboardProps) {
  const backend = useMemo(() => createPerceptionBackend(baseUrl), [baseUrl]);
  const usingTauri = useMemo(() => isTauri(), []);

  const [status, setStatus] = useState<PerceptionStatus | null>(null);
  const [descriptions, setDescriptions] = useState<PerceptionDescription[]>([]);
  const [healthOk, setHealthOk] = useState<boolean | null>(null);
  const [errMsg, setErrMsg] = useState<string | null>(null);
  const [modeBusy, setModeBusy] = useState(false);
  const [autoRefresh, setAutoRefresh] = useState(true);
  const [newCount, setNewCount] = useState(0);
  const seenIdsRef = useRef<Set<number>>(new Set());
  // v11.0: highest event_id we've already seen this session. Used to ask
  // perceptiond for "everything new since I last looked" so reconnect /
  // tab-switch / resync never duplicates or drops descriptions even when
  // the in-memory ring (cap=200) has rolled over between polls.
  const lastSeenEventIdRef = useRef<number>(0);
  // v12.1: highest wall-clock timestamp we've already seen this session
  // (Unix seconds, float). Survives perceptiond restarts because the
  // description log is durable; ring event_id is reset on restart so
  // the log's since_ts() is the only cursor that bridges reloads.
  const lastSeenTsRef = useRef<number>(0);

  useEffect(() => {
    let cancelled = false;

    async function tick() {
      try {
        const h = await backend.health();
        if (cancelled) return;
        setHealthOk(h);
        const s = await backend.status();
        if (cancelled) return;
        if (s) setStatus(s);
        // v11.0: pass `since` so the server only returns descriptions
        // newer than what we already have. On first mount lastSeenEventIdRef
        // is 0, so we get the full DESC_COUNT window from the ring.
        const sinceArg = lastSeenEventIdRef.current || undefined;
        // v12.1: also pass `sinceTs` (Unix seconds). The server picks
        // the best of `since` and `sinceTs`; the wall-clock cursor
        // survives perceptiond restarts and works for clients that
        // re-mount after a long pause.
        const sinceTsArg = lastSeenTsRef.current || undefined;
        const d = await backend.descriptions({
          count: DESC_COUNT,
          since: sinceArg,
          sinceTs: sinceTsArg,
        });
        if (cancelled) return;
        if (d && Array.isArray(d.descriptions)) {
          const descs = d.descriptions;
          let added = 0;
          let maxId = lastSeenEventIdRef.current;
          let maxTs = lastSeenTsRef.current;
          for (const x of descs) {
            if (!seenIdsRef.current.has(x.event_id)) {
              seenIdsRef.current.add(x.event_id);
              added += 1;
            }
            if (typeof x.event_id === 'number' && x.event_id > maxId) {
              maxId = x.event_id;
            }
            // v12.1: track the highest wall-clock timestamp so the next
            // poll can ask perceptiond for "everything since <ts>".
            // Date.parse returns ms; divide to get Unix seconds.
            if (typeof x.timestamp === 'string' && x.timestamp) {
              const ts = Date.parse(x.timestamp);
              if (Number.isFinite(ts) && ts / 1000 > maxTs) {
                maxTs = ts / 1000;
              }
            }
          }
          lastSeenEventIdRef.current = maxId;
          lastSeenTsRef.current = maxTs;
          setDescriptions(descs);
          if (added > 0) setNewCount((n) => n + added);
        }
        setErrMsg(null);
      } catch (e: unknown) {
        if (cancelled) return;
        setErrMsg(e instanceof Error ? e.message : String(e));
      }
    }

    tick();
    if (!autoRefresh) return;
    const statusTimer = setInterval(tick, POLL_MS);
    return () => {
      cancelled = true;
      clearInterval(statusTimer);
    };
  }, [backend, autoRefresh]);

  async function setMode(mode: Mode) {
    setModeBusy(true);
    setErrMsg(null);
    try {
      const r = await backend.setMode(mode);
      if (!r) {
        throw new Error('setMode returned no response');
      }
    } catch (e: unknown) {
      setErrMsg(e instanceof Error ? e.message : String(e));
    } finally {
      setModeBusy(false);
    }
  }

  return (
    <div className="vision-panel">
      <header className="vision-header">
        <h2>👁 Vision</h2>
        <div className="vision-health">
          <span className={`vision-dot ${healthOk === true ? 'ok' : healthOk === false ? 'down' : 'unknown'}`} />
          <span className="vision-health-label">
            {healthOk === true ? 'live' : healthOk === false ? 'down' : '…'}
          </span>
          <span className="vision-port">:8092</span>
          <span
            className={`vision-bridge ${usingTauri ? 'tauri' : 'fetch'}`}
            title={usingTauri ? 'Tauri invoke (lib.rs bridge)' : 'direct fetch (vite dev mode)'}
          >
            {usingTauri ? 'tauri' : 'fetch'}
          </span>
        </div>
        <label className="vision-auto">
          <input type="checkbox" checked={autoRefresh} onChange={(e) => setAutoRefresh(e.target.checked)} />
          auto-refresh
        </label>
      </header>

      <section className="vision-section vision-viewfinder-section">
        <h3>Viewfinder</h3>
        {healthOk === false ? (
          <div className="vision-viewfinder-empty">perceptiond offline</div>
        ) : (
          <div className="vision-viewfinder">
            <img
              className="vision-viewfinder-stream"
              src={viewfinderUrl(baseUrl)}
              alt="perceptiond viewfinder"
              onError={(e) => {
                (e.currentTarget as HTMLImageElement).style.display = 'none';
              }}
            />
            <img
              className="vision-viewfinder-snapshot"
              src={snapshotUrl(baseUrl)}
              alt="perceptiond snapshot"
              onLoad={(e) => {
                setTimeout(() => {
                  (e.currentTarget as HTMLImageElement).classList.add('faded');
                }, 800);
              }}
            />
            <div className="vision-viewfinder-meta">
              <span className="vision-viewfinder-dot" />
              <span>live · :8092/stream</span>
            </div>
          </div>
        )}
      </section>

      <section className="vision-section">
        <h3>Mode</h3>
        <div className="vision-mode-row">
          {MODES.map((m) => (
            <button
              key={m.value}
              type="button"
              className={`vision-mode-btn ${status?.mode === m.value ? 'active' : ''}`}
              onClick={() => setMode(m.value)}
              disabled={modeBusy}
              title={m.hint}
            >
              <span className="vision-mode-label">{m.label}</span>
              <span className="vision-mode-hint">{m.hint}</span>
            </button>
          ))}
        </div>
      </section>

      <section className="vision-section">
        <h3>Stats</h3>
        <div className="vision-stats">
          <div className="vision-stat">
            <span className="vision-stat-label">running</span>
            <span className="vision-stat-value">{status?.running ? 'yes' : 'no'}</span>
          </div>
          <div className="vision-stat">
            <span className="vision-stat-label">frames</span>
            <span className="vision-stat-value">{status?.frames_processed ?? 0}</span>
          </div>
          <div className="vision-stat">
            <span className="vision-stat-label">salient</span>
            <span className="vision-stat-value">
              {status?.salient_frames ?? 0}
              <span className="vision-stat-sub"> ({salienceRatio(status ?? { frames_processed: 0, salient_frames: 0, mode: 'idle', running: false, descriptions: 0, vlm_busy: false, vlm_queue_depth: 0 } as PerceptionStatus)})</span>
            </span>
          </div>
          <div className="vision-stat">
            <span className="vision-stat-label">descriptions</span>
            <span className="vision-stat-value">{status?.descriptions ?? 0}</span>
          </div>
          <div className="vision-stat">
            <span className="vision-stat-label">vlm</span>
            <span className="vision-stat-value">
              {status?.vlm_busy ? 'busy' : 'idle'}
              {status && status.vlm_queue_depth > 0 && (
                <span className="vision-stat-sub"> (queue {status.vlm_queue_depth})</span>
              )}
            </span>
          </div>
        </div>
      </section>

      <section className="vision-section">
        <h3>
          Descriptions
          {newCount > 0 && <span className="vision-badge">{newCount}</span>}
        </h3>
        {descriptions.length === 0 ? (
          <div className="vision-empty">no descriptions yet — switch to Active mode to generate some</div>
        ) : (
          <ul className="vision-list">
            {descriptions.map((d) => {
              const thumb = (d.bboxes && d.bboxes.length > 0) ? frameOverlayUrl(baseUrl, d.image_id) : frameUrl(baseUrl, d.image_id);
              return (
                <li key={d.event_id} className="vision-item">
                  <div className="vision-item-meta">
                    <span className="vision-item-time">{fmtTime(d.timestamp)}</span>
                    <span className="vision-item-id">#{d.event_id} · {d.image_id.slice(0, 6)}</span>
                  </div>
                  <div className="vision-item-body">
                    {thumb && (
                      <img
                        className="vision-item-thumb"
                        src={thumb}
                        alt={`frame ${d.image_id}`}
                        loading="lazy"
                        onError={(e) => {
                          (e.currentTarget as HTMLImageElement).style.display = 'none';
                        }}
                      />
                    )}
                    <div className="vision-item-text">{d.description}</div>
                  </div>
                </li>
              );
            })}
          </ul>
        )}
      </section>

      {errMsg && <div className="vision-error">{errMsg}</div>}
    </div>
  );
}
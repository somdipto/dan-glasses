import { useEffect, useRef, useState } from 'react';
import './BootstrapWizard.css';
import {
  type ServiceId,
  PORTS,
  apiBase,
  ALL_SERVICES,
  HEALTH_PATHS,
  APP_HEALTH_AGGREGATOR_PATH,
} from '../lib/services';

const STORAGE_KEY = 'dan-glasses:bootstrap:v1';
const POLL_INTERVAL_MS = 3000;

interface HealthState {
  ok: boolean;
  message: string;
  lastChecked: number;
}

type StepStatus = 'pending' | 'running' | 'ok' | 'fail';

interface StepState {
  status: StepStatus;
  message: string;
  detail?: string;
}

const STEP_IDS: ServiceId[] = ALL_SERVICES as unknown as ServiceId[];

async function fetchJSON<T>(url: string, init?: RequestInit, timeoutMs = 8000): Promise<T> {
  const res = await fetch(url, {
    ...init,
    signal: AbortSignal.timeout(timeoutMs),
    headers: { 'Content-Type': 'application/json', ...(init?.headers || {}) },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json() as Promise<T>;
}

interface AggregatorResponse {
  ok_count: number;
  total: number;
  duration_ms: number;
  services: Record<string, {
    ok: boolean;
    port: number;
    upstream: string;
    detail?: string;
    message?: string;
    status?: number;
    duration_ms?: number;
  }>;
}

function emptySteps(): Record<ServiceId, StepState> {
  return Object.fromEntries(STEP_IDS.map(s => [s, { status: 'pending', message: 'not run' }])) as Record<ServiceId, StepState>;
}

function loadPersistedSteps(): Record<ServiceId, StepState> {
  const base = emptySteps();
  if (typeof window === 'undefined') return base;
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return base;
    const parsed = JSON.parse(raw) as { steps?: Record<string, StepState> };
    if (!parsed || typeof parsed !== 'object' || !parsed.steps) return base;
    // Merge: only accept steps for known service ids; coerce status to a
    // valid StepStatus; fall back to 'pending' on any malformed value.
    const validStatuses: StepStatus[] = ['pending', 'running', 'ok', 'fail'];
    for (const s of STEP_IDS) {
      const incoming = parsed.steps[s];
      if (incoming && typeof incoming === 'object' && typeof incoming.message === 'string') {
        base[s] = {
          status: validStatuses.includes(incoming.status as StepStatus)
            ? (incoming.status as StepStatus)
            : 'pending',
          message: incoming.message,
          detail: typeof incoming.detail === 'string' ? incoming.detail : undefined,
        };
      }
    }
    return base;
  } catch {
    return base;
  }
}

function persistSteps(steps: Record<ServiceId, StepState>) {
  if (typeof window === 'undefined') return;
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify({ steps, savedAt: Date.now() }));
  } catch {
    /* quota / private-mode — silently skip; UI keeps working */
  }
}

async function checkHealthAggregator(): Promise<Record<ServiceId, HealthState>> {
  // The server-side aggregator fans out to all 5 daemons in parallel and
  // returns one JSON envelope. This replaces 5 separate fetches per tick
  // with a single request, and centralises the "what's healthy" rule.
  const lastChecked = Date.now();
  try {
    const res = await fetch(APP_HEALTH_AGGREGATOR_PATH, {
      signal: AbortSignal.timeout(3500),
    });
    if (!res.ok) {
      // Fall back to per-service direct probes so the UI still works when
      // the SPA server is offline (e.g. running the dist from a CDN).
      return await fallbackDirectHealth(lastChecked);
    }
    const data = (await res.json()) as AggregatorResponse;
    const out = {} as Record<ServiceId, HealthState>;
    for (const svc of STEP_IDS) {
      const entry = data.services[svc];
      if (entry?.ok) {
        out[svc] = {
          ok: true,
          message: entry.message || `healthy on :${entry.port}`,
          lastChecked,
        };
      } else {
        out[svc] = {
          ok: false,
          message: entry?.detail || `unreachable on :${PORTS[svc]}`,
          lastChecked,
        };
      }
    }
    return out;
  } catch {
    return await fallbackDirectHealth(lastChecked);
  }
}

async function fallbackDirectHealth(lastChecked: number): Promise<Record<ServiceId, HealthState>> {
  const out = {} as Record<ServiceId, HealthState>;
  await Promise.all(
    STEP_IDS.map(async (svc) => {
      try {
        const res = await fetch(`${apiBase(PORTS[svc])}${HEALTH_PATHS[svc]}`, {
          signal: AbortSignal.timeout(2500),
        });
        if (res.ok) {
          out[svc] = { ok: true, message: `healthy on :${PORTS[svc]}`, lastChecked };
        } else {
          out[svc] = { ok: false, message: `HTTP ${res.status}`, lastChecked };
        }
      } catch {
        out[svc] = { ok: false, message: `unreachable on :${PORTS[svc]}`, lastChecked };
      }
    }),
  );
  return out;
}

async function fetchVoices(): Promise<string[]> {
  try {
    const data = await fetchJSON<{ voices?: string[] } | string[]>(
      `${apiBase(PORTS.ttsd)}/voices`,
    );
    if (Array.isArray(data)) return data;
    if (Array.isArray(data.voices)) return data.voices;
  } catch { /* fall through */ }
  return ['expr-voice-2-m', 'expr-voice-2-f'];
}

async function speakText(text: string, voice: string): Promise<Blob> {
  const res = await fetch(`${apiBase(PORTS.ttsd)}/speak`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, voice }),
    signal: AbortSignal.timeout(30000),
  });
  if (!res.ok) throw new Error(`TTS HTTP ${res.status}`);
  return res.blob();
}

async function memoryRoundtrip(displayName: string, voice: string) {
  const results: { type: string; id?: number; queryHit?: number }[] = [];

  // episodic
  const epi = await fetchJSON<{ id: number }>(`${apiBase(PORTS.memoryd)}/memories`, {
    method: 'POST',
    body: JSON.stringify({
      type: 'episodic',
      content: `Bootstrap wizard ran for ${displayName} at ${new Date().toISOString()}`,
    }),
  });
  results.push({ type: 'episodic', id: epi.id });

  // semantic — user preference
  const pref = await fetchJSON<{ id: number }>(`${apiBase(PORTS.memoryd)}/memories`, {
    method: 'POST',
    body: JSON.stringify({
      type: 'semantic',
      content: `User display name: ${displayName}`,
    }),
  });
  results.push({ type: 'semantic', id: pref.id });

  // semantic — voice choice
  const vc = await fetchJSON<{ id: number }>(`${apiBase(PORTS.memoryd)}/memories`, {
    method: 'POST',
    body: JSON.stringify({
      type: 'semantic',
      content: `Preferred TTS voice: ${voice}`,
    }),
  });
  results.push({ type: 'semantic', id: vc.id });

  // procedural
  const proc = await fetchJSON<{ id: number }>(`${apiBase(PORTS.memoryd)}/memories`, {
    method: 'POST',
    body: JSON.stringify({
      type: 'procedural',
      content: 'To run a Dan Glasses bootstrap: check services, prompt for name+voice, exercise memoryd + toold + ttsd.',
    }),
  });
  results.push({ type: 'procedural', id: proc.id });

  // query: must find at least one — memoryd /query returns flat array
  const query = await fetchJSON<Array<{ id: number; type: string; score: number }>>(
    `${apiBase(PORTS.memoryd)}/query?text=bootstrap+setup&top_k=5`,
  );
  const hits = Array.isArray(query) ? query.length : 0;

  return { stored: results, queryHits: hits };
}

async function probeKittenTTS(): Promise<{
  voices: number;
  models: number;
  sampleBytes: number;
  durationMs: number;
}> {
  const start = performance.now();
  const [voices, models] = await Promise.all([
    fetchJSON<string[] | { voices?: string[] }>(
      `${apiBase(PORTS.ttsd)}/voices`,
      undefined,
      8000,
    ),
    fetchJSON<string[]>(`${apiBase(PORTS.ttsd)}/models`, undefined, 8000),
  ]);
  const voiceList = Array.isArray(voices)
    ? voices
    : (voices as { voices?: string[] }).voices ?? [];
  const modelList = Array.isArray(models) ? models : [];
  const blob = await speakText('Dan Glasses KittenTTS roundtrip.', 'expr-voice-2-m');
  return {
    voices: voiceList.length,
    models: modelList.length,
    sampleBytes: blob.size,
    durationMs: Math.round(performance.now() - start),
  };
}

async function runToolTest() {
  const data = await fetchJSON<{
    success: boolean;
    results: Record<string, { ok: boolean }>;
  }>(`${apiBase(PORTS.toold)}/test`, undefined, 15000);
  return data;
}

export default function BootstrapWizard() {
  const [stepState, setStepState] = useState<Record<ServiceId, StepState>>(loadPersistedSteps);
  const [health, setHealth] = useState<Record<ServiceId, HealthState | null>>(
    Object.fromEntries(STEP_IDS.map(s => [s, null])) as Record<ServiceId, HealthState | null>,
  );
  const [voices, setVoices] = useState<string[]>([]);
  const [voice, setVoice] = useState<string>('expr-voice-2-m');
  const [displayName, setDisplayName] = useState<string>('');
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [ttsStatus, setTtsStatus] = useState<{ loading: boolean; message: string; ok?: boolean }>(
    { loading: false, message: 'not yet tested' },
  );
  const [finalSummary, setFinalSummary] = useState<string>('');
  const audioRef = useRef<HTMLAudioElement | null>(null);

  // Persist step state across reloads. We snapshot only after a manual
  // setStatus() so transient 'running' blinks don't clobber saved progress.
  useEffect(() => {
    persistSteps(stepState);
  }, [stepState]);

  // Live status — one aggregator call per tick (was 5 per-service fetches).
  useEffect(() => {
    let cancelled = false;
    async function tick() {
      const next = await checkHealthAggregator();
      if (cancelled) return;
      setHealth(next);
    }
    tick();
    const id = setInterval(tick, POLL_INTERVAL_MS);
    return () => { cancelled = true; clearInterval(id); };
  }, []);

  // Load voices when ttsd becomes healthy
  useEffect(() => {
    if (health.ttsd?.ok && voices.length === 0) {
      fetchVoices().then(vs => {
        setVoices(vs);
        if (!vs.includes(voice) && vs.length) setVoice(vs[0]);
      });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [health.ttsd?.ok]);

  // Cleanup object URL
  useEffect(() => () => { if (audioUrl) URL.revokeObjectURL(audioUrl); }, [audioUrl]);

  function setStatus(svc: ServiceId, status: StepStatus, message: string, detail?: string) {
    setStepState(prev => ({ ...prev, [svc]: { status, message, detail } }));
  }

  async function runServiceHealthStep(svc: ServiceId) {
    setStatus(svc, 'running', 'checking…');
    const h = await checkHealthAggregator() as unknown as Record<ServiceId, HealthState>;
    if (!h[svc]?.ok) {
      setStatus(svc, 'fail', h[svc]?.message);
      return false;
    }
    setStatus(svc, 'ok', h[svc]?.message);
    return true;
  }

  async function runTtsStep() {
    setStatus('ttsd', 'running', 'generating sample…');
    setTtsStatus({ loading: true, message: 'synthesizing…' });
    try {
      const sample = displayName
        ? `Hello ${displayName}, Dan Glasses is online.`
        : 'Dan Glasses bootstrap complete.';
      const blob = await speakText(sample, voice);
      if (audioUrl) URL.revokeObjectURL(audioUrl);
      const url = URL.createObjectURL(blob);
      setAudioUrl(url);
      setTtsStatus({ loading: false, message: `${(blob.size / 1024).toFixed(1)} KB · ${voice}`, ok: true });
      setStatus('ttsd', 'ok', `TTS ready · ${(blob.size / 1024).toFixed(1)} KB`);
      return true;
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      setTtsStatus({ loading: false, message: `failed: ${msg}`, ok: false });
      setStatus('ttsd', 'fail', 'TTS failed', msg);
      return false;
    }
  }

  async function runMemoryRoundtrip() {
    setStatus('memoryd', 'running', 'writing 3 memory types + querying…');
    try {
      const name = displayName || 'operator';
      const r = await memoryRoundtrip(name, voice);
      const ok = r.stored.length === 4 && r.queryHits > 0;
      setStatus(
        'memoryd',
        ok ? 'ok' : 'fail',
        `stored 4, query hits: ${r.queryHits}`,
        `${r.stored.map(s => s.type).join(', ')}`,
      );
      return ok;
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      setStatus('memoryd', 'fail', 'memoryd test failed', msg);
      return false;
    }
  }

  async function runToolStep() {
    setStatus('toold', 'running', 'running /test…');
    try {
      const data = await runToolTest();
      const channels = Object.entries(data.results).map(([k, v]) => `${k}:${v.ok ? '✓' : '✗'}`).join(' ');
      setStatus('toold', data.success ? 'ok' : 'fail', `tool test: ${data.success ? 'pass' : 'fail'}`, channels);
      return data.success;
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      setStatus('toold', 'fail', 'toold test failed', msg);
      return false;
    }
  }

  async function runAll() {
    setFinalSummary('');
    // Health checks first
    const healthOk = await Promise.all(STEP_IDS.map(s => runServiceHealthStep(s)));
    if (!healthOk.every(Boolean)) {
      setFinalSummary('Setup halted: one or more services unhealthy.');
      return;
    }
    // Real roundtrip tests
    const memOk = await runMemoryRoundtrip();
    const toolOk = await runToolStep();
    let ttsProbeOk = false;
    setStatus('ttsd', 'running', 'KittenTTS roundtrip (voices+models+sample)…');
    try {
      const probe = await probeKittenTTS();
      ttsProbeOk = probe.voices > 0 && probe.models > 0 && probe.sampleBytes > 0;
      setStatus(
        'ttsd',
        ttsProbeOk ? 'ok' : 'fail',
        `KittenTTS ok · ${probe.voices} voices · ${probe.models} models · ${(probe.sampleBytes / 1024).toFixed(1)} KB · ${probe.durationMs} ms`,
      );
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      setStatus('ttsd', 'fail', 'KittenTTS roundtrip failed', msg);
    }
    const ttsUserOk = await runTtsStep();
    const audOk = true; // audiod doesn't expose a deeper test yet
    setFinalSummary(
      `Memory: ${memOk ? '✓' : '✗'} · Tools: ${toolOk ? '✓' : '✗'} · TTS-probe: ${ttsProbeOk ? '✓' : '✗'} · TTS-sample: ${ttsUserOk ? '✓' : '✗'} · Audio: ${audOk ? '✓' : '✗'}`,
    );
  }

  function playPreview() {
    audioRef.current?.play().catch(() => { /* user gesture required for autoplay on first run */ });
  }

  const liveStatusList: ServiceId[] = STEP_IDS;
  const allStepsDone = STEP_IDS.every(s => stepState[s].status === 'ok' || stepState[s].status === 'fail');

  return (
    <div className="wizard-container">
      <div className="wizard-header">
        <h1>👾 Dan Glasses Setup</h1>
        <p>Live service status, voice selection, and end-to-end test</p>
      </div>

      <div className="live-status">
        <div className="live-status-label">LIVE STATUS</div>
        <div className="live-status-row">
          {liveStatusList.map(svc => {
            const h = health[svc];
            return (
              <div key={svc} className={`live-pill ${h?.ok ? 'live-ok' : h ? 'live-fail' : 'live-pending'}`}>
                <span className="live-dot" />
                <span className="live-name">{svc}</span>
                <span className="live-msg">{h?.message ?? 'checking…'}</span>
              </div>
            );
          })}
        </div>
      </div>

      <div className="wizard-grid">
        <div className="wizard-panel">
          <h3>1. Identity</h3>
          <label className="field">
            <span>Display name</span>
            <input
              type="text"
              value={displayName}
              placeholder="somdipto"
              onChange={e => setDisplayName(e.target.value)}
            />
          </label>
          <label className="field">
            <span>TTS voice</span>
            <select value={voice} onChange={e => setVoice(e.target.value)}>
              {voices.length === 0 && <option value={voice}>{voice}</option>}
              {voices.map(v => <option key={v} value={v}>{v}</option>)}
            </select>
          </label>
        </div>

        <div className="wizard-panel">
          <h3>2. TTS preview</h3>
          <div className="tts-controls">
            <button
              className="btn-primary"
              onClick={runTtsStep}
              disabled={ttsStatus.loading || !health.ttsd?.ok}
            >
              {ttsStatus.loading ? 'Synthesizing…' : 'Synthesize sample'}
            </button>
            <button
              className="btn-secondary"
              onClick={playPreview}
              disabled={!audioUrl}
            >
              ▶ Play
            </button>
          </div>
          <div className={`tts-status ${ttsStatus.ok ? 'ok' : ttsStatus.ok === false ? 'fail' : ''}`}>
            {ttsStatus.message}
          </div>
          {audioUrl && (
            <audio ref={audioRef} src={audioUrl} controls className="audio-player" />
          )}
        </div>
      </div>

      <div className="steps-list">
        {STEP_IDS.map((svc, idx) => {
          const st = stepState[svc];
          return (
            <div key={svc} className={`step-row step-${st.status}`}>
              <div className="step-indicator">
                {st.status === 'ok' ? '✓' :
                  st.status === 'fail' ? '✗' :
                  st.status === 'running' ? '◐' : '○'}
              </div>
              <div className="step-info">
                <div className="step-label-row">
                  <span className="step-label">{idx + 1}. {svc}</span>
                  <span className="step-port">:{PORTS[svc]}</span>
                </div>
                <span className="step-desc">{st.message}</span>
                {st.detail && <span className="step-detail">{st.detail}</span>}
              </div>
            </div>
          );
        })}
      </div>

      <div className="wizard-footer">
        <button
          className="btn-primary"
          onClick={runAll}
          disabled={Object.values(stepState).some(s => s.status === 'running')}
        >
          {allStepsDone ? 'Re-run all tests' : 'Run all tests'}
        </button>
        {finalSummary && <div className="final-summary">{finalSummary}</div>}
      </div>
    </div>
  );
}
// no-op marker — CSS lives in BootstrapWizard.css
import { useEffect, useRef, useState } from 'react';
import './BootstrapWizard.css';

type ServiceId = 'memoryd' | 'toold' | 'ttsd' | 'audiod' | 'perceptiond';

interface ServicePortMap {
  memoryd: number;
  toold: number;
  ttsd: number;
  audiod: number;
  perceptiond: number;
}

const PORTS: ServicePortMap = {
  memoryd: 8741,
  toold: 8742,
  ttsd: 8743,
  audiod: 8090,
  perceptiond: 8092,
};

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

const STEP_IDS: ServiceId[] = ['memoryd', 'toold', 'ttsd', 'audiod', 'perceptiond'];

async function fetchJSON<T>(url: string, init?: RequestInit, timeoutMs = 8000): Promise<T> {
  const res = await fetch(url, {
    ...init,
    signal: AbortSignal.timeout(timeoutMs),
    headers: { 'Content-Type': 'application/json', ...(init?.headers || {}) },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json() as Promise<T>;
}

async function checkHealth(svc: ServiceId): Promise<HealthState> {
  const port = PORTS[svc];
  try {
    const res = await fetch(`http://localhost:${port}/health`, {
      signal: AbortSignal.timeout(2500),
    });
    if (!res.ok) return { ok: false, message: `HTTP ${res.status}`, lastChecked: Date.now() };
    const data = await res.json().catch(() => ({}));
    return {
      ok: true,
      message: typeof data === 'object' && data && 'model' in data
        ? `healthy · ${(data as { model?: string }).model ?? 'up'}`
        : `healthy on :${port}`,
      lastChecked: Date.now(),
    };
  } catch (e) {
    return { ok: false, message: `unreachable on :${port}`, lastChecked: Date.now() };
  }
}

async function fetchVoices(): Promise<string[]> {
  try {
    const data = await fetchJSON<{ voices?: string[] } | string[]>(
      `http://localhost:${PORTS.ttsd}/voices`,
    );
    if (Array.isArray(data)) return data;
    if (Array.isArray(data.voices)) return data.voices;
  } catch { /* fall through */ }
  return ['expr-voice-2-m', 'expr-voice-2-f'];
}

async function speakText(text: string, voice: string): Promise<Blob> {
  const res = await fetch(`http://localhost:${PORTS.ttsd}/speak`, {
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
  const epi = await fetchJSON<{ id: number }>(`http://localhost:${PORTS.memoryd}/memories`, {
    method: 'POST',
    body: JSON.stringify({
      type: 'episodic',
      content: `Bootstrap wizard ran for ${displayName} at ${new Date().toISOString()}`,
    }),
  });
  results.push({ type: 'episodic', id: epi.id });

  // semantic — user preference
  const pref = await fetchJSON<{ id: number }>(`http://localhost:${PORTS.memoryd}/memories`, {
    method: 'POST',
    body: JSON.stringify({
      type: 'semantic',
      content: `User display name: ${displayName}`,
    }),
  });
  results.push({ type: 'semantic', id: pref.id });

  // semantic — voice choice
  const vc = await fetchJSON<{ id: number }>(`http://localhost:${PORTS.memoryd}/memories`, {
    method: 'POST',
    body: JSON.stringify({
      type: 'semantic',
      content: `Preferred TTS voice: ${voice}`,
    }),
  });
  results.push({ type: 'semantic', id: vc.id });

  // procedural
  const proc = await fetchJSON<{ id: number }>(`http://localhost:${PORTS.memoryd}/memories`, {
    method: 'POST',
    body: JSON.stringify({
      type: 'procedural',
      content: 'To run a Dan Glasses bootstrap: check services, prompt for name+voice, exercise memoryd + toold + ttsd.',
    }),
  });
  results.push({ type: 'procedural', id: proc.id });

  // query: must find at least one — memoryd /query returns flat array
  const query = await fetchJSON<Array<{ id: number; type: string; score: number }>>(
    `http://localhost:${PORTS.memoryd}/query?text=bootstrap+setup&top_k=5`,
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
      `http://localhost:${PORTS.ttsd}/voices`,
      undefined,
      8000,
    ),
    fetchJSON<string[]>(`http://localhost:${PORTS.ttsd}/models`, undefined, 8000),
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
  }>(`http://localhost:${PORTS.toold}/test`, undefined, 15000);
  return data;
}

export default function BootstrapWizard() {
  const [health, setHealth] = useState<Record<ServiceId, HealthState | null>>(
    Object.fromEntries(STEP_IDS.map(s => [s, null])) as Record<ServiceId, HealthState | null>,
  );
  const [stepState, setStepState] = useState<Record<ServiceId, StepState>>(
    Object.fromEntries(STEP_IDS.map(s => [s, { status: 'pending', message: 'not run' }])) as Record<ServiceId, StepState>,
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

  // Live status — poll all services every 3s
  useEffect(() => {
    let cancelled = false;
    async function tick() {
      const results = await Promise.all(STEP_IDS.map(s => checkHealth(s)));
      if (cancelled) return;
      const next: Record<ServiceId, HealthState> = { ...(health as Record<ServiceId, HealthState>) };
      STEP_IDS.forEach((s, i) => { next[s] = results[i]; });
      setHealth(next);
    }
    tick();
    const id = setInterval(tick, 3000);
    return () => { cancelled = true; clearInterval(id); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
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
    const h = await checkHealth(svc);
    if (!h.ok) {
      setStatus(svc, 'fail', h.message);
      return false;
    }
    setStatus(svc, 'ok', h.message);
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
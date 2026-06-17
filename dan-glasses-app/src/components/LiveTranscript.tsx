import { useEffect, useRef, useState, useCallback } from 'react';
import './LiveTranscript.css';

export interface TranscriptEvent {
  type: 'transcript';
  text: string;
  start_ms: number;
  end_ms: number;
  confidence: number;
  ts?: number;
}

interface PipelineStatus {
  service?: string;
  running?: boolean;
  vad_ready?: boolean;
  device?: string | null;
  sample_rate?: number | null;
  channels?: number | null;
  whisper_model?: string | null;
  segments_transcribed?: number;
  uptime_ms?: number;
}

type PipelineReachability = 'unknown' | 'ok' | 'unreachable';

interface LiveTranscriptProps {
  wsPort?: number;
  controlPort?: number;
  maxLines?: number;
  autoScroll?: boolean;
}

const WS_URL = (port: number) => `ws://localhost:${port}`;
const HTTP_URL = (port: number) => `http://localhost:${port}`;

export default function LiveTranscript({
  wsPort = 8091,
  controlPort = 8090,
  maxLines = 50,
  autoScroll = true,
}: LiveTranscriptProps) {
  const [events, setEvents] = useState<TranscriptEvent[]>([]);
  const [status, setStatus] = useState<'connecting' | 'open' | 'closed' | 'error'>('connecting');
  const wsRef = useRef<WebSocket | null>(null);
  const tailRef = useRef<HTMLDivElement | null>(null);

  const [pipeline, setPipeline] = useState<PipelineStatus | null>(null);
  const [reachability, setReachability] = useState<PipelineReachability>('unknown');
  const [pending, setPending] = useState<string | null>(null);
  const [controlError, setControlError] = useState<string | null>(null);

  // Transcript WebSocket
  useEffect(() => {
    let cancelled = false;
    let reconnectTimer: number | undefined;

    function connect() {
      if (cancelled) return;
      setStatus('connecting');
      try {
        const ws = new WebSocket(WS_URL(wsPort));
        wsRef.current = ws;

        ws.onopen = () => setStatus('open');
        ws.onclose = () => {
          setStatus('closed');
          if (!cancelled) {
            reconnectTimer = window.setTimeout(connect, 1500);
          }
        };
        ws.onerror = () => setStatus('error');
        ws.onmessage = (msg) => {
          try {
            const event = JSON.parse(msg.data) as TranscriptEvent;
            if (event.type !== 'transcript' || !event.text) return;
            setEvents((prev) => {
              const next = [...prev, { ...event, ts: Date.now() }];
              return next.slice(-maxLines);
            });
          } catch {
            // ignore malformed
          }
        };
      } catch {
        setStatus('error');
        reconnectTimer = window.setTimeout(connect, 2000);
      }
    }

    connect();
    return () => {
      cancelled = true;
      if (reconnectTimer) clearTimeout(reconnectTimer);
      wsRef.current?.close();
    };
  }, [wsPort, maxLines]);

  // Pipeline /status poller
  useEffect(() => {
    let cancelled = false;
    let timer: number | undefined;

    async function tick() {
      try {
        const resp = await fetch(`${HTTP_URL(controlPort)}/status`, { cache: 'no-store' });
        if (!resp.ok) throw new Error(`status ${resp.status}`);
        const body = (await resp.json()) as PipelineStatus;
        if (cancelled) return;
        setPipeline(body);
        setReachability('ok');
        setControlError(null);
      } catch (err) {
        if (cancelled) return;
        setReachability('unreachable');
        setPipeline(null);
        setControlError((err as Error).message);
      } finally {
        if (!cancelled) {
          timer = window.setTimeout(tick, 2000);
        }
      }
    }

    tick();
    return () => {
      cancelled = true;
      if (timer) clearTimeout(timer);
    };
  }, [controlPort]);

  useEffect(() => {
    if (autoScroll) {
      tailRef.current?.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
  }, [events, autoScroll]);

  const sendControl = useCallback(
    async (path: string) => {
      setPending(path);
      setControlError(null);
      try {
        const resp = await fetch(`${HTTP_URL(controlPort)}${path}`, { method: 'POST' });
        if (!resp.ok) {
          const txt = await resp.text();
          throw new Error(`${path} → ${resp.status}: ${txt}`);
        }
      } catch (err) {
        setControlError((err as Error).message);
      } finally {
        setPending(null);
      }
    },
    [controlPort]
  );

  const dotClass = `live-dot live-dot-${status}`;
  const statusLabel = {
    connecting: 'Connecting…',
    open: 'Live',
    closed: 'Reconnecting…',
    error: 'Error',
  }[status];

  const isRunning = pipeline?.running === true;
  const canStart = reachability === 'ok' && !isRunning && pending === null;
  const canStop = reachability === 'ok' && isRunning && pending === null;
  const canPtt = reachability === 'ok' && pending === null;

  const pipelineChipClass =
    reachability !== 'ok'
      ? 'unreachable'
      : isRunning
      ? 'running'
      : 'stopped';
  const pipelineChipLabel =
    reachability !== 'ok'
      ? 'audiod unreachable'
      : isRunning
      ? 'audiod running'
      : 'audiod stopped';
  const uptimeLabel = formatUptime(pipeline?.uptime_ms);
  const segCount = pipeline?.segments_transcribed ?? 0;

  return (
    <div className="live-transcript">
      <div className="live-transcript-header">
        <span className={dotClass} />
        <span className="live-transcript-status">{statusLabel}</span>
        <span className="live-transcript-count">{events.length} utterance{events.length === 1 ? '' : 's'}</span>
      </div>

      <div className="live-controls" role="toolbar" aria-label="audiod controls">
        <div className="live-control-group">
          <span className="live-control-label">Pipeline</span>
          <button
            type="button"
            className="live-control-button start"
            disabled={!canStart}
            onClick={() => sendControl('/start')}
            aria-label="Start audiod capture"
          >
            {pending === '/start' ? 'Starting…' : 'Start'}
          </button>
          <button
            type="button"
            className="live-control-button stop"
            disabled={!canStop}
            onClick={() => sendControl('/stop')}
            aria-label="Stop audiod capture"
          >
            {pending === '/stop' ? 'Stopping…' : 'Stop'}
          </button>
          <button
            type="button"
            className="live-control-button restart"
            disabled={!canPtt}
            onClick={() => sendControl('/restart')}
            aria-label="Restart audiod capture"
          >
            {pending === '/restart' ? 'Restarting…' : 'Restart'}
          </button>
          <button
            type="button"
            className="live-control-button ptt"
            disabled={!canPtt}
            onClick={() => sendControl('/ptt')}
            aria-label="Fire push-to-talk"
            title="Fire push-to-talk"
          >
            {pending === '/ptt' ? 'PTT…' : 'PTT'}
          </button>
        </div>

        <div className="live-control-status">
          {controlError && (
            <span className="live-control-status-chip unreachable" title={controlError}>
              {controlError}
            </span>
          )}
          <span className={`live-control-status-chip ${pipelineChipClass}`}>
            <span className="live-dot" />
            {pipelineChipLabel}
          </span>
          {reachability === 'ok' && (
            <>
              <span title="Transcribed segments since start">{segCount} seg</span>
              {uptimeLabel && <span title="audiod uptime">up {uptimeLabel}</span>}
              {pipeline?.whisper_model && (
                <span title="Whisper model" style={{ maxWidth: 180, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                  {shortModel(pipeline.whisper_model)}
                </span>
              )}
            </>
          )}
        </div>
      </div>

      <ul className="live-transcript-list">
        {events.length === 0 && (
          <li className="live-transcript-empty">Waiting for speech…</li>
        )}
        {events.map((e, i) => (
          <li key={`${e.start_ms}-${i}`} className="live-transcript-item">
            <span className="live-transcript-time">
              {formatTime(e.start_ms)}
            </span>
            <span className="live-transcript-text">{e.text}</span>
            <span className="live-transcript-confidence">
              {(e.confidence * 100).toFixed(0)}%
            </span>
          </li>
        ))}
        <div ref={tailRef} />
      </ul>
    </div>
  );
}

function formatTime(ms: number): string {
  const total = Math.floor(ms / 1000);
  const m = Math.floor(total / 60);
  const s = total % 60;
  return `${m}:${s.toString().padStart(2, '0')}`;
}

function formatUptime(ms?: number): string {
  if (ms == null) return '';
  const s = Math.floor(ms / 1000);
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = s % 60;
  if (h > 0) return `${h}h${m.toString().padStart(2, '0')}m`;
  if (m > 0) return `${m}m${sec.toString().padStart(2, '0')}s`;
  return `${sec}s`;
}

function shortModel(path: string): string {
  const base = path.split('/').pop() || path;
  return base.replace(/^ggml-/, '').replace(/\.bin$/, '');
}

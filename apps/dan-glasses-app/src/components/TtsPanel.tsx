import { useEffect, useRef, useState } from 'react';
import './TtsPanel.css';
import { SERVICE_URLS } from '../lib/services';

const VOICES = [
  'expr-voice-2-m',
  'expr-voice-2-f',
  'expr-voice-3-m',
  'expr-voice-3-f',
  'expr-voice-4-m',
  'expr-voice-4-f',
  'expr-voice-5-m',
  'expr-voice-5-f',
];

interface TtsPanelProps {
  baseUrl?: string;
}

export default function TtsPanel({ baseUrl = SERVICE_URLS.ttsd }: TtsPanelProps) {
  const [text, setText] = useState('Dan Glasses is online. Bootstrap complete.');
  const [voice, setVoice] = useState('expr-voice-2-m');
  const [status, setStatus] = useState<'idle' | 'generating' | 'playing' | 'error'>('idle');
  const [errMsg, setErrMsg] = useState<string | null>(null);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const lastUrl = useRef<string | null>(null);

  useEffect(() => {
    return () => {
      if (lastUrl.current) URL.revokeObjectURL(lastUrl.current);
    };
  }, []);

  async function generate() {
    setStatus('generating');
    setErrMsg(null);
    try {
      const res = await fetch(`${baseUrl}/speak`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, voice }),
      });
      if (!res.ok) {
        const body = await res.text();
        throw new Error(`TTS ${res.status}: ${body.slice(0, 120)}`);
      }
      const blob = await res.blob();
      if (lastUrl.current) URL.revokeObjectURL(lastUrl.current);
      const url = URL.createObjectURL(blob);
      lastUrl.current = url;
      setAudioUrl(url);
      setStatus('idle');
    } catch (e: unknown) {
      setErrMsg(e instanceof Error ? e.message : String(e));
      setStatus('error');
    }
  }

  function play() {
    const a = audioRef.current;
    if (!a || !audioUrl) return;
    a.play().then(() => setStatus('playing')).catch((e) => {
      setErrMsg(e.message);
      setStatus('error');
    });
  }

  function onEnded() {
    setStatus('idle');
  }

  return (
    <div className="tts-panel">
      <header className="tts-header">
        <h2>🔊 TTS</h2>
        <span className={`tts-status tts-status-${status}`}>{status}</span>
      </header>

      <div className="tts-form">
        <label className="tts-field">
          <span>Voice</span>
          <select value={voice} onChange={(e) => setVoice(e.target.value)} disabled={status === 'generating'}>
            {VOICES.map((v) => (
              <option key={v} value={v}>{v}</option>
            ))}
          </select>
        </label>

        <label className="tts-field">
          <span>Text</span>
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows={5}
            disabled={status === 'generating'}
            placeholder="Type something for Dan to say…"
          />
        </label>

        <div className="tts-actions">
          <button className="btn-primary" onClick={generate} disabled={status === 'generating' || !text.trim()}>
            {status === 'generating' ? 'Generating…' : 'Generate'}
          </button>
          <button className="btn-secondary" onClick={play} disabled={!audioUrl || status === 'generating'}>
            ▶ Play
          </button>
        </div>

        {errMsg && <div className="tts-error">{errMsg}</div>}

        <audio ref={audioRef} src={audioUrl ?? undefined} onEnded={onEnded} controls className="tts-audio" />
      </div>
    </div>
  );
}

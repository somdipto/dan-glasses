// Tauri API bridge — typed wrappers over lib.rs commands.
//
// Uses the official @tauri-apps/api/core invoke when running in the Tauri
// webview; falls back to direct HTTP fetch in pure-vite dev mode. Both
// paths implement the same PerceptionBackend interface so the React layer
// stays bridge-agnostic.

import { invoke, isTauri as tauriIsTauri } from '@tauri-apps/api/core';

export { tauriIsTauri };

// Tauri v2 sets __TAURI_INTERNALS__ on the window object. The official
// isTauri() helper from @tauri-apps/api/core is the canonical check.
export function isTauri(): boolean {
  try {
    return tauriIsTauri();
  } catch {
    return false;
  }
}

export type Mode = 'idle' | 'watchful' | 'active';

export interface PerceptionMemorySink {
  enabled: boolean;
  url: string | null;
  queued: number;
  queue_cap: number;
  sent: number;
  dropped: number;
  errors: number;
}

// v9.0 — salience bounding box. Coordinate system matches the salience
// frame (i.e. the per-event thumbnail's reference frame, NOT the user's
// display window). `kind` says which detector produced the rect:
//   - "face"   → Haar cascade face detection
//   - "motion" → changed-region mask bbox
export interface SalienceBBox {
  x: number;
  y: number;
  w: number;
  h: number;
  kind: 'face' | 'motion' | 'region' | string;
}

export interface PerceptionStatus {
  mode: Mode;
  running: boolean;
  frames_processed: number;
  salient_frames: number;
  descriptions: number;
  vlm_busy: boolean;
  vlm_queue_depth: number;
  vlm_invocations?: number;
  scene_skips?: number;
  scene_threshold?: number;
  motion_score?: number;
  face_count?: number;
  last_trigger_kind?: string;
  deduped_count?: number;
  dedup_skip_count?: number;
  sse_subscribers?: number;
  memory_sink?: PerceptionMemorySink;
  description_log?: PerceptionDescriptionLog | null;
  // v11.0: ring-buffer cursor fields exposed in /status.
  total_published?: number;
  ring_oldest_event_id?: number;
}

export interface PerceptionDescription {
  type: 'description';
  image_id: string;
  timestamp: string;
  description: string;
  event_id: number;
  trigger_kind?: string;
  motion_score?: number;
  // v9.0 — salience bboxes for the frame that produced this description.
  // Empty array when no detectors fired. UI uses these to draw overlays
  // on the /frames/<id>.jpg thumbnail.
  bboxes?: SalienceBBox[];
}

export interface PerceptionCursor {
  // v11.0: ring-buffer cursor for incremental polling.
  // ring_oldest_event_id + total_published lets the UI detect when the
  // requested `since` has fallen out of the ring (overflowed=true).
  ring_oldest_event_id: number;
  total_published: number;
  ring_size: number;
  ring_cap: number;
  requested_since?: number | null;
  overflowed: boolean;
}

export interface PerceptionDescriptionsResponse {
  descriptions: PerceptionDescription[];
  cursor?: PerceptionCursor | null;
}

export interface PerceptionModeResponse {
  mode: Mode;
}

export interface PerceptionBackend {
  health(): Promise<boolean>;
  status(): Promise<PerceptionStatus | null>;
  // v11.0: optional `since` event_id. Omit for "last N" (default). The
  // backend returns the cursor block so the UI can detect ring overflow.
  // v12.1: optional `sinceTs` unix seconds. Survives perceptiond restarts
  // because the log is durable. Mutually exclusive with `since`.
  descriptions(opts: { count?: number; since?: number | null; sinceTs?: number | null }): Promise<PerceptionDescriptionsResponse | null>;
  // v11.0: cursor snapshot for resume logic.
  cursor(): Promise<PerceptionCursor | null>;
  setMode(mode: Mode): Promise<PerceptionModeResponse | null>;
  streamUrl(): string | null;
  frameForId(imageId: string): Promise<Uint8Array | null>;
  memorySink(): Promise<PerceptionMemorySink | null>;
  logStats(): Promise<PerceptionDescriptionLog | null>;
}

// v12.0 — durable description log
export interface PerceptionDescriptionLog {
  path: string;
  lines: number;
  bytes: number;
  bytes_cap: number;
  lines_cap: number;
  truncated_count: number;
  first_event_id: number;
  last_event_id: number;
  first_ts: string | null;
  last_ts: string | null;
  writes: number;
  errors: number;
  enabled: boolean;
  queue_depth: number;
}

function createTauriBackend(): PerceptionBackend {
  return {
    async health(): Promise<boolean> {
      try {
        await invoke('perception_health');
        return true;
      } catch {
        return false;
      }
    },
    async status(): Promise<PerceptionStatus | null> {
      try {
        return await invoke<PerceptionStatus>('perception_status');
      } catch {
        return null;
      }
    },
    async descriptions(opts: { count?: number; since?: number | null; sinceTs?: number | null }): Promise<PerceptionDescriptionsResponse | null> {
      try {
        return await invoke<PerceptionDescriptionsResponse>('perception_descriptions', {
          count: opts.count ?? 20,
          since: opts.since ?? null,
          sinceTs: opts.sinceTs ?? null,
        });
      } catch {
        return null;
      }
    },
    async cursor(): Promise<PerceptionCursor | null> {
      try {
        return await invoke<PerceptionCursor>('perception_cursor');
      } catch {
        return null;
      }
    },
    async setMode(mode: Mode): Promise<PerceptionModeResponse | null> {
      try {
        return await invoke<PerceptionModeResponse>('perception_set_mode', { mode });
      } catch {
        return null;
      }
    },
    streamUrl(): string | null {
      return null;
    },
    async frameForId(_imageId: string): Promise<Uint8Array | null> {
      // Tauri webview loads <img src=...> directly from the public daemon URL,
      // so we don't need a byte-level bridge here. Return null as a sentinel
      // to signal "use the direct HTTP URL fallback" — the dashboard handles it.
      return null;
    },
    async memorySink(): Promise<PerceptionMemorySink | null> {
      try {
        const status = await invoke<PerceptionStatus>('perception_status');
        return status.memory_sink ?? null;
      } catch {
        return null;
      }
    },
    async logStats(): Promise<PerceptionDescriptionLog | null> {
      try {
        return await invoke<PerceptionDescriptionLog>('perception_description_log_stats');
      } catch {
        return null;
      }
    },
  };
}

function createFetchBackend(baseUrl: string): PerceptionBackend {
  return {
    async health(): Promise<boolean> {
      try {
        const r = await fetch(`${baseUrl}/health`);
        return r.ok;
      } catch {
        return false;
      }
    },
    async status(): Promise<PerceptionStatus | null> {
      try {
        const r = await fetch(`${baseUrl}/status`);
        return r.ok ? ((await r.json()) as PerceptionStatus) : null;
      } catch {
        return null;
      }
    },
    async descriptions(opts: { count?: number; since?: number | null; sinceTs?: number | null }): Promise<PerceptionDescriptionsResponse | null> {
      try {
        const params = new URLSearchParams();
        params.set('count', String(opts.count ?? 20));
        if (opts.since != null) params.set('since', String(opts.since));
        if (opts.sinceTs != null) params.set('since_ts', String(opts.sinceTs));
        const r = await fetch(`${baseUrl}/descriptions?${params.toString()}`);
        return r.ok ? ((await r.json()) as PerceptionDescriptionsResponse) : null;
      } catch {
        return null;
      }
    },
    async cursor(): Promise<PerceptionCursor | null> {
      try {
        const r = await fetch(`${baseUrl}/status`);
        if (!r.ok) return null;
        const s = (await r.json()) as PerceptionStatus;
        return {
          ring_oldest_event_id: Number((s as unknown as { ring_oldest_event_id?: number }).ring_oldest_event_id ?? 0),
          total_published: Number((s as unknown as { total_published?: number }).total_published ?? 0),
          ring_size: Number(s.descriptions ?? 0),
          ring_cap: 200,
          requested_since: null,
          overflowed: false,
        };
      } catch {
        return null;
      }
    },
    async setMode(mode: Mode): Promise<PerceptionModeResponse | null> {
      try {
        const r = await fetch(`${baseUrl}/mode`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ mode }),
        });
        return r.ok ? ((await r.json()) as PerceptionModeResponse) : null;
      } catch {
        return null;
      }
    },
    streamUrl(): string | null {
      return `${baseUrl}/stream`;
    },
    async frameForId(_imageId: string): Promise<Uint8Array | null> {
      // Tauri webview loads <img src=...> directly from the public daemon URL,
      // so we don't need a byte-level bridge here. Return null as a sentinel
      // to signal "use the direct HTTP URL fallback" — the dashboard handles it.
      return null;
    },
    async memorySink(): Promise<PerceptionMemorySink | null> {
      try {
        const r = await fetch(`${baseUrl}/status`);
        if (!r.ok) return null;
        const s = (await r.json()) as PerceptionStatus;
        return s.memory_sink ?? null;
      } catch {
        return null;
      }
    },
    async logStats(): Promise<PerceptionDescriptionLog | null> {
      try {
        const r = await fetch(`${baseUrl}/log/stats`);
        return r.ok ? ((await r.json()) as PerceptionDescriptionLog) : null;
      } catch {
        return null;
      }
    },
  };
}

export function createPerceptionBackend(baseUrl: string): PerceptionBackend {
  return isTauri() ? createTauriBackend() : createFetchBackend(baseUrl);
}

// Direct MJPEG viewfinder URL. The dashboard's <img src={...}> tag will
// follow the multipart/x-mixed-replace response and re-render on every
// frame boundary, giving a near-live preview without any WebSocket layer.
export function viewfinderUrl(baseUrl: string): string {
  return `${baseUrl}/stream`;
}

// Single-frame JPEG snapshot, used as a fallback paint while the MJPEG
// stream is warming up. Cached by the browser but we set no-store on
// the server side to force a refresh on every reload.
export function snapshotUrl(baseUrl: string): string {
  return `${baseUrl}/frame.jpg`;
}

// Per-event thumbnail URL. Each description has an image_id; this resolves
// to /frames/<image_id>.jpg which serves the JPEG the VLM actually saw.
// v9.0: by default the daemon overlays salience bboxes onto the JPEG.
// Pass `raw=true` to get the unannotated original.
export function frameUrl(baseUrl: string, imageId: string, raw = false): string | null {
  if (!imageId) return null;
  return raw ? `${baseUrl}/frames/${imageId}.jpg?raw=1` : `${baseUrl}/frames/${imageId}.jpg`;
}
// v9.0 — bbox overlay
// In non-Tauri mode the React layer can ask perceptiond to paint the
// salience rectangles onto the thumbnail at request time. The Tauri
// webview loads <img src=...> directly from the public daemon URL
// (perception_frame_url) so the helper there is a no-op.
export function frameOverlayUrl(baseUrl: string, imageId: string): string | null {
  if (!imageId) return null;
  return `${baseUrl}/frames/${imageId}.jpg`;
}

export function frameRawUrl(baseUrl: string, imageId: string): string | null {
  if (!imageId) return null;
  return `${baseUrl}/frames/${imageId}.jpg?raw=1`;
}

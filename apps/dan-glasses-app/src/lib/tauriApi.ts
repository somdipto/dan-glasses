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

export interface PerceptionStatus {
  mode: Mode;
  running: boolean;
  frames_processed: number;
  salient_frames: number;
  descriptions: number;
  vlm_busy: boolean;
  vlm_queue_depth: number;
}

export interface PerceptionDescription {
  type: 'description';
  image_id: string;
  timestamp: string;
  description: string;
  event_id: number;
}

export interface PerceptionDescriptionsResponse {
  descriptions: PerceptionDescription[];
}

export interface PerceptionModeResponse {
  mode: Mode;
}

export interface PerceptionBackend {
  health(): Promise<boolean>;
  status(): Promise<PerceptionStatus | null>;
  descriptions(count: number): Promise<PerceptionDescriptionsResponse | null>;
  setMode(mode: Mode): Promise<PerceptionModeResponse | null>;
  streamUrl(): string | null;
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
    async descriptions(count: number): Promise<PerceptionDescriptionsResponse | null> {
      try {
        return await invoke<PerceptionDescriptionsResponse>('perception_descriptions', { count });
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
    async descriptions(count: number): Promise<PerceptionDescriptionsResponse | null> {
      try {
        const r = await fetch(`${baseUrl}/descriptions?count=${count}`);
        return r.ok ? ((await r.json()) as PerceptionDescriptionsResponse) : null;
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

/**
 * Single source of truth for service endpoints in the Dan Glasses app.
 *
 * Why this file exists:
 * - Service supervisors bind 0.0.0.0:PORT (IPv4 only). The IPv6 ::1 is NOT
 *   bound, so `fetch("http://localhost:PORT")` will hit ECONNREFUSED on
 *   browsers that resolve `localhost` to `::1` first (Chrome --enable-ipv6,
 *   Firefox, Safari). Always use 127.0.0.1 via `apiBase()`.
 * - All port numbers and base-URL helpers live here so components never
 *   embed them inline. A new daemon = one line in `PORTS` + one helper.
 */

export type ServiceId = 'memoryd' | 'toold' | 'ttsd' | 'audiod' | 'perceptiond';

export interface ServicePortMap {
  memoryd: number;
  toold: number;
  ttsd: number;
  audiod: number;
  perceptiond: number;
}

export const PORTS: ServicePortMap = {
  memoryd: 8741,
  toold: 8742,
  ttsd: 8743,
  audiod: 8090,
  perceptiond: 8092,
};

export const apiBase = (port: number): string => `http://127.0.0.1:${port}`;

export const wsBase = (port: number): string => `ws://127.0.0.1:${port}`;

export const serviceUrl = (svc: ServiceId, path = '/'): string =>
  `${apiBase(PORTS[svc])}${path.startsWith('/') ? path : `/${path}`}`;

// Frozen map of fully-qualified base URLs — useful as default prop values
// for components that take a `baseUrl?: string` override.
export const SERVICE_URLS = Object.freeze({
  memoryd: apiBase(PORTS.memoryd),
  toold: apiBase(PORTS.toold),
  ttsd: apiBase(PORTS.ttsd),
  audiod: apiBase(PORTS.audiod),
  perceptiond: apiBase(PORTS.perceptiond),
} as const) satisfies Record<ServiceId, string>;

// Per-daemon health endpoint paths. The wizard's "live status" panel uses
// these to probe a single URL per service; the server's
// /api/services/health aggregator fans them out in one round trip when the
// SPA prefers a single fetch.
export const HEALTH_PATHS = Object.freeze({
  memoryd: '/health',
  toold: '/health',
  ttsd: '/health',
  audiod: '/health',
  perceptiond: '/health',
} as const) satisfies Record<ServiceId, string>;

// `appPath` is the proxied path under this SPA's origin (e.g. the dan-glasses-app
// server on :8747). `serviceUrl()` builds the *direct* URL to the daemon, which
// is what the SPA uses when running against daemons bound to 127.0.0.1 inside
// the Tauri webview. The aggregator is only available through the SPA proxy.
export const APP_HEALTH_AGGREGATOR_PATH = '/api/services/health';

export const ALL_SERVICES = [
  'memoryd',
  'toold',
  'ttsd',
  'audiod',
  'perceptiond',
] as const satisfies readonly ServiceId[];

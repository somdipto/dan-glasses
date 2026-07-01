// Dan Glasses — Tauri v2 backend
// Bridges React UI to the 7-daemon service mesh (audiod, memoryd, perceptiond, toold, ttsd, os-toold, openclaw).

use serde::{Deserialize, Serialize};

const AUDIOD_URL: &str = "http://localhost:8090";
const PERCEPTIOND_URL: &str = "http://localhost:8092";
const PERCEPTIOND_STREAM_URL: &str = "http://localhost:8092/stream";

#[derive(Debug, Serialize, Deserialize)]
pub struct DaemonStatus {
    pub name: String,
    pub url: String,
    pub healthy: bool,
    pub latency_ms: Option<u64>,
    pub version: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct AudiodStatus {
    pub status: String,
    pub service: String,
    pub running: bool,
    pub vad_ready: bool,
    pub device: Option<String>,
    pub sample_rate: Option<u32>,
    pub channels: Option<u32>,
    pub whisper_model: Option<String>,
    pub whisper_threads: Option<u32>,
    pub ptt_enabled: bool,
    pub ptt_hotkey: Option<String>,
    pub started_at_ms: Option<u64>,
    pub uptime_ms: Option<u64>,
    pub pid: Option<u32>,
    pub segments_transcribed: Option<u64>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct AudiodCommandResponse {
    pub status: String,
    pub message: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct PerceptionStatus {
    pub mode: String,
    pub running: bool,
    pub frames_processed: u64,
    pub salient_frames: u64,
    pub descriptions: u64,
    pub vlm_busy: bool,
    pub vlm_queue_depth: u64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct PerceptionDescription {
    #[serde(rename = "type")]
    pub kind: String,
    pub image_id: String,
    pub timestamp: String,
    pub description: String,
    pub event_id: u64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct PerceptionDescriptionsResponse {
    pub count: u64,
    pub descriptions: Vec<PerceptionDescription>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct PerceptionModeResponse {
    pub status: String,
    pub mode: String,
}

fn http_client(timeout_ms: u64) -> reqwest::Result<reqwest::Client> {
    reqwest::Client::builder()
        .timeout(std::time::Duration::from_millis(timeout_ms))
        .build()
}

fn perceptiond_client() -> reqwest::Result<reqwest::Client> {
    http_client(5000)
}

fn audiod_client() -> reqwest::Result<reqwest::Client> {
    http_client(2500)
}

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {name}! You've been greeted from Dan Glasses Rust core.")
}

#[tauri::command]
fn app_info() -> serde_json::Value {
    serde_json::json!({
        "app": "Dan Glasses",
        "identifier": "dev.danlab.danglasses",
        "version": env!("CARGO_PKG_VERSION"),
        "daemons": [
            { "name": "audiod",       "control_port": 8090, "ws_port": 8091, "protocol": "http+ws" },
            { "name": "memoryd",      "control_port": 8741, "protocol": "http" },
            { "name": "perceptiond",  "control_port": 8092, "protocol": "http" },
            { "name": "toold",        "control_port": 8742, "protocol": "http" },
            { "name": "ttsd",         "control_port": 8743, "protocol": "http" },
            { "name": "os-toold",     "control_port": 8744, "protocol": "http" },
            { "name": "openclaw",     "control_port": 18789, "protocol": "http" },
        ],
        "edge_target": {
            "device": "Redax aarch64",
            "dev_target": "x86_64 laptop",
        }
    })
}

#[tauri::command]
async fn daemon_ping(name: String, url: String) -> DaemonStatus {
    let started = std::time::Instant::now();
    let healthy = match http_client(750) {
        Ok(c) => match c.get(&url).send().await {
            Ok(resp) => resp.status().is_success(),
            Err(_) => false,
        },
        Err(_) => false,
    };
    DaemonStatus {
        name,
        url,
        healthy,
        latency_ms: if healthy { Some(started.elapsed().as_millis() as u64) } else { None },
        version: None,
    }
}

// ---------- audiod bridge ----------

#[tauri::command]
async fn audiod_health() -> Result<serde_json::Value, String> {
    let client = audiod_client().map_err(|e| format!("client: {e}"))?;
    let resp = client
        .get(format!("{AUDIOD_URL}/health"))
        .send()
        .await
        .map_err(|e| format!("request: {e}"))?;
    resp.json::<serde_json::Value>().await.map_err(|e| format!("parse: {e}"))
}

#[tauri::command]
async fn audiod_status() -> Result<AudiodStatus, String> {
    let client = audiod_client().map_err(|e| format!("client: {e}"))?;
    let resp = client
        .get(format!("{AUDIOD_URL}/status"))
        .send()
        .await
        .map_err(|e| format!("request: {e}"))?;
    resp.json::<AudiodStatus>().await.map_err(|e| format!("parse: {e}"))
}

async fn audiod_post(path: &str) -> Result<AudiodCommandResponse, String> {
    let client = audiod_client().map_err(|e| format!("client: {e}"))?;
    let resp = client
        .post(format!("{AUDIOD_URL}{path}"))
        .send()
        .await
        .map_err(|e| format!("request: {e}"))?;
    if !resp.status().is_success() {
        let status = resp.status();
        let text = resp.text().await.unwrap_or_default();
        return Err(format!("{path} → {status}: {text}"));
    }
    resp.json::<AudiodCommandResponse>().await.map_err(|e| format!("parse: {e}"))
}

#[tauri::command]
async fn audiod_start() -> Result<AudiodCommandResponse, String> {
    audiod_post("/start").await
}

#[tauri::command]
async fn audiod_stop() -> Result<AudiodCommandResponse, String> {
    audiod_post("/stop").await
}

#[tauri::command]
async fn audiod_restart() -> Result<AudiodCommandResponse, String> {
    audiod_post("/restart").await
}

#[tauri::command]
async fn audiod_ptt() -> Result<AudiodCommandResponse, String> {
    audiod_post("/ptt").await
}

#[tauri::command]
async fn audiod_reload() -> Result<AudiodCommandResponse, String> {
    audiod_post("/reload").await
}

#[tauri::command]
fn audiod_ws_url() -> String {
    "ws://localhost:8091/".to_string()
}

// ---------- perceptiond bridge ----------

#[tauri::command]
async fn perception_health() -> Result<serde_json::Value, String> {
    let client = perceptiond_client().map_err(|e| format!("client: {e}"))?;
    let resp = client
        .get(format!("{PERCEPTIOND_URL}/health"))
        .send()
        .await
        .map_err(|e| format!("request: {e}"))?;
    resp.json::<serde_json::Value>().await.map_err(|e| format!("parse: {e}"))
}

#[tauri::command]
async fn perception_status() -> Result<PerceptionStatus, String> {
    let client = perceptiond_client().map_err(|e| format!("client: {e}"))?;
    let resp = client
        .get(format!("{PERCEPTIOND_URL}/status"))
        .send()
        .await
        .map_err(|e| format!("request: {e}"))?;
    resp.json::<PerceptionStatus>().await.map_err(|e| format!("parse: {e}"))
}

#[tauri::command]
async fn perception_set_mode(mode: String) -> Result<PerceptionModeResponse, String> {
    if !matches!(mode.as_str(), "idle" | "watchful" | "active") {
        return Err(format!("invalid mode: {mode}"));
    }
    let client = perceptiond_client().map_err(|e| format!("client: {e}"))?;
    let resp = client
        .post(format!("{PERCEPTIOND_URL}/mode"))
        .json(&serde_json::json!({ "mode": mode }))
        .send()
        .await
        .map_err(|e| format!("request: {e}"))?;
    resp.json::<PerceptionModeResponse>().await.map_err(|e| format!("parse: {e}"))
}

#[tauri::command]
async fn perception_descriptions(count: Option<u64>) -> Result<PerceptionDescriptionsResponse, String> {
    let n = count.unwrap_or(20).min(200);
    let client = perceptiond_client().map_err(|e| format!("client: {e}"))?;
    let resp = client
        .get(format!("{PERCEPTIOND_URL}/descriptions"))
        .query(&[("count", n.to_string())])
        .send()
        .await
        .map_err(|e| format!("request: {e}"))?;
    resp.json::<PerceptionDescriptionsResponse>().await.map_err(|e| format!("parse: {e}"))
}

// Frame JPEG — used by the React dashboard and the standalone demo page.
#[tauri::command]
async fn perception_frame_jpeg() -> Result<Vec<u8>, String> {
    let client = perceptiond_client().map_err(|e| format!("client: {e}"))?;
    let resp = client
        .get(format!("{PERCEPTIOND_URL}/frame.jpg"))
        .send()
        .await
        .map_err(|e| format!("request: {e}"))?;
    if !resp.status().is_success() {
        return Err(format!("frame.jpg → {}", resp.status()));
    }
    resp.bytes().await.map(|b| b.to_vec()).map_err(|e| format!("bytes: {e}"))
}

// Viewfinder URL — the frontend uses this to build the <img src=...> for the
// MJPEG /stream endpoint. Same as tauriApi.viewfinderUrl() in dev mode.
#[tauri::command]
fn perception_stream_url() -> String {
    PERCEPTIOND_STREAM_URL.to_string()
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![
            greet,
            app_info,
            daemon_ping,
            audiod_health,
            audiod_status,
            audiod_start,
            audiod_stop,
            audiod_restart,
            audiod_ptt,
            audiod_reload,
            audiod_ws_url,
            perception_health,
            perception_status,
            perception_set_mode,
            perception_descriptions,
            perception_frame_jpeg,
            perception_stream_url,
        ])
        .run(tauri::generate_context!())
        .expect("error while running Dan Glasses application");
}

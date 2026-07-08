"""Configuration loading from YAML."""

import yaml
from pathlib import Path
from typing import Optional


DEFAULT_CONFIG = {
    "camera": {
        "device": "/dev/video0",
        "width": 640,
        "height": 480,
        "fps": 5,
    },
    "salience": {
        "motion_threshold": 0.15,
        "pixel_delta_threshold": 30,
        "background_update_interval": 30,
        "mode": "any",  # "motion" | "face" | "any"
        "face_scale_factor": 1.1,
        "face_min_neighbors": 5,
        "face_min_size": 30,
    },
    "vlm": {
        "model_path": "/home/workspace/danlab-multimodal/models/SmolVLM-256M-Q4_K_M.gguf",
        "mmproj_path": "/home/workspace/danlab-multimodal/models/mmproj-SmolVLM-256M-f16.gguf",
        "llama_cli_path": "/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli",
        "prompt": "Describe this image briefly. Focus on: people, objects, text, activities.",
        "max_tokens": 100,
        "timeout": 120,
    },
    "server": {
        "socket_path": "/var/run/perceptiond.sock",
        "mode": "stdout",
    },
    "power": {
        "mode": "watchful",
    },
    "dedup": {
        # v7.0: scene-change gate. Skip VLM if motion score hasn't changed
        # by at least `threshold` from the last triggered frame.
        # 0.0 = disabled (always run VLM on salient frames).
        # 0.02 = suppress ~80% of duplicate "orange circle" VLM calls in
        # mock-capture dev mode while still firing on real scene changes.
        "threshold": 0.02,
        # Sliding window of recent motion scores for the rolling baseline.
        "window": 5,
    },
    "memory_sink": {
        # v8.0: cross-daemon ingest hook. Each description is POSTed to
        # `url` as an episodic memory. Leave `enabled` False (or url empty)
        # to disable. The sink is fire-and-forget and never blocks the
        # publish hot path.
        "enabled": True,
        "url": "http://127.0.0.1:8741/memories",
        "timeout": 2.0,
        "queue_cap": 256,
    },
    "description_log": {
        # v12.0: durable, append-only JSONL description log. Provides
        # the cold-tier backstop for /descriptions?since=<id> so a
        # reconnecting client can replay missed events beyond the
        # in-memory ring's 200-cap window. Bounded by line count and
        # byte count; oldest lines are evicted first.
        "enabled": True,
        "path": "~/.cache/dan-glasses/perceptiond/descriptions.log",
        "lines_cap": 50000,                # ~5 days at 1 description / 10s
        "bytes_cap": 50 * 1024 * 1024,     # 50 MiB
    },
    "image_store": {
        # v10.0: persistent frame retention. Every accepted frame is
        # written to `dir` so memoryd image_id references stay resolvable
        # across the in-memory ring (50 frames) being overrun. Disk is
        # bounded by `max_bytes` (LRU eviction). Set `enabled: false` to
        # fall back to in-memory-only (v9.0 behaviour).
        "enabled": True,
        "dir": "~/.cache/dan-glasses/perceptiond/frames",
        "max_bytes": 200 * 1024 * 1024,  # 200 MiB
        "capacity": 50,                  # in-memory ring size
    },
}


def load_config(config_path: Optional[str] = None) -> dict:
    """Load config from YAML file with defaults."""
    if config_path and Path(config_path).exists():
        with open(config_path) as f:
            user = yaml.safe_load(f)
        # Merge with defaults
        cfg = DEFAULT_CONFIG.copy()
        for section, values in user.items():
            if section in cfg:
                cfg[section].update(values)
            else:
                cfg[section] = values
        return cfg

    return DEFAULT_CONFIG.copy()
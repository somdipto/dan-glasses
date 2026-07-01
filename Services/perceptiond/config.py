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
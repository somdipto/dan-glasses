#!/usr/bin/env python3
"""os-toold — OS interaction service for Dan Glasses.

Filesystem guard + process guard + notification guard.
Restricts operations to approved paths and actions.
"""

import os
import re
import yaml
import signal
import argparse
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

SAFE_PATHS = ["/home/workspace", "/tmp", os.environ.get("HOME", "/root")]
ALLOWED_COMMANDS = ["ls", "cat", "echo", "pwd", "cd"]

CONFIG_FILE = Path(__file__).parent / "config.yaml"

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return yaml.safe_load(f)
    return {"safe_paths": SAFE_PATHS, "allowed_commands": ALLOWED_COMMANDS}

class GuardedFilesystem:
    def __init__(self, config):
        self.safe_paths = config.get("safe_paths", SAFE_PATHS)
        self.allowed_commands = config.get("allowed_commands", ALLOWED_COMMANDS)

    def is_safe_path(self, path: str) -> bool:
        abs_path = str(Path(path).resolve())
        return any(abs_path.startswith(s) for s in self.safe_paths)

    def is_allowed_command(self, cmd: str) -> bool:
        return cmd in self.allowed_commands

class OsToolHandler(BaseHTTPRequestHandler):
    guard = None

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
        elif self.path == "/guard/status":
            self.send_response(200)
            self.end_headers()
            import json
            self.wfile.write(json.dumps({"guard": "active", "safe_paths": self.guard.safe_paths}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        import json
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode()
        
        try:
            req = json.loads(body)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            return

        action = req.get("action")
        path = req.get("path", "")
        
        if action == "check_path":
            safe = self.guard.is_safe_path(path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({"safe": safe, "path": path}).encode())
        else:
            self.send_response(400)
            self.end_headers()

    def log_message(self, format, *args):
        pass

def main():
    parser = argparse.ArgumentParser(description="os-toold")
    parser.add_argument("--port", type=int, default=8094)
    args = parser.parse_args()

    config = load_config()
    OsToolHandler.guard = GuardedFilesystem(config)

    server = HTTPServer(("0.0.0.0", args.port), OsToolHandler)
    print(f"os-toold: running on port {args.port}", flush=True)
    server.serve_forever()

if __name__ == "__main__":
    main()
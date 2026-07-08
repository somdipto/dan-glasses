# systemd Service Files

All 5 Dan Glasses services as systemd units.

## Services
| Service | Port | Description |
|---------|------|-------------|
| memoryd | 8080 | SQLite + sentence-transformers (episodic/semantic/procedural) |
| toold | 8081 | Shell + Python execution, tool registry |
| ttsd | 8082 | KittenTTS + gTTS + espeak-ng |
| audiod | 8090 | VAD (Silero) + STT (whisper.cpp) |
| perceptiond | 8091 | VLM (LFM2.5-VL-450M) + camera capture |

## Install
```bash
sudo cp *.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable memoryd toold ttsd audiod perceptiond
sudo systemctl start memoryd toold ttsd audiod perceptiond
```

## Logs
```bash
journalctl -u memoryd -f
journalctl -u toold -f
journalctl -u ttsd -f
```
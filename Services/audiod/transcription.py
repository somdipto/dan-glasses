"""whisper.cpp transcription runner."""

import subprocess
import tempfile
import numpy as np
import os
from typing import Optional
import re


class WhisperTranscriber:
    """Run whisper.cpp ggml inference on PCM segments."""

    def __init__(
        self,
        model_path: str = "ggml-base.bin",
        language: str = "auto",
        threads: int = 2,
    ):
        self.model_path = model_path
        self.language = language
        self.threads = threads

        # Find whisper.cpp binary
        self._bin = self._find_binary()

    def _find_binary(self) -> Optional[str]:
        """Find whisper-cli binary."""
        for path in [
            "/usr/local/bin/whisper-cli",
            "/usr/bin/whisper-cli",
            "./whisper-cli",
            "./main",
        ]:
            if os.path.exists(path):
                return path
        # Try which
        result = subprocess.run(
            ["which", "whisper-cli"], capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return None

    def transcribe(self, pcm: np.ndarray, sample_rate: int = 16000) -> dict:
        """Transcribe a PCM segment. Returns dict with text and metadata."""
        if len(pcm) < 160:
            return {"text": "", "start_ms": 0, "end_ms": 0, "confidence": 0.0}

        if self._bin is None:
            return self._mock_transcribe(pcm, sample_rate)

        # Write PCM as 16-bit mono WAV (whisper-cli only supports wav/flac/mp3/ogg, not raw)
        import tempfile
        import wave
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            raw_path = f.name
        with wave.open(raw_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(sample_rate)
            wf.writeframes(pcm.tobytes())

        try:
            cmd = [
                self._bin,
                "-m", self.model_path,
                "-f", raw_path,
                "-l", self.language,
                "-t", str(self.threads),
                "-ng",
                "-ml", "1",  # return first result immediately (low latency)
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,  # 10s timeout — short phrases don't need 30s
            )

            if result.returncode == 0:
                # whisper can emit multiple timestamped token lines; join all
                # text tokens, then strip a single BLANK_AUDIO marker if present.
                tokens = re.findall(r'\[\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}\]\s*(\S+)', result.stdout)
                text = " ".join(tokens).strip()
                if "[BLANK_AUDIO]" in text.replace(" ", "").upper() or "BLANK_AUDIO" in text.upper():
                    text = ""
                duration_ms = int(len(pcm) / sample_rate * 1000)
                return {
                    "text": text,
                    "start_ms": 0,
                    "end_ms": duration_ms,
                    "confidence": 0.9,
                }
            else:
                print(f"audiod: whisper error: {result.stderr}")
                return {"text": "", "start_ms": 0, "end_ms": 0, "confidence": 0.0}
        except subprocess.TimeoutExpired:
            print("audiod: whisper timeout")
            return {"text": "", "start_ms": 0, "end_ms": 0, "confidence": 0.0}
        except Exception as e:
            print(f"audiod: whisper exception: {e}")
            return {"text": "", "start_ms": 0, "end_ms": 0, "confidence": 0.0}
        finally:
            os.unlink(raw_path)

    def _mock_transcribe(self, pcm: np.ndarray, sample_rate: int = 16000) -> dict:
        """Mock transcription when whisper binary unavailable."""
        duration_ms = int(len(pcm) / sample_rate * 1000)
        return {
            "text": "[mock transcript - whisper not available]",
            "start_ms": 0,
            "end_ms": duration_ms,
            "confidence": 0.5,
        }
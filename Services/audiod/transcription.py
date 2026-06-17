"""whisper.cpp transcription runner."""

import json
import math
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
            json_path = raw_path + ".json"
            cmd = [
                self._bin,
                "-m", self.model_path,
                "-f", raw_path,
                "-l", self.language,
                "-t", str(self.threads),
                "-ng",
                "-ml", "1",  # return first result immediately (low latency)
                "-ojf",  # full JSON with per-token probabilities → confidence
                "-of", raw_path[:-4],  # whisper-cli appends .json
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,  # 10s timeout — short phrases don't need 30s
            )

            if result.returncode == 0:
                text, confidence, json_offsets = self._parse_output(result.stdout, json_path)
                duration_ms = int(len(pcm) / sample_rate * 1000)
                if json_offsets is not None:
                    seg_from, seg_to = json_offsets
                    # JSON offsets are absolute within the WAV; we wrote only this
                    # segment, so they double as start_ms/end_ms.
                    start_ms = int(seg_from)
                    end_ms = int(seg_to)
                else:
                    start_ms = 0
                    end_ms = duration_ms
                return {
                    "text": text,
                    "start_ms": start_ms,
                    "end_ms": end_ms,
                    "confidence": confidence,
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
            try:
                os.unlink(raw_path)
            except OSError:
                pass
            json_path = raw_path + ".json"
            if os.path.exists(json_path):
                try:
                    os.unlink(json_path)
                except OSError:
                    pass

    def _parse_output(self, stdout: str, json_path: str) -> tuple[str, float, Optional[tuple[float, float]]]:
        """Parse whisper-cli output and return (text, confidence, (seg_from_ms, seg_to_ms)).

        Prefers the JSON sidecar: it has per-token probabilities (the `p` field),
        so we can compute a real confidence. Falls back to stdout timestamps if
        the JSON file is missing (older whisper.cpp builds, or -ojf stripped).
        """
        # 1) Try the JSON sidecar first — has real per-token confidence.
        if os.path.exists(json_path):
            try:
                with open(json_path) as f:
                    payload = json.load(f)
                segments = payload.get("transcription", [])
                if segments:
                    seg = segments[0]
                    # Strip leading space whisper emits; dedupe spaces.
                    text = re.sub(r"\s+", " ", seg.get("text", "")).strip()
                    # Drop BLANK_AUDIO hallucinations (tiny model artifact).
                    bare = re.sub(r"[\s\[\]_]", "", text).upper()
                    if bare in ("", "BLANKAUDIO"):
                        text = ""
                    tokens = seg.get("tokens", [])
                    real_probs = [
                        float(t["p"]) for t in tokens
                        if isinstance(t.get("p"), (int, float))
                        and t.get("text", "").strip() not in ("[_BEG_]", "[_END_]")
                    ]
                    if real_probs:
                        # Geometric mean of token probabilities.
                        # Avoid log(0) by clipping to 1e-6.
                        clipped = [max(p, 1e-6) for p in real_probs]
                        log_mean = sum(math.log(p) for p in clipped) / len(clipped)
                        confidence = float(math.exp(log_mean))
                    else:
                        confidence = 0.0
                    offsets = seg.get("offsets") or {}
                    seg_offsets = None
                    if "from" in offsets and "to" in offsets:
                        seg_offsets = (float(offsets["from"]), float(offsets["to"]))
                    return text, confidence, seg_offsets
            except (OSError, ValueError, KeyError, TypeError) as e:
                # Corrupt JSON or schema drift — fall through to stdout.
                pass

        # 2) Stdout fallback — no real confidence, just text + heuristic.
        return self._parse_stdout(stdout), 0.0, None

    def _parse_stdout(self, stdout: str) -> str:
        """Strip whisper-cli's timestamp-header format and return text only.

        whisper-tiny emits BLANK_AUDIO as multi-line tokens; strip the
        timestamp headers, then look at the remaining content.

        Example:
          [00:00:00.000 --> 00:00:00.000]
          [00:00:00.770 --> 00:00:00.990]  BLANK
          [00:00:00.990 --> 00:00:00.990]  _
          [00:00:00.990 --> 00:00:00.990]  AUDIO
          [00:00:00.990 --> 00:00:10.000]  ]
        """
        cleaned_lines = []
        for line in stdout.splitlines():
            # Drop everything from the timestamp onward on a line
            after = re.sub(
                r'\[\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}\].*$',
                '',
                line,
            ).strip()
            if after:
                cleaned_lines.append(after)
        text = " ".join(cleaned_lines).strip()
        bare = re.sub(r'[\s\[\]_]', '', text).upper()
        if bare in ("", "BLANKAUDIO"):
            return ""
        return text

    def _mock_transcribe(self, pcm: np.ndarray, sample_rate: int = 16000) -> dict:
        """Mock transcription when whisper binary unavailable."""
        duration_ms = int(len(pcm) / sample_rate * 1000)
        return {
            "text": "[mock transcript - whisper not available]",
            "start_ms": 0,
            "end_ms": duration_ms,
            "confidence": 0.5,
        }
"""whisper.cpp transcription runner."""

import json
import math
import subprocess
import tempfile
import numpy as np
import os
from typing import Optional
import re

TIMESTAMP_PREFIX_RE = re.compile(
    r"^\s*\[\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}\]\s*"
)


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

    def reload(self, model_path: Optional[str] = None, threads: Optional[int] = None, language: Optional[str] = None) -> None:
        """Hot-swap model, threads, or language.

        Re-runs binary lookup (in case whisper-cli was installed or
        moved since startup) and re-validates the model file. Raises
        FileNotFoundError if the new model path doesn't exist; the
        caller is expected to roll back on failure.
        """
        if model_path is not None:
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"whisper model not found: {model_path}")
            self.model_path = model_path
        if threads is not None:
            self.threads = int(threads)
        if language is not None:
            self.language = language
        # Re-resolve the binary in case it changed location.
        self._bin = self._find_binary()

    def is_ready(self) -> tuple[bool, dict]:
        """Liveness probe for /health.

        Returns (ready, breakdown) where ready is True iff the
        whisper-cli binary is resolvable AND the configured model
        file exists on disk. This is a fast, side-effect-free check:
        it does NOT attempt to load the model into memory. A true
        "model loaded" probe would require holding a long-lived
        subprocess; for audiod, transcribe() is invoked per segment,
        so binary+file existence is the meaningful readiness signal
        that the pipeline can produce a transcript.

        The breakdown dict exposes each signal independently so /health
        responses and operator tooling can pinpoint the failing piece.
        """
        binary_ok = bool(self._bin)
        model_ok = bool(self.model_path) and os.path.exists(self.model_path)
        return (binary_ok and model_ok, {"binary": binary_ok, "model": model_ok})

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

    @staticmethod
    def _timeout_for(pcm: np.ndarray, sample_rate: int) -> float:
        """Subprocess timeout budget for whisper-cli.

        Adaptive: 15s base + 3s per second of audio, capped at 60s.
        Returns a float in seconds.
        """
        duration_s = len(pcm) / float(sample_rate)
        return float(min(60.0, 15.0 + 3.0 * duration_s))

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
            json_path = raw_path[:-4] + ".json"
            cmd = [
                self._bin,
                "-m", self.model_path,
                "-f", raw_path,
                "-l", self.language,
                "-t", str(self.threads),
                "-ng",
                "-ml", "1",  # return first result immediately (low latency)
                "-ojf",  # full JSON with per-token probabilities → confidence
                "-of", raw_path[:-4],  # whisper-cli writes sidecar to <of>.json
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                # Adaptive: 15s base + 3s per second of audio, capped at 60s.
                # Old fixed 10s was too tight on tiny.en under CPU pressure
                # (the test suite hammered it back-to-back and tripped
                # TimeoutExpired on the first call). Bounded so a runaway
                # segment still can't pin a thread.
                timeout=self._timeout_for(pcm, sample_rate),
            )

            if result.returncode == 0:
                text, confidence, json_offsets = self._parse_output(result.stdout, json_path)
                duration_ms = int(len(pcm) / sample_rate * 1000)
                # If whisper returned no real text (silence, BLANK_AUDIO,
                # or any hallucination we stripped), zero the timing fields
                # too — an empty event should carry zero span. JSON offsets
                # from a BLANK_AUDIO run still report a 0..duration span,
                # which is misleading downstream.
                if not text:
                    start_ms = 0
                    end_ms = 0
                elif json_offsets is not None:
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
            if os.path.exists(json_path):
                try:
                    os.unlink(json_path)
                except OSError:
                    pass

    def _parse_output(self, stdout: str, json_path: str) -> tuple[str, float, Optional[tuple[float, float]]]:
        """Parse whisper-cli output and return (text, confidence, (seg_from_ms, seg_to_ms)).

        Prefers the JSON sidecar: it has per-token probabilities (the `p` field),
        so we can compute a real confidence. Aggregates ALL transcription
        segments (whisper.cpp emits a leading empty marker segment plus one
        per token/word; ignoring the rest would drop real speech).

        Falls back to stdout timestamps if the JSON file is missing
        (older whisper.cpp builds, or -ojf stripped).
        """
        # 1) Try the JSON sidecar first — has real per-token confidence.
        if os.path.exists(json_path):
            try:
                with open(json_path) as f:
                    payload = json.load(f)
                segments = payload.get("transcription", [])
                if segments:
                    # Aggregate across all segments. whisper.cpp emits an
                    # empty leading segment ([_BEG_] marker) and one segment
                    # per token/word — only segments[0] is the empty marker,
                    # the rest are the actual utterance.
                    text_parts: list[str] = []
                    seg_from_ms: Optional[float] = None
                    seg_to_ms: Optional[float] = None
                    real_probs: list[float] = []
                    for seg in segments:
                        seg_text = seg.get("text", "")
                        tokens = seg.get("tokens", [])
                        # Treat a segment as "real" if it has tokens beyond
                        # the [_BEG_]/[_END_] markers, or has non-whitespace
                        # text after stripping markers.
                        token_texts = [
                            t.get("text", "") for t in tokens
                            if isinstance(t, dict)
                        ]
                        has_real_token = any(
                            txt.strip() not in ("[_BEG_]", "[_END_]")
                            for txt in token_texts
                        ) if token_texts else bool(seg_text.strip())
                        if not has_real_token:
                            continue
                        # Strip leading space whisper emits; dedupe spaces.
                        cleaned = re.sub(r"\s+", " ", seg_text).strip()
                        if cleaned:
                            text_parts.append(cleaned)
                        # Pull per-token probabilities (skip [_BEG_]/[_END_]).
                        for t in tokens:
                            if not isinstance(t, dict):
                                continue
                            tok_text = t.get("text", "").strip()
                            if tok_text in ("[_BEG_]", "[_END_]"):
                                continue
                            p = t.get("p")
                            if isinstance(p, (int, float)):
                                real_probs.append(float(p))
                        # Track span across all real segments.
                        offsets = seg.get("offsets") or {}
                        if "from" in offsets and "to" in offsets:
                            f_from = float(offsets["from"])
                            f_to = float(offsets["to"])
                            if seg_from_ms is None or f_from < seg_from_ms:
                                seg_from_ms = f_from
                            if seg_to_ms is None or f_to > seg_to_ms:
                                seg_to_ms = f_to
                    text = " ".join(text_parts).strip()
                    # Drop BLANK_AUDIO hallucinations (tiny model artifact).
                    bare = re.sub(r"[\s\[\]_]", "", text).upper()
                    if bare in ("", "BLANKAUDIO"):
                        text = ""
                    if real_probs:
                        # Geometric mean of token probabilities.
                        # Avoid log(0) by clipping to 1e-6.
                        clipped = [max(p, 1e-6) for p in real_probs]
                        log_mean = sum(math.log(p) for p in clipped) / len(clipped)
                        confidence = float(math.exp(log_mean))
                    else:
                        confidence = 0.0
                    seg_offsets: Optional[tuple[float, float]] = None
                    if seg_from_ms is not None and seg_to_ms is not None:
                        seg_offsets = (seg_from_ms, seg_to_ms)
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
            # Strip only the leading "[hh:mm:ss.mmm --> hh:mm:ss.mmm]" prefix.
            # Anchored at start-of-line so the rest of the line (the actual
            # token text) survives.
            after = TIMESTAMP_PREFIX_RE.sub("", line).strip()
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
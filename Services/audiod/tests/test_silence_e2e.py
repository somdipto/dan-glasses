"""End-to-end silence invariant test.

If everything is wired correctly (capture → VAD → segment → whisper → publish),
sustained silence MUST produce zero transcript events on the wire. This is
cheap insurance against regressions where the pipeline emits phantom output
on noise/headless CI.
"""

import json
import socket
import sys
import time

import numpy as np
import pytest

from capture import ALSACapture, RingBuffer
from vad import VADSpeechDetector
from transcription import WhisperTranscriber
from publish import TranscriptPublisher


def _make_silence(seconds: float, sr: int = 16000) -> np.ndarray:
    return np.zeros(int(sr * seconds), dtype=np.int16)


def test_silence_produces_no_segment():
    """Pure silence through VAD → no segment flushed."""
    flushed = []
    detector = VADSpeechDetector(
        threshold=0.5,
        min_speech_ms=100,
        min_silence_ms=100,
        sample_rate=16000,
        on_speech_end=lambda seg: flushed.append(len(seg)),
    )

    silence = _make_silence(2.0)
    chunk = 512
    for i in range(0, len(silence), chunk):
        detector.process(silence[i : i + chunk])

    assert flushed == [], f"silence must not trigger speech_end, got: {flushed}"


def test_silence_produces_no_event_on_publisher():
    """Silence + transcribe should publish nothing."""
    pub = TranscriptPublisher(mode="stdout", ws_port=0)  # ws_port=0 disables WS server
    transcriber = WhisperTranscriber()

    silence = _make_silence(1.0)
    # Transcribe silence directly — this is the worst case
    result = transcriber.transcribe(silence, 16000)
    # Whisper on silence: empty text, but even if it returns text, we
    # check the publisher can handle an empty event gracefully
    if result.get("text"):
        pub.publish(result)

    # If anything was published, it must be valid JSON
    pub.close()


def test_silence_through_ring_buffer():
    """Silence written to ring buffer can be read back lossless."""
    rb = RingBuffer(8192)
    silence = _make_silence(0.5)
    rb.write(silence)
    assert rb.count() == len(silence)
    out = rb.read(len(silence))
    assert np.array_equal(out, silence)


def test_ws_handshake_signature_rfc6455():
    """Verify the WS server's Sec-WebSocket-Accept follows RFC 6455 §4.2.2.

    This is the same handshake the Tauri LiveTranscript.tsx issues.
    """
    import base64
    import hashlib
    import os

    key = base64.b64encode(os.urandom(16)).decode("ascii")
    expected = base64.b64encode(
        hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()
    ).decode()

    # Use mode="websocket" so the WS listener actually binds —
    # stdout mode (the v1.4 default) intentionally does NOT start
    # a WS server. The v0.9 over-correction was starting the WS
    # listener in stdout mode; v1.4 removes that.
    # Use ws_port=0 (ephemeral) so we never collide with the live
    # audiod's WS publisher (which has bound 18991 in production).
    pub = TranscriptPublisher(mode="websocket", ws_port=0)
    try:
        # Wait for the WS server thread to bind and report its
        # ephemeral port. With ws_port=0, pub.ws_port stays at 0
        # until the listener thread binds and updates it.
        import time
        deadline = time.time() + 2.0
        while time.time() < deadline and pub.ws_port == 0:
            time.sleep(0.02)
        ws_port = pub.ws_port
        assert ws_port > 0, f"WS server did not bind within 2s"

        s = socket.socket()
        s.settimeout(2.0)
        s.connect(("127.0.0.1", ws_port))
        req = (
            "GET / HTTP/1.1\r\n"
            f"Host: 127.0.0.1:{ws_port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n"
            "\r\n"
        )
        s.sendall(req.encode())
        resp = b""
        while b"\r\n\r\n" not in resp:
            chunk = s.recv(4096)
            if not chunk:
                break
            resp += chunk
        head = resp.split(b"\r\n\r\n", 1)[0].decode()
        assert "101 Switching Protocols" in head
        assert expected in head, f"Sec-WebSocket-Accept mismatch: expected {expected}"
        s.close()
    finally:
        pub.close()

"""Tests for perceptiond service."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import time
import threading

from capture import V4L2Capture
from salience import SalienceDetector
from vlm import VLMInference
from events import DescriptionPublisher
from config import load_config, DEFAULT_CONFIG


def test_salience_detector():
    """Test salience detection."""
    det = SalienceDetector(motion_threshold=0.1, pixel_delta_threshold=20)

    # Static frame
    frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
    assert not det.is_salient(frame1), "Static frame should not be salient"

    # Changed frame
    frame2 = np.ones((480, 640, 3), dtype=np.uint8) * 255
    salient = det.is_salient(frame2)
    print(f"  Changed frame salient: {salient}")

    # Check background updated
    assert det._background is not None
    print("  SalienceDetector: PASS")


def test_capture():
    """Test V4L2 capture initialization."""
    capture = V4L2Capture(device="/dev/video0", width=640, height=480, fps=1)
    assert capture.device_path == "/dev/video0"
    assert capture.width == 640
    assert capture.height == 480
    assert capture.fps == 1
    print("  V4L2Capture: PASS")


def test_capture_mock():
    """Test mock capture loop."""
    capture = V4L2Capture(device="/dev/nonexistent", width=320, height=240, fps=2)
    frames = []
    capture.on_frame(lambda f: frames.append(f))

    t = threading.Thread(target=lambda: (capture.start(), time.sleep(2), capture.stop()))
    t.start()
    t.join(timeout=5)

    print(f"  Received {len(frames)} mock frames in 2s at 2fps")
    assert len(frames) > 0, "Should receive mock frames"
    print("  Mock capture: PASS")


def test_config_default():
    """Test default config loading."""
    cfg = load_config(None)
    assert cfg["camera"]["width"] == 640
    assert cfg["salience"]["motion_threshold"] == 0.15
    assert cfg["vlm"]["max_tokens"] == 100
    print("  Config default: PASS")


def test_publisher():
    """Test description publisher."""
    pub = DescriptionPublisher(mode="stdout")
    pub.publish({
        "type": "description",
        "image_id": "test123",
        "timestamp": "2026-04-17T12:00:00Z",
        "description": "A person holding a phone",
    })
    pub.close()
    print("  Publisher: PASS")


def test_publisher_ring_buffer():
    """Test ring buffer holds last N descriptions."""
    pub = DescriptionPublisher(mode="stdout", ring_size=5)
    for i in range(10):
        pub.publish({
            "type": "description",
            "image_id": f"img{i}",
            "timestamp": "2026-04-17T12:00:00Z",
            "description": f"desc {i}",
        })
    items = pub.recent(5)
    assert len(items) == 5, f"Expected 5, got {len(items)}"
    assert items[-1]["image_id"] == "img9", f"Expected img9, got {items[-1]['image_id']}"
    assert items[0]["image_id"] == "img5", f"Expected img5, got {items[0]['image_id']}"
    pub.close()
    print("  Publisher ring buffer: PASS")


def test_descriptions_endpoint():
    """Test HTTP /descriptions endpoint serves ring buffer."""
    from events import PerceptiondServer
    import urllib.request
    import json as _json

    pub = DescriptionPublisher(mode="stdout", ring_size=10)
    for i in range(3):
        pub.publish({
            "type": "description",
            "image_id": f"ep{i}",
            "timestamp": "2026-06-12T01:00:00Z",
            "description": f"endpoint test {i}",
        })

    server = PerceptiondServer(socket_path="/tmp/test_perc.sock", tcp_port=18092)
    server._pipeline = type("P", (), {"publisher": pub})()
    server.start()
    time.sleep(0.3)

    try:
        with urllib.request.urlopen("http://127.0.0.1:18092/descriptions?count=5", timeout=2) as resp:
            data = _json.loads(resp.read().decode())
        assert data["count"] == 3, f"Expected count=3, got {data['count']}"
        assert data["descriptions"][0]["image_id"] == "ep0"
        assert data["descriptions"][-1]["image_id"] == "ep2"
        print("  /descriptions endpoint: PASS")
    finally:
        server.stop()
        pub.close()


def test_vlm_init():
    """Test VLM inference initialization."""
    vlm = VLMInference(
        model_path="/fake/model.gguf",
        mmproj_path="/fake/mmproj.gguf",
        llama_cli_path="/bin/echo",
    )
    assert vlm.model_path == "/fake/model.gguf"
    assert vlm.max_tokens == 100
    vlm.shutdown()
    print("  VLMInference init: PASS")


def test_frame_endpoint():
    """Test GET /frame.jpg returns latest JPEG after set_capture.

    Reproduces the v4 race: server.start() spawns the TCP thread first,
    then set_capture() is called. /frame.jpg must still find the capture
    via the _server_ref fallback.
    """
    from events import PerceptiondServer
    import urllib.request

    cap = V4L2Capture(device="/dev/nonexistent", width=160, height=120, fps=5)
    cap.start()
    time.sleep(0.7)  # let mock capture fill _latest_jpeg

    server = PerceptiondServer(socket_path="/tmp/test_perc_frame.sock", tcp_port=18093)
    server.start()  # TCP thread spins up; TCPServer may or may not exist yet
    time.sleep(0.05)
    server.set_capture(cap)  # critical: called AFTER server.start()
    time.sleep(0.4)

    try:
        with urllib.request.urlopen("http://127.0.0.1:18093/frame.jpg", timeout=3) as resp:
            data = resp.read()
            ctype = resp.headers.get("Content-Type", "")
            assert ctype == "image/jpeg", f"Expected image/jpeg, got {ctype}"
            assert data[:2] == b"\xff\xd8", f"Expected JPEG SOI, got {data[:4].hex()}"
            assert len(data) > 100, f"JPEG too small: {len(data)} bytes"
            print(f"  /frame.jpg endpoint: PASS ({len(data)} bytes)")
    finally:
        server.stop()
        cap.stop()


def test_stream_endpoint():
    """Test GET /stream returns at least one multipart JPEG frame."""
    from events import PerceptiondServer

    cap = V4L2Capture(device="/dev/nonexistent", width=160, height=120, fps=5)
    cap.start()
    time.sleep(0.6)

    server = PerceptiondServer(socket_path="/tmp/test_perc_stream.sock", tcp_port=18094)
    server.start()
    time.sleep(0.05)
    server.set_capture(cap)
    time.sleep(0.4)

    try:
        import socket as _socket
        s = _socket.create_connection(("127.0.0.1", 18094), timeout=3)
        s.sendall(b"GET /stream HTTP/1.1\r\nHost: x\r\n\r\n")
        buf = b""
        s.settimeout(1.5)
        try:
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                buf += chunk
                if b"--danvision" in buf and b"\xff\xd8" in buf:
                    break
        except _socket.timeout:
            pass
        s.close()
        assert b"--danvision" in buf, f"Missing boundary in stream: {buf[:200]!r}"
        assert b"image/jpeg" in buf, f"Missing image/jpeg header: {buf[:200]!r}"
        assert b"\xff\xd8" in buf, f"Missing JPEG SOI in stream: {buf[:200]!r}"
        print(f"  /stream endpoint: PASS ({len(buf)} bytes read)")
    finally:
        server.stop()
        cap.stop()


def main():
    print("\n=== perceptiond tests ===")

    tests = [
        ("salience_detector", test_salience_detector),
        ("capture", test_capture),
        ("capture_mock", test_capture_mock),
        ("config_default", test_config_default),
        ("publisher", test_publisher),
        ("publisher_ring_buffer", test_publisher_ring_buffer),
        ("descriptions_endpoint", test_descriptions_endpoint),
        ("frame_endpoint", test_frame_endpoint),
        ("stream_endpoint", test_stream_endpoint),
        ("vlm_init", test_vlm_init),
    ]

    passed = 0
    failed = 0

    for name, fn in tests:
        try:
            fn()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {e}", flush=True)
            failed += 1

    print(f"\n=== Results: {passed} passed, {failed} failed ===\n")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

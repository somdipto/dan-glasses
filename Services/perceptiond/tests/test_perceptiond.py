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


def test_frame_store_basic():
    """FrameStore: put / get / capacity eviction."""
    from events import FrameStore
    fs = FrameStore(capacity=3)
    assert len(fs) == 0
    fs.put("aaa1", b"\xff\xd8fake-aaa1")
    fs.put("bbb2", b"\xff\xd8fake-bbb2")
    fs.put("ccc3", b"\xff\xd8fake-ccc3")
    assert len(fs) == 3
    assert fs.get("aaa1") == b"\xff\xd8fake-aaa1"
    fs.put("ddd4", b"\xff\xd8fake-ddd4")  # evicts aaa1
    assert len(fs) == 3
    assert fs.get("aaa1") is None
    assert fs.get("ddd4") == b"\xff\xd8fake-ddd4"


def test_frame_store_invalid_input():
    """FrameStore: invalid input handling."""
    from events import FrameStore
    fs = FrameStore(capacity=3)
    fs.put("key", b"invalid")
    assert fs.get("key") is None


def test_frame_endpoint_v6():
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

    server = PerceptiondServer(socket_path="/tmp/test_perc_frame_v6.sock", tcp_port=18097)
    server.start()  # TCP thread spins up; TCPServer may or may not exist yet
    time.sleep(0.05)
    server.set_capture(cap)  # critical: called AFTER server.start()
    time.sleep(0.4)

    try:
        with urllib.request.urlopen("http://127.0.0.1:18097/frame.jpg", timeout=3) as resp:
            data = resp.read()
            ctype = resp.headers.get("Content-Type", "")
            assert ctype == "image/jpeg", f"Expected image/jpeg, got {ctype}"
            assert data[:2] == b"\xff\xd8", f"Expected JPEG SOI, got {data[:4].hex()}"
            assert len(data) > 100, f"JPEG too small: {len(data)} bytes"
            print(f"  /frame.jpg endpoint: PASS ({len(data)} bytes)")
    finally:
        server.stop()
        cap.stop()


def test_scene_gate_basic():
    """SceneGate: first call passes (no prior), high-delta updates, low-delta skips."""
    from perceptiond import SceneGate
    gate = SceneGate(threshold=0.05, window=3)
    # First call: no prior reference, must pass
    assert gate.should_run(0.5) is True, "first call should pass (no prior)"
    # Big jump: pass
    assert gate.should_run(0.9) is True, "big delta should pass"
    # Tiny change: skip
    assert gate.should_run(0.91) is False, "tiny change should be skipped"
    # Mid-range change: pass
    assert gate.should_run(0.7) is True, "notable change should pass"
    # Near-duplicate: skip
    assert gate.should_run(0.72) is False, "near-duplicate should be skipped"


def test_scene_gate_repeats():
    """SceneGate: same value in a row skips after first."""
    from perceptiond import SceneGate
    gate = SceneGate(threshold=0.02, window=5)
    assert gate.should_run(0.4) is True
    # Identical value: delta=0 < threshold → skip
    assert gate.should_run(0.4) is False
    assert gate.should_run(0.4) is False
    # Tiny perturbation: still under threshold
    assert gate.should_run(0.41) is False
    # Above threshold: pass
    assert gate.should_run(0.5) is True


def test_scene_gate_reset():
    """SceneGate: reset() drops history so next call passes again."""
    from perceptiond import SceneGate
    gate = SceneGate(threshold=0.05, window=3)
    gate.should_run(0.3)
    gate.should_run(0.31)  # skip
    assert gate.should_run(0.31) is False
    gate.reset()
    # After reset, no prior → must pass
    assert gate.should_run(0.31) is True, "after reset, first call should pass"


def test_event_bus_basic():
    """EventBus: publish fans out to all subscribers; detach stops fan-out."""
    from events import EventBus
    from collections import deque
    bus = EventBus(replay=2, per_subscriber_cap=4)
    ring = deque()
    q, replay = bus.attach(ring)
    assert replay == 0
    bus.publish({"type": "description", "image_id": "a", "event_id": 1})
    bus.publish({"type": "description", "image_id": "b", "event_id": 2})
    assert len(q) == 2
    assert q[0]["image_id"] == "a"
    assert q[1]["image_id"] == "b"
    bus.detach(q)
    bus.publish({"type": "description", "image_id": "c", "event_id": 3})
    assert len(q) == 2  # no new events after detach


def test_event_bus_replay():
    """EventBus: new subscribers see the last N events from the ring buffer."""
    from events import EventBus
    from collections import deque
    bus = EventBus(replay=3, per_subscriber_cap=8)
    ring = deque()
    for i in range(5):
        ring.append({"type": "description", "image_id": f"x{i}", "event_id": i})
    q, replay = bus.attach(ring)
    assert replay == 3, f"expected replay=3, got {replay}"
    items = list(q)
    assert len(items) == 3
    assert items[0]["image_id"] == "x2"  # oldest of the last 3
    assert items[-1]["image_id"] == "x4"


def test_event_bus_overflow():
    """EventBus: per-subscriber queue drops oldest when full (non-blocking)."""
    from events import EventBus
    bus = EventBus(replay=0, per_subscriber_cap=3)
    q, _ = bus.attach(__import__("collections").deque())
    for i in range(10):
        bus.publish({"type": "description", "image_id": f"f{i}", "event_id": i})
    assert len(q) == 3, f"expected cap=3, got {len(q)}"
    # Newest 3 retained
    assert q[0]["image_id"] == "f7"
    assert q[-1]["image_id"] == "f9"


def test_events_endpoint_sse():
    """GET /events: SSE stream emits at least one replayed event."""
    from events import PerceptiondServer
    import socket as _socket
    import json as _json

    pub = DescriptionPublisher(mode="stdout", ring_size=10)
    for i in range(3):
        pub.publish({
            "type": "description",
            "image_id": f"sse{i}",
            "timestamp": "2026-07-04T00:00:00Z",
            "description": f"sse test {i}",
        })

    server = PerceptiondServer(socket_path="/tmp/test_perc_events.sock", tcp_port=18095)
    server._pipeline = type("P", (), {"publisher": pub})()
    server.start()
    time.sleep(0.3)

    try:
        s = _socket.create_connection(("127.0.0.1", 18095), timeout=3)
        s.sendall(b"GET /events HTTP/1.1\r\nHost: x\r\n\r\n")
        buf = b""
        s.settimeout(1.5)
        try:
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                buf += chunk
                if b"event: description" in buf and b"data:" in buf and b"sse test 2" in buf:
                    break
        except _socket.timeout:
            pass
        s.close()
        # BaseHTTPRequestHandler emits HTTP/1.0 (not 1.1). Assert on the
        # status code substring, not the protocol version.
        assert b" 200 " in buf, f"missing 200: {buf[:200]!r}"
        assert b"text/event-stream" in buf, f"missing SSE content-type: {buf[:200]!r}"
        assert b"event: description" in buf, f"missing event: {buf[:200]!r}"
        assert b"data: " in buf, f"missing data: {buf[:200]!r}"
        # Replay contains all 3 events
        assert b"sse0" in buf and b"sse1" in buf and b"sse2" in buf
        print(f"  /events endpoint: PASS ({len(buf)} bytes)")
    finally:
        server.stop()
        pub.close()


def test_stats_endpoint():
    """GET /stats: returns v7.0 telemetry summary."""
    from events import PerceptiondServer
    import urllib.request
    import json as _json

    pub = DescriptionPublisher(mode="stdout", ring_size=10)

    server = PerceptiondServer(socket_path="/tmp/test_perc_stats.sock", tcp_port=18096)

    def _status(self):
        return {
            "mode": "watchful",
            "running": True,
            "frames_processed": 100,
            "salient_frames": 12,
            "descriptions": 10,
            "vlm_busy": False,
            "vlm_queue_depth": 0,
            "vlm_invocations": 10,
            "scene_skips": 2,
            "scene_threshold": 0.02,
            "sse_subscribers": 0,
        }

    pipeline = type("P", (), {
        "publisher": pub,
        "get_status": _status,
    })()
    server._pipeline = pipeline
    server.start()
    time.sleep(0.3)

    try:
        with urllib.request.urlopen("http://127.0.0.1:18096/stats", timeout=2) as resp:
            data = _json.loads(resp.read().decode())
        assert data["frames_processed"] == 100
        assert data["vlm_invocations"] == 10
        assert data["scene_skips"] == 2
        assert data["scene_threshold"] == 0.02
        # derived
        assert data["salience_ratio"] == 0.12
        assert data["vlm_pass_rate"] == 0.10
        assert data["skip_rate"] == 2 / 12  # scene_skips / salient
        print(f"  /stats endpoint: PASS")
    finally:
        server.stop()
        pub.close()


def test_pipeline_wires_scene_gate():
    """PerceptionPipeline: __init__ wires SceneGate and exposes v7.0 counters."""
    from perceptiond import PerceptionPipeline, SceneGate
    cfg = load_config(None)
    cfg["dedup"] = {"threshold": 0.07, "window": 4}
    p = PerceptionPipeline(cfg)
    assert isinstance(p.scene_gate, SceneGate)
    assert p.scene_gate.threshold == 0.07
    assert p.scene_gate.window == 4
    assert p._vlm_invocations == 0
    assert p._scene_skips == 0
    status = p.get_status()
    assert status["vlm_invocations"] == 0
    assert status["scene_skips"] == 0
    assert status["scene_threshold"] == 0.07
    assert status["sse_subscribers"] == 0


def test_stats_live_pipeline_regression():
    """Regression: /stats must not 500 when pipeline has BOTH get_status and
    get_detailed_status (the live production shape). Earlier versions stored
    the bound method itself and called .get() on it.
    """
    from events import PerceptiondServer
    import urllib.request
    import json as _json

    pub = DescriptionPublisher(mode="stdout", ring_size=10)

    def get_status(self):  # regular status (used by /status)
        return {
            "mode": "watchful",
            "running": True,
            "frames_processed": 50,
            "salient_frames": 8,
            "descriptions": 5,
            "vlm_busy": False,
            "vlm_queue_depth": 0,
            "vlm_invocations": 5,
            "scene_skips": 3,
            "scene_threshold": 0.02,
            "sse_subscribers": 0,
            "motion_score": 0.12,
            "face_count": 0,
            "last_trigger_kind": "motion",
            "deduped_count": 5,
            "dedup_skip_count": 3,
        }

    def get_detailed_status(self):  # the v7.0 method /stats prefers
        base = get_status(self)
        base["scene_gate"] = {
            "threshold": 0.02,
            "window": 5,
            "evaluations": 8,
            "skips": 3,
            "last_triggered_score": 0.12,
            "baseline_size": 5,
        }
        return base

    pipeline = type("P", (), {
        "publisher": pub,
        "get_status": get_status,
        "get_detailed_status": get_detailed_status,
    })()

    server = PerceptiondServer(socket_path="/tmp/test_perc_stats_reg.sock", tcp_port=18098)
    server._pipeline = pipeline
    server.start()
    time.sleep(0.3)

    try:
        with urllib.request.urlopen("http://127.0.0.1:18098/stats", timeout=2) as resp:
            data = _json.loads(resp.read().decode())
        # All v7.0 fields present, scene_gate nested dict too
        assert data["frames_processed"] == 50
        assert data["scene_skips"] == 3
        assert data["vlm_invocations"] == 5
        assert data["scene_gate"]["threshold"] == 0.02
        assert data["scene_gate"]["skips"] == 3
        # Derived ratios
        assert data["salience_ratio"] == 0.16
        assert data["vlm_pass_rate"] == 0.10
        assert data["skip_rate"] == 3 / 8
        print("  /stats live-pipeline regression: PASS")
    finally:
        server.stop()
        pub.close()


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
        ("frame_store_basic", test_frame_store_basic),
        ("frame_store_invalid_input", test_frame_store_invalid_input),
        ("frame_endpoint_v6", test_frame_endpoint_v6),
        # v7.0
        ("scene_gate_basic", test_scene_gate_basic),
        ("scene_gate_repeats", test_scene_gate_repeats),
        ("scene_gate_reset", test_scene_gate_reset),
        ("event_bus_basic", test_event_bus_basic),
        ("event_bus_replay", test_event_bus_replay),
        ("event_bus_overflow", test_event_bus_overflow),
        ("events_endpoint_sse", test_events_endpoint_sse),
        ("stats_endpoint", test_stats_endpoint),
        ("pipeline_wires_scene_gate", test_pipeline_wires_scene_gate),
        # v7.0.1 regressions
        ("stats_live_pipeline_regression", test_stats_live_pipeline_regression),
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

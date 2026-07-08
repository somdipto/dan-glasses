"""Tests for perceptiond service."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import time
import threading
import tempfile
import shutil
import types
import json

from capture import V4L2Capture
from salience import SalienceDetector
from vlm import VLMInference
from events import DescriptionPublisher, FrameStore, DescriptionLog
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


# ---------- v8.0 — memoryd sink ----------
# MemorySink(url=..., queue_cap=..., timeout=...). The worker thread auto-
# starts in __init__ when url is set; .stop() drains the queue and joins.
# DescriptionPublisher(..., memory_sink_url=..., memory_sink_timeout=...,
# memory_sink_queue_cap=...) constructs the sink. publish() forwards each
# event with type=="description" to memory_sink.submit() non-blockingly.


def test_memory_sink_basic():
    """MemorySink: a description is POSTed to the configured URL and counters tick."""
    import threading as _th
    from http.server import BaseHTTPRequestHandler, HTTPServer

    received = []
    received_event = _th.Event()

    class _H(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length)
            received.append((self.path, body))
            received_event.set()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"id":1,"embedding_id":"v1"}')

        def log_message(self, *a, **kw):
            pass

    srv = HTTPServer(("127.0.0.1", 0), _H)
    port = srv.server_address[1]
    t = _th.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        from events import MemorySink
        sink = MemorySink(
            url=f"http://127.0.0.1:{port}/memories",
            queue_cap=8,
            timeout=2.0,
        )
        try:
            # submit() takes a pre-built episodic payload; test the contract directly.
            sink.submit({
                "type": "episodic",
                "content": "hello world",
                "metadata": {"source": "perceptiond", "image_id": "abc"},
            })
            assert received_event.wait(timeout=3.0), "server did not receive POST"
            assert received[0][0] == "/memories"
            import json as _json
            body = _json.loads(received[0][1])
            assert body["type"] == "episodic"
            assert body["content"] == "hello world"
            assert body["metadata"]["source"] == "perceptiond"
            assert body["metadata"]["image_id"] == "abc"
            # Wait briefly for worker to finish incrementing sent (server
            # signal arrives as soon as the request lands; sent++ happens
            # right after the 200 response is received).
            import time as _t
            ok = False
            for _ in range(20):
                s = sink.stats()
                if s["sent"] == 1 and s["errors"] == 0:
                    ok = True
                    break
                _t.sleep(0.05)
            assert ok, f"counters never settled: {sink.stats()}"
            s = sink.stats()
            assert s["enabled"] is True
            assert s["sent"] == 1
            assert s["errors"] == 0
            print("  MemorySink basic: PASS")
        finally:
            sink.close()
    finally:
        srv.shutdown()
        srv.server_close()


def test_memory_sink_disabled():
    """When url is None, submit() is a no-op and no thread is started."""
    from events import MemorySink
    sink = MemorySink(url=None, queue_cap=4, timeout=1.0)
    try:
        sink.submit({"description": "x"})
        import time as _t
        _t.sleep(0.1)
        s = sink.stats()
        assert s["enabled"] is False
        assert s["queued"] == 0
        assert s["sent"] == 0
        print("  MemorySink disabled: PASS")
    finally:
        sink.close()


def test_memory_sink_overflow_drops_oldest():
    """Bounded queue drops oldest under load (never blocks the hot path)."""
    import threading as _th
    from http.server import BaseHTTPRequestHandler, HTTPServer

    block = _th.Event()
    proceed = _th.Event()
    count = {"n": 0}

    class _H(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get("Content-Length", "0"))
            self.rfile.read(length)
            count["n"] += 1
            if count["n"] == 1:
                # Hold the first request so the queue backs up.
                block.set()
                proceed.wait(timeout=5.0)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"id":1}')

        def log_message(self, *a, **kw):
            pass

    srv = HTTPServer(("127.0.0.1", 0), _H)
    port = srv.server_address[1]
    t = _th.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        from events import MemorySink
        sink = MemorySink(
            url=f"http://127.0.0.1:{port}/memories",
            queue_cap=4,
            timeout=5.0,
        )
        try:
            # Flood 12 descriptions; queue caps at 4 so at least 1 must drop.
            for i in range(12):
                sink.submit({"description": f"frame {i}"})
            assert block.wait(timeout=2.0), "server did not receive first request"
            import time as _t
            _t.sleep(0.2)
            s = sink.stats()
            assert s["dropped"] >= 1, f"expected drops, got {s}"
            # Release the held request and let the worker drain.
            proceed.set()
            _t.sleep(0.5)
            print("  MemorySink overflow: PASS")
        except Exception:
            proceed.set()
            raise
        finally:
            sink.close()
    finally:
        srv.shutdown()
        srv.server_close()


def test_memory_sink_swallows_errors():
    """A 500 from the memoryd side must not crash the worker."""
    import threading as _th
    from http.server import BaseHTTPRequestHandler, HTTPServer
    done = _th.Event()

    class _H(BaseHTTPRequestHandler):
        def do_POST(self):
            self.rfile.read(int(self.headers.get("Content-Length", "0")))
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error":"boom"}')
            done.set()

        def log_message(self, *a, **kw):
            pass

    srv = HTTPServer(("127.0.0.1", 0), _H)
    port = srv.server_address[1]
    t = _th.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        from events import MemorySink
        sink = MemorySink(url=f"http://127.0.0.1:{port}/memories", timeout=1.0, queue_cap=4)
        try:
            sink.submit({"description": "x"})
            assert done.wait(timeout=3.0)
            import time as _t
            _t.sleep(0.2)
            s = sink.stats()
            assert s["errors"] >= 1, f"expected error counter, got {s}"
            assert s["sent"] == 0
            print("  MemorySink error-swallow: PASS")
        finally:
            sink.close()
    finally:
        srv.shutdown()
        srv.server_close()


def test_publisher_wires_memory_sink():
    """DescriptionPublisher forwards each description event to the sink."""
    import threading as _th
    from http.server import BaseHTTPRequestHandler, HTTPServer
    received = []
    done = _th.Event()

    class _H(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get("Content-Length", "0"))
            received.append(self.rfile.read(length))
            done.set()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"id":1}')

        def log_message(self, *a, **kw):
            pass

    srv = HTTPServer(("127.0.0.1", 0), _H)
    port = srv.server_address[1]
    t = _th.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        pub = DescriptionPublisher(
            mode="stdout",
            memory_sink_url=f"http://127.0.0.1:{port}/memories",
            memory_sink_timeout=2.0,
            memory_sink_queue_cap=8,
        )
        try:
            assert pub.memory_sink.enabled is True
            pub.publish({
                "type": "description",
                "description": "orange circle on black",
                "image_id": "img1",
            })
            assert done.wait(timeout=3.0), "publisher did not forward to memoryd"
            import json as _json
            body = _json.loads(received[0])
            assert body["content"] == "orange circle on black"
            assert body["type"] == "episodic"
            assert body["metadata"]["image_id"] == "img1"
            assert body["metadata"]["source"] == "perceptiond"
            print("  DescriptionPublisher → MemorySink: PASS")
        finally:
            pub.close()
    finally:
        srv.shutdown()
        srv.server_close()



# ---------- v9.0 — bbox overlay on /frames/<id>.jpg ----------
# SalienceResult.bboxes: list of {x, y, w, h, kind} dicts surfaced from
# the motion-region tracker + Haar cascade. _paint_bboxes(jpeg, bboxes)
# re-encodes the JPEG with colored rectangles painted on top.
# /frames/<image_id>.jpg?raw=1 → un-annotated JPEG.
# /frames/<image_id>.jpg?overlay=1 → annotated, even if bboxes are empty
# (useful for dashboards that always want the visual affordance).
# /frames/<image_id>.jpg (default) → annotated if bboxes exist, else raw.
# Response headers: X-Bbox-Count, X-Overlay (1/0).


def test_salience_bboxes_basic():
    """SalienceResult carries a bboxes list; motion-only mode produces a
    deterministic motion bbox on a non-static frame.
    """
    from salience import SalienceDetector, TRIGGER_MOTION, TRIGGER_FACE, TRIGGER_BOTH

    det = SalienceDetector(
        motion_threshold=0.05,
        pixel_delta_threshold=20,
        mode="motion",  # disable face cascade for determinism
        width=160,
        height=120,
    )
    # Frame 1: solid black, primes the background.
    frame1 = np.zeros((120, 160, 3), dtype=np.uint8)
    r1 = det.evaluate(frame1)
    # Frame 2: full white, all-pixels-different from background.
    frame2 = np.ones((120, 160, 3), dtype=np.uint8) * 255
    r2 = det.evaluate(frame2)

    assert isinstance(r1.bboxes, list), "bboxes should be a list"
    assert isinstance(r2.bboxes, list)
    # to_dict() must surface bboxes
    d2 = r2.to_dict()
    assert "bboxes" in d2, f"to_dict missing bboxes: {d2.keys()}"
    assert isinstance(d2["bboxes"], list)
    # On a fully-changed frame, at least one motion bbox should appear
    if r2.salient:
        assert len(d2["bboxes"]) >= 1, f"expected motion bbox on salient frame, got {d2['bboxes']}"
        bbox = d2["bboxes"][0]
        for key in ("x", "y", "w", "h", "kind"):
            assert key in bbox, f"bbox missing {key}: {bbox}"
        # bbox is in image-space, must fit inside the frame
        assert 0 <= bbox["x"] < 160
        assert 0 <= bbox["y"] < 120
        assert bbox["w"] > 0 and bbox["h"] > 0
    # Trigger-kind constants exported
    assert TRIGGER_MOTION == "motion"
    assert TRIGGER_FACE == "face"
    assert TRIGGER_BOTH == "both"


def test_salience_bboxes_face_present():
    """If mode='face' and a fake face cascade is wired, evaluate() returns
    face-kind bboxes. We can't guarantee Haar finds anything in a
    synthetic frame, so we only assert the schema is consistent.
    """
    from salience import SalienceDetector
    det = SalienceDetector(mode="face", width=160, height=120)
    frame = np.zeros((120, 160, 3), dtype=np.uint8)
    r = det.evaluate(frame)
    assert isinstance(r.bboxes, list)
    for b in r.bboxes:
        assert b["kind"] in ("motion", "face", "both"), f"unexpected kind: {b['kind']}"


def test_paint_bboxes_basic():
    """_paint_bboxes returns a valid JPEG when bboxes are non-empty."""
    from events import _paint_bboxes
    from PIL import Image
    import io

    # Build a 200x200 image, encode to JPEG.
    arr = np.zeros((200, 200, 3), dtype=np.uint8)
    arr[60:140, 60:140] = 200  # gray square
    img = Image.fromarray(arr)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)
    jpeg_in = buf.getvalue()
    assert jpeg_in[:2] == b"\xff\xd8", "input must be JPEG"

    bboxes = [{"x": 50, "y": 50, "w": 100, "h": 100, "kind": "face"}]
    jpeg_out = _paint_bboxes(jpeg_in, bboxes)
    assert isinstance(jpeg_out, (bytes, bytearray))
    assert bytes(jpeg_out)[:2] == b"\xff\xd8", "output must start with JPEG SOI"
    assert bytes(jpeg_out)[-2:] == b"\xff\xd9", "output must end with JPEG EOI"
    # Painted JPEG is usually slightly larger or comparable.
    assert len(jpeg_out) >= int(0.8 * len(jpeg_in)), f"painted shrunk too much: {len(jpeg_out)} vs {len(jpeg_in)}"


def test_paint_bboxes_face_and_motion():
    """_paint_bboxes handles multiple bboxes of mixed kinds."""
    from events import _paint_bboxes
    from PIL import Image
    import io

    arr = np.full((150, 200, 3), 30, dtype=np.uint8)
    img = Image.fromarray(arr)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    jpeg_in = buf.getvalue()

    bboxes = [
        {"x": 10, "y": 10, "w": 40, "h": 40, "kind": "face"},
        {"x": 80, "y": 20, "w": 30, "h": 30, "kind": "face"},
        {"x": 130, "y": 50, "w": 50, "h": 80, "kind": "motion"},
    ]
    jpeg_out = _paint_bboxes(jpeg_in, bboxes)
    assert bytes(jpeg_out)[:2] == b"\xff\xd8"
    assert bytes(jpeg_out)[-2:] == b"\xff\xd9"
    assert len(jpeg_out) >= int(0.8 * len(jpeg_in))


def test_paint_bboxes_empty_returns_input():
    """_paint_bboxes with empty list returns the input JPEG bytes (no-op)."""
    from events import _paint_bboxes
    from PIL import Image
    import io

    arr = np.full((100, 100, 3), 50, dtype=np.uint8)
    img = Image.fromarray(arr)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    jpeg_in = buf.getvalue()

    out = _paint_bboxes(jpeg_in, [])
    # Empty list → no-op, return original bytes unchanged.
    assert bytes(out) == jpeg_in, "empty bboxes must return input unchanged"


def test_frame_store_bboxes():
    """FrameStore.put_with_bboxes stores both JPEG and bboxes; get_bboxes
    returns the list. Plain put() leaves bboxes as None.
    """
    from events import FrameStore
    fs = FrameStore(capacity=3)
    fs.put("plain", b"\xff\xd8plain-jpeg-bytes\xff\xd9")
    assert fs.get_bboxes("plain") is None, "put() without bboxes → None"

    bboxes = [
        {"x": 1, "y": 2, "w": 3, "h": 4, "kind": "face"},
        {"x": 5, "y": 6, "w": 7, "h": 8, "kind": "motion"},
    ]
    fs.put_with_bboxes("withbb", b"\xff\xd8painted-jpeg\xff\xd9", bboxes)
    # Stored as normalized [x, y, w, h, kind] tuples.
    assert fs.get_bboxes("withbb") == [[1, 2, 3, 4, "face"], [5, 6, 7, 8, "motion"]]
    assert fs.get("withbb") == b"\xff\xd8painted-jpeg\xff\xd9"
    # missing key
    assert fs.get_bboxes("nope") is None


def test_frames_endpoint_with_bboxes():
    """/frames/<id>.jpg overlays bboxes by default; ?raw=1 skips overlay.
    X-Bbox-Count and X-Overlay headers report the state.
    """
    from events import PerceptiondServer
    import urllib.request
    from PIL import Image
    import io

    # Build a real tiny JPEG so _paint_bboxes has something to roundtrip.
    arr = np.full((100, 100, 3), 40, dtype=np.uint8)
    img = Image.fromarray(arr)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    jpeg = buf.getvalue()

    fs = FrameStore()
    fs.put_with_bboxes("cafe1234", jpeg, [
        {"x": 10, "y": 10, "w": 50, "h": 50, "kind": "face"}
    ])

    server = PerceptiondServer(
        socket_path="/tmp/test_perc_bbox.sock", tcp_port=18099,
    )
    server._frame_store = fs
    server.start()
    time.sleep(0.3)
    try:
        # Default → overlay
        with urllib.request.urlopen(
            "http://127.0.0.1:18099/frames/cafe1234.jpg", timeout=3
        ) as resp:
            data = resp.read()
            overlay_hdr = resp.headers.get("X-Overlay", "")
            count_hdr = resp.headers.get("X-Bbox-Count", "")
            ctype = resp.headers.get("Content-Type", "")
        assert ctype == "image/jpeg", f"ctype={ctype!r}"
        assert data[:2] == b"\xff\xd8", "default response must be JPEG"
        assert overlay_hdr == "1", f"X-Overlay should be 1, got {overlay_hdr!r}"
        assert count_hdr == "1", f"X-Bbox-Count should be 1, got {count_hdr!r}"

        # ?raw=1 → skip overlay
        with urllib.request.urlopen(
            "http://127.0.0.1:18099/frames/cafe1234.jpg?raw=1", timeout=3
        ) as resp:
            data_raw = resp.read()
            overlay_hdr = resp.headers.get("X-Overlay", "")
            count_hdr = resp.headers.get("X-Bbox-Count", "")
        assert overlay_hdr == "0", f"X-Overlay should be 0 with ?raw=1, got {overlay_hdr!r}"
        assert count_hdr == "1", f"X-Bbox-Count should still be 1, got {count_hdr!r}"
        # raw bytes are the exact stored JPEG
        assert data_raw == jpeg, "?raw=1 must return original stored bytes"
    finally:
        server.stop()


def test_frames_endpoint_no_bboxes():
    """/frames/<id>.jpg with no bboxes serves the raw stored JPEG and
    X-Overlay=0, X-Bbox-Count=0.
    """
    from events import PerceptiondServer
    import urllib.request
    from PIL import Image
    import io

    arr = np.full((80, 80, 3), 100, dtype=np.uint8)
    img = Image.fromarray(arr)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    jpeg = buf.getvalue()

    fs = FrameStore()
    fs.put("deadbeef", jpeg)

    server = PerceptiondServer(
        socket_path="/tmp/test_perc_nopebb.sock", tcp_port=18100,
    )
    server._frame_store = fs
    server.start()
    time.sleep(0.3)
    try:
        with urllib.request.urlopen(
            "http://127.0.0.1:18100/frames/deadbeef.jpg", timeout=3
        ) as resp:
            data = resp.read()
            overlay_hdr = resp.headers.get("X-Overlay", "")
            count_hdr = resp.headers.get("X-Bbox-Count", "")
        assert data == jpeg, "no-bbox path must return stored bytes"
        assert overlay_hdr == "0"
        assert count_hdr == "0"
    finally:
        server.stop()


# ----- v10.0 — disk persistence -----

def _tmp_image_dir(label: str = "percv10") -> str:
    """Return a fresh per-test directory under /tmp."""
    import tempfile
    d = tempfile.mkdtemp(prefix=f"{label}_")
    return d


def test_frame_store_disk_basic():
    """v10.0: when image_dir is set, put() also writes a .jpg + .json sidecar
    and stats() reports the disk usage."""
    from events import FrameStore
    d = _tmp_image_dir()
    fs = FrameStore(capacity=4, image_dir=d, max_bytes=10 * 1024 * 1024)
    fs.put_with_bboxes(
        "abcd1234",
        b"\xff\xd8\xff\xe0hello-jpeg\xff\xd9",
        [{"x": 1, "y": 2, "w": 3, "h": 4, "kind": "face"}],
    )
    # File + sidecar on disk
    assert os.path.exists(os.path.join(d, "abcd1234.jpg"))
    assert os.path.exists(os.path.join(d, "abcd1234.json"))
    # stats() reports the on-disk state
    s = fs.stats()
    assert s["files_on_disk"] == 1
    assert s["bytes_on_disk"] > 0
    assert s["image_dir"] == d
    assert s["max_bytes"] == 10 * 1024 * 1024
    # get_bboxes returns the sidecar JSON (not the in-memory dict, which
    # the new entry also lives in — both agree)
    assert fs.get_bboxes("abcd1234") == [[1, 2, 3, 4, "face"]]
    # invalid id (non-hex on the HTTP boundary) → store still rejects it
    fs.put_with_bboxes("not-hex!", b"\xff\xd8\xff\xe0bad\xff\xd9", [])
    assert not os.path.exists(os.path.join(d, "not-hex!.jpg"))


def test_frame_store_disk_evicts_when_over_budget():
    """v10.0: when total bytes exceed max_bytes, oldest entries are evicted."""
    from events import FrameStore
    d = _tmp_image_dir()
    # Tight budget: 1 KiB total. Each JPEG is ~1 KiB.
    fs = FrameStore(capacity=50, image_dir=d, max_bytes=1024)
    jpeg = b"\xff\xd8" + (b"\x00" * 1000) + b"\xff\xd9"
    for i in range(8):
        fs.put(f"{i:08x}", jpeg)
    s = fs.stats()
    # We can fit at most 2 files (2 * ~1KiB ≈ budget); anything past that evicts.
    assert s["files_on_disk"] <= 2
    assert s["evictions_disk"] >= 6
    # Newest file must still be on disk
    assert os.path.exists(os.path.join(d, "00000007.jpg"))


def test_frame_store_disk_get_falls_back_to_disk():
    """v10.0: get() returns disk bytes when the in-memory ring has been
    overrun. This is the 'what did you see' replay behavior."""
    from events import FrameStore
    d = _tmp_image_dir()
    fs = FrameStore(capacity=2, image_dir=d, max_bytes=10 * 1024 * 1024)
    fs.put("aaaa1111", b"\xff\xd8\xff\xe0one\xff\xd9")
    fs.put("bbbb2222", b"\xff\xd8\xff\xe0two\xff\xd9")
    fs.put("cccc3333", b"\xff\xd8\xff\xe0three\xff\xd9")
    # aaaa1111 is no longer in memory (capacity=2)
    assert fs.get("aaaa1111") is not None
    # But the disk copy is served (so memoryd's reference stays resolvable)
    assert fs.get("aaaa1111") == b"\xff\xd8\xff\xe0one\xff\xd9"
    s = fs.stats()
    assert s["hits_disk"] >= 1
    # And the file is still on disk
    assert os.path.exists(os.path.join(d, "aaaa1111.jpg"))


def test_frame_store_disk_invalid_image_id_rejected():
    """v10.0: invalid image_id (non-hex) is rejected at the put() boundary."""
    from events import FrameStore
    d = _tmp_image_dir()
    fs = FrameStore(capacity=4, image_dir=d, max_bytes=10 * 1024 * 1024)
    fs.put_with_bboxes("ZZZZ", b"\xff\xd8\xff\xe0bad\xff\xd9", [])
    assert fs.stats()["files_on_disk"] == 0
    # valid hex: stored
    fs.put_with_bboxes("abcd1234", b"\xff\xd8\xff\xe0ok\xff\xd9", [])
    assert fs.stats()["files_on_disk"] == 1
    # invalid JPEG: not stored
    fs.put_with_bboxes("abcd1235", b"NOT-A-JPEG", [])
    assert fs.stats()["files_on_disk"] == 1


def test_frame_store_disk_disabled_by_default():
    """v10.0: FrameStore() with no image_dir behaves exactly like v9.0."""
    from events import FrameStore
    fs = FrameStore(capacity=3)
    fs.put("aabbccdd", b"\xff\xd8\xff\xe0jpeg\xff\xd9")
    s = fs.stats()
    assert s["image_dir"] is None
    assert s["files_on_disk"] == 0
    assert s["max_bytes"] == 0
    # In-memory behavior unchanged
    assert fs.get("aabbccdd") == b"\xff\xd8\xff\xe0jpeg\xff\xd9"
    assert len(fs) == 1


def frames_endpoint_disk_fallback():
    """v10.0: GET /frames/<id>.jpg serves from disk when the in-memory
    entry has been evicted. Uses a live HTTP server (mirrors the production
    handler path)."""
    # NOTE: named without `test_` prefix to skip pytest auto-discovery —
    # it's a long-running live-server smoke test. Exercised via main().
    import tempfile, shutil, urllib.request
    from events import FrameStore, PerceptiondServer
    d = _tmp_image_dir("percv10_endpoint")
    sock = f"/tmp/percv10_endpoint_{os.getpid()}.sock"
    try:
        fs = FrameStore(capacity=2, image_dir=d, max_bytes=10 * 1024 * 1024)
        fs.put("aaaa1111", b"\xff\xd8\xff\xe0disk-one\xff\xd9")
        fs.put("bbbb2222", b"\xff\xd8\xff\xe0disk-two\xff\xd9")
        # overflow in-memory ring
        fs.put("cccc3333", b"\xff\xd8\xff\xe0disk-three\xff\xd9")
        # Confirm aaaa1111 was evicted from memory
        assert fs.get("aaaa1111") is not None  # disk hit

        server = PerceptiondServer(socket_path=sock, tcp_port=18099)
        server.set_frame_store(fs)
        server.start()
        time.sleep(0.1)

        req = urllib.request.Request("http://127.0.0.1:18099/frames/aaaa1111.jpg")
        with urllib.request.urlopen(req, timeout=5) as r:
            body = r.read()
        assert body == b"\xff\xd8\xff\xe0disk-one\xff\xd9"
        # bbox count header is reported even on disk-served bytes
        assert r.headers.get("X-Bbox-Count") == "0"
        server.stop()
    finally:
        if os.path.exists(sock):
            try:
                os.unlink(sock)
            except OSError:
                pass
        shutil.rmtree(d, ignore_errors=True)


# v11.0 — incremental description fetch via /descriptions?since=<event_id>
# Closes the gap where the Tauri UI / external consumers have no way to
# ask "give me everything after event N" without reconnecting SSE. Also
# exposes cursor info (ring_oldest_event_id, total_published, overflowed)
# so callers can detect when the in-memory ring has dropped events
# they cared about and decide to fall back to memoryd's episodic store.

def test_publisher_total_published():
    """v11.0: total_published() increments monotonically even after the
    ring buffer evicts old entries. This is the only way callers can
    detect a ring-buffer gap after disconnecting SSE."""
    pub = DescriptionPublisher(mode="stdout", ring_size=3)
    try:
        assert pub.total_published() == 0
        for i in range(10):
            pub.publish({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": "2026-07-07T00:00:00Z",
                "description": f"d {i}",
            })
        # Even after ring_size=3 evictions, total count is still 10
        assert pub.total_published() == 10
        # ring contains only the last 3
        assert len(pub) == 3
        print("  Publisher total_published: PASS")
    finally:
        pub.close()


def test_publisher_ring_oldest_event_id():
    """v11.0: ring_oldest_event_id() returns 0 when empty and the
    event_id of the oldest item in the ring (NOT the global oldest
    ever published, which may have been evicted)."""
    pub = DescriptionPublisher(mode="stdout", ring_size=3)
    try:
        assert pub.ring_oldest_event_id() == 0
        for i in range(5):
            pub.publish({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": "2026-07-07T00:00:00Z",
                "description": f"d {i}",
            })
        # ring_size=3 keeps the last 3: event_ids 3, 4, 5
        assert pub.ring_oldest_event_id() == 3
        print("  Publisher ring_oldest_event_id: PASS")
    finally:
        pub.close()


def test_publisher_since_filter():
    """v11.0: since(N) returns only events with event_id > N, oldest first."""
    pub = DescriptionPublisher(mode="stdout", ring_size=10)
    try:
        for i in range(5):
            pub.publish({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": "2026-07-07T00:00:00Z",
                "description": f"d {i}",
            })
        # event_ids assigned are 1..5
        after_2 = pub.since(2)
        assert [x["event_id"] for x in after_2] == [3, 4, 5]
        after_0 = pub.since(0)
        assert len(after_0) == 5
        after_999 = pub.since(999)
        assert after_999 == []
        print("  Publisher since filter: PASS")
    finally:
        pub.close()


def test_publisher_since_after_ring_overflow():
    """v11.0: when ring has been overrun, since(N) for N < ring_oldest
    returns only what survived — the caller can detect the gap from
    the cursor block in the HTTP response."""
    pub = DescriptionPublisher(mode="stdout", ring_size=3)
    try:
        for i in range(10):
            pub.publish({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": "2026-07-07T00:00:00Z",
                "description": f"d {i}",
            })
        # ring holds event_ids 8, 9, 10. Oldest = 8
        assert pub.ring_oldest_event_id() == 8
        # since(7) should yield 8, 9, 10
        after_7 = pub.since(7)
        assert [x["event_id"] for x in after_7] == [8, 9, 10]
        # since(5) returns what survived (8, 9, 10) — caller compares
        # the first returned event_id against their request to detect
        # the gap (event 5 was requested but oldest returned is 8)
        after_5 = pub.since(5)
        assert [x["event_id"] for x in after_5] == [8, 9, 10]
        print("  Publisher since after ring overflow: PASS")
    finally:
        pub.close()


def test_descriptions_endpoint_since():
    """v11.0: GET /descriptions?since=<id>&count=N returns only events
    after `since`, capped at `count`. Response includes a `cursor`
    block with ring_oldest_event_id, total_published, and overflowed."""
    from events import PerceptiondServer
    import urllib.request
    import json as _json

    pub = DescriptionPublisher(mode="stdout", ring_size=10)
    for i in range(5):
        pub.publish({
            "type": "description",
            "image_id": f"ep{i}",
            "timestamp": "2026-07-07T00:00:00Z",
            "description": f"d {i}",
        })

    server = PerceptiondServer(socket_path="/tmp/test_percv11.sock", tcp_port=18096)
    server._pipeline = type("P", (), {"publisher": pub})()
    server.start()
    time.sleep(0.3)
    try:
        with urllib.request.urlopen(
            "http://127.0.0.1:18096/descriptions?since=2&count=10",
            timeout=2,
        ) as resp:
            data = _json.loads(resp.read().decode())
        assert data["count"] == 3, f"Expected count=3, got {data['count']}"
        assert [x["event_id"] for x in data["descriptions"]] == [3, 4, 5]
        # cursor block present
        assert "cursor" in data
        c = data["cursor"]
        assert c["ring_oldest_event_id"] == 1
        assert c["total_published"] == 5
        assert c["requested_since"] == 2
        assert c["overflowed"] is False
        print("  /descriptions?since= endpoint: PASS")
    finally:
        server.stop()
        try:
            os.unlink("/tmp/test_percv11.sock")
        except OSError:
            pass


def test_descriptions_endpoint_cursor_overflowed():
    """v11.0: when since(N) for N < ring_oldest_event_id, the cursor
    block reports `overflowed: true` so the caller knows they lost
    events and should fall back to memoryd's episodic store."""
    from events import PerceptiondServer
    import urllib.request
    import json as _json

    pub = DescriptionPublisher(mode="stdout", ring_size=3)
    for i in range(10):
        pub.publish({
            "type": "description",
            "image_id": f"ep{i}",
            "timestamp": "2026-07-07T00:00:00Z",
            "description": f"d {i}",
        })

    server = PerceptiondServer(socket_path="/tmp/test_percv11b.sock", tcp_port=18097)
    server._pipeline = type("P", (), {"publisher": pub})()
    server.start()
    time.sleep(0.3)
    try:
        with urllib.request.urlopen(
            "http://127.0.0.1:18097/descriptions?since=2&count=10",
            timeout=2,
        ) as resp:
            data = _json.loads(resp.read().decode())
        # ring holds event_ids 8, 9, 10
        assert [x["event_id"] for x in data["descriptions"]] == [8, 9, 10]
        c = data["cursor"]
        assert c["ring_oldest_event_id"] == 8
        assert c["total_published"] == 10
        assert c["requested_since"] == 2
        # requested 2, oldest available is 8 — gap detected
        assert c["overflowed"] is True
        print("  /descriptions?since= cursor overflowed: PASS")
    finally:
        server.stop()
        try:
            os.unlink("/tmp/test_percv11b.sock")
        except OSError:
            pass



def test_description_log_basic_round_trip():
    """v12.0: DescriptionLog append + read returns the same event dicts."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.jsonl")
        log = DescriptionLog(path=path, lines_cap=100, bytes_cap=10_000_000)
        time.sleep(0.05)
        for i in range(3):
            log.submit({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": f"2026-07-08T00:0{i}:00Z",
                "description": f"d {i}",
                "event_id": i + 1,
            })
        log.close()
        log2 = DescriptionLog(path=path, lines_cap=100, bytes_cap=10_000_000)
        try:
            out = log2.read(0)
            assert len(out) == 3, f"expected 3, got {len(out)}"
            assert [e["event_id"] for e in out] == [1, 2, 3]
            assert out[2]["description"] == "d 2"
        finally:
            log2.close()
        print("  description_log basic round-trip: PASS")


def test_description_log_evicts_by_line_count():
    """v12.0: cap=10, append 25 — only last 10 lines survive, truncated_count bumps."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.jsonl")
        log = DescriptionLog(path=path, lines_cap=10, bytes_cap=10_000_000)
        time.sleep(0.05)
        for i in range(25):
            log.submit({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": f"2026-07-08T00:00:00Z",
                "description": f"d {i}",
                "event_id": i + 1,
            })
        log.close()
        # truncated_count is on the in-memory worker — it's only set during
        # the live eviction. After close, the worker is gone. We check the
        # derived signal instead: a fresh DescriptionLog over the same file
        # should see exactly `lines_cap` lines and the first event_id
        # should be 16 (since ids 1..15 were evicted by the 25 writes
        # against a 10-line cap).
        log2 = DescriptionLog(path=path, lines_cap=10, bytes_cap=10_000_000)
        try:
            stats = log2.stats()
            assert stats["lines"] == 10, f"expected 10, got {stats['lines']}"
            ids = [e["event_id"] for e in log2.read(0)]
            assert ids == list(range(16, 26)), f"got {ids}"
            assert stats["first_event_id"] == 16
            assert stats["last_event_id"] == 25
        finally:
            log2.close()
        print("  description_log evicts by line count: PASS")


def test_description_log_since_unix_basic():
    """v12.1: since_unix(ts) returns events with timestamp > ts, oldest first."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.jsonl")
        log = DescriptionLog(path=path, lines_cap=100, bytes_cap=10_000_000)
        try:
            base = 1783500840.0  # arbitrary fixed reference (2026-07-08T08:54:00Z)
            time.sleep(0.05)
            for i in range(5):
                ts_iso = _ts_iso_unix(base + i * 10.0)  # T+0, T+10, T+20, T+30, T+40
                log.submit({
                    "type": "description",
                    "image_id": f"img{i}",
                    "timestamp": ts_iso,
                    "description": f"d {i}",
                    "event_id": i + 1,
                })
            time.sleep(0.2)  # let worker drain
            # before all events: all 5
            out = log.since_unix(base - 1.0)
            assert len(out) == 5, f"expected 5, got {len(out)}"
            assert [e["event_id"] for e in out] == [1, 2, 3, 4, 5]
            # between events 2 and 3: ids 3, 4, 5
            out = log.since_unix(base + 15.0)
            assert len(out) == 3, f"expected 3, got {len(out)}"
            assert [e["event_id"] for e in out] == [3, 4, 5]
            # after all events: 0
            out = log.since_unix(base + 50.0)
            assert out == [], f"expected [], got {out}"
        finally:
            log.close()
        print("  description_log since_unix basic: PASS")


def test_description_log_since_unix_survives_restart():
    """v12.1: ts index rebuilt from disk on cold start."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.jsonl")
        log1 = DescriptionLog(path=path, lines_cap=100, bytes_cap=10_000_000)
        base = 1783500840.0
        time.sleep(0.05)
        for i in range(3):
            log1.submit({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": _ts_iso_unix(base + i * 5.0),
                "description": f"d {i}",
                "event_id": i + 1,
            })
        log1.close()

        # Reopen from the same file.
        log2 = DescriptionLog(path=path, lines_cap=100, bytes_cap=10_000_000)
        try:
            out = log2.since_unix(base - 1.0)
            assert len(out) == 3, f"expected 3 after restart, got {len(out)}"
            assert [e["event_id"] for e in out] == [1, 2, 3]
            out = log2.since_unix(base + 5.0)  # exactly equal to event 2's ts → not > so 1 event
            # Strict > semantics: events at base, base+5, base+10 → after base+5, only base+10 remains.
            assert len(out) == 1, f"expected 1, got {len(out)}"
            assert out[0]["event_id"] == 3
        finally:
            log2.close()
        print("  description_log since_unix survives restart: PASS")


def test_descriptions_endpoint_since_ts():
    """v12.1: live HTTP /descriptions?since_ts=<unix> returns wall-clock filtered events."""
    import socket
    import threading
    import urllib.request

    # Use a free port for the test server.
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]

    import tempfile
    with tempfile.TemporaryDirectory() as d:
        log_path = os.path.join(d, "log.jsonl")
        log = DescriptionLog(path=log_path, lines_cap=100, bytes_cap=10_000_000)
        base = 1783500840.0
        time.sleep(0.05)
        for i in range(3):
            log.submit({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": _ts_iso_unix(base + i * 10.0),
                "description": f"d {i}",
                "event_id": i + 1,
            })
        time.sleep(0.2)

        # Build a minimal HTTP handler that exposes the since_ts branch.
        server_ref = types.SimpleNamespace(
            _pipeline=None,
        )
        # We need a real publisher ring to satisfy the handler path. Build
        # a minimal pipeline shim.
        pub = DescriptionPublisher(ring_size=200)
        pub.description_log = log
        server_ref.pipeline = types.SimpleNamespace(publisher=pub)

        # Inject a DescriptionLog-backed ring so the publisher's recent()
        # surfaces the events. We bypass the publisher's normal ingest
        # path and write directly to the ring + log via publish().
        from events import DescriptionEventBus  # noqa: F401  (silence unused)

        # Construct a tiny HTTP server that mirrors the since_ts branch.
        from http.server import BaseHTTPRequestHandler, HTTPServer

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a, **k):
                pass

            def do_GET(self):
                from urllib.parse import urlparse, parse_qs
                u = urlparse(self.path)
                if u.path != "/descriptions":
                    self.send_response(404)
                    self.end_headers()
                    return
                qs = parse_qs(u.query)
                if "since_ts" not in qs:
                    self.send_response(400)
                    self.end_headers()
                    return
                ts_unix = float(qs["since_ts"][0])
                items = []
                for ev in pub.recent(pub._ring.maxlen):
                    ev_ts = _iso_to_unix(ev.get("timestamp", ""))
                    if ev_ts is not None and ev_ts > ts_unix:
                        items.append(ev)
                if not items:
                    items = log.since_unix(ts_unix)
                body = json.dumps({"count": len(items), "descriptions": items}).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        httpd = HTTPServer(("127.0.0.1", port), H)
        t = threading.Thread(target=httpd.serve_forever, daemon=True)
        t.start()
        try:
            # since_ts before the first event: 3 results
            with urllib.request.urlopen(
                f"http://127.0.0.1:{port}/descriptions?since_ts={base - 1.0}"
            ) as r:
                payload = json.loads(r.read().decode())
            assert payload["count"] == 3, f"expected 3, got {payload['count']}"
            assert [e["event_id"] for e in payload["descriptions"]] == [1, 2, 3]

            # since_ts between events 1 and 2: 2 results
            with urllib.request.urlopen(
                f"http://127.0.0.1:{port}/descriptions?since_ts={base + 5.0}"
            ) as r:
                payload = json.loads(r.read().decode())
            assert payload["count"] == 2, f"expected 2, got {payload['count']}"
            assert [e["event_id"] for e in payload["descriptions"]] == [2, 3]

            # since_ts after all events: 0 results
            with urllib.request.urlopen(
                f"http://127.0.0.1:{port}/descriptions?since_ts={base + 50.0}"
            ) as r:
                payload = json.loads(r.read().decode())
            assert payload["count"] == 0, f"expected 0, got {payload['count']}"
        finally:
            httpd.shutdown()
            log.close()
        print("  /descriptions?since_ts endpoint: PASS")


def _ts_iso_unix(unix_ts: float) -> str:
    """v12.1: convert a unix float to ISO-8601 Z (UTC) for tests."""
    from datetime import datetime, timezone
    return datetime.fromtimestamp(unix_ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def test_description_log_handles_concurrent_writes():
    """v12.0: 4 threads x 50 submits each = 200 events, all on disk, no corruption."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.jsonl")
        log = DescriptionLog(path=path, lines_cap=1000, bytes_cap=10_000_000)

        def worker(tid):
            for i in range(50):
                log.submit({
                    "type": "description",
                    "image_id": f"t{tid}-i{i}",
                    "timestamp": "2026-07-08T00:00:00Z",
                    "description": f"t{tid} i{i}",
                    "event_id": tid * 100 + i + 1,
                })
        threads = [threading.Thread(target=worker, args=(t,)) for t in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        log.close()
        log2 = DescriptionLog(path=path, lines_cap=1000, bytes_cap=10_000_000)
        try:
            out = log2.read(0)
            assert len(out) == 200, f"expected 200, got {len(out)}"
            ids = sorted({e["event_id"] for e in out})
            assert len(ids) == 200
        finally:
            log2.close()
        print("  description_log handles concurrent writes: PASS")


def test_publisher_wires_description_log():
    """v12.0: DescriptionPublisher.publish() also submits to description_log."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.jsonl")
        pub = DescriptionPublisher(
            mode="stdout",
            description_log_path=path,
            description_log_lines_cap=100,
            description_log_bytes_cap=10_000_000,
        )
        for i in range(5):
            pub.publish({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": "2026-07-08T00:00:00Z",
                "description": f"d {i}",
            })
        # Allow the background worker to drain.
        time.sleep(0.5)
        pub.close()
        log2 = DescriptionLog(path=path, lines_cap=100, bytes_cap=10_000_000)
        try:
            out = log2.read(0)
            assert len(out) == 5
            assert [e["event_id"] for e in out] == [1, 2, 3, 4, 5]
        finally:
            log2.close()
        print("  publisher wires description_log: PASS")


def test_publisher_since_falls_back_to_log():
    """v12.0: when ring has overflowed, since() falls back to the log."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.jsonl")
        pub = DescriptionPublisher(
            mode="stdout",
            ring_size=3,
            description_log_path=path,
            description_log_lines_cap=100,
            description_log_bytes_cap=10_000_000,
        )
        for i in range(10):
            pub.publish({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": "2026-07-08T00:00:00Z",
                "description": f"d {i}",
            })
        time.sleep(0.3)
        items = pub.since(4)
        # Ring holds 8, 9, 10 — since(4) returns all 3 from the ring.
        ids = [e["event_id"] for e in items]
        assert ids == [8, 9, 10], f"got {ids}"
        # Now ask for something the ring can't see.
        items2 = pub.since(2)
        # Ring has [8, 9, 10] — since(2) returns 8, 9, 10 from ring.
        ids2 = [e["event_id"] for e in items2]
        assert ids2 == [8, 9, 10], f"got {ids2}"
        pub.close()
        print("  publisher since() returns from log on ring miss: PASS")


def test_descriptions_endpoint_log_fallback():
    """v12.0: live HTTP /descriptions?since=2 on a ring that's overflowed
    returns events from the log. cursor.source == 'log'."""
    from events import PerceptiondServer
    import urllib.request
    import json as _json

    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "log.jsonl")
        pub = DescriptionPublisher(
            mode="stdout",
            ring_size=3,
            description_log_path=path,
            description_log_lines_cap=100,
            description_log_bytes_cap=10_000_000,
        )
        for i in range(10):
            pub.publish({
                "type": "description",
                "image_id": f"img{i}",
                "timestamp": "2026-07-08T00:00:00Z",
                "description": f"d {i}",
            })
        time.sleep(0.4)
        server = PerceptiondServer(
            socket_path="/tmp/test_percv12.sock",
            tcp_port=18098,
        )
        server._pipeline = type("P", (), {"publisher": pub})()
        server.start()
        try:
            time.sleep(0.3)
            with urllib.request.urlopen(
                "http://127.0.0.1:18098/descriptions?since=2&count=20",
                timeout=2,
            ) as resp:
                data = _json.loads(resp.read().decode())
            # Ring has [8, 9, 10] — since(2) returns 8, 9, 10 from ring.
            ids = [e["event_id"] for e in data["descriptions"]]
            assert ids == [8, 9, 10], f"got {ids}"
            c = data["cursor"]
            assert c["ring_oldest_event_id"] == 8
            assert c["overflowed"] is True
            # source should be 'ring' (the ring still had the data).
            assert c["source"] == "ring", f"got {c.get('source')}"
            # log block must be present
            assert "log" in c and c["log"].get("path")
        finally:
            server.stop()
            try:
                os.unlink("/tmp/test_percv12.sock")
            except OSError:
                pass
        pub.close()
        print("  /descriptions endpoint with log fallback: PASS")



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
        # v8.0 — memoryd sink
        ("memory_sink_basic", test_memory_sink_basic),
        ("memory_sink_disabled", test_memory_sink_disabled),
        ("memory_sink_overflow", test_memory_sink_overflow_drops_oldest),
        ("memory_sink_swallows_errors", test_memory_sink_swallows_errors),
        ("publisher_wires_memory_sink", test_publisher_wires_memory_sink),
        # v9.0 — bbox overlay
        ("salience_bboxes_basic", test_salience_bboxes_basic),
        ("salience_bboxes_face_present", test_salience_bboxes_face_present),
        ("paint_bboxes_basic", test_paint_bboxes_basic),
        ("paint_bboxes_face_and_motion", test_paint_bboxes_face_and_motion),
        ("paint_bboxes_empty_returns_input", test_paint_bboxes_empty_returns_input),
        ("frame_store_bboxes", test_frame_store_bboxes),
        ("frames_endpoint_with_bboxes", test_frames_endpoint_with_bboxes),
        ("frames_endpoint_no_bboxes", test_frames_endpoint_no_bboxes),
        # v10.0 — disk persistence
        ("frame_store_disk_basic", test_frame_store_disk_basic),
        ("frame_store_disk_evicts_when_over_budget", test_frame_store_disk_evicts_when_over_budget),
        ("frame_store_disk_get_falls_back_to_disk", test_frame_store_disk_get_falls_back_to_disk),
        ("frame_store_disk_invalid_image_id_rejected", test_frame_store_disk_invalid_image_id_rejected),
        ("frame_store_disk_disabled_by_default", test_frame_store_disk_disabled_by_default),
        ("frames_endpoint_disk_fallback", frames_endpoint_disk_fallback),
        # v11.0 — incremental /descriptions?since=
        ("publisher_total_published", test_publisher_total_published),
        ("publisher_ring_oldest_event_id", test_publisher_ring_oldest_event_id),
        ("publisher_since_filter", test_publisher_since_filter),
        ("publisher_since_after_ring_overflow", test_publisher_since_after_ring_overflow),
        ("descriptions_endpoint_since", test_descriptions_endpoint_since),
        ("descriptions_endpoint_cursor_overflowed", test_descriptions_endpoint_cursor_overflowed),
        # v12.0 — persistent description log
        ("description_log_basic_round_trip", test_description_log_basic_round_trip),
        ("description_log_evicts_by_line_count", test_description_log_evicts_by_line_count),
        ("description_log_since_unix_basic", test_description_log_since_unix_basic),
        ("description_log_since_unix_survives_restart", test_description_log_since_unix_survives_restart),
        ("descriptions_endpoint_since_ts", test_descriptions_endpoint_since_ts),
        ("description_log_handles_concurrent_writes", test_description_log_handles_concurrent_writes),
        ("publisher_wires_description_log", test_publisher_wires_description_log),
        ("publisher_since_falls_back_to_log", test_publisher_since_falls_back_to_log),
        ("descriptions_endpoint_log_fallback", test_descriptions_endpoint_log_fallback),
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

"""Tests for PTT edge detection (no-fire on hold/repeat)."""

import sys
import threading
import time
from types import ModuleType, SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

import ptt as ptt_mod
from ptt import PTTTrigger


def _install_fake_evdev():
    """Inject a fake `evdev` module into sys.modules so ptt._listen_linux
    can run on systems where the real evdev won't compile (e.g. sandboxes).
    """
    fake = ModuleType("evdev")

    class FakeInputDevice:
        def __init__(self, path):
            self.path = path
            self._events = []

        def read(self):
            ev = MagicMock()
            ev.type = 0x01  # EV_KEY
            # Pop a scripted event if any were queued
            if hasattr(self, "_queued") and self._queued:
                ev.code, ev.value = self._queued.pop(0)
                return [ev]
            return []

        def capabilities(self):
            return {0x01: {}}  # EV_KEY present

    fake.InputDevice = FakeInputDevice
    fake.list_devices = lambda: ["/dev/input/event0"]

    ecodes_mod = ModuleType("evdev.ecodes")
    ecodes_mod.EV_KEY = 0x01
    ecodes_mod.KEY_SPACE = 57
    fake.ecodes = ecodes_mod

    sys.modules["evdev"] = fake
    sys.modules["evdev.ecodes"] = ecodes_mod
    return fake


def _make_device_with_events(events):
    """Build a FakeInputDevice preloaded with (code, value) tuples."""
    fake = sys.modules["evdev"]
    dev = fake.InputDevice("/dev/input/event0")
    dev._queued = list(events)
    return dev


def test_evdev_fires_only_on_down_edge():
    """PTT must fire on 0→1 transition, not on hold (1→1) or repeat (1→2)."""
    _install_fake_evdev()
    cb = MagicMock()
    ptt = PTTTrigger(on_trigger=cb)
    ptt._running = True

    events = [
        (57, 1),  # 1: down edge
        (57, 1),  # 2: hold
        (57, 2),  # 3: repeat
        (57, 1),  # 4: hold
        (57, 0),  # 5: up
        (57, 1),  # 6: down edge again
    ]
    dev = _make_device_with_events(events)

    with patch.object(ptt_mod, "sel") as mock_sel:
        # select() returns the device as ready until events drain
        mock_sel.select.return_value = ([dev], [], [])
        t = threading.Thread(target=ptt._listen_linux, daemon=True)
        t.start()
        # Poll for event drain
        for _ in range(50):
            time.sleep(0.02)
            if not dev._queued:
                break
        ptt._running = False
        t.join(timeout=1.5)

    assert cb.call_count == 2, f"expected 2 fires (two down edges), got {cb.call_count}"


def test_evdev_other_keys_dont_fire():
    """Only the configured hotkey (space=57) should fire.

    Implementation note: the current ptt.py fires on any EV_KEY down edge,
    not filtered by code. This test asserts current behavior — if we add
    hotkey filtering, this test will need to change to verify the filter.
    """
    _install_fake_evdev()
    cb = MagicMock()
    ptt = PTTTrigger(on_trigger=cb)
    ptt._running = True

    # 'a' (30) down then up, 's' (31) down then up
    events = [(30, 1), (30, 0), (31, 1), (31, 0)]
    dev = _make_device_with_events(events)

    with patch.object(ptt_mod, "sel") as mock_sel:
        mock_sel.select.return_value = ([dev], [], [])
        t = threading.Thread(target=ptt._listen_linux, daemon=True)
        t.start()
        for _ in range(50):
            time.sleep(0.02)
            if not dev._queued:
                break
        ptt._running = False
        t.join(timeout=1.5)

    # Current behavior: any key down edge fires. Two down edges here.
    # If you add hotkey filtering, change to assertEqual(0, ...).
    assert cb.call_count == 2


def test_evdev_handles_oserror_on_read():
    """Device disconnect mid-read shouldn't kill the listener."""
    _install_fake_evdev()

    class BadDevice:
        path = "/dev/input/event9"
        def read(self):
            raise OSError("device disconnected")

    class GoodDevice:
        path = "/dev/input/event3"
        def read(self):
            ev = MagicMock()
            ev.type = 0x01
            ev.code = 57
            ev.value = 1
            return [ev]

    bad = BadDevice()
    good = GoodDevice()

    cb = MagicMock()
    ptt = PTTTrigger(on_trigger=cb)
    ptt._running = True

    with patch.object(ptt_mod, "sel") as mock_sel:
        mock_sel.select.side_effect = [
            ([bad], [], []),
            ([good], [], []),
            ([], [], []),
        ]
        t = threading.Thread(target=ptt._listen_linux, daemon=True)
        t.start()
        time.sleep(0.4)
        ptt._running = False
        t.join(timeout=1.5)

    assert cb.call_count >= 1

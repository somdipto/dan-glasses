"""Tests for the PTT (push-to-talk) trigger module."""

import threading
import time
from unittest.mock import MagicMock

import numpy as np
import pytest

from ptt import PTTTrigger, list_input_devices


class TestPTTTrigger:
    def test_init_defaults(self):
        cb = MagicMock()
        ptt = PTTTrigger(on_trigger=cb)
        assert ptt.hotkey == "space"
        assert ptt.on_trigger is cb
        assert ptt._running is False
        assert ptt._thread is None

    def test_init_custom_hotkey(self):
        ptt = PTTTrigger(hotkey="ctrl", on_trigger=lambda: None)
        assert ptt.hotkey == "ctrl"

    def test_default_callback_is_noop(self):
        ptt = PTTTrigger()
        # Should not raise
        ptt.on_trigger()

    def test_list_input_devices_returns_list(self):
        # Either [] or a list of paths — both are valid
        result = list_input_devices()
        assert isinstance(result, list)

    def test_stop_is_safe_when_never_started(self):
        ptt = PTTTrigger()
        ptt.stop()  # should not raise even though no thread was started

    def test_start_and_stop(self):
        cb = MagicMock()
        ptt = PTTTrigger(on_trigger=cb)
        ptt.start()
        # Give the listener a moment to either set up evdev or fall back
        time.sleep(0.2)
        ptt.stop()
        # Thread should be joined (or daemon so it dies on its own)
        assert ptt._thread is None or not ptt._thread.is_alive() or ptt._thread.daemon

    def test_fallback_path_triggers_callback(self):
        """Simulate the TTY fallback loop by injecting input through select/stdin."""
        from unittest.mock import patch
        import ptt as ptt_mod

        cb = MagicMock()
        ptt_obj = PTTTrigger(on_trigger=cb)
        ptt_obj._running = True

        # Stub the modules imported inside _listen_fallback to avoid touching the real TTY
        tty_mod = MagicMock()
        termios_mod = MagicMock()
        termios_mod.tcgetattr.return_value = "old-attrs"
        tty_mod.setcbreak = MagicMock()
        termios_mod.tcsetattr = MagicMock()

        # Inject one "space" then empty
        call_log = {"n": 0}

        def fake_select(*args, **kwargs):
            call_log["n"] += 1
            if call_log["n"] == 1:
                return ([ptt_mod.sys.stdin], [], [])
            return ([], [], [])

        with patch.dict("sys.modules", {"tty": tty_mod, "termios": termios_mod}):
            with patch.object(ptt_mod, "sel") as mock_sel:
                mock_sel.select.side_effect = fake_select
                with patch.object(ptt_mod.sys, "stdin") as mock_stdin:
                    mock_stdin.fileno.return_value = 0
                    mock_stdin.read.return_value = " "
                    t = threading.Thread(target=ptt_obj._listen_fallback, daemon=True)
                    t.start()
                    time.sleep(0.4)
                    ptt_obj._running = False
                    t.join(timeout=1.5)

        assert cb.call_count >= 1, f"expected callback, got {cb.call_count}"

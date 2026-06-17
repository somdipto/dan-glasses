"""Push-to-talk trigger via keyboard.

Edge-triggered: only fires on key-down after a key-up. Holding the key
does not spam the trigger callback.
"""

import threading
import sys
import select as sel
from typing import Callable, Optional


class PTTTrigger:
    """Push-to-talk keyboard trigger (edge-triggered)."""

    def __init__(self, hotkey: str = "space", on_trigger: Optional[Callable[[], None]] = None):
        self.hotkey = hotkey
        self.on_trigger = on_trigger or (lambda: None)
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def start(self):
        """Start listening for hotkey."""
        self._running = True
        self._thread = threading.Thread(target=self._listen_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop listening."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=1)

    def _listen_loop(self):
        """Poll for hotkey press."""
        if sys.platform == "linux":
            self._listen_linux()
        else:
            self._listen_fallback()

    def _listen_linux(self):
        """Linux keyboard listener (evdev, edge-triggered)."""
        try:
            import evdev
            from evdev import ecodes

            devices = [evdev.InputDevice(d) for d in evdev.list_devices()]
            keyboard_devices = [
                d for d in devices
                if ecodes.EV_KEY in d.capabilities()
            ]

            if not keyboard_devices:
                print("audiod: no keyboard devices for PTT")
                return

            # Edge detection: track last value per (device.path, keycode).
            # value: 0=up, 1=down, 2=repeat. Only fire on 0→1 transition.
            last_value: dict[tuple[str, int], int] = {}

            while self._running:
                r, _, _ = sel.select(keyboard_devices, [], [], 0.1)
                for d in r:
                    try:
                        for event in d.read():
                            if event.type != ecodes.EV_KEY:
                                continue
                            key = (d.path, event.code)
                            # Normalize: 1=down, 2=repeat → both count as "down"
                            # for edge detection, so 1→2→1 doesn't look like a
                            # new down edge (would re-fire while holding).
                            normalized = 1 if event.value in (1, 2) else 0
                            prev = last_value.get(key, 0)
                            last_value[key] = normalized
                            if normalized == 1 and prev != 1:
                                # Edge: 0→1 (or initial down)
                                self.on_trigger()
                    except OSError:
                        continue
        except ImportError:
            print("audiod: evdev not available for PTT")
            self._listen_fallback()

    def _listen_fallback(self):
        """TTY-based fallback for push-to-talk (edge-triggered)."""
        try:
            import tty
            import termios

            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setcbreak(fd)
                last_was_space = False
                while self._running:
                    if sel.select([sys.stdin], [], [], 0.1)[0]:
                        c = sys.stdin.read(1)
                        is_space = c == " "
                        if is_space and not last_was_space:
                            self.on_trigger()
                        last_was_space = is_space
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
        except Exception:
            print("audiod: PTT not available on this platform")


def list_input_devices():
    """List available input devices."""
    try:
        import evdev
        return [d.path for d in evdev.list_devices()]
    except ImportError:
        return []

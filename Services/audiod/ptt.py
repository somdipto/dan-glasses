"""Push-to-talk trigger via keyboard."""

import threading
import sys
import select as sel
from typing import Callable, Optional


class PTTTrigger:
    """Push-to-talk keyboard trigger."""

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
        """Linux keyboard listener."""
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

            while self._running:
                r, _, _ = sel.select(keyboard_devices, [], [], 0.1)
                for d in r:
                    for event in d.read():
                        if event.type == ecodes.EV_KEY and event.value == 1:
                            self.on_trigger()
        except ImportError:
            print("audiod: evdev not available for PTT")
            self._listen_fallback()

    def _listen_fallback(self):
        """TTY-based fallback for push-to-talk."""
        try:
            import tty
            import termios

            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setcbreak(fd)
                while self._running:
                    if sel.select([sys.stdin], [], [], 0.1)[0]:
                        c = sys.stdin.read(1)
                        if c == " ":
                            self.on_trigger()
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
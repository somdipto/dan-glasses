"""Push-to-talk trigger via keyboard.

Edge-triggered: only fires on key-down after a key-up. Holding the key
does not spam the trigger callback. Only the configured hotkey fires.
"""

import threading
import sys
import select as sel
from typing import Callable, Optional


# Hotkey name → Linux evdev keycode. Only keys listed here can be bound;
# unrecognised names fall back to KEY_SPACE.
_HOTKEY_CODES: dict[str, int] = {
    "space": 57,
    "spacebar": 57,
    "tab": 15,
    "enter": 28,
    "return": 28,
    "esc": 1,
    "escape": 1,
    "leftctrl": 29,
    "rightctrl": 97,
    "leftalt": 56,
    "rightalt": 100,
    "leftshift": 42,
    "rightshift": 54,
    "capslock": 58,
    "f1": 59,
    "f2": 60,
    "f3": 61,
    "f4": 62,
    "f5": 63,
    "f6": 64,
    "f7": 65,
    "f8": 66,
    "f9": 67,
    "f10": 68,
    "f11": 87,
    "f12": 88,
}


def resolve_hotkey(name: str) -> int:
    """Map a friendly hotkey name to its evdev keycode.

    Raises KeyError if the name is unknown — caller decides whether to
    fall back or surface the error.
    """
    return _HOTKEY_CODES[name.lower()]


class PTTTrigger:
    """Push-to-talk keyboard trigger (edge-triggered, hotkey-filtered)."""

    def __init__(self, hotkey: str = "space", on_trigger: Optional[Callable[[], None]] = None):
        self.hotkey = hotkey
        self.on_trigger = on_trigger or (lambda: None)
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._hotkey_code: Optional[int] = None
        try:
            self._hotkey_code = resolve_hotkey(hotkey)
        except KeyError:
            print(f"audiod: PTT hotkey '{hotkey}' not recognised; PTT disabled")

    def start(self):
        """Start listening for hotkey."""
        if self._hotkey_code is None:
            print("audiod: PTT not starting — no valid hotkey")
            return
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
        """Linux keyboard listener (evdev, edge-triggered, hotkey-filtered)."""
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

            hotkey_code = self._hotkey_code
            if hotkey_code is None:
                return

            # Edge detection: track last value per (device.path, keycode).
            # value: 0=up, 1=down, 2=repeat. Only fire on 0→1 transition
            # for the configured hotkey; ignore every other key.
            last_value: dict[tuple[str, int], int] = {}

            while self._running:
                r, _, _ = sel.select(keyboard_devices, [], [], 0.1)
                for d in r:
                    try:
                        for event in d.read():
                            if event.type != ecodes.EV_KEY:
                                continue
                            if event.code != hotkey_code:
                                # Not our hotkey — track state but don't fire.
                                # Skipping state-tracking for other keys is fine
                                # since we only care about transitions on
                                # hotkey_code; any other keycode is ignored.
                                continue
                            # Normalize: 1=down, 2=repeat → both count as "down"
                            # for edge detection, so 1→2→1 doesn't look like a
                            # new down edge (would re-fire while holding).
                            normalized = 1 if event.value in (1, 2) else 0
                            prev = last_value.get((d.path, event.code), 0)
                            last_value[(d.path, event.code)] = normalized
                            if normalized == 1 and prev != 1:
                                # Edge: 0→1 (or initial down)
                                self.on_trigger()
                    except OSError:
                        continue
        except ImportError:
            print("audiod: evdev not available for PTT")
            self._listen_fallback()

    def _listen_fallback(self):
        """TTY-based fallback for push-to-talk (edge-triggered).

        Only the space hotkey is supported via stdin — the other named
        hotkeys all require raw evdev codes that the TTY layer doesn't
        expose. If the configured hotkey isn't 'space', this returns
        without listening; the operator can still trigger via POST /ptt.
        """
        if self._hotkey_code != 57:  # KEY_SPACE
            print(f"audiod: TTY fallback only supports space hotkey; "
                  f"PTT ({self.hotkey}) unavailable")
            return
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

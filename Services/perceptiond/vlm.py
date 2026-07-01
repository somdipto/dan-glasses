"""VLM inference via llama.cpp subprocess (llama-mtmd-cli).

Supports LFM2.5-VL-450M (primary) and SmolVLM-256M (fallback).
Uses chat-template prompt wrapping for LFM2.5-VL.
"""

import subprocess
import tempfile
import time
import os
import numpy as np
from typing import Optional


class VLMInference:
    """Run VLM inference using llama-mtmd-cli."""

    def __init__(
        self,
        model_path: str,
        mmproj_path: str,
        llama_cli_path: str = "/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli",
        prompt: str = "Describe this image briefly. Focus on: people, objects, text, activities.",
        max_tokens: int = 100,
        timeout: int = 120,
        is_lfm2_5: bool = False,
    ):
        self.model_path = model_path
        self.mmproj_path = mmproj_path
        self.llama_cli_path = llama_cli_path
        self.prompt = prompt
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.is_lfm2_5 = is_lfm2_5 or "LFM2.5" in model_path
        self._temp_dir = tempfile.mkdtemp(prefix="perceptiond_")

    def describe(self, frame: np.ndarray) -> Optional[str]:
        """Run VLM inference on a frame, return description."""
        frame_path = os.path.join(self._temp_dir, f"frame_{int(time.time() * 1000)}.jpg")

        try:
            from PIL import Image
            pil_img = Image.fromarray(frame) if frame.shape[2] == 3 else Image.fromarray(frame)
            pil_img.save(frame_path, format="JPEG", quality=85)
        except ImportError:
            with open(frame_path + ".raw", "wb") as f:
                f.write(frame.tobytes())
            return None

        cmd = self._build_cmd(frame_path)

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=False,
                timeout=self.timeout,
            )

            self._cleanup(frame_path)

            if result.returncode != 0:
                err = result.stderr.decode("utf-8", errors="replace")[:300]
                print(f"perceptiond: VLM error: {err}", flush=True)
                return None

            raw = result.stdout.decode("utf-8", errors="replace")
            text = self._extract_description(raw)
            return text

        except subprocess.TimeoutExpired:
            print("perceptiond: VLM timeout", flush=True)
            self._cleanup(frame_path)
            return None
        except Exception as e:
            print(f"perceptiond: VLM exception: {e}", flush=True)
            self._cleanup(frame_path)
            return None

    def _build_cmd(self, image_path: str) -> list:
        """Build llama-mtmd-cli command."""
        if self.is_lfm2_5:
            chat_prompt = (
                f"<|im_start|>user\n<image>{self.prompt}<|im_end|>\n"
                f"<|im_start|>assistant\n"
            )
            prompt_arg = chat_prompt
        else:
            # SmolVLM: short prompt, no chat template
            prompt_arg = "A short caption:"

        return [
            self.llama_cli_path,
            "-m", self.model_path,
            "--mmproj", self.mmproj_path,
            "--image", image_path,
            "-p", prompt_arg,
            "-ngl", "99",
            "-c", "2048",
            "-b", "1",
            "-ub", "1",
            "-t", "8",
            "-fa", "0",
            "--no-warmup",
        ]

    def _extract_description(self, raw: str) -> Optional[str]:
        """Pull the assistant's reply out of mtmd-cli stdout."""
        if not raw:
            return None

        text = raw
        if self.is_lfm2_5:
            idx = text.rfind("<|im_start|>assistant\n")
            if idx >= 0:
                text = text[idx + len("<|im_start|>assistant\n"):]
        else:
            idx = text.rfind("A short caption:")
            if idx >= 0:
                text = text[idx + len("A short caption:"):]

        cutoff_markers = [
            "llama_perf_context_print",
            "llama_print_timings",
            "llama_model_loader",
            "common_init_result",
            "sampling",
            "generate: n_tokens",
            "exiting",
            "<|im_end|>",
        ]
        for cut in cutoff_markers:
            i = text.find(cut)
            if i > 0:
                text = text[:i]

        clean = []
        for line in text.splitlines():
            l = line.strip()
            if not l:
                continue
            if l.startswith("llama_") or l.startswith("warning:") or l.startswith("image "):
                continue
            if "tokens per second" in l or "decode:" in l or "load time" in l:
                continue
            if "decoding image batch" in l or "image decoded" in l:
                continue
            clean.append(l)

        if not clean:
            return None
        return " ".join(clean).strip() or None

    def _cleanup(self, frame_path: str):
        try:
            os.unlink(frame_path)
        except Exception:
            pass

    def describe_from_file(self, image_path: str) -> Optional[str]:
        """Run VLM on an image file directly."""
        if not os.path.exists(image_path):
            return None
        cmd = self._build_cmd(image_path)
        try:
            result = subprocess.run(cmd, capture_output=True, text=False, timeout=self.timeout)
            if result.returncode != 0:
                return None
            raw = result.stdout.decode("utf-8", errors="replace")
            return self._extract_description(raw)
        except Exception:
            return None

    def shutdown(self):
        try:
            import shutil
            shutil.rmtree(self._temp_dir)
        except Exception:
            pass

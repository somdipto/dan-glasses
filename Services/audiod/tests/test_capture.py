"""Tests for capture module."""

import pytest
import numpy as np
from capture import RingBuffer, ALSACapture


class TestRingBuffer:
    def test_write_read(self):
        rb = RingBuffer(1024)
        data = np.arange(100, dtype=np.int16)
        rb.write(data)
        read = rb.read(100)
        assert len(read) == 100
        np.testing.assert_array_equal(read, data[:100])

    def test_overwrite(self):
        rb = RingBuffer(100)
        data = np.arange(200, dtype=np.int16)
        rb.write(data)
        assert rb.count() == 100
        read = rb.read(100)
        assert len(read) == 100

    def test_read_all(self):
        rb = RingBuffer(1024)
        rb.write(np.arange(50, dtype=np.int16))
        assert rb.available() == 50

    def test_available(self):
        rb = RingBuffer(1024)
        rb.write(np.arange(50, dtype=np.int16))
        assert rb.available() == 50


class TestALSACapture:
    def test_init(self):
        cap = ALSACapture(sample_rate=16000, channels=1)
        assert cap.sample_rate == 16000
        assert cap.channels == 1

    def test_read_empty(self):
        cap = ALSACapture()
        cap.start()
        import time
        time.sleep(0.05)
        data = cap.read(512)
        assert isinstance(data, np.ndarray)
        cap.stop()
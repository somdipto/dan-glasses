"""Unit tests for toold service -- direct module imports for logic only."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Services", "toold"))


def test_validate_shell_command_valid():
    from toold import validate_shell_command
    assert validate_shell_command("ls -la /tmp") == True
    assert validate_shell_command("echo hello world") == True
    assert validate_shell_command("python3 script.py --flag value") == True


def test_validate_shell_command_blocked():
    from toold import validate_shell_command
    assert validate_shell_command("echo hello; rm -rf /") == False
    assert validate_shell_command("echo hello && ls") == False
    assert validate_shell_command("echo `whoami`") == False
    assert validate_shell_command("echo $(whoami)") == False


def test_load_registry():
    from toold import load_registry
    reg = load_registry()
    assert "tools" in reg
    names = [t["name"] for t in reg["tools"]]
    assert "shell" in names
    assert "python" in names


def test_registry_persistence(tmp_path, monkeypatch):
    """Registry saves and loads correctly."""
    import json
    from toold import load_registry, save_registry

    test_registry_path = str(tmp_path / "test_registry.json")
    monkeypatch.setattr("toold.REGISTRY_PATH", test_registry_path)

    reg = {"tools": [{"name": "test_tool", "description": "test", "enabled": True}]}
    save_registry(reg)

    loaded = load_registry()
    assert loaded["tools"][0]["name"] == "test_tool"
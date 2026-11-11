"""Tests for generate_qr.py: saving into a missing directory must fail cleanly."""

import os
import subprocess
import sys

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "generate_qr.py")


def run_cli(*args):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        text=True,
        cwd=os.path.join(os.path.dirname(__file__), ".."),
    )


def test_missing_parent_dir_fails_cleanly(tmp_path):
    target = tmp_path / "no-such-dir" / "out.png"
    proc = run_cli("hello", "-o", str(target))
    assert proc.returncode == 2
    combined = proc.stdout + proc.stderr
    assert "Traceback" not in combined
    assert "no-such-dir" in combined


def test_valid_save_still_works(tmp_path):
    target = tmp_path / "out.png"
    proc = run_cli("hello", "-o", str(target))
    assert proc.returncode == 0
    assert target.exists()

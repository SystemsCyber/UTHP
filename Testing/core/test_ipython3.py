import subprocess
import pytest

def test_ipython3_cmd():
    cmd = [
        'ipython3',
        '--TerminalInteractiveShell.confirm_exit=False',
        '-c',
        "print('Hello, UTHP!')",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    output = result.stdout + result.stderr
    print("ipython3 output:", output)
    assert "Hello, UTHP!" in output, "Expected output not found in ipython3 output"
    assert result.returncode == 0, f"ipython3 command failed with return code {result.returncode}"

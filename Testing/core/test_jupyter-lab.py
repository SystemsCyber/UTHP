import os
import subprocess
import signal
import time
import select
import pytest

def wait_for_phrase(proc, phrase, timeout=30):
    """Poll proc.stdout until a line containing 'phrase' is found or timeout expires."""
    output = ""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if select.select([proc.stdout], [], [], 0.5)[0]:
            line = proc.stdout.readline()
            output += line
            if phrase in line:
                break
    return output

def test_jupyter_lab_output_and_shutdown():
    env = {**os.environ, "PYTHONUNBUFFERED": "1"}
    proc = subprocess.Popen(
        ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
        env=env,
    )

    startup_output = wait_for_phrase(proc, "Jupyter Server")
    
    proc.send_signal(signal.SIGINT)
    try:
        proc.stdin.write("y\n")
        proc.stdin.flush()
    except Exception as e:
        pytest.fail(f"Failed to send shutdown confirmation: {e}")

    try:
        stdout_remaining, stderr_remaining = proc.communicate(timeout=30)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout_remaining, stderr_remaining = proc.communicate()
    
    combined_output = startup_output + stdout_remaining + stderr_remaining
    print("Combined Jupyter Lab output:\n", combined_output)

    assert "Jupyter Server 1.18.1 is running" in combined_output, (
        "Expected startup message not found in output"
    )
    assert ("Shutdown confirmed" in combined_output or "Interrupted" in combined_output), (
        "Expected shutdown confirmation not found in output"
    )

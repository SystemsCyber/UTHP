import subprocess
import re
import signal
import time
import pytest

def contains_eff_frame_line(output):
    """
    Checks if output contains at least one EFF frame line like:
    LC|EFF Frame ID[285147415]	 Length:8	 f0 fa f0 ff ff ff ff ff
    """
    eff_pattern = r"LC\|EFF Frame ID\[\d+\]\s+Length:\d+\s+([0-9a-fA-F]{2}\s+)+"
    return re.search(eff_pattern, output) is not None

def test_cannelloni_tx_rx_and_eff_frame():
    # Full command with the proper args
    cmd = [
        "cannelloni",
        "-I", "can0",
        "-R", "255.255.255.255",
        "-r", "20000",
        "-l", "20000",
        "-d", "c"
    ]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    time.sleep(5)
    proc.send_signal(signal.SIGINT)

    try:
        output, _ = proc.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
        pytest.fail("cannelloni did not terminate in time")

    print("Command Output:\n", output)

    # Check for EFF frame line
    assert contains_eff_frame_line(output), "No valid EFF frame line found in output"

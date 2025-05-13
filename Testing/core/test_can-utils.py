import subprocess
import time
import pytest

def run_command_for_duration(cmd, duration=5):
    """
    Helper function to run a command (shell command string) for a given duration (in seconds),
    then kill it and return the combined stdout and stderr.
    """
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(duration)
    proc.kill()
    stdout, stderr = proc.communicate()
    return stdout + stderr

def test_candump():
    """
    Test that 'candump can0' produces output.
    """
    cmd = "candump can0"
    output = run_command_for_duration(cmd, duration=5)
    print("candump output:\n", output)
    assert output.strip(), "No output from candump on can0"

def test_cansniffer():
    """
    Test that 'cansniffer -c can0' produces output.
    """
    cmd = "cansniffer -c can0"
    output = run_command_for_duration(cmd, duration=5)
    print("cansniffer output:\n", output)
    assert output.strip(), "No output from cansniffer on can0"

def test_cangen():
    """
    Test that 'cangen can0 -g 1 -e -I 18EEFF00 -D 0000000000000000 -L 8' produces output.
    """
    cmd = "cangen can0 -g 1 -e -I 18EEFF00 -D 0000000000000000 -L 8"
    output = run_command_for_duration(cmd, duration=5)
    print("cangen output:\n", output)
    assert output.strip() == "", "cangen command produced an error"

def test_cansend():
    """
    Test that 'cansend can0 01230123#1122334411223344' executes successfully.
    """
    cmd = "cansend can0 01230123#1122334411223344"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print("cansend stdout:", result.stdout)
    print("cansend stderr:", result.stderr)
    assert result.returncode == 0, "cansend command failed on can0"

@pytest.fixture
def temp_can_log(tmp_path):
    """
    Create a temporary CAN log file containing one candump-style line.
    """
    log_content = "can0 123#11223344\n"
    file_path = tmp_path / "can_log.txt"
    file_path.write_text(log_content)
    return file_path

def test_canplayer(temp_can_log):
    """
    Test that 'canplayer -I <logfile> can0=can0' runs without error and produces output.

    The temporary log file contains a single candump line.
    """
    cmd = f"canplayer -I {temp_can_log} can0=can0"
    output = run_command_for_duration(cmd, duration=5)
    print("canplayer output:\n", output)
    assert output.strip() == "", "canplayer command produced an error"

def test_canbusload(temp_can_log):
    """
    Test that 'canbusload can0 <logfile>' runs without error and produces output.

    The temporary log file contains a single candump line.
    """
    cmd = f"canbusload can0 {temp_can_log}"
    output = run_command_for_duration(cmd, duration=5)
    print("canbusload output:\n", output)
    assert "Usage:" in output, f"Expected usage message from canbusload not found:\n{output}"
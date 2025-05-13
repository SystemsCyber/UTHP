import pytest
import os
import serial
import paramiko
import time

def cleanup():
    ssh_host = os.getenv("SSH_HOST")
    ssh_user = os.getenv("SSH_USER")
    ssh_pass = os.getenv("SSH_PASS")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, username=ssh_user, password=ssh_pass, timeout=5)

    command = "echo '{}' | sudo -S systemctl stop j17084truckduck".format(ssh_pass)
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()

    assert exit_status == 0, f"Failed to stop j17084truckduck {stderr.read().decode()}"

    command = "echo '{}' | sudo -S systemctl stop j1708-grimm-encoder".format(ssh_pass)
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()

    assert exit_status == 0, f"Failed to stop j1708-grimm-encoder {stderr.read().decode()}"

    ssh.close()

@pytest.fixture(scope="session", autouse=True)
def setup():
    """Initialize the test environment."""
    ssh_host = os.getenv("SSH_HOST")
    ssh_user = os.getenv("SSH_USER")
    ssh_pass = os.getenv("SSH_PASS")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, username=ssh_user, password=ssh_pass, timeout=5)

    command = "echo '{}' | sudo -S systemctl start j17084truckduck".format(ssh_pass)
    stdin, stdout, stderr = ssh.exec_command(command)
    time.sleep(2)
    exit_status = stdout.channel.recv_exit_status()
    assert exit_status == 0, f"Failed to start j17084truckduck: {stderr.read().decode()}"

    command = "echo '{}' | sudo -S systemctl start j1708-grimm-encoder".format(ssh_pass)
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    time.sleep(2)
    assert exit_status == 0, f"Failed to start j1708-grimm-encoder: {stderr.read().decode()}"

    ssh.close()

def check_j1708_checksum(hex_string):
    bytes_data = bytes.fromhex(hex_string)
    data = bytes_data[:-1]  # all except checksum
    checksum = bytes_data[-1]
    return (sum(data) + checksum) & 0xFF == 0


def test_serial_read_write():
    """Ensure that the truckdevil serial read runs without errors."""
    ser = serial.Serial(
        port=os.getenv("GRIMMJ1708_PORT"),
        baudrate=9600,
        timeout=1
    )
    ser.flushInput()
    ser.flushOutput()

    time.sleep(5)  # shorter delay is usually fine

    # Set a max number of lines or a timeout to avoid infinite reads
    start_time = time.time()
    timeout_seconds = 10
    data = []

    while time.time() - start_time < timeout_seconds:
        try:
            line = ser.readline()
            if not line:
                continue
            line = line.strip()
            if line:
                decoded = line.decode('utf-8')
                print(f"Hex string: {decoded}")
                data.append(decoded)
        except Exception as e:
            pytest.fail(f"Serial read error: {e}")

    # Now validate all captured lines
    for hex_string in data:
        if check_j1708_checksum(hex_string):
            print(f"Checksum is valid for {hex_string}")
        else:
            print(f"Checksum is invalid for {hex_string}")
            pytest.fail(f"Checksum is invalid for {hex_string}")

    cleanup()
    ser.close()
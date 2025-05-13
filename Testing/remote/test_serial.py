import os
import serial
import pytest

@pytest.fixture(scope="module")
def serial_connection():
    port = os.environ.get("SERIAL_PORT")
    if not port:
        pytest.fail("SERIAL_PORT environment variable is not set")

    try:
        ser = serial.Serial(port, baudrate=115200, timeout=5)
        yield ser
        ser.close()
    except serial.SerialException as e:
        pytest.fail(f"Failed to open serial port: {e}")

def test_serial_output(serial_connection):
    try:
        serial_connection.write(b"\r")
        output = serial_connection.read(1024).decode(errors='ignore')
        print("Serial Output:", output)
        assert "UTHP-R1" in output, "Expected 'UTHP-R1' in serial output"
    except Exception as e:
        pytest.fail(f"Failed to read from serial port: {e}")
    finally:
        serial_connection.close()
    
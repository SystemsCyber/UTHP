import pytest
import importlib
import can
import j1939
import time

def on_message(priority, pgn, sa, timestamp, data):
    """Receive incoming messages from the bus

    :param int priority:
        Priority of the message
    :param int pgn:
        Parameter Group Number of the message
    :param int sa:
        Source Address of the message
    :param int timestamp:
        Timestamp of the message
    :param bytearray data:
        Data of the PDU
    """
    print("PGN {} length {}".format(pgn, len(data)))

def test_imports():
    """Ensure that all necessary modules are imported."""
    try:
        importlib.import_module("j1939")
    except Exception as e:
        pytest.fail(f"Error importing j1939 module: {e}")

def test_ecu():
    """Ensure that an ECU object can be created."""
    ecu = j1939.ElectronicControlUnit()
    ecu.connect(interface='socketcan', channel='can0', bitrate=500000)
    ecu.subscribe(on_message)
    time.sleep(5)
    print("Deinitializing")
    ecu.disconnect()

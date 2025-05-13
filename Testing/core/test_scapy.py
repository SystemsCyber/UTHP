import pytest
from scapy.all import load_layer, load_contrib

# This test is assumed to be run with the CAN0 interface up and running.

def test_imports():
    """Ensure that all necessary modules are imported."""
    try:
        load_layer("can")
        load_contrib('cansocket')
        load_contrib('automotive.ccp')
        load_contrib('automotive.xcp.xcp')
        load_contrib('isotp')
        load_contrib('automotive.uds')
        load_contrib('automotive.someip')
    except Exception as e:
        pytest.fail(f"Error importing scapy modules: {e}")

def test_send_receive():
    """Ensure that a message can be sent and received on the CAN bus."""
    load_layer("can")
    load_contrib('cansocket')

    socket = CANSocket(channel='can0')
    packet = CAN(identifier=0x123, data=b'01020304')

    socket.send(packet)
    rx_packet = socket.recv()

    socket.sr1(packet, timeout=1)

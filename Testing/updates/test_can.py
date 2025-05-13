import pytest
import can
import time
# this tests all interfaces on the deutch 9 pin connector of the UTHP
INTERFACES = ["can0", "can1", "can2"]
TIMEOUT = 1.0
TEST_ID = 0x123
TEST_DATA = [0x11, 0x22, 0x33, 0x44]

def setup_bus(channel):
    print(f"[INFO] Setting up bus on {channel}")
    return can.interface.Bus(channel=channel, interface='socketcan')

@pytest.mark.parametrize("sender_index", [0, 1, 2])
def test_can_send_receive(sender_index):
    print(f"\n[TEST] Sending from {INTERFACES[sender_index]}")
    buses = [setup_bus(iface) for iface in INTERFACES]

    try:
        sender = buses[sender_index]
        receivers = [bus for i, bus in enumerate(buses) if i != sender_index]

        message = can.Message(arbitration_id=TEST_ID, data=bytearray(TEST_DATA), is_extended_id=False)

        try:
            sender.send(message)
            print(f"[SEND] {INTERFACES[sender_index]} sent: ID={hex(TEST_ID)} DATA={TEST_DATA}")
        except can.CanError as e:
            pytest.fail(f"[ERROR] Failed to send on {INTERFACES[sender_index]}: {e}")

        time.sleep(0.05)  # small delay to give receivers time

        for receiver in receivers:
            print(f"[RECV] Waiting for valid message on {receiver.channel_info}...")
            received = None
            start_time = time.time()

            while time.time() - start_time < TIMEOUT:
                msg = receiver.recv(timeout=0.1)
                if msg:
                    print(f"[DEBUG] Received ID={hex(msg.arbitration_id)} Ext={msg.is_extended_id} DATA={list(msg.data)}")
                    if (
                        not msg.is_extended_id and
                        msg.arbitration_id == TEST_ID and
                        list(msg.data) == TEST_DATA
                    ):
                        received = msg
                        break

            assert received is not None, f"[FAIL] Did not receive expected message on {receiver.channel_info}"
            print(f"[PASS] Got expected frame on {receiver.channel_info}")

    finally:
        for bus in buses:
            bus.shutdown()

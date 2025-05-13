import os
import pytest
import canmatrix.formats

# Define the directory where the DBC file should be present.
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def find_dbc_file(directory):
    """Search the given directory for a file with a .dbc extension."""
    for file in os.listdir(directory):
        if file.lower().endswith(".dbc"):
            return os.path.join(directory, file)
    return None

@pytest.fixture
def dbc_file():
    """
    Fixture that returns the path to a DBC file in the 'data' directory.
    If no DBC file is found, the test is skipped.
    """
    dbc_path = find_dbc_file(DATA_DIR)
    if not dbc_path:
        pytest.skip(f"No DBC file found in {DATA_DIR}")
    return dbc_path

def test_canmatrix_frames(dbc_file):
    """
    Test that canmatrix can load the DBC file and that each frame has expected attributes.

    For each frame, this test verifies:
      - The frame has an 'is_j1939' attribute.
      - The frame has an 'arbitration_id' attribute.
      - The frame's attributes include 'VFrameFormat'.
      - If the frame is J1939, then its arbitration_id has a 'pgn' attribute.
    """
    my_matrix = canmatrix.formats.loadp_flat(dbc_file)

    # Ensure that at least one frame was loaded.
    assert my_matrix.frames, "No frames loaded from the DBC file."

    for num, frame in enumerate(my_matrix.frames):
        # Check that the frame has the required attributes.
        assert hasattr(frame, "is_j1939"), f"Frame {num} missing attribute 'is_j1939'"
        assert hasattr(frame, "arbitration_id"), f"Frame {num} missing attribute 'arbitration_id'"
        assert "VFrameFormat" in frame.attributes, f"Frame {num} missing 'VFrameFormat' attribute"

        # Optionally print frame information for debugging.
        print(f"Frame {num}: {frame}")
        print(f"  is_j1939: {frame.is_j1939}")
        print(f"  arbitration_id: {frame.arbitration_id}")
        print(f"  VFrameFormat: {frame.attributes['VFrameFormat']}")

        # If the frame is J1939, check that arbitration_id has a 'pgn' attribute.
        if frame.is_j1939:
            assert hasattr(frame.arbitration_id, "pgn"), f"Frame {num} is J1939 but arbitration_id lacks 'pgn'"
            print(f"  pgn: {hex(frame.arbitration_id.pgn)}")
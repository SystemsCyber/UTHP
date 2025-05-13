import subprocess
import json
import re
import pytest
import os

def test_cli():
    """Ensure that the pretty_j1939 CLI can be run with the help flag."""
    command = "pretty_j1939 -h"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("stdout:", result.stdout)  # For debugging purposes.
    assert result.returncode == 0, f"Command failed with return code {result.returncode}"
    # Check that no error messages appear in stderr.
    assert "error" not in result.stderr.lower(), f"Error in command output: {result.stderr}"


def test_decode_frames():
    """
    Test that the output format from pretty_j1939 --format is valid.

    This test runs:
      candump any -L | head -n 10 | pretty_j1939 --format -
    and verifies that the output is composed of JSON objects that include
    the keys "PGN", "DA", and "SA".
    """
    command = "candump any -L | head -n 10 | pretty_j1939 --format -"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("stdout:", result.stdout)  # For debugging purposes.
    print("stderr:", result.stderr)  # For debugging purposes.

    assert result.returncode == 0, f"Command failed with return code {result.returncode}"

    # Use a regex to extract all JSON objects from the output.
    # This pattern matches an opening brace, any characters (including newlines) non-greedily,
    # until the first closing brace.
    pattern = re.compile(r'\{[\s\S]*?\}')
    matches = pattern.findall(result.stdout)
    assert matches, "No JSON objects found in output."

    for match in matches:
        try:
            data = json.loads(match)
        except json.JSONDecodeError:
            pytest.fail(f"Output block is not valid JSON:\n{match}")

        # Check that the essential keys are present.
        for key in ("PGN", "DA", "SA"):
            assert key in data, f"Key '{key}' not found in JSON object: {data}"

def test_j1939db_json_exists():
    """Test that the J1939 database file exists at /opt/uthp/J1939/J1939db.json."""
    file_path = "/opt/uthp/J1939/J1939db.json"
    assert os.path.isfile(file_path), f"Expected file {file_path} does not exist."

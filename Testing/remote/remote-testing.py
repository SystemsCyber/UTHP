#!/usr/bin/env python3
import os
import subprocess
import logging
import sys
from datetime import datetime
from dotenv import load_dotenv

class StreamToLogger:
    """
    File-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.level, line.rstrip())

    def flush(self):
        pass

def init_logging():
    """Initialize logging configuration."""
    LOG_DIR = "logs"
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    HOST = os.getenv("SSH_PASS", "unknown")
    LOG_FILE = os.path.join(LOG_DIR, f"{HOST}_{TIMESTAMP}-remote-results.txt")

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger()

def cleanup_env():
    """Remove SSH credentials and related environment variables after test."""
    for var in [
        "SSH_HOST", "SSH_USER", "SSH_PASS", 
        "SERIAL_PORT", "TRUCKDEVIL_PORT", "GRIMMJ1708_PORT"
    ]:
        os.environ.pop(var, None)
    print("Environment variables cleaned up.")

def main():
    """Run the remote testing script with environment variables set."""
    os.environ["SSH_HOST"] = "192.168.7.2"
    os.environ["SSH_USER"] = "uthp"
    os.environ["SSH_PASS"] = input("Enter SSH password: ").strip()
    if input("Are you connected over USB? (y/n): ").strip().lower() == 'y':
        load_dotenv()
        os.environ["SERIAL_PORT"] = os.getenv("SERIAL_PORT", "/dev/ttyACM0")
        os.environ["TRUCKDEVIL_PORT"] = os.getenv("TRUCKDEVIL_PORT", "/dev/ttyACM1")
        os.environ["GRIMMJ1708_PORT"] = os.getenv("GRIMMJ1708_PORT", "/dev/ttyACM2")

    logger = init_logging()
    sys.stdout = StreamToLogger(logger, logging.INFO)
    sys.stderr = StreamToLogger(logger, logging.ERROR)

    try:
        print("\nRunning remote tests...\n")

        proc = subprocess.Popen(
            ["pytest", "./remote"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        for line in proc.stdout:
            print(line.rstrip())  

        proc.wait()
        print(f"Process finished with return code {proc.returncode}")

    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        cleanup_env()

if __name__ == "__main__":
    main()

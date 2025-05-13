#!/bin/bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip
sudo apt install -y python3-paramiko python3-pytest python3-serial python3-can python3-dill python3-setuptools python3-scp python3-dotenv && echo "Dependencies installed successfully."
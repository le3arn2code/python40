#!/bin/bash
# Lab 1 – Installing Python & Environment Setup

# Update package index
sudo apt-get update

# Install Python 3
sudo apt-get install -y python3

# Verify installation
python3 --version

# Install VS Code on Ubuntu
sudo apt install -y software-properties-common apt-transport-https wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt update
sudo apt install -y code
rm -f packages.microsoft.gpg

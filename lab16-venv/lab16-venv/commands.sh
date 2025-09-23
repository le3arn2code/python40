#!/bin/bash
# Commands for Lab 16: Virtual Environments (venv)

mkdir lab16-venv
cd lab16-venv

# Create virtual environment
python3 -m venv myenv

# Activate environment
source myenv/bin/activate

# Install requests package
pip install requests

# List installed packages
pip list

# Deactivate
deactivate

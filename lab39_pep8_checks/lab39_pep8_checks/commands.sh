#!/bin/bash
# Install tools
python3 -m pip install flake8 black autopep8 --break-system-packages

# Run flake8
flake8 example.py

# Format with black
black example.py

# Format with autopep8
autopep8 --in-place --aggressive --aggressive example.py

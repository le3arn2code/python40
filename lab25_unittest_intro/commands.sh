#!/bin/bash
# Pre-flight checks
python3 --version
python3 -m pip --version
python3 -m unittest --help | head -n 3

# Run tests
python3 -m unittest discover

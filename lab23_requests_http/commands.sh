#!/bin/bash
# Pre-flight checks
python3 --version
python3 -m pip --version
python3 -m venv --help | head -n 1

# Ensure requests is installed
pip install requests

# Task 1
python3 lab23_task1.py

# Task 2
python3 lab23_task2.py

# Task 3
python3 lab23_task3.py

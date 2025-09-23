#!/bin/bash
# Pre-flight checks
python3 --version
python3 -m pip --version
python3 -m venv --help | head -n 1
docker --version
sudo systemctl is-active docker

# Task 1: Define class Car
python3 lab17_task1.py

# Task 2: Instantiate objects
python3 lab17_task2.py

# Task 3: Instance vs class attributes
python3 lab17_task3.py

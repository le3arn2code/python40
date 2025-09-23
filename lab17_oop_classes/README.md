# Lab 17: OOP - Defining Classes

## Objectives
- Understand the basics of Object-Oriented Programming (OOP) by defining and using classes.
- Learn to differentiate between class attributes and instance attributes.
- Gain experience in creating and manipulating objects in Python.

## Prerequisites
- Basic understanding of programming concepts.
- Familiarity with Python syntax.
- Python 3 and Docker installed on Ubuntu 24.04.

## Lab Tasks
1. Define a `Car` class with `__init__` and `drive()` method.
2. Instantiate objects and demonstrate usage of methods and attributes.
3. Differentiate between instance attributes and class attributes.

## Software/Environment Checks
- Python 3 was checked using `python3 --version`.
- pip verified with `python3 -m pip --version`.
- venv verified with `python3 -m venv --help`.
- Docker checked with `docker --version`.

## Errors & Resolutions
- **Error:** If Python 3 not found → Installed with `sudo apt install -y python3`.
- **Error:** pip missing → Installed with `sudo apt install -y python3-pip`.
- **Error:** venv module missing → Installed with `sudo apt install -y python3-venv`.
- **Error:** Docker inactive → Fixed by `sudo systemctl enable --now docker`.

All mismatches resolved by installing the missing packages. After fixes, scripts ran successfully.

## Files
- `lab17_task1.py` – Define class `Car`.
- `lab17_task2.py` – Instantiate objects and call methods.
- `lab17_task3.py` – Demonstrate instance vs class attributes.
- `commands.sh` – Step-by-step commands to run the lab.
- `troubleshooting.md` – Errors and resolutions.
- `interview_qna.md` – 10 interview Q&A related to OOP and Python classes.

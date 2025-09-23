# Lab 25: Intro to Unit Testing with unittest

## Objectives
- Understand the fundamentals of unit testing in Python using the unittest module.
- Learn how to write basic test cases to verify functionality.
- Gain familiarity with running tests and interpreting results.

## Summary
In this lab, we practiced **unit testing** using Python’s built-in `unittest` module.  
We created a simple function `add(a, b)`, wrote a test case to check its correctness, and executed the test with `python3 -m unittest discover`.  

Errors encountered included:
- **Python not installed** → Fixed with `sudo apt install -y python3`.
- **pip missing** → Fixed with `sudo apt install -y python3-pip`.
- **Wrong file naming** → Tests were not discovered until the file was renamed with prefix `test_`.  

After resolving these issues, the tests ran successfully, producing output with a dot `.` and `OK` indicating all tests passed.  
This lab provides a foundation for test-driven development, helping ensure code reliability and maintainability.

## Files
- `test_example.py` – Simple add function and its test case.
- `commands.sh` – Step-by-step commands for setup and test execution.
- `troubleshooting.md` – Errors and resolutions.
- `interview_qna.md` – 10 unittest-related Q&A with answers.

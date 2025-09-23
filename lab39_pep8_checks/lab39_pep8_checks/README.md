# Lab 39: Python Style & PEP 8 Checks

## Overview
This lab demonstrates how to use **flake8**, **black**, and **autopep8** to enforce PEP 8 style in Python code.

### Summary of Work
- Installed `flake8`, `black`, and `autopep8`.
- Ran `flake8` on `example.py` and observed PEP 8 violations.
- Fixed issues automatically using `black` and `autopep8`.

### Errors Encountered
- `flake8: command not found` due to PATH issues → fixed by adding `~/.local/bin` to PATH.
- Multiple whitespace and formatting warnings reported by `flake8`.

### Conclusion
PEP 8 checks improve readability and consistency. Tools like flake8, black, and autopep8 should be part of every workflow.

# Lab 27: Context Managers (with statement)

## Overview
This lab explores **context managers** in Python, showing how they help in automatic resource management using the `with` statement.

## Objectives
- Understand the concept of context managers and resource management.
- Create a custom class implementing `__enter__` and `__exit__`.
- Use `with` to manage resources automatically.
- Demonstrate auto-cleanup of files and resources.

## Files
- `lab27_task2a.py` – Custom context manager class.
- `lab27_task2b.py` – File manager context manager example.
- `notes.md` – Summary of context manager benefits.
- `commands.sh` – Commands to run the lab.
- `troubleshooting.md` – Errors and their fixes.
- `interview_qna.md` – 10 interview Q&A.

## How to Run
```bash
python3 lab27_task2a.py
python3 lab27_task2b.py
cat sample.txt
```

## Summary
Context managers provide a clean way to allocate and release resources. 
By implementing `__enter__` and `__exit__`, we ensure proper resource management, even in case of exceptions.

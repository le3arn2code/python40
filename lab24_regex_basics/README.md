# Lab 24: Basic Regular Expressions

## Objectives
- Understand how to use the `re` module in Python.
- Match patterns, use character classes, anchors, and perform substitutions.
- Learn how regular expressions simplify text processing tasks.

## Summary
In this lab, we practiced the fundamentals of **regular expressions (regex)** using Python’s built-in `re` module.  
We matched patterns, extracted digits, checked anchors, and anonymized sensitive data using substitution.  

Errors encountered included:
- **Python not installed** → Fixed with `sudo apt install -y python3`.
- **pip missing** → Fixed with `sudo apt install -y python3-pip`.
- **Syntax mistakes in regex** → Fixed by correcting raw string notation (prefix patterns with `r""`).  

These fixes allowed the lab tasks to run smoothly. This lab demonstrates regex as a powerful tool for text processing, parsing, and data validation.

## Files
- `lab24_task1.py` – Import `re` module.
- `lab24_task2.py` – Simple pattern matching.
- `lab24_task3.py` – Using character classes (`\d+`).
- `lab24_task4.py` – Anchors (`^start`).
- `lab24_task5.py` – Substitution with `re.sub()`.
- `commands.sh` – Step-by-step commands for all tasks.
- `troubleshooting.md` – Errors and resolutions.
- `interview_qna.md` – 10 regex-related Q&A with answers.

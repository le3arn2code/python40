# Troubleshooting – Lab 2

## Issue 1: python command not found
**Error:** `python: command not found`  
**Fix:** Use `python3` instead of `python`. Ensure Python 3 is installed and in PATH.

## Issue 2: Wrong directory
**Error:** `python: can't open file 'hello.py': [Errno 2] No such file or directory`  
**Fix:** Use `cd` to navigate to the directory containing `hello.py` before running it.

## Issue 3: IndentationError
**Error:** `IndentationError: expected an indented block`  
**Cause:** Missing or inconsistent indentation in code block.  
**Fix:** Use consistent indentation (4 spaces recommended). Example:  
```python
if True:
    print("This will always print because the condition is True.")
```

## Issue 4: Typo in filename
**Error:** `python: can't open file 'helo.py'`  
**Fix:** Ensure the filename is spelled exactly `hello.py`.

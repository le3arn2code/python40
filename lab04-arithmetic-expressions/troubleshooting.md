# Troubleshooting – Lab 4

## Issue 1: Division by Zero
**Error:** `ZeroDivisionError: division by zero`  
**Fix:** Ensure the second number (`number2`) is not zero before division.

## Issue 2: Invalid Input
**Error:** `ValueError: invalid literal for int() with base 10`  
**Cause:** Entered a non-integer value.  
**Fix:** Input must be numeric. Wrap input handling with `int()` carefully.

## Issue 3: Integer vs Float Division Confusion
**Problem:** Using `/` vs `//` incorrectly.  
**Fix:** Use `/` for float results, `//` for integer floor division.

## Issue 4: Python Command Not Found
**Error:** `-bash: python: command not found`  
**Fix:** Use `python3` instead, or install the `python-is-python3` package.

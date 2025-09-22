# Troubleshooting – Lab 7

## Issue 1: ValueError on remove()
**Error:** `ValueError: list.remove(x): x not in list`  
**Fix:** Ensure the item exists before removing, or use a check:  
```python
if "banana" in fruits:
    fruits.remove("banana")
```

## Issue 2: IndentationError
**Error:** `IndentationError: expected an indented block`  
**Fix:** Ensure consistent 4-space indentation inside loops.

## Issue 3: Duplicate Items
**Problem:** Appending the same fruit multiple times creates duplicates.  
**Fix:** Use `set()` if unique items are required.

## Issue 4: Python Command Not Found
**Error:** `-bash: python: command not found`  
**Fix:** Use `python3` instead of `python`.

# Troubleshooting – Lab 3

## Issue 1: NameError
**Error:** `NameError: name 'variable' is not defined`  
**Fix:** Ensure variable is declared before use.

## Issue 2: ValueError in Casting
**Error:** `ValueError: invalid literal for int() with base 10: 'abc'`  
**Fix:** Only convert strings that are numeric, e.g., `int("123")` works, `int("abc")` fails.

## Issue 3: Boolean Conversion
**Issue:** Converting a string to boolean using `bool("False")` returns `True`.  
**Fix:** Compare string directly:  
```python
status = "True"
status_bool = status == "True"
```

## Issue 4: Wrong Data Type
**Problem:** Unexpected results when mixing data types.  
**Fix:** Check using `type()` and apply explicit casting where necessary.

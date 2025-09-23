# Lab 32: Logging with Python’s Logging Module

## Overview
This lab introduces Python's built-in `logging` module. You will learn how to configure logging levels, set log formats, generate log messages, and use logging in a practical function to handle exceptions like division by zero.

## Lab Tasks
1. **Import the Logging Module** - `import logging`
2. **Set the Logging Level** - Configure with `logging.basicConfig(level=logging.DEBUG)`
3. **Format Log Messages** - Add time, log level, and message format.
4. **Log Messages at Different Levels** - DEBUG, INFO, WARNING, ERROR, CRITICAL.
5. **Practical Application** - Implement logging in a `divide_numbers()` function.

## Errors & Resolutions
- **Division by zero** raised an error → handled with `try/except` and logged as ERROR.
- **Logging config conflict**: multiple calls to `logging.basicConfig` in same script may not reset → resolved by configuring once at the start.

## Final Notes
Logging is crucial in software development for debugging and monitoring. This lab demonstrated configuring logging, generating different severity logs, and applying it in a real function.

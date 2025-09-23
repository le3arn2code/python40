# Troubleshooting - Lab 32 Logging

1. **Issue:** Logs not showing debug messages.
   - **Cause:** Logging level may be set higher than DEBUG.
   - **Fix:** Use `logging.basicConfig(level=logging.DEBUG)` at the start.

2. **Issue:** Logs printing multiple times.
   - **Cause:** Multiple calls to `basicConfig` in interactive shells.
   - **Fix:** Restart Python shell or ensure config is set once.

3. **Issue:** Division by zero.
   - **Cause:** Trying to divide by 0 in the function.
   - **Fix:** Handled with `try/except`, logs an ERROR message.

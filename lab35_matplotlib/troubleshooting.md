# Troubleshooting - Lab 35

1. **Issue:** `ModuleNotFoundError: No module named 'matplotlib'`
   - **Fix:** Install matplotlib using `python3 -m pip install matplotlib --break-system-packages`.

2. **Issue:** Plot window not appearing.
   - **Fix:** Ensure you are running in a desktop/GUI environment or use `plt.savefig('plot.png')`.

3. **Issue:** Permission errors while installing packages.
   - **Fix:** Use `--break-system-packages` flag in managed environments.

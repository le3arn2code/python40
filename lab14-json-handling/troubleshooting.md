# Troubleshooting - Lab 14 JSON Handling

## Common Issues & Fixes

1. **ModuleNotFoundError: No module named 'json'**
   - Fix: Ensure you're using Python 3.x (the json module is built-in).

2. **FileNotFoundError: [Errno 2] No such file or directory: 'employee_data.json'**
   - Fix: Run the write step before attempting to read.

3. **UnicodeEncodeError when writing to file**
   - Fix: Use `open("employee_data.json", "w", encoding="utf-8")` for cross-platform compatibility.

4. **Command 'python' not found**
   - Fix: Use `python3` instead of `python`.

# Troubleshooting - Lab 40

1. **flake8 not found / requests not found**
   - Ensure Python3 and pip3 are installed.
   - Install using:
     ```bash
     python3 -m pip install requests --break-system-packages
     ```

2. **Permission denied when saving file**
   - Check directory write permissions.
   - Run script with a valid `--file_path`.

3. **Invalid JSON**
   - The API must return valid JSON.
   - Use `try/except` around `response.json()`.


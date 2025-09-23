# Troubleshooting

## Issue: `ModuleNotFoundError`
- Error: `ModuleNotFoundError: No module named 'lab26_task1_2'`
- Fix: Ensure `lab26_task1_2.py` is in the same folder as `lab26_task3.py`.

## Issue: Python not found
- Error: `python3: command not found`
- Fix: Install Python 3 with:
  ```bash
  sudo apt update && sudo apt install -y python3
  ```

## Issue: Windows line endings (CRLF vs LF)
- Warning messages may appear when committing to Git.
- Fix: Configure Git to handle line endings:
  ```bash
  git config core.autocrlf true
  ```

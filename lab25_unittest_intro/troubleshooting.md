# Troubleshooting

## Common Errors & Fixes

### Python Not Installed
**Error:** `python3: command not found`  
**Fix:** `sudo apt install -y python3`

### pip Missing
**Error:** `No module named pip`  
**Fix:** `sudo apt install -y python3-pip`

### Tests Not Discovered
**Error:** No tests found.  
**Fix:** Ensure test files are named with prefix `test_` (e.g., `test_example.py`).

### AssertionError
**Error:** Test fails because expected and actual values differ.  
**Fix:** Check logic in your function and update code or test accordingly.

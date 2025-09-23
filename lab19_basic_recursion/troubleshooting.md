# Troubleshooting

## Common Errors & Fixes

### Python Not Installed
**Error:** `python3: command not found`  
**Fix:** `sudo apt install -y python3`

### pip Missing
**Error:** `No module named pip`  
**Fix:** `sudo apt install -y python3-pip`

### venv Missing
**Error:** `No module named venv`  
**Fix:** `sudo apt install -y python3-venv`

### Stack Overflow with Large n
**Error:** `RecursionError: maximum recursion depth exceeded`  
**Fix:** Use tail recursion or iterative approach for large values of `n`.

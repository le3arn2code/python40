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

### File Not Found
**Error:** `FileNotFoundError: [Errno 2] No such file or directory: 'sample.csv'`  
**Fix:** Ensure `sample.csv` exists in the same directory as the scripts.

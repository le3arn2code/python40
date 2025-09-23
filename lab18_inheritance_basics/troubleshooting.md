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

### Docker Not Installed or Inactive
(Not needed for this lab, but checked as part of pre-flight.)  
**Fix:**  
```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
```

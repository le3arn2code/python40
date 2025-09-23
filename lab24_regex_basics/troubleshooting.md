# Troubleshooting

## Common Errors & Fixes

### Python Not Installed
**Error:** `python3: command not found`  
**Fix:** `sudo apt install -y python3`

### pip Missing
**Error:** `No module named pip`  
**Fix:** `sudo apt install -y python3-pip`

### Regex Not Matching
**Error:** Pattern returns no matches.  
**Fix:** Ensure correct syntax. Use raw strings with `r"pattern"`.

### Wrong Substitution
**Error:** `re.sub()` not replacing text.  
**Fix:** Double-check regex pattern and input string.

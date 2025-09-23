# Troubleshooting for Lab 33

## Issues Faced
1. **ModuleNotFoundError: No module named 'bs4'**
   - Fixed by running: `python3 -m pip install beautifulsoup4 --break-system-packages`

2. **Externally-managed-environment error**
   - Occurred because of Ubuntu 24.04 restrictions.
   - Fixed by using `--break-system-packages` with pip.

3. **python not found**
   - Used `python3` instead of `python`.

## Final Working Commands
```bash
python3 -m pip install beautifulsoup4 lxml --break-system-packages
python3 lab33_scrape.py
```

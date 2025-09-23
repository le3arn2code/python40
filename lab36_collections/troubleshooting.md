# Troubleshooting - Lab 36

## Error 1
**Message:**
```
-bash: python: command not found
```
**Fix:** Use `python3` instead.

## Error 2
**Message:**
```
WARNING: Package(s) not found: beautifulsoup4
```
**Fix:** Installed using:
```
python3 -m pip install <package> --break-system-packages
```

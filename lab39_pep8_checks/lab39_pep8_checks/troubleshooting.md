# Troubleshooting for Lab 39

## Issues Faced
1. `flake8: command not found`
   - Cause: PATH did not include `~/.local/bin`.
   - Fix: Added `export PATH=$PATH:~/.local/bin`.

2. Formatting differences
   - `black` reformats code in one consistent way.
   - `autopep8` applies aggressive fixes but allows more configuration.


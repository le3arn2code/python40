# Troubleshooting - Lab 9: Dictionaries

## Common Issues

### 1. `NameError: name 'user_profile' is not defined`
- Ensure you initialized the dictionary before accessing it.

### 2. `KeyError`
- Happens if you try to access a key that does not exist.
- Fix: Verify the key exists or use `.get(key)` to safely access.

### 3. `AttributeError: 'dict' object has no attribute '...'`
- Make sure you’re using correct dictionary methods like `.items()`, `.keys()`, `.pop()`.


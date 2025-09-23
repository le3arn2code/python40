# Troubleshooting - Lab 11: Modules & Packages

1. **ModuleNotFoundError: No module named 'mymodule'**
   - Ensure you are importing correctly.
   - If using a package, use: `from mypackage import mymodule`.

2. **ImportError: No module named 'mypackage'**
   - Verify that `mypackage/` exists in the same folder as `main.py`.
   - Ensure it contains an `__init__.py` file.

3. **IndentationError**
   - Check that your code is properly indented.

4. **Python not found**
   - On some systems, use `python3` instead of `python`.

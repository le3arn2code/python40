# Interview Q&A - Lab 11: Modules & Packages

1. **Q: What is a module in Python?**
   A: A single `.py` file containing Python code, functions, or classes.

2. **Q: What is a package in Python?**
   A: A directory containing an `__init__.py` file and modules, used for organizing code.

3. **Q: How do you import a module in Python?**
   A: Using the `import` keyword, e.g., `import math`.

4. **Q: How do you import a module from a package?**
   A: `from package import module`.

5. **Q: What is the role of `__init__.py` in a package?**
   A: It marks a directory as a Python package and can be used to run initialization code.

6. **Q: Can a package contain sub-packages?**
   A: Yes, packages can be nested.

7. **Q: What is the difference between absolute and relative imports?**
   A: Absolute imports specify the full path (`from package import module`), while relative imports use `.` or `..` syntax inside packages.

8. **Q: Why use packages in Python?**
   A: To organize large projects, reuse code, and avoid name conflicts.

9. **Q: Can you import specific functions from a module?**
   A: Yes, e.g., `from math import sqrt`.

10. **Q: How do Python modules help maintainability?**
   A: They separate code into logical units, making debugging and updates easier.

# Lab 11: Modules & Packages

## Objectives
- Understand the concept of Python modules and how to use them.
- Learn how to import and use functions from modules.
- Recognize the structure and function of packages in Python.
- Practice creating your own modules and packages.

## Tasks
### Task 1: Creating and Using a Python Module
1. Create `mymodule.py` with a function `add(a, b)`.
2. Create `main.py` to import `mymodule` and call the function.

### Task 2: Understanding and Creating a Python Package
1. Create folder `mypackage/`.
2. Add `__init__.py` (empty file).
3. Move `mymodule.py` into `mypackage/`.
4. Update `main.py` to use:
```python
from mypackage import mymodule
```

## Expected Output
```
The sum of 5 and 3 is 8
```

## Conclusion
- Modules are single Python files containing definitions and code.
- Packages are directories with an `__init__.py` file, enabling hierarchical organization.
- These are key to structuring reusable, maintainable applications.

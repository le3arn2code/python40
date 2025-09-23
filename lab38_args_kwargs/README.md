# Lab 38: Parameter Passing & Unpacking

## Objectives
- Understand parameter passing in Python
- Use *args and **kwargs for flexible function arguments
- Practice unpacking lists and dictionaries

## Tasks
1. Implement `add_numbers(*args)` to sum arguments.
2. Implement `show_info(**kwargs)` to print named parameters.
3. Use * and ** for unpacking lists/dicts into functions.

## Errors & Fixes
- **Issue:** Syntax error when forgetting * in unpacking.  
  **Fix:** Always prefix with * or ** when unpacking.  

- **Issue:** TypeError if non-iterable passed to *args.  
  **Fix:** Ensure valid iterable/list is unpacked.

## Conclusion
We successfully used *args and **kwargs to pass flexible arguments and applied unpacking.  
These techniques help in writing dynamic, reusable Python functions.

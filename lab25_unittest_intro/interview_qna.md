# Interview Q&A - Lab 25: Intro to Unit Testing with unittest

### 1. What is unit testing?
Testing individual units or components of code to ensure correctness.

### 2. Which module in Python is used for unit testing?
The built-in `unittest` module.

### 3. How do you structure a test case in unittest?
By creating a class that inherits from `unittest.TestCase`.

### 4. What is the naming convention for test files?
Files should be prefixed with `test_` to be auto-discovered.

### 5. How do you run tests with unittest?
Using `python -m unittest discover`.

### 6. What does assertEqual() do?
Checks if two values are equal; fails the test otherwise.

### 7. How is a failed test displayed in output?
It shows `F` instead of `.` and provides error details.

### 8. Can unittest run multiple test cases?
Yes, all test cases in discovered files are executed.

### 9. Why is unit testing important?
It ensures correctness, prevents regressions, and improves maintainability.

### 10. Give a real-world use case of unittest.
Testing business logic like payment calculations or API responses before deployment.

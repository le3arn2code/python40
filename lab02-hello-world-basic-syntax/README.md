# Lab 2 – Hello World & Basic Syntax

## 🎯 Objectives
- Understand how to create a simple Python script.
- Learn how to execute a Python script using the command line.
- Gain familiarity with Python's indentation rules to define code blocks.
- Experiment with basic syntax through simple control structures.

## 📋 Prerequisites
- Basic knowledge of how to navigate your computer's file system.
- Python installed on your computer (version 3.x is recommended).

## 🛠️ Tasks

### Task 1: Create a Simple Python Script
1. Open your favorite text editor (VS Code, Sublime Text, Notepad++).  
2. Create a file named `hello.py`.  
3. Add the following code:  
```python
print("Hello, World!")
```

### Task 2: Run the Python Script
1. Open terminal (Command Prompt/PowerShell on Windows, Terminal on macOS/Linux).  
2. Navigate to the folder where `hello.py` is saved. Example:  
```bash
cd Documents
```
3. Run the script:  
```bash
python hello.py
```
Expected output:  
```
Hello, World!
```

### Task 3: Experiment with Indentation
1. Update `hello.py`:  
```python
if True:
    print("This will always print because the condition is True.")
print("Hello, World!")
```

2. Observe that the indented `print` inside `if` executes correctly.  

3. Try incorrect indentation:  
```python
if True:
print("This will cause an IndentationError.")
```

4. Fix indentation by using 4 spaces:  
```python
if True:
    print("This will always print because the condition is True.")
```

## ✅ Conclusion
- You created and executed a Python script.  
- You learned about Python’s indentation rules.  
- You saw how improper indentation raises an `IndentationError`.  
This foundational knowledge prepares you for writing more complex Python programs.

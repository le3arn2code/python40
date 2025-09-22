# Lab 5 – Understanding Conditionals (if, elif, else)

## 🎯 Objectives
- Understand how to implement conditional logic using if, elif, and else statements.
- Learn to handle multiple conditions and determine the program flow accordingly.
- Practice coding with conditional statements to classify input data.

## 📋 Prerequisites
- Basic understanding of Python syntax.
- Familiarity with variables and data types.

## 🛠️ Tasks

### Task 1: User Input and Number Classification
```python
# conditionals.py
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Task 2: Exploring Multiple Conditions with Elif
```python
# grading_system.py
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

## ✅ Conclusion
- Using if, elif, and else, you can control the flow of your program based on conditions.
- This equips you with the basics to implement multiple condition checks efficiently.

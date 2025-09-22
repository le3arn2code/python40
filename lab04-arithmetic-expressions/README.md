# Lab 4 – Arithmetic & Expressions

## 🎯 Objectives
- Understand and apply basic arithmetic operations using Python.
- Differentiate between integer division and float division.
- Write and execute scripts to perform arithmetic expressions.

## 📋 Prerequisites
- Basic knowledge of Python programming.
- Understanding of fundamental arithmetic operations.
- Python installed on your computer.

## 📝 Introduction
Arithmetic operations are foundational to data manipulation and numerical analysis in programming. They enable you to perform mathematical calculations through expressions, thereby forming the basis of algorithms and logic development.

## 🛠️ Tasks

### Task 1: Writing a Script to Perform Basic Arithmetic Operations
1. Create a file named `arithmetic_operations.py`.
2. Add the following code:
```python
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Addition
addition_result = number1 + number2
print(f"Addition: {number1} + {number2} = {addition_result}")

# Subtraction
subtraction_result = number1 - number2
print(f"Subtraction: {number1} - {number2} = {subtraction_result}")

# Multiplication
multiplication_result = number1 * number2
print(f"Multiplication: {number1} * {number2} = {multiplication_result}")

# Division
division_result = number1 / number2
print(f"Division: {number1} / {number2} = {division_result}")
```

### Task 2: Exploring Integer Division vs Float Division
1. Add the following lines to the script:
```python
# Integer Division
integer_division_result = number1 // number2
print(f"Integer Division: {number1} // {number2} = {integer_division_result}")

# Float Division
float_division_result = number1 / number2
print(f"Float Division: {number1} / {number2} = {float_division_result}")
```

## 🔑 Key Concepts
- **Addition (+):** Combining two numbers into a sum.
- **Subtraction (-):** Subtracting one number from another.
- **Multiplication (*):** Calculating the product of two numbers.
- **Division (/):** Calculating the quotient by dividing one number by another.
- **Integer Division (//):** Returns the floor value of the division.
- **Float Division (/):** Returns the exact decimal value of the division.

## ✅ Conclusion
In this lab, you learned how to implement fundamental arithmetic operations and explored the differences between integer and float division in Python. These operations are a critical step towards mastering more complex programming tasks.

## 🔎 Further Exploration
- Experiment with larger numbers and decimals.
- Use arithmetic operations in real-world problems such as budgeting or calculating areas.

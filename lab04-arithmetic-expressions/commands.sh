#!/bin/bash
# Lab 4 – Arithmetic & Expressions

# Step 1: Create the script
cat <<EOL > arithmetic_operations.py
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Basic operations
addition_result = number1 + number2
print(f"Addition: {number1} + {number2} = {addition_result}")

subtraction_result = number1 - number2
print(f"Subtraction: {number1} - {number2} = {subtraction_result}")

multiplication_result = number1 * number2
print(f"Multiplication: {number1} * {number2} = {multiplication_result}")

division_result = number1 / number2
print(f"Division: {number1} / {number2} = {division_result}")

# Integer vs Float division
integer_division_result = number1 // number2
print(f"Integer Division: {number1} // {number2} = {integer_division_result}")

float_division_result = number1 / number2
print(f"Float Division: {number1} / {number2} = {float_division_result}")
EOL

# Step 2: Run the script
python3 arithmetic_operations.py

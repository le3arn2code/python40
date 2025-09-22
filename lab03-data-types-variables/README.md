# Lab 3 – Data Types & Variables

## 🎯 Objectives
- Understand the concept of data types and variables in programming.
- Learn how to create and manipulate different data types in Python.
- Gain knowledge about implicit and explicit type casting.

## 📋 Prerequisites
- Basic understanding of programming concepts.
- Python installed on your system (version 3.x recommended).

## 🛠️ Tasks

### Task 1: Understanding and Creating Variables
```python
name = "John Doe"  # A string
age = 25           # An integer
is_student = True  # A boolean
height = 175.5     # A float

print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Is Student:", is_student, "Type:", type(is_student))
print("Height:", height, "Type:", type(height))
```

### Task 2: Implicit vs Explicit Type Casting

#### Implicit Casting
```python
a = 10
b = 10.5
result = a + b
print("Result:", result, "Type:", type(result))
```

#### Explicit Casting
```python
age_str = str(age)
print("Age as string:", age_str, "Type:", type(age_str))

number_str = "100"
number_int = int(number_str)
print("Number:", number_int, "Type:", type(number_int))
```

### Task 3: Case Study – Customer Data Intake
```python
customer_name = "Alice Johnson"
customer_age = "30"  # Initially a string
customer_membership = "True"

customer_age = int(customer_age)
customer_membership = customer_membership == "True"

print("Customer Name:", customer_name, "Type:", type(customer_name))
print("Customer Age:", customer_age, "Type:", type(customer_age))
print("Customer Membership Status:", customer_membership, "Type:", type(customer_membership))
```

## ✅ Conclusion
- You learned how to create and manipulate various data types in Python.
- You explored implicit and explicit type casting.
- You applied these concepts to a practical case study.

#!/bin/bash
# Lab 3 – Data Types & Variables

# Step 1: Variables
cat <<EOL > variables.py
name = "John Doe"
age = 25
is_student = True
height = 175.5

print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Is Student:", is_student, "Type:", type(is_student))
print("Height:", height, "Type:", type(height))
EOL
python3 variables.py

# Step 2: Implicit Casting
cat <<EOL > implicit_cast.py
a = 10
b = 10.5
result = a + b
print("Result:", result, "Type:", type(result))
EOL
python3 implicit_cast.py

# Step 3: Explicit Casting
cat <<EOL > explicit_cast.py
age = 25
age_str = str(age)
print("Age as string:", age_str, "Type:", type(age_str))

number_str = "100"
number_int = int(number_str)
print("Number:", number_int, "Type:", type(number_int))
EOL
python3 explicit_cast.py

# Step 4: Case Study
cat <<EOL > customer.py
customer_name = "Alice Johnson"
customer_age = "30"
customer_membership = "True"

customer_age = int(customer_age)
customer_membership = customer_membership == "True"

print("Customer Name:", customer_name, "Type:", type(customer_name))
print("Customer Age:", customer_age, "Type:", type(customer_age))
print("Customer Membership Status:", customer_membership, "Type:", type(customer_membership))
EOL
python3 customer.py

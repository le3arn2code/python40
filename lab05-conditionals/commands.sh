#!/bin/bash
# Lab 5 – Understanding Conditionals (if, elif, else)

# Step 1: Create conditionals.py
cat <<EOL > conditionals.py
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
EOL

# Step 2: Run conditionals.py
python3 conditionals.py

# Step 3: Create grading_system.py
cat <<EOL > grading_system.py
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
EOL

# Step 4: Run grading_system.py
python3 grading_system.py

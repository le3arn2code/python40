#!/bin/bash
# Lab 7 – Lists and List Methods

# Step 1: Create lists_example.py
cat <<EOL > lists_example.py
fruits = ["apple", "banana", "cherry"]
print("Initial list of fruits:", fruits)

fruits.append("orange")
print("List after appending 'orange':", fruits)

fruits.remove("banana")
print("List after removing 'banana':", fruits)

fruits.sort()
print("Sorted list of fruits:", fruits)

for fruit in fruits:
    print("Fruit:", fruit)
EOL

# Step 2: Run the script
python3 lists_example.py

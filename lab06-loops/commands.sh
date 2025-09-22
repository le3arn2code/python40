#!/bin/bash
# Lab 6 – For & While Loops

# Step 1: Create for_loop_example.py
cat <<EOL > for_loop_example.py
for i in range(1, 6):
    print(i)
EOL

# Run for_loop_example.py
python3 for_loop_example.py

# Step 2: Create while_loop_example.py
cat <<EOL > while_loop_example.py
total = 0
i = 1

while total <= 20:
    total += i
    i += 1

print("Final total:", total)
EOL

# Run while_loop_example.py
python3 while_loop_example.py

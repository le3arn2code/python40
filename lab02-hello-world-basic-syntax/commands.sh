#!/bin/bash
# Lab 2 – Hello World & Basic Syntax

# Step 1: Create hello.py
echo 'print("Hello, World!")' > hello.py

# Step 2: Run script
python3 hello.py

# Step 3: Add indentation example
cat <<EOL > hello.py
if True:
    print("This will always print because the condition is True.")
print("Hello, World!")
EOL

# Step 4: Run updated script
python3 hello.py

# Step 5: Create faulty script to show IndentationError
cat <<EOL > hello.py
if True:
print("This will cause an IndentationError.")
EOL

python3 hello.py || echo "IndentationError occurred"

# Step 6: Fix indentation
cat <<EOL > hello.py
if True:
    print("This will always print because the condition is True.")
print("Hello, World!")
EOL

python3 hello.py

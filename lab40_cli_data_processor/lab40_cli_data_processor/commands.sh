#!/bin/bash
# Commands for Lab 40: CLI Data Processor

# Step 1: Install requests
python3 -m pip install requests --break-system-packages

# Step 2: Run CLI tool with sample API
python3 data_processor.py --api_url https://jsonplaceholder.typicode.com/posts --file_path output.json

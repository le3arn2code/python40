# Lab 14: JSON Handling

## Objectives
- Understand how to create a Python dictionary and convert it to JSON.
- Learn how to store JSON data in a file and read it back.
- Comprehend the use of JSON for storing configuration or data.

## Prerequisites
- Basic knowledge of Python programming.
- Understanding of data structures like dictionaries and lists in Python.
- Familiarity with file handling in Python.

## Lab Tasks

### Task 1: Create and Convert a Python Dictionary to JSON
```python
employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "Engineering",
    "skills": ["Python", "Django", "Machine Learning"]
}

import json
employee_data_json = json.dumps(employee_data, indent=4)
print(employee_data_json)
```

### Task 2: Store JSON Data in a File
```python
with open("employee_data.json", "w") as json_file:
    json_file.write(employee_data_json)
```

### Task 3: Read JSON Data from the File
```python
with open("employee_data.json", "r") as json_file:
    data = json.load(json_file)
    print(data)
```

## Errors & Fixes
- `ModuleNotFoundError: No module named 'json'`: Resolved by confirming Python standard library includes `json`.
- File not found error: Ensure working directory contains `employee_data.json` before reading.

## Conclusion
- JSON handling in Python involves converting data structures for storage and transmission.
- The json module provides straightforward methods for working with JSON.
- Essential for modern development, APIs, and configurations.

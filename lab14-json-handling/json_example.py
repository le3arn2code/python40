import json

# Step 1: Create a Python dictionary
employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "Engineering",
    "skills": ["Python", "Django", "Machine Learning"]
}

# Step 2: Convert to JSON string
employee_data_json = json.dumps(employee_data, indent=4)
print("JSON String:")
print(employee_data_json)

# Step 3: Write JSON to a file
with open("employee_data.json", "w") as json_file:
    json_file.write(employee_data_json)

# Step 4: Read JSON back from the file
with open("employee_data.json", "r") as json_file:
    data = json.load(json_file)
    print("\nRead back from file:")
    print(data)

# Lab 9: Dictionaries and Key Operations

## Objectives
- Understand the structure and use of dictionaries in Python.
- Learn how to perform key operations such as adding, updating, accessing, and removing dictionary entries.
- Explore methods for iterating over dictionary items and keys.

## Tasks
1. **Create a Dictionary for a User Profile**
   ```python
   user_profile = {
       "name": "Alice",
       "age": 30,
       "city": "New York"
   }
   print(user_profile)
   ```

2. **Access and Update Dictionary Values**
   ```python
   print("User's Name:", user_profile["name"])
   user_profile["age"] = 31
   print("Updated User Profile:", user_profile)
   ```

3. **Remove a Key from the Dictionary**
   ```python
   user_profile.pop("city")
   print("Profile after removing city:", user_profile)
   ```

4. **Iterate Over Dictionary Items and Keys**
   ```python
   for key, value in user_profile.items():
       print(f"{key}: {value}")
   for key in user_profile.keys():
       print(f"Key: {key}")
   ```

## Conclusion
- You created, updated, removed, and iterated over a dictionary.
- This lab demonstrated essential dictionary operations useful in real-world applications like JSON handling and database mappings.

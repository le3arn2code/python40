# Interview Q&A - Lab 14 JSON Handling

1. **What is JSON?**  
   JSON (JavaScript Object Notation) is a lightweight data interchange format.

2. **How do you convert a Python dictionary into JSON?**  
   Using `json.dumps()`.

3. **How do you read JSON from a file in Python?**  
   Using `json.load(file_object)`.

4. **What’s the difference between json.dump() and json.dumps()?**  
   `dump()` writes JSON to a file, `dumps()` returns JSON as a string.

5. **What’s the difference between json.load() and json.loads()?**  
   `load()` reads JSON from a file, `loads()` reads JSON from a string.

6. **What does indent=4 mean in json.dumps()?**  
   It formats JSON output with 4 spaces indentation.

7. **Why use JSON for configurations?**  
   It’s lightweight, human-readable, and language-independent.

8. **How are JSON arrays represented in Python?**  
   As Python lists.

9. **What are some limitations of JSON?**  
   It cannot represent custom Python objects directly (needs serialization).

10. **Why is JSON popular in APIs?**  
   It’s easy to parse and widely supported across platforms.

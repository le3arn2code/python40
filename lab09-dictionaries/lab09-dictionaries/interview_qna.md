# Interview Q&A - Lab 9: Dictionaries and Key Operations

### Q1: What is a dictionary in Python?
A dictionary is a collection of key-value pairs where each key is unique.

### Q2: How do you access a value from a dictionary?
By using the key inside square brackets, e.g., `dict["key"]`.

### Q3: How do you update a dictionary value?
Reassign the key, e.g., `dict["key"] = new_value`.

### Q4: How do you remove an item from a dictionary?
Use `pop(key)` to remove and return the value of the key.

### Q5: What is the difference between `.items()` and `.keys()`?
- `.items()` returns key-value pairs as tuples.
- `.keys()` returns only the keys.

### Q6: Can dictionary keys be mutable objects?
No, keys must be immutable (e.g., strings, numbers, tuples).

### Q7: How does Python handle duplicate keys in a dictionary?
The latest value assignment overrides the previous one.

### Q8: How do you safely access a key without risking a KeyError?
Use `.get(key)` which returns `None` or a default value if the key doesn’t exist.

### Q9: Can dictionaries be nested?
Yes, dictionaries can contain other dictionaries as values.

### Q10: Give a real-world use case of dictionaries.
Dictionaries are often used for JSON parsing, configuration storage, or mapping unique identifiers to values.

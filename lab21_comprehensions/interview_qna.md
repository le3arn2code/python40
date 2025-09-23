# Interview Q&A - Lab 21: List/Dict Comprehensions

### 1. What is a list comprehension in Python?
A list comprehension is a concise way to create a new list using `[expression for item in iterable]`.

### 2. What is a dictionary comprehension?
A dictionary comprehension uses `{key: value for item in iterable}` to create dictionaries.

### 3. How does list comprehension differ from a loop?
Comprehensions are shorter, more readable, and often faster than loops.

### 4. Can comprehensions include conditions?
Yes, you can filter with conditions, e.g. `[x for x in range(10) if x % 2 == 0]`.

### 5. Are comprehensions faster than loops?
Often yes, because they are optimized internally in Python.

### 6. Can comprehensions replace nested loops?
Yes, nested comprehensions exist, but readability may suffer if overused.

### 7. What is the advantage of dictionary comprehensions?
They allow easy creation of key-value mappings without writing explicit loops.

### 8. Are comprehensions always the best choice?
Not always—if logic is too complex, loops may be clearer.

### 9. What happens if you use comprehensions with large data?
They still work efficiently, but memory usage must be considered.

### 10. Give a practical use case of comprehensions.
Transforming datasets, filtering lists, mapping values to their attributes.

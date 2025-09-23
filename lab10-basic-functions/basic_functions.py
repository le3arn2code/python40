# Lab 10: Basic Functions

# Task 1: Define a function greet(name)
def greet(name="Guest"):
    return f"Hello, {name}!"

# Task 2: Call the function and print results
print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))

# Task 3: Default parameter
print(greet())

# Task 4: Keyword arguments
print(greet(name="Diana"))

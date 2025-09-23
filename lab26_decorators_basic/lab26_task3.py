# Task 3: Applying the Decorator

from lab26_task1_2 import log_decorator

@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Call the function to see decorator in action
say_hello("Alice")

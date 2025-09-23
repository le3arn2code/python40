# Task 2a: Custom Context Manager

class MyContext:
    def __enter__(self):
        print("Entering the context and allocating resources.")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context and cleaning up resources.")

with MyContext() as context:
    print("Running within the context block.")

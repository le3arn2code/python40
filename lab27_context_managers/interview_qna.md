# Interview Q&A: Lab 27 - Context Managers

**Q1. What is a context manager in Python?**  
A context manager is an object that defines `__enter__` and `__exit__` methods to manage resources.

**Q2. What is the role of the `with` statement?**  
It simplifies resource management by automatically calling `__enter__` and `__exit__`.

**Q3. What happens if an exception occurs in a `with` block?**  
The `__exit__` method is still called, ensuring cleanup.

**Q4. Give an example of a built-in context manager.**  
The `open()` function for file handling is a built-in context manager.

**Q5. What methods must a custom context manager implement?**  
`__enter__` and `__exit__`.

**Q6. What does the `__enter__` method return?**  
It usually returns the resource to be managed.

**Q7. What are cross-cutting concerns where context managers help?**  
File handling, database connections, threading locks, sockets.

**Q8. How is a context manager different from try-finally?**  
Context managers automate try-finally logic for resource cleanup.

**Q9. Can context managers be nested?**  
Yes, multiple `with` statements can be nested for managing multiple resources.

**Q10. What module provides utilities for context managers?**  
The `contextlib` module provides helpers like `contextmanager` decorator.

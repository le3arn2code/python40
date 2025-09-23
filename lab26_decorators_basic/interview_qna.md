# Interview Q&A: Lab 26 - Decorators

**Q1. What is a Python decorator?**  
A decorator is a function that modifies another function without changing its source code.

**Q2. Why use decorators?**  
To implement cross-cutting concerns like logging, caching, and authentication.

**Q3. How do you apply a decorator?**  
By using the `@decorator_name` syntax above a function.

**Q4. Can decorators take arguments?**  
Yes, you can nest functions to allow decorators with parameters.

**Q5. What are *args and **kwargs used for in decorators?**  
They allow the decorator to accept arbitrary arguments from the wrapped function.

**Q6. What is the difference between a decorator and a normal function call?**  
A decorator modifies the behavior of a function, while a normal call just executes it.

**Q7. Can multiple decorators be applied to the same function?**  
Yes, they can be stacked and are applied from bottom to top.

**Q8. What module in Python provides built-in decorators?**  
The `functools` module provides `@lru_cache`, `@wraps`, etc.

**Q9. How can decorators help in logging?**  
They centralize logging logic, so you don’t need to add print/log statements inside each function.

**Q10. What happens if you forget to return the wrapper in a decorator?**  
The original function will not be executed because it is replaced by `None`.

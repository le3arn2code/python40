# Interview Q&A - Lab 38

1. Q: What is *args in Python?
   A: *args collects variable positional arguments into a tuple.

2. Q: What is **kwargs?
   A: **kwargs collects keyword arguments into a dictionary.

3. Q: Can you use both *args and **kwargs in one function?
   A: Yes, but *args must come before **kwargs.

4. Q: Why use *args?
   A: To accept arbitrary numbers of positional arguments.

5. Q: Why use **kwargs?
   A: To accept arbitrary numbers of keyword arguments.

6. Q: Difference between * and ** unpacking?
   A: * unpacks sequences, ** unpacks dictionaries.

7. Q: Example of when to use **kwargs?
   A: When passing config parameters into functions.

8. Q: Can *args be empty?
   A: Yes, then it is an empty tuple.

9. Q: Can **kwargs be empty?
   A: Yes, then it is an empty dict.

10. Q: Which is more flexible, *args or **kwargs?
    A: **kwargs, since it allows descriptive named parameters.

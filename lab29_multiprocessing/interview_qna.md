# Interview Q&A - Lab 29: Multiprocessing Basics

**Q1: What is multiprocessing in Python?**  
A1: Multiprocessing allows running multiple processes in parallel, each with its own memory space.

**Q2: How is multiprocessing different from threading?**  
A2: Threads share memory space, while processes run in separate memory spaces, avoiding race conditions but making communication harder.

**Q3: When should you use multiprocessing over threading?**  
A3: Use multiprocessing for CPU-bound tasks and threading for I/O-bound tasks.

**Q4: Why is the `if __name__ == '__main__':` guard important?**  
A4: It prevents recursive process spawning when using multiprocessing on Windows.

**Q5: What are common inter-process communication mechanisms?**  
A5: Queues, Pipes, and shared memory objects.

**Q6: What is a race condition?**  
A6: A bug that occurs when multiple threads or processes attempt to modify shared resources simultaneously without proper synchronization.

**Q7: How does multiprocessing improve performance?**  
A7: It utilizes multiple CPU cores to perform tasks concurrently.

**Q8: Can processes share memory directly?**  
A8: No, but they can communicate via queues, pipes, or managers.

**Q9: What happens if you forget to call join()?**  
A9: The main program may terminate before child processes finish execution.

**Q10: Give a real-world use case for multiprocessing.**  
A10: Processing large datasets, image transformations, or parallel simulations where CPU usage is intensive.

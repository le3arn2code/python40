# Lab 28 Interview Q&A

**Q1: What is a thread in Python?**  
A lightweight subprocess that allows for concurrent execution.

**Q2: Which module provides threading support in Python?**  
The `threading` module.

**Q3: How do you start a thread?**  
By calling `thread.start()`.

**Q4: How do you make the main program wait for a thread to complete?**  
Use `thread.join()`.

**Q5: What is shared memory in threading?**  
Threads share the same memory space, allowing access to the same variables.

**Q6: What is a race condition?**  
An error caused when multiple threads access and modify shared data concurrently without synchronization.

**Q7: How can race conditions be prevented?**  
By using synchronization mechanisms like locks or semaphores.

**Q8: Why is thread output interleaved?**  
Because the scheduler decides the order of execution dynamically.

**Q9: When should you use multithreading?**  
When tasks are I/O-bound and can benefit from concurrent execution.

**Q10: What are alternatives to threading in Python for concurrency?**  
Multiprocessing and asyncio.

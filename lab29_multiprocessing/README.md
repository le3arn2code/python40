# Lab 29: Multiprocessing Basics

## Objectives
- Understand the basics of multiprocessing in Python.
- Learn how to create and manipulate multiple processes.
- Differentiate between processes and threads, especially regarding memory sharing.

## Steps Summary
1. Import the `multiprocessing` module.
2. Define a CPU-bound function (`sum_large_list`).
3. Create and start multiple processes with `multiprocessing.Process`.
4. Use `start()` to run them concurrently and `join()` to wait for completion.
5. Compare multiprocessing with threading.

## Conclusion
Multiprocessing allows you to run processes in parallel, each with its own memory space, ideal for CPU-bound tasks.

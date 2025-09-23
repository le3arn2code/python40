# Troubleshooting - Lab 29: Multiprocessing Basics

## Common Issues

1. **Script does not run**
   - Ensure Python 3 is installed and accessible via `python` or `python3`.

2. **Processes do not start**
   - Make sure the `if __name__ == '__main__':` guard is included.

3. **Performance issues**
   - Multiprocessing is best for CPU-bound tasks; for I/O tasks, use multithreading.

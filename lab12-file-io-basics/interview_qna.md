# Interview Q&A

**Q1: What are file modes in Python?**  
A: 'r' for read, 'w' for write (overwrites file), 'a' for append, 'b' for binary, '+' for read/write.

**Q2: What is the role of context managers in File I/O?**  
A: They automatically handle opening and closing of files, ensuring no resource leaks.

**Q3: What happens if you open a file in 'w' mode and it already exists?**  
A: The file is truncated (cleared) before writing.

**Q4: Difference between readline() and readlines()?**  
A: readline() reads one line, readlines() reads all lines into a list.

**Q5: How to handle exceptions in File I/O?**  
A: Use try-except blocks around file operations, though context managers handle closing automatically.

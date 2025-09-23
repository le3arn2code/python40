# Lab 34 Interview Q&A

**Q1: Why use Python for file management instead of manual operations?**  
A1: Automation reduces repetitive work, avoids human error, and is scalable.

**Q2: What modules are commonly used for file management in Python?**  
A2: `os` for directory and file handling, `shutil` for file operations.

**Q3: How do you list all files in a directory?**  
A3: Using `os.listdir(path)`.

**Q4: How do you ensure a folder exists before copying files?**  
A4: Use `os.makedirs(destination, exist_ok=True)`.

**Q5: What is the advantage of using `shutil.copy()`?**  
A5: It preserves file content and permissions.

**Q6: How can you rename files during copying?**  
A6: Modify the filename with `os.path.splitext()` and append suffix/prefix.

**Q7: What happens if the destination file already exists?**  
A7: It will be overwritten unless explicitly handled.

**Q8: What’s the difference between `shutil.copy()` and `shutil.move()`?**  
A8: `copy()` duplicates files, `move()` transfers them.

**Q9: What real-world use cases need such scripts?**  
A9: Automated backups, log archiving, bulk file renaming.

**Q10: How do you add logging to such scripts?**  
A10: Use Python’s `logging` module for tracking operations and errors.

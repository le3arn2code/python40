# Interview Q&A – Lab 1

**Q1. How do you install Python on Linux?**  
A: `sudo apt-get update && sudo apt-get install python3`.

**Q2. How do you verify the installed Python version?**  
A: Run `python3 --version`.

**Q3. Why check “Add Python to PATH” on Windows?**  
A: To make Python accessible from command line.

**Q4. Popular IDEs for Python?**  
A: VS Code, PyCharm, Sublime, Atom.

**Q5. How do you install VS Code on Ubuntu?**  
A: Add Microsoft repo, then `sudo apt install code`.

**Q6. What causes apt lock errors?**  
A: Background process like unattended-upgrades.

**Q7. How to fix apt lock errors?**  
A: Kill process, remove lock files, run `dpkg --configure -a`.

**Q8. How to avoid exposing secrets in GitHub?**  
A: Use `.env` files, `.gitignore`, environment variables.

**Q9. How do you configure Python in VS Code?**  
A: Install Python extension, set correct interpreter.

**Q10. Why use virtual environments?**  
A: To isolate dependencies and avoid conflicts.

# Interview Q&A - Virtual Environments

1. **What is a virtual environment in Python?**
   An isolated environment for dependencies specific to a project.

2. **Why use virtual environments?**
   To avoid dependency conflicts between projects.

3. **How do you create one?**
   `python3 -m venv myenv`

4. **How do you activate it on Linux/macOS?**
   `source myenv/bin/activate`

5. **How do you activate it on Windows?**
   `.\myenv\Scripts\activate`

6. **How do you deactivate it?**
   Run `deactivate`.

7. **Where are packages installed inside venv?**
   In the `myenv/lib/.../site-packages` folder.

8. **What is the difference between venv and global Python?**
   venv isolates dependencies, global affects the whole system.

9. **Can we have multiple venvs for different projects?**
   Yes, each project can have its own isolated environment.

10. **Why is isolation important?**
    Prevents version clashes and ensures reproducibility.

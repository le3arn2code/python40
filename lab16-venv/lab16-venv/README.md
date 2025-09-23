# Lab 16: Virtual Environments (venv)

## Objectives
- Understand the purpose and benefits of using virtual environments in Python.
- Learn to create, activate, and deactivate a virtual environment.
- Practice installing Python packages within a virtual environment.
- Recognize how virtual environments help maintain project dependencies and isolation.

## Steps
1. Create a virtual environment:
   ```bash
   python3 -m venv myenv
   ```
2. Activate it:
   ```bash
   source myenv/bin/activate   # Linux/macOS
   .\myenv\Scripts\activate  # Windows
   ```
3. Install requests inside venv:
   ```bash
   pip install requests
   ```
4. Verify installation:
   ```bash
   pip list
   ```
5. Deactivate:
   ```bash
   deactivate
   ```

## Conclusion
Virtual environments provide isolation, preventing dependency conflicts across projects.

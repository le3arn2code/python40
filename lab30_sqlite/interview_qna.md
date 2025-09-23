# Interview Q&A – Lab 30: Basic SQLite Usage

1. **Q:** What is SQLite in Python?  
   **A:** A lightweight, file-based relational database included in Python’s standard library.

2. **Q:** What does `sqlite3.connect(':memory:')` do?  
   **A:** Creates a temporary in-memory database that disappears when the program ends.

3. **Q:** What is a cursor in SQLite?  
   **A:** An object that executes SQL queries and retrieves results.

4. **Q:** Why do we use `executemany`?  
   **A:** For efficiently inserting multiple rows in one command.

5. **Q:** What does `connection.commit()` do?  
   **A:** Saves (commits) changes made to the database.

6. **Q:** What is the difference between `fetchone()` and `fetchall()`?  
   **A:** `fetchone()` returns the next single row, `fetchall()` returns all results.

7. **Q:** How do you ensure data persists beyond program execution?  
   **A:** Connect to a file database, e.g., `sqlite3.connect('students.db')`.

8. **Q:** Can SQLite handle multiple users?  
   **A:** Limited support; best suited for single-user or small-scale applications.

9. **Q:** Why is SQLite good for testing?  
   **A:** Lightweight, requires no setup, and supports full SQL.

10. **Q:** How to avoid SQL injection when inserting values?  
    **A:** Use parameterized queries with placeholders `?`.

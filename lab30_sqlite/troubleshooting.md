# Troubleshooting

1. **Error: sqlite3 module not found**
   - Resolution: Ensure you are using Python 3.x. `sqlite3` comes with standard library.

2. **Error: Syntax error in SQL**
   - Resolution: Double-check SQL statements (CREATE TABLE, INSERT, SELECT).

3. **Output not printed**
   - Resolution: Ensure you called `fetchall()` and iterated with a loop.

4. **Database lost after script ends**
   - Explanation: Using `:memory:` creates an in-memory DB. Use `sqlite3.connect('mydb.sqlite')` for persistence.

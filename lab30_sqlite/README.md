# Lab 30: Basic SQLite Usage

## Objectives
- Understand how to use SQLite in Python.
- Establish a connection to an SQLite database.
- Create a table and insert data into it.
- Query the table and fetch results.
- Print and interpret the fetched results.

## Steps
1. Import `sqlite3` (no installation required).
2. Connect to an in-memory SQLite database (`:memory:`).
3. Create a `students` table with `id`, `name`, and `grade`.
4. Insert multiple rows with `executemany`.
5. Query the table with `SELECT * FROM students`.
6. Print the results row by row.

## Expected Output
```
(1, 'Alice', 85.5)
(2, 'Bob', 78.0)
(3, 'Charlie', 92.0)
```

## Summary
This lab demonstrated connecting to SQLite, creating tables, inserting rows, and querying results.  
It reinforced structured database operations and cursor usage.

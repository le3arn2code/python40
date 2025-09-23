import sqlite3

# Task 2: Connect to SQLite Database (In-Memory)
connection = sqlite3.connect(':memory:')

# Task 3: Create a Table
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade REAL
)
""")

# Task 4: Insert Rows into Table
students_data = [
    (1, 'Alice', 85.5),
    (2, 'Bob', 78.0),
    (3, 'Charlie', 92.0)
]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students_data)
connection.commit()

# Task 5: Query the Table
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()

# Task 6: Fetch and Print Results
for row in results:
    print(row)

# Close the connection
connection.close()

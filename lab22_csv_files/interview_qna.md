# Interview Q&A - Lab 22: Reading CSV Files

### 1. What does CSV stand for?
CSV stands for Comma-Separated Values.

### 2. How do you read a CSV file in Python?
By using the built-in `csv` module and `csv.reader()`.

### 3. What is the difference between csv.reader() and csv.DictReader()?
`csv.reader()` returns rows as lists, while `csv.DictReader()` maps rows to dictionaries using headers as keys.

### 4. How do you handle a CSV file with headers?
Use `next(csv_reader)` to skip the header row, or use `csv.DictReader()`.

### 5. What happens if the CSV file has no headers?
You iterate directly over rows with `csv.reader()`.

### 6. How do you store CSV data in a structured format?
Use a list of dictionaries created with `csv.DictReader()`.

### 7. What Python function is commonly used to open CSV files?
The built-in `open()` function with mode `"r"` for reading.

### 8. Why use 'with open(...) as file' syntax?
It ensures the file is properly closed after reading.

### 9. How do you handle missing files gracefully?
Wrap file opening in a try-except block to catch `FileNotFoundError`.

### 10. Give a real-world use case of reading CSV files in Python.
Processing exported data from spreadsheets, databases, or logs for analysis.

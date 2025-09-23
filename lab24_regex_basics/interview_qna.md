# Interview Q&A - Lab 24: Basic Regular Expressions

### 1. What is a regular expression?
A sequence of characters that define a search pattern, mainly for string matching.

### 2. Which Python module is used for regex?
The built-in `re` module.

### 3. How do you search for a pattern in Python?
Using `re.search(pattern, string)`.

### 4. What does `re.findall()` return?
A list of all matches found in the string.

### 5. What does `^` and `$` mean in regex?
`^` matches the start of a string, `$` matches the end.

### 6. What is the purpose of `\d`?
It matches any digit (0–9).

### 7. Why use raw strings in regex patterns?
To prevent Python from interpreting backslashes as escape characters.

### 8. How do you replace text with regex?
Using `re.sub(pattern, replacement, string)`.

### 9. What happens if a pattern does not match?
The regex function returns `None` or an empty list.

### 10. Give a real-world use case of regex.
Validating email addresses, phone numbers, or extracting log data.

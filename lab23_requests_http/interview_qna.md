# Interview Q&A - Lab 23: Using requests for HTTP Calls

### 1. What is the purpose of the requests library in Python?
It simplifies making HTTP requests such as GET and POST.

### 2. How do you install the requests library?
Using `pip install requests`.

### 3. How do you send a GET request using requests?
By calling `requests.get(url)`.

### 4. What does response.status_code represent?
It represents the HTTP status code (e.g., 200 for OK, 404 for Not Found).

### 5. How do you parse JSON responses with requests?
By calling `response.json()` which converts it to a Python dictionary.

### 6. What are common HTTP status codes?
200 (OK), 404 (Not Found), 500 (Server Error).

### 7. Why use 'with open(...)' in file handling but not for requests?
Requests automatically handles connections, while files need explicit closing.

### 8. What happens if requests is not installed?
Python raises `ModuleNotFoundError: No module named 'requests'`.

### 9. Can requests handle other HTTP methods?
Yes, it supports GET, POST, PUT, DELETE, etc.

### 10. Give a real-world use case for requests.
Interacting with REST APIs like GitHub, weather APIs, or payment gateways.

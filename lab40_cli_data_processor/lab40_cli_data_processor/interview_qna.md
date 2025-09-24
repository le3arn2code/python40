# Lab 40: Interview Q&A

### Q1. Why use argparse instead of sys.argv?
Argparse provides structured argument parsing, built-in help messages, and validation.

### Q2. How do you handle invalid API responses?
Check with `response.raise_for_status()` and wrap in try/except blocks.

### Q3. Why use logging instead of print?
Logging adds timestamps, severity levels, and is more suitable for production systems.

### Q4. What is JSON validation here?
We validate JSON implicitly with `response.json()`, which raises an error if invalid.

### Q5. How would you extend this project?
- Add retries with exponential backoff.
- Add schema validation for JSON.

### Q6. Difference between `try/except` and `raise_for_status()`?
- `raise_for_status()` handles HTTP-specific errors.
- `try/except` handles broader runtime issues.

### Q7. What are real-world use cases?
Fetching API data, ETL pipelines, automated data backups.

### Q8. Why save JSON with indent=4?
To make output human-readable.

### Q9. How would you test this tool?
- Use a mock API (e.g., `httpbin.org`).
- Test with invalid URL to ensure exception handling.

### Q10. How does this lab prepare you for bigger projects?
It integrates multiple Python skills: APIs, JSON, CLI, logging, error handling → foundation for automation scripts and microservices.

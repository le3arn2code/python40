# Lab 23: Using requests for HTTP Calls

## Objectives
- Perform HTTP requests using the `requests` library in Python.
- Retrieve and interpret HTTP response status codes.
- Parse JSON data from HTTP responses.
- Build foundational knowledge of working with web APIs.

## Summary
In this lab, we used Python’s **requests** library to make HTTP calls.  
We learned how to send GET requests, check HTTP response status codes, and parse JSON responses.  
We applied this to the GitHub API, retrieving structured API data and printing specific values.  

Errors encountered included:
- **requests not installed** → Fixed with `pip install requests`.
- **Python or pip missing** → Fixed with `sudo apt install -y python3 python3-pip`.
- **Network issues** (if no internet) → Verified connectivity before retrying.  

Once these issues were resolved, all scripts executed successfully.  
This lab demonstrated the essentials of interacting with REST APIs, preparing us for more advanced data integration tasks.

## Files
- `lab23_task1.py` – Import requests library.
- `lab23_task2.py` – Perform a basic GET request and print status code.
- `lab23_task3.py` – Parse JSON response from GitHub API.
- `commands.sh` – Step-by-step commands for the lab.
- `troubleshooting.md` – Errors and resolutions.
- `interview_qna.md` – 10 HTTP/requests-related Q&A with answers.

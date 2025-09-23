# Interview Q&A - Lab 32 Logging

**Q1. What is the purpose of Python’s logging module?**  
A1. It provides a flexible way to track and record program events for debugging and monitoring.

**Q2. Name the common logging levels.**  
A2. DEBUG, INFO, WARNING, ERROR, CRITICAL.

**Q3. How do you configure logging in Python?**  
A3. With `logging.basicConfig(level=logging.DEBUG, format='...')`.

**Q4. What does %(asctime)s in log format mean?**  
A4. It represents the timestamp of the log entry.

**Q5. What happens if you call logging.basicConfig multiple times?**  
A5. Only the first call works unless the logging system is reset.

**Q6. How does logging differ from print statements?**  
A6. Logging provides severity levels, timestamps, and can be redirected to files or systems.

**Q7. What’s the difference between ERROR and CRITICAL levels?**  
A7. ERROR indicates recoverable issues, CRITICAL indicates serious failures.

**Q8. Can you log exceptions automatically?**  
A8. Yes, by using `logging.exception("message")` inside an exception handler.

**Q9. What are practical uses of logging?**  
A9. Debugging, monitoring, auditing, error tracking in production systems.

**Q10. How would you log messages to a file instead of console?**  
A10. Pass `filename='app.log'` in `logging.basicConfig`.

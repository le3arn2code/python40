# Interview Q&A – Lab 5: Conditionals

**Q1. What is the purpose of an if statement in Python?**  
A: To check a condition and execute code only if it is true.

**Q2. What does elif stand for?**  
A: "Else if". It checks additional conditions after the initial if.

**Q3. What happens if multiple elif conditions are true?**  
A: Only the first true condition is executed; the rest are skipped.

**Q4. When is the else block executed?**  
A: When none of the if or elif conditions are true.

**Q5. Can we write an if statement without else?**  
A: Yes, else is optional.

**Q6. What is an IndentationError?**  
A: It occurs when code blocks under if/elif/else are not properly indented.

**Q7. Give an example of nested if statements.**  
A:  
```python
if x > 0:
    if x % 2 == 0:
        print("Positive even")
```

**Q8. Why is elif better than multiple ifs?**  
A: Because elif ensures only one branch executes, making code more efficient.

**Q9. What is a real-world use case of conditionals?**  
A: Grading systems, login validation, or decision-making in apps.

**Q10. What type of input errors are common with conditionals?**  
A: Invalid data types (like entering text instead of numbers).

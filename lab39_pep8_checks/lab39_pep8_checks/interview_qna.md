# Lab 39 Interview Q&A

**Q1. What is PEP 8 and why is it important?**  
A: It’s the official Python style guide, ensuring readability and consistency.

**Q2. Difference between black and autopep8?**  
A: Black enforces one strict style; autopep8 is configurable and can apply aggressive fixes.

**Q3. What does flake8 do?**  
A: It checks for both errors and style violations in code.

**Q4. How do you fix PATH issues for flake8?**  
A: Add `~/.local/bin` to your PATH.

**Q5. Which tool would you recommend for team projects?**  
A: Black, since it enforces a single, consistent style.

**Q6. Can black and autopep8 conflict?**  
A: Yes, sometimes they format differently.

**Q7. What kind of issues does flake8 typically flag?**  
A: Whitespace, missing newlines, operator spacing, etc.

**Q8. Can flake8 fix issues automatically?**  
A: No, it only reports them. Use black or autopep8 to fix.

**Q9. Why integrate these tools into CI/CD pipelines?**  
A: To maintain consistent style and catch errors automatically.

**Q10. Does following PEP 8 improve performance?**  
A: No, it improves readability and maintainability, not execution speed.

# Interview Q&A for Lab 33

1. **What is web scraping?**
   Extracting structured data from web pages.

2. **Which Python libraries are commonly used?**
   `requests` for HTTP, `BeautifulSoup` for parsing.

3. **Difference between requests and urllib?**
   Requests is simpler, more user-friendly.

4. **What does BeautifulSoup do?**
   Parses HTML/XML and makes it easy to navigate DOM.

5. **What are common tags extracted?**
   Titles, headers, links, tables.

6. **What is prettify() in BeautifulSoup?**
   Outputs formatted HTML.

7. **What are potential risks of scraping?**
   Legal/ethical issues, server load.

8. **How do you handle missing attributes in tags?**
   Use `.get('attr')` with safe handling.

9. **Why use lxml parser instead of html.parser?**
   Faster and more robust.

10. **What to check before scraping a site?**
   Robots.txt and Terms of Service.

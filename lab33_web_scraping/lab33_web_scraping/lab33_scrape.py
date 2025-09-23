import requests
from bs4 import BeautifulSoup

# Fetch webpage
response = requests.get("https://example.com")
print("Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')
print("\nFormatted HTML:\n", soup.prettify()[:500])  # show first 500 chars

# Extract title
title = soup.title.string
print("\nPage Title:", title)

# Extract all hyperlinks
print("\nHyperlinks:")
for link in soup.find_all('a'):
    print(link.get('href'))

import re

text = "Hello World 123"
pattern = r"World"

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")

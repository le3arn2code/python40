import re

text = "start middle end"
pattern = r"^start"

if re.match(pattern, text):
    print("Text starts with 'start'")
else:
    print("No match")

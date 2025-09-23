import re

text = "abc123xyz456"
pattern = r"\d+"  # one or more digits

matches = re.findall(pattern, text)
print("All numbers found:", matches)

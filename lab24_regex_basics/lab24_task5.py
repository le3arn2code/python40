import re

text = "My phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"

result = re.sub(pattern, "XXX-XXX-XXXX", text)
print("Anonymized:", result)

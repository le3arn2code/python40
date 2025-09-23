import requests

# Send GET request to GitHub API
response = requests.get("https://api.github.com")

# Print status code
print("Status Code:", response.status_code)

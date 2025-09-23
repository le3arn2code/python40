import requests

# Send GET request to GitHub API
response = requests.get("https://api.github.com")

# Convert response to JSON (Python dictionary)
response_data = response.json()

print("Parsed JSON Data:")
print(response_data)

# Example: Print a specific key
if "current_user_url" in response_data:
    print("API current_user_url:", response_data["current_user_url"])

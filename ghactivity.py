
#githubendpoint = "https://api.github.com/users/{username}/events/public"
import requests
import json
token = ""


headers = {
    "accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}"
}
params = {
    "per_page": 15,
    "page": 1
}



username = input ("Enter GitHub username: ")

data = requests.get(f"https://api.github.com/users/{username}/events/public", headers=headers, params=params)
events = data.json()

print(f"Recent public events for user: {username}")
for event in events:
    event_type = event.get("type", "N/A")
    repo_name = event.get("repo", {}).get("name", "N/A")
    created_at = event.get("created_at", "N/A")
    print(f"Event Type: {event_type}, Repository: {repo_name}, Created At: {created_at}")
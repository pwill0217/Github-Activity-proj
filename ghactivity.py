


#CreateEvent
#“{username} created {ref_type} {repo_name}”
#PushEvent
#“{username} pushed commits to {repo_name}”
#WatchEvent
#“{username} starred {repo_name}”
#PullRequestEvent
#“{username} opened a pull request in {repo_name}”

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
    event_type = event.get("type")
    repo_name = event.get("repo", {}).get("name", "N/A")
    created_at = event.get("created_at", "N/A")
    if event_type == "CreateEvent":
        print(f"{username} created {repo_name}")
    elif event_type == "PushEvent":
        print (f"{username} pushed to {repo_name}")
    elif event_type == "DeleteEvent":
        print (f"{username} pushed to {repo_name}")

    

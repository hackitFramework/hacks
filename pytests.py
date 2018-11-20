import requests
r = requests.get("https://api.github.com/orgs/cornellhackingclub/members")
print(r.text)

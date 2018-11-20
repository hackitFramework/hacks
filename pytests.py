import requests
r = requests.get("https://api.github.com/orgs/cornellhackingclub/members")
r = r.json()
OrgUsers = []
for i in range(0,len(r)):
    OrgUsers.append(str(r[i]['login']))
print(OrgUsers)

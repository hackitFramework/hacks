#
# Git Grab 2018
#
# Henry Samuelson, Christopher Hansen

# Git got grabed

import os, pygithub3
#import requests
#r = requests.get("https://api.github.com/users/hsamuelson/repos")
#print(r.text)

gh = None

def gather_clone_urls(organization, no_forks=True):
    all_repos = gh.repos.list(user=organization).all()
    return all_repos

def fullSearch(userName, usrSearch):
    # First get repo list
    repoList = gather_clone_urls(userName)

    for repo in repoList:
        # Make os call to run bash script
        repo = str(repo)
        repoName = repo[repo.find("(")+1:repo.find(")")]
        individualSearch(userName, repoName, usrSearch)


def individualSearch(userName, repoName, usrSearch):
    command = "bash yomam.sh https://github.com/" + userName + "/" + repoName + " " + repoName + " " + usrSearch
    os.system(command)
def webGrab(webUrl, query):
    command = "bash httrackDump.sh " + webUrl + " " + query
    os.system(command)
#
############# MAIN PROGRAM /UI ######
#
os.system('clear')
print('')
print('  ________.__  __     ________            ___.    ')
print(' /  _____/|__|/  |_  /  _____/___________ \_ |__  ')
print('/   \  ___|  \   __\/   \  __\_  __ \__  \ | __ \ ')
print('\    \_\  \  ||  |  \    \_\  \  | \// __ \| \_\ \ ')
print(' \______  /__||__|   \______  /__|  (____  /___  /')
print('        \/                  \/           \/    \/    v.01')
print("")
print("Christopher Hansen, Henry Samuelson")
print("")
print("*")
print("Search git repos for key text")
print("*")
print("")
print("")
print("Select 0: webGrab")
print("Select 1: gitGrab")
initialSelect = raw_input("Select> ")
if(int(initialSelect) == 0):
    url = raw_input("Target url> ")
    query = raw_input("Query Text> ")
    webGrab(url, query)
if(int(initialSelect) == 1):
    print("Select 0: full search")
    print("Select 1: for individual repo search")

    menuSelect = raw_input("Select Search> ")
    selectText = raw_input("Search phrase> ")
    userName = raw_input("Target User> ")

    if(int(menuSelect) == 0):
        gh = pygithub3.Github()
        print("Results:")
        fullSearch(userName, selectText)
    else:
        repoName = raw_input("Target Repo> ")
        print("Results:")
        individualSearch(userName, repoName, selectText)

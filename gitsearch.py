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

def fullSearch(userName):
    # First get repo list 
    repoList = gather_clone_urls(userName)
    
    for repo in repoList:
        # Make os call to run bash script
        repo = str(repo)
        repoName = repo[repo.find("(")+1:repo.find(")")]
        command = "bash yomam.sh https://github.com/" +  userName + "/" + repoName
        os.system(command)


def individualSearch(userName, repoName):
    command = "bash yomam.sh https://github.com/" + userName + "/" + repoName + " " + repoName
    os.system(command)
#
############# MAIN PROGRAM /UI ######
#
print("#####  #####  #####  #####  ####   #####  #")
print("#        #      #    #      #   #  #   #  #### ")
print("#   #    #      #    #   #  ####   #####  #   #")
print("#####  #####    #    #####  #    # #   #  ####")
print("")
print("Select 0: full search")
print("Select 1: for individual repo search")

menuSelect = raw_input("Select Search> ")
userName = raw_input("Target User> ")
if(int(menuSelect) == 0):
    gh = pygithub3.Github()
    fullSearch(userName)
else:
    repoName = raw_input("Target Repo> ")
    individualSearch(userName, repoName)

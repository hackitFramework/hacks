#
# Git Grab 2018
# 
# Henry Samuelson, Christopher Hansen

# Git got grabed

import os
import requests
import pygithub3
#r = requests.get("https://api.github.com/users/hsamuelson/repos")
#print(r.text)



gh = None
def gather_clone_urls(organization, no_forks=True):
    all_repos = gh.repos.list(user=organization).all()
    for repo in all_repos:

        # Don't print the urls for repos that are forks.
        if no_forks and repo.fork:
            continue

        yield repo.clone_url


if __name__ == '__main__':
    gh = pygithub3.Github()
    username = raw_input("Target User> ")
    clone_urls = gather_clone_urls(username)
    for url in clone_urls:
        print(url)

def fullSearch(userName):
	
    # First get repo list 
    

    for repo in repoList:
        # Make os call to run bash script 
        command = "bash yomam.sh https://github.com/" + userName + "/" + repo + " " + repo
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

menuSelect = input("Select Search> ")
userName = input("Target User> ")
if(menuSelect == 0):
    fullSearch(userName)
else:
    repoName = input("Target Repo> ")
    individualSearch(userName, repoName)

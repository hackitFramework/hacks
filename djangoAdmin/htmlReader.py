#
# html reader
#
# Henry Samuelson 11/30/18

#THIS IS A TEST FILE TO AVLOID REPULLING HTML EVERY TIME WE WANT TO TEST NEW
# HTML ANALYSIS
html_doc1 = open("test.html", 'r')
html_doc = html_doc1.read()
html_doc1.close()

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
#Removes all html

print(soup.get_text("/n"))

contents = []
for line in soup.get_text().split('\n'):
    if(line != ''):
        temp = line.split()
        temp =  str(temp)[1:len(str(temp))-1]
        contents.append(temp)

fContent = []
for i in range(1, len(contents)):
    if(contents[i].isupper()):
        # Add this line and line below it.
        fContent.append(contents[i])
        fContent.append(contents[i+1])
print(fContent)
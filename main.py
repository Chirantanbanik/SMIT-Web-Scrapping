import requests
from bs4 import BeautifulSoup
url = "https://smu.edu.in/smit.html/"

# Get the HTML content
r = requests.get(url)
htmlContent = r.content

# Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

# Get the title
title = soup.title
print(title)

# Get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)

# Get all the links on the page
anchors = soup.find_all('a')
all_links = set()

# Get all the links on the page
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://smu.edu.in/smit.html/" +link.get('href')
        all_links.add(link)
        print(linkText)
        
# Comment
 

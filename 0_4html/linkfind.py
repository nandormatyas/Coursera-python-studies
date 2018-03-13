import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
url = input('Enter page: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')       # put it in BeautifulSoup
# print html                             #print html script of page
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))         # prints only links

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
count = 0
fhand = fhand.read()
for words in fhand:
    count = count+1
print(count)

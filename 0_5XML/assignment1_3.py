import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
address = input('Enter location: ')
if len(address) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_42.json'
uh = urllib.request.urlopen(address)
data = uh.read()
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
# print(lst)
# print('User count: ', len(lst))
y = list()
for item in lst:
    x = item.find('count').text
    x = int(x)
    y.append(x)
    # print(y)
print('summa', sum(y))


# print('Count', item.find('count').text)

# print('Id', item.find('id').text)
# print('Attribute', item.get("x"))

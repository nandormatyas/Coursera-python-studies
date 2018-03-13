import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) > 1:
        address = 'http://py4e-data.dr-chuck.net/comments_5977.json'
    else: 
        break
    # url = serviceurl + urllib.parse.urlencode({'address': address})
    # print('Retrieving ', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    # print(data)
    y = list()
    # print (results)
    info = json.loads(data)
    for item in info['comments']:
        x = item['count']
        y.append(x)
    print(sum(y))

    #info = json.loads(data)
    #for item in info:
    #    print ('count: ', item['count'])
    #lat = results[0].find('geometry').find('location').find('lat').text

#info = json.loads(data)

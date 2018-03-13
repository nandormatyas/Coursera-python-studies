import urllib.request, urllib.parse, urllib.error
import twurl 
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    account = input('Enter twitter account: ')
    if len(account) < 1:
        break
    url = twurl.augment(TWITTER_URL, {'screen name': account, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for x in js['users']:
        print(x['screen name'])
        s = x['status']['text']
        print(' ', s[:50])

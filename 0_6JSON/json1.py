import json
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''
info = json.loads(data)
print('user count: ', len(info))
for item in info:
    print('name', item['name'])
    print('id', item['id'])
    print('attribute', item['x'])

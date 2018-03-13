import re

name = input('Enter file: ')
if len(name) < 1: 
    name = 'mbox-short.txt'
hand = open(name)

for line in hand:
    line = line.rstrip()
    y = re.findall('^X-\S+:', line)    # y list of line start with X- 
    if len(y) > 0: 
        print(y)
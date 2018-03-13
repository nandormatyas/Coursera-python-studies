import re

name = input('Enter file: ')
if len(name) < 1: 
    name = 'mbox-short.txt'    
hand = open(name)
count = 0

for line in hand:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)         # y is a list
    if len(y) > 0: 
        count = count+1
        print(y)
print('COUNT: ', count)
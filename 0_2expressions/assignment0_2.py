import re

name = input('Enter file: ')
if len(name) < 1: 
    name = 'regex_sum_332977.txt' 
hand = open(name)
numlist = list()
count = 0
for line in hand:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)         # y is a list
    for i in y:
        count = count+1
        value = int(i)
        numlist.append(value)
        all = sum(numlist)
#    if len(y) > 0:
print(all, count)
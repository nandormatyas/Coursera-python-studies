import re

name = input('Enter file: ')
if len(name) < 1:
    name = 'mbox-short.txt'
hand = open(name)
for line in hand:
    line = line.strip()
    if re.search('^From: ', line):
        print(line)
import re

name = input('Enter file: ')
if len(name) < 1: 
    name = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'    
# hand = open(name)                            # if file opened
# hand = hand.read()                           # if file opened
# y = re.findall('@([^ ]*)',name)              # version1
y = re.findall('^From .*@([^ ]*)', name)       # version2
print(y)
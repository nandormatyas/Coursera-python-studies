# import re

name = input('Enter file: ')
if len(name) < 1: 
    name = 'mbox-short.txt'    
hand = open(name)
hand = hand.read()

atag_pos = hand.find('@')
print(atag_pos)
space_position = hand.find(' ', atag_pos)
print(space_position)
host = hand[atag_pos+1:space_position]
print(host)
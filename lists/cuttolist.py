abc='With three words'
stuff=abc.split()       #split throws away all spaces
print stuff
print 'darab: ', len(stuff)
choice= raw_input('hanyadik szo?: ')
choice=int(choice)
print stuff[choice]

# example.split(';') words divided by ';' will be split at ';'
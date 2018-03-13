import re

fname = input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    email = pieces[1]
    domain = str(email)
    x = re.findall('.*@(\S+)', domain)
    for i in x:

        i = str(i)
        y = i.strip()
        print(y)

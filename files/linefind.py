fhand=open('mbox1.txt')
for line in fhand:
    line=line.rstrip()              #delete blank lines at print
    if line.startswith('after'):
        print line
        
fhand=open('mbox1.txt')
for line in fhand:
    line=line.rstrip()
    if not 'text' in line:
        continue
    print line
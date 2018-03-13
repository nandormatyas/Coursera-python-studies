fhand=open('mbox-short.txt')
for line in fhand:
    line=line.strip()
    if not line.startswith('From '): continue
    words=line.split()
    print words[5]
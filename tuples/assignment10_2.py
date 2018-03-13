name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
words=list()
counts=dict()
fhand=open(name)
for line in fhand:
    line=line.strip()
    if not line.startswith('From '): continue
    word=line.split()
    a=word[5]
    a=a.split(':')
    b=a[0]
    words.append(b)
    #print word
    
date=words
date.sort()
#print date

for hour in date:
    counts[hour]=counts.get(hour,0)+1
lst=list()
for key, val in counts.items():
    lst.append((key,val))
lst.sort()
for key, val in lst[:10]:
    print key,val


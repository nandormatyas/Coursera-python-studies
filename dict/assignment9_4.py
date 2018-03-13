name = raw_input("Enter file:")
if len(name) < 1: 
    name = "mbox-short.txt"
handle = open(name)
count = 0
counts = dict()
add = list()

for line in handle:
    line = line.strip()
    if not line.startswith('From '):
        continue
    count = count+1
#    print line
    lst = line.split()
    mail = lst[1]
    add.append(mail)
for email in add:
    counts[email] = counts.get(email, 0)+1

bigcount = None
bigword = None
for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = email
        
print bigword, bigcount
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.strip()
    words= line.split() 
    lst.append(words)
a=lst[0]
b=lst[1]
c=lst[2]
d=lst[3]
biglist= a+b+c+d
x=list()    
for i in biglist:
    if i in x:
        continue
    else:
        x.append(i)
x.sort()
print x   

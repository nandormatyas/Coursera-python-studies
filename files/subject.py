fname=raw_input('enter file name: ')
try:                                        #if bad file input
    fhand=open(fname)
except:
    print 'file cant be opened', fname
    exit()
count=0
for line in fhand:
    if line.startswith('after'):
        count=count+1
print 'there were',count,'subjects in', fname
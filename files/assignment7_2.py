fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
add=0
    
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num=line[20:26]
    dotn=float(num)
    add=add+dotn
    count=count+1
#    add+=dotn
            
#    print count, dotn
    
    x= add/count
        
    
print "Average spam confidence:", x
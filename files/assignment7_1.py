fname = raw_input("Enter file name: ")

fh = open(fname)
for cheese in fh :
    cheese=cheese.rstrip()
    print str.upper(cheese)

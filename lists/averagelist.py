#this version of calculation average, uses memory (40mb\10M numbers)

numlist=list()
while True:
    input=raw_input('Enter number: ')
    if input=='done' :break
    value=float(input)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print 'average: ', average
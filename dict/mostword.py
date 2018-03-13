name=raw_input('Enter file .txt: ')
handle=open(name,'r')
text=handle.read()                  #this is string
words=text.split()                  #this is list

counts=dict()
for word in words:
    counts[word]=counts.get(word,0)+1
print counts

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword= word
        
print 'The most used word: ',bigword, bigcount


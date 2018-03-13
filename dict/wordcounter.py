counts=dict()
line=raw_input('TEXT? ')


words=line.split()
print 'Words: ', words

print 'Counting...'
for word in words:
    counts[word]=counts.get(word,0)+1

print 'Counts: ', counts

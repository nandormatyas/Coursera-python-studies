word= raw_input('word?')
count=0
x = raw_input('letter?')
for letter in word :
    if letter == x:
        count = count +1
print count
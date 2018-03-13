import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    domain= str(email)
    x=re.findall('.*@(\S+)', domain)
    for i in x:

        i=str(i)
        y=i.strip()
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (y,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (y,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (y,))
    #cur.execute('SELECT * FROM Counts ORDER BY count DESC LIMIT 100')
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 100'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

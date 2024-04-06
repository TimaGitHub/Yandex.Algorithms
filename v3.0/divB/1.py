from collections import Counter
from sys import stdin

con = ''
for line in stdin:
    con += line

cnt = Counter(list(''.join(con.split())))
a = []
for l in cnt:
    a.append([l, dict(cnt)[l]])
a.sort(key = lambda x:ord(x[0]))
n = max(a, key = lambda x:x[1])[1]


for i in range(n, 0, -1):
    s = ''
    for _ in a:
        if _[1] == i:
            s += "#"
            _[1] -= 1
        else:
            s += " "
    print(s)
s = ""
for _ in a:
    s += _[0]
    
print(s)
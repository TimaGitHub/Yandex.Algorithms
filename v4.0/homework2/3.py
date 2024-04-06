reader = open('input.txt', 'r')

s = reader.readline()
s = s[:-1]
n = len(s)
p = 97999108
x = 257
x_deg = [1]
dictionary = dict()
s = " " + s
for i in range(97, 123):
    dictionary[chr(i)] = i - 96

for i in range(65, 91):
    dictionary[chr(i)] = i - 38
h = [0]

for i in range(1, n + 1):
    x_deg.append( (x_deg[-1] * x) % p )
    temp = h[-1] * x + dictionary[s[i]]
    h.append(temp % p)
    
ans = [0]

for i in range(1, n):
    mid = (n - i) // 2
    low = 1
    high = n - i
    while low <= high:
        if ( h[mid] + h[i] * x_deg[mid] ) % p == ( h[i + mid]) % p   :
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
        
    ans.append(mid)  
        
print(*ans)
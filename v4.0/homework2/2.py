reader = open('input.txt', 'r')

s = reader.readline()

s = s[:-1]

n = len(s)

p = 20999101
x = 33

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
    
ans = 0

temp = h[n] % p

for k in range(0, n):
    if ( h[k] + h[n - k] * x_deg[k] ) % p ==  temp:
        ans = n - k
        
        
print(ans)
        
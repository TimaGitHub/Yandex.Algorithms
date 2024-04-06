def isequal(len_,  from1, from2):
    a = from2 - 0 #if from2 != 0 else 0
    b = from1 - 0 #if from1 != 0 else 0
    if ((h[from1 + len_ - 0] + h[a] * x_deg[len_]) % p) == ((h[from2 + len_ - 0] + h[b] * x_deg[len_]) % p):
        print('yes')
    else:
        print('no')
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

h = [0]

for i in range(1, n + 1):
    
    x_deg.append( (x_deg[-1] * x) % p )
    
    temp = h[-1] * x + dictionary[s[i]]
    h.append(temp % p)


for i in range(int(reader.readline())):
    len_,  from1, from2 = list(map(int, reader.readline().split()))
    isequal(len_,  from1, from2)
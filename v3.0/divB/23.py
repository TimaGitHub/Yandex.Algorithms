n = int(input())
calc = [float('inf')] + [0] * n

for i in range(2, n + 1):

    a = int(i / 2) if i % 2 == 0 else  0
    b = int(i / 3) if i % 3 == 0 else  0 
    c = i - 1
    calc[i] = min(calc[a], calc[b], calc[c]) + 1

oper = [n] + [1]*calc[-1] 
index = 1
print(calc[-1])
k = n
while k != 1:
    a = int(k / 2) if k % 2 == 0 else  0
    b = int(k / 3) if k % 3 == 0 else  0 
    c = k - 1

    d = min(calc[a], calc[b], calc[c])
    
    if calc[a] == d:
        oper[index] = int(k / 2)
        k = int(k / 2)
    elif calc[b] == d:
        oper[index] = int(k / 3)
        k = int(k / 3)
    else:
        oper[index] = k - 1
        k = k - 1
    index += 1 

print(*list(reversed(oper)))
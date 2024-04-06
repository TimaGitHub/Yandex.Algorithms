n = int(input())

a = [[0,1,1,1]]

for i in range(n):
    a.append([0,0,0,0])
    
for i in range(1, n + 1):
    for j in range(1, 4):
        a[i][j] = a[i - 1][3] + a[i - 1][j - 1]

print(a[n][3])   
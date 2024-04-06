n, m = list(map(int, input().split()))

x = [float('inf')] * (m + 1)
array = [x]
for i in range (1, n + 1):
    array.append([float('inf')] + list(map(int,  input().split())))
    for j in range(1, m + 1):
        if i != 1 or j != 1:
            array[i][j] = min(array[i-1][j], array[i][j-1]) + array[i][j]
                 
                 
print(array[n][m])  
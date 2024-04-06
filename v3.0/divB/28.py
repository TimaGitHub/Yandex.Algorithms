n, m = list(map(int, input().split()))


array = [[0 for k in range(m+2)] for i in range(n+2)]
array[2][2] =  1
for i in range (2, n + 2):
    for j in range(2, m + 2):
        if i != 2 or j != 2:
            array[i][j] = (array[i - 2][j - 1] + array[i - 1][j - 2]  )

            
print(array[n + 1][m + 1])
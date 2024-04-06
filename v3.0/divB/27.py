n, m = list(map(int, input().split()))

x = [-1] * (m + 1)
array = [x]
y = [0] * ( m + 1)
new_array = [y]
for i in range (1, n + 1):
    inp = list(map(int,  input().split()))
    array.append([-1] +  inp)
    new_array.append([0] + inp)
               
    for j in range(1, m + 1):
        if i != 1 or j != 1:
            array[i][j] = max(array[i-1][j], array[i][j-1]) + array[i][j]
  
i, j = n, m
ans = []

while i!= 1 or j != 1:
    current = array[i][j] - new_array[i][j]
    if array[i-1][j] == current:
        i -= 1
        ans.append('D')
    else:
        j -= 1
        ans.append('R')
                 
ans.reverse()                 
print(array[n][m]) 
print(*ans)
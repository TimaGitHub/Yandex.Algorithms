N, M, K = map(int, input().split())

matrix = [[]]

for i in range(N):            
    string = list(map(int, input().split()))
    new_string = [0]
    for i in range(M):
        new_string += [new_string[i] + string[i]]
    matrix += [new_string]
               
for i in range(K):
    summer = 0
    a = list(map(int, input().split()))
    xmin = a[0]
    while xmin <= a[2]:
        summer += (matrix[xmin][a[3]] - matrix[xmin][a[1] - 1])
        xmin += 1
    print(summer)
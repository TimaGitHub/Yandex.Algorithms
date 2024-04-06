n = int(input())

array1 = [0] + list(map(int, input().split()))

m = int(input())

array2 = [0] + list(map(int, input().split()))


main_array = [[- float('inf')] * (n + 1)]

for i in range(1, m + 1):
    main_array.append([-float('inf')] + [0] * n)
    for j in range(1, n + 1):
        if i!= 1 or j != 1:
            if array2[i] == array1[j]:
                if main_array[i-1][j-1] != - float('inf'):
                    main_array[i][j] = main_array[i-1][j-1] + 1
                else: 
                    main_array[i][j] = 1
            else:
                main_array[i][j] = max(main_array[i-1][j], main_array[i][j-1])
        else:
            main_array[1][1] = 1 if array1[1] == array2[1] else 0

i = m
j = n

ans = []

while main_array[i][j] not in (- float('inf'), 0):
    a = main_array[i][j]
    b = main_array[i-1][j]
    c = main_array[i][j-1]
    if a == b:
        i -= 1
    elif a == c:
        j -= 1
    else:
        ans.append(array1[j])
        i -= 1
        j -= 1
ans.reverse()        
print(*ans)
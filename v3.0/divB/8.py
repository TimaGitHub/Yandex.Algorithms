k = int(input())
if k > 1:
    a = list(map(int, input().split()))
    min_x = a[0]
    max_x = a[0]
    min_y = a[1]
    max_y = a[1]
    for i in range(k - 1):
        a = list(map(int, input().split()))
        if a[0] < min_x:
            min_x = a[0]
        if a[0] > max_x:
            max_x = a[0]
        if a[1] < min_y:
            min_y = a[1]
        if a[1] > max_y:
            max_y = a[1]
            
    print(min_x, min_y, max_x, max_y)
else:
    a = list(map(int, input().split()))
    print(*a, *a)
def find(i,array):
        if i != array[i]:
            array[i] = find(array[i], array)
        return array[i]
    
n, m = list(map(int, input().split()))
s =  [0] + list(map(int, input().split()))    
b = [i for i in range(n + 1)]
dest_source = []
for i in range(m):
        dest_source.append(list(map(int, input().split())))
max_task = max(s)
for i, j in dest_source:
    if (i != j) and (find(i, b) != find(j, b)):
        if s[find(i,b)] + s[find(j,b)] > max_task:
            max_task = s[find(i,b)] + s[find(j,b)]
        s[find(i,b)] = s[find(j,b)] = s[find(i,b)] + s[find(j,b)]
        b[find(j, b)] = find(i,b)
    print(max_task)
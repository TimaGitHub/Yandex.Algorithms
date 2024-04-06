import queue

file1 = open('input.txt', 'r')
n, m, s ,t ,q = list(map(int, file1.readline().split()))

ans = 0

end = {}

for i in range(q):
    a = tuple(map(int, file1.readline().split()))
    if [a[0], [1]] != [s,t]:
        try:
            end[a] += 1
        except:
            end[a] = 1
    

    
array = []

que = queue.LifoQueue()

visited = [[False] * (m+1) for j in range(n+1)]

que.put([[s,t]])

index =  0

l = 0
while not que.empty() and l != q:
    cells = que.get()
    array.append([])
    one_layer = []
    for cell in cells:
        a, b = cell[0], cell[1]
        if not visited[a][b]:
            array[index].append(cell)
            visited[a][b] = True
            
            try:
                ans += end[(a,b)] * index
                l += end[(a,b)]
            except:
                pass
            
            if a - 2 > 0 and b - 1 > 0:
                one_layer.append([a-2, b-1])
                
            if a - 2 > 0 and b + 1 < m + 1:
                one_layer.append([a-2, b+1])
                
            if a - 1 > 0 and b + 2 < m + 1:
                one_layer.append([a-1, b + 2])

            if a + 1  < n + 1 and b + 2 < m + 1:
                one_layer.append([a+1, b+2])
                                  
            if a +2 < n + 1 and b + 1 < m + 1:
                one_layer.append([a+2, b+1])
                                  
            if a + 2 < n + 1 and b - 1 > 0:
                one_layer.append([a + 2, b-1])
                                  
            if a + 1 < n + 1 and b - 2 > 0:
                one_layer.append([a+1, b-2])
                                  
            if a -1 > 0  and b - 2 > 0:
                one_layer.append([a -1, b-2])
                
    if one_layer != []:
        que.put(one_layer)
        index += 1

if l != q:
    print(-1)
else:
    print(ans)
    
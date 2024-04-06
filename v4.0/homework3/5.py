import heapq
import queue
import copy


reader = open('input.txt', 'r')

n = int(reader.readline())

info = [None]

graph = [None] * (n + 1)
 

for i in range(n):
    info.append(list(map(int, reader.readline().split())))

for i in range(n - 1):
    начало, конец, расстояние = list(map(int, reader.readline().split()))
   
    if graph[начало] == None:
        graph[начало] = [(конец, расстояние)]
    else:
        graph[начало].append((конец, расстояние))
    if graph[конец]== None:    
        graph[конец] = [(начало, расстояние)]
    else:
        graph[конец].append((начало, расстояние))
        
        
visited = [False] * (n + 1)   

que = queue.LifoQueue()

que.put([1])

array = [-1] * (n + 1)

array[1] = 0

changed = [False] * (n + 1)

while not que.empty():
    verts = que.get()
    one_layer = []
    for vert in verts:
        if not visited[vert]:
            visited[vert] = True
            kids = graph[vert]
            for kid in kids:
                if not visited[kid[0]]:
                    array[kid[0]] = array[vert] + kid[1]
                    one_layer += [kid[0]]

    if one_layer != []:
        que.put(one_layer)
        
for i in range(2, n + 1):
    array[i] = array[i] / info[i][1] + info[i][0]    


    
array = [(array[i], i) for i in range(n + 1)]

array = [array[0]] + sorted(array[1:], key = lambda x: x[0])

visited1 = [False] * (n + 1)

visited1[1] = True

for i in range(2, n):
    
    index = array[i][1]
    
    visited = copy.copy(visited1)
    
    visited1[index] = True
    
    que.put(index)
    
    temp = [float('inf')] * (n + 1)
    
    temp[index] = 0
    
    while not que.empty():
        alpha = que.get()
        kids = graph[alpha]
        one_layer = []
        
        for kid in kids:
            if not visited[kid[0]]:
                visited[kid[0]] = True
                temp[kid[0]] = temp[alpha] + kid[1]
                que.put(kid[0])

           
    for j in range(i + 1, n + 1):
        c = array[i][0] + temp[array[j][1]] / info[array[j][1]][1] + info[array[j][1]][0]
        
        if array[j][0] > c:

            array[j] = (c,  array[j][1])
            changed[array[j][1]] = array[i][1]
            k = 1
            while array[j - k][0] > array[j - k + 1][0]:
                array[j - k], array[j -k + 1] = array[j - k + 1], array[j - k]
                k += 1
    
             
ans = array[-1][0]
 
start = array[-1][1]
end = changed[start]
path = [start]
while end != False:
    path.append(end)
    end = changed[end]
            
path.append(1)
print(ans)
print(*path)      

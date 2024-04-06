import heapq

reader = open('input.txt', 'r')

n, k = list(map(int, reader.readline().split()))

graph = [None] * (n + 1)

visited = [False] * (n + 1)

dist = [float('inf')] * (n + 1)


for i in range(k):
    array = list(map(int, reader.readline().split()))
   
    if graph[array[0]] == None:
        graph[array[0]] = [(array[1], array[2])]
    else:
        graph[array[0]].append((array[1], array[2]))
        
    if graph[array[1]]== None:     
        graph[array[1]] = [(array[0], array[2])]
    else:
        graph[array[1]].append((array[0], array[2]))
        
start, end = list(map(int, reader.readline().split()))

dist[start] = 0        

dist2 = [(float('inf'), i) for i in range(n + 1)]

dist2[start] = (0, start)

heapq.heapify(dist2)

for i in range(1, n + 1):
    index = 0
    temp = []
    
    while dist2 != []:
            
        val, index = heapq.heappop(dist2)
        if not visited[index]:
            break
        else:
            temp.append((val, index))
     
    if dist[index] == float('inf'):
        break  
    
        
    visited[index] = True
    if graph[index] != None:
        for child in graph[index]: 
            if dist[child[0]] > val + child[1]:
                dist[child[0]] = val + child[1]
                heapq.heappush(dist2, (val + child[1], child[0]) )



if dist[end] == float('inf'):
    print(-1)
else:
    print(dist[end])
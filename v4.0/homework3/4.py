reader = open('input.txt', 'r')
n = int(reader.readline())
start, end = list(map(int, reader.readline().split()))

r = int(reader.readline())

graph = [None] * (n + 1)

visited = [False] * (n + 1)

dist = [float('inf')] * (n + 1)

dist[start] = 0

for i in range(r):
    
    
    начало, отбытие, конец, прибытие = list(map(int, reader.readline().split()))
   

    if graph[начало] == None:
        graph[начало] = [(отбытие, конец, прибытие)]
    else:
        graph[начало].append((отбытие, конец, прибытие))



for i in range(1, n + 1):
    min_ = 0
    for j in range(1, n + 1):
        
        if not visited[j] and dist[j] < dist[min_]:
            min_ = j
    visited[min_] = True
       
    
    if dist[min_] == float('inf'):
        break  
        
    
    if graph[min_] != None:
        for child in graph[min_]:
            отправление, конец, прибытие = child
            if dist[min_] <= отправление:
                dist[конец] = min(прибытие, dist[конец])



if dist[end] == float('inf'):
    print(-1)
else:
    print(dist[end])
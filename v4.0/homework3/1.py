reader = open('input.txt', 'r')
n, start, end = list(map(int, reader.readline().split()))


graph = [None]

visited = [False] * (n + 1)

dist = [float('inf')] * (n + 1)

dist[start] = 0

for i in range(n):
    graph.append([0] + list(map(int, reader.readline().split())))
    

for i in range(1, n + 1):
    min_ = 0
    for j in range(1, n + 1):
        if not visited[j] and dist[j] < dist[min_]:
            min_ = j
       
    
    if dist[min_] == float('inf'):
        break    
    visited[min_] = True
    
    for child in range(1, n + 1):
        
        if graph[min_][child] > 0:
            
            dist[child] = min(dist[child],  dist[min_] + graph[min_][child])
        
            
# def dijkstra(array: list, visited: list, index: int) -> None:
#     if not visited[index]:
#         for child in range(1, n + 1):
#             if array[index][child] > 0:
#                 dist[child] = min(dist[child],  dist[index] + array[index][child])
                    
#         visited[index] = True
        
#         for child in range(1, n + 1):
#             if array[index][child] > 0:
#                 dijkstra(array, visited, child)
                
# dijkstra(graph, visited, start)

if dist[end] == float('inf'):
    print(-1)
else:
    print(dist[end])
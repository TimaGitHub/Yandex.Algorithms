import queue

file1 = open('input.txt', 'r')

n = int(file1.readline())

graph = [[] for _ in range(n + 1)]

for i in range(1,n + 1):
    verts = list(map(int, file1.readline().split()))
    for j in range(n):
        if verts[j] != 0:
            graph[i].append(j + 1)
            
vert1, vert2 = list(map(int, file1.readline().split()))
file1.close()

array = [[]]

visited = [True] + [False] * n
que = queue.LifoQueue()

que.put([vert1])

index = 0
while not que.empty() and not visited[vert2]:
    verts = que.get()
    array.append([])
    one_layer = []
    for vert in verts:
        if not visited[vert]:
            visited[vert] = True
            array[index].append(vert)

            if vert == vert2:
                break
            else:
                one_layer += graph[vert]
    if (one_layer != []):
        que.put(one_layer)
        index += 1
    
if visited[vert2]:
    print(len(array) - 2)
else:
    print(-1)
import sys
from threading import stack_size

sys.setrecursionlimit(1000000)
stack_size(134217728)


def dfs(graph, visited, now, comp, prev):
    global cycle
    
    if colors[now] == 0:
        colors[now] = 1
    
    for gr in graph[now]:
        if not visited[gr]:
            if not cycle:
                if colors[now] == colors[gr] and prev != gr:
                    comp.append(now)
                    cycle = True
                    return now
                    break
                if prev == gr:
                    pass
                else:
                    dfs(graph, visited, gr, comp, now)    
    colors[now] = 2
    if cycle:
        comp.append(now)
    visited[now] = True

file1 = open('input.txt', 'r')
n = int(file1.readline())
graph = [[] for _ in range(n + 1)]
colors = [0] * (n + 1)
for i in range(1,n + 1):
    verts = list(map(int, file1.readline().split()))
    for j in range(n):
        if verts[j] != 0:
            graph[i].append(j + 1)
file1.close()

visited = [True] + [False] * (n)
cycle = False
i = 1
while not cycle:    
    if i == n + 1:
        break
    while visited[i] == True:
        i += 1
        if i == n + 1:
            break
    if i == n + 1:
        break
    comp = []
    dfs(graph, visited, i, comp, i)
    
if not cycle:
    print('NO')
else:
    print("YES")
    while comp[0] not in graph[comp[-1]]:
        comp = comp[:-1]
    print(len(comp))
    print(*comp)
import sys
from threading import stack_size

sys.setrecursionlimit(1000000)
stack_size(134217728)

def dfs(graph, visited, now, comp, color, colors):
    global Flag
    comp.append(now)
    visited[now] = True   
    if graph[now] != []:
        if colors[now] == None:
             colors[now] = color
    for gr in graph[now]:
        if color == colors[gr[0]]:
            Flag = False
        if not visited[gr[0]]:
            dfs(graph, visited, gr[0], comp, 3 - color, colors)


file1 = open('input.txt', 'r')
n, m = list(map(int, file1.readline().split()))

graph = [[] for _ in range(n + 1)]

for i in range(m):
    left, right = list(map(int, file1.readline().split()))
    
    if left == right:
        graph[left].append([right, None])
    else:
        graph[left].append([right, None])
        graph[right].append([left,None])

colors = [None] * (n + 1)
visited = [True] + [False] * (n)

Flag = True

ans = []
i = 0

while True:
    if i == n + 1:
        break
    while visited[i] == True:
        i += 1
        if i == n + 1:
            break
    if i == n + 1:
        break
    comp = []
    dfs(graph, visited, i, comp, 1, colors)
    ans.append(comp)

if Flag:
    print('YES')
else:
    print('NO')
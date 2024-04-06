import sys
from threading import stack_size

sys.setrecursionlimit(1000000)
stack_size(134217728)

def dfs(graph, visited, now, comp):
    comp.append(now)
    visited[now] = True   
    for gr in graph[now]:
        if not visited[gr]:
            dfs(graph, visited, gr, comp)


file1 = open('input.txt', 'r')
n, m = list(map(int, file1.readline().split()))

graph = [[] for _ in range(n + 1)]

for i in range(m):
    left, right = list(map(int, file1.readline().split()))

    if left == right:
        graph[left].append(right)
    else:
        graph[left].append(right)
        graph[right].append(left)


visited = [True] + [False] * (n)
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
    dfs(graph, visited, i, comp)
    ans.append(comp)


print(len(ans))
for i in ans:
    print(len(i))
    i.sort()
    print(*i)
import sys
from threading import stack_size

sys.setrecursionlimit(1000000)
stack_size(134217728)

def dfs(graph, visited, now, comp):
    global cycle
    
    if colors[now] == 0:
        colors[now] = 1
        
    
    for gr in graph[now]:
        if not visited[gr]:
            if colors[now] == colors[gr]:
                cycle = True
                break
            dfs(graph, visited, gr, comp)
            
    colors[now] = 2
    comp.append(now)
    visited[now] = True

cycle = False



file1 = open('input.txt', 'r')

n, m = list(map(int, file1.readline().split()))

colors = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    left, right = list(map(int, file1.readline().split()))
    
    if left == right:
        graph[left].append(right)
    else:
        graph[left].append(right)
file1.close()

visited = [True] + [False] * (n)

ans = []

i = 1
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
    ans += comp
 

if cycle:
    print(-1)
else:
    
    ans.reverse()
    print(*ans)
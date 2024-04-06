def dfs(graph, visited, now):
    visited[now] = True
    for gr in graph[now]:
        if not visited[gr]:
            dfs(graph, visited, gr)
   

file1 = open('input.txt', 'r')
n, m = list(map(int, file1.readline().strip().split()))
graph = [[] for _ in range(n+1)]
for i in range(m):
    line = file1.readline()
    left, right = list(map(int, line.strip().split()))
    if left == right:
        graph[left].append(right)
    else:
        graph[left].append(right)
        graph[right].append(left) 
file1.close                        

visited = [False] * (n+1)
dfs(graph, visited, 1)
ans = []
count = 0
for _ in range(1, n+1):
    if visited[_] == True:
        count += 1
        ans.append(_)

print(count)
print(*ans)
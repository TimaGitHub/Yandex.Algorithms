import queue

file1 = open('input.txt', 'r')
n = int(file1.readline().split()[0])
m = int(file1.readline())
station_map = {}
for i in range(1, n+1):
    station_map[i] = []
branches = []

for i in range(m):
    new_branch = list(map(int, file1.readline().split()))
    for br in new_branch[1:]:
        station_map[br].append(i)
    branches.append([i] + new_branch[1:])
    
a, b = list(map(int, file1.readline().split()))
file1.close()

indexA = []
indexB = []

que = queue.Queue()
put = []
for i in range(m):
    for k in range(1, len(branches[i])):
        if branches[i][k] == a:
            put.append(branches[i])
            indexA.append(i)
        elif branches[i][k] == b:
            indexB.append(i)
que.put(put)
array = [[]]    
connections = [[]]

for i in range(m):
    for br in branches[i][1:]:
        connections[i] += station_map[br]  
    a = set(connections[i])    
    connections[i] = list(a)
    connections.append([])

min_dist = float('inf')

for i in range(len(indexA)):
    indexA[i]

visited = [False] * m

visitedB = False
index = 0
while not que.empty() and not visitedB:
    one_layer = []
    branch = que.get()
    for br in branch:
        num = br[0]
        if not visited[num]: 
            visited[num] = True
            if num in indexB:
                visitedB = True
            array[index].append(num)
            for con in connections[num]:
                one_layer.append(branches[con])

    if not visitedB and (one_layer != []):
        que.put(one_layer)
        index += 1
        array.append([])
if visitedB:       
    print(index)
else: 
    print(-1)
import heapq

n, k, p = list(map(int, input().split()))

ans = 0
array = [[-1] for i in range(n+1)]

ground = set()
task = []

for i in range(1, p + 1):
    task.append(int(input()))
    if array[task[i- 1]] == [-1]:
        array[task[i - 1]] = []
    else:
        array[task[i - 1]].insert(0, i)
        
for i in range(1, n + 1):
    array[i].insert(0, p + 1)
    

ground2 = []
heapq.heapify(ground2)

for i in range(1, p + 1):
    if task[i-1] not in ground:
        ans += 1
        if len(ground) == k:
            ground.remove(heapq.heappop(ground2)[1])
        ground.add(task[i-1])
           
    heapq.heappush(ground2, [-array[task[i-1]].pop(), task[i-1]])
    
print(ans)
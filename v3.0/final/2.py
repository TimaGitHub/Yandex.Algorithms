import heapq
f = open('input.txt', 'r')

n, w  = list(map(int, f.readline().split()))
dic = {}

for i in range(1, n + 1):
    dic[i] = []

tasks = []
    
heap1 = [[0, i] for i in range(1, n + 1)]
heap2 = []
    
for i in range(1, n + 1):
    tasks.append(list(map(int, f.readline().split())) + [i] )
    
heapq.heapify(tasks)

for i in range(1, n + 1):
    a, b, c = heapq.heappop(tasks)
    while heap1 != [] and heap1[0][0] <= a:
        heapq.heappush(heap2, heapq.heappop(heap1)[1])
    l = heapq.heappop(heap2)
    dic[l].append(c)
    heapq.heappush(heap1, [a + b, l])
    
count = 0
ans = []
for i in range(1, n + 1):
    if dic[i] != []:
        ans += dic[i]
        count += 1
    
print(count)
print(*ans)
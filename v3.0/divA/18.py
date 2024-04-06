import heapq 

f = open('input.txt', 'r') 

k, n = list(map(int, f.readline().split()))

stations = [[-1,k] for k in range(1, k + 1)]

heapq.heapify(stations)
ans = []

okes = []
heapq.heapify(okes)

dim = 0

for i in range(n):
    time_in, time_out = list(map(int, f.readline().split()))
    if len(okes) == 0:
        next_st = heapq.heappop(stations)
        heapq.heappush(okes, next_st[1])
        if time_in <= next_st[0]:
            ans = [0, i + 1]
            break
    else:
        next_st = okes[0]
    
    while len(stations) != 0 and stations[0][0] < time_in:
        heapq.heappush(okes, heapq.heappop(stations)[1])

    el = heapq.heappop(okes)
    ans.append(el)
    dim += 1
    heapq.heappush(stations, [time_out, el])

if ans[0] == 0:
    print(*ans)
else:
    for i in range(dim):
        print(ans[i])
import heapq

file1 = open('input.txt', 'r')
n = int(file1.readline())

elements = list(map(int, file1.readline().split()))

temp_list = []

ans = 0

heapq.heapify(elements)
while n != 1:
    a = heapq.heappop(elements)
    b = heapq.heappop(elements)
    res = (a + b)
    ans += res * 0.05
    heapq.heappush(elements, res)
    n -= 1
print('{:0.2f}'.format(ans))
    
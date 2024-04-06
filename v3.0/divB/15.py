stack = []



N = int(input())

ans = [-1] * N

cities = list(map(int, input().split()))

for i in range(N):
    if len(stack) == 0:
        stack.append([cities[i] , i])
    else:
        while len(stack) != 0 and stack[-1][0] > cities[i]:
            a = stack.pop()
            ans[a[1]] = i
        stack.append([cities[i], i])
print(*ans)   
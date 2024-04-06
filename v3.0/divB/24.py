n = int(input())

array = [[float('inf'), float('inf'), float('inf')], [float('inf'), float('inf'), float('inf')], [float('inf'), float('inf'), float('inf')]]

dp = [0] * (n + 3)

for i in range(n):
    array += [list(map(int, input().split()))]
    dp[i + 3] = min(dp[i+2] + array[i+3][0], dp[i+1] + array[i+2][1], dp[i] + array[i+1][2])
    
print(dp[-1])
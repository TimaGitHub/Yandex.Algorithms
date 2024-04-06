n, k = list(map(int, input().split()))

dp = [0] * (n + k)
dp[k] = 1
for i in range(k + 1, n + k):
    dp[i] = sum(dp[i - k:i])
    
    
print(dp[-1])
n = int(input())

count = int(n**(1/3) // 1 + 1) 

cubes = [0] * (count + 1)

dp = [0] * (n + 1) 

dp[1] = 1

for i in range(1, count +  1):
    b = i ** 3
    cubes[i] = b
    if i != count:
        dp[b] = 1
 
if n in cubes:
    print(1)
else:
    for i in range(2, n + 1):
        a = float('inf')
        if dp[i] == 0:
            index = 1
            while index <= count and cubes[index] < i:
                b = i - cubes[index]
                if a > dp[b]:  
                    a = dp[b]
                index += 1
            dp[i] = a + 1

    print(dp[n])
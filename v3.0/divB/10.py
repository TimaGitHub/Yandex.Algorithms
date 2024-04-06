s = input()
n = len(s)
ans = dict()
index = 1
for _ in range(97,123):
    ans[chr(_)] = 0
    
for sym in s:
    ans[sym] += ((n + 1 - index) * index)
    index += 1
  
for _ in ans:
    if ans[_] != 0:
        print('{}: {}'.format(_, ans[_]))
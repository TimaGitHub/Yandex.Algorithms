n, *hist = list(map(int, input().split()))

min_right = [n] * n
min_left = [-1] * n
stack = []
steck = []

for i in range(n):
    if i == 0:
        stack.append([hist[i], i])
    else:
        while len(stack) != 0 and stack[-1][0] > hist[i]:
            a = stack.pop()
            min_right[a[1]] = i
        stack.append([hist[i], i])
    
    index = n - i - 1
    if index == n - 1:
        steck.append([hist[index], index])
    else:
        while len(steck) != 0 and steck[-1][0] > hist[index]:
            a = steck.pop()
            min_left[a[1]] = index
        steck.append([hist[index], index])
    
    
    
s = 0

for i in range(n):
    left = min_left[i]
    right = min_right[i]
    dist = right - left - 1
    if s < hist[i] * dist:
        s = hist[i] * dist
        
print(s)
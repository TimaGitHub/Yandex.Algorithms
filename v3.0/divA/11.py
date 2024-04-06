n = int(input())
for i in range(n):
    stack = []
    k, *convA = list(map(float, input().split()))
    convB = []
    stack.append(convA[0])
    
    for j in range(1, int(k)):
        while stack != [] and stack[-1] < convA[j]:
            convB.append(stack.pop())
            
        stack.append(convA[j])
    while stack:
        convB.append(stack.pop())
        
    flag = True
    minB = convB[0]
    
    for l in range(1, int(k)):
        if minB <= convB[l]:
            minB = convB[l]
        else:
            flag = False
            break
            
            
    if flag:
        print(1)
    else:
        print(0)
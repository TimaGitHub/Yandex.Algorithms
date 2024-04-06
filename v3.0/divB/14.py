n = input()
s = list(map(int, input().split()))
stack = []
number = 1
flag = True
while len(s) != 0:
    el = s.pop(0)
    if el == number:
        number += 1
    else:
        while stack != [] and stack[-1] == number:
            a = stack.pop()
            number += 1
        stack.append(el)
    
for i in range(number, int(n) + 1):
    if stack != [] and stack.pop() != i:
        print('NO')
        flag = False
        break
if flag:
    print('YES')
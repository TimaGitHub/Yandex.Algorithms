from collections import deque
left_que = deque()
right_que = deque()
a = b = 0
file1 = open('input.txt', 'r')
n = int(file1.readline())
for i in range(1, n + 1):
    task = file1.readline().split()
    if task[0] == '+':
        while b >= a and b != 0:
            left_que.append(right_que.popleft())
            a += 1
            b -= 1
        if a == 0:
            left_que.append(task[1])
            a+= 1
        else:
            right_que.append(task[1])
            b += 1
    elif task[0] == '*':
        left_que.append(task[1])
        a += 1
        while a - b > 1:
            right_que.appendleft(left_que.pop())
            b += 1
            a -= 1
        
    elif task[0] =='-':
        print(left_que.popleft())
        if b != 0 and a -b != 1:
            left_que.append(right_que.popleft())
            b -= 1
        else:
            a -= 1
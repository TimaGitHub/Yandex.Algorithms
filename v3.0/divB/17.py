queue1 = []
queue2 = []

queue1 += map(int, input().split())
queue2 += map(int, input().split())

count = 0

flag = True

while len(queue1) != 0 and len(queue2) != 0:
    a = queue1.pop(0)
    b = queue2.pop(0)
    if (a != 0 or b != 9) and (b != 0 or a != 9):
        if a > b:
            queue1 += [a, b]
        else:
            queue2 += [a, b]
    else:
        if a == 0:
            queue1 += [a, b]
        else:
            queue2 += [a, b]
            
            
            
    count += 1
    if count > 1000000:
        print('botva')
        flag = False
        break
 
if flag:
    ans = 'first' if len(queue2) == 0 else 'second'
    print(ans, count)
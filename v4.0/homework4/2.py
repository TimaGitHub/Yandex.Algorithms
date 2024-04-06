n = int(input())
ans = 0

def rec(not_x, not_y, count, x):
    global ans
    if count != 0:
        for y in range(n):
            flag = True
            for index in range(len(not_y)):
                
                if y == not_y[index] or abs(y - not_y[index]) == abs(x - not_x[index]):
                    flag = False
                    break
                    
            if flag:
                rec(not_x + [x], not_y + [y], count - 1, x + 1)
    else:
        ans += 1
        
        
rec([], [], n, 0)

print(ans)
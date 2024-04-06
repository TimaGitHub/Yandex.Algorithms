s = input().split()
el = []
ans = 0
for _ in s:
    if _ not in ('*', '/', '+', '-'):
        el.append(int(_))
    else:
        b = el.pop()
        a = el.pop()
        if _ == '-':
            el.append(a-b)
        elif _ == '+':
            el.append(a+b)
        elif _ == '*':
            el.append(a*b)
        else:
            el.append(a / b)
            
print(sum(el))
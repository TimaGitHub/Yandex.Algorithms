n = int(input())
a = 0
b = 0
pos = ''
check = ''

def rec():
    if n % 2 == 1:
        print()
        return
    global pos, a, b, check
    if len(pos) == n:
        print(pos)
        return
    if a + b< n/2 and len(pos) != n-1:
        pos += '('
        a += 1
        check += '('
        rec()
        check = check[:-1]
        a -=1
        pos = pos[:-1]
    if a + b < n/2 and len(pos) != n-1:
        pos += '['
        b +=1
        check += '['
        rec()
        check = check[:-1]
        b -=1
        pos = pos[:-1]
    if  check and check[-1] != '[' :
        pos += ')'
        check = check[:-1]
        rec()
        check += '('
        pos = pos[:-1]
    if check and check[-1] != '(' :
        pos += ']'
        check = check[:-1]
        rec()
        check += '['
        pos = pos[:-1]
rec()
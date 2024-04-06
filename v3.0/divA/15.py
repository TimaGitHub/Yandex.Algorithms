s = input()
stack = []

n = len(s)


def correct(s):
    stack = []
    
    a = s.count('<')
    b = s.count('>')
    c = s.count('/')
    if a % 2 != 0 or a == 0:
        return False
    if b % 2 != 0 or b == 0:
        
        return False
    if (a + b) / 4 != c:
        
        return False
    if a != b:
        return False
    n = len(s)
    
    if s[0] != '<':
        return False
    
    tag = ' '
    for i in range(n):
        if  s[i] == '<':
            tag = '<'
        else:
            if tag[0] == '<' and s[i] != '>':
                tag += s[i]
        if s[i] == '>':
            if tag.count('/') == 0:
                stack.append(tag[1:])
            else:
                if stack == []:
                    return False
                else:
                    a = stack.pop()
                    if a != tag[2:]:
                        return False
        
        
    if stack != []:
        return False
                    

    return True
    
    
flag = True
alphabet = 'abcdefghijklmnopqrstuvwxyz<>/'

for sym in alphabet:
    if flag:
        for j in range(n):
            new_s = s[:j] + sym + s[j+1:]
            if correct(new_s):
                flag = False
                break
if not flag:                    
    print(new_s)

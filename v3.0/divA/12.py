stack = []
flag = True
priority = {"*" : 2, "+" : 1, "-" : 1 }
s = input()
string = []
index = 0
for _ in s:
    if _ in ('0','1','2','3','4','5','6','7','8','9'):
        try:
            int(s[index-1])
            string[-1] += _
        except:
            string += _
    else:
        if _ == '(':
            stack.append(_)
        elif _ == ' ':
            pass
        elif _ == ")":
            while len(stack) > 1 and stack[-1] != '(':
                string += stack.pop()
            if stack.pop() !='(':
                print('WRONG')
                flag = False
                break
        elif _ in ("*", "+" ,"-"):
            
            try:
                while stack[-1] != '(' and  priority[_] <= priority[stack[-1]]:
                    string += stack.pop()
            except:
                pass
            stack.append(_)
        else:
            print('WRONG')
            flag = False
            break
    index += 1
if flag:     
    if (len(stack) + len(string)) % 2 == 1:
        while stack:
            string += stack.pop()
        el = []
        for _ in string:
            if _ not in ('*', '+', '-'):
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
        
    else:
        print('WRONG')
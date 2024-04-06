           
def bracket_test(s):
    bracket_stack = []
    for i in s:
        if i in ['[', '(', '{']:
            bracket_stack.append(i)
        else:
            if i in [']', ')', '}']:
                if bracket_stack == []:
                    return 'no'
                last = bracket_stack.pop()
                if (last == '[' and i != ']') or (last == '(' and i != ')') or (last == '{' and i != '}'):
                    return 'no'
    if bracket_stack != []:
            return 'no'
    return 'yes'
    
    
print(bracket_test(input()))
class Steck():
    def __init__(self, S):  
        self.array = S
        self.top = -1
        self.len = len(S)
    def stack_empty(self):
       
        if self.top == -1:
            return True
        else: 
            return False  
    def show(self):
        print(self.array)
       
    def push(self, x):
        try: 
            self.array[self.top + 1] = x
            self.top += 1
        except:
            return "Array is full"
    def pop(self):
        if self.top == -1:
            return 
        else: 
            self.top -= 1
            return self.array.pop(self.top + 1)
           
def bracket_test(s):
    bracket_stack = Steck([0]*len(s))
    count = 0
    new_list = []
    for i in s:
        count += 1
        if i in ['[', '(', '{']:
            bracket_stack.push(i)
            new_list.append(count)
        else:
            if i in [']', ')', '}']:
                if bracket_stack.stack_empty():
                    return count
                last = bracket_stack.pop()
                if (last == '[' and i != ']') or (last == '(' and i != ')') or (last == '{' and i != '}'):
                    return count
                else:
                    a = new_list.pop()
    if not bracket_stack.stack_empty():
            return new_list.pop()
    return 'Success'
    
    
print(bracket_test(input()))
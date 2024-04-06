class Steck():
   def __init__(self):
       self.top = -1
       self.new_array = []
   def push(self, x):
       self.top += 1
       if self.top == 0:
           self.new_array.append(x)
       else: 
           self.new_array.append(max(self.new_array[-1], x))
   def pop(self):
       self.top -= 1
       self.new_array.pop(self.top + 1)
       
   def new_max(self):
       print(self.new_array[-1])
       
new_stack = Steck()
for _ in range(int(input())):
    command, *number = input().strip().split()
    if command == 'push':
        num = int(number[0])
        new_stack.push(num)
    if command == 'pop':
        new_stack.pop()
    if command == 'max':
        new_stack.new_max()

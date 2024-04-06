class Steck():
    
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.array = []
        self.new_array = []
    def push(self, x):
        self.top += 1
        self.array.append(x)
        if self.top == 0:
            self.new_array.append(x)
        else: 
            self.new_array.append(max(self.new_array[-1], x))
    def full(self):
        if self.top == self.size - 1:
            return True
        else: 
            return False
    def empty(self):
        if self.top == -1:
            return True
        else: return False
    def pop(self):
        self.top -= 1
        a = self.new_array.pop(self.top + 1)
        return self.array.pop(self.top + 1)
        
    def new_max(self):
        if self.top == -1:
            return 0
        else: 
            return self.new_array[-1]
       
n = int(input())
new_list = list(map(int, input().split()))
m = int(input())

list_maxima = []

input_steck = Steck(m)
output_steck = Steck(m)
if n == m:
    print(max(new_list))
else:
    while len(new_list) != 0:

        if (not input_steck.full()) and (output_steck.empty()):
            input_steck.push(new_list.pop(0))
        elif (input_steck.full()) and (output_steck.empty()): 
            while not input_steck.empty():
                output_steck.push(input_steck.pop())
            list_maxima.append(output_steck.new_max())
        while (not input_steck.full()) and (not output_steck.empty()) and (len(new_list) != 0):  
            input_steck.push(new_list.pop(0))
            a = output_steck.pop()
            list_maxima.append(max(input_steck.new_max(), output_steck.new_max()))
        if (len(list_maxima)*len(new_list)) != 0:
            a = list_maxima.pop()
    print(*list_maxima)

class d_aryHeap():  # d-ичная куча, c.138 Кормен
    
    def __init__(self, d, array, m):
        self.d = d
        self.m = m
        self.items = array
      
    def size(self): 
        return len(self.items)
        
    def parent(self, index):
        if index in (1,0):
            return 0
        else: 
            return index // self.d if index % self.d != 0 else index // self.d - 1 
    
    def child(self, index, position):  # position starts with 0
        return index * self.d + (position + 1)
    
    def heapify(self, index):
        list_of_children = [self.child(index, position) for position in range(self.d)] 
        least = index
        if self.size() != 1:
            for child in list_of_children:
                if (child < self.size()) and (self.items[child][1] < self.items[least][1]):
                        least = child
            if least != index:
                self.items[least] , self.items[index]  = self.items[index], self.items[least]
                self.heapify(least)
    
    def buildheap(self):
        for i in range(self.size()//2 + 2, -1, -1):
            self.heapify(i)
            
    def extract_min(self):
        minima = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()    
        self.heapify(0)
        return minima
        
    def heap_insert(self, key):
        new_index = self.size()
        self.items.append([])
        if self.size() not in (1,0) :
            while self.items[self.parent(new_index)][1] > key[1] and new_index > 0:
                self.items[new_index] = self.items[self.parent(new_index)]
                new_index = self.parent(new_index)
        self.items[new_index] = key
 

n, m = input().split()

heap_tasks = d_aryHeap(2, [[i, 0] for i in range(int(n))] , int(n))
heap_tasks.buildheap()
new_list = []
for task in map(int, input().split()):
    one_process = heap_tasks.extract_min()
    heap_tasks.heap_insert([one_process[0],one_process[1] + task])
    new_list.append([one_process[0],one_process[1]])

for _ in new_list:
    print(*_, end = '\n')

class d_aryHeap(): #d-ичная куча, c.138 Кормен
    
    def __init__(self, d, array):
        self.d = d
        self.items = array
        
    def size(self): 
        return len(self.items)
    
        
    def parent(self, index):
        parent_index = index // self.d if index % self.d != 0 else index // self.d - 1
        return parent_index
    
    def child(self, index, position): #position starts with 0
        return index * self.d + (position + 1)
    
    def heapify(self, index):
        
        list_of_children = [self.child(index, position) for position in range(self.d)]   
        largest = index
        
        for child in list_of_children:
            
            if child < self.size():
                
                if self.items[child] > self.items[largest]:
                    largest = child
                    
        if largest != index:
            self.items[largest] , self.items[index]  = self.items[index], self.items[largest] 
            self.heapify(largest)
    
    def extract_max(self):
        max_ = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()    
        self.heapify(0)
        return max_
        
    def heap_insert(self, key):
        new_index = self.size()
        self.items.append(-1)
        
        while self.items[self.parent(new_index)] < key and new_index > 0: #Или больше 1, не помню
            self.items[new_index] = self.items[self.parent(new_index)]
            new_index = self.parent(new_index)
            
        self.items[new_index] = key
        
new_heap = d_aryHeap(2, [])       
        
for i in range(int(input())):

    task = input().split()
    if task[0] == '1':
        print(new_heap.extract_max())
    else:
        new_heap.heap_insert(int(task[1]))
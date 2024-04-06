class d_aryHeap(): #d-ичная куча, c.138 Кормен
    
    def __init__(self, d, array):
        self.d = d
        self.items = array
        
    def size(self): 
        return len(self.items)
    
    def heap_delete(self, index):
        self.items.pop(index)
        self.buildheap()
        
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
    
    def buildheap(self):
        for i in range(self.size()//2 + 2, -1, -1):
            self.heapify(i)
    
    def heapsort(self):
        new_list = []
        self.buildheap()
        while self.size() > 0:
            new_list.append(self.items[0])
            self.items[0] = self.items[-1] 
            self.items.pop()
            self.heapify(0)
        
        return new_list
        
n = input()
s = list(map(int, input().split()))
new_heap = d_aryHeap(2, s)


print(*new_heap.heapsort()[::-1])
        
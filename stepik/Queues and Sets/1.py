class d_aryHeap(): #d-ичная куча, c.138 Кормен
    
    def __init__(self, d,  array):
        self.d = d
        self.items = array
        self.m = 0
        self.share_list = []
      
    def size(self): 
        return len(self.items)
    
    def delete_last_element(self):
        self.items.pop(-1)
    
    def heap_delete(self, index):
        self.items.pop(index)
        self.buildheap()
        
    def parent(self, index):
        if index == 1 or index == 0:
            return 0
        else: 
            parent_index = index // self.d if index % self.d != 0 else index // self.d - 1
            return parent_index
    
    def child(self, index, position): #position starts with 0
        return index * self.d + (position + 1)
    
    def heapify(self, index):
        
        list_of_children = [self.child(index, position) for position in range(self.d)] 
        
        least = index
        if self.size() != 1:
        
            for child in list_of_children:

                if child < self.size():

                    if self.items[child] < self.items[least]:
                        least = child

            if least != index:
                self.share_list.append([least,index])
                self.m += 1
                self.items[least] , self.items[index]  = self.items[index], self.items[least]
                self.heapify(least)
    
    def buildheap(self):
        for i in range(self.size()//2 + 2, -1, -1):
            self.heapify(i)
    
    def extract_min(self):
        
        if self.size() == 0:
            print('Sorry, the q-queue is empty')
        else:
            self.buildheap()
            min = self.items[0]
            self.items[0] = self.items[-1]
            self.delete_last_element()    
            self.heapify(0)
            return min[0] , min[1]
        
    def heap_insert(self, key):
        
        new_index = self.size()
        
        self.items.append([])
        
        while self.items[self.parent(new_index)][1] > key[1] and new_index > 0:
            self.items[new_index] = self.items[self.parent(new_index)]
            new_index = self.parent(new_index)
        self.items[new_index] = key

n = int(input())
new_heap = d_aryHeap(2, list(map(int, input().split())))
new_heap.buildheap()

print(new_heap.m)
for _ in new_heap.share_list:
    print(_[0], _[1] , end = '\n')

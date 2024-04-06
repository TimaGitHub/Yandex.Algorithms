class Binary_Search_Tree():  # код взят здесь https://blog.boot.dev/computer-science/binary-search-tree-in-python/#using-the-bst
    
    number_of_nodes = 0
    root = None
    
    def __init__(self, value = None):
        
        Binary_Search_Tree.number_of_nodes += 1
        if Binary_Search_Tree.number_of_nodes == 1:
            Binary_Search_Tree.root = self
            
        self.val = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
    
    def find(self, val):
        if self.val != None:
            if val == self.val:
                return self
            if val < self.val:
                if self.left == None:
                    return False
                return self.left.find(val)

            if self.right == None:
                return False
            return self.right.find(val)
        else:
            return False
    
    def insert(self, val):
        if not self.val:
            self.val = val
            return 
        if self.val == val:
            return
        
        if self.val > val:
            if self.left:
                self.left.insert(val)
                return
            element = Binary_Search_Tree(val)
            self.left = element
            if self.left != None and self.right != None:
                self.height = 1 + max(self.left.height, self.right.height)
            if self.left != None and self.right == None:
                self.height = 1 + self.left.height
            if self.left == None and self.right != None:
                self.height = 1 + self.right.height
            element.parent = self
            self.rotation(self)
            
            
        
        if self.val < val:
            if self.right:
                self.right.insert(val)
                return
            element = Binary_Search_Tree(val)
            self.right = element
            if self.left != None and self.right != None:
                self.height = 1 + max(self.left.height, self.right.height)
            if self.left != None and self.right == None:
                self.height = 1 + self.left.height
            if self.left == None and self.right != None:
                self.height = 1 + self.right.height
            element.parent = self
            self.rotation(self)
    
    def rotation(self, subroot):
        if subroot.left != None and subroot.right != None:
            if abs(subroot.left.height - subroot.right.height) > 1:

                if (subroot.left.height - subroot.right.height == -2):
                    if subroot.right.left != None and subroot.right.right != None:
                        if subroot.right.left.height == subroot.right.right.height:
                            
                       
                            parent = subroot.parent  
                            if parent != None:
                                child = subroot.right.left
                                height = subroot.height
                                if parent.left == subroot:
                                    parent.left = subroot.right
                                    parent.left.height = height
                                    subroot.parent = parent.left
                                    parent.left.left = subroot
                                else:
                                    parent.right = subroot.right
                                    parent.right.height = height
                                    subroot.parent = parent.right
                                    parent.right.left = subroot


                                subroot.height = height - 1
                                subroot.right = child

                                self.rotation(parent)
                            
                        if subroot.right.left.height - subroot.right.right.height == -1:
                        
                            parent = subroot.parent  
                            if parent != None:
                                child = subroot.right.left
                                height = subroot.height
                                if parent.left == subroot:
                                    parent.left = subroot.right
                                    parent.left.height = height - 1
                                    subroot.parent = parent.left
                                    parent.left.left = subroot
                                else:
                                    parent.right = subroot.right
                                    parent.right.height = height - 1
                                    subroot.parent = parent.right
                                    parent.right.left = subroot


                                subroot.height = height - 2
                                subroot.right = child

                                self.rotation(parent)
                            
                            
                        if subroot.right.left.height - subroot.right.right.height == 1:
                            parent = subroot.parent
                            if parent != None:
                                child1 = subroot.right.left.left
                                child2 = subroot.right.left.right
                                height = subroot.height
                                c = subroot.right.left
                                b = subroot.right

                                if parent.left == subroot:
                                    parent.left = c
                                    parent.left.height = height - 1

                                    subroot.parent = parent.left
                                    subroot.right.parent = parent.left
                                    parent.left.left = subroot
                                    parent.left.left.height = height - 2

                                    parent.left.right = b
                                    parent.left.right.height = height -2

                                    parent.left.left.right = child1
                                    child1.parent = parent.left.left

                                    parent.left.right.left = child2
                                    child2.parent = parent.left.right



                                else:
                                    parent.right = c
                                    parent.right.height = height - 1

                                    subroot.parent = parent.right
                                    subroot.right.parent = parent.right
                                    parent.right.left = subroot
                                    parent.right.left.height = height - 2

                                    parent.right.right = b
                                    parent.right.right.height = height -2

                                    parent.right.left.right = child1
                                    child1.parent = parent.right.left

                                    parent.right.right.left = child2
                                    child2.parent = parent.right.right



                                self.rotation(parent)
                            
                            
                            
                            
                elif (subroot.left.height - subroot.right.height == 2):
                    
                    if subroot.right.left != None and subroot.right.right != None:
                        
                        if subroot.right.left.height == subroot.right.right.height:
                        
                            parent = subroot.parent   
                            if parent != None:
                                child = subroot.left.right
                                height = subroot.height
                                if parent.left == subroot:
                                    parent.left = subroot.left
                                    parent.left.height = height
                                    subroot.parent = parent.left
                                    parent.left.left = subroot
                                else:
                                    parent.right = subroot.left
                                    parent.right.height = height
                                    subroot.parent = parent.right
                                    parent.right.left = subroot


                                subroot.height = height - 1
                                subroot.left = child

                                self.rotation(parent)
                        
                        if subroot.right.left.height - subroot.right.right.height == -1:
                    
                            parent = subroot.parent   
                            if parent != None:
                                child = subroot.left.right
                                height = subroot.height
                                if parent.left == subroot:
                                    parent.left = subroot.left
                                    parent.left.height = height -1 
                                    subroot.parent = parent.left
                                    parent.left.left = subroot
                                else:
                                    parent.right = subroot.left
                                    parent.right.height = height - 1
                                    subroot.parent = parent.right
                                    parent.right.left = subroot


                                subroot.height = height - 2
                                subroot.left = child
                            
                                self.rotation(parent)
                            
                            
                        if subroot.right.left.height - subroot.right.right.height == 1:
                            parent = subroot.parent
                            if parent != None:
                                child1 = subroot.left.right.left
                                child2 = subroot.left.right.right
                                height = subroot.height
                                c = subroot.left.right
                                b = subroot.left

                                if parent.left == subroot:
                                    parent.left = c
                                    parent.left.height = height - 1

                                    subroot.parent = parent.left
                                    subroot.left.parent = parent.left
                                    parent.left.right = subroot
                                    parent.left.right.height = height - 2

                                    parent.left.left = b
                                    parent.left.left.height = height -2

                                    parent.left.right.left = child2
                                    child1.parent = parent.left.right

                                    parent.left.left.right = child1
                                    child2.parent = parent.left.left



                                else:
                                    parent.right = c
                                    parent.right.height = height - 1

                                    subroot.parent = parent.left
                                    subroot.right.parent = parent.right
                                    parent.right.right = subroot
                                    parent.right.right.height = height - 2

                                    parent.right.left = b
                                    parent.right.left.height = height -2

                                    parent.right.right.left = child1
                                    child1.parent = parent.right.right

                                    parent.right.left.right = child2
                                    child2.parent = parent.right.left



                                self.rotation(parent)
                    
                    
    
    def get_min(self):
        current = self
        while current.left != None:
            current = current.left
        return current
    
    
    def get_max(self):
        current = self
        while current.right != None:
            current = current.right
        return current
    
    
    def delete(self, val, side):
        if self == None or self.val == None:
            return
        
        elif val < self.val:
            self.left.delete(val,"left")
        
        elif val > self.val and self.right:
            self.right.delete(val,"right")
        
        elif val == self.val:
            if side != None:
                
                if (self.left == None and self.right == None):
                    if side == "right":
                        self.parent.right = None
                        self.parent.height = self.parent.height - 1
                    else:
                        self.parent.left = None
                        self.parent.height = self.parent.height - 1
                    
                elif (self.left == None and self.right != None):
                    if side == "right":
                        self.parent.right = self.right
                        self.right.parent = self.parent
                        self.parent.height = self.right.height + 1
                    else: 
                        self.parent.left = self.right
                        self.right.parent = self.parent
                        self.parent.height = self.right.height + 1
                    
                elif (self.left != None and self.right == None):
                    if side == "right":
                        self.parent.right = self.left
                        self.left.parent = self.parent
                        self.parent.height = self.left.height+ 1
                    else:
                        self.parent.left = self.left
                        self.left.parent = self.parent
                        self.parent.height = self.left.height+ 1
                    
                else:
                    min_node = self.right
                    while min_node.left:
                        min_node = min_node.left
                    
                    self.val = min_node.val
                    min_node.parent.left = min_node.right
                    if min_node.right:
                        min_node.parent.height = min_node.right.height + 1
                    else:
                        min_node.parent.height = 0
                        
                if self:
                    self.rotation(self)
                    
            else:
                
                if (self.left == None and self.right == None):
                    self.val = None
                    self = None
                    
                elif (self.left == None and self.right != None):
                    if side == "right":
                        self.parent.right = self.right
                        #self.right.parent = self.parent
                        self.parent.height = self.right.height + 1
                    else:
                        self.parent.left = self.right
                        #self.right.parent = self.parent
                        self.parent.height = self.right.height + 1
                    
                elif (self.left != None and self.right == None):
                    if side == "right":
                        self.parent.right = self.left
                        #self.left.parent = self.parent
                        self.parent.height = self.left.height+ 1
                    else:
                        self.parent.left = self.left
                        #self.left.parent = self.parent
                        self.parent.height = self.left.height+ 1
                        
                    
                else:
                    min_node = self.right
                    
                    while min_node.left:
                        min_node = min_node.left
                    
                    self.val = min_node.val
                    min_node.parent.left = min_node.right
                    if min_node.right:
                        min_node.parent.height = min_node.right.height + 1
                    else:
                        min_node.parent.height = 0
                
        
    
    def next_el(self, val):
        
        if val == Binary_Search_Tree.root.get_max().val:
         
            return 
        
        element = self.find(val)
        
        if element.right:
            return element.right.get_min()
        
        y = element.parent
        while y != None and self == y.right:
            self = y
            y = y.parent
            
        return y
            
            
    def summer(self, val1 ,val2):
        if val1 <= val2:
        
            new = Binary_Search_Tree.root.get_min()
            while new != None  and new.val != None and new.val < val1:
                new = new.next_el(new.val)
            if new != None and new.val != None:
                ans = 0

                while new != None and new.val != None and new.val <= val2:

                        ans += new.val
                        new = new.next_el(new.val)

                return ans
            else: return 0
        else:
            return 0
    
bst = Binary_Search_Tree()

summs = 0

def func(x, summs):
    return (x + summs) % 1000000001
n = int(input())

for i in range(n):
    request = input().split(" ")
    
    if request[0] == "+":
        bst.insert(func(int(request[1]), summs))
    elif request[0] == "-":
        a = bst.delete(func(int(request[1]), summs), None)
    elif request[0] == "?":
        if bst.find( func(int(request[1]), summs) ) :
                    print("Found")
        else:
                    print("Not found")
                
    elif request[0] == "s":
        summs = bst.summer(func(int(request[1]), summs) , func(int(request[2]), summs))
        print(summs)  
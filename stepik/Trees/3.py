import sys

sys.setrecursionlimit(10**6)

def in_order(binary_list, output_list, index):
    root = binary_list[index]
    if root[1] != -1:
        in_order(binary_list, output_list, root[1])
    if (root[1] != -1 and output_list[-1] == root[0]):
        output_list.append(float("inf"))
        
    output_list.append(root[0])

    if root[2] != -1:
        in_order(binary_list, output_list, root[2])
            
    return output_list


def pre_order(binary_list, output_list, index):
    
    root = binary_list[index]
    
    output_list.append(root[0])
    
    if root[1] != -1:
        pre_order(binary_list, output_list, root[1])
    
    if root[2] != -1:
        pre_order(binary_list, output_list, root[2])
            
    return output_list

def post_order(binary_list, output_list, index):
    
    root = binary_list[index]
    
    if root[1] != -1:
        post_order(binary_list, output_list, root[1])
    
    if root[2] != -1:
        post_order(binary_list, output_list, root[2])
     
    output_list.append(root[0])
    
    return output_list

binary_list = []
for i in range(int(input())):
    binary_list.append(list(map(int, input().split())))
    
if binary_list != []:
    c = in_order(binary_list, [], 0)
    if c ==sorted(c):
        print("CORRECT")
    else: 
        print("INCORRECT")
else:
    print("CORRECT")

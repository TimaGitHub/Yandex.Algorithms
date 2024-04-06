def recursion(values, array, index):
    if array[index] == -1:
        return 1
    else: 
        if values[array[index]] != -2:
            return 1 + values[array[index]]
        else: 
            values[array[index]] = recursion(values, array, array[index])
            return 1 + values[array[index]]
    
    
def high_tree(array):
    d = [-2] * len(array)
    for i in range(len(d)):
        if d[i] == -2:
            d[i] = recursion(d, array, i)
    print(max(d))
        
n = int(input())
high_tree(list(map(int, input().split())))

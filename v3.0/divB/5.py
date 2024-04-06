N = int(input())

def rec(array, count):
    
    q = len(array)
    
    if q in (0,1):
        return count
    
    minim = min(array)
    array = [x - minim for x in array]
    count += minim * (q - 1)
    start = 0
    for i in range(q):
        if array[i] == 0:
            count = rec(array[start:i], count)
            if i != q - 1 :
                start = i + 1
            else:
                start = q - 1
            
    if start != 0:    
        count = rec(array[start:], count)
            
    return count
    
numbers = [0]*N
for i in range(N):
    numbers[i] = int(input())
        
print(rec(numbers, 0))
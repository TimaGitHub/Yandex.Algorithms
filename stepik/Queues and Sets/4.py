import random
def func():
    n, e, d = list(map(int, input().split()))
    def find(i,array):
        if i != array[i]:
            array[i] = find(array[i], array)
        return array[i]

    first = [0] + [i for i in range(1, n+1)]

    for i in range(e):
        i, j = list(map(int, input().split()))
        if random.randint(0,10) > 5:
            first[find(i, first)] = first[find(j, first)]
        else:
            first[find(j, first)] = first[find(i, first)]
            
        find(random.randint(0,n - 1), first)  # перемешиваю случайные кучи, чтобы они не разрастались
        find(random.randint(0,n - 1), first)
        
    for i in range(d):
        i, j = list(map(int, input().split()))   
        if first[find(i, first)] == first[find(j, first)]:
            return 0
    return 1
print(func())

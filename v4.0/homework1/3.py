a = int(input())
ar1 = list(map(int, input().split()))
b = int(input())
ar2 = list(map(int, input().split()))
def simple_merge(list1, list2):
    i, j = 0, 0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    res += list1[i:]
    res += list2[j:] 
    # один из list1[i:] и list2[j:] будет уже пустой, поэтому добавится только нужный остаток
    return res
    
print(*simple_merge(ar1, ar2))
def bin_search(a, el):
    low = 0
    high = len(a) - 1
    mid = high // 2
    while low < high and a[mid] != el:
        if el > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
            
    return low
n = int(input())

list_numbers = list(set(map(int, input().split())))

k = int(input())

list_col = list(map(int, input().split()))

list_numbers.sort()

n = len(list_numbers)

if n != 0:
    for _ in list_col:
        a = bin_search(list_numbers, _)
        while list_numbers[a] < _:
            a += 1
            if a == n:
                break
        print(a)
        
else: print(0)
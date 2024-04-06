import math
reader = open('input.txt', 'r')
n= int(reader.readline())
array = []
for i in range(n):
    array += reader.readline().splitlines()
    
    
m = len(array[0])
print("Initial array:")
ans = ''

for el in array:
    ans += el + ', '
    
ans = ans[:-2]

print(ans)
print("**********")

for i in range(m - 1, - 1, -1):
    print(f'Phase {m - i}')
    new_array = []
    n_r = []
    bucket = {f'{k}': [] for k in range(10)}
    
    
    for j in range(n):
        a = array[j][i]
        bucket[a] += [array[j]] 
        
    for y, el1 in bucket.items():
        if el1 == []:
            print(f'Bucket {y}: empty')
        else:
            ans = ""
            for el2 in el1:
                if ans != '':
                    ans += ', '
                ans += el2 
                new_array.append(el2 + ',')
                n_r.append(el2)
            print(f'Bucket {y}: ' + ans)
    array = n_r.copy()
    print("**********")
    
print('Sorted array:')
new_array[-1] = new_array[-1][:-1]
print(*new_array)
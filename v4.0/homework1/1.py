n= int(input())
array = list(map(int, input().split() ) )
x = int(input())

a = 0

for el in array:
    if el < x:
        a += 1

print(a)
print(n - a)

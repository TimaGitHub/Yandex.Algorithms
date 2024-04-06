import copy

n = int(input())

init_string = ''.join([str(i) for i in range(1,n + 1)])

array = [False for i in range(n)]

ans = []

def recursion(array, ans, string):
    flag = False
    for index in range(n):
        if array[index] == False:
            flag = True
            temp_string = string + ''
            temp_string += init_string[index]
            temp = copy.copy(array)
            temp[index] = True
            recursion(temp, ans, temp_string)
            
    if not flag:
        ans.append(string)
        
        
recursion(array, ans, '')
print('\n'.join(sorted(ans)))
M = input()
new_list = []
for i in range(int(input())):
    el = list(map(int, input().split()))
    for_delete = []
    for i in range(len(new_list)):
        if (new_list[i][0] <= el[1] and el[1] <= new_list[i][1]) or (new_list[i][0] <= el[0] and el[0] <= new_list[i][1]) or (el[0] <= new_list[i][0] and el[1] >= new_list[i][1]):
            for_delete.append(new_list[i])
    for _ in for_delete:
        new_list.remove(_)
    new_list.append(el)
    
print(len(new_list))
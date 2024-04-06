def h(S, m):
    
    answer = 0
    
    for i in range(len(S)):
        answer += (S.encode('ascii')[i] * (263 ** i)) 
    answer = answer % 1000000007
    return answer % m

m = int(input())

hesh_table = [[None]] * m

list_commands = []

for _ in range(int(input())):
    list_commands.append(input().split())

for command in list_commands:
    
    if command[0] == 'add':
        if hesh_table[h(command[1], m)] == [None]:
            hesh_table[h(command[1], m)] = [command[1]]
        else:
            flag = True
            for _ in hesh_table[h(command[1], m)]:
                if _ == command[1]:
                    flag = False
            if flag:
                hesh_table[h(command[1], m)].insert(0, command[1])
        
    if command[0] == 'check':
        if hesh_table[int(command[1])] == [None]:
            print(' ')
        else: 
            for _ in hesh_table[int(command[1])]:
                print(_, end = ' ')
            print('\n')
    if command[0] == 'find':
        if hesh_table[h(command[1], m)] == [None]:
            print('no')
        else:
            flag =True
            for _ in hesh_table[h(command[1], m)]:
                if _ == command[1]:
                    print('yes') 
                    flag = False
            if flag:
                print('no')
                    
    if command[0] == 'del':
        if hesh_table[h(command[1], m)] == [None]:
            pass
        else:
            for _ in hesh_table[h(command[1], m)]:
                if _ == command[1]:
                    hesh_table[h(command[1], m)].remove(_)
                    
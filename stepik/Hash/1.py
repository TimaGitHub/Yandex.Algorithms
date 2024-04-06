list_commands = []

for _ in range(int(input())):
    list_commands.append(input().split())
hesh_table = [None] * 10000000
    
for command in list_commands:
    if command[0] == 'add':
        hesh_table[int(command[1])] = command[2]

    if command[0] == 'find':
        if hesh_table[int(command[1])] == None:
            print('not found')
        else:
            print(hesh_table[int(command[1])])
                    
    if command[0] == 'del':
        hesh_table[int(command[1])] = None
        
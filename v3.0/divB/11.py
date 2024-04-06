command = input()

ex_array = []
while command != 'exit':
    if command == 'pop':
        if len(ex_array) == 0:
            print('error')
        else:
            print(ex_array.pop())
    
    elif command == 'back':
        if len(ex_array) == 0:
            print('error')
        else:
            print(ex_array[-1])
        
        
    elif command == 'size':
        print(len(ex_array))
    elif command == 'clear':
        
        ex_array.clear()
        print('ok')
    else:
        ex_array.append(int(command.split()[1]))
        print('ok')
    command = input()

print('bye')        
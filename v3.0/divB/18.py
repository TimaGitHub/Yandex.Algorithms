queue = []

task = input().split()

while task[0] != 'exit':
    
    if task[0] == 'push_front':
        print('ok')
        queue.insert(0, task[1])
        
    elif task[0] == 'push_back':
        print('ok')
        queue += [task[1]]   

    elif task[0] == 'pop_front':
        
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print('error')
            
    elif task[0] == 'pop_back':
        if len(queue) != 0:
            print(queue.pop(-1))
        else:
            print('error')
    
    elif task[0] == 'front':
        if len(queue) !=0:
            print(queue[0])
        else:
            print('error')
    elif task[0] == 'back':
        if len(queue) !=0:
            print(queue[-1])
        else:
            print('error')

    elif task[0] == 'size':
        print(len(queue))

    elif task[0] == 'clear':
        queue.clear()
        print('ok')

    task = input().split()
    
print('bye')
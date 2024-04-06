f = open('input.txt', 'r')
n = int(f.readline())

stack = []

for i in range(n):
    command = f.readline().split()
    if command[0] == 'add':
        stack.append([int(command[1]), command[2]])
        
    elif command[0] == 'delete':
        count = int(command[1])
        
        while count != 0:
            a = stack.pop()
            count -= a[0]
            if count < 0:
                stack.append([-count, a[1]])
                count = 0
        
    elif command[0] == 'get':
        count = 0
        for i in range(len(stack)):
            if stack[i][1] == command[1]:
                count += stack[i][0]
        print(count)
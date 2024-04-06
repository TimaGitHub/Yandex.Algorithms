import queue

file1 = open('input.txt', 'r')
n = int(file1.readline())

stones = [[[' ' for j in range(n+1)] for i in range(n+1)] for k in range(n+1)]
visited = [[[False for j in range(n+1)] for i in range(n+1)] for k in range(n+1)]

array = []
index = 0 

flag = True

for i in range(1, n+ 1):
    empty = file1.readline()
    for j in range(1, n + 1):
        coords = list(file1.readline())[:-1]
        if flag and 'S' in coords:
            start = [i, j, coords.index('S') + 1]
            flag = False
       
        stones[i][j] = [' '] + coords
        
exit = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if stones[1][i][j] == '.':
            exit.append([1, i, j])
         
que = queue.LifoQueue()
que.put([start])

if start[0] == 1:
    print(0)
    
else:
    flag = True
    while flag:
        array.append([])
        stone = que.get()
        one_layer = []
        for direction in stone:
            a, b, c = direction
            if not visited[a][b][c] and stones[a][b][c] != '#':
                array[index].append(direction)
                visited[a][b][c] = True
                
                if (a - 1 > 0 and a - 1 < n + 1):
                    one_layer.append([a-1, b , c])
                    if  [a - 1, b, c] in exit:
                        flag = False
                        break
                if  (a + 1 > 0 and a + 1 < n + 1):
                    one_layer.append([a+1, b , c])
                    if [a + 1, b, c] in exit:
                        flag = False
                        break
                if (b - 1 > 0 and b - 1 < n + 1):
                    one_layer.append([a, b - 1, c])
                    if [a, b - 1, c ] in exit:
                        flag = False
                        break
                if (b + 1 > 0 and b + 1 < n + 1):
                    one_layer.append([a, b + 1, c])
                    if [a, b + 1, c ] in exit:
                        flag = False
                        break
                if  (c - 1 > 0 and c - 1 < n + 1):
                    one_layer.append([a, b, c-1])
                    if [a, b, c - 1] in exit:
                        flag = False
                        break
                if (c + 1 > 0 and c + 1 < n + 1):
                    one_layer.append([a, b, c+1])
                    if [a, b, c + 1] in exit:
                        flag = False
                        break

        if one_layer != []:
            que.put(one_layer)
            index += 1


    print(index)
        
        
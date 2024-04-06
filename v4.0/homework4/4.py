import copy

reader = open('input.txt', 'r')

n = int(reader.readline())

if n == 1:
    a = list(map(int, reader.readline().split()))
    print(0)
else:
    graph = [[0]]
    gr = [[0]]

    last_info = [float('inf')]

    for i in range(n):

        c1 = [float('inf')] + list(map(int, reader.readline().split()))
        b = copy.copy(c1)
        for index in range(1,n+1):
            if c1[index] == 0:
                c1[index] = float('inf')
                
        graph.append(c1)
        gr.append(copy.copy(c1))

        graph[i+1][i+1] = float('inf')
        gr[i+1][i+1] = float('inf')

        
        if i != n:
            graph[i+1][1] = float('inf')
            if i != n - 1:
                gr[i+1][1] = float('inf')
        
        last_info.append(b[1])

    best = 0
    child = 1
    array = []
    count = 0
    while count != n - 1:
        index = graph[child].index(min(graph[child]))
        best += graph[child][index]
        child = index
        for i in range(1,n + 1):
            graph[i][index] = float('inf')
        count += 1
    if child == 0:
        print(-1)
        
    else:
        best += gr[child][1]
        
        info = [0] + [min(i) for i in gr[1:]]
        gr[n][1] = float('inf')

        def rec(path, count, child, q, min_info):
            global best

            if count != n - 1:
                if path + sum(min_info) < best:
                    for i in range(1, n + 1):
                        if q[child][i] != float('inf'):
                            haha = copy.copy(min_info)
                            haha[i] = 0
                            hehe = copy.deepcopy(q)
                            for j in range(1,n + 1):
                                hehe[j][i] = float('inf')
                            rec(path + q[child][i], count + 1, i , hehe, haha)
            else:
                if child != 1 and best > path + last_info[child]:

                    best = path + last_info[child]


        rec(0, 0, 1, gr, info)
        if best == float('inf'):
            print(-1)
        else:
            print(best)

for i in range(n):
    new_array.append(int(input()))
    
if n != 0:    
    main_array = [[0] * 2 + [float('inf')] * (n +1)]

    for i in range(1, n + 1):
        main_array.append([float('inf')]  * (n+3))
        for j in range(1,n + 2):
            if True:
                c = new_array[i]
                if c > 100:
                    a = min(main_array[i-1][j-1] + c,  main_array[i-1][j] + c , main_array[i-1][j + 1])
                    main_array[i][j] = a
                else:
                    a = min(main_array[i-1][j] + c, main_array[i-1][j + 1])
                    main_array[i][j] = a

            
            
    print(min(main_array[n][1], main_array[n][2]))

    i = n
    j = 1

    ans = []

    a = main_array[i][j]
    b = main_array[i][j + 1]

    if b <= a:
        j +=1
        print(1, end = ' ')
    else:
        print(0, end = ' ')

    while i != 1:
        q = new_array[i]
        c = main_array[i-1][j-1]
        if main_array[i][j] == c + q:
            c += q
        else: c = float('inf')
    
        d = main_array[i-1][j]
        if main_array[i][j] == d + q:
            d += q
        else: d  = float('inf')
        
        e = main_array[i-1][j+1]
        if main_array[i][j] != e:
            e = float('inf')
        l = min(c,d  ,e)
        if e != float('inf') and l == e:
            ans += [i]
            i -=1
            j +=1
        elif d != float('inf') and l == d:
            i -= 1
        elif c != float('inf') and l == c:
            i -=1
            j -=1
        else:
            j -= 1
        
    print(len(ans))
    ans.reverse()

    for el in ans:
        print(el)
        
        
else:
    print(0)
    print(0,0)
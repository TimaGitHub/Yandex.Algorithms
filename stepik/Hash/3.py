pattern = input()
string = input()
hesh_list = [-1] * (len(string) - len(pattern) + 1)
с = 0
h_pattern = 0
degrees = []
hi = string.encode('ascii')
if len(pattern) == len(string) and (pattern == string):
    print(0)
else:
    for _ in range(len(pattern)):
        degrees.append(pow(2,_, 2002577))
        h_pattern += (pattern.encode('ascii')[_] * degrees[_]) % 2002577
        с += (hi[len(string) - len(pattern)  +  _] * degrees[_]) % 2002577
    hesh_list[-1] = (с + 2002577) % 2002577
    new_list = []
    if h_pattern == hesh_list[-1]:
        new_list.append(len(hesh_list) - 1)
    for _ in range(len(hesh_list) - 2, -1, -1):
        hash_i =  ((2 * (hesh_list[_ + 1] - ((hi[_ + len(pattern)]) * (degrees[(len(pattern) - 1)]))))
            + hi[_]) % 2002577
        hesh_list[_] = (hash_i + 2002577) % 2002577
        if (hesh_list[_] == h_pattern):
            new_list.append(_)
    new_list.reverse()  
    print(*new_list)
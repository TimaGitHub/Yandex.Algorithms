A = list(map(int, input().split(':')))
B = list(map(int, input().split(':')))
C = list(map(int, input().split(':')))


for_hours = 0
for_minutes =  0
for_sec = 0

ras = abs(A[2] - C[2]) + 1 if abs(A[2] -  C[2]) % 2 != 0 else abs(A[2] - C[2])

minutes_flag = True
sec_flag = True

if A[0] > C[0]:
    for_hours = abs(24 - A[0] + C[0]) * 3600
elif A[0] < C[0]:
    for_hours = abs(A[0] - C[0]) * 3600               
else: 
    if A[1] < C[1]:
        for_hours = 0
    elif A[1] > C[1]:
        for_hours = 23 * 3600  
    else:
        if A[2] <= C[2]:
            for_hours = 0
            for_minutes = 0
            minutes_flag = False
        else:
            for_hours = 23 * 3600 
            for_minutes = 59 * 60
            minutes_flag = False
    
if minutes_flag:
    if A[1] < C[1]:
        for_minutes = abs(A[1] - C[1]) * 60
    elif A[1] > C[1]:                 
        for_hours -= 3600
        for_minutes =  abs(60 - A[1] + C[1]) * 60                 
    else: 
        if A[2] <= C[2]:
            for_minutes = 0
        else:
            for_minutes = 59 * 60
            minutes_flag = False

            

if A[2] > C[2]:
    if minutes_flag:
        for_minutes -= 60
    ras = abs(60 - A[2] + C[2]) + 1 if abs(60 - A[2] + C[2]) % 2 != 0 else abs(60 - A[2] + C[2])
    

time_diff = ( for_hours + for_minutes + ras ) / 2
    
a = time_diff % 60

time_diff -= a
   
time_diff += ((B[2] + a) // 60) * 60

sec = ( B[2] + a ) % 60

a = time_diff % 3600 

time_diff -= a

time_diff += ((B[1] * 60 + a) // 3600) * 3600

minutes = (B[1] + a // 60)  % 60

hours = (B[0] + time_diff / 3600) % 24 

hour = str(int(hours)) if hours >= 10 else '0' + str(int(hours))
mint = str(int(minutes)) if minutes >= 10 else '0' + str(int(minutes))
sec = str(int(sec)) if sec >= 10 else '0' + str(int(sec))

print('{}:{}:{}'.format(hour, mint, sec))
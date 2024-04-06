n= int(input())
if n != 0:
    ans = list(map(int, input().split()))
    print(*sorted(ans))

else:
    print(' ')
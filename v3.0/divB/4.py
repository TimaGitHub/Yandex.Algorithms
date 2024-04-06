def func (N, k ,row_number, binery):
    num = 2 * row_number - 1 if binery == 1 else 2 * row_number
    left = num - k if num - k  >= 0 else False
    right = num + k if num + k <= N else False

    if k % 2 == 0:
        b = 1 if binery == 1 else 2
    else: 
        b = 2 if binery == 1 else 1
    if left and right:
        if row_number - left // 2 - (left % 2) < right // 2 - row_number + (right % 2):
            a = left // 2 + (left % 2) 
        else:
            a = right // 2 + (right % 2) 
        print(a, b)
    elif left and not right:
        a = left // 2 + (left % 2) 
        print(a,b)
    elif right and not left:
        a = right // 2 + (right % 2) 
        print(a, b)
    else:
        print(-1)
    
func(int(input()) , int(input()) , int(input()), int(input()))
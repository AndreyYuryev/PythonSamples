n = int(input())
num = 0
while num < n:
    if num == 0:
        num = 1
    else:
        if num * 2 > n:
            break
        else:
            num = num * 2
    print(num, end=" ")

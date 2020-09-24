n = int(input())
maxSq = n
num_max = 0
while n != 0:
    if n != 0 and n > maxSq:
        maxSq = n
        num_max = 1
    elif n != 0 and n == maxSq:
        num_max += 1
    n = int(input())
else:
    print(num_max)

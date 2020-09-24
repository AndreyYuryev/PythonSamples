n = int(input())
maxSq = n
p_maxSq = -1
while n != 0:
    if n != 0:
        if n > maxSq:
            p_maxSq = maxSq
            maxSq = n
        elif n < maxSq and p_maxSq < n:
            p_maxSq = n
        elif n == maxSq and p_maxSq >= 0:
            p_maxSq = n
        elif p_maxSq == -1:
            p_maxSq = 0
        n = int(input())
else:
    print(p_maxSq)

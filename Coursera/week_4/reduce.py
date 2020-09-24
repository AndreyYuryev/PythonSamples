def ReduceFraction(n, m):
    p = n
    q = m
    mx = n
    if n > m:
        mx = m
    for i in range(2, mx + 1):
        if n % i == 0 and m % i == 0:
            p = n // i
            q = m // i
    return p, q


a = int(input())
b = int(input())
print(*ReduceFraction(a, b))

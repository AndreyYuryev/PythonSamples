def power(b, m):
    out = b
    if m > 1:
        i = m - 1
        out *= power(b, i)
    elif m == 0:
        return 1
    return out

a = float(input())
n = int(input())
print(power(a, n))

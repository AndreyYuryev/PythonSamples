def sum(n, m):
    out = 0
    if n > 0:
        out = sum(n - 1, m)
        out += 1
    else:
        if m > 1:
            out = sum(m - 1, 0)
            out += 1
        elif m == 1:
            out = 1
    return out


a = int(input())
b = int(input())
print(sum(a, b))

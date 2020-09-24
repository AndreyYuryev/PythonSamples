def sum_seq(a):
    out = a
    if a != 0:
        b = int(input())
        out = a + sum_seq(b)
    return out

n = int(input())
print(str(sum_seq(n)))

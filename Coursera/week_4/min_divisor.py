def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= n ** 0.5:
            return n
        i += 1
    return i


in_n = int(input())
print(MinDivisor(in_n))

from math import ceil, floor
n = float(input())
n_rnd = 0
if 0 <= (n * 10 % 10) < 5:
    n_rnd = floor(n)
else:
    n_rnd = ceil(n)
print(n_rnd)

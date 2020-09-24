import math
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
x1 = 0
x2 = 0
if d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
    print(x1, x2, sep=" ")
elif d == 0:
    x1 = -b / (2 * a)
    print(x1)

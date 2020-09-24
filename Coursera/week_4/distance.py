from math import sqrt


def distance(a, b, c, d):
    return sqrt((c - a) ** 2 + (d - b) ** 2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))

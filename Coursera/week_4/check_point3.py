def IsPointInCircle(x, y, xc, yc, r):
    return ((xc - x) ** 2 + (yc - y) ** 2) ** 0.5 <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")

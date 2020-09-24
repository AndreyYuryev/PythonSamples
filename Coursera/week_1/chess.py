x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x2 == x1 and y2 == y1) or y2 < y1:
    print("NO")
elif abs(x2 - x1) % 2 == 0 and (y2 - y1) % 2 == 0:
    print("YES")
elif abs(x2 - x1) % 2 == 1 and (y2 - y1) % 2 == 1:
    print("YES")
else:
    print("NO")

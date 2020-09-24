x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (abs(x2 - x1) % 2 == 0 and abs(y2 - y1) % 2 == 0):
    print("YES")
elif (abs(x2 - x1) % 2 == 1 and abs(y2 - y1) % 2 == 1):
    print("YES")
else:
    print("NO")

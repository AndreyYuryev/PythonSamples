a = int(input())
b = int(input())
c = int(input())
if (a % 2 == 0 or b % 2 == 0 or c % 2 == 0):
    odd = 1
else:
    odd = 0
if (a % 2 == 1 or b % 2 == 1 or c % 2 == 1):
    even = 1
else:
    even = 0
if odd == 1 and even == 1:
    print("YES")
else:
    print("NO")

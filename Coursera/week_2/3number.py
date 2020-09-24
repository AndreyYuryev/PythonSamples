a, b, c = int(input()), int(input()), int(input())
if not a <= b <= c:
    if b <= a:
        (a, b) = (b, a)
    if c <= b:
        (b, c) = (c, b)
    if b <= a:
        (a, b) = (b, a)
print(a, b, c)

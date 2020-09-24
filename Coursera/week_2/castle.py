a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if not a <= b <= c:
    if b <= a:
        (a, b) = (b, a)
    if c <= b:
        (b, c) = (c, b)
    if b <= a:
        (a, b) = (b, a)
if e <= d:
    (e, d) = (d, e)
if a <= d and b <= e:
    print("YES")
else:
    print("NO")

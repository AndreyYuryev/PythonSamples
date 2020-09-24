a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if not a1 <= b1 <= c1:
    if b1 <= a1:
        (a1, b1) = (b1, a1)
    if c1 <= b1:
        (b1, c1) = (c1, b1)
    if b1 <= a1:
        (a1, b1) = (b1, a1)
if not a2 <= b2 <= c2:
    if b2 <= a2:
        (a2, b2) = (b2, a2)
    if c2 <= b2:
        (b2, c2) = (c2, b2)
    if b2 <= a2:
        (a2, b2) = (b2, a2)
if a1 <= a2 and b1 <= b2 and c1 <= c2:
    if a1 == a2 and b1 == b2 and c1 == c2:
        print("Boxes are equal")
    else:
        print("The first box is smaller than the second one")
elif a2 <= a1 and b2 <= b1 and c2 <= c1:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")

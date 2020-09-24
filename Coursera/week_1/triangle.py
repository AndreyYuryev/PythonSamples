a = int(input())
b = int(input())
c = int(input())
k1 = 0
k2 = 0
g = 0
if a <= b <= c or b <= a <= c:
    k1 = a
    k2 = b
    g = c
    if g ** 2 == k1 ** 2 + k2 ** 2:
        print("rectangular")
    elif g ** 2 > k1 ** 2 + k2 ** 2:
        print("acute")
    elif g ** 2 < k1 ** 2 + k2 ** 2:
        print("obtuse")
    else:
        print("impossible")
elif a <= c <= b or c <= a <= b:
    k1 = a
    k2 = c
    g = b
    if g ** 2 == k1 ** 2 + k2 ** 2:
        print("rectangular")
    elif g ** 2 > k1 ** 2 + k2 ** 2:
        print("acute")
    elif g ** 2 < k1 ** 2 + k2 ** 2:
        print("obtuse")
    else:
        print("impossible")
elif c <= b <= a or b <= c <= a:
    k1 = c
    k2 = b
    g = a
    if g ** 2 == k1 ** 2 + k2 ** 2:
        print("rectangular")
    elif g ** 2 > k1 ** 2 + k2 ** 2:
        print("acute")
    elif g ** 2 < k1 ** 2 + k2 ** 2:
        print("obtuse")
    else:
        print("impossible")
else:
    print("impossible")

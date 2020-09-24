def merge(a, b):
    c = []
    alen = len(a)
    blen = len(b)
    aindx = bindx = 0
    maxa = maxb = False
    while maxa is False or maxb is False:
        if maxa is True or (maxb is False and a[aindx] > b[bindx]):
            c.append(b[bindx])
            if bindx < blen - 1:
                bindx += 1
            else:
                maxb = True
        elif maxb is True or (maxa is False and a[aindx] <= b[bindx]):
            c.append(a[aindx])
            if aindx < alen - 1:
                aindx += 1
            else:
                maxa = True
    return c


mList1 = list(map(int, input().split()))
mList2 = list(map(int, input().split()))
print(*merge(mList1, mList2))

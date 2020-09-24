n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))


def distance(nDst, b):
    Dst = list()
    for i in b:
        Dst.append((abs(nDst - i[0]), i[1]))
    Dst.sort()
    return Dst[0][1]


def distance2(nDst, b):
    Dst = list()
    indx = 0
    for i in b:
        Dst.append((abs(nDst - i), indx))
        indx += 1
    Dst.sort()
    return Dst[0][1]


nDist = list()
for i in range(n):
    nDist.append((nList[i], i, 0))
nDist.sort()
mDist = list()
oDist = list()
for i in range(m):
    mDist.append((mList[i], i))
for nE in nDist:
    oDist.append((nE[1], distance2(nE[0], mList)))
oDist.sort()
out = list()
for nE in oDist:
    out.append(nE[1] + 1)
print(*out)

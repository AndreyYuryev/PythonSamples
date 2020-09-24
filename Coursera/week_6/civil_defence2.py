n = int(input())
nList = list(map(int, input().split()))
for i in range(n):
    nList[i] = [nList[i], i + 1, 0]


def distance2(lst, b):
    Dst = list()
    for i in b:
        Dst.append((abs(lst - i[0]), i[1]))
    Dst.sort()
    return Dst[0][1]


m = int(input())
mList = list(map(int, input().split()))
for i in range(m):
    mList[i] = [mList[i], i + 1]
for i in range(n):
    nList[i][1] = distance2(nList[i][0], mList)
out = list()
for nE in nList:
    out.append(nE[1])
print(*out)

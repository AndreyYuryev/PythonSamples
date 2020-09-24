nList = tuple(map(int, input().split()))


def countSort(a):
    size = 101
    cntList = [0] * size
    oList = []
    for mlist in a:
        cntList[mlist] += 1
    for now in range(size):
        for i in range(cntList[now]):
            oList.append(str(now))
    return oList


print(*countSort(nList))

mList = list(map(int, input().split()))


def countSort(a):
    nList = []
    nList.append(a[0])
    prev = a[0]
    for i in range(1, len(a)):
        if prev <= a[i]:
            nList.append(a[i])
            prev = a[i]
        else:
            for j in range(i):
                if nList[j] >= a[i]:
                    nList.insert(j, a[i])
                    break
            else:
                nList.append(a[i])
                prev = a[i]
    return nList


print(*countSort(mList))

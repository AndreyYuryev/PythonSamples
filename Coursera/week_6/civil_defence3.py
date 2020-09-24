n = int(input())
nList = list(map(int, input().split()))
for i in range(n):
    nList[i] = [nList[i], i + 1, 0]
nList.sort()
m = int(input())
mList = list(map(int, input().split()))
for i in range(m):
    mList[i] = [mList[i], i + 1]
mList.sort()


start = 0
for i in range(n):
    idx = 0
    minimum = 10e10
    for j in range(start, m):
        tmp = abs(nList[i][0] - mList[j][0])
        if tmp < minimum:
            idx = j
            minimum = tmp
            nList[i][2] = mList[j][1]
        else:
            break
    start = idx

nList.sort(key=lambda idx: idx[1])
for i in nList:
    print(i[2], end=" ")

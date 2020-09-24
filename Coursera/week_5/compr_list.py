mList = list(map(int, input().split()))
i = 0
maxI = len(mList)
fExit = False
while fExit is False:
    if mList[i] == 0:
        mList.append(mList.pop(i))
    else:
        i += 1
    maxI -= 1
    if maxI == 0:
        fExit = True
print(*mList)

mList = list(map(int, input().split()))
indxL = len(mList)
if indxL > 1:
    for i in range(indxL // 2):
        mList[i], mList[indxL - i - 1] = mList[indxL - i - 1], mList[i]
print(*mList)

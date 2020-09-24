mList = list(map(int, input().split()))
i = 0
mListInd = [mList[0], mList[len(mList) - 1]]
maxInd = 0
minInd = len(mList) - 1
for i in range(len(mList)):
    if mList[i] > mListInd[0]:
        mListInd[0] = mList[i]
        maxInd = i
    if mList[i] < mListInd[1]:
        mListInd[1] = mList[i]
        minInd = i

(mList[maxInd], mList[minInd]) = (mList[minInd], mList[maxInd])
print(*mList)

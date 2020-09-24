mLen = int(input())
mList = list(map(int, input().split()))
mNum = int(input())
mDif = abs(mNum - mList[0])
mIndx = [mList[0]]
for i in range(1, len(mList)):
    if abs(mNum - mList[i]) < mDif:
        mIndx.insert(0, mList[i])
        mDif = abs(mNum - mList[i])

print(mIndx[0])

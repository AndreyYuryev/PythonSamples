iFile = open('input2.txt', 'r', encoding='utf-8')
iWords = []
for line in iFile:
    iWords.extend(line.strip().split())
iFile.close()
myDict = {}
for item in iWords:
    myDict[item] = myDict.get(item, 0) + 1
iWord = []
for item in myDict:
    iWord.append((myDict[item], item))
iWord.sort(reverse=True)
mDict = {}
mmax = iWord[0][0]
mindex = 0
for i in range(mmax, 0, -1):
    mTuple = []
    while mindex < len(iWord) and iWord[mindex][0] == mmax:
        mTuple.append(iWord[mindex][1])
        mindex += 1
    mDict[i] = sorted(mTuple)
    mmax -= 1
for item in mDict:
    for itm in mDict[item]:
        print(itm)

iFile = open('input3.txt', 'r', encoding='utf-8')
iWords = []
for line in iFile:
    iWords.append(line.strip())
iFile.close()
myDict = {}
mCounter = len(iWords)
mWin = []
for item in iWords:
    myDict[item] = myDict.get(item, 0) + 1
for item in myDict:
    mWin.append((myDict.get(item, 0), item))
mWin.sort(reverse=True)
oFile = open('output3.txt', 'w', encoding='utf-8')
if mWin[0][0] > 0.5 * mCounter:
    print(mWin[0][1], file=oFile)
else:
    print(mWin[0][1], file=oFile)
    print(mWin[1][1], file=oFile)
oFile.close()

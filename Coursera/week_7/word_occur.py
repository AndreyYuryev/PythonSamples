iFile = open('input.txt', 'r', encoding='utf-8')
iWords = []
for line in iFile:
    iWords.extend(line.strip().split())
iFile.close()
myDict = {}
for item in iWords:
    print(myDict.get(item, 0), end=' ')
    myDict[item] = myDict.get(item, 0) + 1

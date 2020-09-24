fin = open('inp.txt', 'r', encoding='utf-8')
inp = []
for line in fin:
    inp.extend(line.strip().split())
fin.close()
myDict = {}
maxNum = 0
for item in inp:
    myDict[item] = myDict.get(item, 0) + 1
    if myDict[item] > maxNum:
        maxNum = myDict[item]
for item in sorted(myDict):
    if myDict[item] == maxNum:
        print(item)
        break

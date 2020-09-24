n = int(input())
myDict = {}
for i in range(1, n + 1):
    key, val = map(str, input().split())
    myDict[key] = val
word = input()
if word in myDict.keys():
    print(myDict[word])
else:
    for item in myDict:
        if myDict[item] == word:
            print(item)
            break

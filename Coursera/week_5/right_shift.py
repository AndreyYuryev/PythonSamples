mList = list(map(int, input().split()))
last = len(mList) - 1
mList.insert(0, mList.pop(last))
print(*mList)

mList = list(map(int, input().split()))
i = 0
while i < len(mList) - 1:
    mList.insert(i, mList.pop(i + 1))
    i += 2
print(*mList)

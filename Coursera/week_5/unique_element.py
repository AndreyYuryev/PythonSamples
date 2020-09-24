mList = list(map(int, input().split()))
mList2 = []
for i in mList:
    if i not in mList2 and mList.count(i) < 2:
        mList2.append(i)

print(*mList2)

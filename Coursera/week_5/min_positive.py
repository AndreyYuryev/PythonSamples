mList = list(map(int, input().split()))
min_pos = 0
for i in range(len(mList)):
    if min_pos == 0 and mList[i] > 0:
        min_pos = mList[i]
    elif 0 < mList[i] < min_pos != 0:
        min_pos = mList[i]
print(min_pos)

cust = list(map(int, input().split()))
mList = []
for i in range(cust[1]):
    mList.append(int(input()))
mList.sort()
maxsize = 0
maxuser = 0
i = 0
while i < cust[1]:
    maxsize += mList[i]
    if maxsize <= cust[0]:
        maxuser += 1
    else:
        break
    i += 1
print(maxuser)

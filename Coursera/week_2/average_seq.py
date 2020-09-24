n = int(input())
sumSq = 0
numSq = 0
while n != 0:
    sumSq += n
    numSq += 1
    n = int(input())
else:
    print(sumSq / numSq)

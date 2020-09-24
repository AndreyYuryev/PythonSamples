n = int(input())
numSq = 0
while n != 0:
    if n % 2 == 0:
        numSq += 1
    n = int(input())
else:
    print(numSq)

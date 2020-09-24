kList = list()
nList = list()
with open('grade_input.txt', 'r', encoding='UTF-8') as inFile:
    n = int(inFile.readline())
    for line in inFile:
        abt = line.split()[-1::-1]
        grade = 0
        if int(abt[0]) >= 40 and int(abt[1]) >= 40 and int(abt[2]) >= 40:
            grade = int(abt[0]) + int(abt[1]) + int(abt[2])
            kList.append(grade)
kList.sort()
oFile = open("grade_output.txt", 'w', encoding='UTF-8')
if int(len(kList)) == 0 or int(len(kList)) == 1:
    print(0, file=oFile, end='')
elif int(len(kList)) < n:
    print(kList[len(kList) - 1], file=oFile, end='')
else:
    if kList[n - 1] == kList[n]:
        if n - 2 >= 0:
            print(kList[n - 2], file=oFile, end='')
        else:
            print(0, file=oFile, end='')
    else:
        print(kList[n - 1], file=oFile, end='')
oFile.close()

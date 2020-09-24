kList = list()
nList = list()
max_grade = 0
count_max = 0
with open('input.txt', 'r', encoding='UTF-8') as inFile:
    n = int(inFile.readline())
    for line in inFile:
        abt = line.split()[-1::-1]
        grade = int(abt[0]) + int(abt[1]) + int(abt[2])
        if int(abt[0]) >= 40 and int(abt[1]) >= 40 and int(abt[2]) >= 40:
            if grade > max_grade:
                max_grade = grade
                count_max = 1
            elif grade == max_grade:
                count_max += 1
            kList.append(grade)
kList.sort(reverse=True)
k_lenght = int(len(kList))
if k_lenght < n:
    out_grade = 0
elif k_lenght == n:
    if count_max == n and count_max > 1:
        out_grade = 1
    else:
        out_grade = 0
else:
    if count_max >= n:
        out_grade = 1
    else:
        i = 0
        min = 0
        i = n - 1
        min = kList[i]
        while i >= 0:
            if kList[i] > min:
                break
            else:
                i -= 1
        out_grade = kList[i]
oFile = open('output.txt', 'w', encoding='utf-8')
print(out_grade, end='', file=oFile)

mlist = list()
with open('l_input.txt', 'r', encoding='UTF-8') as inFile:
    for line in inFile:
        mlist.append(list(map(str, line.split())))
inFile.close()
mlist.sort(key=lambda mlist: mlist[0])
outFile = open('l_output.txt', 'w', encoding='UTF-8')
for i in mlist:
    print(i[0], i[1], i[3], file=outFile)
outFile.close()

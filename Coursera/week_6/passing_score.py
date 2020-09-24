infile = open('input.txt', 'r', encoding='utf-8')
outfile = open('output.txt', 'w', encoding='utf-8')
allitems = infile.read().splitlines()
k = int(allitems[0])
del allitems[0]
my_list = []
for i in allitems:
    data = i.split()
    if int(data[-3]) >= 40 and int(data[-2]) >= 40 and int(data[-1]) >= 40:
        my_list.append(int(data[-3]) + int(data[-2]) + int(data[-1]))
my_list.sort(reverse=True)
if len(my_list) <= k:
    print(0, file=outfile)
elif my_list[0] == my_list[k]:
    print(1, file=outfile)
elif my_list[k] == my_list[k - 1]:
    j = my_list.index(my_list[k], 0, k)
    print(my_list[j - 1], file=outfile)
else:
    print(my_list[k - 1], file=outfile)
infile.close()
outfile.close()

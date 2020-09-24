class AvgGrd():
    name = 0
    value = 0
    counter = 0
    average = .0


avg9 = AvgGrd()
avg10 = AvgGrd()
avg11 = AvgGrd()
inFile = open('avrg_grd_pnt_input.txt', 'r', encoding='UTF-8')
# with open('avrg_grd_pnt_input.txt', 'r', encoding='UTF-8') as inFile:
for line in inFile:
    avg = list(map(str, line.split()))
    if int(avg[2]) == 9:
        avg9.value += int(avg[3])
        avg9.counter += 1
    elif int(avg[2]) == 10:
        avg10.value += int(avg[3])
        avg10.counter += 1
    elif int(avg[2]) == 11:
        avg11.value += int(avg[3])
        avg11.counter += 1
inFile.close()
if avg9.counter > 0:
    avg9.average = avg9.value / avg9.counter
if avg10.counter > 0:
    avg10.average = avg10.value / avg10.counter
if avg11.counter > 0:
    avg11.average = avg11.value / avg11.counter
outFile = open('avrg_grd_pnt_output.txt', 'w', encoding='UTF-8')
print(avg9.average, avg10.average, avg11.average, file=outFile, end='')
outFile.close()
number = int(input())
d1 = number // 1000
d2 = (number // 100) % 10
d3 = (number // 10) % 10
d4 = number % 10
# out = (100 - (10 - d1) % (10 - d4) - (10 - d2) % (10 - d3)) // 100
out1 = (100 - (10 - d1) % (10 - d4) - (10 - d2) % (10 - d3)) // 100
out2 = (100 - (10 - d1) % (10 - d4) - (10 - d2) % (10 - d3)) % 100
out = out1 + out2
print(out)

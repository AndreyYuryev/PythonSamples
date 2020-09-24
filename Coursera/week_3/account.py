from math import floor
p = int(input())
x = int(input())
y = int(input())
p_fl = float(p / 100)
acc = floor((p_fl * (x * 100 + y)) + (x * 100 + y))
print(acc // 100, acc % 100, sep=" ")

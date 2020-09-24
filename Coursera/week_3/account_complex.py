from math import floor
p = int(input())
x = int(input())
y = int(input())
k = int(input())
p_fl = float(p / 100)
i = 1
acc = floor(x * 100 + y)
acc_p = 0
while i <= k:
    acc_p = floor(p_fl * acc)
    acc += acc_p
    i += 1
print(acc // 100, acc % 100, sep=" ")

import math
price = float(input())
rub = math.floor(price)
cp = math.ceil((price * 100) % 100)
print(rub, cp, sep=" ")

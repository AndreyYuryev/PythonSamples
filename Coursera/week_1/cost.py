a = int(input())
b = int(input())
n = int(input())
cost = (a * 100 + b) * n
# cost_a = a * n + (b * n) // 100
# cost_b = (b * n) % 100
print(cost // 100, cost % 100, sep=" ")
# print(cost_a, cost_b, sep=",")

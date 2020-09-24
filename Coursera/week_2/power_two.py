n = int(input())
number = 0
while number < n:
    if number == 0:
        number = 1
    else:
        number = number * 2
else:
    if n == number and (number % 2 == 0 or number == 1):
        print("YES")
    else:
        print("NO")

number = input()
digit1 = int(number) // 100
digit2 = int((int(number) / 10) % 10)
digit3 = int((int(number) % 10))
print(digit1 + digit2 + digit3)

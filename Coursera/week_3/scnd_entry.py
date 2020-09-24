string = input()
pos_1 = string.find("f")
pos_2 = string.find("f", pos_1 + 1)
if pos_1 != -1:
    if pos_2 != -1:
        print(pos_2)
    else:
        print(-1)
else:
    print(str(-2))

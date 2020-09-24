n = int(input())
if 0 < n < 10:
    string1 = "+___"
    string2 = "|" + "1" + " /"
    string3 = "|__\\"
    string4 = "|   "
    for j in range(1, n + 1):
        print("+___", end=" ")
    print("")
    for j in range(1, n + 1):
        print("|" + str(j) + " /", end=" ")
    print("")
    for j in range(1, n + 1):
        print("|__\\", end=" ")
    print("")
    for j in range(1, n + 1):
        print("|   ", end=" ")
    print("")

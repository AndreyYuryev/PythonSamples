n1 = int(input())
n2 = int(input())
n3 = int(input())
if (n1 >= n2 >= n3) or (n1 >= n3 >= n2):
    print(n1)
elif (n2 >= n1 >= n3) or (n2 >= n3 >= n1):
    print(n2)
else:
    print(n3)

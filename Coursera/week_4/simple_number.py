def IsPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


x = int(input())
if IsPrime(x):
    print("YES")
else:
    print("NO")

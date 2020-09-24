n = int(input())
m = int(input())
k = int(input())
if (n % 2 == 0 and m % 2 == 0 and k % 2 != 0) or k >= m * n:
    print("NO")
elif (k >= m and 1 <= k // m <= n and k % m == 0):
    print("YES")
elif (k >= n and 1 <= k // n <= m and k % n == 0):
    print("YES")
else:
    print("NO")

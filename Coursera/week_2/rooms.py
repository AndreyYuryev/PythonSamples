n_first = int(input())
n_last = int(input())
if n_last >= n_first == 1:
    print("YES")
elif n_last >= n_first > 1 and ((n_first - 1) % (n_last - n_first + 1) == 0):
    print("YES")
else:
    print("NO")

minutes = int(input())
hh = (minutes // 60) % 23
mm = minutes % 60
print(hh, mm, sep=' ')

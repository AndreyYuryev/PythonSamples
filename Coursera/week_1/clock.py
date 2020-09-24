minutes_in = input()
hh = (int(minutes_in) // 60) % 24
mm = int(minutes_in) % 60
print(hh, mm, sep=" ")

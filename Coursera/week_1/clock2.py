sec_in = input()
hh = (int(sec_in) // 3600) % 24
m1 = (int(sec_in) // 60) % 60 // 10
m2 = (int(sec_in) // 60) % 60 % 10
s1 = (int(sec_in) % 60) // 10
s2 = (int(sec_in) % 60) % 10
print(hh, ":", m1, m2, ":", s1, s2, sep="")

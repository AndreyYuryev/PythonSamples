strn = input()
str_rev = strn[len(strn)::-1]
pos_f = strn.find('h')
pos_l = len(strn) - str_rev.find('h')
out = strn[:pos_f:] + strn[pos_l::]
print(out)

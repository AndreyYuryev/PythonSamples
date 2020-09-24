strn = input()
strn_rev = strn[len(strn)::-1]
pos_f = strn.find('f')
if pos_f != -1:
    if strn.find('f', pos_f + 1) != -1:
        pos_l = len(strn) - 1 - strn_rev.find('f')
        print(pos_f, pos_l, sep=" ")
    else:
        print(pos_f)
